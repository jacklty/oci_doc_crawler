Updated 2025-03-10
# Managing Resource Records
Learn about managing the many resource **record** types that the Oracle Cloud Infrastructure DNS service supports.
The following list provides a brief explanation of the purpose of each supported record type for _public_ domain name service (DNS) zones. For private DNS, see [Private DNS Supported Resource Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/privatedns.htm#privatedns_topic_supported_resource_records). Avoid entering confidential information when entering record data. The RFC links direct you to further information about the record types and data structure. 
## Note About RDATA 🔗 
Oracle Cloud Infrastructure normalizes all RDATA into the most machine readable format. The returned presentation of RDATA might differ from its initial input.
**Example:**
The RDATA for the ALIAS, CNAME, DNAME, MX, and NS record types might contain one or more absolute domain names. If the specified RDATA for one of these record types doesn't end in a dot or period to represent the root, the period is added.
`www.example.com --> www.example.com.`
You can use various DNS libraries to normalize RDATA before input.
Programming Language | Library  
---|---  
Go | [DNS Library in Go](https://github.com/miekg/dns)  
Java | [dnsjava](http://www.dnsjava.org/)  
Python | [dnspython](http://www.dnspython.org/)  
## Public DNS Resource Record Types 🔗  

A
    An address record used to point a **hostname** to an IPv4 address. For more information about A records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-21). 

AAAA
    An address record used point a hostname at an IPv6 address. For more information about AAAA records, see [RFC 3596](https://tools.ietf.org/html/rfc3596#section-2.1). 

ALIAS
    A nonstandard DNS record type that allows CNAME-like functionality at the apex of a **zone**. ALIAS records can't coexist with steering policy attachments on a domain. 

CAA
    A Certification Authority Authorization record allows a **domain name** holder to specify one or more Certification Authorities authorized to issue certificates for that **domain**. For more information about CAA records, see [RFC 6844](https://tools.ietf.org/html/rfc6844#section-3). 

CERT
    A Certificate record stores public key certificates and related certificate revocation lists in the DNS. For more information about CERT records, see [RFC 2538](https://tools.ietf.org/html/rfc2538) and [RFC 4398](https://tools.ietf.org/html/rfc4398#section-2). 

CNAME
    A Canonical Name record identifies the canonical name for a domain. For more information about CNAME records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-13). 

CSYNC
    A Child-to-Parent Synchronization record syncs records from a child zone to a parent zone. For more information about CNAME records, see [RFC 7477](https://tools.ietf.org/html/rfc7477#section-2). 

DHCID
    A DHCP identifier record provides a way to store **DHCP** client identifiers in the DNS to eliminate potential hostname conflicts within a zone. For more information about DHCID, see [RFC 4701](https://tools.ietf.org/html/rfc4701#section-3). 

DNAME
    A Delegation Name record has similar behavior to a CNAME record, but allows you to map an entire subtree beneath a label to another domain. For more information about DNAME records, see [RFC 6672](https://tools.ietf.org/html/rfc6672#section-2). 

DNSKEY
    A DNSKEY record documents public keys used for DNSSEC. When DNSSEC is enabled on OCI, these records are automatically created and managed by the service, but you can change the TTL (time to live) value. For more information about DNSKEY records, see [RFC 4034](https://tools.ietf.org/html/rfc4034#section-2). 

DS
    
A Delegation Signer record resides at the top-level domain and points to a child zone's DNSKEY record. DS records are created when DNSSEC security authentication is added to the zone. This record is added at the point of delegation to the child zone (on a subdomain). For more information about DS records, see [RFC 4034](https://tools.ietf.org/html/rfc4034#section-5). 

IPSECKEY
    An IPSec Key record stores public keys for a host, network, or application to connect to IP security (IPSec) systems. For more information on IPSECKEY records, see [RFC 4025](https://tools.ietf.org/html/rfc4025#section-2). 

KEY
    A Key record stores a public key that's associated with a domain name. Only used by SIG and TKEY records. IPSECKEY and DNSKEY have replaced key for use in IPSec and DNSSEC. For more information about KEY records, see [RFC 4025](https://tools.ietf.org/html/rfc4025#section-2). 

KX
    A Key Exchanger record identifies a key management agent for the associated domain name with some cryptographic systems (not including DNSSEC). For more information about KX records, see [RFC 2230](http://tools.ietf.org/html/rfc2230). 

LOC
    A Location record stores geographic location data of computers, **subnets** , and networks within the DNS. For more information about LOC records, see [RFC 1876](http://tools.ietf.org/html/rfc1876). 

MX
    A Mail Exchanger record defines the mail server accepting mail for a domain. MX records must point to a hostname. MX records must not point to a CNAME or IP address. For more information about MX records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12). 

NAPTR
    A Naming Authority Pointer record stores information used by ENUM (Telephone Number Mapping) to map E.164 numbers to URIs. For more information about NAPTR records, see [RFC 3403](https://tools.ietf.org/html/rfc3403#section-4). 

NS
    A **Nameserver** record lists the authoritative nameservers for a zone. DNS automatically generates NS records at the apex of each new primary zone. For more information about NS records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12). 

NSAP
    A Network Service Access Point record maps a domain name to an NSAP address. For more information about NSAP records, see [RFC 1637](http://tools.ietf.org/html/rfc1637). 

PTR
    A Pointer record reverse maps an IP address to a hostname. This behavior is the opposite of an A Record, which forward maps a hostname to an IP address. PTR records are commonly found in reverse DNS zones. For more information about PTR records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12). 

PX
    A resource record used in X.400 mapping protocols. For more information about PX records, see [RFC 822](http://tools.ietf.org/html/rfc822) and [RFC 2163](http://tools.ietf.org/html/rfc2163). 

RP
    A Responsible Person record contains information on how to contact the chosen responsible parties for a domain. For more information about RP records, see [RFC 1183](http://tools.ietf.org/html/rfc1183#section-2). 

SOA
    
A Start of Authority record specifies authoritative information about a DNS zone, including:
  * The primary nameserver.
  * The email of the domain administrator.
  * The domain serial number.
  * Several timers relating to refreshing the zone.


OCI DNS automatically generates an SOA record when a zone is created. For more information about SOA records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12). 

SPF
    A Sender Policy Framework record is a special TXT record used to store data designed to detect email spoofing. For more information about SPF records, see [RFC 4408](http://tools.ietf.org/html/rfc4408). 

SRV
    A Service Locator record allows administrators to use several servers for a single domain. For more information about SRV records, see [RFC 2782](http://tools.ietf.org/html/rfc2782). 

SSHFP
    An SSH Public Key Fingerprint record publishes SSH public host key fingerprints using the DNS. For more information about SSHFP records, see [RFC 6594](http://tools.ietf.org/html/rfc6594). 

TLSA
    A Transport Layer Security Authentication record associates a TLS server certificate, or public key, with the domain name where the record is found. This relationship is called a TLSA certificate association. For more information about TLSA records, see [RFC 6698](https://tools.ietf.org/html/rfc6698#section-2). 

TXT
    A record that holds descriptive, human readable text, and can also include non-human readable content for specific uses. Commonly used for SPF records and DKIM records that require non-human readable text items. For more information about TXT records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).
## Records Tasks  🔗 
The Oracle Cloud Infrastructure DNS service lets you manage zone records using the Console, API, or CLI.
You can perform the following tasks with zone records:
  * [Adding a Record to a DNS Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-add.htm#top "Add records that contain domain information to a domain name service \(DNS\) zone. Each record type contains information called record data \(RDATA\).")
  * [Changing DNS Zone Records](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-edit.htm#top "Change the records that contain domain information for a domain name service \(DNS\) zone. You can change various components of the records within zones, such as time-to-live \(TTL\) and relevant RDATA.")
  * [Deleting a DNS Zone Record](https://docs.oracle.com/en-us/iaas/Content/DNS/Tasks/record-delete.htm#top "Delete the records in a domain name service \(DNS\) zone.")


Was this article helpful?
YesNo

