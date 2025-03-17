Updated 2024-10-28
# Creating a Managed Node Pool
_Find out how to create a managed node pool using Kubernetes Engine (OKE)._
You can create managed node pools when you create a new cluster using the Console (see [Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm#Creating_a_Kubernetes_Cluster "Find out about the two ways to create a Kubernetes cluster using Kubernetes Engine \(OKE\).")).
You can also create new managed node pools in an existing cluster to scale up the cluster (see [Adding Node Pools to Scale Up Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingnodepools_topic.htm#contengaddingnodepools_topic "Find out how to scale up clusters by adding node pools using Kubernetes Engine \(OKE\).")).
You can create new managed node pools using the Console, the CLI, and the API.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-node-pool.htm)


  * You can create managed node pools using the Console:
    * When you create a new cluster using one of the Console workflows (see [Creating Kubernetes Clusters Using Console Workflows](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke.htm#Creating_a_Kubernetes_Cluster "Find out about the two ways to create a Kubernetes cluster using Kubernetes Engine \(OKE\).")).
    * When you want to scale up an existing cluster by adding additional node pools (see [Adding Node Pools to Scale Up Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingnodepools_topic.htm#contengaddingnodepools_topic "Find out how to scale up clusters by adding node pools using Kubernetes Engine \(OKE\).")).
  * Use the [oci ce node-pool create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/create.html) command and required parameters to scale up a cluster by adding a managed node pool:
Copy
```
oci ce node-pool create --cluster-id <cluster-ocid> --compartment-id <compartment-ocid> --name <node-pool-name> --node-shape <shape>
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/CreateNodePool) operation to scale up a cluster by adding a managed node pool.


Was this article helpful?
YesNo

