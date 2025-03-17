Updated 2025-01-15
# Getting a Worker Node's Details
_Find out how to get the details of a worker node in a managed node pool using Kubernetes Engine (OKE)._
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-worker-node.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-worker-node.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-worker-node.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster that contains the worker node for which you want to see detailed information.
    4. Under **Resources** , click **Node Pools** and click the name of the node pool that contains the worker node.
    5. Under **Resources** , click **Nodes**.
    6. Click the down arrow beside the worker node for which you want to see detailed information.
  * Use the [oci ce node-pool get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/node-pool/get.html) command and required parameters to get details of worker nodes in a managed node pool:
Command
CopyTry It
```
oci ce node-pool get --node-pool-id <node-pool-ocid> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetNodePool](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/NodePool/GetNodePool) operation to get the details of a worker node in a managed node pool.


Was this article helpful?
YesNo

