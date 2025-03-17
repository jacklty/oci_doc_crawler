Updated 2025-02-21
# Bring Your Own ASN
Bring your own Autonomous System Number (ASN) to Oracle Cloud Infrastructure and use your existing ASN within the OCI environment.
ASN is a unique number assigned to a network over the internet enabling different networks to exchange routing information with each other using the Border Gateway Protocol (BGP). ASN is also used for security policies to identify network traffic source, enabling you to filter traffic based on the originating network. 
As you Bring Your Own IP Addresses (BYOIP) to OCI for seamless workload migration, Bringing Your Own ASN (BYOASN) to OCI avoids the need to reconfigure IP address based access policies and other time-consuming tasks.
Use BYOASN to import your ASN into OCI, associate it with your BYOIP CIDRs (IPv4/IPv6) and advertise the IPv4 or IPv6 addresses with your own ASN instead of the OCI ASN. Traffic originating from OCI as source carries your ASN instead of the OCI ASN. Routes advertised for OCI BYOIP prefixes also carries your ASN instead of OCI ASN enabling OCI BYOIP prefixes to be accepted by the locations that check for both ASN and IP addresses. You can also dynamically change the association between your BYOIP and BYOASN without withdrawing prefix advertisement.
## Requirements and Preparation 🔗 
Before you begin, ensure that:
  * You have completed the prerequisites listed for [BYOIP](https://docs.oracle.com/iaas/Content/Network/Concepts/BYOIP.htm#BYOIP__requirements). 
  * You have brought in your IP addresses using [BYOIP](https://docs.oracle.com/iaas/Content/Network/Concepts/BYOIP.htm).
  * You have ownership of the ASN that you want to import into Oracle Cloud.
  * You have the Route Origin Authorization (ROA) validation for your ASN and CIDR prefix you plan to associate with your ASN.


**Warning**
For a given prefix, OCI creates the route objects in RADB using OCI ASN. When subsequent ASNs are associated with the prefix, they're added to the AS-SET. OCI doesn't update your ASN as the origin ASN in RADB. This should work based on our knowledge with most transit providers. However, if you work with providers who enforce a strict check, update the RADB with your ASN as the origin ASN.
**Note** Be aware of potential 24-hour propagation delays as some providers may take up to 24 hours to update their routing tables. As a result, the prefix with your ASN may not be immediately reachable after being advertised by OCI.
**Note** When you associate an ASN with a BYOIP prefix, it will appear as the origin ASN and will be prepended to OCI ASN, which will then appear as a transit ASN in the AS path.
Was this article helpful?
YesNo

