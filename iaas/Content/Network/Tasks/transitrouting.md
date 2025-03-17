Updated 2025-02-12
# Transit Routing inside a hub VCN 
_Transit routing_ refers to a network topology in which an on-premises network uses an intermediary to reach Oracle resources or services or VCNs. The intermediary can be a VCN or a **Dynamic Routing Gateway (DRG)** the on-premises network is already attached to. You connect the on-premises network to a DRG with [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") or [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\)."), and then configure routing so that traffic _transits through the intermediary_ to its destination. 
The three primary transit routing scenarios are: 
  * **Access between several networks through a single DRG with a firewall between networks:** This scenario uses the DRG as the hub, with routing configured to send packets through a firewall in a VCN before they can be sent to another network. See [Routing traffic through a central network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#scenario_g). This scenario is only available to an implementation using an upgraded [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions).
  * **Access to several VCNs in the same region:** The scenario covered in this topic. This scenario uses a VCN as the hub, and creates communication between an on-premises network and several VCNs (connected by using [local peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region)) in the same region over a single FastConnect private virtual circuit or Site-to-Site VPN. We recommend you use the previous scenario instead. This scenario is available to an implementation using a legacy or upgraded [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions).
  * **Private access to Oracle services:** This scenario uses a VCN as the hub, and gives an on-premises network _private access_ to Oracle services, so that the on-premises hosts can use their private IP addresses and the traffic doesn't go over the internet. See [Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services). This scenario is available to an implementation using either a legacy or upgraded [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions).


## Highlights 🔗 
  * You can use a single FastConnect or Site-to-Site VPN connection between an on-premises network with _several_ VCNs in the same region, in a _hub-and-spoke_ topology.
  * The VCNs must be in the same region but can be in different tenancies. The CIDR blocks of the various subnets of interest in the on-premises network and VCNs must not overlap.
  * The VCN that acts as the _hub_ uses a [dynamic routing gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs) (DRG) to communicate with the on-premises network. This _hub_ VCN peers with each VCN acting as a spoke (referred to as _spoke_ VCNs in this topic). The hub and spoke VCNs use [local peering gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region) (LPGs) to communicate.
  * To enable the intended traffic from the on-premises network through the hub to a peered spoke VCN, you implement route rules for the hub DRG or the hub VCN's DRG attachment and LPG, and for the spoke VCN's subnets.
  * You can set up transit routing _through a private IP in the hub VCN_. For example, you might want to filter or inspect the traffic between the on-premises network and a spoke VCN. In that case, you route the traffic to a private IP on an instance in the hub VCN for inspection, and the resulting traffic continues to its destination. This topic covers both situations: transit routing directly between gateways on the hub VCN, and transit routing through a private IP.
  * Configuring route tables that reside in the hub VCN lets you control whether a particular subnet in a peered spoke VCN is advertised to the on-premises network, and whether a particular subnet in the on-premises network is advertised to a peered spoke VCN. 


**Tip** Another scenario lets you connect an on-premises network to several VCNs. Instead of using a single DRG and hub-and-spoke topology, you set up a separate DRG for each VCN and a separate private virtual circuit over a single FastConnect. However, the scenario can be used only with FastConnect through a [third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#FastConnect_With_a_ThirdParty_Provider "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to a third-party network provider of their choice, and not an Oracle Partner.") or through [colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#FastConnect_Colocation_with_Oracle "This topic is for customers who are colocated with Oracle in a FastConnect location."). The VCNs must be in the same region and same tenancy. For more information, see [FastConnect with Multiple DRGs and VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectmultipledrgs.htm#FastConnect_with_Multiple_DRGs_and_VCNs).
## Overview of Transit Routing 🔗 
_Transit routing_ is the task of routing traffic to either a Virtual Cloud Network (VCN) or an on-premises network through a central hub VCN. Here's a basic example of why you might use transit routing: you have a large organization with different departments, each with their own VCN. An on-premises network needs access to the different VCNs, but you don't want the administration overhead of maintaining a secure connection from each VCN to the on-premises network. Instead you want to use a single FastConnect or Site-to-Site VPN. 
A basic networking scenario involves connecting the on-premises network to a VCN with either Oracle Cloud Infrastructure [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") or an [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\)."). These two basic scenarios illustrate that topology: [Scenario B: Private Subnet with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#Scenario_B_Private_Subnet_with_a_VPN) and [Scenario C: Public and Private Subnets with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm#Scenario_C_Public_and_Private_Subnets_with_a_VPN).
This scenario uses a _hub-and-spoke_ topology, as illustrated in the following diagram. The term _hub_ here means only that a VCN is acting as the hub in this hub-and-spoke design. 
[![This image shows the basic hub and spoke layout of VCNs connected to the on-premises network.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_basic_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_basic_layout.svg)
One of the VCNs acts as the hub (VCN-H) and connects to the on-premises network by way of [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") or an [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\)."). The other VCNs are [locally peered with the hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Access_to_Other_VCNs_Peering). The traffic between the on-premises network and the peered VCNs transits through the hub VCN. The VCNs must be in the same region but can be in different tenancies.
### Gateways Involved in Transit Routing
The next diagram shows the gateways on the VCNs. The hub VCN has a [Dynamic Routing Gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs), which is the communication path with the on-premises network. Each locally peered spoke VCN uses a pair of [local peering gateways (LPGs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region) that anchor the peering connection: one LPG is on the hub VCN and the other is on the spoke VCN.
[![This image shows the basic hub and spoke layout of VCNs along with the gateways required.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_basic_layout_with_gateways.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_basic_layout_with_gateways.svg)
### Summary of New Concepts for Experienced Networking Service Users
If you're already familiar with the Networking service and local VCN peering, these are the most important new concepts to understand:
  * For each spoke VCN subnet that needs to communicate with the on-premises network, update the subnet's route table with a rule that sets the target (the next hop) as the spoke VCN's LPG for all traffic destined for the on-premises network.
  * Add a route table to the hub VCN, associate it with _the DRG attachment_ , and add a route rule with a target that sets the target (the next hop) to the **hub VCN's LPG (for that spoke)** for all traffic destined for that spoke VCN (or a specific subnet in that VCN). 
  * Add another route table to the hub VCN, associate it with _the hub VCN's LPG_ (for that spoke), and add a route rule that sets the target (the next hop) as the **DRG** for all traffic destined for the on-premises network (or a specific subnet in that network). :


For transit routing directly through gateways, see these specific tasks for more information:
  * [For routing directly between gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#For_routing_directly_between_gateways)
  * [Task 6: Set up ingress routing for the DRG and LPG on the hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#drg_lpg_routing)


For transit routing through a private IP: see these specific tasks for more information:
  * [Task 5: Add a route rule to the spoke VCN's subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#spoke_routing)
  * [Task 6: Set up the private IPs on an instance in the hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#set_up_private_ip)
  * [Task 7: Set up ingress routing for the DRG and LPG on the hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#drg_lpg_routing_fw)


## Example: Components and Routing for a Hub and Single Spoke 🔗 
The examples in this section show a VCN acting as a hub and only a single spoke VCN for simplicity. 
**Note** In a hub-and-spoke model, the hub VCN can have several spokes and therefore several LPGs (one per spoke). This topic uses the phrase _the hub VCN's LPG_ , which could therefore be ambiguous. When the phrase is used here, it means the hub LPG for the _particular spoke of interest._ In the following diagrams, the hub is LPG-H-1. More spokes would involve creation of an LPG-H-2, LPG-H-3, and so on.
[For transit routing directly through gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
The following diagram shows the required Networking service route tables and route rules for transit routing directly through gateways. Although the hub VCN doesn't require a subnet to make transit routing work, the example presented here includes a subnet called Subnet-H. 
[![This image shows the route tables and rules required when setting up the scenario.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout.svg)
Callout 1: Route table associated with Subnet-H Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | LPG-H-1  
Callout 2: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
172.16.0.0/12 | LPG-1  
Callout 3: VCN route table associated with DRG attachment Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | LPG-H-1  
Callout 4: Route table associated with LPG-H-1 Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
The scenario in the diagram uses four route tables, each associated with a different resource:
  * **Subnet-H:**
    * This route table belongs to the hub VCN and is associated with Subnet-H. 
    * This route table has a rule to route traffic destined for the on-premises network to the DRG. It has another rule to route traffic destined for the spoke VCN to LPG-H-1.
  * **Subnet-1:**
    * This route table belongs to the spoke VCN and is associated with Subnet-1. 
    * This route table has rules to route traffic destined for the hub VCN or the on-premises network to LPG-1.
  * **VCN route table on DRG attachment:**
    * The route table belongs to the hub VCN and is associated with the DRG _attachment_. Why the attachment and not the DRG itself? Because the DRG is a standalone resource that you can attach to any VCN in the same region and tenancy as the DRG. The attachment itself identifies which VCN. 
    * The route table routes the inbound traffic from the on-premises network and destined for the spoke VCN (VCN-1). You configure the rule to send that traffic to LPG-H-1. 
  * **VCN route table on LPG-H-1:**
    * This route table belongs to the hub VCN and is associated with LPG-H-1.
    * The route table routes inbound traffic from VCN-1 and destined for the on-premises network. You configure the rule to send that traffic to the DRG.


[For transit routing through a private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
The following diagram shows the required Networking service route tables and route rules for transit routing through a private IP on an instance in the hub VCN. You can decide to implement this scenario with either a single VNIC or several VNICs. The next diagram shows two VNICs: one in a subnet called Subnet-H-Frontend, and another in a subnet called Subnet-H-Backend. The frontend VNIC has private IP 10.0.4.3, and the backend VNIC has private IP 10.0.8.3.
[![This image shows the route tables and rules required when setting up the scenario with a network virtual appliance in the hub VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout_firewall.svg)
Callout 1: Route table associated with Subnet-H-Frontend Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | 10.0.4.3  
Callout 2: Route table associated with Subnet-H-Backend Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | LPG-H-1  
172.16.0.0/12 | 10.0.8.3  
Callout 3: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
172.16.0.0/12 | LPG-1  
Callout 4: Route table associated with DRG attachment Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | 10.0.4.3  
Callout 5: Route table associated with LPG-H-1 Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | 10.0.8.3  
No special route table is associated with LPG-1.
The diagram shows five route tables, each associated with a different resource:
  * **DRG attachment:**
    * The route table belongs to the hub VCN and is associated with the DRG _attachment_. Why the attachment and not the DRG itself? Because the DRG is a standalone resource that you can attach to any VCN in the same region and tenancy as the DRG. The attachment itself identifies which VCN. 
    * The route table routes the inbound traffic from the on-premises network and destined for the spoke VCN (VCN-1). You configure the rule to send the traffic to the private IP in the frontend subnet.
  * **LPG-H-1:**
    * This route table belongs to the hub VCN and is associated with LPG-H-1.
    * The route table routes inbound traffic from VCN-1 and destined for the on-premises network. You configure the rule to send that traffic to the private IP in the backend subnet.
  * **Subnet-H-Frontend:**
    * This route table belongs to the hub VCN and is associated with Subnet-H-Frontend. 
    * This route table has a rule to route traffic destined for the on-premises network to the DRG. 
    * Although Oracle doesn't recommend putting workloads in the hub VCN's subnets, the diagram also shows a route rule to route traffic destined for the spoke VCN to the private IP in the frontend subnet (10.0.4.3) for filtering by the instance. The second rule is shown here to give a better picture of routing for this example.
  * **Subnet-H-Backend:**
    * This route table belongs to the hub VCN and is associated with Subnet-H-Backend. 
    * This route table has a rule to route traffic destined for the spoke VCN (VCN-1) to LPG-H-1. 
    * Although Oracle doesn't recommend putting workloads in the hub VCN's subnets, the diagram also shows a route rule to route traffic destined for the on-premises network to the private IP in the backend subnet (10.0.8.3) for filtering by the instance. The second rule is shown here to give a better picture of routing for this example.
  * **Subnet-1:**
    * This route table belongs to the spoke VCN and is associated with Subnet-1. 
    * This route table has rules to route traffic destined for the hub VCN or the on-premises network to LPG-1.


### Important Transit Routing Restrictions to Understand 🔗 
This section includes some other important details about routing:
  * **Route table for the DRG attachment:**
    * A VCN route table associated with a DRG attachment can have only rules that target a service gateway, a private IP, or a local peering gateway. 
    * A DRG attachment always has a route table associated with it, but you can associate a _different_ route table, edit the table's rules, or delete some or all rules. 
  * **Route table for an LPG:**
    * A VCN route table that's associated with a DRG attachment can only have rules that target a service gateway, a private IP, or a local peering gateway.
    * An LPG can exist without a route table associated with it. However, after you associate a route table with an LPG, there must always be a route table associated with it. But, you can associate a different route table. You can also edit the table's rules, or delete some or all rules.
  * **Traffic _through_ the hub VCN:** The route tables discussed here are intended only for moving traffic _through_ the hub VCN between locations in the on-premises network and locations in the spoke VCN. If you're using a private IP in the hub, you configure those route tables so that the private IP is placed in that traffic path going _through_ the hub. 
  * **Inbound traffic to the hub VCN:** Even though the preceding statement is true (about traffic _through_ the hub), inbound traffic to subnets _within the hub VCN_ is always allowed. You don't need to set up explicit rules for this inbound traffic in the DRG attachment's route table or hub LPG's route table. When this kind of inbound traffic reaches the DRG or the hub LPG, the traffic is automatically routed to its destination in the hub VCN by the _VCN local routing_. Because of VCN local routing, for any route table belonging to a particular VCN, you can't create a rule that lists that VCN's CIDR (or a subsection) as the rule's destination.
  * **Hub VCN traffic when transit routing through a private IP:** The immediately preceding statement about VCN local routing means that you only use the hub VCN for _transit_ between the on-premises network and spoke VCNs. **Don't set up workloads in the hub VCN itself.** More explicitly, if you set up transit routing through a private IP in the hub VCN, you can't also route the _hub VCN's_ traffic through that private IP. For example, in the preceding diagram, if you were to change the route rule in the LPG-H-1 route table so that the destination CIDR is 0.0.0.0/0 instead of 172.16.0.0/12, only traffic coming from VCN-1 and destined for addresses _outside_ the hub VCN's CIDR block would be routed through the private IP. Because of VCN local routing, any traffic destined for addresses within the VCN is automatically routed directly to the destination IP address. The VCN local routing takes precedence over the LPG-H-1 route table (in general, over _any_ of the VCN's route tables). 
  * The following traffic flow isn't supported:
[![unsupported route path](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_unsupported.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_unsupported.svg)
    * Traffic goes through DRG-1 out an attachment to VCN-1.
    * Traffic matches a rule in the attachment's ingress route table to LPG-1, which is peered to LPG-2 in VCN-2.
    * Traffic matches a rule in LPG-2's ingress route table to DRG-2 (attached to VCN-2).
While it might seem that this _should_ work, it's not supported. The supported way to move traffic as shown between two DRGs in the same region is through a remote peering connection within the region.


### About CIDR Overlap 🔗 
In this example, the various networks don't have overlapping CIDR blocks (172.16.0.0/12 compared with 10.0.0.0/16 compared with 192.168.0.0/16). The Networking service doesn't allow local VCN peering between two VCNs with overlapping CIDRs. That means each spoke must not overlap with the hub. 
However, the Networking service doesn't validate whether the spoke VCNs overlap with each other, or if any of the VCNs overlap with the on-premises network. Ensure that CIDRs for all the subnets that need to communicate with each other don't overlap. Otherwise, traffic is dropped. 
A Networking service route table can't contain two rules with the exact same destination CIDR. However, if two rules in the same route table have overlapping destination CIDRs, the most specific rule in the table is used to route the traffic (the rule with the [longest prefix match](https://en.wikipedia.org/wiki/Longest_prefix_match)). 
### Route Advertisement to the On-Premises Network and Spoke VCNs 🔗 
From a security standpoint, you can control route advertisement so that only specific subnets in the on-premises network are advertised to the spoke VCNs. Similarly, you can control which subnets in the spoke VCNs are advertised to the on-premises network. 
The routes advertised to the on-premises network consist of:
  * The rules listed in the route table associated with the DRG attachment (192.168.0.0/16 in the preceding diagram)
  * The individual subnets in the hub VCN


The routes advertised to the spoke VCN consist of:
  * The individual subnets in the hub VCN
  * The rules listed in the route table associated with the hub VCN's LPG for the spoke (172.16.0.0/12 in the preceding diagram)


Therefore, the administrator _of the hub VCN_ alone can control which routes are advertised to the on-premises network and spoke VCNs.
In the preceding example, the relevant routes use the full CIDR block of the on-premises network (172.16.0.0/12) and spoke VCN (192.168.0.0/16) as the destination, but they could instead use a subnet of those networks to restrict routing to specific subnets.
### Details About Routing for Different Traffic Paths 🔗 
To further illustrate how routing takes place in the preceding example, let's look more closely at different paths of traffic. Here are the same diagrams again.
First, if you're transit routing directly through gateways on the hub VCN:
[![This image shows the route tables and rules required when setting up the scenario.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout.svg)
Callout 1: Route table associated with Subnet-H Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | LPG-H-1  
Callout 2: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
172.16.0.0/12 | LPG-1  
Callout 3: Route table associated with DRG attachment Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | LPG-H-1  
Callout 4: Route table associated with LPG-H-1 Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
No special route table is associated with LPG-1.
Second, if you're transit routing through a private IP in the hub VCN:
[![This image shows the route tables and rules required when setting up the scenario with a network virtual appliance in the hub VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout_firewall.svg)
Callout 1: Route table associated with Subnet-H-Frontend Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | 10.0.4.3  
Callout 2: Route table associated with Subnet-H-Backend Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | LPG-H-1  
172.16.0.0/12 | 10.0.8.3  
Callout 3: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
172.16.0.0/12 | LPG-1  
Callout 4: Route table associated with DRG attachment Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | 10.0.4.3  
Callout 5: Route table associated with LPG-H-1 Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | 10.0.8.3  
No special route table is associated with LPG-1.
[Traffic from the on-premises network to the spoke VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
  1. Traffic leaves the on-premises network and reaches the DRG. The traffic's destination is in Subnet-1 (for example, 192.168.0.5).
  2. The DRG attachment's associated route table has a rule for 192.168.0.0/16. It matches the destination and sends the traffic to the route target:
     * **Transit routing directly through gateways:** The rule's target is LPG-H-1. 
     * **Transit routing through a private IP:** The rule's target is the private IP 10.0.4.3. The instance receives and processes the traffic and sends any resulting traffic out of the backend subnet's VNIC. The backend subnet's route table sends that traffic to LPG-H-1.
Remember that you can use the rules in the DRG attachment's route table to control which subnets in the spoke VCN are advertised to the on-premises network. You could instead set up the rule to list only a subnet of the spoke VCN.
  3. LPG-H-1 receives the traffic. 
  4. Egress traffic leaving a VCN through an LPG is automatically routed to the LPG's peered LPG, which is LPG-1 in this situation. That routing occurs automatically because of the peering connection between the two LPGs. 
  5. LPG-1 receives the traffic. 
  6. Traffic coming in to a VCN through the LPG is automatically routed to the destination within the VCN because of VCN local routing. No explicit route rules are required.


[Traffic from the spoke VCN to the on-premises network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
  1. Traffic comes from an instance in Subnet-1 in the spoke VCN. The traffic's destination is in the on-premises network (for example, 172.16.0.3). 
  2. Subnet-1's associated route table has a rule for 172.16.0.0/12. It matches the destination and sends the traffic to the route target, LPG-1.
  3. LPG-1 receives the traffic. 
  4. Egress traffic leaving a VCN through an LPG is automatically routed to the LPG's peered LPG, which is LPG-H-1 in this situation. That routing occurs automatically because of the peering connection between the two LPGs. 
  5. LPG-H-1 receives the traffic. 
  6. LPG-H-1's associated route table has a rule for 172.16.0.0/12. It matches the destination and sends the traffic to the route target:
     * **Transit routing directly through gateways:** The rule's target is the DRG.
     * **Transit routing through a private IP:** The rule's target is the private IP 10.0.8.3. The instance receives and processes the traffic and sends any resulting traffic out of the frontend subnet's VNIC. The frontend subnet's route table sends that to the DRG.
Remember that you can use the rules in the LPG's route table to control which subnets in the on-premises network are advertised to the spoke VCN. You could instead set up the rule to list only a subnet of the on-premises network.
  7. The DRG receives the traffic.
  8. Egress traffic leaving the VCN through the DRG is routed based on Site-to-Site VPN and FastConnect configuration. No explicit rules in the DRG attachment's route table are required.


Notice that Subnet-1 in the spoke VCN and LPG-H-1 both have route rules with 172.16.0.0/12 as the destination CIDR. Those rules don't have to use the exact same CIDR block. However, ensure both rules cover the traffic you want to route from the spoke to the on-premises network. The rule in Subnet-1's route table controls which traffic is routed from Subnet-1 to LPG-H-1. The rule in LPG-H-1's route table controls which traffic is routed from the spoke VCN to the on-premises network. If LPG-H-1's route rule is more restrictive than Subnet-1's route rule, some traffic leaving the subnet could be dropped and not reach the DRG.
[Traffic from the spoke VCN to a subnet in the hub VCN (routing directly between gateways only)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
Depending on the situation, you might want to enable traffic between instances in the hub VCN and a spoke VCN, and not only traffic between the on-premises network and a spoke VCN. You can do this if you're routing directly between gateways. **You can't route the traffic from a spoke VCN _through the private IP_ and on to other instances in the hub VCN.** The note at the end of this section explains why.
Here's how traffic would flow from the spoke VCN to a destination with an address in the hub VCN:
  1. Traffic comes from an instance in Subnet-1 in the spoke VCN. The traffic's destination is in a subnet in the hub VCN (for example, 10.0.0.3). 
  2. Subnet-1's associated route table has a rule for 10.0.0.0/16. It matches the destination and sends the traffic to the route target, LPG-1.
  3. LPG-1 receives the traffic. 
  4. Egress traffic leaving a VCN through an LPG is automatically routed to the LPG's peered LPG, which is LPG-H-1 in this situation. That routing occurs automatically because of the peering connection between the two LPGs. 
  5. LPG-H-1 receives the traffic. 
  6. Traffic coming in to a VCN through an LPG and destined for an address in the VCN is automatically routed to the destination by VCN local routing. No explicit route rules are required.


A similar series of routing steps occurs for traffic going from Subnet-H to Subnet-1, but in the reverse direction. Subnet-H's route table has a rule that matches the spoke VCN's CIDR (192.168.0.0/16) and sends the traffic to LPG-H-1, which forwards it on to LPG-1.
**Note** If you set up transit routing through a private IP in the hub VCN, remember that the LPG-H-1 route table only controls routing of traffic destined for addresses _outside the hub VCN_. Traffic destined for addresses within the VCN is handled by the hub VCN local routing, which takes precedence and always routes the traffic directly to the packet's destination address. This means that you can't route traffic destined for addresses inside the hub VCN _through the private IP_ being used for the transit traffic through the hub. Even if the LPG-H-1 route rule uses a destination = 0.0.0.0/0 and target = 10.0.8.3, the hub VCN local routing takes precedence and routes the traffic directly to the destination in the hub VCN instead of the private IP.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're a member of the Administrators group, you already have the required access to set up transit routing. Otherwise, you need access to the Networking service, and you need the ability to create instances. See [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies).
## Setting Up VCN Transit Routing in the Console 🔗 
This section shows how to use the Console to set up transit routing with a VCN to give your on-premises network access to multiple VCNs in the same region.
[For routing directly between gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
**Tip** You might already have many of the necessary Networking components and connections in this advanced scenario already set up. So you might be able to skip some of the following tasks. **If you already have a network topology with a hub VCN connected to your on-premises network, and spoke VCNs locally peered with the hub VCN, then Task 5 and Task 6 are the most important.** They enable traffic to be routed between your on-premises network and the spoke VCN. 
[Task 1: Set up the hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 1: setting up the hub VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task1.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task1.svg)
In this task, you set up the hub VCN. A subnet in the hub VCN is optional. However, this example includes one. The subnet can contain cloud resources that your on-premises network or the spoke VCN need to use. 
For more information and instructions: 
  * [VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure.")


[Task 2: Connect the hub VCN with your on-premises network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 2: connecting the hub VCN to your on-premises network.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task2.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task2.svg)
Callout 1: Route table associated with Subnet-H Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
In this task, you set up either FastConnect or Site-to-Site VPN between your hub VCN and your on-premises network. As part of this process, you attach a DRG to the hub VCN and set up routing between the hub VCN and your on-premises network.Notice that you do not create the route table associated with the DRG attachment yet. That comes in a later step.For more information and instructions: 
  * [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.")
  * [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).")
  * [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs)


[Task 3: Set up a spoke VCN with at least one subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 3: setting up a spoke VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task3.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task3.svg)
In this task, you set up the spoke VCN with at least one subnet. For more information and instructions:
  * [VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure.")


[Task 4: Set up a local peering between the hub VCN and the spoke VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 4: setting up the local peering between the hub and spoke VCNs.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task4.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task4.svg)
Callout 1: Route table associated with Subnet-H Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | LPG-H-1  
Callout 2: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
In this task, you add an LPG to each VCN, establish a connection between the LPGs, and set up routing that enables resources in one VCN to communicate with resources in the other. 
**Important** When setting up local peering between two VCNs, be sure to [establish the connection between the LPGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#establish_cxn). It can be easy to overlook that part of the process.
Notice that you do not create the route table associated with the LPG on the hub VCN (LPG-H-1) yet. That comes in a later step.For more information and instructions: 
  * [Setting Up a Local Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Setting)


[Task 5: Add a route rule to the spoke VCN's subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 5: adding a route rule to the spoke VCN's subnet.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task5.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task5.svg)
Callout 1: Route table associated with Subnet-H Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | LPG-H-1  
Callout 2: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
172.16.0.0/12 | LPG-1  
In this task, you add a rule to the route table associated with the spoke VCN's subnet. This rule routes traffic that is destined for the on-premises network to the spoke VCN's LPG (LPG-1 in the diagram).Prerequisites: You already have an LPG for the spoke VCN, and a route table associated with the subnet (on the spoke VCN) that needs to communicate with the on-premises network. 
  1. For the spoke VCN, view the list of subnets.
  2. For the subnet of interest, look at its details and click the link for its associated route table.
  3. Edit the route table to include a rule that sends traffic to the on-premises network:
    1. Click **Add Route Rules**.
    2. Enter this information for the route rule:
       * **Target Type:** Local Peering Gateway.
       * **Destination CIDR Block** : The on-premises network's CIDR (172.16.0.0/12 in the earlier example).
       * **Compartment:** The compartment where the spoke VCN's LPG is located.
       * **Target Local Peering Gateway:** The spoke VCN's LPG.
       * **Description:** An optional description of the rule.
    3. Click **Add Route Rules**.


[Task 6: Set up ingress routing for the DRG and LPG on the hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 7: setting up ingress routing between the DRG and LPG on the hub VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout.svg)
Callout 1: Route table associated with Subnet-H Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | LPG-H-1  
Callout 2: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
172.16.0.0/12 | LPG-1  
Callout 3: Route table associated with DRG attachment Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | LPG-H-1  
Callout 4: Route table associated with LPG-H-1 Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
In this task, you set up the route tables for the DRG attachment and hub VCN's LPG for the spoke of interest (LPG-H-1).
Prerequisites: 
  * You already have a DRG attached to the hub VCN. 
  * You already have a hub VCN LPG for the spoke of interest. 


  1. Create a route table for the DRG attachment:
    1. In the Console, view the hub VCN's details.
    2. Under **Resources** , click **Route Tables** to view the VCN's route tables.
    3. Click **Create Route Table**. 
    4. Enter the following:
       * **Name:** A descriptive name for the route table. Example: DRG Route Table. Avoid entering confidential information.
       * **Create in Compartment:** Leave as is. 
    5. Click **+ Additional Route Rule** , and enter this information for the route rule:
       * **Target Type:** Local Peering Gateway.
       * **Destination CIDR Block** : This spoke VCN's CIDR (192.168.0.0/16 in the earlier example). Remember that you can use the routes in this table to control which subnets in the spoke VCN are advertised to the on-premises network. You could instead set up the rule to list only a particular subnet of the spoke VCN that the on-premises network.
       * **Compartment:** The compartment where the hub VCN's LPG is located.
       * **Target:** The hub VCN's LPG.
       * **Description:** An optional description of the rule.
    6. Click **Create Route Table**.
The route table is created and displayed in the list. 
  2. Associate the route table (called _DRG Route Table_ in this example) with the hub VCN's DRG attachment:
    1. While still viewing the hub VCN's details, click **Dynamic Routing Gateways** to view the attached DRG.
    2. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Associate Route Table**. 
    3. Select the route table.
    4. Click **Associate Route Table**.
The route table is associated with the DRG attachment. 
  3. Create a route table for the hub VCN's LPG for this spoke:
    1. While still viewing the hub VCN's details, click **Route Tables**.
    2. Click **Create Route Table**. 
    3. Enter the following:
       * **Create in Compartment:** Leave as is. 
       * **Name:** A descriptive name for the route table. Example: Hub LPG-# Route Table (where # indicates which spoke). Avoid entering confidential information.
    4. Click **+ Additional Route Rule** , and enter this information for the route rule:
       * **Target Type:** Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself.
       * **Destination CIDR Block** : The on-premises network's CIDR (172.16.0.0/12 in the earlier example). Remember that you can use the routes in this table to control which subnets in the on-premises network are advertised to this spoke VCN. You could instead set up the rule to list only a subnet of the on-premises network that needs to communicate with this spoke.
       * **Description:** An optional description of the rule.
    5. Click **Create Route Table**.
The route table is created and displayed in the list. 
  4. Associate the route table (called _Hub LPG-# Route Table_ in this example) with the hub VCN's LPG for the spoke of interest:
    1. While still viewing the hub VCN's details, click **Local Peering Gateways** to view the hub VCN's LPG for this spoke.
    2. For the LPG you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Associate With Route Table**. 
    3. Enter the following:
       * **Route Table Compartment:** Select the compartment of the route table for the LPG. 
       * **Route Table:** Select the route table for the LPG.
    4. Click **Associate**.
The route table is associated with the LPG. 


[Later if you need more spoke VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
  1. Repeat Tasks 3 through 5 for the new spoke VCN.
  2. Repeat Task 6 with these changes: 
     * For Step 1: Instead of creating a route table for the DRG attachment, update the existing route table to include a new rule for the new spoke VCN. The destination CIDR is the spoke VCN's CIDR (or a subnet within). The target is the hub VCN's LPG for the new spoke.
     * For Step 2: Skip this step entirely because the DRG attachment is already associated with its route table.
     * For Step 3: Repeat as is. Name the new route table according to which spoke the route table is for (for example, Hub LPG-2 Route Table for the second spoke).
     * For Step 4: Repeat as is. Associate the new route table you created in Step 3 with the hub VCN's LPG for the new spoke.


[For routing through a private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
**Tip** You might already have many of the necessary Networking components and connections in this advanced scenario already set up. So you might be able to skip some of the following tasks. **If you already have a network topology with a hub VCN connected to your on-premises network, and spoke VCNs locally peered with the hub VCN, then Tasks 5 through 7 are the most important.** They enable traffic to be routed between your on-premises network and the spoke VCN. 
[Task 1: Set up the hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 1: setting up the hub VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task1_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task1_firewall.svg)
In this task, you set up the hub VCN. The hub VCN must have two subnets: one for the frontend VNIC on the instance, and one for the backend VNIC on the instance. Oracle recommends using regional _private_ subnets, unless there are resources in the frontend subnet that need internet access. 
For more information and instructions: 
  * [VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure.")


[Task 2: Connect the hub VCN with your on-premises network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 2: connecting the hub VCN to your on-premises network.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task2_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task2_firewall.svg)
Callout 1: Route table associated with Subnet-H-Frontend Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | 10.0.4.3  
In this task, you set up either FastConnect or Site-to-Site VPN between your hub VCN and your on-premises network. As part of this process, you attach a DRG to the hub VCN and set up routing between the hub VCN and your on-premises network.Notice that you do not create the route table associated with the DRG attachment yet. That comes in a later step.For more information and instructions: 
  * [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.")
  * [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).")
  * [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs)


[Task 3: Set up a spoke VCN with at least one subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 3: setting up a spoke VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task3_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task3_firewall.svg)
Callout 1: Route table associated with Subnet-H-Frontend Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | 10.0.4.3  
In this task, you set up the spoke VCN with at least one subnet. For more information and instructions:
  * [VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure.")


[Task 4: Set up a local peering between the hub VCN and the spoke VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 4: setting up the local peering between the hub and spoke VCNs.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task4_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task4_firewall.svg)
Callout 1: Route table associated with Subnet-H-Frontend Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | 10.0.4.3  
Callout 2: Route table associated with Subnet-H-Backend Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | LPG-H-1  
172.16.0.0/12 | 10.0.8.3  
Callout 3: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
172.16.0.0/12 | LPG-1  
In this task, you add an LPG to each VCN, establish a connection between the LPGs, and set up routing that enables resources in one VCN to communicate with resources in the other. 
**Important** When setting up local peering between two VCNs, be sure to [establish the connection between the LPGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#establish_cxn). It can be easy to overlook that part of the process.
Notice that you do not create the route table associated with the LPG on the hub VCN (LPG-H-1) yet. That comes in a later step.For more information and instructions: 
  * [Setting Up a Local Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Setting)


[Task 5: Add a route rule to the spoke VCN's subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 5: adding a route rule to the spoke VCN's subnet.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task5_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task5_firewall.svg)
Callout 1: Route table associated with Subnet-H-Frontend Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | 10.0.4.3  
Callout 2: Route table associated with Subnet-H-Backend Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | LPG-H-1  
172.16.0.0/12 | 10.0.8.3  
Callout 3: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
172.16.0.0/12 | LPG-1  
In this task, you add a rule to the route table associated with the spoke VCN's subnet. This rule routes traffic that is destined for the on-premises network to the spoke VCN's LPG (LPG-1 in the diagram).Prerequisites: You already have an LPG for the spoke VCN, and a route table associated with the subnet (on the spoke VCN) that needs to communicate with the on-premises network. 
  1. For the spoke VCN, view the list of subnets.
  2. For the subnet of interest, look at its details and click the link for its associated route table.
  3. Edit the route table to include a rule that sends traffic to the on-premises network:
    1. Click **Add Route Rules**.
    2. Enter this information for the route rule:
       * **Target Type:** Local Peering Gateway.
       * **Destination CIDR Block** : The on-premises network's CIDR (172.16.0.0/12 in the earlier example).
       * **Compartment:** The compartment where the spoke VCN's LPG is located.
       * **Target Local Peering Gateway:** The spoke VCN's LPG.
       * **Description:** An optional description of the rule.
    3. Click **Add Route Rules**.


[Task 6: Set up the private IPs on an instance in the hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows task 6: setting up the instance in the hub VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task6_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_task6_firewall.svg)
Callout 1: Route table associated with Subnet-H-Frontend Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | 10.0.4.3  
Callout 2: Route table associated with Subnet-H-Backend Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | LPG-H-1  
172.16.0.0/12 | 10.0.8.3  
Callout 3: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
172.16.0.0/12 | LPG-1  
In this task, you set up the instance to have two private IPs.
Prerequisites: 
  * You already have a hub VCN with a subnet.
  * Review this information: [Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route).


  1. If you haven't already, create the instance in the hub VCN. See [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). The primary VNIC is created in the subnet you specify.
  2. Create a secondary VNIC for the other subnet and configure the OS to use it. See [Managing VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#console).
  3. Disable the source/destination check on each of the VNICs. See [Overview of VNICs and Physical NICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview).
  4. For each VNIC, determine which private IP you want to use as the routing target. If you want to use a secondary private IP instead of the VNIC's primary private IP, assign that secondary private IP and configure the OS to use it. See [Assigning a New Secondary Private IP to a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm#top "Assign a new secondary private IP address to a VNIC."). 
  5. For each of the private IPs you created, record the private IP address (for example: 10.0.4.3).
  6. Configure the instance as necessary for the job it performs (for example, configure the firewall or intrusion detection system on the instance). 


[Task 7: Set up ingress routing for the DRG and LPG on the hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
[![This image shows the route tables and rules required when setting up the scenario with a network virtual appliance in the hub VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_transit_detailed_layout_firewall.svg)
Callout 1: Route table associated with Subnet-H-Frontend Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | 10.0.4.3  
Callout 2: Route table associated with Subnet-H-Backend Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | LPG-H-1  
172.16.0.0/12 | 10.0.8.3  
Callout 3: Route table associated with Subnet-1 Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-1  
172.16.0.0/12 | LPG-1  
Callout 4: Route table associated with DRG attachment Destination CIDR | Route Target  
---|---  
192.168.0.0/16 | 10.0.4.3  
Callout 5: Route table associated with LPG-H-1 Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | 10.0.8.3  
No special route table is associated with LPG-1.
In this task, you set up the route tables for the DRG attachment and hub VCN's LPG for the spoke of interest (LPG-H-1).
Prerequisites: 
  * You already have a DRG attached to the hub VCN. 
  * You already have a hub VCN LPG for the spoke of interest. 
  * You already have the two private IPs to use as the routing targets (see the preceding task).


  1. Create a route table for the DRG attachment:
    1. In the Console, view the hub VCN's details.
    2. Under **Resources** , click **Route Tables** to view the VCN's route tables.
    3. Click **Create Route Table**. 
    4. Enter the following:
       * **Name:** A descriptive name for the route table. Example: DRG Route Table. Avoid entering confidential information.
       * **Create in Compartment:** Leave as is. 
    5. Click **+ Additional Route Rule** , and enter this information for the route rule:
       * **Target Type:** Private IP.
       * **Destination CIDR Block** : This spoke VCN's CIDR (192.168.0.0/16 in the earlier example). Remember that you can use the routes in this table to control which subnets in the spoke VCN are advertised to the on-premises network. You could instead set up the rule to list only a particular subnet of the spoke VCN that the on-premises network.
       * **Compartment:** The compartment where the frontend subnet's private IP is located.
       * **Target:** The frontend subnet's private IP, which you recorded in the previous task (10.0.4.3 in the example).
       * **Description:** An optional description of the rule.
    6. Click **Create Route Table**.
The route table is created and displayed in the list. 
  2. Associate the route table (called _DRG Route Table_ in this example) with the hub VCN's DRG attachment:
    1. While still viewing the hub VCN's details, click **Dynamic Routing Gateways** to view the attached DRG.
    2. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Associate With Route Table**. 
    3. Enter the following:
       * **Route Table Compartment:** Select the compartment of the route table for the DRG attachment. 
       * **Route Table:** Select the route table for the DRG attachment.
    4. Click **Associate**.
The route table is associated with the DRG attachment. 
  3. Create a route table for the hub VCN's LPG for this spoke:
    1. While still viewing the hub VCN's details, click **Route Tables**.
    2. Click **Create Route Table**. 
    3. Enter the following:
       * **Create in Compartment:** Leave as is. 
       * **Name:** A descriptive name for the route table. Example: Hub LPG-# Route Table (where # indicates which spoke). Avoid entering confidential information.
    4. Click **+ Additional Route Rule** , and enter this information for the route rule:
       * **Target Type:** Private IP.
       * **Destination CIDR Block** : The on-premises network's CIDR (172.16.0.0/12 in the earlier example). Remember that you can use the routes in this table to control which subnets in the on-premises network are advertised to this spoke VCN. You could instead set up the rule to list only a subnet of the on-premises network that needs to communicate with this spoke.
       * **Compartment:** The compartment where the private IP is located.
       * **Target:** The backend subnet's private IP, which you recorded in the previous task (10.0.8.3 in the example).
       * **Description:** An optional description of the rule.
    5. Click **Create Route Table**.
The route table is created and displayed in the list. 
  4. Associate the route table (called _Hub LPG-# Route Table_ in this example) with the hub VCN's LPG for the spoke of interest:
    1. While still viewing the hub VCN's details, click **Local Peering Gateways** to view the hub VCN's LPG for this spoke.
    2. For the LPG you're interested in, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Associate With Route Table**. 
    3. Enter the following:
       * **Route Table Compartment:** Select the compartment of the route table for the LPG. 
       * **Route Table:** Select the route table for the LPG.
    4. Click **Associate**.
The route table is associated with the LPG. 


Although Oracle does not recommend putting workloads in the hub VCN's subnets, to give you a better picture of routing in the example, the diagram shows two more route rules in the hub VCN's subnet route tables. For the frontend subnet, there's a route rule to route traffic that is destined for the spoke VCN to the private IP in the frontend subnet (10.0.4.3) for filtering by the instance. For the backend subnet, there's a route rule to route traffic that is destined for the on-premises network to the private IP in the backend subnet (10.0.8.3) for filtering by the instance. The following procedure adds those two route rules.
  1. For the spoke VCN, view the list of subnets.
  2. For the frontend subnet, look at its details and click the link for its associated route table.
  3. Edit the frontend subnet's route table to include a rule that sends traffic destined for the spoke VCN to the private IP in the frontend subnet:
    1. Click **Add Route Rules**.
    2. Enter this information for the route rule:
       * **Target Type:** Private IP.
       * **Destination CIDR Block** : This spoke VCN's CIDR (192.168.0.0/16 in the earlier example). 
       * **Compartment:** The compartment where the frontend subnet's private IP is located.
       * **Target:** The frontend subnet's private IP, which you recorded in the previous task (10.0.4.3 in the example).
       * **Description:** An optional description of the rule.
    3. Click **Add Route Rules**.
  4. For the backend subnet, look at its details and click the link for its associated route table.
  5. Edit the backend subnet's route table to include a rule that sends traffic destined for the on-premises network to the private IP in the backend subnet:
    1. Click **Add Route Rules**.
    2. Enter this information for the route rule:
       * **Target Type:** Private IP.
       * **Destination CIDR Block** : The on-premises network's CIDR (172.16.0.0/12 in the earlier example).
       * **Compartment:** The compartment where the backend subnet's private IP is located.
       * **Target:** The backend subnet's private IP, which you recorded in the previous task (10.0.8.3 in the example).
       * **Description:** An optional description of the rule.
    3. Click **Add Route Rules**.


[Later if you need more spoke VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm)
  1. Repeat Tasks 3 through 5 for the new spoke VCN.
  2. Repeat task 7 with these changes: 
     * For Step 1: Instead of creating a route table for the DRG attachment, update the existing route table to include a new rule for the new spoke VCN. The destination CIDR is the spoke VCN's CIDR (or a subnet within). The target is the frontend subnet private IP 10.0.4.3.
     * For Step 2: Skip this step entirely because the DRG attachment is already associated with its route table.
     * For Step 3: Repeat as is. Name the new route table according to which spoke the route table is for (for example, Hub LPG-2 Route Table for the second spoke).
     * For Step 4: Repeat as is. Associate the new route table you created in Step 3 with the hub VCN's LPG for the new spoke.


## Turning Off Transit Routing 🔗 
To turn off transit routing, remove the rules from:
  * The route table associated with the DRG attachment.
  * The route table associated with each LPG on the hub VCN.


A route table can be associated with a resource but have no rules. Without at least one rule, a route table does nothing. 
A DRG attachment or LPG can exist without a route table associated with it. However, after you associate a route table with a DRG attachment or LPG, there must always be a route table associated with it. But, you can associate a _different_ route table. You can also edit the table's rules, or delete some or all rules. 
## Changes to the API 🔗 
For information about changes to the Networking service API to support transit routing, see the [transit routing release notes](https://docs.oracle.com/iaas/releasenotes/changes/60de1e32-eada-4768-9332-860c1b3e880f/).
Was this article helpful?
YesNo

