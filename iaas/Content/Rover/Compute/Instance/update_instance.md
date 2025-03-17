Updated 2024-09-16
# Renaming an Instance for a Roving Edge Infrastructure Device
Describes how to rename a compute instance on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/update_instance.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/update_instance.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/update_instance.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance that you want to rename. The instance's **Details** page appears.
    4. Click **More Actions** and select **Edit Name**. The **Edit Name** dialog box appears.
    5. Rename the instance.
    6. Click **Save Changes**.
  * Use the [oci compute instance update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance/update.html) command and required parameters to rename a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute instance update --instance-id instance_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [UpdateInstance](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/UpdateInstance) operation to rename a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

