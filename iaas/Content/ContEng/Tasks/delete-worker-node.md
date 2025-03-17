Updated 2025-01-15
# Deleting a Worker Node
_Find out how to delete a worker node in a Kubernetes cluster that you've created using Kubernetes Engine (OKE)._
For more information and notes, see [Deleting Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm#contengdeletingworkernodes "Find out about deleting worker nodes, and notes about setting cordon and drain options, with Kubernetes Engine \(OKE\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-worker-node.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-worker-node.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-worker-node.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster that contains the worker node that you want to delete.
    4. Under **Resources** , click **Node Pools** and then click the name of the node pool that contains the worker node that you want to delete.
    5. Under **Resources** , click **Nodes**.
    6. Select **Delete node** from the **Actions** menu beside the node that you want to delete.
Note that deleting a worker node permanently deletes the node. You can't recover a deleted worker node.
    7. Either accept the defaults for advanced options, or select **Show Advanced Options** and specify when and how to cordon and drain worker nodes before terminating them:
       * **Eviction grace period (mins):** The length of time to allow to cordon and drain worker nodes before terminating them. Either accept the default (60 minutes) or specify an alternative. For example, when scaling down a node pool or changing its placement configuration, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To terminate worker nodes immediately, without cordoning and draining them, specify 0 minutes.
       * **Force terminate after grace period:** Whether to terminate worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option isn't selected. 
Select this option if you always want worker nodes terminated at the end of the eviction grace period, even if they haven't been successfully cordoned and drained.
De-select this option if you don't want worker nodes that haven't been successfully cordoned and drained to be terminated at the end of the eviction grace period. Node pools containing worker nodes that can't be terminated within the eviction grace period have the **Needs attention** status. The status of the work request that initiated the termination operation is set to **Failed** , and the termination operation is cancelled. For more information, see [Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm#Monitoring_Clusters "Find out how to monitor the clusters, node pools, and nodes you've created using Kubernetes Engine \(OKE\).").
       * **Decrease node pool size:** Whether to scale down the node pool by subtracting 1 from the number of worker nodes specified for the node pool. Select this option if you want deletion of the worker node to scale down the node pool. If you don't select this option, a new worker node is started, and the node pool is not scaled down.
For more information, see [Notes on Cordoning and Draining Managed Nodes Before Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm#contengscalingnodepools_topic-Notes_on_cordon_and_drain).
    8. Click **Delete** to delete the worker node. 
Depending on the **Decrease node pool size:** option, either a new worker node is created, or the node pool is scaled down.
  * Use the [oci ce node-pool delete-node](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/delete-node.html) command and required parameters to delete a node.
To delete a worker node and scale down the node pool by one:
Command
CopyTry It
```
oci ce node-pool delete-node --node-pool-id <node-pool-ocid> --node-id <node-ocid> [OPTIONS]
```

For example: 
Command
CopyTry It
```
oci ce node-pool delete-node --node-pool-id ocid1.nodepool.oc1.iad.aaaaaaa______eya --node-id ocid1.instance.oc1.iad.anu___4cq
```

To delete a worker node without scaling down the node pool:
Command
CopyTry It
```
oci ce node-pool delete-node --node-pool-id <node-pool-ocid> --node-id <node-ocid> --is-decrement-size false [OPTIONS]
```

For example: 
Command
CopyTry It
```
oci ce node-pool delete-node --node-pool-id ocid1.nodepool.oc1.iad.aaaaaaa______eya --node-id ocid1.instance.oc1.iad.anu___4cq --is-decrement-size false
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteNode](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/DeleteNode) operation to delete a worker node.


Was this article helpful?
YesNo

