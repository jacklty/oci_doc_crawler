Updated 2024-12-12
# Deleting Worker Nodes
_Find out about deleting worker nodes, and notes about setting cordon and drain options, with Kubernetes Engine (OKE)._
You can delete specific worker nodes in node pools in clusters that you've created with Kubernetes Engine.
Note the following considerations:
  * Deleting a worker node deletes that specific worker node from the node pool, and optionally scales down the node pool itself by subtracting 1 from the number of worker nodes specified for the node pool. If you delete a worker node without scaling down the node pool, a new worker node is created to replace it.
  * When you delete managed nodes, the **Cordon and drain** options that you select determine when and how worker nodes are terminated. See [Notes on Cordoning and Draining Managed Nodes Before Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm#contengscalingnodepools_topic-Notes_on_cordon_and_drain). 
  * As well as being able to delete specific worker nodes, note that worker nodes are also deleted when you scale down node pools and change placement configurations.
  * When you have marked a worker node for deletion (during a delete node operation, a scale down operation, or a change to placement configuration), you can't recover the node. Even if the delete node operation is initially unsuccessful, the next update node pool operation (including a scale up operation) attempts to terminate the node again.
  * Kubernetes Engine creates the worker nodes in a cluster with automatically generated names. Managed node names have the following format: `oke-c<part-of-cluster-OCID>-n<part-of-node-pool-OCID>-s<part-of-subnet-OCID>-<slot>`. Virtual node names are the same as the node's private IP address. Do not change the automatically generated names of worker nodes. If you were to change the automatically generated name of a worker node and then delete the cluster, the renamed worker node would not be deleted. You would have to delete the renamed worker node manually.
  * When deleting a worker node from a node pool, you set the **Decrease node pool size** property (`isDecrementSize` in the API) to indicate whether you want deletion of the worker node to scale down the node pool by 1. While the delete node operation is in progress, do not attempt to delete the same node and specify a different value for **Decrease node pool size** (`isDecrementSize`). If you want to delete the node and specify a different value for **Decrease node pool size** (`isDecrementSize`), wait until the first delete node operation is complete.


You can delete worker nodes using the Console, the CLI and the API. See [Deleting a Worker Node](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-worker-node.htm#top "Find out how to delete a worker node in a Kubernetes cluster that you've created using Kubernetes Engine \(OKE\).").
## Notes on Cordoning and Draining Managed Nodes Before Termination 🔗 
### Cordoning 🔗 
Cordoning is the name given to marking a worker node in a Kubernetes cluster as unschedulable. Cordoning a worker node prevents the kube-scheduler from placing new pods onto that node, but doesn't affect existing pods on the node. Cordoning a worker node is a useful preparatory step before terminating the node to perform administrative tasks (such as node deletion, scaling down a node pool, and changing placement configuration). For more information, see [Manual Node Administration](https://kubernetes.io/docs/concepts/architecture/nodes/#manual-node-administration) in the Kubernetes documentation.
### Draining 🔗 
Draining is the name given to safely evicting pods from a worker node in a Kubernetes cluster. Safely evicting pods ensures the pod's containers terminate gracefully and perform any necessary cleanup. For more information, see [Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node) and [Termination of Pods](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) in the Kubernetes documentation.
### Pod disruption budgets 🔗 
Pod disruption budgets are a Kubernetes feature to limit the number of concurrent disruptions that an application experiences. Using pod disruption budgets ensures high application availability whilst at the same time enabling you to perform administrative tasks on worker nodes. Pod disruption budgets can prevent pods being evicted when draining worker nodes. For more information, see [Specifying a Disruption Budget for your Application](https://kubernetes.io/docs/tasks/run-application/configure-pdb) in the Kubernetes documentation.
### Node pools with a "Needs attention" status 🔗 
When deleting worker nodes from clusters you've created with Kubernetes Engine, you can use the following **Cordon and drain** options to specify when and how worker nodes are terminated:
  * **Eviction grace period (mins):** The length of time to allow to cordon and drain worker nodes before terminating them. Either accept the default (60 minutes), or specify an alternative. For example, when scaling down a node pool or changing its placement configuration, you might want to allow 30 minutes to cordon worker nodes and drain them of their workloads. To terminate worker nodes immediately, without cordoning and draining them, specify 0 minutes.
  * **Force terminate after grace period:** Whether to terminate worker nodes at the end of the eviction grace period, even if they haven't been successfully cordoned and drained. By default, this option is not selected. 
Select this option if you always want worker nodes terminated at the end of the eviction grace period, even if they haven't been successfully cordoned and drained.
De-select this option if you don't want worker nodes that have not been successfully cordoned and drained to be terminated at the end of the eviction grace period. Node pools containing worker nodes that couldn't be terminated within the eviction grace period have the **Needs attention** status. See [Monitoring Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm#Monitoring_Clusters "Find out how to monitor the clusters, node pools, and nodes you've created using Kubernetes Engine \(OKE\)."). 


A node pool with the **Needs attention** status indicates that one or more of the worker nodes in the node pool failed to evict all the pods running on it within the eviction grace period. The status of the work request that initiated the termination operation is set to **Failed**. You can view the reason for the failure, including the specific pods that cannot be evicted, in the work request logs (see [Viewing Work Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#contengviewingworkrequests "Find out how to view the operations of Kubernetes Engine \(OKE\) as work requests.")). There are a number of possible reasons why a pod cannot be evicted, including restrictive pod disruption budgets. For more information, see [Scheduling, Preemption and Eviction](https://kubernetes.io/docs/concepts/scheduling-eviction/) in the Kubernetes documentation.
To resolve a node pool's **Needs attention** status and terminate affected worker nodes, do either of the following actions:
  * Re-issue the original command and select the **Force terminate after grace period** option. Nodes are terminated at the end of the eviction grace period, even if they have not been successfully cordoned and drained. 
  * Examine the work request log to determine the reason for the eviction failure, address the reason (for example, by creating a less restrictive pod disruption budget), and re-issue the original command.


#### Using the CLI to resolve a node pool's "Needs attention" status
To use the CLI to resolve a node pool's **Needs attention** status and terminate affected worker nodes, enter:
Copy
```
oci ce node-pool get --node-pool-id <nodepool-ocid> | jq '{ state: .data."lifecycle-state", nodes: (.data.nodes | .[] | {id, "node-error"} ) }'
```

where `--node-pool-id <nodepool-ocid>` is the OCID of the node pool with the **Needs attention** status.
For example:
```
oci ce node-pool get --node-pool-id ocid1.nodepool.oc1.iad.aaaaaaa______eya | jq '{ state: .data."lifecycle-state", nodes: (.data.nodes | .[] | {id, "node-error"} ) }'
```

The response to the command lists worker nodes currently in a node-error state, along with an explanation. For example:
```
{
	"state": "NEEDS_ATTENTION",
	"nodes": {
		"id": "ocid1.instance.oc1.iad.anu___4cq",
		"node-error":
		{
			"code": "PodEvictionFailureError",
			"message": "Pod(s) {sigterm - app - 55 c4f4f657 - wccqn} of Node ocid1.instance.oc1.iad.anuwc______4cq could not be evicted.",
			"opc-request-id": null,
			"status": null
		}
	}
}
```

In this example, you can see that a pod could not be evicted from the worker node within the eviction grace period. As a result, the worker node could not be terminated. It is your responsibility to identify why the pod could not be evicted, and then to fix the underlying problem. For example, by creating a less restrictive pod disruption budget.
Having fixed the problem, you can go ahead and delete the worker node by entering:
Copy
```
oci ce node-pool delete-node --node-pool-id <nodepool-ocid> --node-id <node-ocid>
```

For example:
```
oci ce node-pool delete-node --node-pool-id ocid1.nodepool.oc1.iad.aaaaaaa______eya --node-id ocid1.instance.oc1.iad.anu___4cq
```

If you want to force the deletion of the worker node without cordoning and draining the worker node, and without rectifying the underlying problem, enter:
Copy
```
oci ce node-pool delete-node --node-pool-id <nodepool-ocid> --node-id <node-ocid> --override-eviction-grace-duration PT0M
```

where `--override-eviction-grace-duration PT0M` sets the eviction grace period to 0 minutes. 
For example:
```
oci ce node-pool delete-node --node-pool-id ocid1.nodepool.oc1.iad.aaaaaaa______eya --node-id ocid1.instance.oc1.iad.anu___4cq --override-eviction-grace-duration PT0M
```

### Node pools with quantityPerSubnet set to 1 or more 🔗 
When creating and updating node pools in earlier Kubernetes Engine releases, you specified how many worker nodes you wanted in a node pool by entering a value for the **Quantity per subnet** property (`quantityPerSubnet` in the API).
In more recent Kubernetes Engine releases, you specify how many worker nodes you want in a node pool by entering a value for the **Number of Nodes** property (`size` in the API).
Note that you can only delete specific worker nodes (and select **Cordon and drain** options) when deleting from node pools that have **Quantity per subnet** (`quantityPerSubnet`) set to zero or null. To delete specific worker nodes (and select **Cordon and drain** options) from an older node pool that has **Quantity per subnet** (`quantityPerSubnet`) set to 1 or more, you must first set **Quantity per subnet** (`quantityPerSubnet`) to zero or null. Having set **Quantity per subnet** (`quantityPerSubnet`) to zero or null, you can then specify the number of worker nodes by entering a value for **Number of Nodes** (`size`) instead. From that point onwards, you can delete specific worker nodes (and select **Cordon and drain** options).
To find out the value of **Quantity per subnet** (`quantityPerSubnet`) for a node pool, enter the following command:
Copy
```
oci ce node-pool get --node-pool-id <node-pool-ocid>
```

Was this article helpful?
YesNo

