Updated 2024-09-16
# Deleting an Instance Console Connection from a Roving Edge Infrastructure Device
Describes how to delete an instance console connection from a Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/delete-instance-console-connection.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/delete-instance-console-connection.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/delete-instance-console-connection.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance containing the console connection you want to delete. The instance's **Details** page appears.
    4. Click **Console Connection** under **Resources**. The **Console Connection** page appears.
    5. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) to the right of the console connection entry you want to delete, then click **Delete Console Connection**. The **Delete Console Connection** dialog box appears.
    6. Confirm the deletion.
The **Console Connection** page reappears with the connection you deleted listed as **Deleted**.
  * Use the [oci compute instance-console-connection delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance-console-connection/delete.html) command and required parameters to delete an instance console connection from a Roving Edge Infrastructure device:
```
oci compute instance-console-connection delete --instance-console-connection-id instance_console_connection_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [DeleteInstanceConsoleConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConsoleConnection/DeleteInstanceConsoleConnection) operation to delete an instance console connection from a Roving Edge Infrastructure device.


Was this article helpful?
YesNo

