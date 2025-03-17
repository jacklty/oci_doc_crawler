Updated 2025-01-17
# NEC IX Series
This topic provides a route-based Site-to-Site VPN configuration for NEC IX Series devices. This configuration was validated using an IX3315 running Firmware Ver.10.2.16 and IX2106 running Firmware Ver.10.2.16.
**Important**
Oracle provides configuration instructions for a tested set of [vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices). Use the correct configuration for the vendor and software version. 
If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes. 
If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of [supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and consult the vendor's documentation for help.
Site-to-Site VPN provides a site-to-site IPSec connection that Oracle Cloud Infrastructure offers for connecting your on-premises network to a Virtual Cloud Network (VCN).
The following diagram shows a basic IPSec connection to Oracle Cloud Infrastructure with redundant tunnels. The IP addresses in this diagram are examples only and not for literal use.
[![This image summarizes the general layout of your on-premises network, VPN Connect IPSec tunnels, and VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_cpe_config_basic.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_cpe_config_basic.svg)
## Best Practices 🔗 
This section covers general best practices and considerations for using Site-to-Site VPN.
### Configure All Tunnels for Every IPSec Connection
Oracle deploys two IPSec headends for connections to provide high availability for mission-critical workloads. On the Oracle side, these two headends are on different routers for redundancy purposes. We recommend configuring all available tunnels for maximum redundancy. This is a key part of the "Design for Failure" philosophy.
### Have Redundant CPEs in On-Premises Network Locations
We recommend that each site that connects with IPSec to Oracle Cloud Infrastructure has redundant edge devices (also known as customer-premises equipment (CPE)). You add each CPE to the Oracle Console and create a separate IPSec connection between a **dynamic routing gateway (DRG)** and each CPE. For each IPSec connection, Oracle provisions two tunnels on geographically redundant IPSec headends. For more information, see the [Connectivity redundancy guide (PDF)](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/connectivity-redundancy-guide.pdf).
### Routing Protocol Considerations
When you create a Site-to-Site VPN IPSec connection, it has two redundant IPSec tunnels. Oracle encourages you to configure the CPE to use both tunnels (if the CPE supports it). In the past, Oracle created IPSec connections that had up to four IPSec tunnels.
The following three routing types are available, and you select the routing type separately for each tunnel in the Site-to-Site VPN:
  * **BGP dynamic routing:** The available routes are learned dynamically through BGP. The DRG dynamically learns the routes from the on-premises network. On the Oracle side, the DRG advertises the VCN's subnets. 
  * **Static routing:** When you set up the IPSec connection to the DRG, you specify the particular routes to the on-premises network that you want the VCN to know about. You also must configure the CPE device with static routes to the VCN's subnets. These routes aren't learned dynamically.
  * **Policy-based routing:** When you set up the IPSec connection to the DRG, you specify the particular routes to the on-premises network that you want the VCN to know about. You also must configure the CPE device with static routes to the VCN's subnets. These routes aren't learned dynamically. 


For more information about routing with Site-to-Site VPN, including Oracle recommendations on how to manipulate the BGP best path selection algorithm, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
### Other Important CPE Configurations
Ensure that access lists on the CPE are configured correctly to not block necessary traffic from or to Oracle Cloud Infrastructure.
If you have several tunnels up simultaneously, you might experience asymmetric routing. To account for asymmetric routing, ensure that the CPE is configured to handle traffic coming from the VCN on any of the tunnels. For example, you need to disable ICMP inspection, configure TCP state bypass . For more details about the appropriate configuration, contact the CPE vendor's support. To configure routing to be symmetric, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
## Caveats and Limitations 🔗 
This section covers general important characteristics and limitations of Site-to-Site VPN to be aware of.
### Asymmetric Routing
Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Configure firewalls with that in mind. Otherwise, ping tests or application traffic across the connection don't work reliably. 
When you use several tunnels to Oracle Cloud Infrastructure, We recommend that you configure routing to deterministically route traffic through the preferred tunnel. To use one IPSec tunnel as primary and another as backup, configure more-specific routes for the primary tunnel (BGP) and less-specific routes (summary or default route) for the backup tunnel (BGP/static). Otherwise, if you advertise the same route (for example, a default route) through all tunnels, return traffic from a VCN to an on-premises network routes to any of the available tunnels. This is because Oracle uses asymmetric routing.
For specific Oracle routing recommendations about how to force symmetric routing, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing). 
### Route-Based or Policy-Based Site-to-Site VPN
The IPSec protocol uses Security Associations (SAs) to decide how to encrypt packets. Within each SA, you define encryption domains to map a packet's source and destination IP address and protocol type to an entry in the SA database to define how to encrypt or decrypt a packet. 
**Note** Other vendors or industry documentation might use the term _proxy ID, security parameter index (SPI)_ , or _traffic selector_ when referring to SAs or encryption domains.
There are two general methods for implementing IPSec tunnels:
  * **Route-based tunnels:** Also called _next-hop-based tunnels_. A route table lookup is performed on a packet's destination IP address. If that route's egress interface is an IPSec tunnel, the packet is encrypted and sent to the other end of the tunnel. 
  * **Policy-based tunnels:** The packet's source and destination IP address and protocol are matched against a list of policy statements. If a match is found, the packet is encrypted based on the rules in that policy statement.


The Oracle Site-to-Site VPN headends use route-based tunnels but can work with policy-based tunnels with some caveats listed in the following sections. 
[Encryption domain for route-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/necixCPE.htm)
If the CPE supports route-based tunnels, use that method to configure the tunnel. This is the simplest configuration with the most interoperability with the Oracle VPN headend. 
Route-based IPSec uses an encryption domain with the following values:
  * **Source IP address:** Any (0.0.0.0/0)
  * **Destination IP address:** Any (0.0.0.0/0)
  * **Protocol:** IPv4


If you need to be more specific, you can use a single summary route for encryption domain values instead of a default route.
[Encryption domain for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/necixCPE.htm)
When you use policy-based tunnels, every policy entry (a CIDR block on one side of the IPSec connection) that you define generates an IPSec security association (SA) with every eligible entry on the other end of the tunnel. This pair is referred to as an _encryption domain_. 
In this diagram, the Oracle DRG end of the IPSec tunnel has policy entries for three IPv4 CIDR blocks and one IPv6 CIDR block. The on-premises CPE end of the tunnel has policy entries two IPv4 CIDR blocks and two IPv6 CIDR blocks. Each entry generates an encryption domain with all possible entries on the other end of the tunnel. Both sides of an SA pair must use the same version of IP. The result is a total of eight encryption domains.
[![Diagram showing several encryption domains and how to find their number.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_cross-products.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_cross-products.svg)
**Important**
If the CPE only supports policy-based tunnels, be aware of the following restrictions.
  * Site-to-Site VPN supports multiple encryption domains, but has an upper limit of 50 encryption domains.
  * If you had a situation similar to the prior example and only configured three of the six possible IPv4 encryption domains on the CPE side, the link would be listed in a "Partial UP" state because all possible encryption domains are always created on the DRG side.
  * Depending on when a tunnel was created you might not be able to edit an existing tunnel to use policy-based routing and might need to replace the tunnel with a new IPSec tunnel.
  * The CIDR blocks used on the Oracle DRG end of the tunnel can't overlap the CIDR blocks used on the on-premises CPE end of the tunnel. 
  * An encryption domain must always be between two CIDR blocks of the same IP version.


### If Your CPE Is Behind a NAT Device 🔗 
In general, the CPE IKE identifier configured on the on-premises end of the connection must match the CPE IKE identifier that Oracle is using. By default, Oracle uses the CPE's _public_ IP address, which you provide when you create the CPE object in the Oracle Console. However, if a CPE is behind a NAT device, the CPE IKE identifier configured on the on-premises end might be the CPE's _private_ IP address, as shown in the following diagram.
[![This image shows the CPE behind a NAT device, the public and private IP addresses, and the CPE IKE identifier.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_ipsec_vpn_cpe_ike_identifier.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_ipsec_vpn_cpe_ike_identifier.svg)
**Note** Some CPE platforms don't let you change the local IKE identifier. If you can't, you must change the remote IKE ID in the Oracle Console to match the CPE's local IKE ID. You can provide the value either when you set up the IPSec connection, or later, by editing the IPSec connection. Oracle expects the value to be either an IP address or a fully qualified domain name (FQDN) such as _cpe.example.com_. For instructions, see [Changing the CPE IKE Identifier That Oracle Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id).
## Supported IPSec Parameters 🔗 
For a vendor-neutral list of supported IPSec parameters for all regions, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters).
The Oracle BGP ASN for the commercial cloud realm is 31898. If you're configuring Site-to-Site VPN for the US Government Cloud, see [Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#vpn_params) and also [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn). For the United Kingdom Government Cloud, see [Regions](https://docs.oracle.com/iaas/Content/General/Concepts/govuksouth.htm#Regions).
## CPE Configuration 🔗 
**Important**
The configuration instructions in this section are provided by Oracle Cloud Infrastructure for this CPE. If you need support or further help, contact the CPE vendor's support directly.
The following figure shows the basic layout of the IPSec connection. 
[![This image summarizes the general layout of the IPSec connection and tunnels.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_configure_onpremise_router.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_configure_onpremise_router.svg)
The configuration template provided is for an IX3315 running Firmware Ver.10.2.16 or IX2106 running Firmware Ver.10.2.16 software (or later). The template provides information for each tunnel that you must configure. Oracle recommends setting up all configured tunnels for maximum redundancy.
The configuration template refers to these items that you must provide:
  * **CPE public IP address:** The internet-routable IP address that is assigned to the external interface on the CPE. You or your Oracle administrator provides this value to Oracle when creating the CPE object in the Oracle Console.
  * **Inside tunnel interface (required if using BGP):** The IP addresses for the CPE and Oracle ends of the inside tunnel interface. You provide these values when creating the IPSec connection in the Oracle Console.
  * **BGP ASN (required if using BGP):** Your BGP ASN.


In addition, you must: 
  * Configure internal routing for traffic between the CPE and your local network.
  * Ensure that you permit traffic between your NEC IX Series and your Oracle VCN.
  * Identify the IKE policy used (the following configuration template references this IKE policy as $<ikePolicy1> and $<ikePolicy2>).
  * Identify the IPSec policy used (the following configuration template references this IPSec policy as $<ipsecPolicy1> and $<ipsecPolicy2>).
  * Identify the virtual tunnel interface names used (the following configuration template references these as variables $<tunnelInterfaceNumber1> and $<tunnelInterfaceNumber2>).


**Important**
This following configuration template from Oracle Cloud Infrastructure**is a starting point for what you need to apply to your CPE.** Some of the parameters referenced in the template must be unique on the CPE, and the uniqueness can only be determined by accessing the CPE. Ensure the parameters are valid on your CPE and do not overwrite any previously configured values. In particular, ensure these values are unique:
  * Policy names or numbers
  * Interface names
  * Access list numbers (if applicable)


To find parameters that you must define before applying the configuration, search for the keyword `USER_DEFINED` in the template.
### About Using IKEv2
Oracle supports Internet Key Exchange version 1 (IKEv1) and version 2 (IKEv2). If you [configure the IPSec connection in the Console to use IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#using_ikev2), you must configure your CPE to use only IKEv2 and related IKEv2 encryption parameters that your CPE supports. For a list of parameters that Oracle supports for IKEv1 or IKEv2, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters). 
You specify the IKE version when defining the IKE gateway. In the following configuration, there's a comment showing how to configure the IKE gateway for IKEv1 versus IKEv2.
[IKEv1 Configuration Template](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/necixCPE.htm)
[View the IKEv1 configuration template in full screen for easier reading.](https://docs.oracle.com/en-us/iaas/Content/Network/non-dita/vpn_cpe_nec_ikev1.txt)
Copy
```

!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! IKEv1 Configuration Template
! The configuration consists of two IPSec tunnels. Oracle highly recommends that you configure both tunnels for maximum redundancy.
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! The configuration template involves setting up the following:
! Configure ISAKMPv1 and IPSec Policies
! Configure Keepalive Setting of ICMP
! Configure Virtual Tunnel Interfaces
! IP Routing (BGP or Static)
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! The configuration template has various parameters that you must define before applying the configuration.
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! PARAMETERS REFERENCED:
! $<OracleHeadendIpAddress1> = Oracle public IP endpoint obtained from the Oracle Console.
! $<OracleHeadendIpAddress2> = Oracle public IP endpoint obtained from the Oracle Console.
! $<sharedSecret1> = You provide when you set up the IPSec connection in the Oracle Console, or you can use the default Oracle-provided value.
! $<sharedSecret2> = You provide when you set up the IPSec connection in the Oracle Console, or you can use the default Oracle-provided value.
! $<cpePublicIpAddress> = The public IP address for the CPE. This is the IP address of your outside interface.
! $<vcnCidrBlock> = VCN CIDR block. For example, 10.0.0.0/20.
! $<tunnelInterfaceNumber1> = The number of your tunnel interface for the first tunnel. For example, 1. 
! $<tunnelInterfaceNumber2> = The number of your tunnel interface for the second tunnel. For example, 2.
! $<ikePolicy1> = The name of your IKE Policy. For example, ike-policy1.
! $<ikePolicy2> = The name of your IKE Policy. For example, ike-policy2.
! $<ipsecPolicy1> = The name of your IPSec Policy. For example, ipsec-policy1.
! $<ipsecPolicy2> = The name of your IPSec Policy. For example, ipsec-policy2.
! $<lanInterfaceNumber> = The number of your LAN interface. For example, 1.0.
! $<lanIpAddress> = The IP address of the LAN interface for your CPE.
! $<OracleInsideTunnelIpAddress1> = Inside tunnel IP address of Oracle-side for the first tunnel. You provide these values when creating the IPSec connection in the Oracle Console.
! $<OracleInsideTunnelIpAddress2> = Inside tunnel IP address of Oracle-side for the second tunnel. You provide these values when creating the IPSec connection in the Oracle Console.
! $<cpeInsideTunnelIpAddress1> = The CPE's inside tunnel IP for the first tunnel.
! $<cpeInsideTunnelIpAddress2> = The CPE's inside tunnel IP for the second tunnel.
! $<bgpASN> = Your BGP ASN.
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! Configure ISAKMPv1 and IPSec Policies
	ip access-list sec-list permit ip src any dest any
	ike nat-traversal
	ike proposal ike-prop encryption aes-256 hash sha2-256 group 1536-bit
	ike policy $<ikePolicy1> peer $<OracleHeadendIpAddress1> key $<sharedSecret1> ike-prop
	ike policy $<ikePolicy2> peer $<OracleHeadendIpAddress2> key $<sharedSecret2> ike-prop
	ipsec autokey-proposal ipsec-prop esp-aes-256 esp-sha lifetime time 3600
	ipsec autokey-map $<ipsecPolicy1> sec-list peer $<OracleHeadendIpAddress1> ipsec-prop pfs 1536-bit
	ipsec autokey-map $<ipsecPolicy2> sec-list peer $<OracleHeadendIpAddress2> ipsec-prop pfs 1536-bit
! Configure Keepalive Setting of ICMP
	watch-group watch_tunnel1 10
	event 20 ip unreach-host $<lanIpAddress> Tunnel$<tunnelInterfaceNumber1> source GigaEthernet$<lanInterfaceNumber>
	action 10 ip shutdown-route $<vcnCidrBlock> Tunnel$<tunnelInterfaceNumber1>
	action 20 ipsec clear-sa Tunnel$<tunnelInterfaceNumber1>
	network-monitor watch_tunnel1 enable
	watch-group watch_tunnel2 10
	event 20 ip unreach-host $<lanIpAddress> Tunnel$<tunnelInterfaceNumber2> source GigaEthernet$<lanInterfaceNumber>
	action 10 ip shutdown-route $<vcnCidrBlock> Tunnel$<tunnelInterfaceNumber2>
	action 20 ipsec clear-sa Tunnel$<tunnelInterfaceNumber2>
	network-monitor watch_tunnel2 enable
	! Configure Virtual Tunnel Interfaces
	interface Tunnel$<tunnelInterfaceNumber1>
	tunnel mode ipsec
	ip address $<cpeInsideTunnelIpAddress1>
	ip tcp adjust-mss auto
	ipsec policy tunnel ipsec-policy1 out
	no shutdown
	interface Tunnel$<tunnelInterfaceNumber2>
	tunnel mode ipsec
	ip address $<cpeInsideTunnelIpAddress2>
	ip tcp adjust-mss auto
	ipsec policy tunnel ipsec-policy2 out
	no shutdown
! IP Routing
! Select dynamic (BGP) or static routing. Uncomment the corresponding commands prior to applying configuration.
! Border Gateway Protocol (BGP) Configuration
! Uncomment below lines if you select BGP.
! ip ufs-cache enable cache
! route-map pri1 permit 10
! set metric 5
! set local-preference 200
! route-map pri2 permit 10
! set metric 10
! set local-preference 150
! router bgp $<bgpASN>
! neighbor $<OracleInsideTunnelIpAddress1> remote-as 31898
! neighbor $<OracleInsideTunnelIpAddress1> timers 10 30
! neighbor $<OracleInsideTunnelIpAddress2> remote-as 31898
! neighbor $<OracleInsideTunnelIpAddress2> timers 10 30
! address-family ipv4 unicast
! neighbor $<OracleInsideTunnelIpAddress1> route-map pri1 in
! neighbor $<OracleInsideTunnelIpAddress1> route-map pri1 out
! neighbor $<OracleInsideTunnelIpAddress2> route-map pri2 in
! neighbor $<OracleInsideTunnelIpAddress2> route-map pri2 out
! network 192.168.100.0/24
! Static Route Configuration
! Uncomment below lines if you select static routing.
! ip ufs-cache enable
! ip route $<vcnCidrBlock> Tunnel0.0
! ip route $<vcnCidrBlock> Tunnel1.0
  
```

[IKEv2 Configuration Template](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/necixCPE.htm)
[View the IKEv2 configuration template in full screen for easier reading.](https://docs.oracle.com/en-us/iaas/Content/Network/non-dita/vpn_cpe_ciscoasa_ikev2_policy_based.txt)
Copy
```

!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! IKEv2 Configuration Template
! The configuration consists of two IPSec tunnels. Oracle highly recommends that you configure both tunnels for maximum redundancy.
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! The configuration template involves setting up the following:
! Keyring (Pre-Shared Key)
! Configure ISAKMP and IPSec Policies
! Configure Virtual Tunnel Interfaces
! IP Routing (BGP or Static)
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! The configuration template has various parameters that you must define before applying the configuration.
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! PARAMETERS REFERENCED:
! $<OracleHeadendIpAddress1> = Oracle public IP endpoint obtained from the Oracle Console.
! $<OracleHeadendIpAddress2> = Oracle public IP endpoint obtained from the Oracle Console.
! $<sharedSecret1> = You provide when you set up the IPSec connection in the Oracle Console, or you can use the default Oracle-provided value.
! $<sharedSecret2> = You provide when you set up the IPSec connection in the Oracle Console, or you can use the default Oracle-provided value.
! $<cpePublicIpAddress> = The public IP address for the CPE. This is the IP address of your outside interface.
! $<vcnCidrBlock> = VCN CIDR block. For example, 10.0.0.0/20.
! $<tunnelInterfaceNumber1> = The number of your tunnel interface for the first tunnel. For example, 1.
! $<tunnelInterfaceNumber2> = The number of your tunnel interface for the second tunnel. For example, 2.
! $<lanInterfaceNumber> = The number of your LAN interface. For example, 1.0.
! $<wanInterfaceNumber> = The WAN interface or outside of tunnel interface which is configured with the CPE public IP address. For example, 0.1.
! $<lanIpAddress> = The IP address of the LAN interface for your CPE.
! $<OracleInsideTunnelIpAddress1> = Inside tunnel IP address of Oracle-side for the first tunnel. You provide these values when creating the IPSec connection in the Oracle Console.
! $<OracleInsideTunnelIpAddress2> = Inside tunnel IP address of Oracle-side for the second tunnel. You provide these values when creating the IPSec connection in the Oracle Console.
! $<cpeInsideTunnelIpAddress1> = The CPE's inside tunnel IP for the first tunnel.
! $<cpeInsideTunnelIpAddress2> = The CPE's inside tunnel IP for the second tunnel.
! $<bgpASN> = Your BGP ASN.
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! Keyring (Pre-Shared Key)
! For authentication during IKE a separate keyring is defined for each Oracle VPN Headend peer.
! Add the pre-shared key for each Oracle VPN headend under the corresponding keyring.
ikev2 authentication psk id ipv4 $<OracleHeadendIpAddress1> key char $<sharedSecret1>
ikev2 authentication psk id ipv4 $<OracleHeadendIpAddress2> key char $<sharedSecret2>
! Configure ISAKMP and IPSec Policies
ikev2 default-profile
dpd interval 10
source-address GigaEthernet$<wanInterfaceNumber>
child-pfs 1536-bit
child-proposal enc aes-cbc-256
child-proposal integrity sha1
sa-proposal enc aes-cbc-256
sa-proposal integrity sha2-384
sa-proposal dh 1536-bit
! Configure Virtual Tunnel Interfaces
interface Tunnel$<tunnelInterfaceNumber1>
tunnel mode ipsec-ikev2
ip address $<cpeInsideTunnelIpAddress1>
ip tcp adjust-mss auto
ikev2 connect-type auto
ikev2 ipsec pre-fragment
ikev2 outgoing-interface GigaEthernet$<wanInterfaceNumber>
ikev2 peer $<OracleHeadendIpAddress1> authentication psk id ipv4 $<OracleHeadendIpAddress1>
no shutdown
interface Tunnel$<tunnelInterfaceNumber2>
tunnel mode ipsec-ikev2
ip address $<cpeInsideTunnelIpAddress2>
ip tcp adjust-mss auto
ikev2 connect-type auto
ikev2 ipsec pre-fragment
ikev2 outgoing-interface GigaEthernet$<wanInterfaceNumber>
ikev2 peer $<OracleHeadendIpAddress2> authentication psk id ipv4 $<OracleHeadendIpAddress2>
no shutdown
! IP Routing
! Select dynamic (BGP) or static routing. Uncomment the corresponding commands prior to applying configuration.
! Border Gateway Protocol (BGP) Configuration
! Uncomment below lines if you select BGP.
! ip ufs-cache enable cache
! route-map pri1 permit 10
! set metric 5
! set local-preference 200
! route-map pri2 permit 10
! set metric 10
! set local-preference 150
! router bgp $<bgpASN>
! neighbor $<OracleInsideTunnelIpAddress1> remote-as 31898
! neighbor $<OracleInsideTunnelIpAddress1> timers 10 30
! neighbor $<OracleInsideTunnelIpAddress2> remote-as 31898
! neighbor $<OracleInsideTunnelIpAddress2> timers 10 30
! address-family ipv4 unicast
! neighbor $<OracleInsideTunnelIpAddress1> route-map pri1 in
! neighbor $<OracleInsideTunnelIpAddress1> route-map pri1 out
! neighbor $<OracleInsideTunnelIpAddress2> route-map pri2 in
! neighbor $<OracleInsideTunnelIpAddress2> route-map pri2 out
! network 192.168.100.0/24
! Static Route Configuration
! Uncomment below lines if you select static routing.
! ip ufs-cache enable
! ip route $<vcnCidrBlock> Tunnel0.0
! ip route $<vcnCidrBlock> Tunnel1.0		
		
```

Was this article helpful?
YesNo

