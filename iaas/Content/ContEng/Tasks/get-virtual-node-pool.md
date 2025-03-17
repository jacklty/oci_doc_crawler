Updated 2025-01-15
# Getting a Virtual Node Pool's Details
_Find out how to get details of a specific virtual node pool using Kubernetes Engine (OKE)._
You can get details of a specific virtual node pool using the Console, the CLI, and the API.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-virtual-node-pool.htm)


  * To get details of a virtual node pool in a cluster using the Console:
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Choose a **Compartment** you have permission to work in.
    3. On the **Cluster List** page, click the name of the cluster containing the virtual node pool for which you want to see detailed information.
    4. Under **Resources** , click **Node Pools**.
Node pools in the cluster are shown in tabular form. Virtual node pools are identified as **virtual** in the **Node type** column.
    5. Click the name of the virtual node pool for which you want to see detailed information.
  * Use the [oci ce virtual-node-pool get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/virtual-node-pool/get.html) command and required parameters to get details of a virtual node pool:
Command
CopyTry It
```
oci ce virtual-node-pool get --virtual-node-pool-id <virtual-node-pool-ocid> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetVirtualNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/VirtualNodePool/GetVirtualNodePool) operation to get details of a virtual node pool.


Was this article helpful?
YesNo

