Updated 2023-08-15
# Managing Public DNS Zones
On Compute Cloud@Customer, the Domain Name System (DNS) lets computers use hostnames instead of IP addresses to communicate with each other.
In its most basic form, DNS returns an IP address (if known) when given a string in the DNS namespace for that zone. However, DNS is also the way that an IP host client application knows where to get its own configuration information using DHCP (DHCID records), go to send or receive email (MX records), and more. Without DNS, client devices would have to know the proper IP addresses not only for local servers, but for every server or application they interacted with, no matter where in the world they were located. With DNS, clients can always find the correct location of www.oracle.com or any other application. 
After you create a DNS zone inside a compartment, you can't move the zone to another compartment. 
When creating a DNS zone, you specify the name of the domain it manages – for example: _example.com_. You select whether the zone is primary or secondary. A primary zone contains its own DNS records, while a secondary zone retrieves its records from another zone. To access the external zone's records, the secondary zone needs at least one server IP address for the external zone. In addition, a TSIG (Transaction Signature) key may be required. TSIG keys are shared secrets used for authentication of secondary DNS zones. You can store these keys in the compartment of your choice.
Each DNS zone you create automatically contains two essential records:
  * The SOA (Start of Authority) record specifies authoritative information about the DNS zone. This information includes the primary name server, the domain administrator email address, the domain serial number, and several timers related to refreshing the zone. For more information about SOA records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).
  * The NS (Name Server) record lists the authoritative name servers for a zone. For more information about NS records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).


