Updated 2025-03-10
# FastConnect Redundancy Best Practices
This topic covers best practices for redundancy when implementing FastConnect. 
For general information about FastConnect, see [FastConnect Overview](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#FastConnect_Overview). 
## Overview 🔗 
Design your network to achieve high availability (HA) in preparation for these types of disruptions:
  * Regularly scheduled maintenance on an on-premises network, your provider's network (if you're using one), or Oracle.
  * Unexpected failures on the part of your networking components, your provider, or Oracle. Failures are rare, but you still need to plan for them.


Connections to OCI provide redundancy in the following ways:
  * There are multiple providers and Oracle Partners for each OCI region (see the list of [FastConnect Partners](https://www.oracle.com/cloud/networking/fastconnect/partners/)) which makes provider redundancy possible
  * There are two or more **FastConnect locations** (sometimes called a point of presence or PoP) in regions with multiple entries in the list of FastConnect locations (see the bottom of the list of [FastConnect Partners](https://www.oracle.com/cloud/networking/fastconnect/partners/). Many regions have a single FastConnect location, so region redundancy is sometimes but not always available. 
  * There are always at least two routers in each FastConnect location to enable device redundancy. 
  * There are multiple physical connections between each Oracle partner and each Oracle region.


The redundancy best practices depend on which [connectivity model](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#How) you use.
## If You Use an Oracle Partner 🔗 
Connectivity model:
  * [FastConnect: With an Oracle Partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#FastConnect_With_an_Oracle_Partner "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to an Oracle Partner.")


Oracle handles redundancy of the physical connections between the partner and Oracle, and the redundancy of routers in the FastConnect locations. You should handle redundancy of the physical connection between your existing network and the Oracle partner. 
The remaining best practices depend on the partner you're using, and details of the BGP session from your edge:
  * For some partners, the BGP session from your network's edge goes to Oracle. When you select the partner, this connection can sometimes be labeled as L2. For redundancy best practices, see the next section.
  * For other partners, the BGP session from your network's edge goes to the Oracle partner. When you select the partner, this connection can sometimes be labeled as L3. For redundancy best practices, see [BGP Session to Oracle Partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectresiliency.htm#provider__bgp-provider).


For information about the two scenarios, see [Basic Network Diagrams](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectoverview.htm#diagrams).
### BGP Session to Oracle Partner
Each Oracle partner has at least two separate physical connections to Oracle. When you create a FastConnect virtual circuit in the Console, use the **Redundant virtual circuits** option. Set up one virtual circuit on one physical connection (as primary), and the other virtual circuit on another physical connection (as secondary). The following diagram illustrates these two virtual circuits, each going to a different router in a single FastConnect location. If the region has a second location, the partner's second physical connection might go to that location instead.
[![This image shows a setup with an Oracle provider and multiple virtual circuits to different routers in a single FastConnect location.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay2_resiliency.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay2_resiliency.svg)
If you're working in a region that has only a single FastConnect location, you might also want location diversity. To achieve that, repeat the preceding setup of two virtual circuits with the same Oracle partner, but in a second FastConnect location in a nearby region. Notice that you must have a duplicate setup of your Oracle cloud resources in that second region, as shown in the following diagram.
[![This image shows a setup with an Oracle provider and connections to two different Oracle regions.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay3_resiliency_region.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay3_resiliency_region.svg)
### BGP Session to Oracle Partner 🔗 
In this scenario, the BGP session _from your edge_ goes to the Oracle partner (as shown in the following diagram). Separate from your BGP session, the Oracle partner has _its own_ BGP sessions with Oracle (between the partner's edge and Oracle's edge). The virtual circuit is a logical connection that goes from your edge to the Oracle edge.
An Oracle Partner has two separate physical connections to Oracle. You create one virtual circuit with the partner. In this scenario, the virtual circuit is automatically designed to be redundant and diverse. The virtual circuit has two separate BGP sessions between the partner and Oracle, each on a different physical connection. The following diagram shows the two separate BGP sessions for the single virtual circuit as dotted lines.
By default a single L3 virtual circuit is redundant between OCI and the FC partner by design. This does not guarantee redundancy between the Oracle Partner and an on-premises network. In the case of using an L3 Oracle Partner virtual circuit, work with your Oracle Partner to understand if you require multiple virtual circuits to ensure full end-to-end redundancy all the way between OCI and the on-premises network (not just the single L3 virtual circuit guarantee of redundancy between the Oracle Partner and OCI).
In addition, you could decide to create redundant virtual circuits to an L3 Oracle Partner virtual circuit when you require: location diversity or partner diversity.
[![This image shows a setup with an Oracle provider and multiple BGP sessions between the provider and Oracle for the single virtual circuit.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay3_resiliency.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay3_resiliency.svg)
It is your responsibility to ensure that the connection between your edge and the Oracle Partner is redundant and diverse.
If you're working in a region that has only a single FastConnect location, you might also want location diversity. One way to achieve that is to repeat the preceding setup of a virtual circuit with the same Oracle partner, but in a second FastConnect location in a nearby region. Notice that you must also have a duplicate setup of your Oracle cloud resources in that second region, as shown in the following diagram.
[![This image shows a setup with an Oracle provider and connections to two different Oracle regions.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay3_resiliency_region.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay3_resiliency_region.svg)
### Partner Diversity
If you also want partner diversity, use the **Redundant virtual circuits** option and select a different partner when you create **Virtual circuit 1** and **Virtual circuit 2**. This example shows Partner A and Partner B using different FastConnect locations to connect to the same VCN. No duplicate setup of your Oracle cloud resources is necessary.
[![This image shows a setup with two Oracle partners and connections to a single Oracle region.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay3_resiliency_partner.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay3_resiliency_partner.svg)
This next example shows Partner A and Partner B using the same FastConnect location to connect to the same VCN.
[![This image shows a setup with two Oracle partners and connections to a single Oracle region.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay3_partner_single.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_prov_lay3_partner_single.svg)
## If You Use a Third-Party Provider or Colocate with Oracle 🔗 
Connectivity models:
  * [FastConnect: With a Third-Party Provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#FastConnect_With_a_ThirdParty_Provider "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to a third-party network provider of their choice, and not an Oracle Partner.")
  * [FastConnect: Colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#FastConnect_Colocation_with_Oracle "This topic is for customers who are colocated with Oracle in a FastConnect location.")


Oracle handles redundancy of the Oracle routers in the FastConnect locations. You are responsible for redundancy of the physical connection between an on-premises network and Oracle. 
To achieve redundancy, create two physical connections to Oracle, one for each FastConnect location that serves the region, or for different physical devices in the same FastConnect location. This means that in the Oracle Console, you set up two separate FastConnect connections. You then create two virtual circuits. Set up the first one on the first physical connection (the first FastConnect connection), and the second one on the second physical connection. The following diagram shows the general setup.
[![This image shows a colocation setup where you have two physical connections and virtual circuits to the FastConnect location.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_resiliency.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_resiliency.svg)
You might decide to connect to a single FastConnect location because of cost concerns, or the region might only have a single FastConnect location. In that case, you can always create two physical connections and ensure each goes to a different Oracle router in that FastConnect location. 
If you're using the **FastConnect Direct** and **Single FastConnect** option in the Console to augment the redundancy of any existing connections, you need to manually configure the **Specify router proximity** setting to achieve device redundancy. The following image shows a request for a second physical connection (which is a **cross-connect group**) created on a different router than the first connection in that FastConnect location (called MyConnection-1). 
[![This image shows the router proximity information in the Console.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_router_proximity.png)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_router_proximity.png)
For the initial creation of redundant cross connects or cross-connect groups, select **FastConnect Direct** and **Device redundancy** and configure two redundant cross connects or cross connect groups where the second is pre-configured to be set up on a different physical device (router) than the first. 
If you're working in a region that has only a single FastConnect location, you might also achieve location diversity by repeating the setup in a second FastConnect location in a nearby region. Notice that you must also have a duplicate setup of your Oracle cloud resources in that second region, as shown in the following diagram. 
[![This image shows a colocation setup to two different regions.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_resiliency_region.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_resiliency_region.svg)
If you're working in a region with two or more FastConnect locations you can use the **FastConnect Direct** and **Location redundancy** option to create two redundant cross connects or cross connect groups, one per FastConnect location. You can also do this manually by creating single FastConnects and selecting different physical locations on each. You do not need a duplicate setup of your Oracle cloud resources in that second region, as shown in the following diagram. 
[![This image shows a colocation setup to two different regions.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_resiliency_location.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_colo_resiliency_location.svg)
Regardless of how you achieve redundancy, you must scale the bandwidth of both physical connections evenly, and by using a cross-connect group (also called a link aggregation group or LAG) for each connection. Imagine that you have two individual 10 Gbps cross-connects in a single FastConnect location (each to a different Oracle router for redundancy and diversity). If you need to always have 20-Gpbs bandwidth, you must ensure that each of the physical connections consists of a cross-connect group to contain the cross-connect. Then you need to add another 10 Gbps cross-connect to each cross-connect group, so that _each_ redundant physical connection has two 10 Gbps cross-connects.
## Site-to-Site VPN as Backup for FastConnect 🔗 
Oracle recommends using [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") as a backup for your FastConnect connection. If you do, ensure that the Site-to-Site VPN IPSec tunnels are configured to use [BGP routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/overviewIPsec.htm#ipsec_routing) with a route-based VPN. Within your existing on-premises network, manipulate the routing to prefer routes learned through FastConnect over routes learned through Site-to-Site VPN. For example, use AS_Path Prepend to influence egress traffic from Oracle, and use local preference to influence egress traffic from your network.
If you are using VPN backup, review Oracle's BGP routing behavior in the table shown in [Using AS_PATH to Prefer Routes from Oracle to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#oracle-to-on-prem).
The following diagram shows a setup with redundant FastConnect virtual circuits and redundant Site-to-Site VPN tunnels. 
[![This image shows FastConnect with Site-to-Site VPN as backup.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_resiliency_vpn_backup.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_fc_resiliency_vpn_backup.svg)
## Related Resources 🔗 
  * [Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#Routing_Details_for_Connections_to_Your_OnPremises_Network)
  * [Connectivity redundancy guide (PDF)](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/connectivity-redundancy-guide.pdf)


## What's Next? 🔗 
Choose the topic that suits your situation:
  * [FastConnect: With an Oracle Partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#FastConnect_With_an_Oracle_Partner "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to an Oracle Partner.")
  * [FastConnect: With a Third-Party Provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#FastConnect_With_a_ThirdParty_Provider "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to a third-party network provider of their choice, and not an Oracle Partner.")
  * [FastConnect: Colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#FastConnect_Colocation_with_Oracle "This topic is for customers who are colocated with Oracle in a FastConnect location.")


Was this article helpful?
YesNo

