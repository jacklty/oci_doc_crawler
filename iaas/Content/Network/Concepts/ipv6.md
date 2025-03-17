Updated 2025-02-28
# IPv6 Addresses
This topic describes support for IPv6 addressing in a VCN.
## Highlights 🔗 
  * IPv6 addressing is supported for all commercial and government regions.
  * During VCN creation, you select whether the VCN is enabled for IPv6, or you can enable IPv6 on existing IPv4-only VCNs. You also select whether each subnet in an IPv6-enabled VCN is enabled for IPv6. 
  * IPv6-enabled VCNs can use a /56 IPv6 global unicast address (GUA) prefix allocated by Oracle, specify a /64 or larger [Unique Local Address](https://datatracker.ietf.org/doc/html/rfc4193/) (ULA) prefix, or import a /48 or larger BYOIPv6 prefix. 
  * An Oracle-assigned /56 prefix can be _globally routable_ to the VCN for internet communication, depending on whether the subnet using a /64 part of the prefix is public or private. A ULA prefix is _not globally routable_ for internet communication. 
  * All IPv6 enabled subnets are /64. You can either allow or prohibit internet communication to a subnet by specifying the "public/private" subnet-level flag. 
  * If you use [BYOIP](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/BYOIP.htm#BYOIP "Oracle Cloud Infrastructure allows you to Bring Your Own IP \(BYOIP\) address space to use with resources in Oracle Cloud Infrastructure, in addition to using Oracle owned addresses."), you can import a /48 or larger IPv6 GUA prefix and must assign a /64 prefix or larger to a VCN.
  * You select whether a specific VNIC in an IPv6-enabled subnet has IPv6 addresses (up to 32 maximum per VNIC).
  * Only these Networking gateways support IPv6 traffic: **Dynamic Routing Gateway (DRG)** , **local peering gateway (LPG)** , and **internet gateway**. 
  * Both inbound- and outbound-initiated IPv6 connections are supported between a VCN and the internet, and between a VCN and an on-premises network. Communication between resources within a VCN or between VCNs is also supported.
  * IPv6 traffic between resources within a region (within and between VCNs) is supported. See other important details in [Routing for IPv6 Traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#routing) and [Internet Communication](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#overview__internet_comm).
  * Both FastConnect and Site-to-Site VPN support IPv6 traffic between a VCN and on-premises network. You must configure FastConnect or Site-to-Site VPN for IPv6.
  * IPv6 addresses support optional association with a custom route table (see [Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing)).


## Overview of IPv6 Addresses 🔗 
Oracle VCNs support IPv4-only addressing and dual-stack IPv4 and IPv6 addressing. Every VCN always has at least one private IPv4 CIDR, and you can enable IPv6 during VCN creation. You can also add an IPv6 prefix to an IPv4-only VCN while enabling IPv6. When IPv6 is enabled for a VCN, while creating a subnet of that VCN you can enable it to also have IPv4 addresses only or both IPv4 and IPv6 addresses. Therefore a VCN can have a mix of IPv4-only subnets and subnets that have both IPv4 and IPv6.
When you create a Compute instance, you can add one or more IPv6 addresses to the VNIC. These IP addresses can be assigned from several IPv6 prefixes if they're assigned to the subnet. You can remove an IPv6 address from a VNIC at any time.
### IPv6 Prefixes Assigned to an IPv6-Enabled VCN 🔗 
An IPv6-enabled VCN is dual-stack, meaning it has both an IPv4 CIDR and an IPv6 prefix assigned. A VCN can have up to five IPv4 CIDRs and up to five IPv6 prefixes. An IPv6-enabled VCN can use an Oracle-allocated /56 Global Unicast Address (GUA), let you import and assign a BYOIPv6 prefix, or specify a Unique Local Address (ULA) prefix. Oracle can allocate a GUA IPv6 prefix, also referred to here as a globally routable IPv6 prefix. You can also use Bring Your Own IP (BYOIP) to use a /48 prefix. Both ULA and BYOIPv6 prefixes must be at minimum /64 in size when assigned to a VCN. The following table summarizes the options.
IPv4 or IPv6 | Use and Size | Who Assigns the Address Block | Allowed Values  
---|---|---|---  
Private IPv4 CIDR |  Private communication /16 to /30 | You | Typically RFC 1918 range  
Globally routable IPv6 prefix  |  Internet or Private Communication  /56  |  Oracle |  Oracle allocates the IPv6 prefix.  
BYOIP IPv6 prefix  |  Internet or Private Communication  /64 (minimum) | You |  IPv6 GUA are always in the range of 2000::/3.   
IPv6 ULA |  Private Communication  /64 (minimum)  |  You |  This address type can be in the fc00::/7 ULA range or 2000:/3 GUA range. We recommend you assign ULA prefixes from the fd00 half of the range.  
**Note**
IPv6 ULA addresses allocated to VCNs are only used for internal communications even if the addresses are in the GUA range. OCI doesn't advertise the prefixes to the internet, nor route traffic between these internal prefixes and the internet.
Unique Local Addresses are globally unique addresses that allow communication between nodes on different links within the same site or between sites. They're administratively segmented and aren't for routing on the Internet. [RFC 4193](https://tools.ietf.org/html/rfc4193) provides more information about ULAs. 
### Internet Communication 🔗 
When you enable IPv6 in a VCN, you can decide which types of IPv6 addresses are assigned: Oracle-allocated, BYOIPv6, or ULA. You can then enable IPv6 in subnets (see [Task 2: Create a regional IPv6-enabled public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#task2_create_subnet)) and assign IPv6 addresses to an individual instance's VNICs or load balancers if they were created in an IPv6-enabled subnet with an IPv6 prefix. You can also decide whether internet communication with IPv6-enabled resources is allowed or prohibited by specifying the subnet is public or private. If an IPv6-enabled resource is assigned a GUA address and is hosted in a public subnet, communication to and from the internet is allowed. If an IPv6-enabled resource is hosted in a private subnet, communication to and from the internet is prohibited even if the resource has a GUA address assigned. 
### Assignment of IPv6 Addresses to a VNIC 🔗 
To enable IPv6 for a particular VNIC, [assign an IPv6 to the VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#assign_ipv6). IP addresses can be assigned from several IPv6 prefixes if they're assigned to the subnet. As with IPv4, when assigning an IPv6 address, you can specify the particular address you want to use, or let Oracle select one for you.
A VNIC can have an IPv6 address assigned at Compute instance creation, or you can add one after you create the instance. 
A VNIC can use IPv6-only addressing, if the OS image you selected for the Compute instance supports IPv6-only addressing and the subnet is configured to only use IPv6 addressing.
You can [ move an IPv6 address from one VNIC to another in the same subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#move_ipv6).
### Format of IPv6 Addresses 🔗 
IPv6 addresses have 128 bits.
An IPv6 prefix block for a VCN must be /56 in size. The leftmost 56 bits identify the VCN part of the address. For example:
2001:0db8:0123:7800::/56 (or fd00::/56 for [ULA](https://tools.ietf.org/html/rfc4193) addresses)
An IPv6 prefix block for a subnet must be /64 in size. The rightmost 16 bits in a subnet's prefix identify the subnet part of the address. In the following example, the 7811 is the unique part for the subnet:
2001:0db8:0123:7811::/64 
In the following ULA example, the 11 is the unique part for the subnet:
fd00:0:0:11::/64 
The right-most 64 bits of an IPv6 address identify the unique part specific to the particular IPv6 address. For example:
2001:0db8:0123:7811:abcd:ef01:2345:6789
When you assign an IPv6 to a VNIC, you can specify which specific IPv6 address to use (those 64 bits). 
[Example of Enabling IPv6 in a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
In this example, Oracle assigns this prefix: 2001:0db8:0123: 7811::/56. 
The following diagram illustrates the VCN and includes two subnets: public subnet 1111 and private subnet 1112.
[![This image shows an example of IPv4 and IPv6 addresses used in a VCN with an Oracle-provided IPv6 prefix.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_ipv6_oracle_cidr.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_ipv6_oracle_cidr.svg)
Access to the internet is usually decided at the subnet level, not at the VNIC level.
VNIC 1 in Subnet 1111 has a primary private IPv4 address (10.0.1.4) with an optional IPv6 address assigned. VNIC 1 has a secondary private IPv4 address (10.0.1.5), also with an optional public IP address assigned. 
Because Subnet 1111 has internet access enabled it can only have an internet-routable IPv6 address, which is 2001:0db8:0123:7811:abcd:ef01:2345:0006.
Subnet 1112 is private, which means the VNICs don't have IPv4 or IPv6 access from the internet. The instance using VNIC 2 can still initiate contact with other hosts on the internet and get responses, but doesn't get uninitiated requests.
## Routing for IPv6 Traffic 🔗 
Both inbound- and outbound-initiated IPv6 connections are supported between a VCN and the internet, and between a VCN and an on-premises network. Communication between resources within a VCN or between VCNs is also supported.
Here are other important details about routing of IPv6 traffic:
  * IPv6 traffic is supported only through these gateways:
    * [Dynamic routing gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs): For access to an on-premises network or other networks outside the region (using [remote peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions)). Both Oracle Cloud Infrastructure [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") and [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") support IPv6 traffic. For more details about IPv6 configuration, see the upcoming sections.
    * [Internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway): For access to the internet.
    * [Local peering gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region): For connecting two VCNs in the same region so that their resources can communicate using private IP addresses without routing the traffic over the internet or through an on-premises network. 
  * IPv6 traffic between resources within a region (within and between VCNs) is supported. VCNs are dual-stack, meaning they always support IPv4 and can optionally also support IPv6. A VCN's route tables support both IPv4 and IPv6 rules in the same table. IPv4 and IPv6 rules must be discretely specified. Rules to route traffic that match a certain IPv6 prefix to the VCN's attached DRG, internet gateway, local peering gateway, or an IPv6 address (next hop) are supported. 


### VCN Route Tables and IPv6 🔗 
The VCN's [route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) support both IPv4 rules and IPv6 rules that use a DRG, local peering gateway, or internet gateway as the target. For example, the route table for a particular subnet could have these rules:
  * Rule to route traffic that matches a certain IPv4 CIDR to the VCN's attached DRG
  * Rule to route traffic that matches a certain IPv4 CIDR to the VCN's service gateway
  * Rule to route traffic that matches a certain IPv4 CIDR to the VCN's NAT gateway
  * Rule to route traffic that matches a certain **IPv6** prefix to the VCN's attached DRG
  * Rule to route traffic that matches a certain **IPv6** prefix to the VCN's attached internet gateway


## Security Rules for IPv6 Traffic 🔗 
The VCN's [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) and [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) support both IPv4 and IPv6 [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules). For example, a network security group or security list could have these security rules:
  * Rule to allow SSH traffic from the on-premises network's IPv4 CIDR
  * Rule to allow ping traffic from the on-premises network's IPv4 CIDR
  * Rule to allow SSH traffic from the on-premises network's **IPv6** prefix
  * Rule to allow ping traffic from the on-premises network's **IPv6** prefix


The [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) in an IPv6-enabled VCN includes default IPv4 rules and the following default IPv6 rules: 
  * **Stateful ingress:** Allow IPv6 TCP traffic on destination port 22 (SSH) from source ::/0 and any source port. This rule makes it easy for you to create a VCN with a public subnet and internet gateway, create a Linux instance, add an internet-access-enabled IPv6, and then immediately connect with SSH to that instance without needing to write any security rules yourself. 
**Important**
The default security list doesn't include a rule to allow Remote Desktop Protocol (RDP) access. If you're using [Windows images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm), add a stateful ingress rule for TCP traffic on destination port 3389 from source ::/0 and any source port.
See [To enable RDP access](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm#prerequisites__enablerdp) for more information.
  * **Stateful ingress:** Allow ICMPv6 traffic type 2 code 0 (Packet Too Big) from source ::/0 and any source port. This rule lets instances to receive Path MTU Discovery fragmentation messages.
  * **Stateful egress:** Choosing to allow all IPv6 traffic lets instances initiate IPv6 traffic of any kind to any destination. Notice that instances with an internet-access-enabled IPv6 can talk to any internet IPv6 address if the VCN has a configured internet gateway. And because stateful security rules use connection tracking, the response traffic is automatically allowed regardless of any ingress rules. For more information, see [Stateful Versus Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful).


## FastConnect and IPv6 🔗 
If you use **FastConnect** , you can configure it so that on-premises hosts with IPv6 addresses can communicate with an IPv6-enabled VCN. In general, you must ensure that the FastConnect virtual circuit has IPv6 BGP addresses, and update the VCN's routing and security rules for IPv6 traffic. 
### About the IPv6 BGP Addresses 🔗 
A FastConnect virtual circuit always requires IPv4 BGP addresses, but IPv6 BGP addresses are optional and only required for IPv6 traffic. Depending on how you're using FastConnect, you might be asked to provide the virtual circuit's BGP addresses yourself (both IPv4 and IPv6).
The addresses consist of a pair: one for the on-premises end of the BGP session, and another for the Oracle end of the BGP session.
When you specify a BGP address pair, you must include a subnet mask that contains both of the addresses. For IPv6, the allowed subnet masks are: 
  * /64
  * /96
  * /126
  * /127


For example, you could specify 2001:db8::6/64 for the address at the on-premises end of the BGP session, and 2001:db8::7/64 for the Oracle end. 
### Process to Enable IPv6 🔗 
In general, here's how to enable IPv6 for a FastConnect virtual circuit:
  * **Virtual circuit BGP:** Ensure the FastConnect virtual circuit has IPv6 BGP addresses. If you're responsible for providing the BGP IP addresses, when you set up a new virtual circuit or edit an existing one, the Console has a place for the two IPv4 BGP addresses. The Console also has a separate checkbox for **Enable IPv6 Address Assignment** and a place to provide the two IPv6 addresses. If you're editing an existing virtual circuit to add support for IPv6, it goes down while being reprovisioned to use the new BGP information.
  * **VCN route tables:** For each IPv6-enabled subnet in the VCN, update its [route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) to include rules that route the IPv6 traffic from the VCN to the IPv6 subnets in an on-premises network. For example, the **Destination CIDR Block** for a route rule would be an IPv6 subnet in an on-premises network, and the **Target** would be the **Dynamic Routing Gateway (DRG)** attached to the IPv6-enabled VCN.
  * **VCN security rules:** For each IPv6-enabled subnet in the VCN, update its security lists or relevant network security groups to allow IPv6 traffic between the VCN and an on-premises network. See [Security Rules for IPv6 Traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#security_lists).


If you don't already have a FastConnect connection, see these topics to get started:
  * [FastConnect Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#FastConnect_Overview)
  * [FastConnect Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#FastConnect_Requirements "This topic covers the requirements for implementing FastConnect.")


## Site-to-Site VPN and IPv6 🔗 
If you use [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\)."), you can configure it so that on-premises hosts with IPv6 addresses can communicate with an IPv6-enabled VCN. Here's how to enable IPv6 for the connection:
  * **IPSec connection static routes:** Configure the IPSec connection with the IPv6 static routes of an on-premises network.
  * **VCN route tables:** For each IPv6-enabled subnet in the VCN, update its [route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) to include rules that route the IPv6 traffic from the VCN to the IPv6 subnets in an on-premises network. For example, the **Destination CIDR Block** for a route rule would be an IPv6 static route for an on-premises network, and the **Target** would be the **Dynamic Routing Gateway (DRG)** attached to the IPv6-enabled VCN.
  * **VCN security rules:** For each IPv6-enabled subnet in the VCN, update its security lists or relevant network security groups to allow the wanted IPv6 traffic between the VCN and an on-premises network. See [Security Rules for IPv6 Traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#security_lists).


If you have an existing Site-to-Site VPN IPSec connection that uses static routing, you can update the list of static routes to include ones for IPv6. Changing the list of static routes causes Site-to-Site VPN to go down while being reprovisioned. See [Changing the Static Routes](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_static_route).
If you don't yet have Site-to-Site VPN, see these topics to get started:
  * [Site-to-Site VPN Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#top)
  * [Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Setting_Up_VPN)
  * [Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#Working_with_VPN_Connect)


## DHCPv6 🔗 
DHCPv6 automatic configuration of IP addresses is supported. You don't need to statically configure any IPv6 address. 
## DNS 🔗 
The VCN's [Internet Resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network) supports IPv6, which means resources in a VCN can resolve IPv6 addresses of hosts outside the VCN. Assignment of a hostname to an IPv6 address isn't supported.
## Load Balancers 🔗 
When you create a [load balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm), you can decide to have an IPv4-only or IPv4 and IPv6 dual-stack configuration. When you use the dual-stack option, the Load Balancer service assigns both an IPv4 and an IPv6 address to the Load Balancer. The Load Balancer receives client traffic sent to the assigned IPv6 address. The Load Balancer uses only IPv4 addresses to communicate with backend servers. IPv6 communication between the Load Balancer and the backend servers isn't supported.
IPv6 address assignment occurs only at Load Balancer creation. You can't assign an IPv6 address to an existing Load Balancer.
## Comparison of IPv4 and IPv6 for A VCN 🔗 
The following table summarizes the differences between IPv4 and IPv6 addressing in a VCN.
Characteristic | IPv4 | IPv6  
---|---|---  
Addressing type supported | IPv4 addressing is always required, regardless of whether IPv6 is enabled. This can be a private IPv4 CIDR. | IPv6 addressing is optional per VCN, optional per subnet in an IPv6-enabled VCN, and optional per VNIC in an IPv6-enabled subnet. An IPv6-only subnet or VNIC is allowed.  
Supported traffic types | IPv4 traffic is supported for all gateways. IPv4 traffic between instances within the VCN is supported (east/west traffic). | IPv6 traffic is supported only with these gateways: internet gateway, local peering gateway, and DRG. Both inbound- and outbound-initiated IPv6 connections are supported between a VCN and the internet, and between a VCN and an on-premises network. IPv6 traffic between resources within a region (within or between VCNs) is fully supported (east/west traffic). Also see [Routing for IPv6 Traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#routing).  
VCN size | /16 to /30 |  Oracle GUA: /56 only BYOIPv6: /64 or larger ULA: /64 or larger  
Subnet size | /16 to /30, with 3 addresses reserved in each subnet by Oracle (first 2 and last 1). | /64 only, with 8 addresses in the subnet reserved by Oracle (first 4 and last 4).  
Private and public IP address space |  Private: A VCN's private IPv4 CIDR can be from an RFC 1918 range or a publicly routable range (treated as private). You specify the range, unless you use the Console's VCN creation workflow, which always uses 10.0.0.0/16.  Public: The VCN doesn't have a dedicated public IPv4 address space. Oracle chooses any public addresses in a VCN. |  Unlike with IPv4, a VCN can receive an allocated /56 GUA prefix from Oracle or import and assign a BYOIP prefix. Either of these can be internet routable if assigned to resources in public subnets. You also have an option to assign ULA addresses, which aren't internet routable, regardless of whether the subnet is public or private.  
IP address assignment |  Private: Each VNIC gets a private IPv4 address. You can select the address or let Oracle select it.  Public: You decide whether the private IPv4 address has a public IP address associated with it (assuming the VNIC is in a public subnet). Oracle chooses the public IP address.  From an API standpoint: the `PrivateIp` object is separate from the `PublicIp` object. You can remove the public IP address from the private IPv4 address at any time.  |  You might assign IPv6 addresses from distinct prefixes to a VNIC if they're assigned to the subnet. You can select the IPv6 address or let Oracle select it. From an API standpoint: IP addresses are included in the `Ipv6` object and the distinction between public and private is controlled using the public/private subnet flag.  
Internet access  | You control whether a subnet is public or private. You add or remove a public IP address from a private IPv4 address on a VNIC (assuming the VNIC is in a public subnet). | You control whether a subnet is public or private. You don't add or remove a public IP address to or from the VNIC as you do with IPv4. Instead you enable or disable the internet access for all IPv6-enabled resources in the subnet using the public/private subnet flag.  
Primary and secondary labels | Each VNIC automatically has a primary private IP address, and you can assign up to 32 secondary private IPs per VNIC.  | You can decide to add an IPv6 address to a VNIC, with no _primary_ or _secondary_ label. You can assign up to 32 IPv6 addresses per VNIC.   
Hostnames | You can assign hostnames to IPv4 addresses.  | You can't assign hostnames to IPv6 addresses.   
Route rule limits | See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#network_limits). | IPv4 and IPv6 route rules can reside together in the same route table. IPv6 route rules can target only an internet gateway, local peering gateway, or DRG. Limit on number of IPv6 route rules in a route table: 50.  
Security rule limits | See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#network_limits). | IPv4 and IPv6 security rules can reside together in same network security group or security list. IPv6 security rules can use only IPv6 prefix ranges for source or destination, and not a service prefix label used for a service gateway. Limit on number of IPv6 security rules in a security list: 50 ingress and 50 egress. Limit on number of IPv6 security rules in a network security group: 16 total.  
Reserved public IP addresses | Supported. | Not supported.  
Regional or AD-specific | Primary private IPv4 addresses are **AD** -specific. Secondary private IPv4 addresses are AD-specific unless assigned to a VNIC in a regional subnet. Public IP addresses can be AD-specific or regional depending on the type (ephemeral or reserved). See [Public IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#Public_IP_Addresses). | IPv6 addresses are regional.  
## Setting Up an IPv6-Enabled VCN with Internet Access 🔗 
Use the following process to set up an IPv6-enabled VCN with internet access so you can easily create an instance and connect to it by using its globally routable IPv6 address.
[Task 1: Create the IPv6-enabled VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
  1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
  2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
  3. Select **Create Virtual Cloud Network**.
  4. Enter the following:
     * **Name:** A descriptive name for the VCN. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **Create in Compartment:** Leave as is. 
     * **CIDR Block:** A single, contiguous IPv4 CIDR block for the VCN. For example: 172.16.0.0/16. You _can't_ change this value later. See [Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Allowed). For reference, here's a [CIDR calculator](http://www.ipaddressguide.com/cidr).
     * **Enable IPv6 Address Assignment:** Oracle can allocate an IPv6 prefix for you, you can select a BYOIPv6 prefix you have already imported, or you can specify a ULA prefix. You _can't_ later disable IPv6 for the VCN, but you can change the IPv6 prefix or prefixes on the VCN if at least one IPv6 prefix is always assigned to the VCN. If you accept an Oracle-allocated IPv6 prefix, you receive a /56. For BYOIPv6 or ULA, specify any prefix size of /64 or larger. All IPv6-enabled subnets are /64 in size.
     * **Use DNS Hostnames in this VCN**(supported for IPv4 only): This option is required to assign DNS hostnames to hosts in the VCN, and required if you plan to use the VCN's default DNS feature (called the _Internet and VCN Resolver_). If you select this option you can specify a **DNS Label** for the VCN, or you can let the Console to generate one for you. The dialog box automatically displays the corresponding **DNS Domain Name** for the VCN (`<VCN_DNS_label>.oraclevcn.com`). For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network).
     * **Tags:** Leave as is. You can add tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  5. Select **Create Virtual Cloud Network**.
The VCN is then created and displayed on the **Virtual Cloud Networks** page in the compartment you chose. 


[Task 2: Create a regional IPv6-enabled public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
  1. While still viewing the VCN, select **Create Subnet**.
  2. Enter the following:
     * **Name:** A descriptive name for the subnet (for example, Regional Public Subnet). It doesn't have to be unique, and you can change it later. Avoid entering confidential information.
     * **Regional or Availability Domain-specific subnet:** We recommend creating only [regional subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview "Learn about virtual cloud networks \(VCNs\) and subnets in OCI."), which means that the subnet can contain resources in any of the region's availability domains. If you instead select **Availability Domain-Specific** , you must also specify an availability domain. This choice means that any instances or other resources later created in this subnet must also be in that availability domain. 
     * **CIDR Block:** A single, contiguous IPv4 CIDR block for the subnet (for example, 172.16.0.0/24). The address block must be within the VCN's IPv4 CIDR block and not overlap any other subnets. You _can't_ change this value later. See [Allowed VCN Size and Address Ranges](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Allowed). For reference, here's a [CIDR calculator](http://www.ipaddressguide.com/cidr).
     * **Enable IPv6 Address Assignment:** You can add and remove prefixes to an IPv6-enabled subnet. However, at least one IPv6 prefix must always remain after IPv6 has been enabled. An IPv6 enabled subnet can't become an IPv4-only subnet. The subnet can only have one IPv6 prefix. All IPv6 enabled subnets are always /64 in size. If you already assigned several IPv6 prefixes to the VCN that contains this subnet, you can select which prefix you assign to the subnet. 
       * If you have an Oracle-allocated prefix assigned to the VCN, select the checkbox and enter two hexadecimal characters (00-FF). 
       * If you assigned a BYOIPv6 or ULA prefix in the VCN, select it and specify hex characters to assign a /64 to the subnet. 
For more information about the IPv6 address format, see [Overview of IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#overview).
     * **Route Table:** Select the default route table.
     * **Private or****public subnet** : Select **Public Subnet** , which means instances in the subnet can optionally have public IPv4 addresses. Internet communication using IPv6 is allowed when GUA IPv6 addresses are assigned to resources hosted in a public subnet. For more information, see [Access to the Internet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Private).
     * **Use DNS Hostnames in this Subnet** (supported for IPv4 only): This option is available only if a DNS label was provided for the VCN when it was created. The option is required for assignment of DNS hostnames to hosts in the subnet, and also when you plan to use the VCN's default DNS feature (called the _Internet and VCN Resolver_). If you select the checkbox, you can specify a DNS label for the subnet, or let the Console generate one for you. The dialog box automatically displays the corresponding DNS domain name for the subnet as an FQDN. For more information, see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network).
     * **DHCP Options:** Select the default set of DHCP options.
     * **Security Lists:** Select the default security list.
     * **Tags:** Leave as is. You can add tags later if you want. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  3. Select **Create Subnet**.
The subnet is then created and displayed on the **Subnets** page. 


[Task 3: Create the internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
  1. Under **Resources** , select **Internet Gateways**.
  2. Select **Create Internet Gateway**.
  3. Enter the following:
     * **Name:** A descriptive name for the internet gateway. It doesn't have to be unique, and it can't be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **Create in Compartment:** Leave as is. 
     * **Tags:** Leave as is. You can add tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  4. Select **Create Internet Gateway**.
An internet gateway is created and displayed on the **Internet Gateways** page. The internet gateway is already enabled, but you must add route rules that allow IPv4 and IPv6 traffic.


[Task 4: Update the default route table to use the internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
The default route table starts out with no rules. Here you add rules that route all IPv4 and IPv6 traffic destined for addresses outside the VCN to the internet gateway. The existence of these rules also allows inbound connections to come from the internet to the subnet, through the internet gateway. You use security rules to control the _types of traffic_ that are allowed in and out of the instances in the subnet (see the next task).
No route rule is required to route traffic within the VCN.
  1. Under **Resources** , select **Route Tables**.
  2. Select the default route table to view its details.
  3. Select **Add Route Rules**.
  4. Enter the following:
     * **Target Type:** Internet Gateway
     * **Destination CIDR block:** 0.0.0.0/0 (which means that all IPv4 non-intra-VCN traffic not already covered by other rules in the route table goes to the target specified in this rule).
     * **Compartment:** The compartment with the internet gateway.
     * **Target:** The internet gateway you created.
     * **Description:** An optional description of the rule.
  5. Select **+ Additional Route Rule**.
  6. Enter the following:
     * **Target Type:** Internet Gateway
     * **Destination CIDR block:** ::/0 (for the IPv6 traffic).
     * **Compartment:** The compartment with the internet gateway.
     * **Target:** The internet gateway you created.
     * **Description:** An optional description of the rule.
  7. Select **Add Route Rules**.


The default route table now has two rules for the internet gateway, one for IPv4 traffic and one for IPv6 traffic. Because the subnet was set up to use the default route table, the resources in the subnet can now use the internet gateway. The next step is to specify the types of traffic you want to allow in and out of the instances you later create in the subnet.
[Task 5: Update the default security list (optional)](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
**Note** This task is about configuring [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) to allow traffic to and from Compute instances. Although this task uses a [security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) to implement those rules, you can also use [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) to implement security rules. 
Earlier you set up the subnet to use the VCN's [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default). This list already includes basic rules that allow essential IPv4 and IPv6 traffic. In this task, you add any _other_ security rules that allow the types of connections that the instances in the VCN need. 
For example: in a public subnet with an internet gateway, the instances you create might need to receive inbound HTTPS connections from the internet (if they're web servers). Here's how to add another rule to the default security list to enable that traffic:
  1. Under **Resources** , select **Security Lists.**
  2. Select the default security list to view its details. By default, you land on the **Ingress Rules** page. 
  3. Select **Add Ingress Rule**.
  4. To enable inbound connections for HTTPS (TCP port 443), enter the following:
     * **Stateless** : Unselected (this is a [stateful rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful))
     * **Source Type:** CIDR
     * **Source CIDR:** 0.0.0.0/0 (or ::/0 to enable IPv6 traffic with this rule)
     * **IP Protocol:** TCP
     * **Source Port Range:** All
     * **Destination Port Range** : 443
     * **Description:** An optional description of the rule.
  5. Select **Add Ingress Rule**.


**Important**
Security List Rule for Windows Instances
If you're going to create Windows instances, you need to add a security rule to enable Remote Desktop Protocol (RDP) access. RDP requires a stateful ingress rule for TCP traffic on destination port 3389 from source 0.0.0.0/0 (and a separate rule with ::/0 for IPv6 traffic) and any source port. For more information, see [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules).
For a production VCN, you typically set up one or more _custom_ security lists for each subnet. You can edit the subnet to [use different security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/change-use-securitylist.htm#change-rules-securitylist "Change which security lists are used in a particular subnet in a virtual cloud network \(VCN\)."). If you decide not to use the default security list, do so only after carefully assessing which of its default rules you want to duplicate in a custom security list. For example: the [default ICMP rules in the default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) are important for receiving connectivity messages for IPv4.
[Task 6: Create an instance](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
The next step is to create an instance in the subnet. When you create the instance, you select the **availability domain** , which VCN and subnet to use, and several other characteristics. 
Each instance automatically gets a private IPv4 address. When you create an instance in a _public subnet_ , you select whether the instance gets a public IPv4 address. A public IPv4 address isn't required for globally routable IPv6 traffic. But to connect to the instance from an IPv4 host, you _must_ give the instance a public IP address, or else you can't access them through the internet gateway. The default (for a public subnet) is for the instance to get a public IP address.
If the instance's VNIC is associated with a VCN and subnet that support IPv6 addressing, you have the choice of creating a Compute instance with IPv6 addresses assigned at instance creation or assigning IPv6 addresses some other time.
For more information and instructions, see [Launching an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
[Task 7: Add an IPv6 address to the instance](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
  1. While viewing the instance you created in the previous step, select **Attached VNICs**. 
  2. Select the name of the primary VNIC from the list of attached VNICs.
  3. Under **Resources** , select **IPv6 Addresses**.
  4. Select **Assign IPv6 Address**. 
  5. Enter the following:
     * **Prefix:** Select an IPv6 prefix from which the IPv6 address is automatically assigned (the VNIC's subnet must already be enabled to use IPv6 and have one or more IPv6 prefixes assigned). Available choices depend on what you select in **IPv6 address assignment** : 
       * **Automatically assign IPv6 addresses from prefix:** Select this option to let the Console select an available IPv6 address from an IPv6 prefix assigned to this subnet. A subnet can have more than one IPv6 prefix, and the prefixes can be one of three types: ULA, BYOIP, or Oracle-allocated. 
       * **Manually assign IPv6 addresses from prefix:** Select this option to use a specific address from an IPv6 prefix assigned to this subnet. Example: 0000:0000:1a1a:1a2b. This option is only available for IPv6-enabled subnets.
       * **Unassign if already assigned to another VNIC:** (Only available if you select **Manually assign IPv6 addresses from prefix:**) Leave this checkbox as is (cleared). Only use this option to force reassignment of an IPv6 address already assigned to another VNIC in the subnet.
     * **Route Table:** (Optional) Assign a custom route table to this IP address. See [Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing) for more details. If you use this option, remember that traffic from this IP address doesn't use the default VCN or subnet route tables.
     * **Tags:** Leave as is. You can add tags later. For more information, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
If you select **+ Another subnet prefix** you can assign more IPv6 addresses to the instance VNIC. You can assign one and only one IPv6 address to the VNIC from each IPv6 prefix (there can be several IPv6 prefixes assigned to a subnet). If this VNIC is being attached to an existing instance after its creation, remember that an instance OS needs specific configuration to use IPv6 addressing. 
  6. Select **Assign**.
The IPv6 is created and then displayed on the **IPv6 Addresses** page for the VNIC. 


[Task 8: Configure the instance's OS to use IPv6](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
You must configure the instance's OS to use the IPv6. For more information, see [Configuring an Instance OS to use IPv6](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#os_config).
Assign the IPv6 address dynamically when using Oracle Linux 8. Enabling IPv6 during the instance creation isn't supported, so you might not see the IPv6 address immediately after the instance is created. After the Compute instance is up, you can wait for the next DHCPv6 cycle to get the IPv6 address, or you can use the DHCPv6 client service to manually cycle DHCP and update with the newly added IPv6 address. To use the DHCPv6 client, enter: 
```
sudo dhclient -6 ens3
```

**Note** You might want to use the following command to start the DHCPv6 client service from the firewall-cmd daemon on the virtual machine:
```
sudo firewall-cmd --add-service=dhcpv6-client 
```

## Managing IPv6 in the Console 🔗 
This section includes basic tasks for working with IPv6-related resources.
[To create an IPv6-enabled VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
**Important** After enabling IPv6 for a VCN, you can't disable it. 
See the instructions in [Task 1: Create the IPv6-enabled VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#task1_create_vcn). 
[To create an IPv6-enabled subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
**Important** After enabling IPv6 for a subnet, you can't disable it. 
**Summary:** Creating an IPv6-enabled subnet is similar to creating an IPv4 subnet. The difference is that you must select which VCN IPv6 prefix you want to assign a /64 from and specify characters as appropriate. If selecting an Oracle-allocated prefix, you can provide 8 bits for the subnet's part of the IPv6 prefix. See [Overview of IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#overview). 
For general instructions, see [Task 2: Create a regional IPv6-enabled public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#task2_create_subnet). If you want a private subnet, select the radio button for **Private Subnet** when creating the subnet.
[To assign an IPv6 address to a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
The process for adding an IPv6 address to a VNIC is similar to adding a [secondary private IPv4 address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#overview). You can specify the particular IPv6 address to use or let Oracle select it from the subnet. For more information, see [Overview of IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#overview). After assigning the IPv6 to the VNIC, you must [configure the OS to use the IPv6](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#os_config).
  1. Assign the IPv6. For general instructions, see [Task 7: Add an IPv6 address to the instance](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#task7_add_ipv6). 
  2. Configure the OS to use the IPv6 address. For more information, see [Configuring an Instance OS to use IPv6](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#os_config).


[To move an IPv6 address to another VNIC in the subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
The process is similar to [moving a secondary private IPv4 address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm#top "Move a secondary private IP address to another VNIC in the same subnet.") from one VNIC to another (let's call them the _original VNIC_ and the _new VNIC_). You assign the IPv6 to the new VNIC, specify the IPv6 address, and select **Unassign if already assigned to another VNIC**. Oracle automatically unassigns it from original VNIC and assigns it to the new VNIC.
  1. Confirm you're viewing the compartment that contains the instance you're interested in.
  2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  3. Select the instance to view its details. 
  4. Under **Resources** , select **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed.
  5. Select the VNIC you're interested in.
  6. Under **Resources** , select **IPv6 Addresses**.
  7. Select **Assign Private IP Address**.
  8. Enter the following:
     * **IPv6 Address:** The IPv6 address that you want to move.
     * **Unassign if already assigned to another VNIC:** Select this checkbox to move the IPv6 address from the assigned VNIC.
     * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  9. Select **Assign**.


The IP address is moved from the original VNIC to the new VNIC. 
[To delete an IPv6 address from a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm)
  1. Confirm you're viewing the compartment that contains the instance you're interested in.
  2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  3. Select the instance to view its details. 
  4. Under **Resources** , select **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed.
  5. Select the VNIC you're interested in.
  6. Under **Resources** , select **IPv6 Addresses**.
  7. For the IPv6 you want to delete, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete IPv6**.
  8. Confirm when prompted. 


The IPv6 address is returned to the pool of available addresses in the subnet. 
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
IPv6 addressing uses an [Ipv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/) object with the following operations:
  * [ListIpv6s](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/ListIpv6s)
  * [GetIpv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/GetIpv6)
  * [UpdateIpv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/UpdateIpv6)
  * [CreateIpv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/CreateIpv6)
  * [DeleteIpv6](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Ipv6/DeleteIpv6)


## Configuring an Instance OS to use IPv6  🔗 
After assigning an IPv6 address to the VNIC through the Console, the associated instance OS need to learn the assigned address. DHCPv6 automatically takes care of this, but that requires you to wait for the next refresh cycle. You can require the instance's OS to immediately refresh its IPv6 address.
### Oracle Linux Configuration 🔗 
Oracle Linux 8 uses the following command to refresh an IPv6 address on an instance:
Copy
```
sudo dhclient -6 <interface>

```

**Note** The NetworkManager service in Oracle Linux 8 is enabled by default, if you use a custom image you might first need to run these commands:
Copy
```
sudo firewall-cmd --add-service=dhcpv6-client --permanent
sudo firewall-cmd --reload

```

See the [Setting Up Networking](https://docs.oracle.com/en/operating-systems/oracle-linux/8/network/) documentation for Oracle Linux 8 for more details.
If you haven't yet, ensure that the VCN's route table and security rules are configured for the wanted IPv6 traffic. See [Routing for IPv6 Traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#routing) and [Security Rules for IPv6 Traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#security_lists).
###  Windows Configuration 🔗 
You can use the following at the Windows command line or the Network Connections UI to ask the instance to refresh the IPv6 address: 
Copy
```
ipconfig /renew6
```

If you use PowerShell, you must run it as an administrator. The configuration persists through a reboot of the instance. Apply it as soon as possible after the instance is created. 
If you haven't yet, ensure that the VCN's route table and security rules are configured for the wanted IPv6 traffic. See [Routing for IPv6 Traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#routing) and [Security Rules for IPv6 Traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#security_lists).
Was this article helpful?
YesNo

