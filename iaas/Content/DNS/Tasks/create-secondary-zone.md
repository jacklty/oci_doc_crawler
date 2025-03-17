Updated 2025-03-10
# Creating a Secondary DNS Zone
Create a secondary domain name service (DNS) zone to set up ingress from an external DNS provider to Oracle Cloud Infrastructure (OCI) DNS.
This topic describes how to set up an OCI secondary zone that accepts zone transfers from an external DNS provider (secondary ingress). To set up a scenario where a primary OCI DNS zone transfers to a secondary external DNS provider (secondary egress), see the [Secondary DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/secondary-dns.htm#secondary-dns "Set up secondary domain name system \(DNS\) zones using the Oracle Cloud Infrastructure DNS service.") overview page. 
Secondary ingress DNS requires that you define the zone name and the IP addresses of the primary external server during the secondary zone creation process. Also, you need connectivity to OCI IP addresses on the externally managed primary DNS servers. Connectivity to OCI IP addresses is a requirement for secondary DNS because it lets the service perform the required zone transfer process from the primary DNS to keep the secondary zone in sync. 
You can obtain the OCI IP addresses that perform the zone transfers from the primary DNS in one of the following ways: 
  * Use the OCI API before you begin setup. [ ListZoneTransferServers](https://docs.oracle.com/iaas/api/#/en/dns/latest/ZoneTransferServer/ListZoneTransferServers) returns a list of IP addresses provided for the specified root compartment. The provided transfer name server IP addresses vary by region. For more information, see [Listing Zone Transfer Servers](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-transfer-server-list.htm#top "You can use the CLI or API to obtain a list of IP addresses of OCI domain name service \(DNS\) nameservers for inbound and outbound transfer of zones.").
  * If you're using the Console, the list of zone transfer servers appears in the Create public zone page.


You can optionally configure a secondary DNS zone to use a TSIG key. If you don't already have an existing TSIG key, create one before you begin setting up the secondary DNS zone. For more information, see [Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.").
See [Secondary DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/secondary-dns.htm#secondary-dns "Set up secondary domain name system \(DNS\) zones using the Oracle Cloud Infrastructure DNS service.") for a feature overview and more information.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-secondary-zone.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-secondary-zone.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-secondary-zone.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. On the **Public zones** tab, select **Create zone**.
    3. For **Method** , select **Manual**.
    4. For **Zone type** , select **Secondary**.
    5. Enter a descriptive name for the zone. Avoid entering confidential information.
    6. Specify the compartment to create the zone in. Be sure you have permission to work in the compartment.
**Important** Ensure the primary nameservers can accept a transfer request from the list of OCI zone transfer destination IP addresses provided in the **Create public zone** panel.
    7. For **Upstream server IP** , add an external upstream nameserver IP address. Select **Add additional server IP** to add more upstream server IP addresses.
    8. (Optional) Select a [TSIG key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.").
    9. Select **Create**.
  * Use the [zone create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/create.html) command and required parameters to create a secondary zone:
Command
CopyTry It
```
oci dns zone create --compartment-id compartment_id --name "zone_name" --zone-type SECONDARY --scope GLOBAL
--external-masters '[{"address":"external_server_ip","port":"port_number","tsigKeyId":"tsig_key_OCID"}]' ... [OPTIONS]
```

The `external-masters` option becomes a required parameter when the _zoneType_ value is _SECONDARY_.
For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone) operation to create a secondary zone. Specify the `zoneType` as `SECONDARY` and the scope as `GLOBAL`. 
The `externalMasters` attribute becomes a required parameter when the _zoneType_ value is _SECONDARY_.


Was this article helpful?
YesNo

