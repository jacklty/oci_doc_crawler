Updated 2025-01-15
# Listing Virtual Nodes
_Find out how to list the virtual nodes in a virtual node pool using Kubernetes Engine (OKE)._
You can list the virtual nodes in a virtual node pool using the Console, the CLI, and the API.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-nodes.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-nodes.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-virtual-nodes.htm)


  * To list the virtual nodes in a virtual node pool using the Console:
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Choose a **Compartment** you have permission to work in.
    3. On the **Cluster List** page, click the name of the cluster containing the virtual nodes you want to list.
    4. Under **Resources** , click **Node Pools** and click the name of the virtual node pool containing the virtual nodes you want to list.
    5. Under **Resources** , click **Virtual Nodes**.
  * Use the [oci ce virtual-node-pool list-virtual-nodes](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/list-virtual-nodes.html) command and required parameters to list virtual nodes in a virtual node pool:
Command
CopyTry It
```
oci ce virtual-node-pool list-virtual-nodes --virtual-node-pool-id <virtual-node-pool-ocid> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListVirtualNodes](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/ListVirtualNodes) operation to list the virtual nodes in a virtual node pool.


Was this article helpful?
YesNo

