Updated 2025-03-10
# Rolling Over a Key-Signing Key (KSK)
DNSSEC key-signing keys (KSKs) require annual rollover and key promotion.
KSK rollover begins annually when a replacement DNSSEC key version is automatically created. You need to complete the rollover process manually. You're notified that the new key version requires promotion in the Console. To avoid a service disruption, we also recommend that you set up alarms to ensure that you perform all required key rollovers on time. See [DNSSEC](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnssec.htm#top "Domain name system security extensions \(DNSSEC\) provides cryptographic authentication for DNS lookup responses.") for more information.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-rollover-ksk.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-rollover-ksk.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/dnssec-rollover-ksk.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Select the zone name in the list to open its Details page.
    3. In the zone, under **Resources** , select **DNS security extensions**.
    4. In the DNSSEC list, verify that the KSK for the zone has a status of **Needs Promotion**. 
**Note** You can rollover a KSK sooner than the default 1 year period. Select the key's Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and then select **Stage replacement key version**. A new KSK is created.
    5. Create a new [DS record](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_ds) containing the new (KSK) information to the parent zone. The parent zone can be an OCI zone, or a zone in another provider:
      1. In the zone, under **Resources** , select **DNS security extensions**.
      2. In the **Promote KSK** infoblock, select the data type:
         * **Structured:** Digest fields are copied separately. Select this option if the parent zone DNS provider requires separate input for each field in the DS record.
         * **Unstructured:** Digest fields are copied into a single string. Select this option if the parent zone DNS provider supports presentation format input for the DS record.
      3. Select **Copy** to copy the digest information and the recommended TTL (time to live) information.
      4. Paste the DS record digest information into a DS record for the zone. If the zone is an OCI zone, see [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).") for instructions.
      5. Select **Promote new key-signing key**.
    6. Remove the old [DS record](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_ds) containing the old (KSK) information from the parent zone. 
**Important** To avoid service disruptions, after the new DNSKEY record is created **you must wait until the DNSKEY record's TTL expires before removing the old DS record**. 
  * Use the [zone stage DNSSEC key version](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/stage-dnssec-key-version.html) command o stage a new key:
Command
CopyTry It
```
oci dns zone stage-dnssec-key-version --zone-name-or-id zone_name or zone_OCID --predecessor-dnssec-key-version-uuid previous-key-ID ... [OPTIONS]
```

Use the [zone promote DNSSEC key version](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/promote-dnssec-key-version.html) command to promote the staged key:
Command
CopyTry It
```
oci dns zone promote-dnssec-key-version --zone-name-or-id zone_name or zone_OCID --dnssec-key-version-uuid key-ID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [stageDnssecKeyVersion](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/StageZoneDnssecKeyVersion) operation to stage a new key. Run the [promoteDnssecKeyVersion](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/PromoteZoneDnssecKeyVersion) to promote the staged key.


Was this article helpful?
YesNo

