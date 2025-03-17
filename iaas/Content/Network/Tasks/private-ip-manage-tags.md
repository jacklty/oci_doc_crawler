Updated 2025-02-06
# Managing Tags For a Private IP Address
Update tag information for a private IP address.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-manage-tags.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-manage-tags.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-manage-tags.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Select the name of the instance to open its details page.
    3. Under **Resources** , select **Attached VNICs**.
    4. Select the VNIC that you're interested in.
    5. Under **Resources** , select **IPv4 Addresses**.
The VNIC's associated IP addresses are listed in tabular form.
    6. Find the IP address you want to update, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **View tags**.
       * If you're editing an existing tag, select the pencil icon next to the tag, make the changes, and then select **Save**.
       * If you're deleting an existing tag, select the pencil icon next to the tag and then select **Remove tag**.
       * If you're adding a new tag, select **Add tag**. Add the tag information and then select **Add tags**.
    7. When you're done, select **Cancel** to exit the View tags page.
  * Use the [private-ip update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/update.html) command and required parameters to update tags for the private IP address:
Command
CopyTry It
```
oci network private-ip update --private-ip-id IP_address_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp) operation to update tags for a private IP address.


Was this article helpful?
YesNo

