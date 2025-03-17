Updated 2025-01-15
# Remote VCN Peering using a Legacy DRG
This topic is about _remote VCN peering._ In this case, _remote_ means that the VCNs reside _in different regions._ If the VCNs you want to connect are in the same region, see [Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region). 
**Note** This article refers specifically to using a legacy DRG, the information in [Remote VCN Peering through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e "This topic is about remote VCN peering.") using an upgraded DRG is the current recommendation from Oracle. See [DRG versions](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions) for a breakdown on the possible versions of DRG.
## Overview of Remote VCN Peering 🔗 
_Remote VCN peering_ is the process of connecting two VCNs in different regions (but the same **tenancy**). The peering allows the VCNs' resources to communicate using private IP addresses without routing the traffic over the internet or through your on-premises network. Without peering, a given VCN would need an [internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway) and public IP addresses for the instances that need to communicate with another VCN in a different region.
### Summary of Networking Components for Remote Peering
At a high level, the Networking service components required for a remote peering include:
  * Two VCNs with non-overlapping CIDRs, in different regions that support remote peering. 
**Note**
All VCN CIDRs Must Not Overlap
The two VCNs in the peering relationship must not have overlapping CIDRs. Also, if a particular VCN has multiple peering relationships, those other VCNs must not have overlapping CIDRs with each other. For example, if VCN-1 is peered with VCN-2 and also VCN-3, then VCN-2 and VCN-3 must not have overlapping CIDRs.
  * A Dynamic Routing Gateway (DRG) attached to each VCN in the peering relationship. Your VCN already has a DRG if you're using a [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") IPSec tunnel or an [Oracle Cloud Infrastructure FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") private virtual circuit. 
  * A _remote peering connection (RPC)_ on each DRG in the peering relationship.
  * A _connection_ between those two RPCs.
  * Supporting [route rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) to enable traffic to flow over the connection, and only to and from select subnets in the respective VCNs (if desired).
  * Supporting [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) to control the types of traffic allowed to and from the instances in the subnets that need to communicate with the other VCN.


