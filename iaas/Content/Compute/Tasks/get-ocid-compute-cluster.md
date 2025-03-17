Updated 2025-02-13
# Retrieving a Compute Cluster's OCID
If you don't already have the OCID of a compute cluster, you can retrieve a list of compute clusters in a compartment with their corresponding OCIDs.
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
The OCID is displayed on the **Compute cluster details** page.


## Using the API 🔗 
Use the [ListComputeClusters](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCluster/ListComputeClusters) operation to retrieve a list of compute clusters with their corresponding OCIDs.
## Using the CLI 🔗 
To list the compute clusters and retrieve the OCID of the compute cluster, use the [compute-cluster list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-cluster/list.html) command:
Command
CopyTry It
```
oci compute compute-cluster list --compartment-id <compartment_OCID>
```

For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
Was this article helpful?
YesNo

