Updated 2024-09-16
# Powering an Instance On and Off for a Roving Edge Infrastructure Device
Describes how to power a compute instance on or off on your Roving Edge Infrastructure devices.
**Note**
The Device Console does not accurately reflect the instance's lifecycle state. It displays the instance state as **Running** when actually in a **Started** state. Use the CLI method to accurately determine the instance lifecycle state when powering on and off.
See [Stopping and Starting an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/action_vnic.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/action_vnic.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/action_vnic.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance that you want to power on or off. The instance's **Details** page appears.
    4. Click one of the following actions:
       * **Start** : Restarts a stopped instance.
       * **Stop** : Gracefully shuts down the instance by sending a shutdown command to the operating system.
**Note**
If the applications that run on the instance take a long time to shut down, they could be improperly stopped, resulting in data corruption. To avoid this occurrence, shut down the instance using the commands available in the OS before you stop the instance using the Device Console.
       * **Reboot** : Gracefully reboots the instance by sending a shutdown command to the operating system, and then powers the instance back on.
  * Use the [oci compute instance action](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/action.html) command and required parameters to power on or off a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute instance action --instance-id instance_ocid --action action [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [InstanceAction](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/InstanceAction) method to power on or off a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

