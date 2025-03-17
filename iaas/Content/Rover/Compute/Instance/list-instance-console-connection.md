Updated 2024-09-16
# Listing the Instance Console Connections for a Roving Edge Infrastructure Device
Describes how to list the instance console connections for a Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-instance-console-connection.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-instance-console-connection.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-instance-console-connection.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance for which you want to list the console connections. The instance's **Details** page appears.
    4. Click **Console Connection** under **Resources**. The **Console Connection** page appears.
All console connections are listed in tabular form.
  * Use the [oci compute instance-console-connection list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/instance-console-connection/list.html) command and required parameters to list the instance console connections for a Roving Edge Infrastructure device:
```
oci compute instance-console-connection list --compartment-id compartment_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListInstanceConsoleConnections](https://docs.oracle.com/iaas/api/#/en/iaas/latest/InstanceConsoleConnection/ListInstanceConsoleConnections) operation to list the instance console connections for a Roving Edge Infrastructure device.


Was this article helpful?
YesNo

