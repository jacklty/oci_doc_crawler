Updated 2025-03-10
# Creating a Private DNS Zone
Create a private domain name service (DNS) zone to manage records and hostname resolution for applications running within and between virtual cloud networks (VCNs), and on-premises or other private networks. 
Private DNS also provides DNS resolution across networks (for example, another VCN within the same region, cross region, or an external network). See [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns "Create and manage private domain name system \(DNS\) zones.") for a feature overview and more information.
**Note**
  * Private zones can be viewed only in the region in which they're created.
  * You can't create a private zone at or under `oraclevcn.com` within the default protected view of a VCN dedicated resolver.


  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-private-zone.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-private-zone.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-private-zone.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. On the **Private zones** tab, select **Create zone**.
    3. Enter the zone information.
       * **Zone type:** Select **Primary**.
       * **Zone name:** Enter a domain name for the zone. Avoid entering confidential information.
       * **Create in compartment:** Specify the compartment to create the zone in. Be sure you have permission to work in the compartment.
       * **DNS private view:** Select an existing private view from the list, or create a new one and enter a descriptive name for it. Avoid entering confidential information.
    4. (Optional) Select **Show Advanced Options:** to apply tags for the zone. 
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    5. Select **Create**.
The zone is created and published with the necessary SOA and NS records, and its details page is displayed. You can view the private view associated with this zone by select the name of the private view on the **Zone information** tab.
Next, you can [add records to the zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).").
  * Use the [zone create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/create.html) command and required parameters to create a private zone. Specify the scope as `PRIVATE`.
Command
CopyTry It
```
oci dns zone create --compartment-id compartment_id --name "zone_name" --zone-type PRIMARY --scope PRIVATE
--view-id view_OCID ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. You can view the private view associated with this zone by selecting the Private View name in the Zone Information section. For information on adding a record to a zone, see [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).").
  * Run the [CreateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone) operation to create a private zone. Specify the zone `scope` as `PRIVATE`.
The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. You can view the private view associated with this zone by selecting the Private View name in the Zone Information section. For information on adding a record to a zone, see [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).").


Was this article helpful?
YesNo

