Updated 2025-02-12
# Networking Scenarios
## Basic Scenarios
All except the first of these basic routing scenarios send traffic from a subnet in the VCN to the DRG. To accomplish this, [set up a rule in the subnet's route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables_topic-working.htm#add_route_rule). The rule's destination CIDR is the CIDR of the network you want to reach through the DRG, and the rule's target is the DRG. For more information, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2). 
  * [Scenario A: Public Subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioa.htm#Scenario_A_Public_Subnet) (no DRG required)
  * [Scenario B: Private Subnet with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenariob.htm#Scenario_B_Private_Subnet_with_a_VPN)
  * [Scenario C: Public and Private Subnets with a VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarioc.htm#Scenario_C_Public_and_Private_Subnets_with_a_VPN)


## Peering
These scenarios all allow traffic to flow from one VCN to another. 
  * [Local VCN Peering Through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_d.htm#scenariod "This scenario describes using a mutual connection to an upgraded DRG to enable traffic between two or more VCNs.") (Upgraded DRG)
  * [Remote VCN Peering through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e "This topic is about remote VCN peering.") (Upgraded DRG)
  * [Local VCN Peering using Local Peering Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region) (Legacy DRG)
  * [Remote VCN Peering using a Legacy DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/remoteVCNpeering.htm#Remote_VCN_Peering_Across_Regions) (Legacy DRG)


## Advanced Scenarios Using a Single DRG
**VCN Ingress Routing** : Some advanced scenarios require ingress routing of traffic entering the VCN from a DRG through the VCN attachment. To accomplish this, you must associate a VCN route table (this is a route table created inside a VCN) with the VCN attachment. After a VCN route table is associated with a VCN attachment, there must always be a VCN route table associated with that attachment (you can't update the field in the corresponding data object to "Null"). Removing the VCN ingress routing functionality from a VCN attachment can only be done by emptying the associated VCN route table or updating the attachment to use an empty VCN route table.
  * [Remote on-ramp](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_f.htm#scenario_f "The remote on-ramp scenario shows how to let your on-premises network access two or more virtual cloud networks \(VCNs\) through a single FastConnect virtual circuit or Site-to-Site VPN IPSec connection, even if the VCNs are in different regions or tenancies.") (Upgraded DRG)
  * [Routing traffic through a central network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#scenario_g) (Upgraded DRG)
  * [Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#Transit_Routing_Private_Access_to_Oracle_Services)
  * [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region)


## Advanced Scenario with Several DRGs and Several VCNs
The transit routing scenario illustrates the use of several DRGs and VCNs. In this case, each VCN has its own **dynamic routing gateway (DRG)** and its own FastConnect **private virtual circuit**. Contrast this with [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region), which has a single DRG with either Site-to-Site VPN or a single FastConnect private virtual circuit.
Here are some restrictions for using this scenario with several DRGs:
  * The scenario works only with FastConnect through a [third-party provider](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectthirdpartyprovider.htm#FastConnect_With_a_ThirdParty_Provider "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to a third-party network provider of their choice, and not an Oracle Partner.") or through [colocation with Oracle](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectcolocate.htm#FastConnect_Colocation_with_Oracle "This topic is for customers who are colocated with Oracle in a FastConnect location."). The scenario isn't supported for FastConnect through an [Oracle partner](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm#FastConnect_With_an_Oracle_Partner "This topic is for customers who want to use Oracle Cloud Infrastructure FastConnect by connecting to an Oracle Partner.").
  * The scenario is supported only for VCNs in the same region and same tenancy. This is because all the virtual circuits use a single cross-connect, a regional resource.


See [FastConnect with Multiple DRGs and VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectmultipledrgs.htm#FastConnect_with_Multiple_DRGs_and_VCNs).
Was this article helpful?
YesNo

