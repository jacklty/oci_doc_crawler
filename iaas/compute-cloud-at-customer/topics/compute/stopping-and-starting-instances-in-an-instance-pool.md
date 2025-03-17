Updated 2024-01-18
# Stopping and Starting Instances in an Instance Pool
On Compute Cloud@Customer, performing operations such as reset or stop on the pool object performs that operation on all instances that are members of the pool. Performing these operations on an individual instance that's a member of the pool doesn't affect any other member instances.
When instances are stopped, the instances are disconnected and unassigned from their compute nodes. When instances are started, the Compute service restarts the instances in the same fault domain that they were in when they were stopped.
Instances continue to count toward the pool size while they're stopped, and configuration of stopped pool instances is preserved. Configuration changes such as fault domain changes don't apply to pool instances that are restarted or reset.
When you perform an operation on an instance pool, all the instances in the pool are stopped, started, or rebooted. See [Stopping, Starting, and Resetting an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-starting-and-resetting-an-instance.htm#stopping-starting-and-resetting-an-instance "On Compute Cloud@Customer, you can control the state of an instance using the Compute Cloud@Customer Console, CLI, and API.") for how to prepare for an instance to stop. Stopping and starting an instance can take up to five minutes.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-and-starting-instances-in-an-instance-pool.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-and-starting-instances-in-an-instance-pool.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-and-starting-instances-in-an-instance-pool.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instance Pools**.
    2. At the top of the page, select the compartment that contains the instance pool that you want to manage.
    3. For the instance pool that you want to manage, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and click either **Start** , **Stop** , or **Reboot**.
By default, clicking Stop selects Soft Stop and clicking Reboot selects Soft Reboot. To stop or reboot all instances in a pool immediately, click the **Force** option on the confirmation dialog.
    4. Confirm the action.
Under **Resources** , click **Work Request(s)** to check the status of the instance pool stop, start, or reboot. Click **Attached Instances** to view the status of the instances.
  * Use the [oci compute-management instance-pool](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute-management/instance-pool.html) commands and required parameters to manage the state of instanced in an instance pool.
Copy
```
oci compute-management instance-pool {start | stop | reset | softreset} [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use these operations to manage the state of instanced in an instance pool:
    * [StartInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/StartInstancePool)
    * [StopInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/StopInstancePool)
    * [ResetInstancePool](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstancePool/ResetInstancePool)
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

