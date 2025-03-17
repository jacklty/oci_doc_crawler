Updated 2025-03-10
# Adding a Record to a DNS Zone
Add records that contain domain information to a domain name service (DNS) zone. Each record type contains information called record data (RDATA).
For example, the RDATA of an [A](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_a-record) or [AAAA](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_aaaa) record contains an IP address for a domain name, while MX records contain information about the mail server for a domain. Oracle Cloud Infrastructure normalizes all RDATA into the most machine-readable format. The returned presentation of RDATA might differ from its initial input. For more information, see [Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#supported-records "Learn about managing the many resource record types that the Oracle Cloud Infrastructure DNS service supports.").
For general service information, see the [DNS Service Overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.")
**Note** You can't manage records when a zone isn't active. 
  * If the zone is updating, wait a few moments and try again.
  * If the zone is in a failed state, delete the zone and re-create it. Be sure the zone name is unique, and that no error exists in any zone file you might have used to create the zone.


  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm)


  * **Note** The number and type of records in a zone depend on the goals for the zone and its DNS management.
    1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Under **List scope** , select the compartment that contains the zone that you want to add a record to.
    3. Select the name of the zone to open its details page.
    4. Under **Resources** , select **Records**.
A list of records appear. Records that have the same name, type, and TTL are displayed as a single RRset in the Zone Records list.
    5. Select **Manage records**.
    6. Select **Add record**.
    7. In the **Add record** panel, enter record information:
      1. (Optional) Enter a **Name** for the record. Avoid entering confidential information.
      2. Select a record **Type**. For more information about record types, see [Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#supported-records "Learn about managing the many resource record types that the Oracle Cloud Infrastructure DNS service supports.").
      3. Enter a TTL (time to live) for the record.
    8. In the **RDATA/Answers** section, select the RDATA entry mode and then enter the record information: 
       * Select **Basic** to enter one record at a time. Select **+Another record** to add more records.
       * Select the switch to select **Advanced** and add many records at the same time. Each record must be on its own line.
    9. Select **Add record**.
    10. Select **Publish changes**.
    11. On the **Confirm** page, review the changes, and then select **Confirm publish changes**.
  * **Important**
    * If a specified record doesn't exist, it's created. If the record exists, then it's updated to represent the record in the body of the request.
    * When the zone name is provided as a path parameter and _PRIVATE_ is used for the scope query parameter, then the `viewId` query parameter is required.
    * Use the [record rrset update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/record/rrset/update.html) command and required parameters to add a single record in an RRset in a zone. An RRset is defined as a group of records that have the same name, type, and TTL values.
Command
CopyTry It
```
oci dns record rrset update --domain FQDN_1 --rtype "record_type_1" --zone-name-or-id zone_name or zone_OCID
--items '[{"domain":"FQDN_1","rdata":"record_data","rtype":"record_type_1","ttl":"time_to_live_seconds"}]' ... [OPTIONS]
```

    * Use the [record zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/record/zone/update.html) command and required parameters to bulk add records to a zone. 
Command
CopyTry It
```
oci dns record zone update --zone-name-or-id zone_name or zone_OCID --items 
'[{"domain":"FQDN_1","rdata":"record_data","rtype":"record_type_1","ttl":"time_to_live_seconds"};
{"domain":"FQDN_2","rdata":"record_data","rtype":"record_type_1","ttl":"time_to_live_seconds"}]' ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * **Important**
    * If a specified record doesn't exist, it's created. If the record exists, then it's updated to represent the record in the body of the request.
    * When the zone name is provided as a path parameter and _PRIVATE_ is used for the scope query parameter then the `viewId` query parameter is required.
    * Run the [UpdateRrset](https://docs.oracle.com/iaas/api/#/en/dns/latest/RRSet/UpdateRRSet) operation to add a single record to an RRset in a zone. An RRset is defined as a group of records that have the same name, type, and TTL values.
    * Run the [UpdateZoneRecords](https://docs.oracle.com/iaas/api/#/en/dns/latest/Records/UpdateZoneRecords) operation to bulk add many records to a zone.


Was this article helpful?
YesNo

