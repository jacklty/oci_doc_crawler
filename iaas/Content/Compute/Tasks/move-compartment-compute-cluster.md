Updated 2025-02-13
# Moving a Compute Cluster to a Different Compartment
After you create a compute cluster, you can move it to a different compartment.
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
  3. Click **Move resource**.
  4. Choose the destination compartment from the list.
  5. Click **Move resource**.
  6. Optionally, move the instances and other resources that are associated with the compute cluster to the new compartment.


## Using the API 🔗 
Use the [ChangeComputeClusterCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCluster/ChangeComputeClusterCompartment) operation.
## Using the CLI 🔗 
Use the [compute-cluster change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-cluster/change-compartment.html) command.
Command
CopyTry It
```
oci compute compute-cluster change-compartment --compute-cluster-id <compute_cluster_OCID> --compartment-id <compartment_OCID>
```

For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
Was this article helpful?
YesNo

