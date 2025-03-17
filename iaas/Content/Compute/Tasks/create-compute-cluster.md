Updated 2023-09-30
# Creating a Compute Cluster
When you first create a compute cluster, you create an empty RDMA network group. After the compute cluster is created, you can create instances in the compute cluster.
For steps to create instances, See [Creating an Instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service.").
For information about required IAM policies, see [Compute Clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-clusters__permissions).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-compute-cluster.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-compute-cluster.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-compute-cluster.htm)


  *     1. Open the navigation menu and click **Compute**. Under **Compute** , click **Compute Clusters**.
    2. Click **Create compute cluster**.
    3. Enter a name for the compute cluster. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
    4. Select the compartment to create the compute cluster in.
    5. Select the availability domain to run the compute cluster in. Only availability domains with hardware that supports compute clusters are listed.
    6. To assign tags to the cluster, click **Show tagging options**. 
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    7. Click **Create**.
  * Use the [compute-cluster create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/compute-cluster/create.html) command:
Command
CopyTry It
```
oci compute compute-cluster create --compartment-id <compartment_OCID> --availability-domain <availability_domain_OCID>
```

For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
  * Use the [CreateComputeCluster](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCluster/CreateComputeCluster) operation.


Was this article helpful?
YesNo

