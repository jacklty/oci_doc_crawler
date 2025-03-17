Updated 2025-02-06
# Working with VCN Route Tables and Route Rules
Learn about VCN route tables and route rules.
Each VCN has a default route table. You can also create custom route tables. You can add, remove and edit route rules in any route table. By default, each VCN automatically routes traffic between sources and destinations within the VCN. You don’t need to define explicit route rules for this routing behavior inside a VCN, but you can change it by defining your own route rules for traffic between subnets in a VCN. For example, you can redirect traffic between two subnets in a VCN to flow through a firewall by defining an [intra-VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__intra_vcn) route rule defining the firewall private IP address as the next-hop for each other’s IP prefixes.
Each subnet in a VCN uses a single route table. When you create a subnet, you can specify which route table to use. If you don’t specify any, the default route table for the VCN will be used. You can [change which route table the subnet uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm#subnet-change-routetable "Change which virtial cloud network \(VCN\) route table a subnet uses.") at any time. When you have a public subnet and a private subnet in your VCN (for an example of this usage, see [Scenario C: Public and Private Subnets with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm#Scenario_C_Public_and_Private_Subnets_with_a_VPN)), you'll need to use different route tables for the subnets because the route rules for the subnets need to be different.
You can optionally assign a descriptive name to a custom route table during creation. It doesn't have to be unique, and you can change it later. Oracle automatically assigns the route table a unique identifier called an Oracle Cloud ID (OCID). For more information on OCIDs, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
A route rule specifies a destination CIDR block and the target (the next hop) for any traffic that matches that CIDR. Here are the allowed types of targets for a route rule:
  * [Dynamic Routing Gateway (DRG)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs): For subnets that need private access to networks connected to your VCN (for example, your on-premises network connected with a [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") or [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure."), a[ peered VCN in the same region](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region), or a [peered VCN in another region](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions)).
  * [Internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway): For public subnets that need direct access to the internet.
  * [NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm#NAT_Gateway): For subnets with instances that do not have public IP addresses but need outbound access to the internet.
  * [Service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway): For subnets that need private access to Oracle services such as Object Storage.
  * [Local peering gateway (LPG):](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Access_to_Other_VCNs_Peering) For subnets that need private access to a peered VCN in the same region.
  * [Private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#Private_IP_Addresses): For subnets that need to route traffic to an instance in the VCN. For more information, see [Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route). Also see [Overview of Routing for a VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN).


**Note** You can't delete a particular resource when it is the target for a route rule. For example, you can't delete an internet gateway that has traffic routed to it. Delete all rules (in all route tables) with that internet gateway as the target before you try to delete the gateway or other resource.
When adding a route rule to a route table, you provide the destination CIDR block and target (plus the **compartment** where the target resides). Exception: if the target is a **service gateway** , instead of a destination CIDR block, you specify an Oracle-provided string that represents the public endpoints for the service of interest. That way you don't need to know all the service's CIDR blocks, which might change over time.
If you misconfigure a rule (for example, enter the wrong destination CIDR block), the network traffic you intended to route might be dropped (blackholed) or sent to an unintended target. 
You can [move route tables from one compartment to another](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm#move-routetable "Move a Virtual Cloud Network \(VCN\) route table to a different compartment."). Moving a route table doesn't affect its attachment to VCNs or subnets. When you move a route table to a new compartment, inherent policies apply immediately and affect access to the route table. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
You can't delete a VCN's default route table. To delete a custom route table, it must not be associated with a subnet or a gateway, such as DRG, LPG, IGW, NGW or SGW. See the [Learn routing in OCI Networking with examples (PDF)](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/learn-routing-in-oci-networking-with-examples.pdf) technical brief to learn more about VCN routing.
See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
The following management tasks can be performed with route tables: 
  * [Creating a VCN Route Table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-routetable.htm#create-routetable "Create a Virtual Cloud Network \(VCN\) route table in a specific VCN and compartment.")
  * [Listing VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/list-routetable.htm#list-routetable "List VCN route tables in a given VCN and compartment.")
  * [Getting a VCN Route Table's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/get-details-routetable.htm#get-details-routetable "Get details for a Virtual Cloud Network \(VCN\) route table.")
  * [Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.")
  * [Changing Which VCN Route Table a Subnet Uses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/subnet-change-routetable.htm#subnet-change-routetable "Change which virtial cloud network \(VCN\) route table a subnet uses.")
  * [Moving a VCN Route Table to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/move-routetable.htm#move-routetable "Move a Virtual Cloud Network \(VCN\) route table to a different compartment.")
  * [Tagging a VCN Route Table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/tagging-routetable.htm#tagging-routetable "Manage tags for a Virtual Cloud Network \(VCN\) route table.")
  * [Deleting a VCN Route Table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/delete-routetable.htm#delete-routetable "Delete a Virtual Cloud Network \(VCN\) route table.")


[To route a subnet's traffic to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm)
For each VCN subnet that must send traffic to a connected [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs), you must add a route rule to the VCN route table associated with that subnet. If all the subnets in the VCN use the default route table, you must add a rule to only that one table.
If all non-intra-VCN traffic that's not covered by another rule in the table must be routed to the DRG, add this new rule:
  * **Target Type:** Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself. 
  * **Destination CIDR Block** = 0.0.0.0/0. If you want to limit the rule to a specific network (for example, your on-premises network), then use that network's CIDR instead of 0.0.0.0/0.


For step-by-step instructions, see [Updating a VCN Route Table's Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.").
[To associate a VCN route table with an existing DRG attachment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm)
**Important** Perform this task only if you're setting up an advanced scenario for transit routing. See [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region) and [Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services).
A DRG attachment always has a route table associated with it, but you can associate a _different_ route table, edit the table's rules, or delete some or all rules. 
**Prerequisites:** the VCN that the DRG is already attached to must have a route table.
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Click the DRG that is attached to the VCN that has the route table you want to use with the attachment.
  3. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click either:
     * **Associate Route Table:** If the DRG attachment has no route table associated with it yet.
     * **Associate Different Route Table:** If you're changing which route table is associated with the DRG attachment.
  4. Select the route table.
  5. Click **Associate Route Table**.


The route table is now associated with the DRG attachment.
Was this article helpful?
YesNo

