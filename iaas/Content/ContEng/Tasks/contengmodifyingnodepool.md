Updated 2024-10-28
# Modifying Node Pool and Worker Node Properties
_Find out how to modify properties of existing node pools and worker nodes you've created using Kubernetes Engine (OKE)._
You can use Kubernetes Engine to modify the properties of node pools and worker nodes in existing Kubernetes clusters.
You can change:
  * the name of a node pool
  * the version of Kubernetes to run on new worker nodes
  * the number of worker nodes in a node pool, and the availability domains, fault domains, and subnets in which to place them
  * the image to use for new worker nodes
  * the shape to use for new worker nodes
  * the boot volume size and encryption settings to use for new worker nodes
  * the cordon and drain options to use when terminating worker nodes
  * the cloud-init script to use for instances hosting worker nodes
  * the public SSH key to use to access new worker nodes


Note that you must not change the auto-generated names of resources that Kubernetes Engine has created (such as the names of worker nodes).
**Important** Any changes you make to worker node properties will only apply to new worker nodes. You cannot change the properties of existing worker nodes. If you want the changes to take effect immediately, consider creating a new node pool with the necessary settings and shift work from the original node pool to the new node pool (see [Creating Worker Nodes with Updated Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode.htm#Upgrading_the_Image_Running_on_Worker_Nodes_by_Creating_a_New_Node_Pool "Find out about the different ways to update worker node properties using Kubernetes Engine \(OKE\)."))
Also note the following:
  * In some situations, you might want to update properties of all the worker nodes in a node pool simultaneously, rather than just the properties of new worker nodes that start in the node pool. For example, to upgrade all worker nodes to a new version of Oracle Linux. In this case, you can create a new node pool with worker nodes that have the required properties, and shift work from the original node pool to the new node pool using the `kubectl drain` command and pod disruption budgets. For more information, see [Creating Worker Nodes with Updated Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode.htm#Upgrading_the_Image_Running_on_Worker_Nodes_by_Creating_a_New_Node_Pool "Find out about the different ways to update worker node properties using Kubernetes Engine \(OKE\).").
  * If you change a node pool's placement configuration (the availability domains, fault domains, and subnets in which worker nodes are placed, but not the node pool's capacity type), existing worker nodes are terminated and new worker nodes are created in the new locations.
  * If you use the [UpdateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/UpdateNodePool) API operation to modify properties of an existing node pool, be aware of the [Worker node properties out-of-sync with updated node pool properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/known-issues/conteng-known-issues.htm#contengworkernodepropertiesoutofsync) known issue and its workarounds.
  * Do not use the `kubectl delete node` command to scale down or terminate worker nodes in a cluster that was created by Kubernetes Engine. Instead, reduce the number of worker nodes by changing the corresponding node pool properties using the Console or the API. The `kubectl delete node` command does not change a node pool's properties, which determine the desired state (including the number of worker nodes). Also, although the `kubectl delete node` command removes the worker node from the cluster's etcd key-value store, the command does not delete the underlying compute instance.


You can modify the properties of node pools and worker nodes using the Console, the CLI, and the API. For more information, see:
  * [Updating a Managed Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-node-pool.htm#update-nodepool "Find out how to update a managed node pool using Kubernetes Engine \(OKE\).")
  * [Updating a Virtual Node Pool](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/update-virtual-node-pool.htm#update-virtual-nodepool "Find out how to update a virtual node pool using Kubernetes Engine \(OKE\).")


Was this article helpful?
YesNo

