Updated 2025-01-15
# Remote on-ramp
The _remote on-ramp_ scenario shows how to let your on-premises network access two or more virtual cloud networks (VCNs) through a single FastConnect virtual circuit or Site-to-Site VPN IPSec connection, even if the VCNs are in different regions or tenancies.
## Overview
In this scenario, connectivity is established between VCNs and the on-prem network, but not between VCNs. This choice of routing policy is implemented by configuring the **dynamic routing gateway** (DRG) routing tables, and otherwise this scenario resembles [remote peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e "This topic is about remote VCN peering.").
This scenario is only available to an upgraded [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions). 
## Summary of Networking components for single on-ramp
At a high level, the Networking service components required for single on-ramp include:
  * Two VCNs with non-overlapping CIDRs, in different regions. 
**Note**
No VCN CIDRs can overlap
The two VCNs in the peering relationship cannot have overlapping CIDRs. Also, if a particular VCN has multiple peering relationships, those other VCNs must not have overlapping CIDRs with each other. For example, if VCN-1 is peered with VCN-2 and also VCN-3, then VCN-2 and VCN-3 must not have overlapping CIDRs.
If you are configuring this scenario, you have to meet this requirement in the planning stage. Routing problems are likely when overlapping CIDRs occur, but the Console or API operations do not prevent you from creating a configuration that causes issues.
  * A Dynamic Routing Gateway (DRG) attached to each VCN in the peering relationship. Your VCN already has a DRG if you're using [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") or an [Oracle Cloud Infrastructure FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") private virtual circuit. 
  * Two custom DRG route tables: one routing traffic to the VCNs, and one routing traffic to the on-premises network. The default DRG route tables (one for local VCN attachments and one for all other attachments) are not used after the configuration is complete.
  * A _remote peering connection (RPC)_ on each DRG in the peering relationship.
  * An established _remote peering connection_ between those two RPCs.
  * Supporting [route rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) to enable traffic to flow over the connection, and only to and from select subnets in the respective VCNs (if wanted).
  * Supporting [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) to control the types of traffic allowed to and from the instances in the subnets that need to communicate with the other VCN.


