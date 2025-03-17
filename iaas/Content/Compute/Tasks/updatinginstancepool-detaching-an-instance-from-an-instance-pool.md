Updated 2025-02-03
# Detaching an Instance from an Instance Pool
Detach an instance from an instance pool when you no longer want to manage the instance as part of the pool.
When you detach an instance from a pool, you can choose whether to delete the instance or to retain it. You can also choose whether to replace the detached instance by creating an instance in the pool. If you don't replace the detached instance, then the pool size decreases.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/updatinginstancepool-detaching-an-instance-from-an-instance-pool.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
    2. In the **List scope** section, select the compartment that contains the instance pool that you want to update.
    3. Click the name of the instance pool from which you want to detach an instance to display the details page.
    4. In the **Resources** section, click **Attached instances**.
    5. For the instance that you want to detach, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and click **Detach instance** to display the Detach instance from instance pool dialog.
    6. To delete the instance and its boot volume, select **Permanently terminate (delete) this instance and its attached boot volume**.
    7. If you want the pool to remain the same size after you detach the instance, then you can provision a replacement instance. Select **Replace the instance with a new instance, using the pool's instance configuration as a template for the instance**.
    8. Click **Detach** (or **Detach and terminate** , if you're also deleting the instance).
To track the progress of the operation and [troubleshoot errors](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/instances-monitoring-work-requests.htm#work-requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") that occur during instance creation, use the associated [work request](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm#viewingwr).
  * Use the [instance-pool-instance detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool-instance/detach.html) command to detach an instance from an instance pool.
Copy
```
oci compute-management instance-pool-instance detach --instance-id <INSTANCE_OCID> --instance-pool-id <INSTANCE_POOL_OCID>
```

For a complete list of flags and variable options for the Compute Service CLI commands, see the [command line reference for Compute](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute.html).
  * For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the [DetachInstancePoolInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePoolInstance/DetachInstancePoolInstance) operation to detach an instance from an instance pool.


Was this article helpful?
YesNo

