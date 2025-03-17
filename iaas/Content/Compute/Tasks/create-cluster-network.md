Updated 2025-02-03
# Creating a Cluster Network with Instance Pools
Create a cluster network with instance pools.
Cluster networks are built on top of the [instance pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instancemanagement.htm#Instance) feature. Most operations in the instance pool are managed directly by the cluster network, though you can resize the underlying instance pool, change the instance configuration that the pool uses to create new instances, monitor the pool, and add tags. For background information, see [Cluster Networks with Instance Pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#top).
**Tip** If you want to manage instances in the RDMA network independently of each other or use different types of instances in the network group, then use [compute clusters](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/compute-clusters.htm#compute-clusters) instead.
**Note** For information about permissions and prerequisites, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#iam) and [Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#prerequisites).
To determine whether capacity is available for a specific shape before you create a cluster network, use the [CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport) operation.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-cluster-network.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-cluster-network.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/create-cluster-network.htm)


  *     1. Open the navigation menu and click **Compute**. Under **Compute** , click **Cluster Networks**.
    2. Click **Create cluster network**.
    3. Accept the default name or enter a name for the cluster network. It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
    4. Select the compartment in which to create the cluster network.
    5. Select the availability domain in which to run the cluster network. You can select only the availability domains that have hardware that supports cluster networks.
    6. In the **Configure networking** section, specify the network that you want to use to administer the cluster network. This network is separate from the closed RDMA network between nodes within the cluster. Enter the following information:
       * **Virtual cloud network in _compartment_** : The virtual cloud network (VCN) for the cluster network.
       * **Subnet in _compartment_** : The subnet for the cluster network.
    7. In the **Configure instance pool** section, enter the following information:
       * **Instance pool name in _compartment_** : A name for the instance pool that is managed by the cluster network. Avoid entering confidential information.
       * **Number of instances** : The number of instances in the pool.
       * **Instance configuration in _compartment_** : Select the instance configuration to use when creating instances in the cluster network's instance pool, as described in the [prerequisites](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#prerequisites).
    8. (Optional) Click **Show tagging options** to add tags to the cluster network.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    9. Click **Create cluster network**.
Instances are provisioned until the required number of instances in the pool are launched, subject to the host capacity for nodes in the cluster's RDMA network.
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
  * Use the [cluster-network create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network/create.html) command and required parameters to create a cluster network.
Copy
```
oci compute-management cluster-network create [OPTIONS]
```

For a complete list of flags and variable options for cluster network CLI commands, see the [command line reference for Compute cluster networks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/cluster-network.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [CreateClusterNetwork](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/CreateClusterNetwork) operation to create a cluster network.


Was this article helpful?
YesNo