The following diagram illustrates the components.
[![This image shows the basic layout of two VCNs that are remotely peered, each with a remote peering connection on the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_basic.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_basic.svg)
**Note** A given VCN can use the connected RPCs to reach only VNICs in the other VCN or your on-premises network, and not destinations outside of the VCNs such as the internet. For example, if VCN-1 in the preceding diagram were to have an internet gateway, the instances in VCN-2 could NOT use it to send traffic to endpoints on the internet. For more information, see [Important Implications of Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Importan2).
### Spoke-to-Spoke: Remote Peering with Transit Routing
**Note** The scenario this section mentions is still supported, but is deprecated. Oracle recommends you use the DRG Transit routing method described in [Routing traffic through a central network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#scenario_g).
Imagine that in each region you have multiple VCNs in a hub-and-spoke layout, as shown in the following diagram. This type of layout within a region is discussed in detail in [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region). The spoke VCNs in a given region are [locally peered](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Access_to_Other_VCNs_Peering) with the hub VCN in the same region, using **local peering gateways**.
You can set up remote peering between the two hub VCNs. You can then also set up transit routing for the hub VCN's DRG and LPGs, as discussed in [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region). This setup allows a spoke VCN in one region to communicate with one or more spoke VCNs in the other region without needing a remote peering connection directly between those VCNs. 
For example, you could configure routing so that resources in VCN-1-A could communicate with resources in VCN-2-A and VCN-2-B by way of the hub VCNs. That way, VCN 1-A is not required to have a _separate_ remote peering with each of the spoke VCNs in the other region. You could also set up routing so that VCN-1-B could communicate with the spoke VCNs in region 2, without needing its own remote peerings to them.
[![This image shows the basic layout of two regions with VCNs in a hub-and-spoke layout, with remote peering between the hub VCNs.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_spoke_to_spoke.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_spoke_to_spoke.svg)
### Explicit Agreement Required from Both Sides
Peering involves two VCNs in the same tenancy that might be administered by the same party or two different ones. The two parties might both be in your company but in different departments. 
Peering between two VCNs requires explicit agreement from both parties in the form of Oracle Cloud Infrastructure Identity and Access Management policies that each party implements for their own VCN's **compartment**. 
## Important Remote Peering Concepts 🔗 
The following concepts help you understand the basics of peering and how to establish a remote peering. 

PEERING
    A _peering_ is a single peering relationship between two VCNs. Example: If VCN-1 peers with two other VCNs, then there are two peerings. The _remote_ part of _remote peering_ indicates that the VCNs are in different regions.  

VCN ADMINISTRATORS
    In general, VCN peering can occur only if both of the VCN administrators agree to it. In practice, this means that the two administrators must:     
  * Share some basic information with each other.
  * Coordinate to set up the required Oracle Cloud Infrastructure Identity and Access Management policies to enable the peering.
  * Configure their VCNs for the peering.

    Depending on the situation, a single administrator might be responsible for both VCNs and the related policies.      For more information about the required policies and VCN configuration, see [Setting Up a Remote Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Setting). 

ACCEPTOR AND REQUESTOR
    To implement the IAM policies required for peering, the two VCN administrators must designate one administrator as the _requestor_ and the other as the _acceptor_. The requestor must be the one to initiate the request to connect the two RPCs. In turn, the acceptor must create a particular IAM policy that gives the requestor permission to connect to RPCs in the acceptor's **compartment**. Without that policy, the requestor's request to connect fails. 

REGION SUBSCRIPTION
    To peer with a VCN in another region, your tenancy must first be subscribed to that region. For information about subscribing, see [Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm).  

REMOTE PEERING CONNECTION (RPC)
    A _remote peering connection (RPC)_ is a component you create on the DRG attached to your VCN. The RPC's job is to act as a connection point for a remotely peered VCN. As part of configuring the VCNs, each administrator must create an RPC for the DRG on their VCN. A given DRG must have a separate RPC for each remote peering it establishes for the VCN. To continue with the previous example: the DRG on VCN-1 would have two RPCs to peer with two other VCNs. In the API, a [RemotePeeringConnection](https://docs.oracle.com/iaas/api/#/en/iaas/latest/RemotePeeringConnection/) is an object that contains information about the peering. You can't reuse an RPC to later establish another peering with it. 

CONNECTION BETWEEN TWO RPCS
    When the requestor initiates the request to peer (in the Console or API), they're effectively asking to _connect the two RPCs_. This means the requestor must have information to identify each RPC (such as the RPC's region and **OCID**).      Either VCN administrator can terminate a peering by deleting their RPC. In that case, the other RPC's status switches to REVOKED. The administrator could instead render the connection non-functional by removing the route rules that enable traffic to flow across the connection (see the next section).  

ROUTING TO THE DRG
    As part of configuring the VCNs, each administrator must update the [VCN's routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) to enable traffic to flow between the VCNs. For each subnet that needs to communicate with the other VCN, you update the subnet's route table. The route rule specifies the destination traffic's CIDR and your DRG as the target. Your DRG routes traffic that matches that rule to the other DRG, which in turn routes the traffic to the next hop in the other VCN.     In the following diagram, VCN-1 and VCN-2 are peered. Traffic from an instance in Subnet A (10.0.0.15) that is destined for an instance in VCN-2 (192.168.0.15) is routed to DRG-1 based on the rule in Subnet A's route table. From there the traffic is routed through the RPCs to DRG-2, and then from there, on to the destination in Subnet X.     
[![This image shows the route tables and path of traffic routed from one DRG to the other.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_layout.svg)
Callout 3: Subnet A Route Table Destination CIDR | Route Target  
---|---  
0.0.0.0/0 | Internet Gateway  
192.168.0.0/16 | DRG-1  
Callout 4: Subnet X Route Table Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | DRG-2       
**Note**
As mentioned earlier, a given VCN can use the connected RPCs to reach only VNICs in the other VCN, and not destinations outside of the VCNs (such as the internet or your on-premises network). For example, in the preceding diagram, VCN-2 cannot use the internet gateway attached to VCN-1. 

SECURITY RULES
    Each subnet in a VCN has one or more [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) that control traffic in and out of the subnet's VNICs at the packet level. You can use security lists to control the type of traffic allowed with the other VCN. As part of configuring the VCNs, each administrator must determine which subnets in their own VCN need to communicate with VNICs in the other VCN and update their subnet's security lists accordingly.      If you use [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) (NSGs) to implement security rules, notice that you have the option to write security rules for an NSG that specify _another_ NSG as the source or destination of traffic. However, the two NSGs _must belong to the same VCN_.
## Important Implications of Peering 🔗 
If you haven't yet, read [Important Implications of Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Importan2) to understand important access control, security, and performance implications for peered VCNs.
## Setting Up a Remote Peering 🔗 
This section covers the general process for setting up a peering between two VCNs in different regions.
**Important**
The following procedure assumes that:
  * Your tenancy is subscribed to the other VCN's region. If it's not, see [Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm). 
  * You already have a DRG attached to your VCN. If you don't, see [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs).


  1. **Create the RPCs:** Each VCN administrator creates an RPC for their own VCN's DRG. 
  2. **Share information:** The administrators share the basic required information. 
  3. **Set up the required IAM policies for the connection:** The administrators set up IAM policies to enable the connection to be established. 
  4. **Establish the connection:** The _requestor_ connects the two RPCs (see [Important Remote Peering Concepts](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Importan) for the definition of the _requestor_ and _acceptor_).
  5. **Update route tables:** Each administrator updates their VCN's route tables to enable traffic between the peered VCNs as desired.
  6. **Update security rules:** Each administrator updates their VCN's security rules to enable traffic between the peered VCNs as desired.


If desired, the administrators can perform tasks E and F _before_ establishing the connection. Each administrator needs to know the CIDR block or specific subnets from the other's VCN and share that in task B.
[Task A: Create the RPCs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
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
  4. Under **Resources** , click **Remote Peering Connections**.
  5. Click **Create Remote Peering Connection**.
  6. Enter the following:
     * **Name:** A friendly name for the RPC. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **Create in compartment** : The compartment where you want to create the RPC, if different from the compartment you're currently working in. 
  7. Click **Create Remote Peering Connection**.
The RPC is then created and displayed on the **Remote Peering Connections** page in the compartment you chose. 
  8. If you're the acceptor, record the RPC's region and OCID to later give to the requestor. 


[Task B: Share information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
  * If you're the acceptor, give this information to the requestor (for example, by email or other out-of-band method):
    * The region your VCN is in (the requestor's tenancy must be subscribed to this region). 
    * Your RPC's OCID. 
    * The CIDR blocks for subnets in your VCN that should be available to the other VCN. The requestor needs this information when setting up routing for the requestor VCN.
  * If you're the requestor, give this information to the acceptor:
    * The region your VCN is in (the acceptor's tenancy must be subscribed to this region).
    * The name of the IAM group that should be granted permission to create a connection in the acceptor's compartment (in the example in the next task, the group is RequestorGrp). 
    * The CIDR blocks for subnets in your VCN that should be available to the other VCN. The acceptor needs this information when setting up routing for the acceptor VCN.


[Task C: Set up the IAM policies ](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
When both VCNs are in the same tenancy but different regions, use the policies provided in [Remote Peering with a Legacy DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__remote-peer-policy). 
If both VCNs are in different tenancies but the same region, use the policies provided in [Attaching to VCNs in Other Tenancies](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__xtenancy-VCN).
[Task D: Establish the connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
The requestor must perform this task.
Prerequisite: The requestor must have:
  * The region the acceptor's VCN is in (the requestor's tenancy must be subscribed to the region).
  * The OCID of the acceptor's RPC.


  1. In the Console, view the details for the requestor RPC that you want to connect to the acceptor RPC.
  2. Click **Establish Connection**.
  3. Enter the following: 
     * **Region:** The region that contains the acceptor's VCN. The drop-down list includes only those regions that both support remote VCN peering and your tenancy is subscribed to.
     * **Remote Peering Connection OCID:** The OCID of the acceptor's RPC. 
  4. Click **Establish Connection**.


The connection is established and the RPC's state changes to PEERED.
[Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
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
[Task F: Configure the security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
As mentioned earlier, each administrator can do this task before or after the connection is established. 
Prerequisite: Each administrator must have the CIDR block or specific subnets for the other VCN. In general, you should use the same CIDR block you used in the route table rule in [Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Step4). 
What rules should you add? 
  * Ingress rules for the types of traffic you want to allow from the other VCN, specifically from the VCN's CIDR or specific subnets.
  * Egress rule to allow outgoing traffic from your VCN to the other VCN. If the subnet already has a broad egress rule for all types of protocols to all destinations (0.0.0.0/0), then you don't need to add a special one for the other VCN.


**Note** The following procedure uses security lists, but you could instead implement the security rules in a [network security group](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) and then create all of the subnet's resources in that NSG. 
For your own VCN:
  1. Determine which subnets in your VCN need to communicate with the other VCN.
  2. Update the security list for each of those subnets to include rules to allow the desired egress or ingress traffic specifically with the CIDR block or subnet of the other VCN: 
    1. In the Console, while viewing the VCN you're interested in, click **Security Lists**. 
    2. Click the security list you're interested in. 
    3. Under **Resources** , click either **Ingress Rules** or **Egress Rules** depending on the type of rule you want to work with. 
    4. If you want to add a new rule, click **Add Ingress Rule** (or **Add Egress Rule**).
    5. If you want to delete an existing rule, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Remove**.
    6. If you wanted to edit an existing rule, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.


For more information about security rules, see [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules).
[Example](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
Let's say you want to add a stateful rule that enables ingress HTTPS (port 443) traffic from the other VCN's CIDR. Here are the basic steps you take when adding a rule: 
  1. In the **Allow Rules for Ingress** section, click **+Add Rule**.
  2. Leave the **Stateless** checkbox unselected.
  3. **Source Type:** Leave as CIDR.
  4. **Source CIDR:** Enter the same CIDR block that the route rules use (see [Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Step4)).
  5. **IP Protocol:** Leave as TCP. 
  6. **Source Port Range:** Leave as All.
  7. **Destination Port Range** : Enter 443.
  8. **Description:** An optional description of the rule.


## Using the Console 🔗 
[To create a remote peering connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
See the instructions in [Task A: Create the RPCs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Step).
[To delete a remote peering connection](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm)
Deleting an RPC terminates the peering. The RPC at the other side of the peering changes to the REVOKED state.
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Click the DRG you're interested in. 
  3. Under **Resources** , click **Remote Peering Connections**.
  4. Click the RPC you're interested in. 
  5. Click **Terminate**.
  6. Confirm when prompted.


**Note**
After deleting an RPC (and thus terminating a peering), it's recommended you review your route tables and security rules to remove any rules that enabled traffic with the other VCN. 
Was this article helpful?
YesNo

