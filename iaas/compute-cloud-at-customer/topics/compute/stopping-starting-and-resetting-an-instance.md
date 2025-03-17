Updated 2024-12-16
# Stopping, Starting, and Resetting an Instance
On Compute Cloud@Customer, you can control the state of an instance using the Compute Cloud@Customer Console, CLI, and API.
The following note applies to all the stop and reset actions.
**Important**
For soft stop and soft reset, any application that's running on the instance that takes more than 15 minutes to shut down could be improperly stopped, resulting in data corruption. For stop and reset, any application that's running on the instance is immediately stopped, possibly resulting in data corruption. To avoid stopping the instance while applications are running, manually shut down the instance using the commands available in the instance OS.
After the instance is shut down from the OS, then stop, soft stop, reset, or soft reset the instance.
You can perform the following actions on an instance:
  * **STOP**. Power off the instance. Compute resources are released and the instance is disconnected and unassigned from the compute node. See the important note at the beginning of this section.
Stopping an instance can take up to five minutes.
An instance that's Stopped can't be migrated to a different compute node.
  * **START**. Power on the instance. The Compute service attempts to restart the instance in the same fault domain that it was in when it was stopped, or in the specified fault domain if the fault domain was updated while the instance was stopped. If the instance start operation fails, the instance remains stopped.
If the start operation fails because of resource constraints, you could specify a different fault domain for the instance (see [Updating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/updating-an-instance.htm#updating-an-instance "On Compute Cloud@Customer, you can change instance parameters.")), change the configuration of the instance, or stop, reconfigure, or delete other instances.
If the start operation fails, and no reason is provided for the failure, the cause of the failure might be temporary. If no reason is provided for the failure, wait a short time and then retry the instance start.
Starting an instance can take up to five minutes.
  * **RESET**. Power off the instance and then power it back on. See the descriptions of STOP and START and the important note at the beginning of this section.
  * **SOFTSTOP**. Gracefully shut down the instance by sending a shutdown command to the OS. After waiting 15 minutes for the OS to shut down, the instance is powered off. If the applications that run on the instance take more than 15 minutes to shut down, they could be improperly stopped, resulting in data corruption. To avoid this, manually shut down the instance using the commands available in the OS before you softstop the instance. See the description of STOP and the important note at the beginning of this section.
  * **SOFTRESET**. Gracefully reboot the instance by sending a shutdown command to the OS. After waiting 15 minutes for the OS to shut down, the instance is powered off and then powered back on. See the important note at the beginning of this section.


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-starting-and-resetting-an-instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-starting-and-resetting-an-instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-starting-and-resetting-an-instance.htm)


  *     1. On the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") **Dashboard** , in the **Compute** block, click **Instances**.
    2. At the top of the page, select the compartment that contains the instance you want to manage.
    3. For the instance that you want to manage, click Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Start** , **Stop** , or **Reset**.
Alternatively, in the instance list, click the name of the instance to display the details page for that instance. Click the **Controls** , then click the **Start** , **Stop** , or **Reset** option.
    4. If applicable, enable force stop or force reboot options.
By default, clicking **Stop** selects Soft Stop and clicking **Reset** selects Soft Reset. To stop or reset the instance immediately, click the **Force** option on the confirmation dialog box.
       * On the **Stop the instance named <instance_name>** dialog box, enable **Force stop the instance by immediately powering off**.
       * On the**Reboot the instance named <instance_name>** dialog box, enable **Force reboot the instance by immediately powering off, then powering back on**.
    5. Click **Start Instance** , **Stop Instance** , or **Reboot Instance** on the confirmation dialog box.
On the instance details page, under **Resources** , click **Work Request(s)** to check the status of the instance stop, start, or reboot.
  * Use the [oci compute instance action](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/action.html) command and required parameters to stop, start, or reset the specified instance.
Copy
```
oci compute instance action --instance-id <instance_OCID> --action {START | STOP | RESET | SOFTSTOP | SOFTRESET} [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction) operation to stop, start, or reset the specified instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

