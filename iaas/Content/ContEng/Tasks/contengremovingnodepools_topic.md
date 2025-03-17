Updated 2025-01-15
# Removing Node Pools to Scale Down Clusters
_Find out how to scale down clusters by removing node pools using Kubernetes Engine (OKE)._
You can scale down clusters by removing node pools using the Console, the CLI, and the API.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengremovingnodepools_topic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengremovingnodepools_topic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengremovingnodepools_topic.htm)


  * To scale down an existing cluster by decreasing the number of node pools in the cluster:
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster that you want to modify.
    4. Under **Resources** , click **Node Pools**.
    5. Scale down the cluster by removing node pools as follows:
      1. Select **Delete Node Pool** from the **Actions** menu beside the node pool that you want to remove.
Note that deleting a node pool permanently deletes the node pool. You can't recover a deleted node pool.
      2. Enter the name of the node pool to confirm that you want to delete it.
      3. Either accept the defaults for advanced node pool options, or select **Show Advanced Options** and specify when and how to cordon and drain worker nodes before terminating them:
         * **Eviction grace period (mins):** The length of time to allow to cordon and drain worker nodes before terminating them. Either accept the default (60 minutes) or specify an alternative. For example, when scaling down a node pool or changing its placement configuration, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To terminate worker nodes immediately, without cordoning and draining them, specify 0 minutes.
         * **Force terminate after grace period:** Whether to terminate worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option isn't selected. 
Select this option if you always want worker nodes terminated at the end of the eviction grace period, even if they haven't been successfully cordoned and drained.
De-select this option if you don't want worker nodes that haven't been successfully cordoned and drained to be terminated at the end of the eviction grace period. Node pools containing worker nodes that can't be terminated within the eviction grace period have the **Needs attention** status. The status of the work request that initiated the termination operation is set to **Failed** , and the termination operation is cancelled. For more information, see [Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm#Monitoring_Clusters "Find out how to monitor the clusters, node pools, and nodes you've created using Kubernetes Engine \(OKE\).").
For more information, see [Notes on Cordoning and Draining Managed Nodes Before Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm#contengscalingnodepools_topic-Notes_on_cordon_and_drain).
      4. Click **Delete** to delete the node pool.
  * Use the [oci ce node-pool delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/delete.html) command and required parameters to scale down a cluster by deleting a managed node pool:
Command
CopyTry It
```
oci ce node-pool delete --node-pool-id <node-pool-ocid> [OPTIONS]
```

Use the `oci ce virtual-node-pool delete` command and required parameters to scale down a cluster by deleting a virtual node pool:
Command
CopyTry It
```
oci ce virtual-node-pool delete --virtual-node-pool-id <virtual-node-pool-ocid> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/DeleteNodePool) operation to decrease the number of managed node pools in a cluster.
Run the [DeleteVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/DeleteVirtualNodePool) operation to decrease the number of virtual node pools in a cluster.


Was this article helpful?
YesNo

