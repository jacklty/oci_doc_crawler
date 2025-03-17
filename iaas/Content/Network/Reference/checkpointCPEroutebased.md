Updated 2025-03-10
# Check Point: Route-Based
This topic provides a route-based configuration for Check Point CloudGuard. The instructions were validated with Check Point CloudGuard version R80.20.
**Important**
Oracle provides configuration instructions for a tested set of [vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices). Use the correct configuration for the vendor and software version. 
If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes. 
If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of [supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and consult the vendor's documentation for help.
This topic is for route-based (VTI-based) configuration. If you instead want policy-based configuration, see [Check Point: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEpolicybased.htm#Check_Point_PolicyBased). Policy-based routing is mentioned in passing in this article, we advise that you understand both methods.
Check Point experience is required. This topic does not include how to add Check Point CloudGuard Security Gateway to Check Point CloudGuard Security Manager. For more information about using Check Point products, see the Check Point documentation.
**Important**
Oracle provides configuration instructions for a tested set of [vendors and devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices). Use the correct configuration for the vendor and software version. 
If the device or software version that Oracle used to verify the configuration doesn't exactly match the device or software, you might still create the necessary configuration on the device. Consult the vendor's documentation and make any necessary changes. 
If the device is from a vendor not in the list of verified vendors and devices, or if you're already familiar with configuring the device for IPSec, see the list of [supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and consult the vendor's documentation for help.
Oracle Cloud Infrastructure offers Site-to-Site VPN, a secure IPSec connection between your on-premises network and a virtual cloud network (VCN).
The following diagram shows a basic IPSec connection to Oracle Cloud Infrastructure with redundant tunnels. IP addresses used in this diagram are for example purposes only.
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
See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
### Asymmetric Routing
Oracle uses asymmetric routing across the tunnels that make up the IPSec connection. Configure firewalls with that in mind. Otherwise, ping tests or application traffic across the connection don't work reliably. 
When you use several tunnels to Oracle Cloud Infrastructure, We recommend that you configure routing to deterministically route traffic through the preferred tunnel. To use one IPSec tunnel as primary and another as backup, configure more-specific routes for the primary tunnel (BGP) and less-specific routes (summary or default route) for the backup tunnel (BGP/static). Otherwise, if you advertise the same route (for example, a default route) through all tunnels, return traffic from a VCN to an on-premises network routes to any of the available tunnels. This is because Oracle uses asymmetric routing.
For specific Oracle routing recommendations about how to force symmetric routing, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing). 
### Route-Based or Policy-Based IPSec Connection
The IPSec protocol uses Security Associations (SAs) to decide how to encrypt packets. Within each SA, you define encryption domains to map a packet's source and destination IP address and protocol type to an entry in the SA database to define how to encrypt or decrypt a packet. 
**Note** Other vendors or industry documentation might use the term _proxy ID, security parameter index (SPI)_ , or _traffic selector_ when referring to SAs or encryption domains.
There are two general methods for implementing IPSec tunnels:
  * **Route-based tunnels:** Also called _next-hop-based tunnels_. A route table lookup is performed on a packet's destination IP address. If that route's egress interface is an IPSec tunnel, the packet is encrypted and sent to the other end of the tunnel. 
  * **Policy-based tunnels:** The packet's source and destination IP address and protocol are matched against a list of policy statements. If a match is found, the packet is encrypted based on the rules in that policy statement.


The Oracle Site-to-Site VPN headends use route-based tunnels but can work with policy-based tunnels with some caveats listed in the following sections. 
[Encryption domain for route-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm)
If the CPE supports route-based tunnels, use that method to configure the tunnel. This is the simplest configuration with the most interoperability with the Oracle VPN headend. 
Route-based IPSec uses an encryption domain with the following values:
  * **Source IP address:** Any (0.0.0.0/0)
  * **Destination IP address:** Any (0.0.0.0/0)
  * **Protocol:** IPv4


If you need to be more specific, you can use a single summary route for encryption domain values instead of a default route.
[Encryption domain for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm)
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
## CPE Configuration (Route-Based) 🔗 
**Important**
The configuration instructions in this section are provided by Oracle Cloud Infrastructure for this CPE. If you need support or further help, contact the CPE vendor's support directly.
The following figure shows the basic layout of the IPSec connection. 
[![This image summarizes the general layout of the IPSec connection and tunnels.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_configure_onpremise_router.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_configure_onpremise_router.svg)
### About Using IKEv2
Oracle supports Internet Key Exchange version 1 (IKEv1) and version 2 (IKEv2). If you [configure the IPSec connection in the Console to use IKEv2](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#using_ikev2), you must configure your CPE to use only IKEv2 and related IKEv2 encryption parameters that your CPE supports. For a list of parameters that Oracle supports for IKEv1 or IKEv2, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters). 
If you want to use IKEv2, there's a variation on one of the tasks presented in the next section. Specifically, in [task 4](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#task4), when configuring encryption, select **IKEv2 only** for the encryption method. 
### Redundancy with BGP Over IPSec
For redundancy, Oracle recommends using BGP over IPSec. By default, if you have two connections of the same type (for example, two IPSec VPNs that both use BGP), and you advertise the same routes across both connections, Oracle prefers the oldest established route when responding to requests or initiating connections. If you want to force routing to be symmetric, Oracle recommends using BGP and AS path prepending with your routes to influence which path Oracle uses when responding to and initiating connections. For more information, see [Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#Routing_Details_for_Connections_to_Your_OnPremises_Network).
The Oracle DRG uses /30 or /31 as subnets for configuring IP addresses on the interface tunnels. Remember that the IP address must be part of Site-to-Site VPN's encryption domain and must be allowed in the firewall policy to reach the peer VPN through the interface tunnel. You might need to implement a static route through the tunnel interface for the peer IP address.
Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. If you're configuring Site-to-Site VPN for the Government Cloud, see [Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#vpn_params) and also [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn).
For your side, you can use a private ASN. Private ASNs are in the range 64512–65534.
[Task 1: InstallSite-to-Site VPN on Check Point CloudGuard Security Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm)
**Prerequisite:** Before starting, add Check Point CloudGuard Security Gateway to Check Point CloudGuard Security Manager. Also establish the Secure Internal Communication (SIC) so you can configure the IPSec tunnel by using the Check Point Smart Console. For instructions to add the Security Gateway to CloudGuard or to establish the SIC, see the Check Point documentation. 
[![This image illustrates the prerequisite.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_prereq.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_prereq.png)
  1. Install the IPSec VPN module. Oracle recommends that you also install the Monitoring module for traffic analysis.
[![This image shows where to enable the IPSec VPN module.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_install_ipsec_module.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_install_ipsec_module.png)
  2. Click **OK** to save your changes.


[Task 2: Create the VTI interface from GAIA](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm)
In this task, you configure a VTI interface that passes traffic by using routing rules from the VTI interface to the newly created IPSec tunnel.
  1. Log in to the GAIA portal using the Check Point CloudGuard Security Gateway public or private IP address.
  2. On the GAIA portal, select the **Advanced** view.
  3. Under **Network Management** , go to **Network Interfaces**.
  4. Click **Add** , and then click **VPN Tunnel**.
[![This image shows where to add a VPN tunnel in the GAIA portal.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_gaia_add_vpn_tunnel.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_gaia_add_vpn_tunnel.png)
  5. Specify the following items:
     * **VPN Tunnel ID:** A number that will be added to the VTI interface called vpnt*, where the asterisk is the VPN tunnel ID number specified . For VPN tunnel ID = 1, the interface is labeled vpnt1.
     * **Peer:** The name of the interoperable device that you created earlier for the IPSec tunnel. In this case, the name is OCI-VPN_BGP1.
**Important** If the name you specify here does not match the name of the interoperable device, traffic does not flow through the IPSec tunnel.
     * **Numbered:** Select **Numbered** to create a numbered interface.
     * **Local Address:** The local IP address that was specified in the Oracle Console as the **Inside Tunnel Interface - CPE**.
     * **Remote Address:** The remote IP address that was specified in the Oracle Console as the **Inside Tunnel Interface - Oracle**.
[![This image shows the VPN tunnel parameters to configure in the GAIA portal.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_gaia_configure_vpn_tunnel.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_gaia_configure_vpn_tunnel.png)
  6. Click **OK**.
  7. Under **Network Management** , go to **IPv4 Static Routes**.
  8. Specify the following items:
     * **Static route for the Oracle IP address:** Add an IP address with /32 mask for the remote IP address that was specified in the Oracle Console as the **Inside Tunnel Interface - Oracle**.
     * **Static routes to the VCN subnets:** If you're using static routing for this IPSec connection to Oracle, add at least one subnet for the Oracle VCN to be reached through the IPSec tunnel. The following screenshot shows a static route to 172.31.2.0/26. If you're using BGP for this IPSec connection to Oracle, skip this item because thoe routes are learned through BGP (see the next section).
[![This image shows the static routes to configure in the GAIA portal.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_gaia_add_static_routes.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_gaia_add_static_routes.png)
Now all traffic with a specific destination learned from a static route will pass through the newly created IPSec tunnel.
  9. Get the interfaces and verify that the VPN tunnel is in the list:
    1. In the Smart Console, go to **Gateways & Servers**.
    2. Select the **Check Point Security Gateways** , and double-click.
    3. Under **General Properties** , on the **Network Management** page, select **Get Interfaces**.
The VPN tunnel interface should appear in the list.
  10. To force a route-based VPN to take priority, create an empty group and assign it to the VPN domain:
    1. On the **VPN Domain** page, select **Manually defined** , and then select **Create empty group**.
    2. Click **New** , select **Group** , and then select **Simple Group**.
    3. Enter an **Object Name** , and then click **OK**. Do not assign any objects to this empty group.
[![This image shows the empty group for the VPN domain.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_empty_group.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_empty_group.png)


[Task 3: Create an interoperable device](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm)
Later, you will create a VPN Community. Before you can, you must create an **Interoperable Device** that will be used in Check Point CloudGuard Security Gateway to define the Oracle DRG.
  1. Create the new interoperable device.
[![This image shows where to create a new interoperable device.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_create_interoperable_device.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_create_interoperable_device.png)
  2. On the **General Properties** page of the new interoperable device, add a name to identify the IPSec tunnel. Enter the IP address that Oracle assigned for the Oracle end of the tunnel when creating the IPSec connection.
[![This image shows where to configure the interoperable device.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_configure_interoperable_device.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_configure_interoperable_device.png)
  3. To force the route-based VPN to take priority, you must create an empty group and assign it to the VPN domain. To do that, on the **Topology** page, in the **VPN Domain** section, select **Manually defined** , and select the empty group.
  4. On the **IPSec VPN** page, you can optionally add the new interoperable device to an existing VPN Community. You can skip this step if you don't yet have any VPN Communities created. 
Notice that you skip the **Traditional mode configuration** , because you will define all the Phase 1 and Phase 2 parameters in the VPN Community in a later step. The VPN Community applies those parameters to all interoperable devices that belong to the VPN Community.
[![This image shows where to add the interoperable device to a VPN community.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_interoperable_device_add_to_community.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_interoperable_device_add_to_community.png)
  5. On the **Link Selection** page, under **Always use this IP address** , select **Main address** , which was the address you specified when creating the interoperable device. If necessary, you can use a specific IP address that will be used as the IKE ID. 
[![This image shows where to specify the address to use for the interoperable device.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_interoperable_device_main_address.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_interoperable_device_main_address.png)
  6. On the **VPN Advanced** page, select **Use the community settings** , which applies all the options and values in the VPN Community, including the Phase 1 and Phase 2 parameters. 
[![This image shows where to specify advanced VPN settings.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_interoperable_device_vpn_advanced.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_interoperable_device_vpn_advanced.png)
  7. Click **OK** to save your changes.


[Task 4: Create a VPN community](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm)
  1. Go to **Security Policies** , and then from **Access Tools** , select **VPN Communities**.
  2. Create a **Star Community**.
[![This image shows where to create a VPN community.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_vpn_community_create.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_vpn_community_create.png)
  3. For the star community, add a name. 
  4. On the **Gateways** page, select the values for **Center Gateways** and **Satellite Gateways**. This star community acts as a settings template for the interoperable devices you specify in **Center Gateways** and **Satellite Gateways**. 
     * **Center Gateways** : For the Check Point CloudGuard Security Gateway.
     * **Satellite Gateways** : For the CPE that connects to the Oracle DRG for each IPSec tunnel.
[![This image shows where to configure the gateways for the VPN community.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_vpn_community_gateways.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_vpn_community_gateways.png)
  5. To allow traffic, go to **Global Properties** , and then **VPN** , and then **Advanced**. 
[![This image shows where to find the global properties.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_global_properties.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_global_properties.png)
[![This image shows where to find the VPN advanced properties to allow traffic.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_global_properties_vpn_advanced.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_global_properties_vpn_advanced.png)
  6. Select **Enable VPN Directional Match in VPN Column**. Later you will create a security policy that uses a directional match condition to allow traffic to pass based on routing rules.
  7. Click **OK**.
  8. On the **Encryption** page, configure the Phase 1 and Phase 2 parameters that Oracle supports. For a list of those values, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters).
If you're configuring Site-to-Site VPN for the Government Cloud, see [Required Site-to-Site VPN Parameters for Government Cloud](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#vpn_params).
Notice that if you want to use IKEv2, for the **Encryption Method** , instead select **IKEv2 only**.
[![This image shows where you can configure the Phase 1 and Phase 2 parameters.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_vpn_community_encryption.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_vpn_community_encryption.png)
  9. On the **Tunnel Management** page, select **Set Permanent Tunnels**. Oracle recommends that you:
     * Select **On all tunnels in the community** to keep all the Oracle IPSec tunnels up all the time.
     * In the **VPN Tunnel Sharing** section, select **One VPN tunnel per Gateway pair**.
The latter option generates only one pair of IPSec security associations (SAs), and each SA with only one security parameter index (SPI) (unidirectional).
When you use policy-based tunnels, every policy entry generates a pair of IPSec SAs, (also referred to as an _encryption domain_).
**Important** The Oracle VPN headend can support multiple encryption domains, but there are limitations. See [Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel) for full details. 
Oracle creates a route-based IPSec connection, which means that everything is routed through an encryption domain that has 0.0.0.0/0 (any) for local traffic and 0.0.0.0/0 (any) for remote traffic. For more information, see [Supported Encryption Domain or Proxy ID](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#Supported_Encryption_Domain_or_Proxy_ID).
[![This image shows where you can configure tunnel management options.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_vpn_community_tunnel_management.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_vpn_community_tunnel_management.png)
  10. On the **Shared Secret** page, select **Use only Shared Secret for all external members** , and add the shared secret that Oracle generated for the tunnel when creating the IPSec connection. 
Currently Oracle supports only shared secret keys. Note that you can [change the shared secret](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_shared_secret) in the Oracle Console.
[![This image shows where you can specify the shared secret for the tunnel.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_vpn_community_shared_secret.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_vpn_community_shared_secret.png)
  11. Click **OK** to save your changes.


[Task 5: Create a security policy](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm)
  1. Go to **Access Control** , and then the **Policy** tab. Create specific security policies by using **Directional Match Condition** , which allows traffic to pass based on route tables. Set up the condition with these settings:
     * **Internal_Clear** > _VPN Community_ created
     * _VPN Community_ created > _VPN Community_ created
     * _VPN Community_ created > **Internal_Clear**
In this case, the _VPN Community_ is **OCI-DRG-BGP** and the **Internal_Clear** is predefined by Check Point.
[![This image shows how to configure the security policy directional match condition.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_security_policy_condition.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_security_policy_condition.png)
  2. Click **OK** to save your changes.
  3. Click **Install Policy** to apply the configuration.
[![This image shows where to click Install Policy.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_install_policy.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_policy_install_policy.png)


[Task 6: Enable BGP](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm)
Perform the following steps for each tunnel.
  1. Go to **Advanced Routing,** and then **BGP**.
  2. Under **BGP Global Settings** , click **Change Global Settings** , and then add a router ID and local ASN.
[![This image shows where to change the BGP global settings.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_bgp_change_global_settings.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_bgp_change_global_settings.png)
  3. Click **Save**.


[Task 7: Redistribute routes into BGP](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm)
  1. Go to **Advanced Routing,** and then **Route Distribution**.
  2. Click **Add Redistribution From** , and then select **Interface** , which is for adding all connected subnets.
[![This image shows where to configure route distribution.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_bgp_route_distribution.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_bgp_route_distribution.png)
  3. In the **Add Redistribution from Interface** dialog, configure the following items:
     * **To Protocol:** Select **BGP AS 31898**. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. If you're configuring Site-to-Site VPN for the Government Cloud, see [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn).
     * **Interface:** Select **all** to advertise all connected subnets.
[![This image shows the Add Redistribution from Interface dialog.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_bgp_route_distribution_from_interface.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_checkpoint_route_bgp_route_distribution_from_interface.png)
  4. Click **Save**.


Now the BGP session should be up and advertising and receiving subnets.
## Verification 🔗 
The following CLI command verifies BGP peers and routing.
Copy
```
show bgp peers
```

The following command verifies that you're receiving BGP routes.
Copy
```
show route bgp
```

The following command verifies the routes that are being advertised. In this example, replace <remote_IP_address> with the remote IP address that was specified in the Oracle Console as the **Inside Tunnel Interface - Oracle**
Copy
```
show bgp peer <remote_IP_address> advertise 
```

The following command verifies the routes that are being received.
Copy
```
show bgp peer <remote_IP_address> received
```

Use options 2 and 4 in the following command to verify security associations (SAs).
Copy
```

vpn tunnelutil

**********   Select Option   **********

(1)        List all IKE SAs
(2)       * List all IPsec SAs
(3)        List all IKE SAs for a given peer (GW) or user (Client)
(4)       * List all IPsec SAs for a given peer (GW) or user (Client)
(5)        Delete all IPsec SAs for a given peer (GW)
(6)        Delete all IPsec SAs for a given User (Client)
(7)        Delete all IPsec+IKE SAs for a given peer (GW)
(8)        Delete all IPsec+IKE SAs for a given User (Client)
(9)        Delete all IPsec SAs for ALL peers and users
(0)        Delete all IPsec+IKE SAs for ALL peers and users

* To list data for a specific CoreXL instance, append "-i <instance number>" to your selection.

(Q)        Quit

*******************************************
```

A [Monitoring service](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) is also available from Oracle Cloud Infrastructure to actively and passively monitor cloud resources. For information about monitoring a Site-to-Site VPN, see [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics).
If you have issues, see [Site-to-Site VPN Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/ipsectroubleshoot.htm#VPN_Connect_Troubleshooting).
Was this article helpful?
YesNo

