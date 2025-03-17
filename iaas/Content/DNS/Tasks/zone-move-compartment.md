Updated 2025-03-10
# Moving a DNS Zone Between Compartments
Move a domain name service (DNS) zone from one compartment to another. 
See [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm) for information about compartments and access control.
For more information about DNS, see the [DNS service overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.")
  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-move-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-move-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-move-compartment.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Under **List scope** , select the compartment that contains the zone.
    3. Find the zone in the list, select its Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and select **Move resource**.
    4. Select a destination compartment from the list.
    5. Select **Move resource**.
  * Use the [zone change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/change-compartment.html) command and required parameters to move a zone to a different compartment:
Command
CopyTry It
```
oci dns zone change-compartment --zone-id zone_OCID --compartment-id compartment_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeZoneCompartment](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/ChangeZoneCompartment) operation to move a zone to a different compartment.


Was this article helpful?
YesNo

