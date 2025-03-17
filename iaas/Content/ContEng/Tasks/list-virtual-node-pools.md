Updated 2025-01-15
# Listing Virtual Node Pools
_Find out how to list virtual node pools using Kubernetes Engine (OKE)._
You can list virtual node pools using the Console, the CLI, and the API.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-node-pools.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-node-pools.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-node-pools.htm)


  * To list the virtual node pools in a cluster using the Console:
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Choose a **Compartment** you have permission to work in.
    3. On the **Cluster List** page, click the name of the cluster containing the virtual node pools you want to list.
    4. Under **Resources** , click **Node Pools**.
Node pools in the cluster are shown in tabular form. Virtual node pools are identified as **virtual** in the **Node type** column.
  * Use the [oci ce virtual-node-pool list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/list.html) command and required parameters to list virtual node pools:
Command
CopyTry It
```
oci ce virtual-node-pool list --compartment-id <compartment-ocid> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListVirtualNodePools](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePoolSummary/ListVirtualNodePools) operation to list virtual node pools.


Was this article helpful?
YesNo

