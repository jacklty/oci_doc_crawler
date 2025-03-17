Updated 2025-01-15
# Deleting a Kubernetes Cluster
_Find out how to delete an existing Kubernetes cluster that you've created using Kubernetes Engine (OKE)._
For more information and notes, see [Deleting Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingcluster.htm#contengdeletingcluster "Find out about deleting Kubernetes clusters, and notes about cluster deletion, with Kubernetes Engine \(OKE\).").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-cluster.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-cluster.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/delete-cluster.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
    2. Select the compartment that contains the cluster.
    3. On the **Clusters** page, click the name of the cluster that you want to delete.
    4. On the **Cluster details** page, click the **Delete** button, and then confirm that you want to delete the cluster.
  * Use the [oci ce cluster delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/cluster/delete.html) command and required parameters to delete a cluster:
Command
CopyTry It
```
oci ce cluster delete --cluster-id <cluster-ocid>
```

For example: 
Command
CopyTry It
```
oci ce cluster delete --cluster-id ocid1.cluster.oc1.iad.aaaaaaaaaf______jrd
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteCluster](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/Cluster/DeleteCluster) operation to delete a cluster.


Was this article helpful?
YesNo

