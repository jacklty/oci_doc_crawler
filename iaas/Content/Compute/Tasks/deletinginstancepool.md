Updated 2025-02-13
# Deleting Instance Pools
Permanently delete instance pools that you no longer need. 
**Caution** When you delete an instance pool, the resources that are associated with the pool are permanently deleted. Resources include instances created by the pool, instances that are attached to the pool, and attached boot volumes and block volumes created by the pool. Block volumes attached to instances after they were created are detached but not deleted.
If an autoscaling configuration applies to the instance pool, then the autoscaling configuration is deleted asynchronously after the pool is deleted. You can also [manually delete the autoscaling configuration](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/autoscalinginstancepools.htm#delete).
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: For a typical policy that gives access to instance pools and instance configurations, see [Let users manage Compute instance configurations, instance pools, and cluster networks](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#manage-instance-pools).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/deletinginstancepool.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. In the **List scope** section, select the compartment that contains the instance pool that you want to delete.
    3. Click the instance pool that you want to delete to display the details page.
    4. Click **More Actions** , and then click **Terminate**.
    5. Confirm when prompted.
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that might occur when deleting an instance pool, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
  * To delete an instance pool using the CLI, open a command prompt and run the [instance-pool terminate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool/terminate.html) command:
Command
CopyTry It
```
oci compute-management instance-pool terminate instance-pool-id <INSTANCE_POOL_OCID>
```

For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
In the API, use the [TerminateInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/TerminateInstancePool) operation to delete an instance pool.


Was this article helpful?
YesNo

