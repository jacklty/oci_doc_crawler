Updated 2025-01-15
# Working with the Cluster Autoscaler as a Cluster Add-on
_Find out how to install, configure, and use the Kubernetes Cluster Autoscaler as a cluster add-on to automatically resize the managed node pools in a cluster you've created using Kubernetes Engine (OKE)._
Using the Kubernetes Cluster Autoscaler as a cluster add-on (the 'Cluster Autoscaler add-on') rather than as a standalone program simplifies configuration and ongoing maintenance. You can more simply:
  * Enable or disable the Cluster Autoscaler.
  * Opt into, and out of, automatic updates by Oracle.
  * Select Cluster Autoscaler add-on versions.
  * Manage add-on specific customizations using approved key/value pair configuration arguments.


These sections describe how to work with the Cluster Autoscaler add-on to manage node pools:
  * [Deploying the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on)
  * [Updating the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Updating_Cluster_Autoscaler_Add-on)
  * [Disabling (and Removing) the Cluster Autoscaler Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Disabling_Removing_Cluster_Autoscaler_Add-on)


## Deploying the Cluster Autoscaler Add-on 🔗 
The instructions below describe how to deploy the Kubernetes Cluster Autoscaler as a cluster add-on (the 'Cluster Autoscaler add-on') to manage node pools:
  * [Step 1: Setting Up an Instance Principal or Workload Identity Principal to Enable the Cluster Autoscaler Add-on to Access to Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-setup-access)
  * [Step 2: Create the Cluster Autoscaler Add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-create-CA-addon-config-file)
  * [Step 3: Deploy the Cluster Autoscaler add-on on the cluster and confirm successful deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-deploy-CA-addon)
  * [Step 4: View the Scaling Operation](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-view-scaling)
  * [Step 5: Clean Up](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-clean-up)


### Step 1: Setting Up an Instance Principal or Workload Identity Principal to Enable the Cluster Autoscaler Add-on to Access to Node Pools 🔗 
To manage node pools, the Kubernetes Cluster Autoscaler performs actions on other Oracle Cloud Infrastructure service resources. To perform those actions on OCI service resources, the Kubernetes Cluster Autoscaler uses the credentials of an authorized actor (or principal). You can currently set up the following types of principal to enable the Kubernetes Cluster Autoscaler to perform actions on OCI service resources:
  * **Instance principal:** The Kubernetes Cluster Autoscaler uses the identity of the instance on which it is running. 
  * **Workload identity principal:** The Kubernetes Cluster Autoscaler uses the identity of a workload resource running on a Kubernetes cluster.


Note the use of workload identity principals to enable the Kubernetes Cluster Autoscaler to access OCI services and resources:
  * is supported with enhanced clusters, but not with basic clusters.
  * is only supported with Cluster Autoscaler version 1.26 (or later)


#### Using instance principals to enable the Cluster Autoscaler add-on to access node pools 🔗 
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



Note that before you deploy the Cluster Autoscaler add-on, you will indicate that you want the Cluster Autoscaler add-on to access node pools using instance principals by setting the `authType` parameter to `instance` in the configuration file. See [Step 2: Create the Cluster Autoscaler Add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-create-CA-addon-config-file).
#### Using workload identity principals to enable the Cluster Autoscaler add-on to access to node pools 🔗 
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



