Updated 2025-02-06
# Getting a Private IP Address's Details 
View details about a private IP address.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-get.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Select the name of the instance to open its details page.
    3. Under **Resources** , select **Attached VNICs**.
    4. Select the VNIC that you're interested in.
    5. Under **Resources** , select **IPv4 Addresses**.
The VNIC's associated IP addresses are listed in tabular form. Information such as any associated FQDN and date assigned is displayed.
    6. To view tagging information for a private IP address, select its Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and then select **View tags**.
  * Use the [private-ip get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/get.html) command and required parameters to view details about a private IP address:
Command
CopyTry It
```
oci network private-ip get --private-ip-id private_IP_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetPrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/GetPrivateIp) operation to view details about a private IP address.


Was this article helpful?
YesNo

