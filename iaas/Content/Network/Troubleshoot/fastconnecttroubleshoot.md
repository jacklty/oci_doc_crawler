Updated 2024-08-21
# FastConnect Troubleshooting
This topic covers troubleshooting techniques for a FastConnect connection that has issues.
Some of the troubleshooting techniques assume that you are a network engineer with access to your CPE's configuration.
## Microsoft Azure Connection Issues 🔗 
### Problems terminating the Azure connection 🔗 
The connection components must be [terminated in a specific order](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/azure.htm#terminate_connection). If you don't follow this order, the FastConnect virtual circuit switches to a "Failed" state and cannot be deleted.
To fix a virtual circuit in the "Failed" state, go to the Azure portal and confirm the following items:
  * The ExpressRoute circuit is not in the "Failed" state. If it is, click the ExpressRoute circuit's **Refresh** button. The circuit should return to its normal state.
  * The ExpressRoute circuit has no connections. [Delete all its connections](https://docs.microsoft.com/azure/expressroute/expressroute-howto-linkvnet-portal-resource-manager#delete-a-connection-to-unlink-a-vnet) and then retry terminating the connection.


After you've confirmed the preceding items, you can continue with the termination process in the following steps:
  1. In the Oracle Console, delete your FastConnect virtual circuit. Ensure that it is deleted before proceeding.
  2. In the Azure portal, confirm that the private peering for the ExpressRoute circuit has been deleted. Also confirm that the ExpressRoute circuit's status has changed to "Not Provisioned".
  3. In the Azure portal, [delete the ExpressRoute circuit](https://docs.microsoft.com/azure/expressroute/expressroute-howto-circuit-portal-resource-manager#delete).


## General Issues 🔗 
### FastConnect is DOWN 🔗 
**Important** If you're working with an [Oracle partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#FastConnect_With_an_Oracle_Partner "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to an Oracle Partner.") or a [third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#FastConnect_With_a_ThirdParty_Provider "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to a third-party network provider of their choice, and not an Oracle Partner."), contact both the provider and Oracle to help troubleshoot the issue. If you're [colocated with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#FastConnect_Colocation_with_Oracle "This topic is for customers who are colocated with Oracle in a FastConnect location."), contact Oracle.
#### Cross-connect and physical connection (layer 1) 🔗 
Check these items:
  * **Port allocation:** Verify that your connection is using the correct port, and the port is UP and activated. 
  * **Optical signal:** Verify that your connection is using the correct optics and transceiver, and the port is sending and receiving an optimal signal. For more information, see [FastConnect Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#FastConnect_Requirements "This topic covers the requirements for implementing FastConnect.").
  * **Fiber strands:** Try rolling or flipping the Tx/Rx fiber strands.
  * **End-to-end physical connectivity:** Verify the end-to-end physical connectivity. Also verify the Tx/Rx optic signal between your CPE, the provider's network device (if you're working with a provider), and the Oracle FastConnect router.


#### Data-link (layer 2) 🔗 
Check the following items on your CPE. If you're working with a provider, also have them check the items on their network device:
  * **BGP address:** Verify that the router is configured with the correct BGP peering IP address under the correct VLAN on the interface. 
  * **MAC address:** Verify that the router is receiving the MAC address from the Oracle FastConnect router, and that the MAC address has an entry in the router's address resolution protocol (ARP) table.
  * **LAG and LACP:** Verify that the router has LAG configured and LACP is enabled on the interface (the Oracle FastConnect router requires both). For more information, see [FastConnect Requirements](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectrequirements.htm#FastConnect_Requirements "This topic covers the requirements for implementing FastConnect.").


#### Network and transport (layers 3 and 4) 🔗 
Check the following items on your CPE. If you're working with a provider, also have them check the items on their network device:
  * **BGP address:** Verify that the router is configured with the correct BGP peering IP address.
  * **ASN:** Verify that the router is configured with the correct BGP local ASN and Oracle BGP ASN. Oracle's BGP ASN for the commercial cloud is 31898, except the Serbia Central (Jovanovac) region which is 14544. For the Government Cloud, see [Oracle's BGP ASN](https://docs.oracle.com/iaas/Content/General/Concepts/govinfo.htm#bgp_asn).
  * **MD5:** If you're using MD5 authentication, verify that the authentication string (the password) is correct.
  * **Maximum prefixes:** Verify that you are advertising less than the maximum allowed number of prefixes for virtual circuits. If you're advertising more prefixes than allowed, BGP establishment fails. Here are the limits:
    * Public virtual circuits: maximum 200 prefixes
    * Private virtual circuits: maximum 2000 prefixes
  * **Firewalls:** Verify that your on-premises firewall or access control lists are not blocking TCP port 179 (BGP) or any high-numbered TCP ports.


### FastConnect virtual circuit is UP, but BGP session is DOWN 🔗 
The Oracle Console displays an alert if the virtual circuit is in the PROVISIONED state, but the BGP session is DOWN.
Typically, the alert indicates one of the following issues:
  * You have not yet configured your CPE with the required information for the FastConnect connection. After you configure the CPE, the alert should no longer appear.
  * You have configured your CPE with incorrect information. Verify that your CPE is configured with the correct information.


The CPE configuration information includes these items:
  * BGP address for each side of the connection
  * ASN for your network and for Oracle's network
  * MD5 authentication string (if you're using MD5 authentication)
  * Maximum number of allowed prefixes


For more details, see the preceding information shown for network and transport (layers 3 and 4) in [FastConnect is DOWN](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/fastconnecttroubleshoot.htm#down).
**Exception:** The preceding information is not relevant if you're using an Oracle partner, and the BGP session from your CPE goes to that partner and not Oracle. In that case, contact your provider to confirm that the BGP session they have with Oracle is configured correctly. 
### FastConnect virtual circuit is UP, but no traffic is passing through 🔗 
Check these items:
  * **VCN security lists:** Ensure you've set up the [VCN security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) to allow the desired traffic (both ingress and egress rules). Note that the VCN's [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) does not allow ping traffic (ICMP type 8 and ICMP type 0). You must add the appropriate ingress and egress rules to allow ping traffic.
  * **Correct routes on both ends:** Verify that you have received the correct VCN routes from FastConnect and the CPE is using those routes. Likewise, verify that you are advertising the correct on-premises network routes to FastConnect and the VCN route tables use those routes.


### FastConnect virtual circuit is UP, but traffic is passing in only one direction 🔗 
Check these items:
  * **VCN security lists:** Ensure that your [VCN security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) allow traffic in both directions (ingress and egress).
  * **Firewalls:** Verify that your on-premises firewall or access control lists are not blocking traffic to or from the Oracle end.
  * **Asymmetric routing:** Oracle uses asymmetric routing. If you have multiple virtual circuits, ensure that your CPE is configured for asymmetric route processing. 
  * **Redundant connections:** If you have redundant FastConnect virtual circuits, ensure that they're both advertising the same routes.


## Redundant Connections 🔗 
Remember that FastConnect uses BGP dynamic routing, and IPSec connections can use either static routing or BGP, or a combination. 
### IPSec and FastConnect are both set up, but traffic is only passing through IPSec 🔗 
Verify that the route tables use more specific routes for the connection you want as primary. If you're using the same routes for both IPSec and FastConnect, see the discussion of routing preferences in [Routing for Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing).
Was this article helpful?
YesNo

