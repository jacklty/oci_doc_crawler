Updated 2025-02-03
# Updating the Size of an Instance Pool
You can manually update the number of instances for an instance pool.
When you increase the size of an instance pool, the pool creates instances using the pool's instance configuration as a template. To add existing instances to the pool, you can instead [attach instances to the pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-attaching-an-instance-to-an-instance-pool.htm#attach-instance "Attach an existing instance to an instance pool, and then select which instances you want to manage as a group.").
When you decrease the size of an instance pool, the pool deletes (terminates) the extra instances. Instances are terminated in this order: the number of instances is balanced across [availability domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm), and then balanced across [fault domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault). Finally, within a fault domain, the oldest instance is terminated first. If you need to perform tasks on an instance before deletion, then [detach the instance from the pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm#detach-instance "Detach an instance from an instance pool when you no longer want to manage the instance as part of the pool.") and then [delete the instance separately](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/terminatinginstance.htm#top "You can permanently delete \(terminate\) instances that you no longer need. Any attached VNICs and volumes are automatically detached when the instance terminates. Eventually, the instance's public and private IP addresses are released and become available for other instances.").
To automatically adjust the number of instances in an instance pool based on performance metrics or a schedule, [enable autoscaling](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#Autoscaling) for the instance pool.
To determine whether capacity is available for a specific shape before you resize an instance pool, use the [CreateComputeCapacityReport](https://docs.oracle.com/iaas/api/#/en/iaas/latest/ComputeCapacityReport/CreateComputeCapacityReport) operation.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-update-instance-pool-size.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-update-instance-pool-size.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool_topic-update-instance-pool-size.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. In the **List scope** section, select the compartment that contains the instance pool that you want to update.
    3. Click the name of the instance pool that you want to update to display the details page.
    4. Click **Edit**.
    5. In the **Number of instances** field, specify the updated number of instances for the instance pool, and then click **Save**.
When you update the instance pool size, the operation triggers a scaling event. Be aware of the following:
    * If the instance pool's lifecycle state is **Scaling** , then the pool creates new instances or deletes existing instances at that time, to match the updated size of the pool. To balance the instances across placements ([availability domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About) and [fault domain](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#fault)), instances are deleted first based on how many instances from the instance pool are in that availability domain and fault domain. Within a placement, the oldest instances are terminated first.
    * If the instance pool's lifecycle state is **Stopped** , then, for an increase in size, new instances are configured for the pool, but are not launched. For a decrease in size, the instances are terminated.
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
**Important** If the instance pool has been in the scaling or provisioning state for an extended period of time, then it might be because the number of instances requested has exceeded the tenancy's service limits for that shape and availability domain. Check the tenancy's [service limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#computelimits) for Compute.
  * To update the size of an instance pool, use the [instance-pool update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/update.html) command:
Copy
```
oci compute-management instance-pool update --instance-pool-id <INSTANCE_POOL_OCID> --size <NUMBER>
```

For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [UpdateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/UpdateInstancePool) operation to update the size of an instance pool.


Was this article helpful?
YesNo

