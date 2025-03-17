Updated 2025-03-10
# Adding Downstream Servers to a Primary DNS Zone
Set up secondary egress from OCI DNS to an external DNS provider. 
Obtain the following items before you begin: 
  * IP addresses of the external downstream servers.
  * (Optional) TSIG keys to assign to each downstream server.
  * Ensure that externally managed primary DNS servers can access OCI egress nameservers. The OCI nameservers perform the required zone transfers that keep the secondary zone in sync. To list OCI egress nameserver IP addresses for the root compartment, see [Listing Zone Transfer Servers](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-transfer-server-list.htm#top "You can use the CLI or API to obtain a list of IP addresses of OCI domain name service \(DNS\) nameservers for inbound and outbound transfer of zones."). The provided transfer name server IP addresses vary by region.


See [Secondary DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/secondary-dns.htm#secondary-dns "Set up secondary domain name system \(DNS\) zones using the Oracle Cloud Infrastructure DNS service.") for more information and a feature overview.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Under **List scope** , select the compartment that contains the zone that you want to add external downstream servers to.
**Note** You can add downstream servers only to a _primary_ zone.
    3. Select the name of the zone to open its details page.
    4. Under **Resources** , select **Downstream servers**.
    5. Select **Manage downstream servers**.
    6. Enter a downstream server IP address. The IP address can be IPv4 or IPv6.
    7. (Optional) Select a [TSIG key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.").
    8. (Optional) Select **Add additional server IP** to add more downstream servers.
    9. Select **Submit**.
  * Use the [zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/update.html) command and required parameters to update the external secondary (downstream) servers for a zone:
Command
CopyTry It
```
oci dns zone update --zone-name-or-id zone_name or zone_OCID --external-downstream '[{"address":"new_external_server_ip"}]' ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/UpdateZone) operation to update the external secondary (downstream) servers for a zone.


Was this article helpful?
YesNo

