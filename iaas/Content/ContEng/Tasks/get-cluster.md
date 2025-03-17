Updated 2025-01-15
# Getting a Cluster's Details
_Find out how to get the details of a cluster created using Kubernetes Engine (OKE)._
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-cluster.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-cluster.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/get-cluster.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster for which you want to see detailed information.
  * Use the [oci ce cluster get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/get.html) command and required parameters to get details of a cluster:
Command
CopyTry It
```
oci ce cluster get --cluster-id <cluster-ocid> [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/GetCluster) to get details of a cluster.


Was this article helpful?
YesNo

