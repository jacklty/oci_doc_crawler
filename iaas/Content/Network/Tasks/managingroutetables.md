Updated 2025-03-10
# VCN Route Tables
This topic describes how to manage the **route tables** in a Virtual Cloud Network (VCN). For more on route tables in a Dynamic Routing Gateway (DRG), see [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs).
## Overview of Routing for a VCN 🔗 
A VCN uses route tables to send traffic out of the VCN (for example, to the internet, to an on-premises network, or to a peered VCN). These route tables have rules that look and act similar to traditional network route rules you might already be familiar with. Each rule specifies a destination CIDR block and the target (the next hop) for any traffic that matches that CIDR. 
Here are basics about routing in a VCN:
  * The primary routing scenario is for sending a subnet's traffic to destinations outside the subnet. A subnet has a single route table of you select associated with it unless a VNIC has a route table directly associated with itself or with its IP addresses. For details, see the [Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing) section. All VNICs in that subnet are subject to the rules in the route table. The rules govern how the traffic leaving the subnet is routed.
  * VCN _local routing_ automatically handles traffic between and within the VCN's subnets. Local routing doesn't require defining explicit route rules to enable traffic, local routing rules are implicit and not shown in the routing table. Routing between a VCN's subnets can be changed by adding static routes (see [Intra VCN Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__intra_vcn)). 
  * You can use _[intra-VCN routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__intra_vcn)_ to specify a next-hop private IP, LPG, or DRG within a VCN for traffic destined to another subnet in the VCN. Intra VCN routing lets you create more complex security and network virtualization use cases. OCI also supports Intra VCN routing for traffic entering a VCN through a gateway in addition to traffic between subnets.
  * You can use [Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing) to associate a custom VCN route table with a VNIC or an IP address on a VNIC, which lets you route traffic differently for workloads in the same subnet. 
  * If a route table has overlapping rules, Oracle uses the most specific rule in the table to route the traffic (the rule with the [longest prefix match](https://en.wikipedia.org/wiki/Longest_prefix_match)). Two CIDRs are said to overlap when one CIDR is contained within the other. VCN route tables contain entries for the local VCN routes. If you create a static route for the VCN CIDR block (with the same prefix length as the VCN local route), the static route takes precedence.
  * If no route rule matches the network traffic you intend to route outside the VCN, the traffic is dropped (blackholed).
  * IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses). 


For important details about routing between a VCN and on-premises network, see [Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#Routing_Details_for_Connections_to_Your_OnPremises_Network).
### Working with Route Tables and Route Rules 🔗 
Each VCN automatically comes with a default route table that has implicit rules which include the routes for VCN CIDRs. If you don't specify otherwise, every subnet uses the VCN's default route table. When you add route rules to a VCN, you can add them to the default table. However, you can create custom route tables for each subnet if needed. For example, when you have a public subnet and a private subnet in a VCN (for an example, see [Scenario C: Public and Private Subnets with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm#Scenario_C_Public_and_Private_Subnets_with_a_VPN)), you need to use different route tables for the subnets because the route rules for the subnets need to be different.
Each subnet in a VCN uses a single route table. When you create the subnet, you specify which one to use. You can [change which route table the subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm#subnet-change-routetable "Change which virtial cloud network \(VCN\) route table a subnet uses.") at any time. You can also edit a route table's rules, or remove all the rules from the table.
You can optionally assign a descriptive name to a custom route table during creation. It doesn't have to be unique, and you can change it later. Oracle automatically assigns the route table a unique identifier called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
A route rule specifies a destination CIDR block and the target (the next hop) for any traffic that matches that CIDR. Here are the allowed types of targets for a route rule:
  * [Dynamic Routing Gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs): For subnets that need private access to networks connected to a VCN (for example, an on-premises network connected with a [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") or [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure."), a[ peered VCN in the same region](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region), or a [peered VCN in another region](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions)).
  * [Internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway): For public subnets that need direct access to the internet.
  * [NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm#NAT_Gateway): For subnets with instances that don't have public IP addresses but need outbound access to the internet.
  * [Service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway): For subnets that need private access to Oracle services such as Object Storage.
  * [Local peering gateway (LPG):](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Access_to_Other_VCNs_Peering) For subnets that need private access to a peered VCN in the same region.
  * [Private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#Private_IP_Addresses): For subnets that need to route traffic to an instance in the VCN. For more information, see [Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route). Also see [Overview of Routing for a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN).


**Note** You can't delete a particular resource when it's the target for a route rule. For example, you can't delete an internet gateway that has traffic routed to it. Delete all rules (in all route tables) with that internet gateway as the target before you try to delete the gateway or other resource.
When adding a route rule to a route table, you provide the destination CIDR block and target (plus the **compartment** where the target resides). Exception: if the target is a **service gateway** , instead of a destination CIDR block, you specify an Oracle-provided string that represents the public endpoints for the service of interest. That way you don't need to know all the service's CIDR blocks, which might change over time.
If you misconfigure a rule (for example, enter the wrong destination CIDR block), the network traffic you intended to route might be dropped (blackholed) or sent to an unintended target. 
You can [move a route tables from one compartment to another](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm#move-routetable "Move a Virtual Cloud Network \(VCN\) route table to a different compartment."). Moving a route table doesn't affect its attachment to VCNs or subnets. When you move a route table to a new compartment, inherent policies apply immediately and affect access to the route table. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
You can't delete a VCN's default route table. To delete a custom route table, it must not be associated with a subnet or a gateway, such as DRG, LPG, IGW, NGW or SGW. 
See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
### Intra VCN Routing 🔗 
Intra VCN routing lets you override the default routing decisions applied to traffic destined to IP addresses contained within the VCN CIDR block. Intra VCN routing has the following capabilities: 
  * **Local routes:** Each VCN automatically routes traffic within the VCN and between the VCN subnets, unless you add route rules stating otherwise. Local traffic uses the route table associated with the subnet, including local routing within the VCN CIDR.
  * **Custom Intra VCN routes:** These are route rules you create in the VCN or subnet route table for Intra VCN traffic, which can override normal local routes. All custom Intra VCN routes have a target (DRG, LPG, or private IP in the VCN) and a route type of _static_. 
  * **Best Route Selection:** The longest prefix match (or most specific route) is selected. When several routes for the same prefix are possible, the best route is selected based on the following route type priority:
    1. Static routes (user-defined)
    2. Implicit local routes (created automatically by OCI) not visible in the route table
  * **IPv6:** OCI supports Intra VCN routing for IPv6 VCN prefixes.


**Note** Intra subnet routing isn't supported. Traffic with a destination IP address in the same subnet as the originating VNIC is forwarded (not routed) directly to the appropriate destination.
### Intra VCN Routing Usage 
In the following example, all traffic flowing between the internet and VNICs in a VCN is routed through a security appliance in Subnet-A. Also, traffic between subnets goes through the same firewall. To implement this example, you would:
  1. Create static route rules in the IGW route table that specify a next hop of 10.0.1.4 (a firewall) for inbound traffic.
  2. Create route tables for subnets A, B, and C. Traffic from the internet to subnet B and C must go through the firewall appliance at 10.0.1.4 in subnet A. Traffic between subnet B and C must go through the same firewall.


The following image shows an example of internal routing:
[![Internal Routing example diagram](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vcn_internal.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vcn_internal.svg)
Callout 1: IGW route table Destination | Target | Route Type  
---|---|---  
10.0.0.0/16 | 10.0.1.4 | Static  
Callout 2: Subnet A route table Destination | Target | Route Type  
---|---|---  
0.0.0.0/0 | IGW | Static  
Callout 3: Subnet B route table Destination | Target | Route Type  
---|---|---  
10.0.0.0/16 | 10.0.1.4 | Static  
0.0.0.0/0 | 10.0.1.4  | Static  
Callout 4: Subnet C route table Destination | Target | Route Type  
---|---|---  
10.0.0.0/16 | 10.0.1.4 | Static  
0.0.0.0/0 | 10.0.1.4  | Static  
### Per-resource Routing 🔗 
You can use per-resource routing to assign a custom VCN route table to one or more VNICs or to particular IP addresses on a VNIC. An IP address with an assigned route table can be a primary or secondary IP address for the VNIC. With per-resource routing, a hierarchical preference applies in terms of which route table to use for the routing lookup: the route table on the IP address is preferred over the route table on the VNIC, and the route table on a VNIC is preferred over the route table on the subnet. Here is the route table selection process:
  1. If the VNIC IP address has an associated own route table, this route table is used to route traffic from the IP address.
  2. If a VNIC IP address doesn't have its own route table, the VNIC level route table is used to route traffic from the IP address.
  3. If a VNIC has an associated route able, all IP addresses on the VNIC that don't have an associated route table use the VNIC route table.
  4. If a VNIC doesn't have an associated route table, all IP addresses on the VNIC that don't have an associated route table use the subnet route table.


**Note** Only one route table is used to decide traffic routing for a VNIC or IP address. If per-resource routing is used on a VNIC or IP address, other route tables on the hierarchical chain are skipped. For example, if a VNIC IP address is associated with a route table, that route table is used for routing traffic from the IP address, and the route tables on the VNIC and the subnet are skipped.
The following image shows an example using per-resource routing:
[![Per-resource routing example diagram](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_source_routing.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_source_routing.svg)
Callout A: Custom Route Table A to On-premises Destination | Target | Route Type  
---|---|---  
0.0.0.0/0 | DRG | Static  
Callout B: Custom Route Table B to the Internet Destination | Target | Route Type  
---|---|---  
0.0.0.0/0 | IGW | Static  
In this example, an OCI Compute instance with two VNICs in the same subnet has an application running that needs access to the internet and also to databases or other resources in the on-premises data center. The application uses VNIC A for all traffic bound for an on-premises network and VNIC B for all Internet bound traffic. The cloud network administrator can associate a custom route table with VNIC A where the default route has the DRG as the target, and routes all traffic from VNIC A to the DRG. A second custom route table is associated with VNIC B where the default route has the internet gateway as the target, and routes all traffic from VNIC B to the internet gateway. 
One advantage here is that because these are static rules, the rules are insulated from changes in the CIDR blocks used in the on-premises data center. All changes in the on-premises environment are shared with the DRG using BGP advertisement, and the VCN route tables can be simple and stable.
### Gateway Ingress Routing
Traffic leaving a subnet is routed by using the subnet route table. Traffic entering a subnet is routed using a gateway route table (a route table associated with that gateway). Route rules for gateway ingress routing are supported in route tables associated with the following resources: 
  * Local Peering Gateway (LPG)
  * Dynamic Routing Gateways
  * Internet Gateways 
  * NAT Gateways
  * Service Gateways


**Note** If you associate a route table with one of these gateways, afterward the gateway must always have an associated route table. The associated route table's rules can be changed or removed. For an internet gateway, the target must be in a public subnet.
### Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 
## VCN Route Table Limits 🔗 
This section is specific to limits for VCN route tables. DRG route table limits are provided in the [DRG Route Table Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#DRG_RT_limits) section.
Resource |  Scope |  Oracle Universal Credits |  Pay As You Go or Trial  
---|---|---|---  
VCN Route tables | VCN | 300 | 300  
Route rules | VCN Route table | 200 | 200  
## Using a Private IP as a Route Target 🔗 
If you're not familiar with the definition of a private IP, see [Private IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#Private_IP_Addresses). In short: a private IP is an object that contains a private IP address and related properties and has its own [OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). 
### General Use Cases
OCI uses a subnet's route table to route traffic to a destination IP address outside of the subnet. If the destination is outside the VCN, typically you set up a route rule to route the traffic to a gateway on the VCN (for example, a DRG connected to an on-premises network or another VCN, or an Internet gateway connected to the Internet). If the destination is in another subnet of the same VCN, by default the traffic is routed using the local route for the VCN CIDR. However, you might want to route that traffic through an instance in the VCN first. In that case, you can use a private IP in the VCN as the target instead of a gateway in the VCN. Here are a few reasons you might do this: 
  * To implement a virtual network appliance (NVA) such as a firewall or intrusion detection that filters outgoing traffic from instances.
  * To manage an overlay network on the VCN, which lets you run container orchestration workloads. 
  * To implement Network Address Translation (NAT) in the VCN. Note that Oracle instead recommends using a [NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm#NAT_Gateway) with the VCN. In general, NAT creates outbound internet access for instances that don't have direct internet connectivity. 


To implement these use cases requires more than routing traffic to the instance. Configuration is also required on the instance itself. 
**Tip** You can enable high availability of the private IP route target by using a [secondary private IP address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#overview). In the event of a failure, you can move the secondary private IP from an existing VNIC to another VNIC in the same subnet. See [Moving a Secondary Private IP Address to a Different VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm#top "Move a secondary private IP address to another VNIC in the same subnet.") (Console instructions) and [UpdatePrivateIp](https://docs.oracle.com/iaas/api/#/en/iaas/latest/PrivateIp/UpdatePrivateIp) (API instructions).
### Requirements for Using a Private IP as a Target
  * The private IP must be in the same VCN as the route table.
  * The private IP's VNIC must be configured to skip the source/destination check so that the VNIC can forward traffic. By default, VNICs are configured to perform the check. For more information, see [Overview of VNICs and Physical NICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview).
  * You must configure the instance itself to forward packets.
  * The route rule must specify the OCID of the private IP as the target, and not the IP address itself. Exception: If you use the Console, you can instead specify the private IP address itself as the target, and the Console uses the OCID corresponding to the private IP address in the rule.
**Important**
A route rule with a private IP target can result in blackholing in these cases: 
    * The instance the private IP is assigned to is stopped or terminated
    * The VNIC the private IP is assigned to is updated to enable the source/destination check or is deleted
    * The private IP is unassigned from the VNIC
When a target private IP is terminated, in the Console, the route rule displays a note that the target OCID no longer exists.
For failover: If a target instance is terminated before you can move the secondary private IP to a standby, you must update the route rule to use the OCID of the new target private IP on the standby. The rule uses the target's OCID and not the private IP address itself.


### General Setup Process
  1. Decide which instance you want to receive and forward the traffic.
  2. Select a private IP on the instance (can be on the instance's primary VNIC or a secondary VNIC). To implement failover, set up a [secondary private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#Private_IP_Addresses) on one of the VNICs on the instance. 
  3. Disable the source/destination check on the private IP's VNIC. See [Overview of VNICs and Physical NICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview).
  4. Get the OCID for the private IP. If you're using the Console, you can get either the OCID or the private IP address itself, along with the name of the private IP's compartment. 
  5. For the subnet that needs to route traffic to the private IP, view the subnet's route table. If the table already has a rule with the same destination CIDR but a different target, delete that rule. 
  6. [Add a route rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.") with the following:
     * **Target Type:** See the list of target types in [Overview of Routing for a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN). If the target type is a DRG, the VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself. If the target is a private IP object, before you specify the target you must first disable the source/destination check on the VNIC that uses that private IP object. For more information, see [Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route). 
     * **Destination CIDR Block** : Available only if the target isn't a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway). The value is the destination CIDR block for the traffic. You can provide a specific destination CIDR block, or use 0.0.0.0/0 if all traffic leaving the subnet needs to be routed to the target specified in this rule.
     * **Destination Service:** Available only if the target is a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway). The value is the [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that you're interested in.
     * **Compartment:** The compartment containing the target.
     * **Target:** The target. If the target is a private IP object, enter its OCID. Or you can enter the private IP address itself, in which case the Console finds the corresponding OCID and uses it as the target for the route rule.
     * **Description:** An optional description of the rule.


As mentioned earlier, you must configure the instance itself to forward packets.
Was this article helpful?
YesNo

