Updated 2025-03-10
# Creating a Private DNS Zone in a Private View
Create a private domain name service (DNS) zone in a private view to manage records and hostname resolution for applications running within and between virtual cloud networks (VCNs), and on-premises or other private networks.
Private DNS also provides DNS resolution across networks (for example, another VCN within the same region, cross region, or an external network). See [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns "Create and manage private domain name system \(DNS\) zones.") and [Private Views](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/views.htm#top "Use private views to logically group a set of private domain name service \(DNS\) zones. A zone can only belong to a single view.") for a feature overview and more information. 
For general service information, see the [DNS Service Overview](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
**Note**
  * Private zones can be viewed only in the region in which they're created.
  * You can't create a private zone at or under `oraclevcn.com` within the default protected view of a VCN dedicated resolver.


  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-add-zone.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-add-zone.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/view-add-zone.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Private views**.
    2. Under **List scope** , select the compartment that contains private view that you want to add a zone to. 
    3. Select the name of the view.
    4. Select **Create zone**.
**Note** The **Zone type** is set to `Primary` and is read-only.
    5. Enter a descriptive name for the zone. Avoid entering confidential information.
    6. Select a compartment to create the zone in.
    7. Select **Create**.
  * Use the [zone create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/create.html) command and required parameters to create a private zone in a specified private view:
Command
CopyTry It
```
oci dns zone create --compartment-id compartment_id --name "zone_name" --zone-type PRIMARY --scope PRIVATE
--view-id view_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. You can view the private view associated with this zone by selecting the Private View name in the Zone Information section. For information on adding a record to a zone, see [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).").
sd
  * Run the [CreateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone) operation to create a private zone in a specified private view.
Specify the zone `scope` as `PRIVATE`. Include the `viewId` parameter, populated with the **OCID** of the view you want to create the zone in.
The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. You can view the private view associated with this zone by selecting the Private View name in the Zone Information section. For information on adding a record to a zone, see [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).").


Was this article helpful?
YesNo

