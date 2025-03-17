Updated 2025-03-10
# Changing DNS Zone Records
Change the records that contain domain information for a domain name service (DNS) zone. You can change various components of the records within zones, such as time-to-live (TTL) and relevant RDATA.
For example, the RDATA of an [A](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_a-record) or [AAAA](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_aaaa) record contains an IP address for a domain name, while MX records contain information about the mail server for a domain. Oracle Cloud Infrastructure normalizes all RDATA into the most machine-readable format. The returned presentation of RDATA might differ from its initial input. For more information, see [Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#supported-records "Learn about managing the many resource record types that the Oracle Cloud Infrastructure DNS service supports.").
**Note**
  * Some records are protected and contain information that you can't change. 
  * You can't manage records when a zone isn't active. 
    * If the zone is updating, wait a few moments and try again.
    * If the zone is in a failed state, delete the zone and re-create it. Be sure the zone name is unique, and that no error exists in any zone file you might have used to create the zone.


For general service information, see the [DNS Service Overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.")
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-edit.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-edit.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-edit.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Under **List scope** , select the compartment that contains the zone in which you want to update a record. 
    3. Select the name of the zone to open its details page.
If you're updating a record in a private zone, select the **Private Zones** tab and then select the zone name. You can use filters to sort by zones that are protected (system generated) or by associated private view names.
    4. Under **Resources** , select **Records**. 
A list of records appears. Records that have the same name, type, and TTL are displayed as a single RRset in the Zone Records list.
    5. Select **Manage Records**.
    6. Use the **Filters** options to filter by record state or type.
    7. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the record that you want to update, and select **Edit**.
    8. In the **Edit Record** panel, make the changes, and then select **Save changes**.
When records are added, they're staged to combine records in an RRSet. Record changes don't take effect until they're published in the next steps.
    9. Select **Publish Changes**.
    10. On the **Confirm** page, review the changes and compare them with the previous published version, and then select **Confirm publish changes**.
  * **Important**
    * If a record in the zone or RRset doesn't exist in the request body, the record is _removed_ from the zone or RRset.
    * If a specified record doesn't exist, it's created. If the record exists, then it's updated to represent the record in the body of the request.
    * When the zone name is provided as a path parameter and _PRIVATE_ is used for the scope query parameter then the `viewId` query parameter is required.
    * Use the [record rrset update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/record/rrset/update.html) command and required parameters to edit a single record in an RRset. 
Command
CopyTry It
```
oci dns record rrset update --domain FQDN_1 --rtype "record_type_1" --zone-name-or-id zone_name or zone_OCID
--items '[{"domain":"FQDN_1","rdata":"updated_record_data" ,"rtype":"record_type_1","ttl":"time_to_live_seconds"}]' ... [OPTIONS]
```

    * Use the [record zone update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/record/zone/update.html) command and required parameters to bulk edit many records in a zone. 
Command
CopyTry It
```
oci dns record zone update --zone-name-or-id zone_name or zone_OCID --items 
'[{"domain":"FQDN_1","rdata":"updated_record_data","rtype":"record_type_1","ttl":"time_to_live_seconds"};
{"domain":"FQDN_2","rdata":"updated_record_data","rtype":"record_type_1","ttl":"time_to_live_seconds"}]' ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * **Important**
    * If a specified record doesn't exist, it's created. If the record exists, then it's updated to represent the record in the body of the request.
    * When the zone name is provided as a path parameter and _PRIVATE_ is used for the scope query parameter then the viewId query parameter is required.
    * Run the [UpdateRrset](https://docs.oracle.com/iaas/api/#/en/dns/latest/RRSet/UpdateRRSet) operation to edit a single record in an RRset in a zone. An RRset is defined as a group of records that have the same name, type, and TTL values.
    * Run the [UpdateZoneRecords](https://docs.oracle.com/iaas/api/#/en/dns/latest/Records/UpdateZoneRecords) operation to bulk edit many records in a zone.


Was this article helpful?
YesNo

