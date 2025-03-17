Updated 2025-03-10
# Site-to-Site VPN Overview
Site-to-Site VPN provides a site-to-site IPSec connection between your on-premises network and your Virtual Cloud Network (VCN). The IPSec protocol suite encrypts IP traffic before the packets are transferred from the source to the destination and decrypts the traffic when it arrives. Site-to-Site VPN was previously referred to as VPN Connect and IPSec VPN.
Other secure VPN solutions include OpenVPN, a Client VPN solution that can be accessed in the [Oracle Marketplace](https://cloudmarketplace.oracle.com/marketplace/listing/67830324). OpenVPN connects individual devices to your VCN, but not whole sites or networks.
This topic gives an overview of Site-to-Site VPN for your VCN. For scenarios that include Site-to-Site VPN, see [Scenario B: Private Subnet with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#Scenario_B_Private_Subnet_with_a_VPN) and [Scenario C: Public and Private Subnets with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm#Scenario_C_Public_and_Private_Subnets_with_a_VPN). 
See [Site-to-Site VPN Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#VPN_Conn) and [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti) for limits-related information.
## Required Personnel and Knowledge 🔗 
Typically the following types of personnel are involved in setting up Site-to-Site VPN with Oracle Cloud Infrastructure: 
  * **Dev Ops team member** (or similar function) who uses the Oracle Cloud InfrastructureConsole to set up the cloud components required for the virtual network and Site-to-Site VPN.
  * **Network engineer** (or similar function) who configures the customer-premises equipment (CPE) device with information provided by the Dev Ops team member.


**Tip** The Dev Ops team member must have the required permission to create and manage the cloud components. If the person is the default administrator for your Oracle Cloud Infrastructure tenancy or a member of the [Administrators group](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm#The), then they have the required permission. For information about restricting access to your networking components, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
The personnel should be familiar with the following concepts and definitions:
  * The fundamentals of Oracle Cloud Infrastructure described in [Welcome to Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/Content/GSG/Concepts/baremetalintro.htm)
  * [The basic Networking service components](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Componen)
  * [General IPSec tunnel functionality](https://en.wikipedia.org/wiki/IPsec)



CLOUD RESOURCES
    Anything you provision on a cloud platform. For example, with Oracle Cloud Infrastructure, a cloud resource can refer to a VCN, compute instance, user, compartment, load balancer, or any other service component on the platform. 

ON-PREMISES
    A widely used term in cloud technologies that refers to your traditional data center environments. On-premises can refer to a colocation scenario, a dedicated floor space, a dedicated data center building, or a desktop running under your desk.  

ORACLE CLOUD IDENTIFIER (OCID)
     A unique identifier assigned to each resource that you provision on Oracle Cloud Infrastructure. The OCID is a long string that Oracle automatically generates. You can't choose the value for an OCID or change a resource's OCID. For more information, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
## About the Oracle IPSec Connection 🔗 
In general, an IPSec connection can be configured in the following modes:
  * **Transport mode:** IPSec encrypts and authenticates only the actual payload of the packet, and the header information stays intact.
  * **Tunnel mode (supported by Oracle):** IPSec encrypts and authenticates the entire packet. After encryption, the packet is then encapsulated to form a new IP packet that has different header information.


Oracle Cloud Infrastructure supports only the tunnel mode for IPSec VPNs.
Each Oracle IPSec connection consists of multiple redundant IPSec tunnels. For a given tunnel, you can use either Border Gateway Protocol (BGP) dynamic routing or static routing to route that tunnel's traffic. More details about routing follow.
Site-to-Site VPN IPSec tunnels offer the following advantages:
  * Public internet lines are used to transmit data, so dedicated, expensive lease lines from one site to another aren't necessary.
  * The internal IP addresses of the participating networks and nodes are hidden from external users.
  * The entire communication between the source and destination sites is encrypted, significantly lowering the chances of information theft.


## Routing for Site-to-Site VPN 🔗 
When you set up Site-to-Site VPN, it has two redundant IPSec tunnels. Oracle encourages you to configure your CPE device to use both tunnels (if your device supports it). Note that in the past, Oracle created IPSec connections that had up to four IPSec tunnels. 
The following three routing types are available, and you choose the routing type separately _for each IPSec tunnel_ in Site-to-Site VPN:
  * **BGP dynamic routing:** The available routes are learned dynamically through BGP. The DRG dynamically learns the routes from the on-premises network. On the Oracle side, the DRG advertises the VCN's subnets. 
  * **Static routing:** When you set up the IPSec connection to the DRG, you specify the particular routes to the on-premises network that you want the VCN to know about. You also must configure the CPE device with static routes to the VCN's subnets. These routes aren't learned dynamically.
  * **Policy-based routing:** When you set up the IPSec connection to the DRG, you specify the particular routes to the on-premises network that you want the VCN to know about. You also must configure the CPE device with static routes to the VCN's subnets. These routes aren't learned dynamically. 


### Important Routing Details for Site-to-Site VPN 🔗 
Here are important details to understand about routing for your Site-to-Site VPN:
  * **Routing choices:**
    * Originally, Site-to-Site VPN supported only static routing, and you were required to provide at least one static route for the overall IPSec connection. 
    * Now two different types of routing are available (BGP and static routing), and you configure the routing type _per tunnel_. _Only one type of routing at a time is supported for a given tunnel_. 
    * In general, Oracle encourages you to use the same routing type for all tunnels in your IPSec connection. Exception: if you're in the process of transitioning between static routing and BGP, then one tunnel might temporarily still use static routing while the other has already been switched to BGP.
    * When you create an IPSec connection, static routing is the default type of routing for all tunnels _unless you explicitly configure each tunnel to use BGP_.
  * **Routing information required:**
    * If you choose BGP, for each tunnel you must provide two IP addresses (one for each of the two BGP speakers in the tunnel's BGP session). The addresses must be in the encryption domain for the IPSec connection. You must also provide the BGP autonomous system number (BGP ASN) for your network. 
    * If you choose static routing, you must provide at least one static route (maximum 10). The static routes are configured with the _overall IPSec connection_ , so the same set of static routes are used for _all_ tunnels in the IPSec connection that are configured to use static routing. You can change the static routes at any time after creating the IPSec connection. If you're doing PAT between your CPE device and VCN, the static route for the IPSec connection is the PAT IP address. See [Example Layout with PAT](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_pat). 
    * If you choose static routing, you may optionally provide an IP address for each end of the tunnel for the purposes of tunnel troubleshooting or monitoring. 
    * If the tunnel is configured to use BGP, the IPSec connection's static routes are ignored. Any static routes associated with the IPSec connection are used for routing a given tunnel's traffic _only if that tunnel is configured to use static routing_. This is especially relevant if you have Site-to-Site VPN that uses static routing, but want to switch to using BGP.
  * **Changing the routing:**
    * If you want to change a tunnel from BGP to static routing, you must first ensure that the IPSec connection itself has at least one static route associated with it. 
    * You can change an existing tunnel's routing type at any time (unless the tunnel is currently being provisioned by Oracle). While you change the routing, the tunnel remains up (its IPSec status does not change). However, traffic flowing through the tunnel is disrupted temporarily during reprovisioning and while you reconfigure your CPE device. For information about making changes to Site-to-Site VPN, see [Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#Working_with_VPN_Connect).
    * Because you configure the routing type separately for each tunnel, if you want to switch your Site-to-Site VPN from static routing to BGP, you can do it one tunnel at a time. This avoids the entire IPSec connection being down. For instructions, see [Changing from Static Routing to BGP Dynamic Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#static_to_bgp).


### Route Advertisements and Path Preferences When You Have Multiple Connections 🔗 
When you use BGP, the DRG attached to your VCN advertises routes to your CPE. 
If you set up multiple connections between your on-premises network and VCN, you must understand what routes the DRG advertises and how to set path preferences to use your desired connection.
For important information, see [Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#Routing_Details_for_Connections_to_Your_OnPremises_Network).
### Preferring a Specific Tunnel in Site-to-Site VPN 🔗 
Within Site-to-Site VPN, you can influence _which tunnel_ is preferred. Here are items you can configure:
  * **Your CPE's BGP local preference:** If you use BGP, you can configure the BGP local preference attribute on your CPE device to control which tunnel is preferred for connections initiated from your on-premises network to your VCN. Because Oracle generally uses asymmetric routing, you must configure other attributes if you want Oracle to respond on that same tunnel. See the next two items.
  * **More specific routes on the preferred tunnel:** You can configure your CPE to advertise more specific routes for the tunnel that you want to prefer. Oracle uses the route with the [longest prefix match](https://en.wikipedia.org/wiki/Longest_prefix_match) when responding to or initiating connections. 
  * **AS path prepending:** BGP prefers the shortest AS path, so if you use BGP, you can use AS path prepending to control which tunnel has the shortest path for a given route. Oracle uses the shortest AS path when responding to or initiating connections.


## Overview of Site-to-Site VPN Components 🔗 
If you're not already familiar with the basic Networking service components, see [Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/landing.htm#top "Oracle Cloud Infrastructure Networking helps you set up virtual versions of traditional network components.") before proceeding.
When you set up Site-to-Site VPN for your VCN, you must create several Networking components. You can create the components with either the Console or the API. See the following diagram and description of the components.
[![This image shows the components of Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_ipsec_vpn.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_ipsec_vpn.svg)
Callout 1: Default VCN route table Destination CIDR | Route target  
---|---  
0.0.0.0/0 | DRG 

cpe object
    At your end of Site-to-Site VPN is the actual device in your on-premises network (whether hardware or software). The term _customer-premises equipment (CPE)_ is commonly used in some industries to refer to this type of on-premises equipment. When setting up the VPN, you must create a _virtual representation_ of the device. Oracle calls the virtual representation a CPE, but this documentation typically uses the term _CPE object_ to help distinguish the virtual representation from the actual CPE device. The CPE object contains basic information about your device that Oracle needs. A single CPE object public IP can have up to 8 IPSec connections. 

Dynamic Routing Gateway (DRG)
    At Oracle's end of Site-to-Site VPN is a virtual router called a dynamic routing gateway, which is the gateway into your VCN from your on-premises network. Whether you're using Site-to-Site VPN or [Oracle Cloud Infrastructure FastConnect private virtual circuits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") to connect your on-premises network and VCN, the traffic goes through the DRG. For more information, see [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs).     A network engineer might think of the DRG as the _VPN headend_. After creating a DRG, you must _attach_ it to your VCN, using either the Console or API. You must also add one or more route rules that route traffic from the VCN to the DRG. Without that DRG attachment and the route rules, traffic does not flow between your VCN and on-premises network. At any time, you can detach the DRG from your VCN but maintain all the remaining VPN components. You can then reattach the DRG, or attach it to another VCN.  

ipsec connection
    After creating the CPE object and DRG, you connect them by creating an IPSec connection, which you can think of as a parent object that represents the Site-to-Site VPN. The IPSec connection has its own **OCID**. When you create this component, you configure the type of routing to use for each IPSec tunnel, and you provide any related routing information. A single CPE object public IP can have up to 8 IPSec connections. 

TUNNEL
    An IPSec tunnel is used to encrypt traffic between secure IPSec endpoints. Oracle creates two tunnels in each IPSec connection for redundancy. Each tunnel has its own **OCID**. Oracle recommends that you configure your CPE device to support both tunnels in case one fails or Oracle takes one offline for maintenance. Each tunnel has configuration information that your network engineer needs when [configuring your CPE device](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration). This information includes an IP address and shared secret, as well as ISAKMP and IPSec parameters. You can use the [CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper) to gather the information that the network engineer needs. For more information, see [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices).   
### Access Control for the Components
For the purposes of access control, when you set up Site-to-Site VPN, you must specify the compartment where you want each of the components to reside. If you're not sure which compartment to use, put all the components in the same compartment as the VCN. Note that the IPSec tunnels always reside in the same compartment as the parent IPSec connection. For information about compartments and restricting access to your networking components, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
### Component Names and Identifiers
You can optionally assign a descriptive name to each of the components when you create them. These names don't have to be unique, although it's a best practice to use unique names across your tenancy. Avoid entering confidential information. Oracle automatically assigns each component an OCID. For more information, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
### If Your CPE Is Behind a NAT Device 🔗 
In general, the CPE IKE identifier configured on the on-premises end of the connection must match the CPE IKE identifier that Oracle is using. By default, Oracle uses the CPE's _public_ IP address, which you provide when you create the CPE object in the Oracle Console. However, if a CPE is behind a NAT device, the CPE IKE identifier configured on the on-premises end might be the CPE's _private_ IP address, as shown in the following diagram.
[![This image shows the CPE behind a NAT device, the public and private IP addresses, and the CPE IKE identifier.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_ipsec_vpn_cpe_ike_identifier.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_ipsec_vpn_cpe_ike_identifier.svg)
**Note** Some CPE platforms don't let you change the local IKE identifier. If you can't, you must change the remote IKE ID in the Oracle Console to match the CPE's local IKE ID. You can provide the value either when you set up the IPSec connection, or later, by editing the IPSec connection. Oracle expects the value to be either an IP address or a fully qualified domain name (FQDN) such as _cpe.example.com_. For instructions, see [Changing the CPE IKE Identifier That Oracle Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id).
### About the Tunnel Shared Secret 🔗 
Each tunnel has a shared secret. By default, Oracle assigns the shared secret to the tunnel unless you provide a shared secret yourself. You can provide a shared secret for each tunnel when you create the IPSec connection, or later after the tunnels are created. For the shared secret, only letters, numbers, and spaces are allowed. If you change an existing tunnel's shared secret, the tunnel goes down while it is being reprovisioned. 
For instructions, see [Changing the Shared Secret That an IPSec Tunnel Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_shared_secret).
## Resources for Configuring the CPE 🔗 
Your network engineer must configure the CPE at your end of the IPSec connection. To make it easier, Oracle provides these resources:
  * [CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper): A tool in the Oracle Console that generates a set of content that the network engineer can use when configuring the CPE.
  * [A list of verified CPE devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices): For each device, Oracle provides configuration instructions.
  * [A list of supported IPSec parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters): If your CPE is not on the list of verified devices, you can use this list of parameters to configure your CPE.


For more information, also see [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration).
## Monitoring Your Connection 🔗 
You can monitor the health, capacity, and performance of Oracle Cloud Infrastructure resources by using metrics, alarms, and notifications. For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
For information about monitoring your connection, [Site-to-Site VPN Metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ipsecmetrics2.htm#VPN_Connect_Metrics).
## What's Next? 🔗 
See these related topics:
  * [Site-to-Site VPN Wizard](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/quickstartIPsec.htm#VPN_Connect_Quickstart)
  * [Setting Up Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#Setting_Up_VPN)
  * [Supported IPSec Parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters)
  * [CPE Configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/configuringCPE.htm#CPE_Configuration)
  * [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices)
  * [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper)
  * [Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#Routing_Details_for_Connections_to_Your_OnPremises_Network)
  * [Working with Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#Working_with_VPN_Connect)
  * [Site-to-Site VPN FAQ](https://www.oracle.com/cloud/networking/site-to-site-vpn/faq/)
  * [Using the API for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#Using_the_API_for_VPN_Connect)


Was this article helpful?
YesNo

