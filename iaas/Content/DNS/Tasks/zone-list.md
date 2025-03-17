Updated 2025-03-10
# Listing DNS Zones
View a list of domain name service (DNS) zones in a compartment.
For more information, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Under **List scope** , select a compartment.
  * Use the [zone list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/list.html) command and required parameters to view a list of zones in a compartment.
Command
CopyTry It
```
oci dns zone list --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListZones](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/ListZones) operation to view all zones in a compartment.


Was this article helpful?
YesNo

