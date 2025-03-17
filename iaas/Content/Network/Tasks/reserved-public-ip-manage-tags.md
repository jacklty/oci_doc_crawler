Updated 2025-01-15
# Managing Tags for a Reserved Public IP
Update the tag information for a reserved public IP address.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-manage-tags.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-manage-tags.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-manage-tags.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **IP management** , select **Reserved public IPs**.
    2. For the reserved public IP you want to edit, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **View tags**. 
From there you can view the existing tags, edit them, and apply new ones. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). 
  * Use the [network public-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/update.html) command and required parameters to manage tags for a public IP:
Command
CopyTry It
```
oci network public-ip update --public-ip-id public_IP_OCID --freeform-tags {"Department": "Finance"} ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdatePublicIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/UpdatePublicIp) operation to manage tags for a reserved public IP address.


Was this article helpful?
YesNo

