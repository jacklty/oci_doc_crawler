Updated 2025-02-06
# Editing Private IP Address Information
Update information for a private IP address such as hostname or associated IP type.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-update.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Select the name of the instance to open its details page.
    3. Under **Resources** , select **Attached VNICs**.
    4. Select the VNIC that you're interested in.
    5. Under **Resources** , select **IPv4 Addresses**.
The VNIC's associated IP addresses are listed in tabular form.
    6. Find the IP address you want to update, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Edit**.
    7. Update the hostname or public IP type.
    8. Select **Update**.
  * Use the [private-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/update.html) command and required parameters to update information for the private IP address:
Command
CopyTry It
```
oci network private-ip update --private-ip-id IP_address_OCID
--hostname-label new_hostname_label ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp) operation to update a private IP address.


Was this article helpful?
YesNo

