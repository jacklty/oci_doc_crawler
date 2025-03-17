Updated 2024-09-16
# Listing Subnets for a Roving Edge Infrastructure Device
Describes how to list the subnets under a VCN on your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/list_subnet.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/list_subnet.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/Subnet/list_subnet.htm)


  *     1. Open the navigation menu and select **Networking > Virtual Cloud Networks**. The **Virtual Cloud Networks** page appears. The single virtual cloud network (VCN) is listed in tabular form.
    2. Click the VCN. The VCN's **Details** page appears. 
    3. Click **Subnets**. All subnets are listed in tabular form.
  * Use the [oci network subnet list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/subnet/list.html) command and required parameters to list the subnets under a VCN on your Roving Edge Infrastructure devices:
Copy
```
oci network subnet list --compartment-id compartment_ocid [OPTIONS]
```

To determine your Roving Edge Infrastructure device compartment OCID, see [Compartments](https://docs.oracle.com/en-us/iaas/Content/Rover/compartments.htm#comparments "Describes how the Roving Edge Infrastructure device uses its compartment, and how to gain information on it.").
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListSubnets](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Subnet/ListSubnets) operation to list the subnets under a VCN on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

