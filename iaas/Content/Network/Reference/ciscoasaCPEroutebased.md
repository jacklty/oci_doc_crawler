Updated 2025-01-17
# Cisco ASA: Route-Based
This topic provides a route-based configuration for a Cisco ASA that is running software version 9.7.1 (or newer). 
**Important**
Oracle provides configuration instructions for a tested set of [vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices). Use the correct configuration for the vendor and software version. 
If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes. 
If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of [supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and consult the vendor's documentation for help.
As a reminder, Oracle provides different configurations based on the ASA software:
  * **9.7.1 or newer:** Route-based configuration (this topic)
  * **8.5 to 9.7.0:** [Policy-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#Cisco_ASA_PolicyBased)
  * **Older than 8.5:** Not supported by the Oracle configuration instructions. Consider upgrading to a newer version.


**Important**
Oracle provides configuration instructions for a tested set of [vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices). Use the correct configuration for the vendor and software version. 
If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes. 
If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of [supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and consult the vendor's documentation for help.
Oracle Cloud Infrastructure offersSite-to-Site VPN, a secure IPSec connection between your on-premises network and a virtual cloud network (VCN).
The following diagram shows a basic IPSec connection to Oracle Cloud Infrastructure with redundant tunnels. The IP addresses in this diagram are examples only and not for literal use.
[![This image summarizes the general layout of your on-premises network, Site-to-Site VPN IPSec tunnels, and VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_cpe_config_basic_v2.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_cpe_config_basic_v2.svg)
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
## Specific to Cisco ASA: Caveats and Limitations 🔗 
This section covers important characteristics and limitations that are specific to Cisco ASA. See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
### Tunnel MTU and Path MTU Discovery
You have two options for addressing tunnel MTU and path MTU discovery with Cisco ASA:
  * [Option 1: TCP MSS adjustment](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm#option1)
  * [Option 2: Clear/set the Don't Fragment bit](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm#option2)


### Option 1: TCP MSS adjustment 🔗 
The maximum transmission unit (packet size) through the IPSec tunnel is less than 1500 bytes. You can fragment packets that are too large to fit through the tunnel. Or, you can signal back to the hosts that are communicating through the tunnel that they need to send smaller packets.
You can configure the Cisco ASA to change the maximum segment size (MSS) for any new TCP flows through the tunnel. The ASA looks at any TCP packets where the SYN flag is set and changes the MSS value to the configured value. This configuration might help new TCP flows avoid using path maximum transmission unit discovery (PMTUD).
Use the following command to change the MSS. This command is not part of the sample configuration in the [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#CPE) section of this topic. Apply the TCP MSS adjustment command manually, if needed.
Copy
```
sysopt connection tcpmss 1387
```

### Option 2: Clear/set the Don't Fragment bit 🔗 
Path MTU discovery requires that all TCP packets have the **Don't Fragment** (DF) bit set. If the DF bit is set and a packet is too large to go through the tunnel, the ASA drops the packet when it arrives. The ASA sends an ICMP packet back to the sender indicating that the received packet was too large for the tunnel. The ASA offers three options for handling the DF bit. Choose one of the options and apply it to the configuration:
  * **Set the DF bit (recommended):** Packets have the DF bit set in their IP header. The ASA may still fragment the packet if the original received packet cleared the DF bit.
Copy
```
crypto ipsec df-bit set-df ${outsideInterface}
```

  * **Clear the DF bit:** The DF bit is cleared in the packet's IP header. Allows the packet to be fragmented and sent to the end host in Oracle Cloud Infrastructure for reassembly.
Copy
```
crypto ipsec df-bit clear-df ${outsideInterface}
```

  * **Ignore (copy) the DF bit** : The ASA looks at the original packet's IP header information and copies the DF bit setting.
Copy
```
crypto ipsec df-bit copy-df ${outsideInterface}
```



### VPN Traffic Might Enter One Tunnel and Exit Another 🔗 
If VPN traffic enters an interface with the same security level as an interface toward the packet's next hop, you must allow that traffic. By default, the packets between interfaces that have identical security levels on your ASA are dropped.
Add the following command manually if you need to permit traffic between interfaces with the same security levels. This command is not part of the sample configuration in the [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#CPE) section.
Copy
```
same-security-traffic permit inter-interface
```

## General Caveats and Limitations 🔗 
This section covers general characteristics and limitations of Site-to-Site VPN. See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
### Asymmetric Routing
Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Configure firewalls with that in mind. Otherwise, ping tests or application traffic across the connection don't work reliably. 
When you use several tunnels to Oracle Cloud Infrastructure, We recommend that you configure routing to deterministically route traffic through the preferred tunnel. To use one IPSec tunnel as primary and another as backup, configure more-specific routes for the primary tunnel (BGP) and less-specific routes (summary or default route) for the backup tunnel (BGP/static). Otherwise, if you advertise the same route (for example, a default route) through all tunnels, return traffic from a VCN to an on-premises network routes to any of the available tunnels. This is because Oracle uses asymmetric routing.
For specific Oracle routing recommendations about how to force symmetric routing, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing). 
### Route-Based or Policy-Based IPSec Connections
The IPSec protocol uses Security Associations (SAs) to decide how to encrypt packets. Within each SA, you define encryption domains to map a packet's source and destination IP address and protocol type to an entry in the SA database to define how to encrypt or decrypt a packet. 
**Note** Other vendors or industry documentation might use the term _proxy ID, security parameter index (SPI)_ , or _traffic selector_ when referring to SAs or encryption domains.
There are two general methods for implementing IPSec tunnels:
  * **Route-based tunnels:** Also called _next-hop-based tunnels_. A route table lookup is performed on a packet's destination IP address. If that route's egress interface is an IPSec tunnel, the packet is encrypted and sent to the other end of the tunnel. 
  * **Policy-based tunnels:** The packet's source and destination IP address and protocol are matched against a list of policy statements. If a match is found, the packet is encrypted based on the rules in that policy statement.


The Oracle Site-to-Site VPN headends use route-based tunnels but can work with policy-based tunnels with some caveats listed in the following sections. 
[Encryption domain for route-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm)
If the CPE supports route-based tunnels, use that method to configure the tunnel. This is the simplest configuration with the most interoperability with the Oracle VPN headend. 
Route-based IPSec uses an encryption domain with the following values:
  * **Source IP address:** Any (0.0.0.0/0)
  * **Destination IP address:** Any (0.0.0.0/0)
  * **Protocol:** IPv4


If you need to be more specific, you can use a single summary route for encryption domain values instead of a default route.
[Encryption domain for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm)
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
The configuration template provided is for a Cisco router running Cisco ASA 9.7.1 software (or later). The template provides information for each tunnel that you must configure. Oracle recommends setting up all configured tunnels for maximum redundancy.
The configuration template refers to these items that you must provide:
  * **CPE public IP address:** The internet-routable IP address that is assigned to the external interface on the CPE. You or your Oracle administrator provides this value to Oracle when creating the CPE object in the Oracle Console.
  * **Inside tunnel interface (required if using BGP):** The IP addresses for the CPE and Oracle ends of the inside tunnel interface. You provide these values when creating the IPSec connection in the Oracle Console.
  * **BGP ASN (required if using BGP):** Your BGP ASN.


In addition, you must:
  * Configure internal routing that routes traffic between the CPE and your local network.
  * Ensure that you permit traffic between your ASA and your Oracle VCN.
  * Identify the IPSec profile used (the following configuration template references this group policy as `oracle-vcn-vpn-policy`).
  * Identify the transform set used for your crypto map (the following configuration template references this transform set as `oracle-vcn-transform`).
  * Identify the virtual tunnel interface names used (the following configuration template references these as variables `${tunnelInterfaceName1}` and `${tunnelInterfaceName2}`).


**Important**
This following configuration template from Oracle Cloud Infrastructure **is a starting point for what you need to apply to your CPE.** Some of the parameters referenced in the template must be unique on the CPE, and the uniqueness can only be determined by accessing the CPE. Ensure that the parameters are valid on your CPE and do not overwrite any previously configured values. In particular, ensure these values are unique:
  * Policy names or numbers
  * Interface names or numbers
  * Access list numbers (if applicable)


Oracle supports Internet Key Exchange version 1 (IKEv1) and version 2 (IKEv2). If you [configure the IPSec connection in the Console to use IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#using_ikev2), you must configure your CPE to use only IKEv2 and related IKEv2 encryption parameters that your CPE supports. For a list of parameters that Oracle supports for IKEv1 or IKEv2, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters). 
Oracle provides a separate configuration template for IKEv1 versus IKEv2.
Oracle also provides a tool that can generate the template for you, with some of the information automatically filled in. For more information, see [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper).
[IKEv1 Configuration Template](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm)
[View the IKEv1 configuration template in full screen for easier reading.](https://docs.oracle.com/en-us/iaas/Content/Network/non-dita/vpn_cpe_ciscoasa_route_based.txt)
Copy
```
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! IKEv1 Configuration Template
! The configuration consists of two IPSec tunnels. Oracle highly recommends that you configure both tunnels for maximum redundancy.
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! The configuration template involves setting up the following:
! ISAKMP Policy
! IPSec Configuration
! IPSec Tunnel Group Configuration
! VTI Interface Configuration
! IP Routing (BGP or Static)
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! The configuration template has various parameters that you must define before applying the configuration.
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! PARAMETERS REFERENCED:
! ${OracleInsideTunnelIpAddress1} = Inside tunnel IP address of Oracle-side for the first tunnel. You provide these values when creating the IPSec connection in the Oracle Console.
! ${OracleInsideTunnelIpAddress2} = Inside tunnel IP address of Oracle-side for the second tunnel. You provide these values when creating the IPSec connection in the Oracle Console.
! ${bgpASN} = Your BGP ASN
! ${cpePublicIpAddress} = The public IP address for the CPE. This is the IP address of your outside interface
! ${oracleHeadend1} = Oracle public IP endpoint obtained from the Oracle Console.
! ${oracleHeadend2} = Oracle public IP endpoint obtained from the Oracle Console.
! ${sharedSecret1} = You provide when you set up the IPSec connection in the Oracle Console, or you can use the default Oracle-provided value.
! ${sharedSecret2} = You provide when you set up the IPSec connection in the Oracle Console, or you can use the default Oracle-provided value.
! ${outsideInterface} = The public interface or outside of tunnel interface which is configured with the CPE public IP address.
! ${tunnelInterfaceName1} = The name of the first VTI used on your ASA.
! ${tunnelInterfaceName2} = The name of the second VTI used on your ASA.
! ${cpeInsideTunnelIpAddress1} = The CPE's inside tunnel IP for the first tunnel.
! ${cpeInsideTunnelIpAddress2} = The CPE's inside tunnel IP for the second tunnel.
! ${cpeInsideTunnelNetmask1} = The CPE's inside tunnel netmask for the first tunnel.
! ${cpeInsideTunnelNetmask2} = The CPE's inside tunnel netmask for the second tunnel.
! ${vcnCidrNetwork} = VCN IP range
! ${vcnCidrNetmask} = Subnet mask for VCN
! ${onPremCidrNetwork} = On-premises IP range
! ${onPremCidrNetmask} = ON-premises subnet mask
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
 
! ISAKMP Policy
 
! ISAKMP Phase 1 configuration.
! IKEv1 is enabled on the outside interface.
! IKEv1 policy is created for Phase 1 which specifies to use a Pre-Shared Key, AES256, SHA1, Diffie-Hellman Group 5, and a Phase 1 lifetime of 28800 seconds (8 hours).
! If different parameters are required, modify this template before applying the configuration.
! WARNING: The IKEv1 group policy is created with a priority of 10. Make sure this doesn't conflict with any pre-existing configuration on your ASA.
 
crypto ikev1 enable ${outsideInterface}
 
crypto ikev1 policy 10
 authentication pre-share
 encryption aes-256
 hash sha
 group 5
 lifetime 28800
 
! IPSec Configuration
 
! Create an IKEv1 transform set named 'oracle-vcn-transform' which defines a combination of IPSec (Phase 2) policy options. Specifically, AES256 for encryption and SHA1 for authentication.
! If different parameters are required, modify this template before applying the configuration.
 
crypto ipsec ikev1 transform-set oracle-vcn-transform esp-aes-256 esp-sha-hmac
 
! A IPSec profile named 'oracle-vcn-vpn-policy' is created.
! The previously created transform set is added to this policy along with settings for enabling PFS Group 5 and the security association lifetime to 3600 seconds (1 hour).
! If different parameters are required, modify this template before applying the configuration.
 
crypto ipsec profile oracle-vcn-vpn-policy
 set ikev1 transform-set oracle-vcn-transform
 set pfs group5
 set security-association lifetime seconds 3600
 
! IPSec Tunnel Group Configuration
 
! A tunnel group is created for each Oracle VPN Headend. Each tunnel group defines the pre-shared key used for each respective tunnel.
 
tunnel-group ${oracleHeadend1} type ipsec-l2l
tunnel-group ${oracleHeadend1} ipsec-attributes
 ikev1 pre-shared-key ${sharedSecret1}
 
tunnel-group ${oracleHeadend2} type ipsec-l2l
tunnel-group ${oracleHeadend2} ipsec-attributes
 ikev1 pre-shared-key ${sharedSecret2}
 
! VTI Interface Configuration
 
! A virtual tunnel interface (VTI) is a logical interface representing the local end of a VPN tunnel to a remote VPN peer. Two VTIs are created representing two tunnels, one to each Oracle VPN Headend. The IP address of each VPN headend is provided when you create your IPSec connection in Oracle Console.
! All traffic routed to a VTI will be encrypted and sent across the tunnel towards Oracle Cloud Infrastructure.
! Each VTI configuration also references the previously created IPSec profile 'oracle-vcn-vpn-policy' for its IPSec parameters.
 
interface ${tunnelInterfaceName1}
 nameif ORACLE-VPN1
 ip address ${cpeInsideTunnelIpAddress1} ${cpeInsideTunnelNetmask1}
 tunnel source interface ${outsideInterface}
 tunnel destination ${oracleHeadend1}
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile oracle-vcn-vpn-policy
 
interface ${tunnelInterfaceName2}
 nameif ORACLE-VPN2
 ip address ${cpeInsideTunnelIpAddress2} ${cpeInsideTunnelNetmask2}
 tunnel source interface ${outsideInterface}
 tunnel destination ${oracleHeadend2}
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile oracle-vcn-vpn-policy
 
! IP Routing
! Pick either dynamic (BGP) or static routing. Uncomment the corresponding commands prior to applying configuration.
 
! Border Gateway Protocol (BGP) Configuration
! Uncomment below lines if you want to use BGP.
 
! router bgp ${bgpASN}
! address-family ipv4 unicast
!  neighbor ${OracleInsideTunnelIpAddress1} remote-as 31898
!  neighbor ${OracleInsideTunnelIpAddress1} activate
!  neighbor ${OracleInsideTunnelIpAddress2} remote-as 31898
!  neighbor ${OracleInsideTunnelIpAddress2} activate
!  network ${onPremCidrNetwork} mask ${onPremCidrNetmask}
!  no auto-summary
!  no synchronization
! exit-address-family
 
! Static Route Configuration
! Each static route references the other VTI by its nameif value.
! Uncomment below line if you want to use static routing.
 
! route ORACLE-VPN1 ${VcnCidrNetwork} ${VcnCidrNetmask} ${OracleInsideTunnelIpAddress1} 1 track
! route ORACLE-VPN2 ${VcnCidrNetwork} ${VcnCidrNetmask} ${OracleInsideTunnelIpAddress2} 100
 
! Configuration for Tunnel Failover
 
! Uncomment the below IP SLA lines if using static routing.
! Use this IP SLA configuration for static route failover This IP SLA configuration is used for static route failover between the two tunnels.
! Make sure that the SLA monitor and tracking numbers used do not conflict with any existing configuration on your ASA.
 
! sla monitor 10
! type echo protocol ipIcmpEcho ${oracleHeadend1} interface outside
! frequency 5
! sla monitor schedule 10 life forever start-time now
 
! track 1 rtr 10 reachability
```

[IKEv2 Configuration Template](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm)
[View the IKEv2 configuration template in full screen for easier reading.](https://docs.oracle.com/en-us/iaas/Content/Network/non-dita/vpn_cpe_ciscoasa_ikev2_route_based.txt)
Copy
```
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! IKEv2 Configuration Template
! The configuration consists of two IPSec tunnels. Oracle highly recommends that you configure both tunnels for maximum redundancy.
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! The configuration template involves setting up the following:
! IKEv2 Policy
! IPSec Configuration
! IPSec Tunnel Group Configuration
! VTI Interface Configuration
! IP Routing (BGP or Static)
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! The configuration template has various parameters that you must define before applying the configuration.
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! PARAMETERS REFERENCED:
! ${OracleInsideTunnelIpAddress1} = Inside tunnel IP address of Oracle-side for the first tunnel. You provide these values when creating the IPSec connection in the Oracle Console.
! ${OracleInsideTunnelIpAddress2} = Inside tunnel IP address of Oracle-side for the second tunnel. You provide these values when creating the IPSec connection in the Oracle Console.
! ${bgpASN} = Your BGP ASN
! ${cpePublicIpAddress} = The public IP address for the CPE. This is the IP address of your outside interface
! ${oracleHeadend1} = Oracle public IP endpoint obtained from the Oracle Console.
! ${oracleHeadend2} = Oracle public IP endpoint obtained from the Oracle Console.
! ${sharedSecret1} = You provide when you set up the IPSec connection in the Oracle Console, or you can use the default Oracle-provided value.
! ${sharedSecret2} = You provide when you set up the IPSec connection in the Oracle Console, or you can use the default Oracle-provided value.
! ${outsideInterface} = The public interface or outside of tunnel interface which is configured with the CPE public IP address.
! ${tunnelInterfaceName1} = The name of the first VTI used on your ASA.
! ${tunnelInterfaceName2} = The name of the second VTI used on your ASA.
! ${cpeInsideTunnelIpAddress1} = The CPE's inside tunnel IP for the first tunnel.
! ${cpeInsideTunnelIpAddress2} = The CPE's inside tunnel IP for the second tunnel.
! ${cpeInsideTunnelNetmask1} = The CPE's inside tunnel netmask for the first tunnel.
! ${cpeInsideTunnelNetmask2} = The CPE's inside tunnel netmask for the second tunnel.
! ${vcnCidrNetwork} = VCN IP range
! ${vcnCidrNetmask} = Subnet mask for VCN
! ${onPremCidrNetwork} = On-premises IP range
! ${onPremCidrNetmask} = ON-premises subnet mask
!-------------------------------------------------------------------------------------------------------------------------------------------------------------
! IKEv2 Policy
! IKEv2 is enabled on the outside interface.
! IKEv2 policy is created and specifies use of a Pre-Shared Key, AES256, SHA1, Diffie-Hellman Group 5, and a lifetime of 28800 seconds (8 hours).
! If different parameters are required, modify this template before applying the configuration.
! WARNING: The IKEv2 group policy is created with a priority of 10. Make sure this doesn't conflict with any pre-existing configuration on your ASA.
crypto ikev2 enable ${outsideInterface}
crypto ikev2 policy 10
 encryption aes-256
 integrity sha
 group 5
 prf sha
 lifetime seconds 28800
! IPSec Configuration
! Create an IKEv2 IPSec proposal named 'oracle_v2_ipsec_proposal' which defines AES256 for encryption and SHA1 for authentication.
! If different parameters are required, modify this template before applying the configuration.
crypto ipsec ikev2 ipsec-proposal oracle_v2_ipsec_proposal
 protocol esp encryption aes-256
 protocol esp integrity sha-1
! An IPSec profile named 'oracle-vcn-vpn-policy' is created.
! The previously created IPSec proposal is added to this policy along with settings for enabling PFS Group 5 and the security association lifetime to 3600 seconds (1 hour).
! If different parameters are required, modify this template before applying the configuration.
crypto ipsec profile oracle-vcn-vpn-policy
 set ikev2 ipsec-proposal oracle_v2_ipsec_proposal
 set pfs group5
 set security-association lifetime seconds 3600
! IPSec Tunnel Group Configuration
group-policy oracle_v2_group_policy internal
group-policy oracle_v2_group_policy attributes
 vpn-tunnel-protocol ikev2
! A tunnel group is created for each Oracle VPN Headend. Each tunnel group defines the pre-shared key used for each respective tunnel.
tunnel-group ${oracleHeadend1} type ipsec-l2l
tunnel-group ${oracleHeadend1} general-attributes
 default-group-policy oracle_v2_group_policy
tunnel-group ${oracleHeadend1} ipsec-attributes
 ikev2 local-authentication pre-shared-key ${sharedSecret1}
 ikev2 remote-authentication pre-shared-key ${sharedSecret1}
tunnel-group ${oracleHeadend2} type ipsec-l2l
tunnel-group ${oracleHeadend2} general-attributes
 default-group-policy oracle_v2_group_policy
tunnel-group ${oracleHeadend2} ipsec-attributes
 ikev2 local-authentication pre-shared-key ${sharedSecret2}
 ikev2 remote-authentication pre-shared-key ${sharedSecret2}
! VTI Interface Configuration
! A virtual tunnel interface (VTI) is a logical interface representing the local end of a VPN tunnel to a remote VPN peer. Two VTIs are created representing two tunnels, one to each Oracle VPN Headend. The IP address of each VPN headend is provided when you create your IPSec connection in Oracle Console.
! All traffic routed to a VTI will be encrypted and sent across the tunnel towards Oracle Cloud Infrastructure.
! Each VTI configuration also references the previously created IPSec profile 'oracle-vcn-vpn-policy' for its IPSec parameters.
interface ${tunnelInterfaceName1}
 nameif ORACLE-VPN1
 ip address ${cpeInsideTunnelIpAddress1} ${cpeInsideTunnelNetmask1}
 tunnel source interface ${outsideInterface}
 tunnel destination ${oracleHeadend1}
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile oracle-vcn-vpn-policy
interface ${tunnelInterfaceName2}
 nameif ORACLE-VPN2
 ip address ${cpeInsideTunnelIpAddress2} ${cpeInsideTunnelNetmask2}
 tunnel source interface ${outsideInterface}
 tunnel destination ${oracleHeadend2}
 tunnel mode ipsec ipv4
 tunnel protection ipsec profile oracle-vcn-vpn-policy
! IP Routing
! Pick either dynamic (BGP) or static routing. Uncomment the corresponding commands prior to applying configuration.
! Border Gateway Protocol (BGP) Configuration
! Uncomment below lines if you want to use BGP.
! router bgp ${bgpASN}
! address-family ipv4 unicast
!  neighbor ${OracleInsideTunnelIpAddress1} remote-as 31898
!  neighbor ${OracleInsideTunnelIpAddress1} activate
!  neighbor ${OracleInsideTunnelIpAddress2} remote-as 31898
!  neighbor ${OracleInsideTunnelIpAddress2} activate
!  network ${onPremCidrNetwork} mask ${onPremCidrNetmask}
!  no auto-summary
!  no synchronization
! exit-address-family
! Static Route Configuration
! Each static route references the other VTI by its nameif value.
! Uncomment below line if you want to use static routing.
! route ORACLE-VPN1 ${VcnCidrNetwork} ${VcnCidrNetmask} ${OracleInsideTunnelIpAddress1} 1 track
! route ORACLE-VPN2 ${VcnCidrNetwork} ${VcnCidrNetmask} ${OracleInsideTunnelIpAddress2} 100
! Configuration for Tunnel Failover
! Uncomment the below IP SLA lines if using static routing.
! Use this IP SLA configuration for static route failover This IP SLA configuration is used for static route failover between the two tunnels.
! Make sure that the SLA monitor and tracking numbers used do not conflict with any existing configuration on your ASA.
! sla monitor 10
! type echo protocol ipIcmpEcho ${oracleHeadend1} interface outside
! frequency 5
! sla monitor schedule 10 life forever start-time now
! track 1 rtr 10 reachability
```

## Verification 🔗 
The following ASA commands are included for basic troubleshooting. For more exhaustive information, refer to Cisco's [IPSec Troubleshooting](https://www.cisco.com/c/en/us/support/docs/security-vpn/ipsec-negotiation-ike-protocols/5409-ipsec-debug-00.html) document.
Use the following command to verify that ISAKMP security associations are being built between the two peers.
Copy
```
show crypto isakmp sa
```

Use the following command to verify the status of all your BGP connections.
Copy
```
show bgp summary
```

Use the following command to verify the ASA's route table.
Copy
```
show route
```

A [Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) is also available from Oracle Cloud Infrastructure to actively and passively monitor cloud resources. For information about monitoring a Site-to-Site VPN, see [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics).
If you have issues, see [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/ipsectroubleshoot.htm#VPN_Connect_Troubleshooting).
Was this article helpful?
YesNo

