Updated 2025-01-17
# Juniper MX
This topic provides configuration for a Juniper MX that is running software version JunOS 15.0 (or newer).
**Important**
Oracle provides configuration instructions for a tested set of [vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices). Use the correct configuration for the vendor and software version. 
If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes. 
If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of [supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and consult the vendor's documentation for help.
Oracle Cloud Infrastructure offersSite-to-Site VPN, a secure IPSec connection between your on-premises network and a virtual cloud network (VCN).
The following diagram shows a basic IPSec connection to Oracle Cloud Infrastructure with redundant tunnels. IP addresses used in this diagram are for example purposes only.
[![This image summarizes the general layout of your on-premises network, Site-to-Site VPN IPSec tunnels, and VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_cpe_config_basic.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vpn_cpe_config_basic.svg)
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
This section covers general important characteristics and limitations of Site-to-Site VPN to be aware of. See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
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
[Encryption domain for route-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/junipermxCPE.htm)
If the CPE supports route-based tunnels, use that method to configure the tunnel. This is the simplest configuration with the most interoperability with the Oracle VPN headend. 
Route-based IPSec uses an encryption domain with the following values:
  * **Source IP address:** Any (0.0.0.0/0)
  * **Destination IP address:** Any (0.0.0.0/0)
  * **Protocol:** IPv4


If you need to be more specific, you can use a single summary route for encryption domain values instead of a default route.
[Encryption domain for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/junipermxCPE.htm)
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


#### If Your CPE Is Behind a NAT Device 🔗 
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
The configuration template provided is for a Juniper MX router running JunOS 15.0 (or newer). The template provides information for each tunnel that you must configure. Oracle recommends setting up all configured tunnels for maximum redundancy.
The configuration template refers to these items that you must provide:
  * **CPE public IP address:** The internet-routable IP address that is assigned to the external interface on the CPE. You or your Oracle administrator provides this value to Oracle when creating the CPE object in the Oracle Console.
  * **Inside tunnel interface (required if using BGP):** The IP addresses for the CPE and Oracle ends of the inside tunnel interface. You provide these values when creating the IPSec connection in the Oracle Console.
  * **BGP ASN (required if using BGP):** Your BGP ASN.


In addition, you must:
  * Configure the Juniper MX public interface (the CPE public IP address is bound to this interface).
  * Configure internal routing that routes traffic between the CPE and your local network.
  * Configure the tunnel interfaces. See the next section for more information.


### About the Tunnel Interfaces
In the following configuration template, the tunnel interfaces are referred to with the following variables:
  * `msInterface#` - one per tunnel
    * These interfaces correspond to one of the four encryption ASICs on the MS-MPC card.
    * You can distribute load across the ASICs by spreading your tunnels across them.
    * Example values: ms-2/3/0, ms-2/3/1
  * `insideMsUnit#` and `outsideMsUnit#` - one pair per tunnel
    * For every tunnel, you need an ms-mpc interface pair of units.
    * One represents the outside of the IPSec tunnel. The other represents the inside of the tunnel.
    * The router forwards packets from your on-premises network to your VCN into the inside unit.
      * The encryption ASIC then encrypts the packets based on the rules and policies.
      * Then the encrypted packet egresses out the outside unit as an ESP packet, ready to be forwarded to the Oracle VPN headend routers.
    * There are over 16,000 possible values for unit numbers.
      * One way to allocate the units is to offset them by 8,000.
      * You can pick values between 0 - 7999 for `insideMsUnit#` and 8000-15999 for `outsideMsUnit#`.


**Important**
This following configuration template from Oracle Cloud Infrastructure **is a starting point for what you need to apply to your CPE.** Some of the parameters referenced in the template must be unique on the CPE, and the uniqueness can only be determined by accessing the CPE. Ensure the parameters are valid on your CPE and do not overwrite any previously configured values. In particular, ensure these values are unique:
  * Policy names or numbers
  * Interface names
  * Access list numbers (if applicable)


To find parameters that you must define before applying the configuration, search for the keyword `USER_DEFINED` in the template.
### About Using IKEv2
Oracle supports Internet Key Exchange version 1 (IKEv1) and version 2 (IKEv2). If you [configure the IPSec connection in the Console to use IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#using_ikev2), you must configure your CPE to use only IKEv2 and related IKEv2 encryption parameters that your CPE supports. For a list of parameters that Oracle supports for IKEv1 or IKEv2, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters). 
You specify the IKE version when defining the IKE policy. In the following configuration, there's a comment showing how to configure the IKE policy for IKEv1 versus IKEv2.
### Configuration Template
[View the configuration template in full screen for easier reading.](https://docs.oracle.com/en-us/iaas/Content/Network/non-dita/vpn_cpe_juniper_mx.txt)
Copy
```

--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Configuration Template
# The configuration consists of two IPSec tunnels. Oracle highly recommends that you configure both tunnels for maximum redundancy.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
# The configuration template involves setting up the following:
# PHASE 1
# PHASE 2
# SETTING THE TUNNEL INTERFACES FOR ORACLE
# SETTING THE SERVICES FOR ORACLE.
# SETTING BGP/STATIC ROUTING
# SETTING ROUTING-INSTANCES FOR ORACLE (OPTIONAL).
--------------------------------------------------------------------------------------------------------------------------------------------------------------
# The configuration template has various parameters that you must define before applying the configuration.
# Search in the template for the keyword "USER_DEFINED" to find those parameters.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
# PARAMETERS REFERENCED:
# oracle_headend_1 = Oracle public IP endpoint obtained from the Oracle Console.
# oracle_headend_2 = Oracle public IP endpoint obtained from the Oracle Console.
# connection_presharedkey_1 = You provide when you set up the IPSec connection in the Oracle Console, or you can use the default Oracle-provided value.
# connection_presharedkey_2 = You provide when you set up the IPSec connection in the Oracle Console, or you can use the default Oracle-provided value.
# cpe_public_ip_address = The internet-routable IP address that is assigned to the public interface on the CPE. You provide this when creating the CPE object in the Oracle Console.
# cpe_public_interface = The name of the Juniper interface where the CPE IP address is configured. Eg: ge-0/0/1.0
# msInterface1 = The interface correspond to one of the four encryption ASICs on the MS-MPC card. Eg: ms-2/3/0, ms-2/3/1
# msInterface2 = Second tunnel interface that needs to be configured. Eg: ms-2/3/0, ms-2/3/1
# insideMsUnit1 = The inside interface of the MS-MPC interface pair for tunnel_1
# insideMsUnit2 = The inside interface of the MS-MPC interface pair for tunnel_2
# outsideMsUnit1 = The outside interface of the MS-MPC interface pair for tunnel_1
# outsideMsUnit2 = The outside interface of the MS-MPC interface pair for tunnel_2
# inside_tunnel_interface_ip_address = The IP addresses for the CPE and Oracle ends of the inside tunnel interface. You provide these when creating the IPSec connection in the Oracle Console.
# inside_tunnel_interface_ip_address_neighbor = The neighbor IP address between the MX and Oracle end points of the inside tunnel interface.
# bgp_asn = Your ASN
# vcn_range = VCN IP Range
 
# OPTIONAL PARAMETERS:
# customer_on-prem_to_oracle = Name of the routing instance to be defined on the CPE for the tunnel interfaces connecting to the Oracle headends.
# internet_routing_instance = Name of the routing instance to be defined on the CPE for the tunnel interfaces that are connected to the Internet.
--------------------------------------------------------------------------------------------------------------------------------------------------------------
 
# IPSec Tunnel 1
  
# #1: Internet Key Exchange (IKE) Configuration (Phase 1)
# Defining the IKE Proposal for Oracle
# This IKE (Phase 1) configuration template uses AES256, SHA384, Diffie-Hellman Group 5, and 28800 second (8 hours) IKE session key lifetime.
# If different parameters are required, modify this template before applying the configuration.
  
set services ipsec-vpn ike proposal oracle-ike-proposal authentication-method pre-shared-keys
set services ipsec-vpn ike proposal oracle-ike-proposal authentication-algorithm sha-384
set services ipsec-vpn ike proposal oracle-ike-proposal encryption-algorithm aes-256-cbc
set services ipsec-vpn ike proposal oracle-ike-proposal lifetime-seconds 28800
set services ipsec-vpn ike proposal oracle-ike-proposal dh-group group5
  
# Defining the IKE Policy for Oracle
# USER_DEFINED: Replace the parameters in the section below as needed
# If using IKEv1, uncomment the following two lines, and comment out the line after (the line with "version 2" at the end) 
# set services ipsec-vpn ike policy oracle-ike-policy-tunnel_1 mode main
# set services ipsec-vpn ike policy oracle-ike-policy-tunnel_1 version 1
  
set services ipsec-vpn ike policy oracle-ike-policy-tunnel_1 version 2
set services ipsec-vpn ike policy oracle-ike-policy-tunnel_1 proposals oracle-ike-proposal
set services ipsec-vpn ike policy oracle-ike-policy-tunnel_1 local-id ipv4_addr <cpe_public_ip_address>
set services ipsec-vpn ike policy oracle-ike-policy-tunnel_1 remote-id ipv4_addr <oracle_headend_1>
set services ipsec-vpn ike policy oracle-ike-policy-tunnel_1 pre-shared-key ascii-text <connection_presharedkey_1>
 
# Setting up Public Interface with the CPE Public IP.
# USER_DEFINED: Replace the parameters in the section below as needed
  
set interfaces <cpe_public_interface> unit 0 family inet address <cpe_public_ip_address> 
 
 
# #2: IPSec Configuration
 
# Defining the IPSec (Phase 2) Proposal for Oracle
# The IPSec proposal defines the protocol, authentication, encryption, and lifetime parameters for the IPsec security association.
# The configuration template sets AES256 for encryption, SHA256 for authentication, enables PFS group 14, and sets the IPSec session key lifetime to 3600 seconds (1 hour).
# The IPsec policy incorporates the Diffie-Hellman group and the IPsec proposal.
# If different parameters are required, modify this template before applying the configuration.
  
set services ipsec-vpn ipsec proposal oracle-ipsec-proposal
set services ipsec-vpn ipsec proposal oracle-ipsec-proposal protocol esp
set services ipsec-vpn ipsec proposal oracle-ipsec-proposal authentication-algorithm hmac-sha-256-128
set services ipsec-vpn ipsec proposal oracle-ipsec-proposal encryption-algorithm aes-256-cbc
set services ipsec-vpn ipsec proposal oracle-ipsec-proposal lifetime-seconds 3600
 
# Defining the IPSec (PHASE 2) policy for Oracle
 
set services ipsec-vpn ipsec policy oracle-ipsec-policy perfect-forward-secrecy keys group14
set services ipsec-vpn ipsec policy oracle-ipsec-policy proposals oracle-ipsec-proposal
  
# Defining Security Association for Oracle
# USER_DEFINED: Replace the parameters in the section below as needed.
# The IKE and IPSEC policies are associated with the tunnel interface. Eg: ms-2/3/0.101
# The IPsec Dead Peer Detection option causes periodic messages to be sent to ensure a Security Association remains operational.
  
set services ipsec-vpn rule oracle-vpn-tunnel_1 term 1 from ipsec-inside-interface <msInterface1>.<insideMsUnit1>
set services ipsec-vpn rule oracle-vpn-tunnel_1 term 1 then remote-gateway <oracle_headend_1>
set services ipsec-vpn rule oracle-vpn-tunnel_1 term 1 then dynamic ike-policy oracle-ike-policy-tunnel_1
set services ipsec-vpn rule oracle-vpn-tunnel_1 term 1 then dynamic ipsec-policy oracle-ipsec-policy
set services ipsec-vpn rule oracle-vpn-tunnel_1 term 1 then tunnel-mtu 1430
set services ipsec-vpn rule oracle-vpn-tunnel_1 term 1 then initiate-dead-peer-detection
set services ipsec-vpn rule oracle-vpn-tunnel_1 term 1 then dead-peer-detection
set services ipsec-vpn rule oracle-vpn-tunnel_1 term 1 then dead-peer-detection interval 5
set services ipsec-vpn rule oracle-vpn-tunnel_1 term 1 then dead-peer-detection threshold 4
set services ipsec-vpn rule oracle-vpn-tunnel_1 match-direction input
  
 
# #3: Tunnel Interface Configuration
  
# Defining the Tunnel Interfaces
# USER_DEFINED: Replace the parameters in the section below as needed.
  
set interfaces <msInterface1> unit <insideMsUnit1> description oracle-vpn-tunnel-1-INSIDE
set interfaces <msInterface1> unit <insideMsUnit1> family inet address <inside_tunnel_interface_ip_address>
set interfaces <msInterface1> unit <insideMsUnit1> service-domain inside
 
set interfaces <msInterface1> unit <outsideMsUnit1> description oracle-vpn-tunnel-1-OUTSIDE
set interfaces <msInterface1> unit <outsideMsUnit1> family inet
set interfaces <msInterface1> unit <outsideMsUnit1> service-domain outside
 
# #4: Service Set Configuration
 
# USER_DEFINED: Replace the parameters in the section below as needed
# Service set configuration to direct traffic to the tunnel interfaces and associating the appropriate IPSec-VPN-Rule.
 
set services service-set oracle-vpn-tunnel_1 next-hop-service inside-service-interface <msInterface1>.<insideMsUnit1>
set services service-set oracle-vpn-tunnel_1 next-hop-service outside-service-interface <msInterface1>.<outsideMsUnit1>
set services service-set oracle-vpn-tunnel_1 ipsec-vpn-options local-gateway <cpe_public_ip_address>
set services service-set oracle-vpn-tunnel_1 ipsec-vpn-rules oracle-vpn-tunnel-tunnel_1
 
# This option causes the router to reduce the Maximum Segment Size of TCP packets to prevent packet fragmentation.
  
set services service-set oracle-vpn-tunnel_1 tcp-mss 1387
  
# #5a: Border Gateway Protocol (BGP) Configuration
  
# USER_DEFINED: Replace the parameters in the section below as needed                                         
# BGP is used within the tunnel to exchange prefixes between the Dynamic Routing Gateway and your CPE. The DRG dynamically learns the routes from your on-premises network. On the Oracle side, the DRG advertises the VCN's subnets.
# The configuration template uses a basic route policy to advertise a default route to the DRG.
# To advertise additional prefixes to the Oracle VCN, add additional prefixes to the term ORACLE-DEFAULT policy. Make sure the prefix is present in the route table of the device with a valid next-hop.                                         
# You configure the local BGP Autonomous System Number (BGP ASN) when you set up the IPSec connection in the Oracle Console. If you later need to change the ASN, you must recreate the CPE object and IPSec connection in the Oracle Console.  
  
set policy-options policy-statement ORACLE-DEFAULT term default from route-filter 0.0.0.0/0 exact                              
set policy-options policy-statement ORACLE-DEFAULT term default then accept 
set policy-options policy-statement ORACLE-DEFAULT term reject then reject
  
set protocols bgp group ebgp type external
set protocols bgp group ebgp neighbor <inside_tunnel_interface_ip_address_neighbor> export ORACLE-DEFAULT
set protocols bgp group ebgp neighbor <inside_tunnel_interface_ip_address_neighbor> peer-as 31898
set protocols bgp group ebgp neighbor <inside_tunnel_interface_ip_address_neighbor> local-as <bgp_asn>
 
 
# #5b: Static Route Configuration
 
# USER_DEFINED: Replace the parameters in the section below as needed
# In case you plan to use static routing to get traffic through the IPSec tunnels, you can point the routes down to the tunnel interfaces. You should redistribute these routes into your on-premises network. Configuration for CPE to VCN static routes:
  
set routing-options static route <vcn_range> next-hop <msInterface1>.<insideMsUnit1>
 
##6: Routing Instances Configuration (Optional)
# USER_DEFINED: Replace the parameters in the section below as needed.
# If you are using routing-instances on your CPE, you need to make sure you account for them in your configuration. Merge the following configuration into the template provided above.
 
set routing-instances <customer_on-prem_to_oracle> interface <msInterface1>.<insideMsUnit1>
set routing-instances <internet_routing_instance> interface <msInterface1>.<outsideMsUnit1>
set services service-set oracle-vpn-tunnel-tunnel_1 ipsec-vpn-options local-gateway <cpe_public_ip_address> routing-instance <internet_routing_instance>
 
--------------------------------------------------------------------------------------------------------------------------------------------------------------
  
# IPSec Tunnel 2
  
# #1: Internet Key Exchange (IKE) Configuration (Phase 1)
 
# Defining the IKE Proposal for Oracle
# This IKE (Phase 1) configuration template uses AES256, SHA384, Diffie-Hellman Group 5, and 28800 second (8 hours) IKE session key lifetime.
# If different parameters are required, modify this template before applying the configuration.
  
set services ipsec-vpn ike proposal oracle-ike-proposal authentication-method pre-shared-keys
set services ipsec-vpn ike proposal oracle-ike-proposal authentication-algorithm sha-384
set services ipsec-vpn ike proposal oracle-ike-proposal encryption-algorithm aes-256-cbc
set services ipsec-vpn ike proposal oracle-ike-proposal lifetime-seconds 28800
set services ipsec-vpn ike proposal oracle-ike-proposal dh-group group5
  
# Defining the IKE Policy for Oracle
# USER_DEFINED: Replace the parameters in the section below as needed
# If using IKEv1, uncomment the following two lines, and comment out the line after (the line with "version 2" at the end) 
# set services ipsec-vpn ike policy oracle-ike-policy-tunnel_2 mode main
# set services ipsec-vpn ike policy oracle-ike-policy-tunnel_2 version 1
  
set services ipsec-vpn ike policy oracle-ike-policy-tunnel_2 version 2
set services ipsec-vpn ike policy oracle-ike-policy-tunnel_2 proposals oracle-ike-proposal
set services ipsec-vpn ike policy oracle-ike-policy-tunnel_2 local-id ipv4_addr <cpe_public_ip_address>
set services ipsec-vpn ike policy oracle-ike-policy-tunnel_2 remote-id ipv4_addr <oracle_headend_2>
set services ipsec-vpn ike policy oracle-ike-policy-tunnel_2 pre-shared-key ascii-text <connection_presharedkey_2>
  
# Setting up Public Interface with the CPE Public IP.
# USER_DEFINED: Replace the parameters in the section below as needed
  
set interfaces <cpe_public_interface> unit 0 family inet address <cpe_public_ip_address>
 
  
# #2: IPSec Configuration
 
# Defining the IPSec (Phase 2) Proposal for Oracle
# The IPSec proposal defines the protocol, authentication, encryption, and lifetime parameters for the IPsec security association.
# The configuration template sets AES256 for encryption, SHA256 for authentication, enables PFS group 14, and sets the IPSec session key lifetime to 3600 seconds (1 hour).
# The IPsec policy incorporates the Diffie-Hellman group and the IPsec proposal.
# If different parameters are required, modify this template before applying the configuration.
  
set services ipsec-vpn ipsec proposal oracle-ipsec-proposal
set services ipsec-vpn ipsec proposal oracle-ipsec-proposal protocol esp
set services ipsec-vpn ipsec proposal oracle-ipsec-proposal authentication-algorithm hmac-sha-256-128
set services ipsec-vpn ipsec proposal oracle-ipsec-proposal encryption-algorithm aes-256-cbc
set services ipsec-vpn ipsec proposal oracle-ipsec-proposal lifetime-seconds 3600
 
# Defining the IPSec (PHASE 2) policy for Oracle
 
set services ipsec-vpn ipsec policy oracle-ipsec-policy perfect-forward-secrecy keys group14
set services ipsec-vpn ipsec policy oracle-ipsec-policy proposals oracle-ipsec-proposal
  
# Defining Security Association for Oracle
# USER_DEFINED: Replace the parameters in the section below as needed
# The IKE and IPSEC policies are associated with the tunnel interface. Eg: ms-2/3/0.101
# The IPsec Dead Peer Detection option causes periodic messages to be sent to ensure a Security Association remains operational.
  
set services ipsec-vpn rule oracle-vpn-tunnel_2 term 1 from ipsec-inside-interface <msInterface2>.<insideMsUnit2>
set services ipsec-vpn rule oracle-vpn-tunnel_2 term 1 then remote-gateway <oracle_headend_2>
set services ipsec-vpn rule oracle-vpn-tunnel_2 term 1 then dynamic ike-policy oracle-ike-policy-tunnel_2
set services ipsec-vpn rule oracle-vpn-tunnel_2 term 1 then dynamic ipsec-policy oracle-ipsec-policy
set services ipsec-vpn rule oracle-vpn-tunnel_2 term 1 then tunnel-mtu 1420
set services ipsec-vpn rule oracle-vpn-tunnel_2 term 1 then initiate-dead-peer-detection
set services ipsec-vpn rule oracle-vpn-tunnel_2 term 1 then dead-peer-detection
set services ipsec-vpn rule oracle-vpn-tunnel_2 term 1 then dead-peer-detection interval 5
set services ipsec-vpn rule oracle-vpn-tunnel_2 term 1 then dead-peer-detection threshold 4
set services ipsec-vpn rule oracle-vpn-tunnel_2 match-direction input
 
  
# #3: Tunnel Interface Configuration
  
# Defining the Tunnel Interfaces
# USER_DEFINED: Replace the parameters in the section below as needed.
  
set interfaces <msInterface2> unit <insideMsUnit2> description oracle-vpn-tunnel-2-INSIDE
set interfaces <msInterface2> unit <insideMsUnit2> family inet address <inside_tunnel_interface_ip_address>
set interfaces <msInterface2> unit <insideMsUnit2> service-domain inside
 
set interfaces <msInterface2> unit <outsideMsUnit2> description oracle-vpn-tunnel-2-OUTSIDE
set interfaces <msInterface2> unit <outsideMsUnit2> family inet
set interfaces <msInterface2> unit <outsideMsUnit2> service-domain outside
 
# #4: Service Set Configuration
 
# USER_DEFINED: Replace the parameters in the section below as needed
# Service set configuration to direct traffic to the tunnel interfaces and associating the appropriate IPSec-VPN-Rule.
 
set services service-set oracle-vpn-tunnel_2 next-hop-service inside-service-interface <msInterface2>.<insideMsUnit2>
set services service-set oracle-vpn-tunnel_2 next-hop-service outside-service-interface <msInterface2>.<outsideMsUnit2>
set services service-set oracle-vpn-tunnel_2 ipsec-vpn-options local-gateway <cpe_public_ip_address>
set services service-set oracle-vpn-tunnel_2 ipsec-vpn-rules oracle-vpn-tunnel-tunnel_2
  
# This option causes the router to reduce the Maximum Segment Size of TCP packets to prevent packet fragmentation.
  
set services service-set oracle-vpn_1 tcp-mss 1387
  
  
# #5a: Border Gateway Protocol (BGP) Configuration
  
# USER_DEFINED: Replace the parameters in the section below as needed                                         
# BGP is used within the tunnel to exchange prefixes between the dynamic routing gateway and your CPE. The DRG dynamically learns the routes from your on-premises network. On the Oracle side, the DRG advertises the VCN's subnets.
# THe configuration templates uses a basic route policy to advertise a default route to the DRG.
# To advertise additional prefixes to the Oracle VCN, add additional prefixes to the term ORACLE-DEFAULT policy. Make sure the prefix is present in the route table of the device with a valid next-hop.                                         
# You configure the local BGP Autonomous System Number (BGP ASN) when you set up the IPSec connection in the Oracle Console. If you later need to change the ASN, you must recreate the CPE object and IPSec connection in the Oracle Console. 
  
set policy-options policy-statement ORACLE-DEFAULT term default from route-filter 0.0.0.0/0 exact                              
set policy-options policy-statement ORACLE-DEFAULT term default then accept 
set policy-options policy-statement ORACLE-DEFAULT term reject then reject
  
set protocols bgp group ebgp type external
set protocols bgp group ebgp neighbor <inside_tunnel_interface_ip_address_neighbor> export ORACLE-DEFAULT
set protocols bgp group ebgp neighbor <inside_tunnel_interface_ip_address_neighbor> peer-as 31898
set protocols bgp group ebgp neighbor <inside_tunnel_interface_ip_address_neighbor> local-as <bgp_asn>
 
# #5b: Static Route Configuration
 
# USER_DEFINED: Replace the parameters in the section below as needed
# In case you plan to use static routing to get traffic through the IPSec tunnels, you can point the routes down to the tunnel interfaces. You should redistribute these routes into your on-premises network. Configuration for CPE to VCN static routes:
 
set routing-options static route <vcn_range> next-hop <msInterface2>.<insideMsUnit2>
 
 
##6: Routing Instances Configuration (Optional)
# USER_DEFINED: Replace the parameters in the section below as needed.
# If you are using routing-instances on your CPE, you need to make sure you account for them in your configuration. Merge the following configuration into the template provided above.
 
set routing-instances <customer_on-prem_to_oracle> interface <msInterface2>.<insideMsUnit2>
set routing-instances <internet_routing_instance> interface <msInterface2>.<outsideMsUnit2>
set services service-set oracle-vpn-tunnel-tunnel_2 ipsec-vpn-options local-gateway <cpe_public_ip_address> routing-instance <internet_routing_instance>
```

## Verification 🔗 
Use the following command to verify security associations (SAs).
Copy
```
show services ipsec-vpn ipsec security-associations detail

```

Use the following command to check the BGP status.
Copy
```

show bgp summary

```

Use the following commands to check the routes advertised to and received from Oracle Cloud Infrastructure. If you've configured the CPE to use routing instances, use the commands with `table` <table-name> at the end.
Copy
```

show route advertising-protocol bgp <neighbor-address>
 
show route receive-protocol bgp <neighbor-address>
			
show route advertising-protocol bgp <neighbor-address> table <table-name>
 
show route receive-protocol bgp <neighbor-address> table <table-name>
```

A [Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) is also available from Oracle Cloud Infrastructure to actively and passively monitor cloud resources. For information about monitoring a Site-to-Site VPN, see [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics).
If you have issues, see [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/ipsectroubleshoot.htm#VPN_Connect_Troubleshooting).
Was this article helpful?
YesNo