Note that before you deploy the Cluster Autoscaler add-on, you will indicate that you want the Cluster Autoscaler add-on to access node pools using workload identity principals by setting the `authType` parameter to `workload` in the configuration file. See [Step 2: Create the Cluster Autoscaler Add-on configuration file](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-create-CA-addon-config-file).
### Step 2: Create the Cluster Autoscaler Add-on configuration file 🔗 
**Note**
These instructions describe how to create a Cluster Autoscaler add-on configuration file to enable you to deploy the Cluster Autoscaler add-on using the CLI. The configuration file contains approved key/value pair configuration arguments. You have to create a configuration file when you deploy the add-on using the CLI (or using the API). You can also use the Console to deploy the Cluster Autoscaler add-on, in which case you specify configuration arguments in the UI. For more information about deploying the Cluster Autoscaler add-on using the Console, see [Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm#install-add-on "Find out how to install a cluster add-on using Kubernetes Engine \(OKE\).").
  1. In a suitable editor, create a JSON file with a name of your choice (these instructions assume the file is called `cluster-autoscaler-add-on.json`) containing the following:
```
{
 "addonName": "ClusterAutoscaler",
 "configurations": [
  {
   "key": "nodes",
   "value": "1:5:{{ node pool ocid 1 }}"
  }
 ]
}
```

  2. In the `cluster-autoscaler-add-on.json` file you created, specify each of the cluster's node pools that you want the Kubernetes Cluster Autoscaler to manage.
You can specify multiple node pools in the `cluster-autoscaler-add-on.json` file. Note the recommendation is to always have at least one node pool that is not managed by the Kubernetes Cluster Autoscaler. Also note that it is your responsibility to manually scale any node pools you do not specify in the configuration file.
    1. In the `cluster-autoscaler-add-on.json` file, locate the following template lines:
Copy
```
   "key": "nodes",
   "value": "1:5:{{ node pool ocid 1 }}"
```

The `nodes` parameter value has the following format:
```
"value": "<min-nodes>:<max-nodes>:<nodepool-ocid>"
```

where:
       * `<min-nodes>` is the minimum number of nodes allowed in the node pool. The Kubernetes Cluster Autoscaler will not reduce the number of nodes below this number. 
       * `<max-nodes>` is the maximum number of nodes allowed in the node pool. The Kubernetes Cluster Autoscaler will not increase the number of nodes above this number. Make sure the maximum number of nodes you specify does not exceed the tenancy limits for the worker node shape defined for the node pool.
       * `<nodepool-ocid>` is one or more node pool OCIDs.
    2. Change the value of the `nodes` parameter to specify:
       * The minimum number of nodes allowed in the node pool. For example, 1.
       * The maximum number of nodes allowed in the node pool. For example, 5.
       * The OCID of the node pool you want the Kubernetes Cluster Autoscaler to manage.
For example:
Copy
```
   "key": "nodes",
   "value": "2:4:ocid1.nodepool.oc1.iad.aaaaaaaaae____ydq"
```

    3. If you want the Kubernetes Cluster Autoscaler to manage a second node pool in the cluster, append appropriate details for the second node pool to the value of the `nodes` parameter. For example:
Copy
```
   "key": "nodes",
   "value": "2:4:ocid1.nodepool.oc1.iad.aaaaaaaaae____ydq, 1:5:ocid1.nodepool.oc1.iad.aaaaaaaaah____bzr"
```

    4. If you want the Kubernetes Cluster Autoscaler to manage more node pools, append appropriate details to the value of the `nodes` parameter.
    5. Save the `cluster-autoscaler-add-on.json` file.
  3. In the `cluster-autoscaler-add-on.json` file you created, use the `authType` parameter to specify how you have set up Kubernetes Cluster Autoscaler to access OCI services and resources: 
     * If you have set up an instance principal to enable the Kubernetes Cluster Autoscaler to access OCI services and resources, set the `authType` parameter to `instance`. 
     * If you have set up a workload identity principal to enable the Kubernetes Cluster Autoscaler to access OCI services and resources, set the `authType` parameter to `workload`.
For example:
Copy
```
   "key": "authType",
   "value": "workload"
```

Note that `instance` is the default value of the `authType` parameter, so if you do not explicitly specify a value for `authType`, the Kubernetes Cluster Autoscaler uses the identity of the instance on which it is running to access OCI services and resources. For more information, see [Step 1: Setting Up an Instance Principal or Workload Identity Principal to Enable the Cluster Autoscaler Add-on to Access to Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler_topic-Working_with_Cluster_Autoscaler_as_Cluster_Add-on.htm#contengusingclusterautoscaler_topic-Deploying_Cluster_Autoscaler_Cluster_Add-on-step-setup-access).
  4. In the `cluster-autoscaler-add-on.json` file you created, specify other parameters for the Kubernetes Cluster Autoscaler. For information about the parameters you can set, see [Supported Kubernetes Cluster Autoscaler Parameters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler__CA_parameters).
For example:
```
{
 "configurations": [
  {
   "key": "nodes",
   "value": "2:4:ocid1.nodepool.oc1.iad.aaaaaaaaae____ydq, 1:5:ocid1.nodepool.oc1.iad.aaaaaaaaah____bzr"
  },
  {
   "key": "authType",
   "value": "workload"
  },
  {
   "key": "numOfReplicas",
   "value": "1"
  },
  {
   "key": "maxNodeProvisionTime",
   "value": "15m"
  },
  {
   "key": "scaleDownDelayAfterAdd",
   "value": "15m"
  },
  {
   "key": "scaleDownUnneededTime",
   "value": "10m"
  },
  {
   "key": "annotations",
   "value": "{\"prometheus.io/scrape\":\"true\",\"prometheus.io/port\":\"8086\"}"
  }
 
```

  5. Save and close the `cluster-autoscaler-add-on.json` file.


### Step 3: Deploy the Cluster Autoscaler add-on on the cluster and confirm successful deployment 🔗 
**Note**
These instructions describe how to deploy the Cluster Autoscaler add-on using the CLI and a configuration file. You can also deploy the add-on using the Console and the API. For more information, see [Installing a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/install-add-on.htm#install-add-on "Find out how to install a cluster add-on using Kubernetes Engine \(OKE\).").
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. Confirm that the Cluster Autoscaler add-on has not already been installed on the cluster by entering:```
oci ce cluster list-addons --cluster-id <cluster-ocid>
```

where `<cluster-ocid>` is the OCID of the cluster on which you want to deploy the Cluster Autoscaler add-on.
  3. Deploy the Cluster Autoscaler add-on on the cluster by entering:
```
oci ce cluster install-addon --addon-name ClusterAutoscaler --from-json file://<path-to-config-file> --cluster-id <cluster-ocid>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to deploy the Cluster Autoscaler add-on.
     * `--from-json file://<path-to-config-file>` specifies the location of the Cluster Autoscaler add-on configuration file to use when deploying the add-on. For example, `--from-json file://./cluster-autoscaler-add-on.json`
For example:
```
oci ce cluster install-addon --addon-name ClusterAutoscaler --from-json file://./cluster-autoscaler-add-on.json --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr
```

A work request is created to install the Kubernetes resources required by the Kubernetes Cluster Autoscaler on the cluster.
  4. **Optional:** View the status of the Kubernetes Cluster Autoscaler pods to observe progress of the deployment, by entering:```
kubectl get pods -n kube-system | grep cluster-autoscaler
```

  5. View the Kubernetes Cluster Autoscaler logs to confirm that the add-on was successfully deployed and is currently monitoring the workload of node pools in the cluster, by entering:```
kubectl -n kube-system logs -f deployment.apps/cluster-autoscaler
```



### Step 4: View the Scaling Operation 🔗 
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


### Step 5: Clean Up 🔗 
  1. Delete the sample Nginx application by entering:```
kubectl delete deployment nginx-deployment
```

  2. After ten minutes, confirm that the worker nodes have reduced to the original number, by entering:```
kubectl get nodes
```



Note that after deleting the sample Nginx application and waiting, you might see fewer worker nodes but still more than the original number. This is probably because kube-system pods have been scheduled to run on those nodes. kube-system pods can prevent the Kubernetes Cluster Autoscaler from removing nodes because the Autoscaler's `skip-nodes-with-system-pods` parameter is set to `true` by default.
## Updating the Cluster Autoscaler Add-on 🔗 
**Note**
These instructions describe how to update the Cluster Autoscaler add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see [Updating a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-add-on.htm#update-add-on "Find out how to update a cluster add-on using Kubernetes Engine \(OKE\).").
  1. Open the Cluster Autoscaler add-on configuration file in a suitable editor
  2. Add, remove, or change configuration parameters in the configuration file as required. For information about the parameters you can set, see [Supported Kubernetes Cluster Autoscaler Parameters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingclusterautoscaler.htm#Using_the_Kubernetes_Cluster_Autoscaler__CA_parameters).
  3. Update the Cluster Autoscaler add-on using the [oci ce cluster update-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/update-addon.html) command, by entering:
Copy
```
oci ce cluster update-addon --addon-name ClusterAutoscaler --from-json file://<path-to-config-file> --cluster-id <cluster-ocid>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to update the Cluster Autoscaler add-on.
     * `--from-json file://<path-to-config-file>` specifies the location of the Cluster Autoscaler add-on configuration file to use when updating the add-on. For example, `--from-json file://./cluster-autoscaler-add-on.json`
For example:
Copy
```
oci ce cluster update-addon --addon-name ClusterAutoscaler --from-json file://./cluster-autoscaler-add-on.json --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr
```

A work request is created to update the Kubernetes resources required by the Kubernetes Cluster Autoscaler.
  4. **Optional:** View the status of the Kubernetes Cluster Autoscaler pods to observe progress, by entering:```
kubectl get pods -n kube-system | grep cluster-autoscaler
```



## Disabling (and Removing) the Cluster Autoscaler Add-on 🔗 
**Note**
These instructions describe how to disable and remove the Cluster Autoscaler add-on using the CLI and a configuration file. You can also update the add-on using the Console and the API. For more information, see [Disabling (and Removing) a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm#disable-add-on "Find out how to disable \(and remove\) a cluster add-on using Kubernetes Engine \(OKE\).").
  1. Disable (and optionally remove) the Cluster Autoscaler add-on using the [oci ce cluster disable-addon](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/disable-addon.html) command, by entering:
Copy
```
oci ce cluster disable-addon --addon-name ClusterAutoscaler --cluster-id <cluster-ocid> --is-remove-existing-add-on <true|false>
```

where:
     * `--cluster-id <cluster-ocid>` is the OCID of the cluster in which you want to disable (and optionally remove) the Cluster Autoscaler add-on.
     * `--is-remove-existing-add-on <true|false>` specifies either to completely remove the Cluster Autoscaler add-on (when set to `true`), or to not remove the add-on but simply disable it and not use it (when set to `false`). If you disable the add-on, Oracle no longer updates it automatically when new versions become available. 
For example:
Copy
```
oci ce cluster disable-addon --addon-name ClusterAutoscaler --cluster-id ocid1.cluster.oc1.iad.aaaaaaaam______dfr --is-remove-existing-add-on true
```

A work request is created to disable (and optionally remove) the Kubernetes Cluster Autoscaler.
  2. **Optional:** View the status of the Kubernetes Cluster Autoscaler pods to observe progress, by entering:```
kubectl get pods -n kube-system | grep cluster-autoscaler
```



Was this article helpful?
YesNo

