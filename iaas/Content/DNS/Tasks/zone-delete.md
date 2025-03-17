Updated 2025-03-10
# Deleting a DNS Zone
Delete a domain name service (DNS) zone and its records.
**Caution** Deletion permanently removes a zone and its records from the DNS service.
For more information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Under **List scope** , select the compartment that contains the zone that you want to delete. All zones are listed in tabular form.
    3. Find the zone you want to delete, and then select **Delete** from its Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)).
    4. Enter the zone name to confirm the deletion, and then select **Delete**.
  * Use the [zone delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/delete.html) command and required parameters to delete a zone:
Command
CopyTry It
```
oci dns zone delete --zone-name-or-id zone_id or zone_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/DeleteZone) operation to delete a zone.


Was this article helpful?
YesNo

