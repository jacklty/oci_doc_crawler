Updated 2025-01-15
# Listing Clusters
_Find out how to list clusters using Kubernetes Engine (OKE)._
You can list clusters using the Console, the CLI, and the API.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/list-clusters.htm)


  * To list clusters using the Console:
    1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Choose a **Compartment** you have permission to work in.
The **Cluster List** page shows the clusters in the selected compartment.
  * Use the [oci ce cluster list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/list.html) command and required parameters to list clusters:
Command
CopyTry It
```
oci ce cluster list --compartment-id <compartment-ocid> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListClusters](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/ClusterSummary/ListClusters) operation to list clusters.


Was this article helpful?
YesNo

