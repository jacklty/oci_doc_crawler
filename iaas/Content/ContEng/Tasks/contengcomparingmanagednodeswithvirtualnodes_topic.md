Updated 2024-10-28
# Comparing Managed Nodes with Virtual Nodes
_Find out about the differences between the managed nodes and virtual nodes you can create using Kubernetes Engine (OKE)._
When creating a node pool with Kubernetes Engine, you specify the type of worker nodes to create in the node pool as one or other of the following:
  * **Managed nodes:** Managed nodes run on compute instances (either bare metal or virtual machine) in your tenancy, and are at least partly managed by you. See [Managed Nodes and Managed Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingmanagednodeswithvirtualnodes_topic.htm#contengcomparingmanagedwithvirtualnodes_topic_managednodes).
  * **Virtual nodes:** Virtual nodes are fully managed by Oracle. See [Virtual Nodes and Virtual Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingmanagednodeswithvirtualnodes_topic.htm#contengcomparingmanagedwithvirtualnodes_topic_virtualnodes).


You can create managed nodes in both basic clusters and enhanced clusters. You can only create virtual nodes in enhanced clusters. 
All references to 'nodes' and 'worker nodes' in the Kubernetes Engine documentation refer to both virtual nodes and managed nodes, unless explicitly stated otherwise.
## Managed Nodes and Managed Node Pools 🔗 
Managed nodes run on compute instances (either bare metal or virtual machine) in your tenancy. You create managed nodes by creating a managed node pool. Managed nodes and managed node pools are managed by you. 
As you are responsible for managing managed nodes, you have the flexibility to configure them to meet your specific requirements. You are responsible for upgrading Kubernetes on managed nodes, and for managing cluster capacity.
When using managed nodes, you pay for the compute instances that execute applications.
You can create managed nodes and node pools in both basic clusters and enhanced clusters.
### Notable features supported differently by managed nodes
Some features are supported differently when using managed nodes rather than virtual nodes:
  * **Resource Allocation:** Resource allocation is at the worker node level, rather than at the pod level. Consequently, you specify CPU and memory resource requirements for the worker nodes in a node pool, rather than in the pod specification.
  * **Load Balancing:** Load balancing is between worker nodes, rather than between pods (as is the case with virtual nodes). Consequently, you cannot use pod readiness gates to route traffic to load balancer backend sets in clusters with managed nodes.
  * **Pod Networking:** Both the VCN-Native Pod Networking CNI plugin and the flannel CNI plugin are supported.
  * **Autoscaling:** Use of the Kubernetes Cluster Autoscaler and the Vertical Pod Autoscaler are supported.


### Notable features not supported, or not yet available, when using managed nodes
Some features are not yet available when using managed nodes rather than virtual nodes, including:
  * Kubernetes taints


## Virtual Nodes and Virtual Node Pools 🔗 
Virtual nodes run in the Kubernetes Engine tenancy. You create virtual nodes by creating a virtual node pool. Virtual nodes and virtual node pools are fully managed by Oracle. 
Virtual nodes provide a 'serverless' Kubernetes experience, enabling you to run containerized applications at scale without the operational overhead of upgrading the data plane infrastructure and managing the capacity of clusters.
You can only create virtual nodes and node pools in enhanced clusters.
For more information, see [Comparing Virtual Nodes with Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm#contengusingvirtualormanagednodes_topic "Find out about the differences between the virtual nodes and managed nodes you can create using Kubernetes Engine \(OKE\).").
Was this article helpful?
YesNo

