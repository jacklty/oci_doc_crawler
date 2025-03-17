Updated 2025-02-03
# Resizing a Cluster Network with Instance Pools
Change the number of instances in a cluster network by resizing the underlying instance pool.
When you increase the size, instances are provisioned until the required number of instances in the instance pool are launched, subject to host capacity for nodes in the cluster's RDMA network.
When you decrease the size, instances are terminated (deleted) in the order that they were created, first-in, first-out. If you want to remove a specific instance from the cluster network, you can instead [detach the instance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm#detach-instance "Remove specific nodes from a cluster network by detaching instances from the cluster network's underlying instance pool. The instances that you detach are no longer managed as part of the cluster network.") from the cluster network.
To determine whether capacity is available for a specific shape before you resize a cluster network, use the [CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport) operation.
**Note** For information about permissions and prerequisites, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#iam) and [Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#prerequisites).
**Note** The cluster network must be in the **Running** state to be resized.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm)


  *     1. Open the navigation menu and click **Compute**. Under **Compute** , click **Cluster Networks**.
    2. In the **List scope** section, select the compartment that contains the cluster network.
    3. Click the name of the cluster network that you want to resize.
    4. Click **Edit**.
    5. In the **Number of instances** box, specify the updated number of instances for the instance pool.
    6. Click **Save changes**.
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
  * To resize a cluster network, you can use the [instance-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html) command to resize the underlying instance pool to increase or decrease the size of the instance pool.
Copy
```
oci compute-management instance-pool update --instance-pool-id <INSTANCE_POOL_OCID> --size <NUMBER>
```

```
oci compute-management instance-pool-instance attach [OPTIONS]
```

Copy
```
oci compute-management instance-pool-instance detach [OPTIONS]
```

For a complete list of flags and variable options for cluster network CLI commands, see the [command line reference for compute management tasks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [UpdateClusterNetwork](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/UpdateClusterNetwork) operation to resize a cluster network with instance pools.


Was this article helpful?
YesNo

