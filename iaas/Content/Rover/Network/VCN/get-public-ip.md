Updated 2024-09-16
# Getting a Reserved Public IP Address' Details for a Roving Edge Infrastructure Device
Describes how to get the details of a reserved public IP address for your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/get-public-ip.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/get-public-ip.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/get-public-ip.htm)


  *     1. Open the navigation menu and select **Networking > IP Management**. The **IP Management** page appears.
    2. Click **Reserved Public IPs**. The **Reserved Public IP Addresses** page appears. The reserved public IP addresses are listed in tabular form.
The reserved public IP addresses list contains the details on each address, including the state, IP address, VNIC, and IP pool.
  * Use the [oci network public-ip get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/get.html) command and required parameters to get the details of a reserved public IP address for your Roving Edge Infrastructure device:
Command
CopyTry It
```
oci network public-ip get [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [GetPublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/GetPublicIp) operation to get the details of a reserved public IP address for your Roving Edge Infrastructure device.


Was this article helpful?
YesNo

