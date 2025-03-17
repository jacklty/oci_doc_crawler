Updated 2025-03-10
# Enabling DNSSEC on a Zone
Enable DNS security extensions (DNSSEC) on a public zone.
**Note** You can't enable DNSSEC on a private zone, or on a zone with downstream servers configured.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-enable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-enable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-enable.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Select the zone name in the list to open its Details page.
    3. In **Zone information** , under DNSSEC, select **Edit**.
    4. Select the DNSSEC switch to **Enabled**.
    5. Select **Save changes**. 
**Important** Wait for the work request to complete successfully before proceeding.
    6. For DNSSEC to work correctly, you need to add the key signing key (KSK) information to the parent zone [DS record](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_ds). The parent zone can be an OCI zone, or a zone in another provider:
      1. In the zone, under **Resources** , select **DNSSEC**.
      2. In the **Promote KSK** infoblock, select the data type:
         * **Structured:** Digest fields are copied separately. Select this option if the parent zone DNS provider requires separate input for each field in the DS record.
         * **Unstructured:** Digest fields are copied into a single string. Select this option if the parent zone DNS provider supports presentation format input for the DS record.
      3. Select **Copy** to copy the digest information and the recommended TTL (time to live) information.
      4. Paste the DS record digest information into a DS record for the zone. If the zone is an OCI zone, see [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).") for instructions. Here is an example of a DS record containing KSK digest information: 
```
20873 8 2 E2CEF72555BAF4978418FDB718F97F6421189B0862C456A5F75C25185EE61446
```

      5. Select **Promote new key-signing key**.
  * Use the [zone create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/create.html) command and required parameters to create a public primary zone. To enable DNSSEC, set the `dnssec-state` option to enabled:
Command
CopyTry It
```
oci dns zone create --compartment-id compartment_id --name "zone_name" --zone-type PRIMARY --scope GLOBAL
--dnssec-state ENABLED... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. For information on adding a record to the zone, see [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).").
  * Run the [CreateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone) operation to create a public primary zone. Specify the zone type as `PRIMARY` and zone scope as `GLOBAL`. To enable DNSSEC, specify the `dnssecState` as `ENABLED`.
The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. For information on adding a record to the zone, see [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).").


Was this article helpful?
YesNo

