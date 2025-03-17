Updated 2024-04-23
# Attaching Instances to a Compute Cluster
After you create a compute cluster, you can create instances within the cluster. The instances must be in the same compartment and availability domain as the cluster.
For steps to create a compute cluster, see [Creating a Compute Cluster](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-compute-cluster.htm#top "When you first create a compute cluster, you create an empty RDMA network group. After the compute cluster is created, you can create instances in the compute cluster.").
When you use the API, SDKs, or CLI to create instances in a compute cluster, provide the compute cluster's OCID with the `launch instance` operation. For steps to find the OCID of a compute cluster, see [Retrieving a Compute Cluster's OCID](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/get-ocid-compute-cluster.htm#top "If you don't already have the OCID of a compute cluster, you can retrieve a list of compute clusters in a compartment with their corresponding OCIDs.").
If the placement ([Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm) and [Fault Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault)) of the compute cluster doesn't have enough capacity for the instances that you create, you might get an out of capacity error. If that occurs, create a compute cluster in a different placement, and launch instances into the new compute cluster.
To remove instances from a compute cluster, [delete (terminate) the instances](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.").
For information about required IAM policies, see [Compute Clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-clusters__permissions).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/add-instances-compute-cluster.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/add-instances-compute-cluster.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/add-instances-compute-cluster.htm)


  *     1. Open the navigation menu and click **Compute**. Under **Compute** , click **Compute Clusters**.
    2. Click the compute cluster that you're interested in.
    3. Click **Attach instance**.
    4. Follow the steps to [create an instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/launchinginstance.htm#top "Create a bare metal or virtual machine \(VM\) compute instance by using Compute service."), with the following specific choices for this instance. 
      1. In the **Placement** section, if advanced options aren't shown, click **Show advanced options**.
      2. For **Capacity type** , ensure **Compute cluster** is selected. In the **Compute cluster** list, confirm that the compute cluster that you want to create the instance in is selected.
      3. In the **Image and shape** section, click **Change shape**. Select **Bare metal machine** , and then select a [shape that supports compute clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#shapes).
    5. Click **Create**.
  * Use the [instance launch](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/launch.html) command. Include the OCID of the compute cluster in the `compute-cluster-id` parameter.
Command
CopyTry It
```
oci compute instance launch --compartment-id <compartment_OCID> --availability-domain <availability_domain> --shape <instance_shape> --subnet-id <subnet_OCID> --compute-cluster-id <compute_cluster_OCID>
```

For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
  * Use the [LaunchInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) operation, passing the OCID of the compute cluster in the `computeClusterId` parameter in [LaunchInstanceDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LaunchInstanceDetails).


Was this article helpful?
YesNo

