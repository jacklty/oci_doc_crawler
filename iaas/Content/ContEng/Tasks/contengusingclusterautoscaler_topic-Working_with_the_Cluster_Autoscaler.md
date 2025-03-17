Updated 2025-01-15
# Working with the Cluster Autoscaler as a Standalone Program
_Find out how to install, configure, and use the Kubernetes Cluster Autoscaler as a standalone program to automatically resize the managed node pools in a cluster you've created using Kubernetes Engine (OKE)._
Using the Kubernetes Cluster Autoscaler as a standalone program rather than as a cluster add-on gives you complete control and responsibility for configuration and ongoing maintenance, including:
  * Installing a version of the Kubernetes Cluster Autoscaler that is compatible with the version of Kubernetes running on the cluster.
  * Specifying configuration arguments correctly.
  * Manually upgrading the Kubernetes Cluster Autoscaler when you upgrade a cluster to a new version of Kubernetes, to ensure the Kubernetes Cluster Autoscaler is compatible with the cluster's new Kubernetes version.


The instructions below describe how to run the Kubernetes Cluster Autoscaler as a standalone program to manage node pools:
  * [Step 1: Setting Up an Instance Principal or Workload Identity Principal to Enable Cluster Autoscaler Access to Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler-setup-access)
  * [Step 2: Copy and customize the Cluster Autoscaler configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler-step-copy-CA-config-file)
  * [Step 3: Deploy the Kubernetes Cluster Autoscaler in the cluster and confirm successful deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler-step-deploy-CA)
  * [Step 4: View the Scaling Operation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler-step-view-scaling)
  * [Step 5: Clean Up](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler.htm#contengusingclusterautoscaler_topic-Working_with_the_Cluster_Autoscaler-step-clean-up)


## Step 1: Setting Up an Instance Principal or Workload Identity Principal to Enable Cluster Autoscaler Access to Node Pools 🔗 
To manage node pools, the Kubernetes Cluster Autoscaler performs actions on other Oracle Cloud Infrastructure service resources. To perform those actions on OCI service resources, the Kubernetes Cluster Autoscaler uses the credentials of an authorized actor (or principal). You can currently set up the following types of principal to enable the Kubernetes Cluster Autoscaler to perform actions on OCI service resources:
  * **Instance principal:** The Kubernetes Cluster Autoscaler uses the identity of the instance on which it is running. 
  * **Workload identity principal:** The Kubernetes Cluster Autoscaler uses the identity of a workload resource running on a Kubernetes cluster.


Note the use of workload identity principals to enable the Kubernetes Cluster Autoscaler to access OCI services and resources:
  * is supported with enhanced clusters, but not with basic clusters.
  * is only supported with Cluster Autoscaler version 1.26 (or later)


### Using instance principals to enable access to node pools 🔗 
You can set up an instance principal to enable the Kubernetes Cluster Autoscaler to perform actions on OCI service resources.
To set up an instance principal:
  1. Log in to the Console.
  2. Create a new compartment-level dynamic group containing the worker nodes (compute instances) in the cluster:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Under **Identity domain** , select **Dynamic groups**. 
    2. Select the compartment containing the cluster.
    3. Follow the instructions in [To create a dynamic group](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#To), and give the dynamic group a name (for example, `acme-oke-cluster-autoscaler-dyn-grp`).
    4. Enter a rule that includes the worker nodes in the compartment, in the format:
Copy
```
ALL {instance.compartment.id = '<compartment-ocid>'}
```

where `<compartment-ocid>` is the OCID of the compartment to which the cluster belongs.
For example:
Copy
```
ALL {instance.compartment.id = 'ocid1.compartment.oc1..aaaaaaaa23______smwa'}
```

    5. Click **Create Dynamic Group**.
  3. Create a policy to allow worker nodes to manage node pools:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
    2. Follow the instructions in [To create a policy](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy), and give the policy a name (for example, `acme-oke-cluster-autoscaler-dyn-grp-policy`).
    3. Enter a policy statement to allow worker nodes to manage node pools (along with other policy statements related to initializing worker nodes), in the format:
Copy
```
Allow dynamic-group <dynamic-group-name> to manage cluster-node-pools in compartment <compartment-name>
Allow dynamic-group <dynamic-group-name> to manage instance-family in compartment <compartment-name>
Allow dynamic-group <dynamic-group-name> to use subnets in compartment <compartment-name>
Allow dynamic-group <dynamic-group-name> to read virtual-network-family in compartment <compartment-name>
Allow dynamic-group <dynamic-group-name> to use vnics in compartment <compartment-name>
Allow dynamic-group <dynamic-group-name> to inspect compartments in compartment <compartment-name>
```

where:
       * `<dynamic-group-name>` is the name of the dynamic group you created earlier. For example, `acme-oke-cluster-autoscaler-dyn-grp`. Note that if a dynamic group is not in the default identity domain, prefix the dynamic group name with the identity domain name, in the format `dynamic-group '<identity-domain-name>'/'<dynamic-group-name>'`. You can also specify the dynamic group using its OCID, in the format `dynamic-group id <dynamic-group-ocid>`.
       * `<compartment-name>` is the name of the compartment to which the cluster belongs. For example, `acme-oke-cluster-autoscaler-compartment`
For example:
Copy
```
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to manage cluster-node-pools in compartment acme-oke-cluster-autoscaler-compartment
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to manage instance-family in compartment acme-oke-cluster-autoscaler-compartment
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to use subnets in compartment acme-oke-cluster-autoscaler-compartment
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to read virtual-network-family in compartment acme-oke-cluster-autoscaler-compartment
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to use vnics in compartment acme-oke-cluster-autoscaler-compartment
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to inspect compartments in compartment acme-oke-cluster-autoscaler-compartment
```

    4. Click **Create** to create the new policy.
**Note**
If a node pool belongs to one compartment, and the network resources used by the node pool belong to a different compartment, you have to create policies in both compartments as follows:
     * In the node pool's compartment, create a policy with policy statements in the following format:
Copy
```
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to manage cluster-node-pools in compartment <nodepool-compartment-name>
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to manage instance-family in compartment <nodepool-compartment-name>
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to use subnets in compartment <nodepool-compartment-name>
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to use vnics in compartment <nodepool-compartment-name>
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to inspect compartments in compartment <nodepool-compartment-name>
```

     * In the network resources' compartment, create a policy with policy statements in the following format:
Copy
```
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to use subnets in compartment <network-compartment-name>
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to read virtual-network-family in compartment <network-compartment-name>
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to use vnics in compartment <network-compartment-name>
Allow dynamic-group acme-oke-cluster-autoscaler-dyn-grp to inspect compartments in compartment <network-compartment-name>
```



### Using workload identity principals to enable access to node pools 🔗 
You can set up a workload identity principal to enable the Kubernetes Cluster Autoscaler to perform actions on OCI service resources. Note that you can only use workload identity principals with enhanced clusters. 
To set up a workload identity principal:
  1. Obtain the OCID of the cluster (for example, using the **Cluster Details** tab in the Console).
  2. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
  3. Follow the instructions in [Creating a Policy](https://docs.oracle.com/iaas/Content/Identity/policymgmt/managingpolicies_topic-To_create_a_policy.htm), and give the policy a name (for example, `acme-oke-cluster-autoscaler-policy`).
  4. Enter policy statements to allow node pool management, in the format:
Copy
```
Allow any-user to manage cluster-node-pools in compartment <compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to manage instance-family in compartment <compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to use subnets in compartment <compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to read virtual-network-family in compartment <compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to use vnics in compartment <compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to inspect compartments in compartment <compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'} 
```

where:
     * `<compartment-name>` is the name of the compartment to which the cluster belongs. For example, `acme-oke-cluster-autoscaler-compartment`
     * `<cluster-ocid>` is the cluster's OCID that you obtained previously.
For example:
Copy
```
Allow any-user to manage cluster-node-pools in compartment acme-oke-cluster-autoscaler-compartment where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = 'ocid1.cluster.oc1.iad.aaaaaaaa______ska'}
Allow any-user to manage instance-family in compartment acme-oke-cluster-autoscaler-compartment where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = 'ocid1.cluster.oc1.iad.aaaaaaaa______ska'}
Allow any-user to use subnets in compartment acme-oke-cluster-autoscaler-compartment where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = 'ocid1.cluster.oc1.iad.aaaaaaaa______ska'}
Allow any-user to read virtual-network-family in compartment acme-oke-cluster-autoscaler-compartment where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = 'ocid1.cluster.oc1.iad.aaaaaaaa______ska'}
Allow any-user to use vnics in compartment acme-oke-cluster-autoscaler-compartment where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = 'ocid1.cluster.oc1.iad.aaaaaaaa______ska'}
Allow any-user to inspect compartments in compartment acme-oke-cluster-autoscaler-compartment where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = 'ocid1.cluster.oc1.iad.aaaaaaaa______ska'} 
```

  5. Click **Create** to create the new policy.


**Note**
If a node pool belongs to one compartment, and the network resources used by the node pool belong to a different compartment, you have to create policies in both compartments as follows: 
  * In the node pool's compartment, create a policy with policy statements in the following format:
Copy
```
Allow any-user to manage cluster-node-pools in compartment <nodepool-compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to manage instance-family in compartment <nodepool-compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to use subnets in compartment <nodepool-compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to use vnics in compartment <nodepool-compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to inspect compartments in compartment <nodepool-compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'} 
```

  * In the network resources' compartment, create a policy with policy statements in the following format:
Copy
```
Allow any-user to use subnets in compartment <network-compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to read virtual-network-family in compartment <network-compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to use vnics in compartment <network-compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'}
Allow any-user to inspect compartments in compartment <network-compartment-name> where ALL {request.principal.type='workload', request.principal.namespace ='kube-system', request.principal.service_account = 'cluster-autoscaler', request.principal.cluster_id = '<cluster-ocid>'} 
```



## Step 2: Copy and customize the Cluster Autoscaler configuration file 🔗 
  1. In a text editor, create a file called `cluster-autoscaler.yaml` with the following content:
Copy
```
---
apiVersion: v1
kind: ServiceAccount
metadata:
 labels:
  k8s-addon: cluster-autoscaler.addons.k8s.io
  k8s-app: cluster-autoscaler
 name: cluster-autoscaler
 namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
 name: cluster-autoscaler
 labels:
  k8s-addon: cluster-autoscaler.addons.k8s.io
  k8s-app: cluster-autoscaler
rules:
 - apiGroups: [""]
  resources: ["events", "endpoints"]
  verbs: ["create", "patch"]
 - apiGroups: [""]
  resources: ["pods/eviction"]
  verbs: ["create"]
 - apiGroups: [""]
  resources: ["pods/status"]
  verbs: ["update"]
 - apiGroups: [""]
  resources: ["endpoints"]
  resourceNames: ["cluster-autoscaler"]
  verbs: ["get", "update"]
 - apiGroups: [""]
  resources: ["nodes"]
  verbs: ["watch", "list", "get", "patch", "update"]
 - apiGroups: [""]
  resources:
   - "pods"
   - "services"
   - "replicationcontrollers"
   - "persistentvolumeclaims"
   - "persistentvolumes"
  verbs: ["watch", "list", "get"]
 - apiGroups: ["extensions"]
  resources: ["replicasets", "daemonsets"]
  verbs: ["watch", "list", "get"]
 - apiGroups: ["policy"]
  resources: ["poddisruptionbudgets"]
  verbs: ["watch", "list"]
 - apiGroups: ["apps"]
  resources: ["statefulsets", "replicasets", "daemonsets"]
  verbs: ["watch", "list", "get"]
 - apiGroups: ["storage.k8s.io"]
  resources: ["storageclasses", "csinodes"]
  verbs: ["watch", "list", "get"]
 - apiGroups: ["batch", "extensions"]
  resources: ["jobs"]
  verbs: ["get", "list", "watch", "patch"]
 - apiGroups: ["coordination.k8s.io"]
  resources: ["leases"]
  verbs: ["create"]
 - apiGroups: ["coordination.k8s.io"]
  resourceNames: ["cluster-autoscaler"]
  resources: ["leases"]
  verbs: ["get", "update"]
 - apiGroups: [""]
  resources: ["namespaces"]
  verbs: ["watch", "list"]
 - apiGroups: ["storage.k8s.io"]
  resources: ["csidrivers", "csistoragecapacities"]
  verbs: ["watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
 name: cluster-autoscaler
 namespace: kube-system
 labels:
  k8s-addon: cluster-autoscaler.addons.k8s.io
  k8s-app: cluster-autoscaler
rules:
 - apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["create","list","watch"]
 - apiGroups: [""]
  resources: ["configmaps"]
  resourceNames: ["cluster-autoscaler-status", "cluster-autoscaler-priority-expander"]
  verbs: ["delete", "get", "update", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
 name: cluster-autoscaler
 labels:
  k8s-addon: cluster-autoscaler.addons.k8s.io
  k8s-app: cluster-autoscaler
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: ClusterRole
 name: cluster-autoscaler
subjects:
 - kind: ServiceAccount
  name: cluster-autoscaler
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
 name: cluster-autoscaler
 namespace: kube-system
 labels:
  k8s-addon: cluster-autoscaler.addons.k8s.io
  k8s-app: cluster-autoscaler
roleRef:
 apiGroup: rbac.authorization.k8s.io
 kind: Role
 name: cluster-autoscaler
subjects:
 - kind: ServiceAccount
  name: cluster-autoscaler
  namespace: kube-system
---
apiVersion: apps/v1
kind: Deployment
metadata:
 name: cluster-autoscaler
 namespace: kube-system
 labels:
  app: cluster-autoscaler
spec:
 replicas: 3
 selector:
  matchLabels:
   app: cluster-autoscaler
 template:
  metadata:
   labels:
    app: cluster-autoscaler
   annotations:
    prometheus.io/scrape: 'true'
    prometheus.io/port: '8085'
  spec:
   serviceAccountName: cluster-autoscaler
   containers:
    - image: iad.ocir.io/oracle/oci-cluster-autoscaler:{{ image tag }}
     name: cluster-autoscaler
     resources:
      limits:
       cpu: 100m
       memory: 300Mi
      requests:
       cpu: 100m
       memory: 300Mi
     command:
      - ./cluster-autoscaler
      - --v=4
      - --stderrthreshold=info
      - --cloud-provider=oci
      - --max-node-provision-time=25m
      - --nodes=1:5:{{ node pool ocid 1 }}
      - --nodes=1:5:{{ node pool ocid 2 }}
      - --scale-down-delay-after-add=10m
      - --scale-down-unneeded-time=10m
      - --unremovable-node-recheck-timeout=5m
      - --balance-similar-node-groups
      - --balancing-ignore-label=displayName
      - --balancing-ignore-label=hostname
      - --balancing-ignore-label=internal_addr
      - --balancing-ignore-label=oci.oraclecloud.com/fault-domain
     imagePullPolicy: "Always"
     
```

  2. In the `cluster-autoscaler.yaml` file you created, add environment variables to specify how you have set up the Kubernetes Cluster Autoscaler to access OCI services and resources:
     * If you have set up an instance principal to enable the Kubernetes Cluster Autoscaler to access OCI services and resources, after the line `imagePullPolicy: "Always"` at the end of the file, add the following:
Copy
```
     env:
     - name: OKE_USE_INSTANCE_PRINCIPAL
      value: "true"
     - name: OCI_SDK_APPEND_USER_AGENT
      value: "oci-oke-cluster-autoscaler"
```

For example:
Copy
```
...
     imagePullPolicy: "Always"
     env:
     - name: OKE_USE_INSTANCE_PRINCIPAL
      value: "true"
     - name: OCI_SDK_APPEND_USER_AGENT
      value: "oci-oke-cluster-autoscaler"
```

     * If you have set up a workload identity principal to enable the Kubernetes Cluster Autoscaler to access OCI services and resources, after the line `imagePullPolicy: "Always"` at the end of the file, add the following:
Copy
```
     env:
     - name: OKE_USE_INSTANCE_PRINCIPAL
      value: "false"
     - name: OCI_USE_WORKLOAD_IDENTITY
      value: "true"
     - name: OCI_RESOURCE_PRINCIPAL_VERSION
      value: "2.2"
     - name: OCI_RESOURCE_PRINCIPAL_REGION
      value: "<cluster-region>"
     - name: OCI_SDK_APPEND_USER_AGENT
      value: "oci-oke-cluster-autoscaler"
```

where `<cluster-region>` is the region in which the cluster is located.
For example:
Copy
```
...
     imagePullPolicy: "Always"
     env:
     - name: OKE_USE_INSTANCE_PRINCIPAL
      value: "false"
     - name: OCI_USE_WORKLOAD_IDENTITY
      value: "true"
     - name: OCI_RESOURCE_PRINCIPAL_VERSION
      value: "2.2"
     - name: OCI_RESOURCE_PRINCIPAL_REGION
      value: "us-phoenix-1"
     - name: OCI_SDK_APPEND_USER_AGENT
      value: "oci-oke-cluster-autoscaler"
```

  3. In the `cluster-autoscaler.yaml` file you created, confirm that the `--cloud-provider` parameter is set correctly for the version of Kubernetes running on the cluster. By default, the parameter assumes the cluster is running Kubernetes version 1.27 or later (or 1.23 or earlier) and is set to `oci`. If the cluster is running Kubernetes version 1.26, 1.25, or 1.24, change the value of the `--cloud-provider` parameter to `oci-oke`:
    1. In the `cluster-autoscaler.yaml` file, locate the following line:
Copy
```
- --cloud-provider=oci
```

    2. If the cluster is running Kubernetes version 1.26, 1.25, or 1.24, change the value of the `--cloud-provider` parameter to `oci-oke` :
Copy
```
- --cloud-provider=oci-oke
```

    3. Save the `cluster-autoscaler.yaml` file.
  4. In the `cluster-autoscaler.yaml` file you created, change the image path of the Kubernetes Cluster Autoscaler image to download from Oracle Cloud Infrastructure Registry. Images are available in a number of regions. For the best performance, choose the region closest to the one where the cluster is deployed:
    1. In the `cluster-autoscaler.yaml` file, locate the following template line:
Copy
```
- image: iad.ocir.io/oracle/oci-cluster-autoscaler:{{ image tag }}
```

    2. Change the image path to one of the following, according to the location and Kubernetes version of the cluster in which to run the Kubernetes Cluster Autoscaler:
Image Location | Kubernetes Version | Image Path  
---|---|---  
Germany Central (Frankfurt) | Kubernetes 1.28 | fra.ocir.io/oracle/oci-cluster-autoscaler:1.28.6-4  
Germany Central (Frankfurt) | Kubernetes 1.29 | fra.ocir.io/oracle/oci-cluster-autoscaler:1.29.4-3  
Germany Central (Frankfurt) | Kubernetes 1.30 | fra.ocir.io/oracle/oci-cluster-autoscaler:1.30.2-10  
Germany Central (Frankfurt) | Kubernetes 1.31 | fra.ocir.io/oracle/oci-cluster-autoscaler:1.31.0-1  
UK South (London) | Kubernetes 1.28 | lhr.ocir.io/oracle/oci-cluster-autoscaler:1.28.6-4  
UK South (London) | Kubernetes 1.29 | lhr.ocir.io/oracle/oci-cluster-autoscaler:1.29.4-3  
UK South (London) | Kubernetes 1.30 | lhr.ocir.io/oracle/oci-cluster-autoscaler:1.30.2-10  
UK South (London) | Kubernetes 1.31 | lhr.ocir.io/oracle/oci-cluster-autoscaler:1.31.0-1  
US East (Ashburn) | Kubernetes 1.28 | iad.ocir.io/oracle/oci-cluster-autoscaler:1.28.6-4  
US East (Ashburn) | Kubernetes 1.29 | iad.ocir.io/oracle/oci-cluster-autoscaler:1.29.4-3  
US East (Ashburn) | Kubernetes 1.30 | iad.ocir.io/oracle/oci-cluster-autoscaler:1.30.2-10  
US East (Ashburn) | Kubernetes 1.31 | iad.ocir.io/oracle/oci-cluster-autoscaler:1.31.0-1  
US West (Phoenix) | Kubernetes 1.28 | phx.ocir.io/oracle/oci-cluster-autoscaler:1.28.6-4  
US West (Phoenix) | Kubernetes 1.29 | phx.ocir.io/oracle/oci-cluster-autoscaler:1.29.4-3  
US West (Phoenix) | Kubernetes 1.30 | phx.ocir.io/oracle/oci-cluster-autoscaler:1.30.2-10  
US West (Phoenix) | Kubernetes 1.31 | phx.ocir.io/oracle/oci-cluster-autoscaler:1.31.0-1  
For example, if you want to run the Kubernetes Cluster Autoscaler in a Kubernetes 1.31 cluster located in the UK South region, specify the following image:
Copy
```
- image: lhr.ocir.io/oracle/oci-cluster-autoscaler:1.31.0-1
```

**Tip**
If you want to deploy the Kubernetes Cluster Autoscaler on a Kubernetes cluster that is not in the same region as any of the Oracle repositories containing Cluster Autoscaler images, we recommend you push the image to a repository that is in the same region as the cluster, as follows:
**i.** Pull the image from an Oracle repository using the `docker pull` command. See [Pulling Images Using the Docker CLI](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrypullingimagesusingthedockercli.htm).
**ii.** Tag the image (using the `docker tag` command), and then push the image to a repository in Oracle Cloud Infrastructure Registry that is in the same region as the cluster in which you want to run the Kubernetes Cluster Autoscaler (using the `docker push` command). See [Pushing Images Using the Docker CLI](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrypushingimagesusingthedockercli.htm).
**iii.** Specify the location of the image in the `cluster-autoscaler.yaml` file. 
**Note**
If you want to deploy the Kubernetes Cluster Autoscaler on a Kubernetes cluster where you have enabled image verification, do not simply specify an image path from one of the Oracle repositories in the `cluster-autoscaler.yaml` file. Instead, do the following:
**i.** Pull the image from an Oracle repository using the `docker pull` command. See [Pulling Images Using the Docker CLI](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrypullingimagesusingthedockercli.htm).
**ii.** Tag the image (using the `docker tag` command), and then push the image to a repository in Oracle Cloud Infrastructure Registry that is in the same region as the cluster in which you want to run the Kubernetes Cluster Autoscaler (using the `docker push` command). See [Pushing Images Using the Docker CLI](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrypushingimagesusingthedockercli.htm).
**iii.** Sign the image using a master key and key version in the Vault service, creating an image signature. See [Signing Images for Security](https://docs.oracle.com/iaas/Content/Registry/Tasks/registrysigningimages_topic.htm).
**iv.** Specify the location of the signed image in the `cluster-autoscaler.yaml` file. Reference the image using the image digest rather than the image tag (see [Enforcing the Use of Signed Images from Registry](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengenforcingsignedimagesfromocir.htm#Enforcing_Use_of_Signed_Images_from_Registry "Find out how to enforce the use of signed images from Oracle Cloud Infrastructure Registry when deploying applications to a cluster you've created using Kubernetes Engine \(OKE\).")).
    3. Save the `cluster-autoscaler.yaml` file.
  5. In the `cluster-autoscaler.yaml` file you created, specify each of the cluster's node pools that you want the Kubernetes Cluster Autoscaler to manage.
You can specify multiple node pools in the `cluster-autoscaler.yaml` file. Note the recommendation is to always have at least one node pool that is not managed by the Kubernetes Cluster Autoscaler. Also note that it is your responsibility to manually scale any node pools you do not specify in the configuration file.
    1. In the `cluster-autoscaler.yaml` file, locate the following template line:
Copy
```
- --nodes=1:5:{{ node pool ocid 1 }}
```

The `--nodes` parameter has the following format:
```
--nodes=<min-nodes>:<max-nodes>:<nodepool-ocid>
```

where:
       * `<min-nodes>` is the minimum number of nodes allowed in the node pool. The Kubernetes Cluster Autoscaler will not reduce the number of nodes below this number. 
       * `<max-nodes>` is the maximum number of nodes allowed in the node pool. The Kubernetes Cluster Autoscaler will not increase the number of nodes above this number. Make sure the maximum number of nodes you specify does not exceed the tenancy limits for the worker node shape defined for the node pool.
       * `<nodepool-ocid>` is one or more node pool OCIDs.
    2. Change the value of the `--nodes` parameter to specify:
       * The minimum number of nodes allowed in the node pool. For example, 1.
       * The maximum number of nodes allowed in the node pool. For example, 5.
       * The OCID of the node pool you want the Kubernetes Cluster Autoscaler to manage.
For example:
```
--nodes=1:5:ocid1.nodepool.oc1.iad.aaaaaaaaaeydq...
```

    3. If you only want the Kubernetes Cluster Autoscaler to manage one node pool in the cluster, locate the following line in the `cluster-autoscaler.yaml` file and remove it:
Copy
```
- --nodes=1:5:{{ node pool ocid 2 }}
```

    4. If you want the Kubernetes Cluster Autoscaler to manage a second node pool in the cluster, locate the following line in the `cluster-autoscaler.yaml` file and set appropriate values for the `--nodes` parameter:
Copy
```
- --nodes=1:5:{{ node pool ocid 2 }}
```

    5. If you want the Kubernetes Cluster Autoscaler to manage more node pools, insert additional `--nodes` parameters in the `cluster-autoscaler.yaml` file and set appropriate values for them.
    6. Save the `cluster-autoscaler.yaml` file.
  6. In the `cluster-autoscaler.yaml` file you created, confirm that the default values of the CPU and memory limit parameters are sufficient for the number of node pools that you want the Kubernetes Cluster Autoscaler to manage. The default limits are relatively low, so consider increasing the limits if you want the Kubernetes Cluster Autoscaler to manage a large number of node pools. Note that it is your responsibility to set the limits to suitable values. 
    1. In the `cluster-autoscaler.yaml` file, locate the following lines:
Copy
```
     resources:
      limits:
       cpu: 100m
       memory: 300Mi
```

    2. Set the CPU and memory limits to values that are appropriate for the number of node pools that you want the the Kubernetes Cluster Autoscaler to manage. For example:
Copy
```
     resources:
      limits:
       cpu: 200m
       memory: 600Mi
```

    3. Save the `cluster-autoscaler.yaml` file.
  7. In the `cluster-autoscaler.yaml` file you created, specify other parameters for the Kubernetes Cluster Autoscaler. For information about the parameters you can set, see [Supported Kubernetes Cluster Autoscaler Parameters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler__CA_parameters).
  8. Save and close the `cluster-autoscaler.yaml` file.


## Step 3: Deploy the Kubernetes Cluster Autoscaler in the cluster and confirm successful deployment 🔗 
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. Deploy the Kubernetes Cluster Autoscaler on the cluster by entering:```
kubectl apply -f cluster-autoscaler.yaml
```

  3. View the Kubernetes Cluster Autoscaler logs to confirm that it was successfully deployed and is currently monitoring the workload of node pools in the cluster, by entering:```
kubectl -n kube-system logs -f deployment.apps/cluster-autoscaler
```

  4. Identify which one of the three Kubernetes Cluster Autoscaler pods defined in the `cluster-autoscaler.yaml` file is currently performing actions, by entering:```
kubectl -n kube-system get lease
```

  5. Obtain a high-level view of the Kubernetes Cluster Autoscaler's state from the configmap in the kube-system namespace, by entering:```
kubectl -n kube-system get cm cluster-autoscaler-status -oyaml
```



## Step 4: View the Scaling Operation 🔗 
You can watch the Kubernetes Cluster Autoscaler you have deployed as it automatically scales worker nodes in a node pool. To make the scaling operation more obvious, consider the following suggestions (note these are for observation purposes only, and might be contrary to recommendations shown in [Recommendations when using the Kubernetes Cluster Autoscaler in Production Environments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler__CA_recommendations)):
  * Observe a cluster that has a single node pool (the node pool being managed by the Kubernetes Cluster Autoscaler).
  * If the cluster you want to observe has more than one node pool, restrict pods to running on nodes on the single node pool being managed by the Kubernetes Cluster Autoscaler. See [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/) in the Kubernetes documentation.
  * Start with one node in the node pool being managed by the Kubernetes Cluster Autoscaler.
  * In the Kubernetes Cluster Autoscaler configuration file, you specify the maximum number of nodes allowed in the node pool. Make sure the maximum number of nodes you specify does not exceed the tenancy limit for the worker node shape defined for the node pool.


To view the Kubernetes Cluster Autoscaler automatically scaling worker nodes:
  1. Confirm the current total number of worker nodes in the cluster by entering:```
kubectl get nodes
```

  2. Define a sample Nginx application by creating a file called `nginx.yaml` in a text editor, with the following content: 
Copy
```
apiVersion: apps/v1
kind: Deployment
metadata:
 name: nginx-deployment
spec:
 selector:
  matchLabels:
   app: nginx
 replicas: 2
 template:
  metadata:
   labels:
    app: nginx
  spec:
   containers:
   - name: nginx
    image: nginx:latest
    ports:
    - containerPort: 80
    resources:
     requests:
      memory: "500Mi"
```

Notice that a resource request limit has been set. 
  3. Deploy the sample application by entering:```
kubectl create -f nginx.yaml
```

  4. Increase the number of pods in the deployment to 100 (from 2) by entering:```
kubectl scale deployment nginx-deployment --replicas=100
```

The Kubernetes Cluster Autoscaler now adds worker nodes to the node pool to meet the increased workload.
  5. Observe the status of the deployment by entering:```
kubectl get deployment nginx-deployment --watch
```

  6. After a few minutes, view the increased total number of worker nodes in the cluster by entering:```
kubectl get nodes
```

Note that the number of worker nodes that you see will depend on the worker node shape and the maximum number of nodes specified in the Kubernetes Cluster Autoscaler configuration file. 


## Step 5: Clean Up 🔗 
  1. Delete the sample Nginx application by entering:```
kubectl delete deployment nginx-deployment
```

  2. After ten minutes, confirm that the worker nodes have reduced to the original number, by entering:```
kubectl get nodes
```



Note that after deleting the sample Nginx application and waiting, you might see fewer worker nodes but still more than the original number. This is probably because kube-system pods have been scheduled to run on those nodes. kube-system pods can prevent the Kubernetes Cluster Autoscaler from removing nodes because the Autoscaler's `skip-nodes-with-system-pods` parameter is set to `true` by default.
Was this article helpful?
YesNo

