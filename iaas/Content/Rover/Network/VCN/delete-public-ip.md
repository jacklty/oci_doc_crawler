Updated 2024-09-16
# Delete a Reserved Public IP Address for a Roving Edge Infrastructure Device
Describes how to delete a reserved public IP address from your Roving Edge Infrastructure device.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete-public-ip.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete-public-ip.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/delete-public-ip.htm)


  *     1. Open the navigation menu and select **Networking > IP Management**. The **IP Management** page appears.
    2. Click **Reserved Public IPs**. The **Reserved Public IP Addresses** page appears. The reserved public IP addresses are listed in tabular form.
    3. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) to the right of the IP address, and select **Terminate**.
    4. Confirm the termination when prompted.
The reserved public IP address list reappears without the IP address you terminated.
  * Use the [oci network public-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/delete.html) command and required parameters to delete a reserved public IP address from your Roving Edge Infrastructure device:
Command
CopyTry It
```
oci network public-ip delete --public-ip-id public_ip_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [DeletePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/DeletePublicIp) operation to delete a reserved public IP address from your Roving Edge Infrastructure device.


Was this article helpful?
YesNo

