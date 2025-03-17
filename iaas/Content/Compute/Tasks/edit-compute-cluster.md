Updated 2025-02-13
# Editing the Name of a Compute Cluster
You can edit the name of a compute cluster.
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
  3. Click **Edit name**.
  4. Enter a name for the compute cluster. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
  5. Click **Save changes**.


## Using the API 🔗 
Use the [UpdateComputeCluster](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCluster/UpdateComputeCluster) operation.
## Using the CLI 🔗 
Use the [compute-cluster update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-cluster/update.html) command.
Command
CopyTry It
```
oci compute compute-cluster update --compute-cluster-id <compute_cluster_OCID> --display-name <new_name>
```

For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
Was this article helpful?
YesNo

