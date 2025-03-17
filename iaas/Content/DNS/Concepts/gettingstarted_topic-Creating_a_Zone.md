Updated 2025-03-10
# Creating a Public DNS Zone
Create a public domain name service (DNS) zone to hold the trusted DNS records that reside on Oracle Cloud Infrastructure's nameservers.
You can create primary public zones with publicly available domain names reachable on the internet. For more information, see [Public DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted.htm#getting-started "Get started with the Oracle Cloud Infrastructure DNS service.").
You can also create a [secondary zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/secondary-dns.htm#secondary-dns "Set up secondary domain name system \(DNS\) zones using the Oracle Cloud Infrastructure DNS service."), which pulls records for the zone from an external primary server.
  * The OCI DNS service is limited to 1000 zones per account and 25,000 records per zone. Customers with zone and record size needs exceeding these values are encouraged to contact support at [support.oracle.com](http://support.oracle.com/). 
  * Zone file uploads are limited to 1 megabyte (MB) in size per zone file. If a zone file is larger than 1 MB, you need to split the zone file into smaller batches to upload all the zone information. For more information and a workaround for this limitation, see [Zone File Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/formattingzonefile.htm#formattingzonefile_topic-zone-file-limits).
  * Public DNS zones are only supported in the OC1 commercial realm. For more information and to check if a region is included in OC1, see [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).


  * [Console](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **DNS management** , select **Zones**.
    2. Select a compartment, and then in the **Public zones** tab, select **Create zone**.
    3. On the **Create public zone** panel, select the method to use to create the zone, **Manual** or **Import**.
    4. If you chose the manual method, enter the zone information:
       * **Zone type:** Select **Primary**.
       * **Zone name:** Enter the domain name for the zone. For example, `mydomain.com.` Avoid entering confidential information.
       * **Create in compartment:** Specify the compartment to create the zone in. Be sure you have permission to work in the compartment.
    5. If you chose the import method, then drag, select, or paste a [valid zone file](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/formattingzonefile.htm#format-zone-file "A domain name service \(DNS\) zone file is a text file that describes a DNS zone. The BIND file format is the industry preferred zone file format and has been widely adopted by DNS server software.") into the panel.
The zone is imported as a primary zone.
    6. (Optional) Configure one or more secondary servers to receive zone transfers.
      1. Select **Add additional server IP**.
      2. Enter a valid IPv4 or IPv6 address.
      3. Select a [TSIG key](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.").
For more information, see [Secondary DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/secondary-dns.htm#secondary-dns "Set up secondary domain name system \(DNS\) zones using the Oracle Cloud Infrastructure DNS service.") and [Adding Downstream Servers to a Primary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm#top "Set up secondary egress from OCI DNS to an external DNS provider."). 
    7. (Optional) To apply tags to the zone, select **Show Advanced Options**.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    8. (Optional) Select **Show Advanced Options:** to enable DNSSEC.
**Note** You can't enable DNSSEC if you plan to use downstream servers with the zone. DNSSEC requires updates to the DS records on the zone. See [DNSSEC](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnssec.htm#top "Domain name system security extensions \(DNSSEC\) provides cryptographic authentication for DNS lookup responses.") for more information.
    9. Select **Create**.
The zone is created and published with the necessary SOA and NS records, and its details page is displayed. 
Next:
       * [Delegate the public zone with a registrar](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Delegating_Your_Zone.htm#top "Make an OCI public domain name service \(DNS\) zone accessible through the internet.")
**Note** The zone doesn't work on the internet until delegation is complete. 
       * [Add records to the zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).")
If you have problems, see [Troubleshooting DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/troubleshooting.htm#troubleshooting "Use troubleshooting information to identify and address common issues that can occur while working with DNS.").
  * Use the [zone create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/dns/zone/create.html) command and required parameters to create a public primary zone:
Command
CopyTry It
```
oci dns zone create --compartment-id compartment_id --name "zone_name" --zone-type PRIMARY --scope GLOBAL... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. For information on adding a record to a zone, see [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).").
  * Run the [CreateZone](https://docs.oracle.com/iaas/api/#/en/dns/latest/Zone/CreateZone) operation to create a public primary zone. Specify the zone type as `PRIMARY` and zone scope as `GLOBAL`.
The system creates and publishes the zone, complete with the necessary SOA and NS records. The details for the zone appear. For information on adding a record to a zone, see [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).").


Was this article helpful?
YesNo

