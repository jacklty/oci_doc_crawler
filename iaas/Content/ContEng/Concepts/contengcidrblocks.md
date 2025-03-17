Updated 2025-02-28
# IPv4 CIDR Blocks and Kubernetes Engine (OKE)
_Find out about the CIDR blocks to specify when using Kubernetes Engine (OKE)._
When configuring the VCN and subnets to use with Kubernetes Engine, you specify CIDR blocks to indicate the network addresses that can be allocated to the resources. The CIDR blocks are used for the Kubernetes API endpoint, for worker nodes, for load balancers, and (in the case of VCN-native pod networking) for pods. See [Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#Network_Resource_Configuration_for_Cluster_Creation_and_Deployment "Find out how to configure network resources to use Kubernetes Engine \(OKE\).").
## IPv4 CIDR blocks when using the flannel CNI plugin for pod networking
When creating a cluster with Kubernetes Engine and using the flannel CNI plugin for pod networking, you specify:
  * CIDR blocks for the Kubernetes services
  * CIDR blocks that can be allocated to pods running in the cluster (see [Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm#Creating_a_Kubernetes_Cluster "Find out about the two ways to create a Kubernetes cluster using Kubernetes Engine \(OKE\)."))


Note the following when using the flannel CNI plugin for pod networking:
  * You can use the flannel CNI plugin for pod networking with clusters that have managed node pools, but not with clusters that have virtual node pools.
  * The CIDR block you specify for the VCN and subnets must not overlap with the CIDR block you specify for the Kubernetes services and pods.
  * The Kubernetes API endpoint subnet only requires a small CIDR block, since the cluster only requires one IP address in this subnet. A /29 CIDR block of network addresses is usually sufficient for the Kubernetes API endpoint subnet (unless you want to use the same CIDR block for several clusters, in which case specify a larger CIDR block).
  * The CIDR blocks you specify for pods running in the cluster must not overlap with CIDR blocks you specify for the Kubernetes API endpoint, worker node, and load balancer subnets.
  * Each pod running on a worker node is assigned its own network address. Kubernetes Engine allocates a /25 CIDR block of network addresses for each worker node in a cluster, to assign to pods running on that node. A /25 CIDR block equates to 128 distinct IP addresses, of which one is reserved. So a maximum of 127 network addresses are available to assign to pods running on each worker node (more than sufficient, given that the number of pods per node is capped at 110).
  * When you create a cluster, you specify a value for the cluster's **Pods CIDR Block** property, either implicitly in the case of the 'Quick Create' workflow or explicitly in the case of the 'Custom Create' workflow. You cannot change the cluster's **Pods CIDR Block** property after the cluster has been created. The cluster's **Pods CIDR Block** property constrains the maximum total number of network addresses available for allocation to pods running on all the nodes in the cluster, and therefore effectively limits the number of nodes in the cluster. By default, the cluster's **Pods CIDR Block** property is set to a /16 CIDR block, making 65,536 network addresses available for all the nodes in the cluster. Since 128 network addresses are allocated for each node, specifying a /16 CIDR block for the cluster's **Pods CIDR Block** property limits the number of nodes in the cluster to 512. This is generally sufficient. To support more than 512 nodes in a cluster, create a cluster in the 'Custom Create' workflow and specify a larger value for the cluster's **Pods CIDR Block** property. For example:
    * To support a cluster with 2,000 nodes, specify a /14 CIDR block for the cluster's **Pods CIDR Block** property. This block contains 262,144 network addresses, which is sufficient space for 2048 /25 CIDR blocks.
    * To support a cluster with 5,000 nodes, specify a /12 CIDR block for the cluster's **Pods CIDR Block** property. This block contains 1,048,576 network addresses, which is sufficient space for 8192 /25 CIDR blocks.


## IPv4 CIDR blocks when using the OCI VCN-Native Pod Networking CNI plugin for pod networking
When creating a cluster with Kubernetes Engine and using the OCI VCN-Native Pod Networking CNI plugin for pod networking, you specify:
  * CIDR blocks for the Kubernetes services


Note the following when using the OCI VCN-Native Pod Networking CNI plugin for pod networking:
  * You can use the OCI VCN-Native Pod Networking CNI plugin for pod networking with clusters that have managed node pools, and with clusters that have virtual node pools.
  * The CIDR block you specify for the VCN and subnets must not overlap with the CIDR block you specify for the Kubernetes services.
  * The Kubernetes API endpoint subnet only requires a small CIDR block, since the cluster only requires one IP address in this subnet. A /29 CIDR block of network addresses is usually sufficient for the Kubernetes API endpoint subnet (unless you want to use the same CIDR block for several clusters, in which case specify a larger CIDR block).
  * Every worker node (instance) in a node pool has a primary virtual network interface card (VNIC), with a primary IP address. Depending on the shape you choose for the node pool, each worker node might have one or more secondary VNICs attached to it as well. The VNICs reside in the subnet selected for pod communication. Each VNIC can be associated with multiple secondary IP addresses. A pod running on a worker node can obtain a secondary IP address from a VNIC, assign the IP address to itself, and use that IP address for inbound and outbound communication. Every secondary VNIC attached to a worker node can assign up to 31 secondary IP addresses.
  * A /19 CIDR block of network addresses for the pod subnet is usually sufficient. However, a cluster with a large number of pods will require a larger CIDR block of network addresses (for example, /16).


Was this article helpful?
YesNo

