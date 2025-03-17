Updated 2025-03-10
# Deleting a DNS Zone Record
Delete the records in a domain name service (DNS) zone.
For more information, see [Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#supported-records "Learn about managing the many resource record types that the Oracle Cloud Infrastructure DNS service supports.").
For general service information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.")
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Under **List scope,** select the compartment that contains the zone in which you want to delete a record.
    3. Select the name of the zone to open its details page. 
If you're deleting a record in a private zone, select the **Private Zones** tab and then select the zone name. You can use filters to sort by zones that are protected (system generated) or by associated private view names.
    4. Under **Resources** , select **Records**. 
A list of records appear. Records that have the same name, type, and TTL are displayed as a single RRset.
    5. Select **Manage records**.
    6. Use the **Filters** option to filter by state or type.
    7. Find the record that you want to delete, select its Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete**.
Record changes don't take effect until they're published in the next steps.
    8. Select **Publish Changes**.
    9. On the Confirm page, review the changes, and then select **Confirm publish changes**.
  * Use the [record rrset delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/record/rrset/delete.html) command and required parameters to delete a record.
Command
CopyTry It
```
oci dns record rrset delete --domain FQDN_1 --rtype "record_type_1" --zone-name-or-id zone_name or zone_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteRrset](https://docs.oracle.com/iaas/api/#/en/dns/latest/RRSet/DeleteRRSet) operation to delete a record in a zone. 


Was this article helpful?
YesNo

