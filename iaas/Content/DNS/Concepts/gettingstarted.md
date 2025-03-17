Updated 2025-03-10
# Public DNS
Get started with the Oracle Cloud Infrastructure DNS service.
Public domain name service (DNS) zones hold the authoritative DNS records that reside on OCI's nameservers. You can create public zones with publicly available domain names reachable on the internet. For more information, see [Overview of DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/dnszonemanagement.htm#overview "The DNS service helps you create and manage DNS zones.").
## Service Capabilities and Limits 🔗 
  * The OCI DNS service is limited to 1000 zones per account and 25,000 records per zone. Customers with zone and record size needs exceeding these values are encouraged to contact support at [support.oracle.com](http://support.oracle.com/). 
  * Zone file uploads are limited to 1 megabyte (MB) in size per zone file. If a zone file is larger than 1 MB, you need to split the zone file into smaller batches to upload all the zone information. For more information and a workaround for this limitation, see [Zone File Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/formattingzonefile.htm#formattingzonefile_topic-zone-file-limits).
  * Public DNS zones are only supported in the OC1 commercial realm. For more information and to check if a region is included in OC1, see [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).
  * Traffic Management is only available for public DNS, and isn't supported on private DNS.


## Setting Up Public DNS 🔗 
Use these steps to set up public DNS:
  1. [Create a public zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm#top "Create a public domain name service \(DNS\) zone to hold the trusted DNS records that reside on Oracle Cloud Infrastructure's nameservers.")
  2. [Delegate the zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Delegating_Your_Zone.htm#top "Make an OCI public domain name service \(DNS\) zone accessible through the internet.")
  3. [Add records to the zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).")


## Public DNS Tasks 🔗 
See these sections for information on managing DNS resources:
  * [Managing DNS Service Zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/managingdnszones.htm#managing-zones "The Oracle Cloud Infrastructure DNS service lets you manage zones using the Console, CLI, or API.")
  * [Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#supported-records "Learn about managing the many resource record types that the Oracle Cloud Infrastructure DNS service supports.")
  * [HTTP Redirects](https://docs.oracle.com/iaas/Content/DNS/Tasks/httpredirect.htm)
  * [Managing TSIG Keys](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/tsig.htm#manage-tsig "Transaction signature \(TSIG\), also referred to as Secret Key Transaction Authentication, ensures that domain name service \(DNS\) packets originate from an authorized sender by using shared secret keys and one-way hashing to add a cryptographic signature to the DNS packets.")


Was this article helpful?
YesNo

