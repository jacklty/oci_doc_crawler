Updated 2025-02-06
# Deleting a Private IP Address
Delete a private IP address from a VNIC.
Prerequisite: We recommend removing the IP address from the OS configuration before deleting it from the VNIC. See [Configuring Linux to Use a Secondary Private IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Linux_Details_about_Secondary_IP_Addresses.htm#Linux "Configure Linux to use a secondary private IP address.") or [Configuring Windows to Use a Secondary IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm#Windows "Configure the Windows OS to use a secondary private IP.").
**Caution** If the private IP is the [target of a route rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route), deleting it from the VNIC causes the route rule to drop the traffic. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Select the name of the instance to open its details page.
    3. Under **Resources** , select **Attached VNICs**.
    4. Select the VNIC that you're interested in.
    5. Under **Resources** , select **IPv4 Addresses**.
The VNIC's associated IP addresses are listed in tabular form.
    6. Find the IP address you want to update, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete Private IP**.
    7. Confirm when prompted.
  * Use the [private-ip delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/delete.html) command and required parameters to delete a private IP address:
Command
CopyTry It
```
oci network private-ip delete --private-ip-id IP_address_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeletePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/DeletePrivateIp) operation to delete a private IP address.


Was this article helpful?
YesNo

