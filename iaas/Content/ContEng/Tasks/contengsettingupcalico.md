Updated 2025-01-09
# Example: Installing Calico and Setting Up Network Policies
_Find out how to install Calico and set up network policies on a cluster you've created using Kubernetes Engine (OKE)._
The Kubernetes networking model assumes containers (pods) have unique and routable IP addresses within a cluster. In the Kubernetes networking model, containers communicate with each other using those IP addresses, regardless of whether the containers are deployed on the same node in a cluster or on a different node. Kubernetes has adopted the Container Network Interface (CNI) specification for network resource management. The CNI consists of a specification and libraries for writing plugins to configure network interfaces in Linux containers, along with a number of supported plugins.
By default, pods accept traffic from any source. To enhance cluster security, pods can be 'isolated' by selecting them in a network policy (the Kubernetes NetworkPolicy resource). A network policy is a specification of how groups of pods are allowed to communicate with each other and other network endpoints. NetworkPolicy resources use labels to select pods and to define rules that specify what traffic is allowed to the selected pods. If a NetworkPolicy in a cluster namespace selects a particular pod, that pod will reject any connections that are not allowed by any NetworkPolicy. Other pods in the namespace that are not selected by a NetworkPolicy will continue to accept all traffic. For more information about network policies, see [the Kubernetes documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/).
Network policies are implemented by the CNI network provider. Simply creating the NetworkPolicy resource without a CNI network provider to implement it will have no effect. Note that not all CNI network providers implement the NetworkPolicy resource.
When you create clusters with Kubernetes Engine, you select a **Network type**. The **Network type** you select determines the CNI network provider and associated CNI plugin that is used for pod networking, as follows:
  * **VCN-native pod networking:** Uses the OCI VCN-Native Pod Networking CNI plugin to connect worker nodes to pod subnets in an Oracle Cloud Infrastructure VCN. As a result, pod IP addresses within a VCN are directly routable from other VCNs connected (peered) to that VCN, and from on-premise networks. See [Using the OCI VCN-Native Pod Networking CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-OCI_CNI_plugin.htm#OCI_CNI_plugin "Find out about the OCI VCN-Native Pod Networking CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\).").
  * **Flannel overlay:** Uses the flannel CNI plugin to encapsulate communication between pods in the flannel overlay network, a simple private overlay virtual network that attaches IP addresses to containers. The pods in the private overlay network are only accessible from other pods in the same cluster. See [Using the flannel CNI plugin for pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-flannel_CNI_plugin.htm#flannel_CNI_plugin "Find out about using the flannel CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\).").


Although both the OCI VCN-Native Pod Networking CNI plugin and the flannel CNI plugin satisfy the requirements of the Kubernetes networking model, neither of them support Kubernetes NetworkPolicy resources. If you want to enhance the security of clusters you create with Kubernetes Engine by implementing network policies, you have to install and configure a network provider that does support NetworkPolicy resources in the cluster. One such provider is Calico (refer to the [Kubernetes documentation](https://kubernetes.io/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-networking-model) for a list of other network providers). 
Calico is an open source networking and network security solution for containers, virtual machines, and native host-based workloads. For more information about Calico, see the [Calico documentation](https://projectcalico.docs.tigera.io/about/about-calico).
**Note**
  * You can use Calico with managed node pools, but not with virtual node pools.
  * Only the use of open source Calico is supported. Use of Calico Enterprise is not supported.
  * In the case of flannel, if you install Calico on a cluster that has existing node pools in which pods are already running, you will have to restart the pods when the Calico installation is complete. For example, by running the `kubectl rollout restart` command. If you install Calico on a cluster before creating any node pools in the cluster (recommended), you can be sure that there will be no pods to restart.


## Calico Compatibility 🔗 
The table lists the versions of the Calico network plugin that Oracle has successfully tested on clusters created using Kubernetes Engine. Oracle only supports Calico versions that have been successfully tested. For each Calico version, the table shows the Kubernetes version that was running on clusters in successful tests.
Note that only the use of open source Calico is supported. Use of Calico Enterprise is not supported.
For more information, see [Example: Installing Calico and Setting Up Network Policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupcalico.htm#Example_Installing_Calico_and_Setting_Up_Network_Policies "Find out how to install Calico and set up network policies on a cluster you've created using Kubernetes Engine \(OKE\).").
Calico Version | Tested (and supported) on clusters running Kubernetes 1.28? | Tested (and supported) on clusters running Kubernetes 1.29? | Tested (and supported) on clusters running Kubernetes 1.30? | Tested (and supported) on clusters running Kubernetes 1.31?  
---|---|---|---|---  
3.25.1 | (not tested) | (not tested) | (not tested) | (not tested)  
3.26.1 | (not tested) | (not tested) | (not tested) | (not tested)  
3.26.4 | Yes | (not tested) | (not tested) | (not tested)  
3.27.2 | (not tested) | Yes | (not tested) | (not tested)  
3.28.0 | (not tested) | (not tested) | Yes | (not tested)  
3.28.2 | (not tested) | (not tested) | (not tested) | Yes  
## Installing Calico in place of the flannel CNI plugin 🔗 
Having created a cluster using Kubernetes Engine (using either the Console or the API) and selected **flannel overlay** as the **Network type** , you can subsequently install Calico on the cluster to support network policies. Before you install Calico in place of the flannel CNI plugin, you must first disable the flannel CNI plugin.
For convenience, Calico installation instructions are included below. Note that Calico installation instructions vary between Calico versions. For information about installing different versions of Calico, always refer to the [Calico installation documentation](https://docs.tigera.io/calico/latest/getting-started/kubernetes/).
  1. Disable the flannel CNI plugin.
How to disable the flannel CNI plugin depends on whether the cluster is an enhanced cluster or a basic cluster, as follows:
     * **Enhanced cluster:** Disable the flannel CNI plugin cluster add-on. See [Disabling (and Removing) a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/disable-add-on.htm#disable-add-on "Find out how to disable \(and remove\) a cluster add-on using Kubernetes Engine \(OKE\).").
     * **Basic cluster:** Update node pools in the cluster to add the following Kubernetes label:
Copy
```
oci.oraclecloud.com/custom-k8s-networking=true
```

See [Updating a Managed Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-node-pool.htm#update-nodepool "Find out how to update a managed node pool using Kubernetes Engine \(OKE\)."). Note that the Kubernetes label must be added to all node pools in the basic cluster (including node pools added to the cluster in future).
  2. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  3. In a terminal window, download the Calico policy-only manifest for the Kubernetes API datastore by entering:
Command
CopyTry It
```
curl https://raw.githubusercontent.com/projectcalico/calico/v3.25.1/manifests/calico-policy-only.yaml -o calico.yaml
```

Note that the url differs, according to the version of Calico that you want to install.
  4. You have to set one or more additional environment variables in the calico-policy-only.yaml file.
    1. Open the calico-policy-only.yaml file in a text editor of your choice.
    2. Add the following environment variables for the `calico-node` container in the manifest of the `calico-node` DaemonSet:
       * `CALICO_MANAGE_CNI="true"`
       * `FELIX_IPTABLESBACKEND="NFT"` **Note:** Only add this environment variable if you have selected an Oracle Linux 8 image for worker nodes in the cluster.
Before you make the change, the `calico-node` container environment variables (`env:`) section of the `calico-node` DaemonSet manifest looks like this:
```
   ...
   containers:
    # Runs calico-node container on each Kubernetes node. This
    # container programs network policy and routes on each
    # host.
    - name: calico-node
     image: docker.io/calico/node:v3.25.1
     env:
      # Use Kubernetes API as the backing datastore.
      - name: DATASTORE_TYPE
       value: "kubernetes"
      # Wait for the datastore.
      - name: WAIT_FOR_DATASTORE
       value: "true"
      # Set based on the k8s node name.
      - name: NODENAME
       valueFrom:
        fieldRef:
         fieldPath: spec.nodeName
      # Don't enable BGP.
      - name: CALICO_NETWORKING_BACKEND
       value: "none"
      - name: CLUSTER_TYPE
       value: "k8s"
      - name: FELIX_HEALTHENABLED
       value: "true"
      - name: FELIX_LOGSEVERITYSCREEN
       value: "Info"
      # Disable file logging so `kubectl logs` works.
      - name: CALICO_DISABLE_FILE_LOGGING
       value: "true"
      # Disable IPv6 on Kubernetes.
      - name: FELIX_IPV6SUPPORT
       value: "false"
```

After you have made the change, check that the `calico-node` container environment variables (`env:`) section of the `calico-node` DaemonSet manifest looks like this:
```
   ...
   containers:
    # Runs calico-node container on each Kubernetes node. This
    # container programs network policy and routes on each
    # host.
    - name: calico-node
     image: docker.io/calico/node:v3.25.1
     env:
      # Use Kubernetes API as the backing datastore.
      - name: DATASTORE_TYPE
       value: "kubernetes"
      # Wait for the datastore.
      - name: WAIT_FOR_DATASTORE
       value: "true"
      # Set based on the k8s node name.
      - name: NODENAME
       valueFrom:
        fieldRef:
         fieldPath: spec.nodeName
      # Don't enable BGP.
      - name: CALICO_NETWORKING_BACKEND
       value: "none"
      - name: CLUSTER_TYPE
       value: "k8s"
      - name: FELIX_HEALTHENABLED
       value: "true"
      - name: FELIX_LOGSEVERITYSCREEN
       value: "Info"
      # Disable file logging so `kubectl logs` works.
      - name: CALICO_DISABLE_FILE_LOGGING
       value: "true"
      # Disable IPv6 on Kubernetes.
      - name: FELIX_IPV6SUPPORT
       value: "false"
      - name: CALICO_MANAGE_CNI
       value: "true"
      - name: FELIX_IPTABLESBACKEND
       value: "NFT"
      ...
```

    3. Save and close the modified `calico-policy-only.yaml` file.
  5. Install and configure Calico by entering the following command:
Command
CopyTry It
```
kubectl apply -f calico.yaml
```



## Installing Calico alongside the OCI VCN-Native Pod Networking CNI plugin 🔗 
Having created a cluster using Kubernetes Engine (using either the Console or the API) and selected **VCN-native pod networking** as the **Network type** , you can subsequently install Calico on the cluster alongside the OCI VCN-Native Pod Networking CNI plugin to support network policies.
For convenience, Calico installation instructions are included below. Note that Calico installation instructions vary between Calico versions. For information about installing different versions of Calico, always refer to the [Calico installation documentation](https://docs.tigera.io/calico/latest/getting-started/kubernetes/).
  1. If you haven't already done so, follow the steps to set up the cluster's kubeconfig configuration file and (if necessary) set the KUBECONFIG environment variable to point to the file. Note that you must set up your own kubeconfig file. You cannot access a cluster using a kubeconfig file that a different user set up. See [Setting Up Cluster Access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.").
  2. In a terminal window, download the Calico policy-only manifest for the Kubernetes API datastore by entering:
Command
CopyTry It
```
curl https://raw.githubusercontent.com/projectcalico/calico/v3.25.1/manifests/calico-policy-only.yaml -o calico.yaml
```

Note that the url differs, according to the version of Calico that you want to install.
  3. The calico-policy-only.yaml file includes Calico components that are not required when using Calico alongside the OCI VCN-Native Pod Networking CNI plugin, so you have to remove these components. You also have to set some additional environment variables.
    1. Open the calico-policy-only.yaml file in a text editor of your choice.
    2. Remove the `initContainers` section from the manifest of the `calico-node` DaemonSet.
    3. Remove the following from the `env` section for the `calico-node` container from the manifest of the `calico-node` DaemonSet:```
     # Typha support: controlled by the ConfigMap.
     - name: FELIX_TYPHAK8SSERVICENAME
       valueFrom:
         configMapKeyRef:
           name: calico-config
           key: typha_service_name
```

    4. Remove the following `envFrom` section for the `calico-node` container from the manifest of the `calico-node` DaemonSet:```
     envFrom:
     - configMapRef:
       # Allow KUBERNETES_SERVICE_HOST and KUBERNETES_SERVICE_PORT to be overridden for eBPF mode.
       name: kubernetes-services-endpoint
       optional: true
```

    5. Remove the following volumes from the `volumes` section of the manifest of the `calico-node` DaemonSet:
       * `cni-bin-dir`
       * `cni-net-dir`
       * `cni-log-dir`
Before you make the change, the `volumes` section of the `calico-node` DaemonSet manifest looks like this:
```
   ...
   volumes:
    # Used by calico-node.
    - name: lib-modules
     hostPath:
      path: /lib/modules
    - name: var-run-calico
     hostPath:
      path: /var/run/calico
    - name: var-lib-calico
     hostPath:
      path: /var/lib/calico
    - name: xtables-lock
     hostPath:
      path: /run/xtables.lock
      type: FileOrCreate
    - name: sysfs
     hostPath:
      path: /sys/fs/
      type: DirectoryOrCreate
    # Used to install CNI.
    - name: cni-bin-dir
     hostPath:
      path: /opt/cni/bin
    - name: cni-net-dir
     hostPath:
      path: /etc/cni/net.d
    # Used to access CNI logs.
    - name: cni-log-dir
     hostPath:
      path: /var/log/calico/cni
    # Used to create per-pod Unix Domain Sockets
    - name: policysync
     hostPath:
      type: DirectoryOrCreate
      path: /var/run/nodeagent
     ...
```

After you have made the change, check that the `volumes` section of the `calico-node` DaemonSet manifest looks like this:
```
   ...
   volumes:
    # Used by calico-node.
    - name: lib-modules
     hostPath:
      path: /lib/modules
    - name: var-run-calico
     hostPath:
      path: /var/run/calico
    - name: var-lib-calico
     hostPath:
      path: /var/lib/calico
    - name: xtables-lock
     hostPath:
      path: /run/xtables.lock
      type: FileOrCreate
    - name: sysfs
     hostPath:
      path: /sys/fs/
      type: DirectoryOrCreate
    # Used to create per-pod Unix Domain Sockets
    - name: policysync
     hostPath:
      type: DirectoryOrCreate
      path: /var/run/nodeagent
     ...
```

    6. Remove the following volume mounts from the `volumeMounts` section for the `calico-node` container in the manifest of the `calico-node` DaemonSet:
       * `cni-net-dir`, including the associated comment `# For maintaining CNI plugin API credentials.`
       * `cni-log-dir`
Before you make the change, the `volumeMounts` section looks like this:
```
     ...
     volumeMounts:
      # For maintaining CNI plugin API credentials.
      - mountPath: /host/etc/cni/net.d
       name: cni-net-dir
       readOnly: false
      - mountPath: /lib/modules
       name: lib-modules
       readOnly: true
      - mountPath: /run/xtables.lock
       name: xtables-lock
       readOnly: false
      - mountPath: /var/run/calico
       name: var-run-calico
       readOnly: false
      - mountPath: /var/lib/calico
       name: var-lib-calico
       readOnly: false
      - name: policysync
       mountPath: /var/run/nodeagent
      # For eBPF mode, we need to be able to mount the BPF filesystem at /sys/fs/bpf so we mount in the
      # parent directory.
      - name: bpffs
       mountPath: /sys/fs/bpf
      - name: cni-log-dir
       mountPath: /var/log/calico/cni
       readOnly: true
       ...
```

After you have made the change, check that the `volumeMounts` section looks like this:
```
     ...
     volumeMounts:
      - mountPath: /lib/modules
       name: lib-modules
       readOnly: true
      - mountPath: /run/xtables.lock
       name: xtables-lock
       readOnly: false
      - mountPath: /var/run/calico
       name: var-run-calico
       readOnly: false
      - mountPath: /var/lib/calico
       name: var-lib-calico
       readOnly: false
      - name: policysync
       mountPath: /var/run/nodeagent
      # For eBPF mode, we need to be able to mount the BPF filesystem at /sys/fs/bpf so we mount in the
      # parent directory.
      - name: bpffs
       mountPath: /sys/fs/bpf
       ...
```

    7. Add the following environment variables for the `calico-node` container in the manifest of the `calico-node` DaemonSet:
       * `FELIX_INTERFACEPREFIX="oci"`
       * `NO_DEFAULT_POOLS="true"`
       * `FELIX_CHAININSERTMODE="Append"`
       * `FELIX_IPTABLESMANGLEALLOWACTION="Return"`
       * `FELIX_IPTABLESBACKEND="NFT"` **Note:** Only add this environment variable if you have selected an Oracle Linux 8 image for worker nodes in the cluster.
Before you make the change, the `calico-node` container environment variables (`env:`) section of the `calico-node` DaemonSet manifest looks like this:
```
   ...
   containers:
    # Runs calico-node container on each Kubernetes node. This
    # container programs network policy and routes on each
    # host.
    - name: calico-node
     image: docker.io/calico/node:v3.25.1
     env:
      # Use Kubernetes API as the backing datastore.
      - name: DATASTORE_TYPE
       value: "kubernetes"
      # Wait for the datastore.
      - name: WAIT_FOR_DATASTORE
       value: "true"
      # Set based on the k8s node name.
      - name: NODENAME
       valueFrom:
        fieldRef:
         fieldPath: spec.nodeName
      # Don't enable BGP.
      - name: CALICO_NETWORKING_BACKEND
       value: "none"
      - name: CLUSTER_TYPE
       value: "k8s"
      - name: FELIX_HEALTHENABLED
       value: "true"
      - name: FELIX_LOGSEVERITYSCREEN
       value: "Info"
      # Disable file logging so `kubectl logs` works.
      - name: CALICO_DISABLE_FILE_LOGGING
       value: "true"
      # Disable IPv6 on Kubernetes.
      - name: FELIX_IPV6SUPPORT
       value: "false"
```

After you have made the change, check that the `calico-node` container environment variables (`env:`) section of the `calico-node` DaemonSet manifest looks like this:
```
   ...
   containers:
    # Runs calico-node container on each Kubernetes node. This
    # container programs network policy and routes on each
    # host.
    - name: calico-node
     image: docker.io/calico/node:v3.25.1
     env:
      # Use Kubernetes API as the backing datastore.
      - name: DATASTORE_TYPE
       value: "kubernetes"
      # Wait for the datastore.
      - name: WAIT_FOR_DATASTORE
       value: "true"
      # Set based on the k8s node name.
      - name: NODENAME
       valueFrom:
        fieldRef:
         fieldPath: spec.nodeName
      # Don't enable BGP.
      - name: CALICO_NETWORKING_BACKEND
       value: "none"
      - name: CLUSTER_TYPE
       value: "k8s"
      - name: FELIX_HEALTHENABLED
       value: "true"
      - name: FELIX_LOGSEVERITYSCREEN
       value: "Info"
      # Disable file logging so `kubectl logs` works.
      - name: CALICO_DISABLE_FILE_LOGGING
       value: "true"
      # Disable IPv6 on Kubernetes.
      - name: FELIX_IPV6SUPPORT
       value: "false"
      # Configuration for Native Pod Networking
      - name: FELIX_INTERFACEPREFIX
       value: "oci"
      - name: NO_DEFAULT_POOLS
       value: "true"
      - name: FELIX_CHAININSERTMODE
       value: "Append"
      - name: FELIX_IPTABLESMANGLEALLOWACTION
       value: "Return"  
      - name: FELIX_IPTABLESBACKEND
       value: "NFT"     
      ...
```

    8. Save and close the modified `calico-policy-only.yaml` file.
  4. Install and configure Calico by entering the following command:
Command
CopyTry It
```
kubectl apply -f calico.yaml
```



## Setting up Network Policies 🔗 
Having installed Calico on a cluster you've created with Kubernetes Engine, you can create Kubernetes NetworkPolicy resources to isolate pods as required.
For NetworkPolicy examples and how to use them, see the Calico documentation and specifically:
  * [Kubernetes policy, demo](https://projectcalico.docs.tigera.io/security/tutorials/kubernetes-policy-demo/kubernetes-demo)
  * [Kubernetes policy, basic tutorial](https://projectcalico.docs.tigera.io/security/tutorials/kubernetes-policy-basic)
  * [Kubernetes policy, advanced tutorial](https://docs.tigera.io/calico/latest/network-policy/get-started/kubernetes-policy/kubernetes-policy-advanced)


Note that the examples vary, according to the Calico version you've installed.
Was this article helpful?
YesNo

