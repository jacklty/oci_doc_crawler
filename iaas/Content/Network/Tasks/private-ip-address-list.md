Updated 2025-02-06
# Listing Private IP Addresses
View a list of all private IP addresses for an instance.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-list.htm)


  *     1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
    2. Select the name of the instance to open its details page.
    3. Under **Resources** , select **Attached VNICs**.
    4. Select the VNIC that you're interested in.
    5. Under **Resources** , select **IPv4 Addresses**.
The VNIC's associated IP addresses are listed in tabular form.
  * Use the [private-ip list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/private-ip/list.html) command and required parameters to list private IP addresses for an instance:
Command
CopyTry It
```
oci network private-ip list --vnic-id VNIC_OCID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListPrivateIps](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/ListPrivateIps) operation to list private IPs for an instance.


Was this article helpful?
YesNo

