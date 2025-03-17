Updated 2025-02-13
# Getting Details About a Compute Cluster
After you create a compute cluster, you can retrieve details about the cluster.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: To allow users to do all things with compute clusters in all compartments, write the following policy:
Copy
```
Allow group ComputeClusterUsers to manage compute-clusters in tenancy
```

You must also allow users to create instances in cluster networks. For a typical policy, see [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances).
## Using the Console 🔗 
  1. Open the navigation menu and click **Compute**. Under **Compute** , click **Compute Clusters**.
  2. Click the compute cluster that you're interested in.
Information about the compute cluster is displayed on the **Compute cluster details** page.
  3. (Optional) To see a list of instances that are placed on the cluster, under **Resources** , click **Attached instances**.


## Using the API 🔗 
Use the [GetComputeCluster](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCluster/GetComputeCluster) operation.
## Using the CLI 🔗 
Use the [compute-cluster get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-cluster/get.html) command.
Command
CopyTry It
```
oci compute compute-cluster get --compute-cluster-id <compute_cluster_OCID>
```

For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
Was this article helpful?
YesNo

