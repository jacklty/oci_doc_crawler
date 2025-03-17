Updated 2025-01-15
# Changing the Display Name of a Reserved Public IP
Change the display name of a reserved public IP object in Oracle Cloud Infrastructure.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-change-display-name.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-change-display-name.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-change-display-name.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Reserved public IPs**.
    2. Under **List Scope** , select the compartment that contains the reserved public IP object in Oracle Cloud Infrastructure.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. For the reserved public IP object that you want to change, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Rename**.
    4. Enter a new display name. The name doesn't have to be unique. Avoid entering confidential information.
    5. Click **Save changes**.
  * Use the [network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html) command and required parameters to change the display name of a public IP:
Command
CopyTry It
```
oci network public-ip update --public-ip-id public_IP_OCID --display-name new_display_name ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp) operation to change the display name of a reserved public IP address.


Was this article helpful?
YesNo

