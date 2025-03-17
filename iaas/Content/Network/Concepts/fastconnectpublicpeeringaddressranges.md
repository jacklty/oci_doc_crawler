Updated 2024-10-16
# FastConnect Public Peering Advertised Routes
This topic discusses the public IP address ranges (routes) that BGP advertises to your on-premises network over FastConnect public peering (a public virtual circuit). You may need this information when configuring firewall allow lists for your on-premises network.
By default, when you connect with FastConnect to Oracle Cloud Infrastructure (OCI) in a particular region, the routes advertised over the public virtual circuit include routes for _other_ OCI regions in the same market, and for specific Oracle Cloud Infrastructure Classic regions. For more information about regions, see [About Regions and Availability Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).
If you do not own a Public ASN or Public IP Address, you might need to review this section: [To use FastConnect if you do not own a Public ASN or Public IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#public_asn_ip). 
Using [route filtering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#route_filtering) you can also choose to advertise public routes used by ephemeral IP address ranges, reserved IP address ranges, and Oracle Services Network (OSN) to your on-premises network at the _region_ , _market_ , or _global_ (all regions in all markets) scope. You can also choose to only advertise routes to OSN from the local region. The following map and tables show which regions are in the same [market](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm#FastConnect_Public_Peering_Advertised_Routes__markets) group. 
You can select route filtering options when you set up a FastConnect virtual circuit. The details vary depending on whether you are using a [FastConnect partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#set_up_vc), a [third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#task_set_up_vc), or [colocation](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#task_set_up_vc).
## Downloading the JSON File 🔗 
[Use this link to download the current list of all public IP ranges in all commercial regions](https://docs.oracle.com/iaas/tools/public_ip_ranges.json). This list is formatted in JSON, and provides the most current list of the actual public routes advertised by a region. If necessary, you can concatenate several regional lists into market lists.
You can poll the published file to check for new IP address ranges as frequently as every 24 hours. We recommend that you poll the published file at least weekly. More information on reading and using this JSON file is at [IP Address Ranges](https://docs.oracle.com/iaas/Content/General/Concepts/addressranges.htm).
## Security considerations for FastConnect public peering 🔗 
Always consider FastConnect public peering as an untrusted interface, and put in place firewalls and other access controls as you would for any network interface connected to the Internet.
When your on-premises network is connected to OCI using FastConnect public peering without access controls or [route filtering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#route_filtering), your on-premises network can potentially receive packets from: 
  * All VCNs in the same market in your tenancy (or tenancies, if you have more than one) with internet access
  * Any VCN resources with internet access operated by other OCI customers in the same market
  * OCI public services such as Object Storage, the Console, or APIs


When your on-premises network is connected to OCI using FastConnect public peering without access controls, your on-premises network cannot receive packets from: 
  * Routers used by other OCI customers' on-premises networks that are also connected with FastConnect public peering
  * Internet users and resources


## Markets 🔗 
Markets are groupings of OCI regions that are in the same general part of the world. The following map shows the OCI regions grouped into the four existing markets. It also indicates which regions interconnect with Azure ExpressRoute.
Regions in each market:
[![Map showing which regions are in each market.](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/network-fc-markets.svg)](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/network-fc-markets.svg)
The following table shows the OCI regions grouped into the four existing markets. If you use FastConnect public peering to connect to one of the following OCI regions, and you set [route filtering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#route_filtering) to the market scope, BGP advertises routes from the region to which you are directly connected and also the other regions in the market to your on-premises network. 
Links are also provided to lists of Oracle Cloud Infrastructure Classic regional routes that can be advertised over the public virtual circuit.
The Microsoft Logo ![Microsoft logo](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/msft-logo.svg)() shown on the map indicates regions that allow direct [Access to Microsoft Azure](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm#Access_to_Microsoft_Azure). 
Market | OCI regions in the market - region keys |  Oracle Cloud Infrastructure Classic regions in the market   
---|---|---  
Asia Pacific (APAC) |  Australia East (Sydney) - SYD Australia Southeast (Melbourne) - MEL India South (Hyderabad) - HYD India West (Mumbai) - BOM Japan Central (Osaka) - KIX Japan East (Tokyo) - NRT Singapore (Singapore) - SIN Singapore West (Singapore) - XSP South Korea Central (Seoul) - ICN South Korea North (Chuncheon) - YNY |  [Sydney-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm#oci_c_sydney)  
Europe, Middle East, Africa (EMEA) |  France Central (Paris) - CDG France South (Marseille) - MRS Germany Central (Frankfurt) - FRA Israel Central (Jerusalem) - MTZ Italy Northwest (Milan) - LIN Netherlands Northwest (Amsterdam) - AMS Saudi Arabia Central (Riyadh) - RUH Saudi Arabia West (Jeddah) - JED South Africa Central (Johannesburg) - JNB Spain Central (Madrid) - MAD Sweden Central (Stockholm) - ARN Switzerland North (Zurich) - ZRH UAE Central (Abu Dhabi) - AUH UAE East (Dubai) - DXB UK South (London) - LHR UK West (Newport) - CWL |  [Amsterdam-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm#oci_c_amsterdam) [Slough-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm#oci_c_slough)  
Serbia |  Serbia Central (Jovanovac) - BEG *   
North America (NA) |  Canada Southeast (Montreal) - YUL Canada Southeast (Toronto) - YYZ Mexico Central (Queretaro) - QRO Mexico Northeast (Monterrey) - MTY US East (Ashburn) - IAD US Midwest (Chicago) - ORD US West (Phoenix) - PHX US West (San Jose) - SJC |  [Ashburn-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm#oci_c_ashburn) [Chicago-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm#oci_c_chicago)  
Latin America Division (LAD) |  Brazil East (Sao Paulo) - GRU Brazil Southeast (Vinhedo) - VCP Chile Central (Santiago) - SCL Chile West (Valparaiso) - VAP Colombia Central (Bogota) - BOG | [Sao Paulo-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm#oci_c_sao_paulo)  
* BGP route sharing of routes in other commercial regions to on-premises networks is not available for Serbia Central (Jovanovac).  
## Oracle Cloud Infrastructure Classic Regional Routes 🔗 
[Amsterdam-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm)
  * 130.162.0.0/16
  * 132.226.0.0/16
  * 140.86.0.0/16
  * 141.145.0.0/19
  * 160.34.16.0/20
  * 160.34.120.0/24
  * 160.34.121.0/24
  * 205.223.82.0/24
  * 205.223.83.0/24


[Ashburn-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm)
  * 68.233.64.0/21
  * 68.233.72.0/21
  * 74.117.200.0/23
  * 74.117.203.0/24
  * 74.117.206.0/24
  * 129.144.0.0/16
  * 129.145.16.0/21
  * 129.145.24.0/23
  * 129.145.28.0/23
  * 129.145.39.0/24
  * 129.145.40.0/22
  * 129.149.0.0/17
  * 129.149.128.0/17
  * 129.150.0.0/15
  * 129.152.32.0/20
  * 129.152.60.0/22
  * 129.152.80.0/20
  * 129.152.128.0/17
  * 129.156.64.0/18
  * 129.157.0.0/22
  * 129.157.4.0/22
  * 129.157.8.0/21
  * 129.157.112.0/20
  * 129.157.128.0/17
  * 129.158.0.0/15
  * 129.191.0.0/16
  * 142.0.160.0/21
  * 142.0.170.0/24
  * 144.25.128.0/17
  * 160.34.0.0/20
  * 160.34.72.0/23
  * 160.34.82.0/24
  * 160.34.86.0/24
  * 160.34.88.0/23
  * 160.34.100.0/22
  * 160.34.104.0/24
  * 160.34.105.0/24
  * 160.34.107.0/24
  * 160.34.108.0/23
  * 160.34.110.0/23
  * 160.34.124.0/23
  * 192.18.192.0/23
  * 199.167.172.0/24
  * 208.72.89.0/24
  * 208.72.91.0/24
  * 208.72.92.0/23
  * 208.72.94.0/24


[Chicago-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm)
  * 68.233.72.0/21
  * 74.117.200.0/23
  * 74.117.203.0/24
  * 74.117.206.0/24
  * 129.145.24.0/23
  * 129.145.28.0/23
  * 129.145.39.0/24
  * 129.145.40.0/22
  * 129.149.0.0/17
  * 129.149.128.0/17
  * 129.150.0.0/15
  * 129.152.80.0/20
  * 129.152.128.0/17
  * 129.191.0.0/16
  * 160.34.0.0/20
  * 160.34.72.0/23
  * 160.34.82.0/24
  * 160.34.86.0/24
  * 160.34.88.0/23
  * 160.34.104.0/24
  * 160.34.108.0/23
  * 160.34.110.0/23
  * 199.167.172.0/24
  * 208.72.89.0/24
  * 208.72.91.0/24
  * 208.72.92.0/23
  * 208.72.94.0/24


[Sao Paulo-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm)
  * 129.91.0.0/20
  * 144.22.0.0/17


[Slough-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm)
  * 74.117.207.0/24
  * 129.152.64.0/22
  * 129.156.0.0/18
  * 141.144.0.0/16
  * 141.144.32.0/19
  * 141.145.32.0/20
  * 141.145.48.0/20
  * 141.145.82.0/23
  * 141.145.85.0/24
  * 141.145.96.0/20
  * 141.145.112.0/20
  * 144.21.0.0/16
  * 144.24.0.0/16
  * 160.34.64.0/23
  * 160.34.66.0/23
  * 160.34.78.0/24
  * 160.34.79.0/24
  * 160.34.87.0/24
  * 160.34.122.0/24
  * 160.34.126.0/23
  * 199.167.173.0/24
  * 199.167.174.0/24
  * 199.167.175.0/24
  * 208.72.90.0/24


[Sydney-Classic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectpublicpeeringaddressranges.htm)
  * 140.238.160.0/21
  * 140.238.224.0/21
  * 140.238.240.0/20
  * 132.145.112.0/20
  * 140.238.32.0/20
  * 140.238.48.0/20
  * 132.145.80.0/20
  * 140.238.0.0/20
  * 140.204.4.0/23
  * 192.29.48.0/22
  * 192.29.160.0/21
  * 134.70.80.0/22
  * 140.91.32.0/23
  * 140.204.8.0/23
  * 192.29.36.0/22
  * 134.70.96.0/22
  * 140.91.40.0/23
  * 140.204.24.0/23
  * 192.29.20.0/22
  * 134.70.76.0/23
  * 134.70.78.0/23
  * 140.204.4.0/23
  * 140.204.6.0/23
  * 132.145.116.0/22
  * 132.145.120.0/21
  * 134.70.82.0/23
  * 140.204.8.0/23
  * 140.204.10.0/23
  * 158.101.128.0/19
  * 158.101.128.0/20
  * 192.29.32.0/20
  * 192.29.32.0/22
  * 132.145.84.0/22
  * 132.145.88.0/21
  * 134.70.98.0/23
  * 140.204.24.0/23
  * 140.204.26.0/23
  * 140.238.0.0/20
  * 192.29.16.0/22
  * 140.204.20.0/23
  * 129.91.16.0/21
  * 129.91.176.0/20
  * 129.154.0.0/16
  * 129.154.0.0/24
  * 129.154.2.0/24
  * 160.34.48.0/20
  * 160.34.74.0/23
  * 160.34.83.0/24
  * 160.34.112.0/24
  * 160.34.113.0/24
  * 205.223.86.0/23
  * 205.223.86.0/24
  * 205.223.87.0/24


Was this article helpful?
YesNo

