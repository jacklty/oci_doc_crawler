Updated 2025-01-10
# Managing DNS Service Zones
The Oracle Cloud Infrastructure DNS service lets you manage **zones** using the Console, CLI, or API.
A zone is a part of the domain name service (DNS) namespace. A Start of Authority record (SOA) defines a zone. A zone contains all labels underneath itself in the tree, unless otherwise specified.
## Service Capabilities and Limits 🔗 
  * The OCI DNS service is limited to 1000 zones per account and 25,000 records per zone. Customers with zone and record size needs exceeding these values are encouraged to contact support at [support.oracle.com](http://support.oracle.com/). 
  * Zone file uploads are limited to 1 megabyte (MB) in size per zone file. If a zone file is larger than 1 MB, you need to split the zone file into smaller batches to upload all the zone information. For more information and a workaround for this limitation, see [Zone File Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/formattingzonefile.htm#formattingzonefile_topic-zone-file-limits).
  * Public DNS zones are only supported in the OC1 commercial realm. For more information and to check if a region is included in OC1, see [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).


## Zone Tasks 🔗 
You can perform the following tasks with zones:
  * [Creating a Public DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm#top "Create a public domain name service \(DNS\) zone to hold the trusted DNS records that reside on Oracle Cloud Infrastructure's nameservers.")
  * [Creating a Private DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-private-zone.htm#top "Create a private domain name service \(DNS\) zone to manage records and hostname resolution for applications running within and between virtual cloud networks \(VCNs\), and on-premises or other private networks.")
  * [Creating a Secondary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/create-secondary-zone.htm#top "Create a secondary domain name service \(DNS\) zone to set up ingress from an external DNS provider to Oracle Cloud Infrastructure \(OCI\) DNS.")
  * [Delegating a Public DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Delegating_Your_Zone.htm#top "Make an OCI public domain name service \(DNS\) zone accessible through the internet.")
  * [Adding Downstream Servers to a Primary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-downstream-servers-primary-zone.htm#top "Set up secondary egress from OCI DNS to an external DNS provider.")
  * [Listing DNS Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-list.htm#top "View a list of domain name service \(DNS\) zones in a compartment.")
  * [Getting a DNS Zone's Details](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-get.htm#top "View detailed information about a domain name service \(DNS\) zone.")
  * [Moving a DNS Zone Between Compartments](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-move-compartment.htm#top "Move a domain name service \(DNS\) zone from one compartment to another.")
  * [Updating a Secondary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-update.htm#top "Update the master server IP information for a secondary domain name service \(DNS\) zone.")
  * [Adding a TSIG Key to a Secondary DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/add-tsig-key-to-zone.htm#top "You can add a TSIG key directly to a secondary domain name service \(DNS\) zone. A TSIG key lets DNS authenticate updates to secondary zones.")
  * [Deleting a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/zone-delete.htm#top "Delete a domain name service \(DNS\) zone and its records.")
  * [Formatting a DNS Zone File](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/formattingzonefile.htm#format-zone-file "A domain name service \(DNS\) zone file is a text file that describes a DNS zone. The BIND file format is the industry preferred zone file format and has been widely adopted by DNS server software.")


Was this article helpful?
YesNo

