Updated 2025-03-10
# Getting a DNS Zone's Details
View detailed information about a domain name service (DNS) zone.
For more information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-get.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Under **List scope** , select the compartment that contains the zone that you want to view.
    3. Select the name of the zone to open its details page.
The zone details page displays general information about the zone and links to its resources. Some items in the page are read-only, such as zone name and type.
  * Use the [zone get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/get.html) command and required parameters to view details about a specific zone.
Command
CopyTry It
```
oci dns zone get --zone-name-or-id zone_name or zone_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/GetZone) operation to view details about a zone.


Was this article helpful?
YesNo

