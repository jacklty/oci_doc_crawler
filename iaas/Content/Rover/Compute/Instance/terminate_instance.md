Updated 2024-09-16
# Terminating an Instance for a Roving Edge Infrastructure Device
Describes how to terminate a compute instance on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/terminate_instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/terminate_instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/terminate_instance.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance that you want to terminate. The instance's **Details** page appears.
    4. Click **More Actions** and select **Terminate**.
    5. Confirm the termination when prompted.
  * Use the [instance terminate](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/terminate.html) command and required parameters to terminate a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute instance terminate --instance-id instance_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [TerminateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/TerminateInstance) operation to terminate a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

