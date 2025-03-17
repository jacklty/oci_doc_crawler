Updated 2025-01-15
# Remote VCN Peering through an Upgraded DRG
This topic is about _remote VCN peering._
In this case, _remote_ means that the virtual cloud networks (VCNs) are each attached to a different **dynamic routing gateway** (DRG) that resides _in a different region._ If the VCNs you want to connect are in the same region, see [Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod "This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs."). 
**Note** This scenario is available to an upgraded or legacy DRG, with the exception that a legacy DRGs will not support connecting DRGs in different tenancies. See [DRG versions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions) for a breakdown on the possible versions of DRG. 
Before you attempt to implement this scenario, ensure that: 
  * VCN A is attached to DRG A in region 1
  * VCN B is attached to DRG B in region 2
  * Routing configuration in both DRGs is unchanged
  * [Appropriate IAM permissions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways.") are applied for VCNs that are either in the same or different tenancies


## Overview of Remote VCN Peering
_Remote VCN peering_ is the process of connecting two VCNs in different regions. The peering allows the VCNs' resources to communicate using private IP addresses without routing the traffic over the internet or through your on-premises network. The VCNs can be in the same Oracle Cloud Infrastructure **tenancy** or different ones. Without peering, a given VCN would need an [internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway) and public IP addresses for the instances that need to communicate with another VCN in a different region.
## Summary of Networking Components for Remote Peering 🔗 
At a high level, the Networking service components required for a remote peering include:
  * Two VCNs with non-overlapping CIDRs, in different regions. 
**Note**
No VCN CIDRs can overlap
The two VCNs in the peering relationship cannot have overlapping CIDRs. Also, if a particular VCN has multiple peering relationships, those other VCNs must not have overlapping CIDRs with each other. For example, if VCN-1 is peered with VCN-2 and also VCN-3, then VCN-2 and VCN-3 must not have overlapping CIDRs.
If you are configuring this scenario, you have to meet this requirement in the planning stage. Routing problems are likely when overlapping CIDRs occur, but you aren't prevented by the Console or API operations from creating a configuration that causes issues.
  * A Dynamic Routing Gateway (DRG) attached to each VCN in the peering relationship. Your VCN already has a DRG if you're using a [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") IPSec tunnel or an [Oracle Cloud Infrastructure FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") private virtual circuit. 
  * A _remote peering connection (RPC)_ on each DRG in the peering relationship.
  * A _connection_ between those two RPCs.
  * Supporting [route rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) to enable traffic to flow over the connection, and only to and from select subnets in the respective VCNs (if wanted).
  * Supporting [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) to control the types of traffic allowed to and from the instances in the subnets that need to communicate with the other VCN.


The following diagram illustrates the components.
[![This image shows the basic layout of two VCNs that are remotely peered, each with a remote peering connection on the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_basic.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_basic.svg)
**Note** A given VCN can use the connected RPCs to reach only VNICs in the other VCN, or your on-premises network if the DRG has a connection to an on-premises CPE. For example, if VCN-1 in the preceding diagram were to have an internet gateway, the instances in VCN-2 could NOT use it to send traffic to endpoints on the internet. For more information, see [Important Implications of Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Importan2).
## Important Implications of Peering
If you haven't yet, read [Important Implications of Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Importan2) to understand important access control, security, and performance implications for peered VCNs.
Peering VCNs in different tenancies has some permissions complications that need to be resolved in both tenancies. See [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways.") for details on the permissions needed. 
## Spoke-to-Spoke: Remote Peering with Transit Routing (Legacy DRGs Only)
**Note** The scenario this section mentions is still supported, but Oracle recommends you use the DRG transit routing method described in [Routing traffic through a central network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#scenario_g).
Imagine that in each region you have multiple VCNs in a hub-and-spoke layout, as shown in the following diagram. This type of layout within a region is discussed in detail in [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region). The spoke VCNs in a given region are [locally peered](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Access_to_Other_VCNs_Peering) with the hub VCN in the same region, using **local peering gateways**.
You can set up remote peering between the two hub VCNs. You can then also set up transit routing for the hub VCN's DRG and LPGs, as discussed in [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region). This setup allows a spoke VCN in one region to communicate with one or more spoke VCNs in the other region without needing a remote peering connection directly between those VCNs. 
For example, you could configure routing so that resources in VCN-1-A could communicate with resources in VCN-2-A and VCN-2-B by way of the hub VCNs. That way, VCN 1-A is not required to have a _separate_ remote peering with each of the spoke VCNs in the other region. You could also set up routing so that VCN-1-B could communicate with the spoke VCNs in region 2, without needing its own remote peerings to them.
[![This image shows the basic layout of two regions with VCNs in a hub-and-spoke layout, with remote peering between the hub VCNs.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_spoke_to_spoke.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_spoke_to_spoke.svg)
## Spoke-to-Spoke: Remote Peering with Transit Routing (Upgraded DRG)
**Note** The scenario this section uses the DRG transit routing method described in [Routing traffic through a central network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#scenario_g).
Imagine that in each region you have multiple VCNs in a hub-and-spoke layout, as shown in the following diagram. This type of layout within a region is discussed in detail in [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region). The spoke VCNs in a given region are [locally peered](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod "This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs.") with the hub DRG/VCN pair in the same region by mutual connection to the DRG.
You can set up remote peering between the two hub VCNs. You can then also set up transit routing for the hub VCN's DRG, as discussed in [Routing traffic through a central network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#scenario_g). This setup allows a spoke VCN in one region to communicate with one or more spoke VCNs in the other region without needing a remote peering connection directly between those VCNs. 
For example, you could configure routing so that resources in VCN-1-A could communicate with resources in VCN-2-A and VCN-2-B by way of the hub VCNs. That way, VCN 1-A is not required to have a _separate_ remote peering with each of the spoke VCNs in the other region. You could also set up routing so that VCN-1-B could communicate with the spoke VCNs in region 2, without needing its own remote peerings to them.
[![This image shows the basic layout of two regions with VCNs in a hub-and-spoke layout, with remote peering between the hub VCNs.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_spoke_to_spoke_2021.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_spoke_to_spoke_2021.svg)
## Important Remote Peering Concepts
The following concepts help you understand the basics of VCN peering and how to establish a remote peering. 

PEERING
    A _peering_ is a single peering relationship between two VCNs. Example: If VCN-1 peers with two other VCNs, two peerings exist. The _remote_ part of _remote peering_ indicates that the VCNs are in different regions. For this method of remote peering, the VCNs can be in the same tenancy or in different tenancies. 

VCN ADMINISTRATORS
    In general, VCN peering can occur only if both of the VCN administrators agree to it. In practice, the two administrators must:     
  * Share some basic information with each other.
  * Coordinate to set up the required Oracle Cloud Infrastructure Identity and Access Management policies to enable the peering.
  * Configure their VCNs for the peering.

    Depending on the situation, a single administrator might be responsible for both VCNs and the related policies. The VCNs can be in the same tenancy or in different tenancies.     For more information about the required policies and VCN configuration, see [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways."). 

ACCEPTOR AND REQUESTOR
    To implement the IAM policies required for peering, the two VCN administrators must designate one administrator as the _requestor_ and the other as the _acceptor_. The requestor must be the one to initiate the request to connect the two RPCs. In turn, the acceptor must create a particular IAM policy that gives the requestor permission to connect to RPCs in the acceptor's **compartment**. Without that policy, the requestor's request to connect fails. 

REGION SUBSCRIPTION
    To peer with a VCN in another region, your tenancy must first be subscribed to that region. For information about subscribing, see [Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm).  

REMOTE PEERING CONNECTION (RPC)
    A _remote peering connection (RPC)_ is a component you create on the DRG attached to your VCN. The RPC's job is to act as a connection point for a remotely peered VCN. As part of configuring the VCNs, each administrator must create an RPC for the DRG on their VCN. A given DRG must have a separate RPC for each remote peering it establishes for the VCN. To continue with the previous example: the DRG on VCN-1 would have two RPCs to peer with two other VCNs. In the API, a [RemotePeeringConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/) is an object that contains information about the peering. You can't reuse an RPC to later establish another peering with it. 

CONNECTION BETWEEN TWO RPCS
    When the requestor initiates the request to peer (in the Console or API), they're effectively asking to _connect the two RPCs_. The requestor must have information to identify each RPC (such as the RPC's region and **OCID**).      Either VCN administrator can terminate a peering by deleting their RPC. In that case, the other RPC's status switches to REVOKED. The administrator could instead render the connection non-functional by removing the route rules that enable traffic to flow across the connection (see the next section).  

ROUTING TO THE DRG
    As part of configuring the VCNs, each administrator must update the [VCN's routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) to enable traffic to flow between the VCNs. For each subnet that needs to communicate with the other VCN, you update the subnet's route table. The route rule specifies the destination traffic's CIDR and your DRG as the target. Your DRG routes traffic that matches that rule to the other DRG, which in turn routes the traffic to the next hop in the other VCN.     In the following diagram, VCN-1 and VCN-2 are peered. Traffic from an instance in Subnet A (10.0.0.15) destined for an instance in VCN-2 (192.168.0.15) is routed to DRG-1 based on the rule in Subnet A's route table. From there the traffic is routed through the RPCs to DRG-2, and then from there, on to the destination in Subnet X.     
[![This image shows the route tables and path of traffic routed from one DRG to the other.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_layout.svg)
Callout 1: Subnet A Route Table Destination CIDR | Route Target  
---|---  
0.0.0.0/0 | Internet Gateway  
192.168.0.0/16 | DRG-1  
Callout 2: Subnet X Route Table Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | DRG-2       
**Note**
As mentioned earlier, a given VCN can use the connected RPCs to reach only VNICs in the other VCN or your on-premises network, and not destinations on the internet. For example, in the preceding diagram, VCN-2 cannot use the internet gateway attached to VCN-1. 

SECURITY RULES
    Each subnet in a VCN has one or more [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) that control traffic in and out of the subnet's VNICs at the packet level. You can use security lists to control the type of traffic allowed with the other VCN. As part of configuring the VCNs, each administrator must determine which subnets in their own VCN need to communicate with VNICs in the other VCN and update their subnet's security lists accordingly.      If you use [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) (NSGs) to implement security rules, notice that you can write security rules for an NSG that specify _another_ NSG as the source or destination of traffic. However, the two NSGs _must belong to the same VCN_.
## Important Implications of Peering
If you haven't yet, read [Important Implications of Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Importan2) to understand important access control, security, and performance implications for peered VCNs.
## Setting Up a Remote Peering
This section covers the general process for setting up a peering between two VCNs in different regions.
**Important**
The following procedure assumes that:
  * Your tenancy is subscribed to the other VCN's region. If not, see [Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm). 
  * You already have a VCN attached to your DRG. If you don't, see [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs).
  * You have already set up the required IAM policies for the connection. IAM policies for remote peering in the same tenancy and between tenancies are different. See [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways.")


Overview of required steps:
  1. **Create the RPCs:** Each VCN administrator creates an RPC for their own VCN's DRG. 
  2. **Share information:** The administrators share the basic required information. 
  3. **Establish the connection:** The _requestor_ connects the two RPCs (see [Important Remote Peering Concepts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Importan) for the definition of the _requestor_ and _acceptor_).
  4. **Update route tables:** Each administrator updates their VCN's route tables to enable traffic between the peered VCNs as intended.
  5. **Update security rules:** Each administrator updates their VCN's security rules to enable traffic between the peered VCNs as intended.


If you want, the administrators can perform tasks 4 and 5 _before_ establishing the connection. Each administrator needs to know the CIDR block or specific subnets from the other's VCN and share that in task 2.
[Task A: Create the RPCs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm)
Each administrator creates an RPC for their own VCN's DRG. "You" in the following procedure means an administrator (either the [acceptor or requestor](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Importan)).
**Note**
Required IAM Policy to Create RPCs
If the administrators already have broad network administrator permissions (see [Let network admins manage a cloud network](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network)), then they have permission to create, update, and delete RPCs. Otherwise, here's an example policy giving the necessary permissions to a group called RPCAdmins. The second statement is required because creating an RPC affects the DRG it belongs to, so the administrator must have permission to manage DRGs.
Copy
```
Allow group RPCAdmins to manage remote-peering-connections in tenancy
Allow group RPCAdmins to manage drgs in tenancy

```

  1. In the Console, confirm you're viewing the compartment that contains the DRG that you want to add the RPC to. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
  2. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  3. Click the DRG you're interested in. 
  4. Under **Resources** , click **Remote Peering Connections Attachments**.
  5. Click **Create Remote Peering Connection**.
  6. Enter the following:
     * **Name:** A friendly name for the RPC. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **Create in compartment** : The compartment where you want to create the RPC, if different from the compartment you're currently working in. 
  7. Click **Create Remote Peering Connection**.
The RPC is then created and displayed on the **Remote Peering Connections** page in the compartment you chose. 
  8. If you're the acceptor, record the RPC's region and OCID to later give to the requestor. 
  9. If the two VCNs are in different tenancies, record your tenancy OCID (found on the bottom of the page in the Console). Give the OCID to the other administrator later.


[Task B: Share information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm)
This task is specific to a cross-tenancy connection. If your connection is in the same tenancy, you can skip to the next task.
  * If you're the acceptor, give this information to the requestor (for example, by email or other out-of-band method):
    * The region your VCN is in (the requestor's tenancy must be subscribed to this region). 
    * Your RPC's OCID. 
    * The CIDR blocks for subnets in your VCN you want available to the other VCN. The requestor needs this information when setting up routing for the requestor VCN.
    * If the VCNs are in different tenancies: the OCID for your tenancy.
  * If you're the requestor, give this information to the acceptor:
    * The region your VCN is in (the acceptor's tenancy must be subscribed to this region).
    * If the VCNs are in the same tenancy: The name of the IAM group that will be granted permission to create a connection in the acceptor's compartment (in the example in the next task, the group is RequestorGrp). 
    * If the VCNs are in different tenancies: the OCID for your tenancy.
    * The CIDR blocks for subnets in your VCN you want available to the other VCN. The acceptor needs this information when setting up routing for the acceptor VCN.


[Task C: Establish the connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm)
The requestor must perform this task.
Prerequisite: The requestor must have:
  * The region the acceptor's VCN is in (the requestor's tenancy must be subscribed to the region).
  * The OCID of the acceptor's RPC.
  * The OCID of the acceptor's tenancy (only if the acceptor's VCN is in a different tenancy)


  1. In the Console, confirm you're viewing the compartment that contains the DRG that you want to add the RPC to. For information about compartments and access control, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
  2. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  3. Click the DRG you're interested in. 
  4. Under **Resources** , click **Remote Peering Connections**.
  5. View the details for the requestor RPC that you want to connect to the acceptor RPC. To do this, click the name of the RPC in the **Remote Peering Connection** column corresponding to the RPC attachment that you created in Task A.
**Note** If this is an RPC within the same tenancy, you don't need to worry about whether the RPC gets established from the requestor or acceptor.
  6. Click **Establish Connection**.
  7. Enter the following: 
     * **Region:** The region that contains the acceptor's VCN. The list includes only regions that both support remote VCN peering and that your tenancy is subscribed to.
     * **Remote Peering Connection OCID:** The OCID of the acceptor's RPC. 
  8. Click **Establish Connection**.


The connection is established and the RPC's state changes to PEERED.
[Task D: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm)
As mentioned earlier, each administrator can do this task before or after the connection is established. 
Prerequisite: Each administrator must have the CIDR block or specific subnets for the other VCN. 
For your own VCN:
  1. Determine which subnets in your VCN need to communicate with the other VCN.
  2. Update the route table for each of those subnets to include a new rule that directs traffic destined for the other VCN to your DRG: 
    1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the VCN you're interested in. 
    3. Under **Resources** , click **Route Tables**. 
    4. Click the route table you're interested in. 
    5. Click **Add Route Rule** and enter the following:
       * **Target Type:** Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself. 
       * **Destination CIDR Block:** The other VCN's CIDR block. If you want, you can specify a subnet or particular subset of the peered VCN's CIDR.
       * **Description:** An optional description of the rule.
    6. Click **Add Route Rule**.


Any subnet traffic with a destination that matches the rule is routed to your DRG. For more information about setting up route rules, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
**Tip** Without the required routing, traffic doesn't flow between the peered DRGs. If a situation occurs where you need to temporarily stop the peering, you can simply remove the route rules that enable traffic. You don't need to delete the RPCs.
[Task E: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm)
As mentioned earlier, each administrator can do this task before or after the connection is established. 
Prerequisite: Each administrator must have the CIDR block or specific subnets for the other VCN. In general, use the same CIDR block you used in the route table rule in [Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Step4). 
What rules should you add? 
  * Ingress rules for the types of traffic you want to allow from the other VCN, specifically from the VCN's CIDR or specific subnets.
  * Egress rule to allow outgoing traffic from your VCN to the other VCN. If the subnet already has a broad egress rule for all types of protocols to all destinations (0.0.0.0/0), then you don't need to add a special one for the other VCN.


**Note** The following procedure uses security lists, but you could instead implement the security rules in a [network security group](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) and then create the subnet's resources in that NSG. 
For your own VCN:
  1. Determine which subnets in your VCN need to communicate with the other VCN.
  2. Update the security list for each of those subnets to include rules to allow the intended egress or ingress traffic specifically with the CIDR block or subnet of the other VCN: 
    1. In the Console, while viewing the VCN you're interested in, click **Security Lists**. 
    2. Click the security list you're interested in. 
    3. Under **Resources** , click either **Ingress Rules** or **Egress Rules** depending on the type of rule you want to work with. 
    4. If you want to add a rule, click **Add Ingress Rule** (or **Add Egress Rule**).
    5. If you want to delete an existing rule, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Remove**.
    6. If you wanted to edit an existing rule, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.


For more information about security rules, see [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules).
Was this article helpful?
YesNo

