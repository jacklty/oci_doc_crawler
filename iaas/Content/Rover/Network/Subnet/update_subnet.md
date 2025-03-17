Updated 2024-09-16
# Renaming a Subnet for a Roving Edge Infrastructure Device
Describes how to rename a subnet under a VCN on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/update_subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/update_subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/update_subnet.htm)


  *     1. Open the navigation menu and select **Networking > Virtual Cloud Networks**. The **Virtual Cloud Networks** page appears. The single virtual cloud network (VCN) is listed in tabular form.
    2. Click the VCN. The VCN's **Details** page appears. 
    3. Click **Subnets**. All subnets are listed in tabular form.
    4. Click the subnet whose details you want to get. The subnet's **Details** page appears.
    5. Click **Edit**. The **Edit Subnet** dialog box appears.
    6. Enter the new **Name** of the subnet.
    7. Click **Save Changes**.
  * Use the [oci network subnet update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/update.html) command and required parameters to rename a subnet under a VCN on your Roving Edge Infrastructure devices:
Copy
```
oci network subnet update --subnet-id subnet_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [UpdateSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/UpdateSubnet) operation to rename a subnet under a VCN on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