The following diagram illustrates the components. VCN-1 is optional if your primary intent is to access VCN-2. Supporting route tables and security rules are needed in each VCN to enable traffic.
[![This image shows the basic layout of two VCNs that are remotely peered, each with a remote peering connection on the DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_single_onramp_basic.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_single_onramp_basic.svg)
**Note** A given VCN can use the connected RPCs only to reach your on-premises network or VCNs connected to the DRG. For example, if VCN-1 in the preceding diagram were to have an internet gateway, the instances in VCN-2 could NOT use it to send traffic to endpoints on the internet. For more information, see [Important Implications of Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Importan2).
## Important implications of peering
If you haven't yet, read [Important Implications of Peering](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Importan2) to understand important access control, security, and performance implications for peered VCNs.
Peering VCNs in different tenancies has some permissions complications that need to be resolved in both tenancies. See [IAM Policies for Routing Between VCNs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-iam.htm#scenario_m "Learn about IAM policies used with peering and dynamic routing gateways.") for details on the permissions needed. 
## Important remote peering concepts
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
    As part of configuring the VCNs, each administrator must update the [VCN's routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) to enable traffic to flow between the VCNs. For each subnet that needs to communicate with the on-premises network, you update the subnet's route table. The route rule specifies the destination traffic's CIDR and your DRG as the target. Your DRG routes traffic that matches that rule to the other DRG, which in turn routes the traffic to the next hop in the other VCN. 

SECURITY RULES
    Each subnet in a VCN has one or more [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) that control traffic in and out of the subnet's VNICs at the packet level. You can use security lists to control the type of traffic allowed with the other VCN. As part of configuring the VCNs, each administrator must determine which subnets in their own VCN need to communicate with VNICs in the other VCN and update their subnet's security lists accordingly.      If you use [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) (NSGs) to implement security rules, notice that you can write security rules for an NSG that specify _another_ NSG as the source or destination of traffic. However, the two NSGs _must belong to the same VCN_.
## Setting up single on-ramp
Before you attempt to implement this scenario, be sure that: 
  1. VCN-1 is attached to DRG-1 in region 1 following the steps in [Attaching a VCN to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm#attach-vcn-drg "Attach a Virtual Cloud Network \(VCN\) to a Dynamic Routing Gateway \(DRG\)."). 
  2. VCN-2 is attached to DRG-2 in region 2 following the steps in [Attaching a VCN to a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/attach-vcn-drg.htm#attach-vcn-drg "Attach a Virtual Cloud Network \(VCN\) to a Dynamic Routing Gateway \(DRG\).").
  3. VCN-2 is peered to VCN-1 following the steps in [Remote VCN Peering through an Upgraded DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_e.htm#scenario_e "This topic is about remote VCN peering.")
  4. Both DRGs are otherwise unmodified.
  5. FastConnect virtual circuit 1 is in region 1, connected to DRG-1 following the appropriate method depending on the source of the virtual circuit (Oracle partner, Oracle colocation, third-party provider) as described in the documentation for [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.").


The following diagram shows the beginning state before implementing this scenario. VCN-1 and VCN-2 are peered. Traffic from an instance in Subnet A (10.0.0.15) destined for an instance in VCN-2 (192.168.0.15) is routed to DRG-1 based on the rule in Subnet A's route table. From there the traffic is routed through the RPCs to DRG-2, and then from there, on to the destination in Subnet X. The on-premises network can address resources in VCN-1 but not in VCN-2. 
[![This image shows the route tables and path of traffic routed from one DRG to the other.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_remote_peering_layout.svg)
**Callout 1: Subnet A Route Table** Destination CIDR | Route Target  
---|---  
0.0.0.0/0 | Internet Gateway  
192.168.0.0/16 | DRG-1  
172.16.0.0/12 | DRG-1  
**Callout 2: Subnet X Route Table** Destination CIDR | Route Target  
---|---  
10.0.0.0/16 | DRG-2  
The implemented onramp scenario described in the next diagram does not allow the VCNs to route traffic to each other. VCN-1 and VCN-2 are peered. Traffic from an on-premises resource in your network (172.16.0.10) destined for an instance in VCN-2 (192.168.0.15) is routed to DRG-1 based on the rule in the IPSEC_TUNNEL attachment route table To-on-premises. From there the traffic is routed through the RPC attachment to DRG-2, and then to the destination in Subnet X.
[![This image shows the route tables and path of traffic routed from one DRG to the other.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_single_onramp_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_single_onramp_layout.svg)
Callout 1: DRG-1 Route Table RT-OnPrem  Destination CIDR | Route Target | Type  
---|---|---  
10.0.0.0/16 | VCN Attachment | Dynamic  
192.168.0.0/16 | RPC Attachment | Dynamic  
Callout 2: DRG-1 Route Table RT-VCN  Destination CIDR | Route Target | Type  
---|---|---  
172.16.0.0/12 | Virtual Circuit Attachment | Dynamic  
Callout 3: DRG-1 Route Table RT-RPC  Destination CIDR | Route Target | Type  
---|---|---  
172.16.0.0/12 | Virtual Circuit Attachment | Dynamic  
Callout 4: Subnet X Route Table  Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG-2  
**Note**
As mentioned earlier, a given VCN can use the connected DRG's RPC attachment to reach only VNICs in your on-premises network, and not destinations on the internet. For example, in the preceding diagram, VCN-2 cannot use the internet gateway attached to VCN-1.
**Steps**
These steps are all performed on DRG-1:
[Step 1: Create new DRG route tables ](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_f.htm)
This table doesn't need any static routes.
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Click the DRG you're interested in, DRG-1.
  3. Under **Resources** , click **DRG Route Tables**. 
  4. Click **Create DRG Route Table**. 
  5. Enter the following:
     * **Name:** Enter "RT-VCN" or choose some other descriptive name.
  6. Click **Create DRG Route Table**.


Repeat these steps to create two more empty route tables named "RT-OnPrem" and "RT-RPC" before you move to the next task.
[Step 2: Create an import route distribution for "RT-VCN"](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_f.htm)
Create an import route distribution for the DRG attachment used by VCN-1. The import route distribution will contain one statement, accepting routes from attachments of type virtual circuit.
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Click the DRG you're interested in, DRG-1.
  3. Under **Resources** , click **Import Route Distributions**. 
  4. Click **Create Import Route Distribution**. 
  5. Enter the following:
     * **Name:** Enter "Import-VCN" or choose some other descriptive name.
     * **Priority** : Enter "10" or choose some other priority number.
     * **Match Type:** Choose **Attachment Type**.
**Attachment Type:** Choose **Virtual Circuit**.
**Note** When you use the **Attachment Type** option, the import route distribution will include routes from all attachments to this DRG with the chosen type.
  6. Click **Create Import Route Distribution** when finished.
  7. Under **Resources** , click **DRG route tables**.
  8. Click the name of the route table you want to assign to the new import route distribution, "RT-VCN."
  9. Click **Edit**.
  10. Click **Enable Import Route Distribution** : This option allows you to assign an import route distribution to the route table so it dynamically learns new routes based on BGP advertisements.
     * Choose the import route distribution you created in earlier steps, named "Import-VCN"
  11. Click **Save Changes**.


[Step 3: Create an import route distribution for "RT-OnPrem"](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_f.htm)
Create an import route distribution for the DRG attachment used by the virtual circuit attachment. The import route distribution will contain two statements, one accepting routes from attachments of type VCN and another accepting routes from attachments of type RPC.
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Click the DRG you're interested in, DRG-1.
  3. Under **Resources** , click **Import Route Distributions**. 
  4. Click **Create Import Route Distribution**. 
  5. Enter the following:
     * **Name:** Enter "Import-OnPrem" or choose some other descriptive name.
     * **Priority** : Enter "10" or choose some other priority number.
     * **Match Type:** Choose **Attachment Type**.
**Attachment Type:** Choose **Virtual Cloud Network**.
  6. Click **+ Another Statement** to add another route distribution statement.
     * **Priority** : Enter "20" or choose some other priority number.
     * **Match Type:** Choose **Attachment Type**.
     * **Attachment Type:** Choose **Remote Peering Connection**.
**Note** When you use the **Attachment Type** option, the import route distribution will include routes from all attachments to this DRG with the RPC type. Any RPC connection to VCNs in other regions will be included.
  7. Click **Create Import Route Distribution** when finished.
  8. Under **Resources** , click **DRG route tables**.
  9. Click the name of the route table you want to assign to the new import route distribution, "RT-OnPrem."
  10. Click **Edit**.
  11. Click **Enable Import Route Distribution** : This option allows you to assign an import route distribution to the route table so it dynamically learns new routes based on BGP advertisements.
     * Choose the import route distribution you created in earlier steps, named "Import-OnPrem"
  12. Click **Save Changes**.


[Step 4: Create an import route distribution for "RT-RPC" ](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_f.htm)
Create an import route distribution for the DRG attachment used by the remote peering connection attachment. The import route distribution will contain one statement, accepting routes from attachments of type virtual circuit.
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Click the DRG you're interested in, DRG-1.
  3. Under **Resources** , click **Import Route Distributions**. 
  4. Click **Create Import Route Distribution**. 
  5. Enter the following:
     * **Name:** Enter "Import-RPC" or choose some other descriptive name.
     * **Priority** : Enter "10" or choose some other priority number.
     * **Match Type:** Choose **Attachment Type**.
**Attachment Type:** Choose **Virtual Circuit**.
**Note**
If you want inter-region VCNs to communicate with each other, import the RPC attachment into the import distribution used by RT-VCN, and VCN attachment into import distribution used by RT-RPC.
  6. Click **Create Import Route Distribution** when finished.
  7. Under **Resources** , click **DRG route tables**.
  8. Click the name of the route table you want to assign to the new import route distribution, "RT-RPC."
  9. Click **Edit**.
  10. Click **Enable Import Route Distribution** : This option allows you to assign an import route distribution to the route table so it dynamically learns new routes based on BGP advertisements.
     * Choose the import route distribution you created in earlier steps, named "Import-RPC"
  11. Click **Save Changes**.


[Step 5: Reassign the attachment route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_f.htm)
  1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
  2. Click the name of the DRG you're interested in, DRG-1. 
  3. Under **Resources** , click **Virtual Cloud Networks Attachments**. 
  4. Click the name of the DRG attachment used by VCN-1. 
  5. Click **Edit**.
  6. Click **Show Advanced Options**. 
  7. Change the DRG route table from the autogenerated route table for VCN attachments to "RT-VCN"
  8. Click **Save Changes**.
  9. In the breadcrumb at the top of the screen, click the name of the DRG you're interested in, DRG-1. 
  10. Under **Resources** , click **Virtual Circuits Attachments**. 
  11. Click the name of the DRG attachment used by virtual circuit 1. 
  12. Click **Edit**.
  13. Click **Show Advanced Options**. 
  14. Change the DRG route table from the autogenerated route table for RPC, VIRTUAL_CIRCUIT and IPSEC_TUNNEL attachments to "RT-OnPrem."
  15. Click **Save Changes**.
  16. In the breadcrumb at the top of the screen, click the name of the DRG you're interested in, DRG-1. 
  17. Under **Resources** , click **Remote Peering Connections Attachments**. 
  18. Click the name of the DRG attachment used by RPC-1. 
  19. Click **Edit**.
  20. Click **Show Advanced Options**. 
  21. Change the DRG route table from the autogenerated route table for RPC, VIRTUAL_CIRCUIT and IPSEC_TUNNEL attachments to "RT-RPC."


This completes configuration of single on-ramp. At this point, any packets sent from a local or remote VCN to your on-premises network are sent to the mutually attached DRG, and then to your on-premises network.
Was this article helpful?
YesNo

