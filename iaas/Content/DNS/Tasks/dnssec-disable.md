Updated 2025-03-10
# Disabling DNSSEC on a Zone
Disable DNS security extensions (DNSSEC) on a public zone.
To avoid service disruptions, follow these steps in the order presented to disable DNSSEC.
  1. Remove DS records for the zone from all child zone delegation subdomains. See [Changing DNS Zone Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-edit.htm#top "Change the records that contain domain information for a domain name service \(DNS\) zone. You can change various components of the records within zones, such as time-to-live \(TTL\) and relevant RDATA.") for information about updating OCI zone records.
  2. Remove the DS record from the parent zone.
  3. Wait until the TTL (time to live) for the removed parent zone DS record expires.
  4. Either [delete the zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm#top "Delete a domain name service \(DNS\) zone and its records.") or disable DNSSEC on the zone.


  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-disable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-disable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-disable.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Select the zone name in the list to open its Details page.
    3. In **Zone information** , under DNSSEC, select **Edit**.
    4. Select the DNSSEC switch to **Disabled**.
    5. Select **Save changes**.
  * Use the [zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/update.html) command and required parameters to update the zone. To disable DNSSEC, specify the `dnssec-state` as `DISABLED`.:
Command
CopyTry It
```
oci dns zone update --zone-name-or-id zone_name or zone_OCID --dnssec-state DISABLED ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/UpdateZone) operation to update the zone. To disable DNSSEC, specify the `dnssecState` as `DISABLED`.


Was this article helpful?
YesNo

