Updated 2025-03-10
# Updating a Secondary DNS Zone
Update the master server IP information for a secondary domain name service (DNS) zone.
**Tip** For OCI to transfer data from a zone, the nameservers must accept a transfer request from the following IP addresses: 208.78.68.65, 204.13.249.65, 2600:2001:0:1::65, 2600:2003:0:1::65
Information such as zone name and type aren't editable after you create a zone.
To update zone records for a _primary_ zone, see [Changing DNS Zone Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-edit.htm#top "Change the records that contain domain information for a domain name service \(DNS\) zone. You can change various components of the records within zones, such as time-to-live \(TTL\) and relevant RDATA.").
For general information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.")
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-update.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Under List scope, select the compartment that contains the zone.
    3. Select the name of the zone to open its details page.
**Tip** You can use the **Zone Type** sort filter to sort zone type alphanumerically in ascending or descending order.
    4. Select **Upstream servers**.
    5. Select **Manage upstream servers**.
    6. Make the changes to the existing upstream server information.
    7. (Optional) Select **Add additional server IP** to add another server IP address.
    8. Select **Submit**.
**Tip** For OCI to transfer data from the zone, the nameservers must accept a transfer request from the following IP addresses: 208.78.68.65, 204.13.249.65, 2600:2001:0:1::65, 2600:2003:0:1::65
  * Use the [zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/update.html) command and required parameters to update the master server IP addresses of a secondary zone:
Command
CopyTry It
```
oci dns zone update --zone-name-or-id zone_name or zone_OCID --external-masters '[{"address":"new_external_server_ip"}]' ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/UpdateZone) operation to update the master server IP addresses for a secondary zone.


Was this article helpful?
YesNo

