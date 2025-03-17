Updated 2024-09-16
# Editing a Reserved Public IP Address for a Roving Edge Infrastructure Device
Describes how to edit a reserved public IP address for your Roving Edge Infrastructure device.
You can only rename the reserved public IP address using the Device Console. Use the CLI or API method to perform other edits on the IP address.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/update-public-ip.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/update-public-ip.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Network/VCN/update-public-ip.htm)


  *     1. Open the navigation menu and select **Networking > IP Management**. The **IP Management** page appears.
    2. Click **Reserved Public IPs**. The **Reserved Public IP Addresses** page appears. The reserved public IP addresses are listed in tabular form.
    3. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libs-rover/libraries/global-images/actions-menu.png)) to the right of the IP address, and select **Rename**. The **Rename** dialog box appears.
    4. Enter the updated name the IP address and click **Save Changes**.
The reserved public IP address list reappears displaying the updated IP address name.
  * Use the [oci network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html) command and required parameters to edit a reserved public IP address for your Roving Edge Infrastructure device:
Command
CopyTry It
```
oci network public-ip update --public-ip-id public_ip_ocid [OPTIONS]
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp) operation to edit a reserved public IP address for your Roving Edge Infrastructure device.


Was this article helpful?
YesNo