You configure the DNS zone by adding specific domain information in the form of resource records. For example, using an address record, you make a domain name resolve to the public IP address of an instance in a public subnet of a VCN. The public DNS zones in Compute Cloud@Customer support the resource record types described in the following table.
Resource Record Type |  Description   
---|---  
A |  An address record used to point a host name to an IPv4 address. For more information about A records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).  
AAAA |  An address record used to point a host name at an IPv6 address. For more information about AAAA records, see [RFC 3596](https://tools.ietf.org/html/rfc3596#section-2.1).  
ALIAS |  A private pseudo-record that allows CNAME functionality at the apex of a zone.  
CAA |  A Certification Authority Authorization record allows a domain name holder to specify one or more Certification Authorities authorized to issue certificates for that domain. For more information about CAA records, see [RFC 6844](https://tools.ietf.org/html/rfc6844#section-3).  
CDNSKEY |  A Child DNSKEY moves a CDNSSEC key from a child zone to a parent zone. The information provided in this record must match the CDNSKEY information for your domain at your other DNS provider. This record is automatically created if you enable DNSSEC on a primary zone in Compute Cloud@Customer DNS. For more information about CDNSKEY, see [RFC 7344](https://tools.ietf.org/html/rfc7344#section-3.2).  
CDS |  A Child Delegation Signer record is a child copy of a DS record, for transfer to a parent zone. For more information about CDS records, see [RFC 7344](https://tools.ietf.org/html/rfc7344#section-3.2).  
CERT |  A Certificate record stores public key certificates and related certificate revocation lists in the DNS. For more information about CERT records, see [RFC 2538](https://tools.ietf.org/html/rfc2538) and [RFC 4398](https://tools.ietf.org/html/rfc4398#section-2).  
CNAME |  A Canonical Name record identifies the canonical name for a domain. For more information about CNAME records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).  
CSYNC |  A Child-to-Parent Synchronization record syncs records from a child zone to a parent zone. For more information about CNAME records, see [RFC 7477](https://tools.ietf.org/html/rfc7477#section-2).  
DHCID |  A DHCP identifier record provides a way to store DHCP client identifiers in the DNS to eliminate potential host name conflicts within a zone. For more information about DHCID, see [RFC 7477](https://tools.ietf.org/html/rfc7477#section-2).  
DKIM |  A Domain Keys Identified Mail is a special TXT record set up specifically to supply a public key used to authenticate arriving mail for a domain. For more information about DKIM records, see [RFC 6376](https://tools.ietf.org/html/rfc6376).  
DNAME |  A Delegation Name record has similar behavior to a CNAME record, but allows you to map an entire subtree beneath a label to another domain. For more information about DNAME records, see [RFC 6672](https://tools.ietf.org/html/rfc6672#section-2).  
DNSKEY |  A DNS Key record documents public keys used for DNSSEC. The information in this record must match the DNSKEY information for your domain at your other DNS provider. For more information about DNSKEY records, see [RFC 4034](https://tools.ietf.org/html/rfc4034#section-2).  
DS |  A Delegation Signer record resides at the top-level domain and points to a child zone's DNSKEY record. DS records are created when DNSSEC security authentication is added to the zone. For more information about DS records, see [RFC 4034](https://tools.ietf.org/html/rfc4034#section-2).  
IPSECKEY |  An IPSec Key record stores public keys for a host, network, or application to connect to IP security (IPSec) systems. For more information on IPSECKEY records, see [RFC 4025](https://tools.ietf.org/html/rfc4025#section-2).  
KEY |  A Key record stores a public key that is associated with a domain name. Currently only used by SIG and TKEY records. IPSECKEY and DNSKEY have replaced key for use in IPSec and DNSSEC, respectively. For more information about KEY records, see [RFC 4025](https://tools.ietf.org/html/rfc4025#section-2).  
KX |  A Key Exchanger record identifies a key management agent for the associated domain name with some cryptographic systems (not including DNSSEC). For more information about KX records, see [RFC 2230](https://tools.ietf.org/html/rfc2230).  
LOC |  A Location record stores geographic location data of computers, subnets, and networks within the DNS. For more information about LOC records, see [RFC 1876](https://tools.ietf.org/html/rfc1876).  
MX |  A Mail Exchanger record defines the mail server accepting mail for a domain. MX records must point to a host name. MX records must not point to a CNAME or IP address. For more information about MX records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).  
NS |  A Nameserver record lists the authoritative nameservers for a zone. NS records are automatically generated at the apex of each new primary zone you create. For more information about NS records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).  
PTR |  A Pointer record reverse maps an IP address to a hostname. This behavior is the opposite of an A Record, which forward maps a hostname to an IP address. PTR records are commonly found in reverse DNS zones. For more information about PTR records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).  
PX |  A resource record used in X.400 mapping protocols. For more information about PX records, see [RFC 822](https://tools.ietf.org/html/rfc822) and [RFC 2163](https://tools.ietf.org/html/rfc2163).  
SOA |  A Start of Authority record specifies authoritative information about a DNS zone, including:
  * the primary nameserver
  * the email of the domain administrator
  * the domain serial number
  * several timers relating to refreshing the zone

An SOA record is generated automatically when a zone is created. For more information about SOA records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).  
SPF |  A Sender Policy Framework record is a special TXT record used to store data designed to detect email spoofing. For more information about SPF records, see [RFC 4408](https://tools.ietf.org/html/rfc4408).  
SRV |  A Service Locator record allows administrators to use several servers for a single domain. For more information about SRV records, see [RFC 2782](https://tools.ietf.org/html/rfc2782).  
SSHFP |  An SSH Public Key Fingerprint record publishes SSH public host key fingerprints using the DNS. For more information about SSHFP records, see [RFC 6594](https://tools.ietf.org/html/rfc6594).  
TLSA |  A Transport Layer Security Authentication record associates a TLS server certificate, or public key, with the domain name where the record is found. This relationship is called a TLSA certificate association. For more information about TLSA records, see [RFC 6698](https://tools.ietf.org/html/rfc6698#section-2).  
TXT |  A Text record holds descriptive, human readable text, and can also include non-human readable content for specific uses. It is commonly used for SPF records and DKIM records that require non-human readable text items. For more information about TXT records, see [RFC 1035](https://tools.ietf.org/html/rfc1035#page-12)[RFC 1035](https://tools.ietf.org/html/rfc1035#page-12).  
Was this article helpful?
YesNo

