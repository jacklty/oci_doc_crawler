Updated 2025-01-15
# Getting a Virtual Node's Details
_Find out how to get the details of a virtual node in a virtual node pool using Kubernetes Engine (OKE)._
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster that contains the virtual node for which you want to see detailed information.
    4. Under **Resources** , click **Node Pools** and click the name of the virtual node pool that contains the virtual node.
    5. Under **Resources** , click **Virtual Nodes**.
    6. Click the down arrow beside the virtual node for which you want to see detailed information.
  * Use the [oci ce virtual-node-pool get-virtual-node](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/get-virtual-node.html) command and required parameters to get the details of a virtual node in a virtual node pool:
Command
CopyTry It
```
oci ce virtual-node-pool get-virtual-node --virtual-node-pool-id <virtual-node-pool-ocid> --virtual-node-id <virtual-node-ocid> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetVirtualNode](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/GetVirtualNode) operation to get the details of a virtual node in a virtual node pool.


Was this article helpful?
YesNo

