Updated 2024-08-14
# Upgrading Virtual Nodes to a Newer Kubernetes Version
_Find out how to upgrade the version of Kubernetes running on virtual nodes in an enhanced cluster created with Kubernetes Engine._
When you upgrade a cluster's Kubernetes version, Kubernetes Engine upgrades the control plane and virtual nodes in a coordinated manner. Kubernetes Engine upgrades the virtual nodes in place, ensuring highly available workloads running in the cluster are not disrupted during the upgrade.
To reduce application downtime, we recommend configuring multiple pod replicas on virtual nodes spread across availability domains and fault domains. You can further control the availability of workloads by configuring pod disruption budgets to maximize workload availability (see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb) in the Kubernetes documentation).
Each pod running on a virtual node includes a kube-proxy component, which is specific to the Kubernetes version running on the cluster's control nodes. When upgrading a virtual node, Kubernetes Engine evicts each pod before rescheduling it on the virtual node pool with the correct kube-proxy component for the version of Kubernetes running on the upgraded control plane nodes.
To upgrade virtual nodes to a newer Kubernetes version:
  1. Follow the instructions to upgrade the version of Kubernetes running on the cluster's control plane nodes (see [Upgrading the Kubernetes Version on Control Plane Nodes in a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm#top "Find out how to upgrade the version of Kubernetes running on the control plane nodes of clusters that you create using Kubernetes Engine \(OKE\).")).
The version of Kubernetes running on virtual nodes in each virtual node pool in the cluster is automatically upgraded. 
  2. (Optional) Use the [GetVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/GetVirtualNodePool) API operation to see the status of a virtual node pool upgrade as the value of the `lifecycleState` property. 
The status of the virtual node pool upgrade is returned as one of the following:
     * **Updating:** Indicates that the cluster, virtual nodes, and pods in the virtual node pool are being upgraded.
     * **Active:** Indicates that cluster, virtual nodes and all pods in the virtual node pool have been upgraded.
  3. (Optional) Use the `oci.oraclecloud.com/pod.info.kubernetes_version` pod annotation to see the version of kube-proxy currently running on each pod in the cluster. For example, by entering:
Command
CopyTry It
```
kubectl get pods --all-namespaces -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{", "}{.metadata.annotations.oci\.oraclecloud\.com\/pod\.info\.kubernetes_version}{"\n"}'
```



Was this article helpful?
YesNo

