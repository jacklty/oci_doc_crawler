Updated 2025-01-15
# Local VCN Peering Through an Upgraded DRG
This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs. 
## Overview
Instead of using [local peering connections](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region), you can establish private network communications between two or more virtual cloud networks (VCNs) in the same region by attaching them to a common **dynamic routing gateway** (DRG) and making appropriate adjustments to VCN and DRG route tables.
This scenario is only available to an upgraded [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions).
If you are using the legacy DRG, you can peer two VCNs in the same region using Local Peering Gateways (LPG) as described in the scenario [Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region). Peering two VCNs in the same region through a DRG gives you more flexibility in your routing and simplified management but comes at the cost of microseconds increase in latency due to routing traffic through a virtual router, the DRG.
This sample scenario peers two VCNs. Before you attempt to implement this scenario, be sure that: 
  * VCN-A is not attached to a DRG
  * VCN-B is not attached to a DRG
  * VCN-A and VCN-B have non-overlapping CIDRs


Peering VCNs in different tenancies requires more IAM policies for cross-tenancy authorization. See [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways.") for details on the permissions needed. When you attach a VCN in a different region to a DRG, use the steps in [Attaching a DRG to a VCN in a Different Tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm#drg-create-xten-attachment "Learn to attach a Dynamic Routing Gateway \(DRG\) to a VCN in another tenancy ."). Most of the steps in this scenario assume the DRG and both VCNs are in the same tenancy.
**Steps**
Here's the general process for setting up a peering between two VCNs in the same region using a DRG:
  1. **Create the DRG** : See [Task A: Create a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_a_dita).
  2. **Attach VCN A to the DRG** : See [Task B: Attach VCN-A to the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_b_dita).
  3. **Attach VCN B to the DRG** : See [Task C: Attach VCN-B to the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_c_dita).
  4. **Configure route tables in VCN A to send traffic destined to VCN B's CIDR to the DRG** : See [Task D: Configure route tables in VCN-A to send traffic destined to VCN-B's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_d_dita).
  5. **Configure route tables in VCN B to send traffic destined to VCN A's CIDR to the DRG** : See [Task E: Configure route tables in VCN-B to send traffic destined to VCN-A's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_e_dita).
  6. **Update security rules** : Update each VCN's security rules to enable traffic between the peered VCNs as intended. See [Task F: Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenario_dtask_f_dita).


This page summarizes some access control, security, and performance implications for peered VCNs. You can control access and traffic between two peered VCNs by using IAM policies, route tables in each VCN, route tables in the DRG, and security lists in each VCN. 
## Summary of Networking components for peering through a DRG
At a high level, the Networking service components required for a local peering through a DRG include:
  * Two VCNs with non-overlapping CIDRs, in the same region
  * A single _Dynamic Routing Gateway (DRG)_ attached to each peer VCN. 
  * Supporting route rules to enable traffic to flow over the connection, and only to and from select subnets in the respective VCNs (if wanted).
  * Supporting security rules to control the types of traffic allowed to and from the instances in the subnets that need to communicate with the other VCN.


