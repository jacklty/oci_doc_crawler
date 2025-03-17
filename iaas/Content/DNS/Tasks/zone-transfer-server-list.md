Updated 2025-03-10
# Listing Zone Transfer Servers
You can use the CLI or API to obtain a list of IP addresses of OCI domain name service (DNS) nameservers for inbound and outbound transfer of zones.
Zone transfer servers are OCI nameservers for inbound and outbound transfer of zones. You can obtain a list of transfer servers in a specified compartment that transfer zone data with external master or downstream nameservers. The compartment you specify must be the root compartment of the tenancy.
For general service information, see the [DNS Service Overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-transfer-server-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-transfer-server-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-transfer-server-list.htm)


  * This task isn't available in the Console.
  * Use the [zone-transfer-server list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone-transfer-server/list.html) command and required parameters to list transfer servers in a compartment:
Command
CopyTry It
```
oci dns zone-transfer-server list --compartment-id compartment_id ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListZoneTransferServers](https://docs.oracle.com/iaas/api/#/en/dns/latest/ZoneTransferServer/ListZoneTransferServers) operation to see all transfer servers in a compartment.


Was this article helpful?
YesNo

