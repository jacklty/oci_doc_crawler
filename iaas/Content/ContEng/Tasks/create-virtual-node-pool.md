Updated 2024-08-14
# Creating a Virtual Node Pool
_Find out how to create a virtual node pool using Kubernetes Engine (OKE)._
You can create virtual node pools when you create a new enhanced cluster using the Console (see [Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm#Creating_a_Kubernetes_Cluster "Find out about the two ways to create a Kubernetes cluster using Kubernetes Engine \(OKE\).") and [Creating Virtual Nodes and Virtual Node Pools in a New Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingvirtualnodes_topic.htm#top "Find out how to create virtual nodes and virtual node pools in a new cluster using Kubernetes Engine \(OKE\).")).
You can also create new virtual node pools in an existing enhanced cluster to scale up the cluster (see [Adding Node Pools to Scale Up Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingnodepools_topic.htm#contengaddingnodepools_topic "Find out how to scale up clusters by adding node pools using Kubernetes Engine \(OKE\).")).
You can create new virtual node pools using the Console, the CLI, and the API.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-virtual-node-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-virtual-node-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-virtual-node-pool.htm)


  * You can create virtual node pools using the Console:
    * When you create a new enhanced cluster using one of the Console workflows (see [Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm#Creating_a_Kubernetes_Cluster "Find out about the two ways to create a Kubernetes cluster using Kubernetes Engine \(OKE\).")).
    * When you want to scale up an existing enhanced cluster by adding additional node pools (see [Adding Node Pools to Scale Up Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingnodepools_topic.htm#contengaddingnodepools_topic "Find out how to scale up clusters by adding node pools using Kubernetes Engine \(OKE\).")).
  * Use the [oci ce virtual-node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/create.html) command and required parameters to scale up an enhanced cluster by adding a virtual node pool:
Copy
```
oci ce virtual-node-pool create \
--cluster-id <cluster-ocid> \
--compartment-id <compartment-ocid> \
--display-name <node-pool-name> \
--kubernetes-version <kubernetes-version> \
--placement-configurations "[{\"availabilityDomain\":\"<ad-name>\",\"faultDomain\":[\"FAULT-DOMAIN-<n>\"],\"subnetId\":\"<virtualnode-subnet-ocid>\"}]" \
--nsg-ids "[\"<virtual-node-nsg-ocid>\"]" \
--pod-configuration "{\"subnetId\":\"<pod-subnet-ocid>\",\"nsgIds\":[\"<pod-nsg-ocid>\"],\"shape\":\"<shape-name>\"}" \
--size <number-of-nodes>
```

where:
    * `<ad-name>` is the name of the availability domain in which to place virtual nodes. To find out the availability domain name to use, run:
Copy
```
oci iam availability-domain list
```

    * `<shape-name>` is one of `Pod.Standard.E3.Flex`, `Pod.Standard.E4.Flex`.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/CreateVirtualNodePool) operation to scale up an enhanced cluster by adding a virtual node pool.


Was this article helpful?
YesNo

