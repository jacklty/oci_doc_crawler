Updated 2024-09-16
# Getting a Subnet's Details for a Roving Edge Infrastructure Device
Describes how to get the details of a subnet under a VCN on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/get_subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/get_subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/get_subnet.htm)


  *     1. Open the navigation menu and select **Networking > Virtual Cloud Networks**. The **Virtual Cloud Networks** page appears. The single virtual cloud network (VCN) is listed in tabular form.
    2. Click the VCN. The VCN's **Details** page appears. 
    3. Click **Subnets**. All subnets are listed in tabular form.
    4. Click the subnet whose details you want to get. The subnet's **Details** page appears.
  * Use the [oci network subnet get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/get.html) command and required parameters to get the details of a subnet under a VCN on your Roving Edge Infrastructure devices:
Copy
```
oci network subnet get --subnet-id subnet_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetSubnet](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/GetSubnet) operation to get the details of a subnet under a VCN on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

