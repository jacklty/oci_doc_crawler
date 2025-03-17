Updated 2025-02-12
# Access Control
This topic gives basic information about using **compartments** and IAM **policies** to control access to your cloud network. 
## Compartments and Your Cloud Network 🔗 
Anytime you create a cloud resource such as a Virtual Cloud Network (VCN) or compute instance, you must specify which IAM _compartment_ you want the resource in. A compartment is a collection of related resources that can only be accessed by certain groups that have been given permission by an administrator in your organization. The administrator creates compartments and corresponding IAM policies to control which users in your organization access which compartments. Ultimately, the goal is to ensure that each person can only access the resources they need. 
If your company is starting to try out Oracle Cloud Infrastructure, only a few people need to create and manage the VCN and its components, launch instances into the VCN, and attach block storage volumes to those instances. Those few people need access to _all_ these resources, so all those resources could be in the same compartment. 
In an enterprise production environment with a VCN, your company can use multiple compartments to more easily control access to certain types of resources. For example, your administrator could create Compartment_A for your VCN and other networking components. The administrator could then create Compartment_B for all the compute instances and block storage volumes that the HR organization uses, and Compartment_C for all the instances and block storage volumes that the Marketing organization uses. The administrator would then create IAM policies that give users only the level of access they need in each compartment. For example, the HR instance administrator is not entitled to modify the existing cloud network. So they would have full permissions for Compartment_B, but limited access to Compartment_A (just what's required to launch instances into the network). If they tried to modify other resources in Compartment_A, the request would be denied. 
Network resources such as VCNs, subnets, route tables, security lists, service gateways, NAT gateways, VPN connections, and FastConnect connections can be [moved from one compartment to another](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#Working). When you move a resource to a new compartment, inherent policies apply immediately. 
For more information about compartments and how to control access to your cloud resources, see [Learn Best Practices for Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm) and [Overview of Identity and Access Management](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm) . 
## IAM Policies for Networking 🔗 
The most straightforward approach to granting access to Networking is the policy listed in [Let network admins manage a cloud network](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#network-admins-manage-cloud-network). It covers the cloud network and all the other Networking components (subnets, security lists, route tables, gateways, and so on). To also give network admins the ability to create instances (to test network connectivity), see [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances). 
If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). 
For reference material for writing more detailed policies for Networking, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm). 
### Individual Resource-Types
You can write policies that focus on individual resource-types (for example, security lists only) instead of the broader `virtual-network-family`. The `instance-family` resource-type also includes several permissions for VNICs, which reside in a subnet but attach to an instance. For more information, see [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm#Core) and [Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs).
A resource-type called `local-peering-gateways` is included within `virtual-network-family` and includes two other resource-types related to local VCN peering (within region):
  * `local-peering-from`
  * `local-peering-to`


The `local-peering-gateways` resource-type covers all permissions related to local peering gateways (LPGs). The `local-peering-from` and `local-peering-to` resource-types are for granting permission to _connect_ two LPGs and define a peering relationship within a single region. For more information, see [Local Peering using an LPG (VCNs in the Same Tenancy)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG) or [Local Peering using an LPG (VCNs in Different Tenancies)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__local-LPG-xten).
Similarly, a resource-type called `remote-peering-connections` is included within `virtual-network-family` and includes two other resource-types related to remote VCN peering (across regions):
  * `remote-peering-from`
  * `remote-peering-to`


The `remote-peering-connections` resource-type covers all permissions related to remote peering connections (RPCs). The `remote-peering-from` and `remote-peering-to` resource-types are for granting permission to _connect_ two RPCs and define a peering relationship across regions. For more information, see [Remote Peering with a Legacy DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__remote-peer-policy) and [Remote Peering with an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m__IAM_cross-tenancy).
### Nuances of Different Verbs
You can write policies that limit the level of access by using a different policy verb (`manage` instead of `use`, and so on). If you do, here are some nuances to understand about the policy verbs for Networking.
Be aware that the `inspect` verb not only returns general information about the cloud network's components (for example, the name and OCID of a security list, or of a route table). It also includes the contents of the component (for example, the actual rules in the security list, the routes in the route table, and so on). 
Also, the following types of abilities are available only with the `manage` verb, not the `use` verb:
  * Update (enable/disable) `internet-gateways`
  * Update `security-lists`
  * Update `route-tables`
  * Update `dhcp-options`
  * Attach a Dynamic Routing Gateway (DRG) to a Virtual Cloud Network (VCN)
  * Create an IPSec connection between a DRG and customer-premises equipment (CPE)
  * Peer VCNs


**Important** Each VCN has various components that directly affect the behavior of the network (route tables, security lists, DHCP options, Internet Gateway, and so on). When you create one of these components, you establish a relationship between that component and the VCN, which means you must be allowed in a policy to both create the component and manage the VCN itself. However, the ability to _update_ that component (to change the route rules, security list rules, and so on) **doesn't** require permission to manage the VCN itself, even though changing that component can directly affect the behavior of the network. This discrepancy is designed to give you flexibility in granting least privilege to users, and not require you to grant excessive access to the VCN so the user can manage other components of the network. Be aware that by giving someone the ability to update a particular type of component, you're implicitly trusting them with controlling the network's behavior.
For more information about policy verbs, see [Policy Basics](https://docs.oracle.com/iaas/Content/Identity/Concepts/policies.htm#Policy). 
### Peering Policies
For policies used in connecting a DRG to VCNs and DRGs in other regions and tenancies, see [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways.").
Was this article helpful?
YesNo

