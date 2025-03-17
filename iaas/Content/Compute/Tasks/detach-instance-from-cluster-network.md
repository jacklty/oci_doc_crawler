Updated 2025-02-03
# Detaching Instances from a Cluster Network with Instance Pools
Remove specific nodes from a cluster network by detaching instances from the cluster network's underlying instance pool. The instances that you detach are no longer managed as part of the cluster network.
If you want to remove instances from the cluster network by deleting instances, you can instead [resize the cluster network](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/resize-cluster-network.htm#top "Change the number of instances in a cluster network by resizing the underlying instance pool.").
When you detach an instance, you can choose whether to delete or retain the instance. You can also choose whether to replace the detached instance by creating a new instance in the cluster network. If you don't replace the detached instance, then the size of the cluster network decreases.
**Note** For information about permissions and prerequisites, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#iam) and [Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingclusternetworks.htm#prerequisites).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/detach-instance-from-cluster-network.htm)


  *     1. Open the navigation menu and click **Compute**. Under **Compute** , click **Cluster Networks**.
    2. Under **List scope** , select the compartment that contains the cluster network.
    3. Click the name of the cluster network that you want to manage.
    4. On the **Instance pools** page, click the instance pool that you want to detach instances from.
    5. Under **Resources** , click **Attached instances.**
    6. For the instance that you want to detach, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)); and then select **Detach instance**.
    7. To delete the instance and its boot volume, select the **Permanently terminate (delete) this instance and its attached boot volume** check box.
By default, the size of the underlying instance pool is reduced. If you want the cluster network to remain the same size after you detach the instance, then you can provision a replacement instance.
    8. (Optional) Select the **Replace the instance with a new instance, using the pool's instance configuration as a template for the instance** check box.
    9. Click **Detach** (or **Detach and terminate** , if you're also deleting the instance).
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
  * Use the [instance-pool-instance detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool-instance/detach.html) command and required parameters to detach an instance from the underlying instance pool of a cluster network.
Copy
```
oci compute-management instance-pool-instance detach [OPTIONS]
```

For a complete list of flags and variable options for cluster network CLI commands, see the [command line reference for compute management tasks](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To list the instances in a cluster network, use the [ListClusterNetworkInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ClusterNetwork/ListClusterNetworkInstances) operation.
To detach instances from a cluster network's underlying instance pool, use the [DetachInstancePoolInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePoolInstance/DetachInstancePoolInstance) operation.


Was this article helpful?
YesNo

