Updated 2025-01-15
# Viewing Reserved Public IP Addresses
View a list of all reserved public IP addresses in a compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-reserved-public-ip.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-reserved-public-ip.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-reserved-public-ip.htm)


  * Open the **navigation menu** and select **Networking**. Under **IP management** , select **Reserved public IPs**.
If the reserved public IP is assigned, there's a link to the relevant VNIC. 
  * Use the [network public-ip list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/public-ip/list.html) command and required parameters to view a list of reserved public IP addresses:
Command
CopyTry It
```
oci network public-ip list --compartment-id compartment_ID ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListPublicIPs](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PublicIp/ListPublicIps) operation to list public IPs.


Was this article helpful?
YesNo

