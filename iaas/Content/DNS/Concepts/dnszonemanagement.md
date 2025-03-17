Updated 2025-03-10
# Overview of DNS
The DNS service helps you create and manage DNS zones.
You can [create zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted_topic-Creating_a_Zone.htm#top "Create a public domain name service \(DNS\) zone to hold the trusted DNS records that reside on Oracle Cloud Infrastructure's nameservers."), [add records to zones](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\)."), and have Oracle Cloud Infrastructure's edge network handle your domain's DNS queries. 
See [Managing Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#supported-records "Learn about managing the many resource record types that the Oracle Cloud Infrastructure DNS service supports.") for more information.
**Tip** Watch a [video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:32173) to the service.
## What is DNS? 🔗 
The domain name system (DNS) translates human-readable **domain names** to machine-readable IP addresses. A DNS **nameserver** stores the DNS **records** for a **zone** , and responds with answers to queries against its database. When you type a domain name into a browser, the computer OS queries several DNS nameservers until it finds the authoritative nameserver for that domain. The authoritative nameserver then responds with an IP address or other requested record data. The answer is then relayed back to the browser and the DNS record is resolved to the web page.
The DNS service offers the following configurations and features:
  * [Public DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Concepts/gettingstarted.htm#getting-started "Get started with the Oracle Cloud Infrastructure DNS service."): Create zones with publicly available domain names reachable on internet. You need to register with a DNS registrar (delegation).
  * [Private DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#private-dns "Create and manage private domain name system \(DNS\) zones."): Provides **hostname** resolution for applications running within and between virtual cloud networks
  * [Secondary DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/secondary-dns.htm#secondary-dns "Set up secondary domain name system \(DNS\) zones using the Oracle Cloud Infrastructure DNS service."): Secondary DNS provides redundancy for primary DNS **servers**.
  * [Reverse DNS](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/reversedns.htm#reverse-dns "Reverse DNS maps an IP address to a hostname."): (RDNS) Maps an IP address to a **hostname**. 


## DNS Service Components 🔗 
The following list describes the components used to build a DNS zone and make it accessible from the internet. 

domain
    Domain names identify a specific location or group of locations on the Internet as a whole. A common definition of _domain_ is the complete part of the DNS tree that has been delegated to a user's control. For example, `example.com` or `oracle.com`. 

zone
    A zone is a part of the DNS namespace. A Start of Authority record (SOA) defines a zone. A zone contains all labels underneath itself in the tree, unless otherwise specified. 

label
    Labels are prepended to the zone name, separated by a period, to form the name of a subdomain. For example, the `www` section of `www.example.com` or the `docs` and `us-ashburn-1` sections of `docs.us-ashburn-1.oraclecloud.com` are labels. Records are associated with these domains. 

child zone
    Child zones are independent subdomains with their own Start of Authority and Name Server (NS) records. The parent zone of a child zone must contain NS records that refer DNS queries to the name servers responsible for the child zone. Each child zone creates another link in the delegation chain. 

resource records
    A record contains specific domain information for a zone. Each record type contains information called record data (RDATA). For example, the RDATA of an [A](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_a-record) or [AAAA](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#types__dlentry_aaaa) record contains an IP address for a domain name, while MX records contain information about the mail server for a domain. OCI normalizes all RDATA into the most machine readable format. The returned presentation of the RDATA might differ from its initial input. For more information about RDATA, see [Supported DNS Resource Record Types](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/supporteddnsresource.htm#supported-records "Learn about managing the many resource record types that the Oracle Cloud Infrastructure DNS service supports."). 

delegation
    
Delegating a domain with a registrar makes the OCI hosted **zone** accessible through the internet. OCI isn't a registrar. However, you can delegate OCI DNS zones with registrars such as VeriSign or GoDaddy. 
## Domain Name Normalization 🔗 
The OCI DNS service normalizes domain names that use [Internationalized Domain Names (IDNs)](https://www.icann.org/resources/pages/idn-2012-02-25-en) by converting them into [Punycode format](https://www.rfc-editor.org/rfc/rfc3492). Requests to OCI DNS can use IDNs, but responses use Punycode. For example, if you create a zone and provide an IDN zone name, the resulting response for the created zone uses Punycode.
## Ways to Access the DNS Service 🔗 
You can access Oracle Cloud Infrastructure (OCI) by using the [Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin_topic-Signing_In_for_the_First_Time.htm) (a browser-based interface), [REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm), or [OCI CLI](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). Instructions for using the Console, API, and CLI are included in topics throughout this documentation. For a list of available SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
## Authentication and Authorization 🔗 
Each service in Oracle Cloud Infrastructure integrates with IAM for authentication and authorization, for all interfaces (the Console, SDK or CLI, and REST API).
An administrator in an organization needs to set up **groups** , **compartments** , and **policies** that control which users can access which services, which resources, and the type of access. For example, the policies control who can create new users, create and manage the cloud network, create instances, create buckets, download objects, and so on. For more information, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm). For specific details about writing policies for each of the different services, see [Policy Reference](https://docs.oracle.com/iaas/Content/Identity/Reference/policyreference.htm). 
If you're a regular user (not an administrator) who needs to use the Oracle Cloud Infrastructure resources that the company owns, contact an administrator to set up a user ID for you. The administrator can confirm which compartment or compartments you can use.
## Monitoring Resources 🔗 
You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
## DNS Service Capabilities and Limits 🔗 
  * The OCI DNS service is limited to 1000 zones per account and 25,000 records per zone. Customers with zone and record size needs exceeding these values are encouraged to contact support at [support.oracle.com](http://support.oracle.com/). 
  * Zone file uploads are limited to 1 megabyte (MB) in size per zone file. If a zone file is larger than 1 MB, you need to split the zone file into smaller batches to upload all the zone information. For more information and a workaround for this limitation, see [Zone File Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/formattingzonefile.htm#formattingzonefile_topic-zone-file-limits).
  * Public DNS zones are only supported in the OC1 commercial realm. For more information and to check if a region is included in OC1, see [Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm).


## Required IAM Service Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm). For more details about policies for DNS, see [Details for the DNS Service](https://docs.oracle.com/iaas/Content/Identity/policyreference/dnspolicyreference.htm).
Permissions are required for managing DNS. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, the `read` verb covers permissions to read and inspect. The `manage` verb covers permissions for inspect, read, update, create, delete, and move. 
**Policy examples:**
  * To enable all operations on zones for a specific user group: ```
Allow group <GroupName> to manage dns in tenancy
```

  * To enable a specific group to read zones:```
Allow group <GroupName> to read dns-zones in tenancy
```

  * To create a read-only DNS management group:```
Allow group <GroupName> to read dns in tenancy
```



Was this article helpful?
YesNo

