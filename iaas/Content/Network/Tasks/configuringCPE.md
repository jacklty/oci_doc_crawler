Updated 2024-10-16
# CPE Configuration
This topic is for network engineers. It explains how to configure the on-premises device (the customer-premises equipment, or CPE) at your end of Site-to-Site VPN so traffic can flow between your on-premises network and Virtual Cloud Network (VCN). See these related topics:
  * [Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/landing.htm#top "Oracle Cloud Infrastructure Networking helps you set up virtual versions of traditional network components."): For general information about the parts of a VCN
  * [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\)."): For various topics about IPSec VPNs
  * [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices): For a list of CPE devices Oracle has verified


The following figure shows the basic layout of Site-to-Site VPN's IPSec connection using the internet. [IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec) is similar, but the traffic will only traverse a private virtual circuit.
[![This image summarizes the general layout of the IPSec connection and tunnels.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_configure_onpremise_router.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_configure_onpremise_router.svg)
## Requirements and Prerequisites 🔗 
There are several requirements and prerequisites to be aware of before moving forward. 
### Routing Considerations
For important details about routing for your Site-to-Site VPN see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
Oracle uses asymmetric routing across the multiple tunnels that make up the IPSec connection. Even if you configure one tunnel as primary and another as backup, traffic from your VCN to your on-premises network can use any tunnel that is "up" on your device. Configure your firewalls accordingly. Otherwise, ping tests or application traffic across the connection will not reliably work. 
If you use BGP dynamic routing with your Site-to-Site VPN, you can configure routing so that Oracle prefers one tunnel over the other. 
If you want to use [IPSec over FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectsecurity.htm#ipsec) you can't update a CPE object to add that functionality; support must be established at the CPE's initial setup. You also can't have the IPsec tunnels and virtual circuits for this connection use the same DRG route tables.
Note that the [Cisco ASA policy-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPE.htm#Cisco_ASA_Configuration_Options) uses a single tunnel.
### Creation of Cloud Network Components
You or someone in your organization must have already used the Oracle Console to create a VCN and an IPSec connection, which consists of multiple IPSec tunnels for redundancy. You must gather the following information about those components:
  * VCN OCID: The VCN [OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm) is a unique Oracle Cloud Infrastructure identifier that has a UUID at the end. You can use this UUID or any other string that helps you identify this VCN in the device configuration and doesn't conflict with other object-group or access-list names.
  * VCN CIDR 
  * VCN CIDR subnet mask
  * For each IPSec tunnel:
    * The IP address of the Oracle IPSec tunnel endpoint (the VPN headend)
    * The shared secret 


### Information About Your CPE Device 🔗 
You also need some basic information about the inside and outside interfaces of your on-premises device (your CPE). For a list of the required information for your particular CPE, see the links in this list: [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices).
By default, NAT-T is enabled on all Site-to-Site VPN IPSec tunnels. Oracle recommends leaving NAT-T enabled when configuring Site-to-Site VPN to OCI.
If your CPE is behind a NAT device, you can provide Oracle with your CPE's IKE identifier. For more information, see [Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components). 
A single CPE object public IP can have up to 8 IPSec connections.
### Route-Based Versus Policy-Based IPSec
The Oracle VPN headends use route-based tunnels, but can work with policy-based tunnels with some caveats. See [Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel) for full details. 
## Site-to-Site VPN Best Practices 🔗 
  * **Configure all tunnels for every IPSec connection:** Oracle deploys multiple IPSec headends for all your connections to provide high availability for your mission-critical workloads. Configuring all the available tunnels is a key part of the "Design for Failure" philosophy. (Exception: [Cisco ASA policy-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPE.htm#Cisco_ASA_Configuration_Options), which uses a single tunnel.)
  * **Have redundant CPEs in your on-premises locations:** Each of your sites that connects with IPSec to Oracle Cloud Infrastructure should have redundant CPE devices. You add each CPE to the Oracle Cloud Infrastructure Console and create a separate IPSec connection between your **Dynamic Routing Gateway (DRG)** and each CPE. For each IPSec connection, Oracle provisions two tunnels on geographically redundant IPSec headends. Oracle may use any tunnel that is "up" to send traffic back to your on-premises network. For more information, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
  * **Consider backup aggregate routes:** If you have multiple sites connected via IPSec VPNs to Oracle Cloud Infrastructure, and those sites are connected to your on-premises backbone routers, consider configuring your IPSec connection routes with both the local site aggregate route as well as a default route.
Note that the DRG routes learned from the IPSec connections are only used by traffic you route from your VCN to your DRG. The default route will only be used by traffic sent to your DRG whose destination IP address does not match the more specific routes of any of your tunnels.


## Confirming the Status of the Connection 🔗 
After you configure the IPSec connection, you can test the connection by launching an instance into the VCN and then pinging it from your on-premises network. For information about launching an instance, see [Launching an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). To ping the instance, the VCN's security rules must [allow ping traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#ping).
You can get the status of the IPSec tunnels in the API or Console. For instructions, see [To view the status and configuration information for the IPSec tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#get_tunnel_status_config).
## Device Configurations 🔗 
For links to the specific configuration information for each verified CPE device, see [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices).
Was this article helpful?
YesNo

