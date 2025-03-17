Updated 2024-08-21
# Local VCN Peering using Local Peering Gateways
This topic is about _local VCN peering._ In this case, _local_ means that the VCNs reside _in the same region._ If the VCNs are in different regions, see [Remote VCN Peering using a Legacy DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions).
Local peering gateways are still supported. This scenario assumes you are using a legacy [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions). Oracle currently recommends routing traffic from one VCN to another through an upgraded DRG as described in [Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod "This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs."). 
## Overview of Local VCN Peering 🔗 
_Local VCN peering_ is the process of connecting two VCNs in the same region so that their resources can communicate using private IP addresses without routing the traffic over the internet or through your on-premises network. The VCNs can be in the same Oracle Cloud Infrastructure **tenancy** or different ones. Without peering, a given VCN would need an [internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway) and public IP addresses for the instances that need to communicate with another VCN.
See [Gateway Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#gateway_limits) and [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti) for limits-related information.
For more information, see [Access to Other VCNs: Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Access_to_Other_VCNs_Peering). 
### Summary of Networking Components for Peering using an LPG
At a high level, the Networking service components required for a local peering include:
  * Two VCNs with non-overlapping CIDRs, in the same region
  * A _local peering gateway (LPG)_ on each VCN in the peering relationship.
  * A _connection_ between those two LPGs.
  * Supporting route rules to enable traffic to flow over the connection, and only to and from select subnets in the respective VCNs (if wanted).
  * Supporting security rules to control the types of traffic allowed to and from the instances in the subnets that need to communicate with the other VCN.


The following diagram illustrates the components.
[![This image shows the basic layout of two VCNs that are locally peered, each with a local peering gateway.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_basic.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_basic.svg)
**Note**
A given VCN can use the peered LPGs to reach these resources:
  * VNICs in the other VCN
  * An on-premises network attached to the other VCN, if an advanced routing scenario called [transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region) has been set up for the VCNs


A VCN can't use its peered VCN to reach other destinations outside of the VCNs (such as the internet). For example, if VCN-1 in the preceding diagram were to have an internet gateway, the instances in VCN-2 couldn't use it to send traffic to endpoints on the internet. However, VCN-2 could _receive_ traffic from the internet by way of VCN-1. For more information, see [Important Implications of VCN Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Importan2).
### Explicit Agreement Required from Both Sides
Peering involves two VCNs that might be owned by the same party or two different ones. The two parties might both be in your company but in different departments. Or the two parties might be in entirely different companies (for example, in a service-provider model).
Peering between two VCNs requires explicit agreement from both parties in the form of Oracle Cloud Infrastructure Identity and Access Management policies that each party implements for their own VCN's **compartment** or tenancy. If the VCNs are in different tenancies, each administrator must provide their tenancy [OCID](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm) and put in place special policy statements to enable the peering.
### Advanced Scenario: Transit Routing
The advanced routing scenario called [transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region) enables communication between an on-premises network and multiple VCNs over a _single_[Oracle Cloud Infrastructure FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") or [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\)."). The VCNs must be in the same region and locally peered in a hub-and-spoke layout. As part of the scenario, the VCN acting as the hub has a route table _associated with each LPG_ (typically route tables are associated with a VCN's subnets). 
When you create an LPG, you can optionally associate a route table with it. Or if you already have an existing LPG without a route table, you [can associate a route table with it](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/lpg-add-route-table.htm#add_route_table "To use transit routing, you must associate a route table to an LPG after you create the LPG."). The route table must belong to the LPG's VCN. A route table associated with an LPG can contain only rules that use the VCN's [attached DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs) as the target. It can also support private IP next hop routes to an instance in the VCN.
An LPG can exist without a route table associated with it. However, after you associate a route table with an LPG, there must always be a route table associated with it. But, you can associate a _different_ route table. You can also edit the table's rules, or delete some or all rules.
## Important Local Peering Concepts 🔗 
The following concepts help you understand the basics of VCN peering and how to establish a local peering. 

PEERING
    A _peering_ is a single peering relationship between two VCNs. Example: If VCN-1 peers with three other VCNs, there are three peerings. The _local_ part of _local peering_ indicates that the VCNs are in the same region. A specific VCN can have a maximum of 10 local peerings at a time.     
**Caution** The two VCNs in the peering relationship must not have overlapping CIDRs. However, if VCN-1 is peered with three other VCNs, those three VCNs can have overlapping CIDRs with each other. You would set up the subnets in VCN-1 to have route rules that direct traffic to the targeted peered VCN. 

VCN ADMINISTRATORS
    In general, VCN peering can occur only if both of the VCN administrators agree to it. In practice, this means that the two administrators must:     
  * Share some basic information with each other.
  * Coordinate to set up the required Oracle Cloud Infrastructure Identity and Access Management policies to enable the peering.
  * Configure their VCNs for the peering.

    Depending on the situation, a single administrator might be responsible for both VCNs and the related policies.      For more information about the required policies and VCN configuration, see [Setting Up a Local Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Setting). 

ACCEPTOR AND REQUESTOR
    To implement the IAM policies required for peering, the two VCN administrators must assign one administrator to be the _requestor_ and the other as the _acceptor_. The requestor must be the one to initiate the request to connect the two LPGs. In turn, the acceptor must create a particular IAM policy that gives the requestor permission to connect to LPGs in the acceptor's **compartment**. Without that policy, the requestor's request to connect fails. 

LOCAL PEERING GATEWAY (LPG)
    A _local peering gateway (LPG)_ is a component on a VCN for routing traffic to a locally peered VCN. As part of configuring the VCNs, each administrator must create an LPG for their VCN. A specific VCN must have a separate LPG for each local peering it establishes (maximum 10 LPGs per VCN). To continue with the previous example: VCN-1 would have three LPGs to peer with three other VCNs. In the API, a [LocalPeeringGateway](https://docs.oracle.com/iaas/api/#/en/iaas/latest/LocalPeeringGateway/) is an object that contains information about the peering. You can't reuse an LPG to later establish another peering. 

PEERING CONNECTION
    When the requestor initiates the request to peer (in the Console or API), they're effectively asking to _connect the two LPGs_. The requestor must have information to identify each LPG (such as the LPG's compartment and name, or the LPG's OCID). Each administrator must put the required IAM policies in place for their compartment or tenancy.     Either VCN administrator can terminate a peering by deleting their LPG. In that case, the other LPG's status switches to REVOKED. The administrator could instead make the connection stop functioning by removing the route rules or security rules that enable traffic to flow across the connection (see the next sections).  

ROUTING TO THE LPG
    As part of configuring the VCNs, each administrator must update the [VCN's routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) to enable traffic to flow between the VCNs. In practice, this looks like routing you set up for any gateway (such as an [internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway) or [dynamic routing gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs)). For each subnet that needs to communicate with the other VCN, you update the subnet's route table. The route rule specifies the destination traffic's CIDR and the LPG as the target. The LPG routes traffic that matches that rule to the other LPG, which in turn routes the traffic to the next hop in the other VCN.     In the following diagram, VCN-1 and VCN-2 are peered. Traffic from an instance in Subnet A (10.0.0.15) destined for an instance in VCN-2 (192.168.0.15) is routed to LPG-1 based on the rule in Subnet A's route table (see [Callout 1: Subnet A Route Table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Importan__callout1 "Route table for subnet A.")). From there the traffic is routed to LPG-2, and then from there, on to its destination in Subnet X.     
[![This image shows the path of traffic routed from one local peering gateway to the other.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_layout.svg)
Callout 1: Subnet A Route Table Destination CIDR | Route Target  
---|---  
0.0.0.0/0 | Internet Gateway  
172.16.0.0/12 | DRG  
192.168.0.0/16 | LPG-1  
Callout 2: Subnet X Route Table Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | LPG-2       
**Note**
As mentioned earlier, a specific VCN can use the peered LPGs to reach VNICs in the other VCN, or the on-premises network if [transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region) is set up for the VCNs. But a VCN can't use the peered VCN to reach other destinations outside of the VCNs (such as the internet). For example, in the preceding diagram, VCN-2 can't use the internet gateway attached to VCN-1. 

SECURITY RULES
    Each subnet in a VCN has one or more [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) that control traffic in and out of the subnet's VNICs at the packet level. You can use security lists to control the type of traffic allowed with the other VCN. As part of configuring the VCNs, each administrator must choose which subnets in their own VCN need to communicate with VNICs in the other VCN and update their subnet's security lists to match.      If you use [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) (NSGs) to implement security rules, notice that you have the option to write security rules for an NSG that specify _another_ NSG as the source or destination of traffic. However, the two NSGs _must belong to the same VCN_.
## Important Implications of VCN Peering 🔗 
If you haven't yet, read [Important Implications of Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Importan2) to understand important access control, security, and performance implications for peered VCNs.
## Setting Up a Local Peering 🔗 
Here's the general process for setting up a peering between two VCNs in the same region:
  1. **Create the LPGs:** Each VCN administrator creates an LPG for their own VCN. 
  2. **Share information:** The administrators share the basic required information. 
  3. **Set up the required IAM policies for the connection:** The administrators set up IAM policies to enable the connection to be established. 
  4. **Establish the connection:** The requestor connects the two LPGs.
  5. **Update route tables:** Each administrator updates their VCN's route tables to enable traffic between the peered VCNs as wanted.
  6. **Update security rules:** Each administrator updates their VCN's security rules to enable traffic between the peered VCNs as wanted.


If wanted, the administrators can perform tasks E and F _before_ establishing the connection. In that case, each administrator must know the CIDR block or specific subnets from the other's VCN and share that in task B. After the connection is established, you can also get the CIDR block of the other VCN by viewing your own LPG's details in the Console. Look for **Peer Advertised CIDR**. Or if you're using the API, see the `peerAdvertisedCidr` parameter.
You will also need to pre-configure some IAM settings like groups prior to going through the step-by-step process.
[Task A: Create the LPGs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm)
See the instructions in [Creating a Local Peering Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-lpg.htm#create-lpg "Create a local peering gateway \(LPG\) that instances, load balancers, and other resources can use to connect to resources in other virtual cloud networks \(VCNs\) in the same Oracle Cloud Infrastructure \(OCI\) region."). 
[Task B: Share information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm)
If you're the **requestor** , give this information to the acceptor (for example, by email or other out-of-band method):
  * If the VCNs are in the **same tenancy:** Name of the IAM group that should be granted permission to create a connection in the acceptor's compartment. In the example in the next task, the group is RequestorGrp. 
  * If the VCNs are in **different tenancies:** [OCID for your tenancy](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm#Oracle), and OCID for the IAM group that should be granted permission to create a connection in the acceptor's compartment. In the example in the next task, it's the OCID for the RequestorGrp.
  * Optional: Your VCN's CIDR, or specific subnets for peering with the other VCN.


If you're the **acceptor** , give this information to the requestor:
  * If the VCNs are in the **same tenancy:** OCID for your LPG. Optionally, also the names of your VCN, LPG, and the compartment each is in.
  * If the VCNs are in **different tenancies:** OCID for your LPG, and OCID for your tenancy.
  * Optional: Your VCN's CIDR, or specific subnets for peering with the other VCN.


[Task C: Set up the IAM policies](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm)
If both VCNs are in the same tenancy, use the policy in [Local Peering using an LPG (VCNs in the Same Tenancy)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG).
If the VCNs are in different tenancies, use the policy in [Local Peering using an LPG (VCNs in Different Tenancies)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG-xten).
[Task D: Establish the connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm)
See the instructions in [Connecting to Another LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/connect-lpg.htm#lpg-connection "Connect a local peering gateway \(LPG\) to another one in a different virtual cloud network \(VCN\) in the same region."). 
[Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm)
Configure the route tables to use the information for the other VCN that you were given in [Task B: Share information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#share_info), using the instructions in [Configuring VCN Route Tables to Use an LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-rt.htm#give-lpg-rt "Update a Virtual Cloud Network \(VCN\) route table to include a new rule that directs traffic destined for the other VCN's CIDR to flow through the local peering gateway \(LPG\)."). 
[Task F: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm)
Configure the security rules to use the information for the other VCN that you were given in [Task B: Share information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#share_info), using the instructions in [Configuring Security Rules to Use an LPG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/give-lpg-sl.htm#give-lpg-sl "Update a security list in a Virtual Cloud Network \(VCN\) to include a new rule that allows traffic destined for the other VCN's CIDR to flow through a local peering gateway \(LPG\)."). 
Was this article helpful?
YesNo