The following diagram illustrates the components.
[![This image shows the basic layout of two VCNs that are locally peered, each with a local peering gateway.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_basic_DRG.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_basic_DRG.svg)
**Note**
A given VCN can reach these resources:
  * VNICs in the other VCN
  * An on-premises network attached to the other VCN, if an advanced routing scenario called [transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region) has been set up for the VCNs


Two VCNs interconnected with a DRG cannot reach other cloud gateways (such as an internet Gateway or NAT Gateway) except for transit routing via an LPG. For example, if VCN-1 in the preceding diagram were to have an internet gateway, the instances in VCN-2 could not use it to send traffic to endpoints on the internet. However, VCN-2 could _receive_ traffic from the internet by way of VCN-1. For more information, see [Important Implications of VCN Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Importan2).
## Important Local Peering Concepts 🔗 
The following concepts help you understand the basics of VCN peering using a DRG and how to establish a local peering. 

PEERING
    A _peering_ is a relationship between two VCNs that both connect to the same DRG and can mutually route traffic. The _local_ part of _local peering_ indicates that the VCNs are in the same region. A given DRG can have a maximum of 300 local DRG attachments at a time.     
**Caution** Peer VCNs must not have overlapping CIDRs.  

ADMINISTRATORS
    In general, VCN peering can occur only if all involved VCN administrators and DRG administrators agree to it. Depending on the situation, a single administrator might be responsible for all involved DRGs, VCNs, and the related policies.      For more information about the required policies and VCN configuration, see [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways."). 

ROUTING TO THE DRG
    As part of configuring the VCNs, each administrator must update the [VCN's routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) to enable traffic to flow between the VCNs. In practice, this looks just like routing you set up for any gateway (such as an [internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway) or [dynamic routing gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs)). For each subnet that needs to communicate with the other VCN, you update the subnet's route table. The route rule specifies the destination traffic's CIDR and your DRG as the target. Your VCN routes traffic that matches that rule to the DRG, which in turn routes the traffic to the next hop in the other VCN.     In the following diagram, VCN-1 and VCN-2 are peered. Traffic from an instance in Subnet A (10.0.0.15) destined for an instance in VCN-2 (192.168.0.15) is routed to the DRG based on the rule in Subnet A's route table. From there the traffic is routed to VCN-2, and then from there, on to its destination in Subnet X. The DRG in this scenario uses the auto-generated route table.     
[![This image shows the route tables and path of traffic routed from one VCN to the other.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_layout_DRG.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_local_peering_layout_DRG.svg)
Callout 1: Subnet A Route Table Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
192.168.0.0/16 | DRG  
0.0.0.0/0 | Internet Gateway  
Callout 2: Subnet X Route Table Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
10.0.0.0/16 | DRG 

SECURITY RULES
    Each subnet in a VCN has one or more [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) that control traffic in and out of the subnet's VNICs at the packet level. You can use security lists to control the type of traffic allowed with the other VCN. As part of configuring the VCNs, each administrator must determine which subnets in their own VCN need to communicate with VNICs in the other VCN and update their subnet's security lists accordingly.      If you use [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) (NSGs) to implement security rules, notice that you can write security rules for an NSG that specify _another_ NSG as the source or destination of traffic. However, the two NSGs _must belong to the same VCN_.  
## Setting up this scenario in the console
[Task A: Create a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm)
A DRG created before May 2021 is not able to perform routing between on-premises networks and multiple VCNs, or provide local peering between VCNs. If you require that functionality and you see an **Upgrade DRG** button, click it. 
**Note** Clicking the **Upgrade DRG** button also resets all existing BGP sessions and temporarily interrupt traffic from the on-premises network while the DRG upgrades. Be aware you can't roll back the upgrade.
While working in the same region as the VCNs you want to peer, perform the following steps: 
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Under **List Scope** , select a compartment that you have permission to work in.The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). 
  3. Click **Create Dynamic Routing Gateway**.
  4. Enter the following items:
     * **Name:** A descriptive name for the DRG. It doesn't have to be unique, and it cannot be changed later in the Console (but you can change it with the API). Avoid entering confidential information.
     * **Create in Compartment:** The compartment where you want to create the DRG, which could be different from the compartment you're currently working in. 
     * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  5. Click **Create Dynamic Routing Gateway**.


The new DRG is created and then displayed on the **Dynamic Routing Gateways** page of the compartment you chose. The DRG is in the "Provisioning" state for a short period. You can connect it to other parts of your network only after provisioning is complete. 
Provisioning includes creating two route tables: one route table for connected VCNs and one for other resources such as virtual circuits and IPSec tunnels. The default route tables can't be deleted, but they can be edited. If left unmodified, the default routing policies in a DRG allow traffic to be routed between all VCNs attached to it.
**Note** The default upgraded DRG routing tables implement the same routing behavior as legacy DRGs for backward compatibility.
[Task B: Attach VCN-A to the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm)
**Note** An upgraded DRG can be attached to many VCNs, but a VCN can be attached to only one DRG at a time. The attachment is automatically created in the compartment that holds the VCN. A VCN does not need to be in the same compartment or tenancy as the upgraded DRG. 
You can eliminate local peering connections from your overall network design if you connect several VPNs in the same region to the same DRG and configure the DRG routing tables appropriately. 
Peering VCNs in different tenancies requires more IAM policies for cross-tenancy authorization. See [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways.") for details on the permissions needed. When you attach a VCN in a different region to a DRG, use the steps in [Attaching a DRG to a VCN in a Different Tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm#drg-create-xten-attachment "Learn to attach a Dynamic Routing Gateway \(DRG\) to a VCN in another tenancy ."). 
The following instructions have you navigate to the upgraded DRG and then choose which VCN to attach. You could instead navigate to the VCN and then choose which DRG to attach. 
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Click the upgraded DRG you want to attach to VCN A.
  3. Under **Resources** , click **Virtual cloud network attachments**. 
  4. Click **Create VCN attachment**.
     * (Optional) Give the attachment point a friendly name. If you don't specify a name, one is created for you.
     * Select VCN A from the list. You can also click **Change compartment** and choose a different compartment if VCN is not in the current compartment, then select VCN A from the list.
  5. (Optional) If you're setting up an [advanced scenario for transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region), you can associate a VCN route table with the DRG attachment (you can do this later): 
    1. Click **Show Advanced Options**.
    2. Click the **VCN route table** tab.
    3. Select the route table that you want to associate with the VCN attachment on the DRG. If you select **None** , the default VCN route table is used. 
  6. Click **Create VCN attachment**.


The attachment is in the "Attaching" state for a short period. 
When the attachment is ready, create a route rule that directs subnet traffic to this DRG. See [To route a subnet's traffic to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm#add_route_rule).
[Task C: Attach VCN-B to the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm)
**Note** A DRG can be attached to many VCNs, but VCN can be attached to only one DRG at a time. The attachment is automatically created in the compartment that holds the VCN. A VCN does not need to be in the same compartment as the DRG. 
You can eliminate local peering connections from your overall network design if you connect several VPNs in the same region to the same DRG and configure the DRG routing tables appropriately. 
Peering VCNs in different tenancies requires more IAM policies for cross-tenancy authorization. See [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways.") for details on the permissions needed. When you attach a VCN in a different region to a DRG, use the steps in [Attaching a DRG to a VCN in a Different Tenancy](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-create-xten-attachment.htm#drg-create-xten-attachment "Learn to attach a Dynamic Routing Gateway \(DRG\) to a VCN in another tenancy ."). 
The following instructions have you navigate to the DRG and then choose which VCN to attach. You could instead navigate to the VCN and then choose which DRG to attach. 
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Click the DRG you want to attach to VCN B.
  3. Under **Resources** , click **Virtual cloud network attachments**. 
  4. Click **Create VCN attachment**.
     * (Optional) Give the attachment point a friendly name. If you don't specify a name, one is created for you.
     * Select VCN B from the list. You can also click **Change compartment** and choose the compartment that contains VCN B, then select VCN B from the list.
  5. (Optional) If you're setting up an [advanced scenario for transit routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region), you can associate a VCN route table with the DRG attachment (you can do this later): 
    1. Click **Show Advanced Options**.
    2. Click the **VCN route table** tab.
    3. Select the route table that you want to associate with the VCN attachment on the DRG. If you select **None** , the default VCN route table is used. 
  6. Click **Create VCN attachment**.


The attachment is in the "Attaching" state for a short period. 
When the attachment is ready, create a route rule that directs subnet traffic to this DRG. See [To route a subnet's traffic to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm#add_route_rule).
[Task D: Configure route tables in VCN-A to send traffic destined to VCN-B's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm)
As mentioned earlier, each administrator can do this task before or after the VCN is attached to the DRG. 
Prerequisite: Each administrator must have the CIDR block or specific subnets for the other VCN. 
For VCN A:
  1. Determine which subnets in VCN-A need to communicate with the other VCN.
  2. Update the route table for each of those subnets to include a new rule that directs traffic destined for the other VCN's CIDR to your DRG: 
    1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the VCN you're interested in, VCN-A. 
    3. Under **Resources** , click **Route Tables**. 
    4. Click the route table you're interested in.
    5. Click **Add Route Rule** and enter the following:
       * **Target Type:** Dynamic Routing Gateway.
       * **Destination CIDR Block:** VCN-B's CIDR block. If you want, you can specify a subnet or particular subset of VCN-B's CIDR.
       * **Target Compartment:** The compartment where the other VCN is located, if not the current compartment.
       * **Target:** The DRG.
       * **Description:** An optional description of the rule.
    6. Click **Add Route Rule**.


Any subnet traffic with a destination that matches the rule is routed to your DRG. For more information about setting up route rules, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
If in the future you no longer need the peering and want to end the peering relationship, first delete all the route rules in your VCN that specify the other as the target.
**Tip** Without the required routing, traffic doesn't flow between the peered VCNs. If a situation occurs where you need to temporarily stop the peering relationship, remove the route rules that enable traffic.
[Task E: Configure route tables in VCN-B to send traffic destined to VCN-A's CIDR to the DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm)
As mentioned earlier, each administrator can do this task before or after the VCN is attached to the DRG. 
Prerequisite: Each administrator must have the CIDR block or specific subnets for the other VCN. 
For VCN-B:
  1. Determine which subnets in VCN B need to communicate with the other VCN.
  2. Update the route table for each of those subnets to include a new rule that directs traffic destined for the other VCN's CIDR to your DRG: 
    1. Open the **navigation menu** , select **Networking** , and then select **Virtual cloud networks**.
    2. Click the VCN you're interested in, VCN-B. 
    3. Under **Resources** , click **Route Tables**. 
    4. Click the route table you're interested in.
    5. Click **Add Route Rule** and enter the following:
       * **Target Type:** Dynamic Routing Gateway.
       * **Destination CIDR Block:** VCN-A's CIDR block. If you want, you can specify a subnet or particular subset of VCN A's CIDR block.
       * **Target Compartment:** The compartment where the other VCN is located, if not in the current compartment.
       * **Target:** The DRG.
       * **Description:** An optional description of the rule.
    6. Click **Add Route Rule**.


Any subnet traffic with a destination that matches the rule is routed to your DRG. For more information about setting up route rules, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
If later on you no longer need the peering and want to end the peering relationship, delete all the route rules in your VCN that specify the other VCN as the target.
**Tip** Without the required routing, traffic doesn't flow between the peered VCNs. If a situation occurs where you need to temporarily stop the peering, you can simply remove the route rules that enable traffic. 
[Task F: Update security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm)
As mentioned earlier, each administrator can do this task before or after the connection is established. 
Prerequisite: Each administrator must have the CIDR block or specific subnets for the other VCN. In general, use the same CIDR block you used in the route table rule in [Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Step4). 
What rules should you add? 
  * Ingress rules for the types of traffic you want to allow from the other VCN, specifically from the VCN's CIDR or specific subnets.
  * Egress rule to allow outgoing traffic from your VCN to the other VCN. If the subnet already has a broad egress rule for all types of protocols to all destinations (0.0.0.0/0), then you don't need to add a special one for the other VCN.


**Note** The following procedure uses security lists, but you could instead implement the security rules in a [network security group](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) and then create the subnet's resources in that NSG. 
For each VCN:
  1. Determine which subnets in your VCN need to communicate with the other VCN.
  2. Update the security list for each of those subnets to include rules to allow the intended egress or ingress traffic specifically with the CIDR block or subnet of the other VCN: 
    1. In the Console, while viewing the VCN you're interested in, click **Security Lists**. 
    2. Click the security list you're interested in. 
    3. Under **Resources** , click either **Ingress Rules** or **Egress Rules** depending on the type of rule you want to work with. 
    4. If you want to add a rule, click **Add Ingress Rule** (or **Add Egress Rule**).
**Example**
Let's say you want to add a stateful rule that enables ingress HTTPS (port 443) traffic from the other VCN's CIDR. Here are the basic steps you take when adding a rule: 
      1. Leave the **Stateless** checkbox unselected.
      2. **Source Type:** Leave as CIDR.
      3. **Source CIDR:** Enter the same CIDR block that the route rules use (see [Task E: Configure the route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Step4)).
      4. **IP Protocol:** Leave as TCP. 
      5. **Source Port Range:** Leave as All.
      6. **Destination Port Range** : Enter 443.
      7. **Description:** An optional description of the rule.
    5. If you want to delete an existing rule, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Remove**.
    6. If you wanted to edit an existing rule, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Edit**.


For more information about security rules, see [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules).
Was this article helpful?
YesNo

