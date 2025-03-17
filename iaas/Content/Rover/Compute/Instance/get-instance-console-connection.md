Updated 2024-09-16
# Getting an Instance Console Connection's Details for a Roving Edge Infrastructure Device
Describes how to get an instance console connection's details for a Roving Edge Infrastructure device.
See [Connecting to the Console of an Instance](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/console-connection-instance.htm#top "Describes how to connect to the serial or VNC console of an instance for a Roving Edge Infrastructure device using the console connection you create.") for details on how to connect to the console of an instance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-instance-console-connection.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-instance-console-connection.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-instance-console-connection.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance containing the console connection whose details you want to get. The instance's **Details** page appears.
    4. Click **Console Connection** under **Resources**. The **Console Connection** page appears.
The **Console Connection** page displays all console connections in tabular form. The **State** column displays the state of the instance console connection for each connection entry and the **Public Key for Fingerprint** column displays the finger for each connection entry.
  * Use the [oci compute instance-console-connection get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance-console-connection/get.html) command and required parameters to get an instance console connection's details for a Roving Edge Infrastructure device:
```
oci compute instance-console-connection get --instance-console-connection-id instance_console_connection_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetInstanceConsoleConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConsoleConnection/GetInstanceConsoleConnection) operation to get an instance console connection's details for a Roving Edge Infrastructure device.


Was this article helpful?
YesNo

