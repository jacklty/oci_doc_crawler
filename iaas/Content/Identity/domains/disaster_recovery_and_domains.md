Updated 2025-02-03
# Disaster Recovery and Identity Domains
A disaster can be any event that puts applications at risk, for example failures caused by natural disasters. In regions with cross-region disaster recovery (DR) enabled, identity domains have built-in cross-region DR to minimize data loss. Data for a region is replicated to a nearby region in the event of a disaster. If an entire OCI region becomes unavailable, traffic is routed to the disaster recovery region to speed service recovery and retain as much data as possible. Oracle pairs regions with disaster recovery (DR) regions for you.
See [Learn about protecting your cloud topology against disasters](https://docs.oracle.com/en/solutions/design-dr/index.html) to learn more about DR in Oracle Cloud Infrastructure.
If a region outage occurs, the identity domain will experience a brief outage and then recover. After recovered to the DR region: 
  * Users in the identity domain are authenticated and authorized as usual.
  * Identity domain URLs don't change. No changes are needed for any applications.
  * Failed-over identity domains don't replicate to replicated regions.
  * Identity domains replicated to other regions might not be in sync with the DR region. For example, any changes to users, groups, and domain settings might not be reflected in the DR region. Inconsistencies are resolved when the identity domain fails back.


## Accessing the DR Region
Use these steps to confirm that the network can reach the DR region.
  1. Find the DR region identifier in the DR Region Pairings table, See [Disaster Recovery Region Pairings](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/disaster_recovery_and_domains.htm#disaster_recovery_region_pairings "Use the following table to find the DR region pairings in the Oracle Cloud Infrastructure commercial realm:"). 
  2. Use the DR region identifier to look up the public IP addresses assigned to the region. See [Public IP Addresses for VCNs and the Oracle Services Network](https://docs.oracle.com/iaas/tools/public_ip_ranges.json).
  3. Add those public IP addresses to your firewalls to allow traffic from that DR region.


**Note**
For complete disaster recovery functionality, we recommend subscribing a tenancy to its DR region pairing. Replicate the tenancy's domains to the DR region. This all IAM principal-based authentication while the home region is down.
To edit an existing identity domain, see [Editing an Identity Domain's Details](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-edit-domain-details.htm#edit-identity-domain "You can edit details for an identity domain in IAM. For example, you can select whether to show the identity domain on the sign-in page or upgrade a domain by changing the domain type.").
To create a new identity domain, see [Creating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm#create-identity-domain "To create an identity domain in IAM, administrators need to know which identity domain type they want to create, in which compartment to create it, and the new identity domain administrator's sign-in credentials, if needed. The domain types that you're allowed to create are based on your subscription.").
To view the disaster recovery region pairings, see [Disaster Recovery Region Pairings](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/disaster_recovery_and_domains.htm#disaster_recovery_region_pairings "Use the following table to find the DR region pairings in the Oracle Cloud Infrastructure commercial realm:").
## Read-only Failover and Identity Domains 🔗 
If a region outage occurs, OCI might initiate a failover of that region's identity domains (and IDCS stripes) to a failover region which restores access to those identity domains (and IDCS stripes) in a read-only access mode. Check the outage information for when the region-outage state is enabled & disabled.
In read-only access mode: 
  1. Resources can't be updated. No updates to any identity domain (or IDCS stripe) resources are allowed. For example, users can't update or delete users, applications, groups, or domain settings. Users have read permissions to all resources.
  2. Users can't change their passwords. If a user is in the force password reset state, they can't reset their password and don't have access until the region outage has been mitigated.
  3. Users with multifactor authentication can sign-in while the identity domain is in read-only mode.
  4. Applications using the identity domain can authenticate and authorize. For example, a custom application can authenticate and authorize calls using the identity domain while in read-only mode.
**Note** See [Disaster Recovery Region Pairings](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/disaster_recovery_and_domains.htm#disaster_recovery_region_pairings "Use the following table to find the DR region pairings in the Oracle Cloud Infrastructure commercial realm:").


## Disaster Recovery Region Pairings 🔗 
Use the following table to find the DR region pairings in the Oracle Cloud Infrastructure commercial realm:
See [Oracle Cloud Regions—Data Centers](https://www.oracle.com/cloud/architecture-and-regions/) for information about available regions.
Region Name | Region Identifier | Region Location | Disaster Recovery Region Name | Disaster Recovery Region Identifier  
---|---|---|---|---  
Australia East (Sydney) | ap-sydney-1 | Sydney, Australia | Australia Southeast (Melbourne) | ap-melbourne-1  
Australia Southeast (Melbourne)  | ap-melbourne-1  | Melbourne, Australia | Australia East (Sydney)  | ap-sydney-1   
Brazil East (Sao Paulo)  | sa-saopaulo-1  | Sao Paulo, Brazil | Brazil Southeast (Vinhedo)  | sa-vinhedo-1   
Brazil Southeast (Vinhedo)  | sa-vinhedo-1  | Vinhedo, Brazil | Brazil East (Sao Paulo)  | sa-saopaulo-1   
Canada Southeast (Montreal)  | ca-montreal-1  | Montreal, Canada | Canada Southeast (Toronto)  | ca-toronto-1   
Canada Southeast (Toronto)  | ca-toronto-1  | Toronto, Canada | Canada Southeast (Montreal)  | ca-montreal-1   
Chile Central (Santiago)  | sa-santiago-1  | Santiago, Chile | Chile West (Valparaiso) | sa-valparaiso-1  
Chile West (Valparaiso) | sa-valparaiso-1 | Valparaiso, Chile | Chile Central (Santiago) | sa-santiago-1  
France South (Marseille) | eu-marseille-1 | France South (Marseille) | Paris (France) | eu-paris-1  
Germany Central (Frankfurt)  | eu-frankfurt-1  | Frankfurt, Germany | Netherlands Northwest (Amsterdam)  | eu-amsterdam-1   
Netherlands Northwest (Amsterdam)  | eu-amsterdam-1  | Amsterdam, Netherlands | Germany Central (Frankfurt)  | eu-frankfurt-1   
India South (Hyderabad)  | ap-hyderabad-1  | Hyderabad, India | India West (Mumbai)  | ap-mumbai-1   
India West (Mumbai)  | ap-mumbai-1  | Mumbai, India | India South (Hyderabad)  | ap-hyderabad-1   
Italy Northwest (Milan)  | eu-milan-1  | Milan, Italy | France South (Marseille)  | eu-marseille-1   
Japan Central (Osaka)  | ap-osaka-1  | Osaka, Japan | Japan East (Tokyo)  | ap-tokyo-1   
Japan East (Tokyo)  | ap-tokyo-1  | Tokyo, Japan | Japan Central (Osaka)  | ap-osaka-1   
Saudi Arabia West (Jeddah)  | me-jeddah-1  | Saudi Arabia West (Jeddah)  | Saudi Arabia Central (Riyadh) | me-riyadh-1  
Singapore (Singapore)  | ap-singapore-1  | Singapore West (Singapore) | Singapore West (Singapore)  | ap-singapore-2  
South Korea Central (Seoul)  | ap-seoul-1  | Seoul, South Korea | South Korea North (Chuncheon)  | ap-chuncheon-1   
South Korea North (Chuncheon)  | ap-chuncheon-1  | Chuncheon, South Korea | South Korea Central (Seoul)  | ap-seoul-1   
Sweden Central (Stockholm)  | eu-stockholm-1  | Sweden Central (Stockholm) | Italy Northwest (Milan) | eu-milan-1  
Switzerland North (Zurich)  | eu-zurich-1  | Zurich, Switzerland | Germany Central (Frankfurt)  | eu-frankfurt-1   
UAE Central (Abu Dhabi)  | me-abudhabi-1  | Abu Dhabi, UAE | UAE East (Dubai)  | me-dubai-1   
UAE East (Dubai)  | me-dubai-1  | Dubai, UAE | UAE Central (Abu Dhabi)  | me-abudhabi-1   
UK South (London)  | uk-london-1  | London, United Kingdom | UK West (Newport)  | uk-cardiff-1   
UK West (Newport)  | uk-cardiff-1  | Newport, United Kingdom | UK South (London)  | uk-london-1   
US East (Ashburn)  | us-ashburn-1  | Ashburn, VA | US West (Phoenix)  | us-phoenix-1   
US Midwest (Chicago) | us-chicago-1 | US Midwest (Chicago) | US West (Phoenix) | us-phoenix-1  
US West (Phoenix)  | us-phoenix-1  | Phoenix, AZ  | US East (Ashburn)  | us-ashburn-1   
US West (San Jose)  | us-sanjose-1  | San Jose, CA  | US West (Phoenix)  | us-phoenix-1   
Was this article helpful?
YesNo

