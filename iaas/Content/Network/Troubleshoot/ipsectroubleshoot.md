Updated 2024-12-16
# Site-to-Site VPN Troubleshooting
Create a service request at [My Oracle Support](http://support.oracle.com/)
This topic covers the most common troubleshooting issues for Site-to-Site VPN. Some suggestions assume that you are a network engineer with access to your CPE device's configuration.
## Log Messages
Viewing log messages generated for various operational aspects of Site-to-Site VPN can be a valuable aid in troubleshooting many of the issues presented during operation. Enabling and accessing the Site-to-Site VPN log messages can be done via Site-to-Site VPN or the Logging service.
  * For an overview of the Logging service in general, refer to the [Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm)
  * For details on enabling and accessing the Site-to-Site VPN log messages via the logging service, refer to [Service Logs](https://docs.oracle.com/iaas/Content/Logging/Concepts/service_logs.htm)
  * For details on enabling and accessing the Site-to-Site VPN log messages via the Networking service, refer to [Viewing Site-to-Site VPN Log Messages](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#viewing_your_vpn_connect_log_messages).
  * For details on the Site-to-Site VPN log message schema, refer to [Details for Site-to-Site VPN](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_vpn_connect.htm).


Refer to the table below for a better interpretation of IPsec VPN log messages , which lists of the different tunnel-down scenarios and the possible logs seen on the OCI console.
Interpreting Console Logs Tunnel down reason | Logs populated in OCI logging section  
---|---  
Mismatched IKE version |  `STATE_V2_PARENT_I1: 60 second timeout exceeded after 7                     retransmits. No response (or no acceptable response) to our                     first IKEv2 message` `dropping unexpected IKE_SA_INIT message containing                     NO_PROPOSAL_CHOSEN notification; message payloads: N;                     missing payloads: SA,KE,Ni` `received and ignored notification payload:                     NO_PROPOSAL_CHOSEN_date_time ep_85 pluto[68971]: "xxxxxxx"                     #xxx: set ikev1 error <14>`  
Mismatched subnets |  `No IKEv2 connection found with compatible Traffic                     Selectors` `responding to CREATE_CHILD_SA message (ID 30) from                     CPE_PUBLIC_IP:4500 with encrypted notification                     TS_UNACCEPTABLE` `cannot respond to IPsec SA request because no connection                     is known for                     MISMATCHED_SOURCE_SUBNET===VPN_PUBLIC_IP[+S?C]...VPN_PUBLIC_IP[+S?C]===MISMATCHED_DESTINATION_SUBNET`  
Mismatched Pre-shared key |  ` STATE_MAIN_I3: 60 second timeout exceeded after 7                     retransmits. Possible authentication failure: no acceptable                     response to our first encrypted messag` `IKE SA authentication request rejected by peer:                     AUTHENTICATION_FAILED` `authentication failed: computed hash does not match hash                     received from peer ID_IPV4_ADDR 'VPN_PUBLIC_IP'` `responding to IKE_AUTH message (ID 1) from                     VPN_PUBLIC_IP:4500 with encrypted notification                     AUTHENTICATION_FAILED`  
Proposal mismatched |  `OAKLEY proposal refused: missing encryption ` `Oakley Transform [AES_CBC (128), HMAC_SHA2_256, DH19]                     refused` `no acceptable Oakley Transform` `sending notification NO_PROPOSAL_CHOSEN to                     VPN_PUBLIC_IP:500` `failed to add connection: ESP DH algorithm 'modp1024' is                     not supported` `received unauthenticated v2N_NO_PROPOSAL_CHOSEN -                     ignored`  
Mismatched PFS |  `ignoring informational payload NO_PROPOSAL_CHOSEN,                     msgid=xxxxxx, length=12` `received and ignored notification payload:                     NO_PROPOSAL_CHOSEN` `dropping unexpected ISAKMP_v2_CREATE_CHILD_SA message                     containing v2N_INVALID_SYNTAX notification; message                     payloads: SK; encrypted payloads: N; missing payloads:                     SA,Ni,TSi,TSr` `"xxxxxxxx"[1] VPN_PUBLIC_IP #580: encountered fatal error                     in state STATE_V2_REKEY_CHILD_I`  
Mismatched IKE ID |  `Peer ID 'MISMATCHED_IKE_ID_IP_ADDRESS' mismatched on                     first found connection and no better connection                     found` `sending encrypted notification INVALID_ID_INFORMATION to                     VPN_PUBLIC_IP:4500`  
## Tunnel Flapping
**Interesting traffic at all times:** In general, Oracle recommends having interesting traffic running through the IPSec tunnels at all times if your CPE supports it. Cisco ASA requires that you configure SLA monitoring, which keeps interesting traffic running through the IPSec tunnels. For more information, see the section for "IP SLA Configuration" in the [Cisco ASA policy-based configuration template](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#CPE). 
**Multiple IPSEC Connections:** You can use two IPSec connections for redundancy. If both IPSec connections have only a default route (0.0.0.0/0) configured, traffic will route to either of those connections because Oracle uses asymmetric routing. If you want one IPSec connection as primary and another one as backup, configure more-specific routes for the primary connection and less-specific routes (or the default route of 0.0.0.0/0) on the backup connection.
**Local IKE identifier:** Some CPE platforms do not allow you to change the local IKE identifier. If you cannot, you must change the remote IKE ID in the Oracle Console to match your CPE's local IKE ID. You can provide the value either when you set up the IPSec connection, or later, by editing the IPSec connection. Oracle expects the value to be either an IP address or a fully qualified domain name (FQDN) such as _cpe.example.com_. For instructions, see [Changing the CPE IKE Identifier That Oracle Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id).
**Maximum Transmission Unit (MTU):** The standard internet MTU size is 1500 bytes. For more information on how to determine your MTU please see [Overview of MTU](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/connectionhang.htm#Overview).
## CPE Configuration
**Local IKE identifier:** Some CPE platforms do not allow you to change the local IKE identifier. If you cannot, you must change the remote IKE ID in the Oracle Console to match your CPE's local IKE ID. You can provide the value either when you set up the IPSec connection, or later, by editing the IPSec connection. Oracle expects the value to be either an IP address or a fully qualified domain name (FQDN) such as _cpe.example.com_. For instructions, see [Changing the CPE IKE Identifier That Oracle Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/workingwithIPsec.htm#edit_cpe_ike_id).
**Cisco ASA: Policy Based:** Oracle recommends using a [route-based configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm#Cisco_ASA_RouteBased) to avoid interoperability issues and to achieve tunnel redundancy with a single Cisco ASA device. 
The Cisco ASA does not support route-based configuration for software versions older than 9.7.1. For the best results, if your device allows it, Oracle recommends that you upgrade to a software version that supports route-based configuration.
With policy-based configuration, you can configure only a single tunnel between your Cisco ASA and your Dynamic Routing Gateway (DRG).
**Multiple Tunnels** If you have multiple tunnels up simultaneously, ensure that your CPE is configured to handle traffic coming from your VCN on any of the tunnels. For example, you need to disable ICMP inspection, configure TCP state bypass, and so on. For more details about the appropriate configuration, contact your CPE vendor's support.
## Encryption Domain Issues
The Oracle VPN headends use route-based tunnels, but can work with policy-based tunnels with some caveats. See [Encryption domains for policy-based tunnels](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/ipsecencryptiondomains.htm#spi_policy_based_tunnel) for full details. 
**Stateful security list rules:** If you're using [stateful security list rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful) (for TCP, UDP, or ICMP traffic), you don't need to ensure that your security list has an explicit rule to allow ICMP type 3 code 4 messages because the Networking service tracks the connections and automatically allows those messages. Stateless rules require an explicit ingress security list rule for ICMP type 3 code 4 messages. Confirm that the instance firewalls are set up correctly. 
## General Site-to-Site VPN Issues 🔗 
### IPSec tunnel is DOWN 🔗 
Check these items:
  * **Basic configuration** : The IPSec tunnel consists of both phase-1 and phase-2 parameters. Confirm that both are configured correctly. You can configure the CPE phase 1 and phase 2 parameters in the OCI end using custom configurations. To use custom configurations on the tunnel, go to advanced options and enable **set custom configurations**. This allows you to manually define phase 1 and phase 2 parameters on the OCI end. 
Oracle has also recommended certain parameters for phase 1 and phase 2. See the parameters for [phase-1 (ISAKMP) and phase-2 (IPSec) configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) and use those parameters if the above step does not bring up the tunnel. For more information on configuring CPE device, see the configuration appropriate for your CPE device:
    * [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices)
    * [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper)
    * Checkpoint:
      * [Check Point: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#Check_Point_RouteBased)
      * [Check Point: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEpolicybased.htm#Check_Point_PolicyBased)
    * Cisco ASA:
      * [Cisco ASA: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm#Cisco_ASA_RouteBased)
      * [Cisco ASA: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#Cisco_ASA_PolicyBased)
    * [Cisco IOS](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoiosCPE.htm#Cisco_IOS)
    * [FortiGate](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/fortigateCPE.htm#FortiGate)
    * [Furukawa Electric](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/furukawaCPE.htm#Furukawa_Electric "Learn how to configure a Furukawa Electric router for Site-to-Site VPN between your on-premises network and cloud network.")
    * [Juniper MX](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/junipermxCPE.htm#Juniper_MX)
    * [Juniper SRX](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/junipersrxCPE.htm#Juniper_SRX)
    * [Libreswan](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm#Libreswan)
    * [NEC IX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/necixCPE.htm#NEC_IX_Series)
    * [Openswan](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/openswanCPE.htm#Openswan)
    * [Palo Alto](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#Palo_Alto)
    * [WatchGuard](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/watchguardCPE.htm#WatchGuard)
    * [Yamaha RTX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/yamahartx.htm#Yamaha_RTX_Series)
  * **Local and remote proxy IDs:** If you're using a policy-based configuration, check if the CPE is configured with more than one pair of local and remote proxy IDs (subnets). The Oracle VPN router supports only one pair on older connections. If the CPE has more than one pair, update the configuration to include only one pair, and choose one of the following two options: 
Option  | Local Proxy ID | Remote Proxy ID  
---|---|---  
1 | ANY (or 0.0.0.0/0) | ANY (or 0.0.0.0/0)  
2 | On-premises CIDR (an aggregate that covers all the subnets of interest) | VCN's CIDR  
  * **NAT device:** If the CPE is behind a NAT device, the CPE IKE identifier configured on your CPE might not match the CPE IKE identifier Oracle is using (the public IP address of your CPE). If your CPE does not support setting the CPE IKE identifier on your end, you can provide Oracle with your CPE IKE identifier in the Oracle Console. For more information, see [Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components). 


### IPSec tunnel is UP, but no traffic is passing through 🔗 
Check these items:
  * **Phase 2 (IPSec) configuration:** Confirm that the [phase 2 (IPSec) parameters](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters) are configured correctly on your CPE device. See the configuration appropriate for your CPE device:
List of configurations 
    * [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices)
    * [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper)
    * Checkpoint:
      * [Check Point: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#Check_Point_RouteBased)
      * [Check Point: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEpolicybased.htm#Check_Point_PolicyBased)
    * Cisco ASA:
      * [Cisco ASA: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm#Cisco_ASA_RouteBased)
      * [Cisco ASA: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#Cisco_ASA_PolicyBased)
    * [Cisco IOS](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoiosCPE.htm#Cisco_IOS)
    * [FortiGate](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/fortigateCPE.htm#FortiGate)
    * [Furukawa Electric](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/furukawaCPE.htm#Furukawa_Electric "Learn how to configure a Furukawa Electric router for Site-to-Site VPN between your on-premises network and cloud network.")
    * [Juniper MX](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/junipermxCPE.htm#Juniper_MX)
    * [Juniper SRX](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/junipersrxCPE.htm#Juniper_SRX)
    * [Libreswan](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm#Libreswan)
    * [NEC IX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/necixCPE.htm#NEC_IX_Series)
    * [Openswan](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/openswanCPE.htm#Openswan)
    * [Palo Alto](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#Palo_Alto)
    * [WatchGuard](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/watchguardCPE.htm#WatchGuard)
    * [Yamaha RTX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/yamahartx.htm#Yamaha_RTX_Series)
  * **VCN security lists:** Ensure you've set up the [VCN security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) to allow the desired traffic (both ingress and egress rules). Note that the VCN's [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) does not allow ping traffic (ICMP type 8 and ICMP type 0). You must add the appropriate ingress and egress rules to allow ping traffic.
  * **Firewall rules:** Ensure that your firewall rules allow both ingress and egress traffic with the Oracle VPN headend IPs and the VCN CIDR block.
  * **Asymmetric routing:** Oracle uses asymmetric routing across the multiple tunnels that make up the IPSec connection. Even if you configure one tunnel as primary and another as backup, traffic from your VCN to your on-premises network can use any tunnel that is "up" on your device. Configure your firewalls accordingly. Otherwise, ping tests or application traffic across the connection will not reliably work. 
  * **Cisco ASA:** Do not use the originate-only option with an Oracle Site-to-Site VPN IPSec tunnel. It causes the tunnel's traffic to be inconsistently blackholed. The command is only for tunnels between two Cisco devices. Here's an example of the command that you should NOT use for the IPSec tunnels: `crypto map <map name> <sequence             number> set connection-type originate-only`


### IPSec tunnel is UP, but traffic is passing in only one direction 🔗 
Check these items:
  * **Asymmetric routing:** Oracle uses asymmetric routing across the multiple tunnels that make up the IPSec connection. Even if you configure one tunnel as primary and another as backup, traffic from your VCN to your on-premises network can use any tunnel that is "up" on your device. Configure your firewalls accordingly. Otherwise, ping tests or application traffic across the connection will not reliably work. 
  * **Single tunnel preferred:** If you want to use only one of the tunnels, ensure that you have the proper policy or routing in place on the CPE to prefer that tunnel.
  * **Multiple IPSec connections:** If you have multiple IPSec connections with Oracle, make sure to specify more specific static routes for the preferred IPSec connection. 
  * **VCN security lists:** Ensure that your [VCN security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) allow traffic in both directions (ingress and egress).
  * **Firewall rules:** Ensure that your firewall rules allow traffic in _both_ directions with the Oracle VPN headend IPs and the VCN CIDR block.


## Troubleshooting Site-to-Site VPN with a Policy-Based Configuration 🔗 
### IPSec tunnel is DOWN 🔗 
Check these items:
  * **Basic configuration:** The IPSec tunnel consists of both [phase-1 (ISAKMP) and phase-2 (IPSec) configuration](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/supportedIPsecparams.htm#Supported_IPSec_Parameters). Confirm that both are configured correctly on your CPE device. See the configuration appropriate for your CPE device:
List of configurations 
    * [Verified CPE Devices](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/CPElist.htm#Verified_CPE_Devices)
    * [Using the CPE Configuration Helper](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/CPEconfigurationhelper.htm#Using_the_CPE_Configuration_Helper)
    * Checkpoint:
      * [Check Point: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEroutebased.htm#Check_Point_RouteBased)
      * [Check Point: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/checkpointCPEpolicybased.htm#Check_Point_PolicyBased)
    * Cisco ASA:
      * [Cisco ASA: Route-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEroutebased.htm#Cisco_ASA_RouteBased)
      * [Cisco ASA: Policy-Based](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#Cisco_ASA_PolicyBased)
    * [Cisco IOS](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoiosCPE.htm#Cisco_IOS)
    * [FortiGate](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/fortigateCPE.htm#FortiGate)
    * [Furukawa Electric](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/furukawaCPE.htm#Furukawa_Electric "Learn how to configure a Furukawa Electric router for Site-to-Site VPN between your on-premises network and cloud network.")
    * [Juniper MX](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/junipermxCPE.htm#Juniper_MX)
    * [Juniper SRX](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/junipersrxCPE.htm#Juniper_SRX)
    * [Libreswan](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/libreswanCPE.htm#Libreswan)
    * [NEC IX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/necixCPE.htm#NEC_IX_Series)
    * [Openswan](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/openswanCPE.htm#Openswan)
    * [Palo Alto](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/paloaltoCPE.htm#Palo_Alto)
    * [WatchGuard](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/watchguardCPE.htm#WatchGuard)
    * [Yamaha RTX Series](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/yamahartx.htm#Yamaha_RTX_Series)
  * **Local and remote proxy IDs:** If you're using a policy-based configuration, check if the CPE is configured with more than one pair of local and remote proxy IDs (subnets). The Oracle VPN router supports only one pair on older connections. If the CPE has more than one pair, update the configuration to include only one pair, and choose one of the following two options: 
Option  | Local Proxy ID | Remote Proxy ID  
---|---|---  
1 | ANY (or 0.0.0.0/0) | ANY (or 0.0.0.0/0)  
2 | On-premises CIDR (an aggregate that covers all the subnets of interest) | VCN's CIDR  
  * **NAT device:** If the CPE is behind a NAT device, the CPE IKE identifier configured on your CPE might not match the CPE IKE identifier Oracle is using (the public IP address of your CPE). If your CPE does not support setting the CPE IKE identifier on your end, you can provide Oracle with your CPE IKE identifier in the Oracle Console. For more information, see [Overview of Site-to-Site VPN Components](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#components). 
  * **Cisco ASA:** Do not use the originate-only option with an Oracle Site-to-Site VPN IPSec tunnel. It causes the tunnel's traffic to be inconsistently blackholed. The command is only for tunnels between two Cisco devices. Here's an example of the command that you should NOT use for the IPSec tunnels: `crypto map <map name> <sequence             number> set connection-type originate-only`


### IPSec tunnel is UP but keeps flapping 🔗 
Check these items:
  * **Initiation of connection:** Ensure that your CPE device is initiating the connection.
  * **Local and remote proxy IDs:** If you're using a policy-based configuration, check if the CPE is configured with more than one pair of local and remote proxy IDs (subnets). The Oracle VPN router supports only one pair on older connections. If the CPE has more than one pair, update the configuration to include only one pair, and choose one of the following two options: 
Option  | Local Proxy ID | Remote Proxy ID  
---|---|---  
1 | ANY (or 0.0.0.0/0) | ANY (or 0.0.0.0/0)  
2 | On-premises CIDR (an aggregate that covers all the subnets of interest) | VCN's CIDR  
  * **Interesting traffic at all times:** In general, Oracle recommends having interesting traffic running through the IPSec tunnels at all times if your CPE supports it. Cisco ASA requires that you configure SLA monitoring, which keeps interesting traffic running through the IPSec tunnels. For more information, see the section for "IP SLA Configuration" in the [Cisco ASA policy-based configuration template](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#CPE). 


### IPSec tunnel is UP but traffic is unsteady 🔗 
Check these items:
  * **Local and remote proxy IDs:** If you're using a policy-based configuration, check if the CPE is configured with more than one pair of local and remote proxy IDs (subnets). The Oracle VPN router supports only one pair on older connections. If the CPE has more than one pair, update the configuration to include only one pair, and choose one of the following two options: 
Option  | Local Proxy ID | Remote Proxy ID  
---|---|---  
1 | ANY (or 0.0.0.0/0) | ANY (or 0.0.0.0/0)  
2 | On-premises CIDR (an aggregate that covers all the subnets of interest) | VCN's CIDR  
  * **Interesting traffic at all times:** In general, Oracle recommends having interesting traffic running through the IPSec tunnels at all times if your CPE supports it. Cisco ASA requires that you configure SLA monitoring, which keeps interesting traffic running through the IPSec tunnels. For more information, see the section for "IP SLA Configuration" in the [Cisco ASA policy-based configuration template](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#CPE). 


### IPSec tunnel is only partially UP
[![Diagram showing multiple encryption domains and how to determine their number.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_cross-products.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_cross-products.svg)
If you had a configuration similar to the example above and only configured three of the six possible IPv4 encryption domains on the CPE side, the link would be listed in a "Partial UP" state since all possible encryption domains are always created on the DRG side.
**Partial up SA:** In general, Oracle recommends having interesting traffic running through the IPSec tunnels at all times. Certain CPE vendors require you to always have interesting traffic through the tunnel to keep phase 2 up. Vendors like Cisco ASA require the [SLA monitor](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/ciscoasaCPEpolicybased.htm#Cisco_ASA_PolicyBased) monitor to be configured. Similarly, Palo Alto features like path monitoring can be used. Such features keep interesting traffic running through the IPSec tunnels. Numerous scenarios have been seen with vendors like Cisco ASA acting as the "initiator" does not bring phase 2 up until there is no interesting traffic. This causes the SA to be down either when the tunnel is brought up or after security association rekey.
## BGP Session Troubleshooting for Site-to-Site VPN 🔗 
### BGP status is DOWN 🔗 
Check these items:
  * **IPSec status:** For the BGP session to be up, the IPSec tunnel itself must be up. 
  * **BGP address:** Verify that both ends of the tunnel are configured with the correct BGP peering IP address.
  * **ASN:** Verify that both ends of the tunnel are configured with the correct BGP local ASN and Oracle BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the Government Cloud, see [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn).
  * **MD5:** Verify that MD5 authentication is disabled or not configured on your CPE device. Site-to-Site VPN does not support MD5 authentication.
  * **Firewalls:** Verify that your on-premises firewall or access control lists are not blocking the following ports:
    * TCP port 179 (BGP)
    * UDP port 500 (IKE)
    * IP protocol port 50 (ESP)
If your CPE device's firewall is blocking TCP port 179 (BGP), the BGP neighborship state will always be down. Traffic cannot flow through the tunnel because the CPE device and Oracle router do not have any routes.


### BGP status is flapping 🔗 
Check these items:
  * **IPSec status:** For the BGP session to be up and not flapping, the IPSec tunnel itself must be up and not flapping. 
  * **Maximum prefixes:** Verify that you are advertising no more than 2000 prefixes. If you're advertising more, BGP won't be established.


### BGP status is UP, but no traffic is passing through 🔗 
Check these items:
  * **VCN security lists:** Ensure you've set up the [VCN security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) to allow the desired traffic (both ingress and egress rules). Note that the VCN's [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) does not allow ping traffic (ICMP type 8 and ICMP type 0). You must add the appropriate ingress and egress rules to allow ping traffic. 
  * **Correct routes on both ends:** Verify that you have received the correct VCN routes from Oracle and the CPE device is using those routes. Likewise, verify that you are advertising the correct on-premises network routes over the Site-to-Site VPN, and the VCN route tables use those routes.


### BGP status is UP, but traffic is passing in only one direction 🔗 
Check these items:
  * **VCN security lists:** Ensure that your [VCN security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) allow traffic in both directions (ingress and egress).
  * **Firewalls:** Verify that your on-premises firewall or access control lists are not blocking traffic to or from the Oracle end.
  * **Asymmetric routing:** Oracle uses asymmetric routing. If you have multiple IPSec connections, ensure that your CPE device is configured for asymmetric route processing. 
  * **Redundant connections:** If you have redundant IPSec connections, ensure that they're both advertising the same routes.


##  Troubleshooting Redundant IPSec connections  🔗 
Remember these important notes:
  * FastConnect uses BGP dynamic routing. Site-to-Site VPN IPSec connections can use either static routing or BGP, or a combination. 
  * For important details about routing and preferred routes when using redundant connections, see [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
  * You can use two IPSec connections for redundancy. If both IPSec connections have only a default route (0.0.0.0/0) configured, traffic will route to either of those connections because Oracle uses asymmetric routing. If you want one IPSec connection as primary and another one as backup, configure more-specific routes for the primary connection and less-specific routes (or the default route of 0.0.0.0/0) on the backup connection.


### IPSec and FastConnect are both set up, but traffic is only passing through IPSec 🔗 
Ensure that you use more specific routes for the connection you want as primary. If you're using the same routes for both IPSec and FastConnect, see the discussion of routing preferences in [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
### Two on-premises data centers each have an IPSec connection to Oracle, but only one is passing traffic 🔗 
Verify that both IPSec connections are up and ensure that you have asymmetric route processing enabled on the CPE.
If both IPSec connections have only a default route (0.0.0.0/0) configured, traffic will route to either of those connections because Oracle uses asymmetric routing. If you want one IPSec connection as primary and another one as backup, configure more-specific routes for the primary connection and less-specific routes (or the default route of 0.0.0.0/0) on the backup connection. 
For more information about this type of setup, see [Example Layout with Multiple Geographic Areas](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/settingupIPsec.htm#example_multi_geo).
Was this article helpful?
YesNo

