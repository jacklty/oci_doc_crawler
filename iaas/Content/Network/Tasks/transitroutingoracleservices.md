Updated 2025-03-10
# Private Access to Oracle Services
_Transit routing_ refers to a network topology in which an on-premises network uses an intermediary to reach Oracle resources or services or VCNs. The intermediary can be a VCN or a **Dynamic Routing Gateway (DRG)** the on-premises network is already attached to. You connect the on-premises network to a DRG with [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") or [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\)."), and then configure routing so that traffic _transits through the intermediary_ to its destination. 
The three primary transit routing scenarios are: 
  * **Private access to Oracle services:** The scenario covered in this topic. This scenario gives your on-premises network _private access_ to Oracle services, so that your on-premises hosts can use their private IP addresses and the traffic does not go over the public internet. Instead, the traffic travels over a FastConnect private virtual circuit or Site-to-Site VPN, transits through a Virtual Cloud Network (VCN), and then through a **service gateway** to the Oracle service of interest. This scenario is available to an implementation using either a legacy or upgraded [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions).
  * **Access between multiple networks through a single DRG with a firewall between networks:** This scenario connects several VCNs to a single DRG, with all routing configured to send packets through a firewall in a hub VCN before they can be sent to another network. See [Routing traffic through a central network virtual appliance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenario_g.htm#scenario_g). This scenario is only available to an implementation using an upgraded [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions).
  * **Access to multiple VCNs in the same region:** This scenario enables communication between an on-premises network and multiple VCNs in the same region over a single FastConnect private virtual circuit or Site-to-Site VPN and uses a VCN as the hub. See [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region). This scenario is available to an implementation using a legacy [DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions).


## Highlights 🔗 
  * You can set up a VCN so that your on-premises network has _private access_ to Oracle services in the Oracle Services Network by way of the VCN. The hosts in your on-premises network communicate with their private IP addresses. 
  * The VCN uses a [dynamic routing gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs) (DRG) to communicate with the on-premises network. Access to Oracle services is through a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway) on the VCN. The traffic from the VCN to the Oracle service travels over the Oracle network fabric and never traverses the public internet.
  * The service gateway is regional and enables access only to supported Oracle services _in the same region_ as the VCN. 
  * The supported Oracle services are Oracle Cloud Infrastructure Object Storage and others in the Oracle Services Network. For a list, see [Service Gateway: Supported Cloud Services](https://www.oracle.com/cloud/networking/service-gateway/service-gateway-supported-services/) in Oracle Services Network.
  * The service gateway uses the concept of a _service CIDR label_ , which is a string that represents all the regional public IP address ranges for the service or group of services of interest (for example, _OCI PHX Object Storage_ is the string for Object Storage in US West (Phoenix)). You use that service CIDR label when you configure the service gateway and related route rules to control traffic to the service. You can optionally use it when configuring security rules. If the service's public IP addresses change in the future, you don't have to adjust those rules.
  * To enable the intended traffic from the on-premises network through the VCN to Oracle services, you implement route rules for the VCN's DRG attachment and service gateway.
  * If you want, you can set up transit routing _through a private IP in the VCN_. For example, you might want to filter or inspect the traffic between the on-premises network and the Oracle service. In that case, you route the traffic to a private IP on an instance in the VCN for inspection, and the resulting traffic continues to its destination. This topic covers both situations: transit routing directly between gateways on the VCN, and transit routing through a private IP.


## Overview of the Oracle Services Network 🔗 
The _Oracle Services Network_ is a conceptual network in Oracle Cloud Infrastructure that is reserved for Oracle services. These services have [public IP addresses](https://docs.oracle.com/iaas/Content/General/Concepts/addressranges.htm#osn-ranges) that you typically reach over the public internet. However, you can access the Oracle Services Network _without the traffic going over the public internet_. There are different ways, depending on which of your hosts need the access:
  * **Hosts in your on-premises network:**
    * Private access through a VCN with FastConnect private peering or Site-to-Site VPN: This scenario is covered in this topic. The on-premises hosts use private IP addresses and reach the Oracle Services Network by way of the VCN and the VCN's service gateway.
    * [Public access with FastConnect public peering](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure."): The on-premises hosts use public IP addresses.
  * **Hosts in your VCN:**
    * [Private access through a service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway): The VCN's hosts use private IP addresses.


## Overview of On-Premises Network Private Access to Oracle Services 🔗 
The following diagram illustrates the basic layout for giving your on-premises network private access to Oracle services.
[![This image shows the basic layout of the networks.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_basic_layout_with_gateways.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_basic_layout_with_gateways.svg)
Your on-premises network connects to the VCN by way of a [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") private virtual circuit or [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\)."). Each of these types of connections terminates on a Dynamic Routing Gateway (DRG) that is attached to the VCN. The VCN also has a service gateway, which gives the VCN access to the Oracle Services Network. The traffic from your on-premises network transits through the VCN, through the service gateway, and to the Oracle service of interest. The responses return through the service gateway and VCN to your on-premises network.
When you set up a service gateway, you enable a _service CIDR label_ , which is a string that represents all the regional public IP address ranges for the service or group of services that you want to access through the service gateway. For example, _All PHX Services in Oracle Services Network_ is the service CIDR label for the Oracle services available in US West (Phoenix) through a service gateway. Oracle uses Border Gateway Protocol (BGP) on the DRG to advertise those regional public IP address ranges to the edge device (also called the customer-premises equipment or CPE) in your on-premises network. For a list of those ranges available through the service gateway, see [Public IP Addresses for VCNs and the Oracle Services Network](https://docs.oracle.com/iaas/Content/General/Concepts/addressranges.htm#osn-ranges).
### Multiple Connection Paths to Oracle Services
You can configure your on-premises network with multiple connection paths to Oracle Cloud Infrastructure and Oracle services for redundancy or other reasons. For example, you could use both FastConnect public peering and FastConnect private peering. If you have multiple paths, your edge device receives route advertisement of the Oracle services public IP address ranges over multiple paths. For important information about configuring your edge device correctly, see [Routing Details for Connections to the On-premises Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/routingonprem2.htm#Routing_Details_for_Connections_to_Your_OnPremises_Network).
### Multiple VCNs with Private Access to Oracle Services 🔗 
Your organization might choose to use multiple VCNs, each with a service gateway to give the VCN's resources access to Oracle services. For example, you might have a different VCN for each department in your organization.
If you _also_ want to set up your on-premises network with private access to Oracle services through a VCN with a service gateway, this section describes two different network layouts you could use.
In the first layout, you set up a _single_ DRG, with the VCNs in a hub-and-spoke layout as shown in the next diagram. The VCN that acts as the hub is dedicated to providing the on-premises network with private access to Oracle services. The other VCNs are [locally peered](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/localVCNpeering.htm#Local_VCN_Peering_Within_Region) with the hub VCN. You configure only the hub VCN according to instructions in [Setting Up Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#setup_process). This hub-and-spoke layout is recommended and described further in [Transit Routing inside a hub VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitrouting.htm#Transit_Routing_Access_to_Multiple_VCNs_in_the_Same_Region). 
[![This image shows the on-premises network connected to a single DRG.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_single_drg.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_single_drg.svg)
In the second layout, there's a separate DRG for each VCN, with a separate FastConnect private virtual circuit or Site-to-Site VPN from your on-premises network to each DRG. You dedicate one DRG and VCN to providing your on-premises network with private access to Oracle services. In the next diagram, it's the VCN in the center. To configure that VCN, follow the instructions in [Setting Up Private Access to Oracle Services](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm#setup_process). 
[![This image shows the on-premises network connected to multiple DRGs.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_multiple_drgs.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_multiple_drgs.svg)
Notice that in both of these layouts, the on-premises network can reach the Oracle services only through a single VCN's service gateway (the one dedicated for this purpose) and not through the service gateways of the other VCNs. For those other VCNs, only the resources _inside_ those VCNs can reach Oracle services through their VCN's service gateway.
Regardless of which layout you choose, you can write an IAM policy to restrict access to an Object Storage bucket so that _only requests that come through a specific VCN's service gateway_ are allowed for that bucket. With either of these layouts, you might want to write the policy to allow requests from _multiple_ VCNs. To restrict access to specific VCNs, create a network source to specify the allowed VCN, and then write the policy restricting access to only the network source. One network source can specify multiple VCNs or you can create one network source for each VCN. For information on creating networks sources, see [Managing Network Sources](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingnetworksources.htm).
The following example policy assumes you set up one network source for each of your VCNs. The policy lets resources in the example ObjectBackup group write objects to an existing bucket called db-backup that resides in a compartment called ABC. When writing a policy like this one, you can specify one or more network sources. This example shows three.
Copy
```
Allow group ObjectBackup to read buckets in compartment ABC
Allow group ObjectBackup to manage objects in compartment ABC where
  all {target.bucket.name='db-backup', 
    any {request.networkSource.name='<hub_VCN_network_source>', request.networkSource.name='<spoke_1_VCN_network_source>', request.networkSource.name='<spoke_2_VCN_network_source>'},
    any {request.permission='OBJECT_CREATE', request.permission='OBJECT_INSPECT'}}
```

For more information, see [Setting Up a Service Gateway in the Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#setting_up_sgw) in the procedure for setting up a service gateway.
### Requests from Oracle Services to Your Clients
The service gateway does not allow incoming connection requests to the VCN or your on-premises network. Any connection requests coming from an Oracle service to your on-premises network must come over a public path such as the internet or FastConnect public peering.
If you use Oracle Analytics Cloud so that it initiates connection requests to clients, and you _also_ want to set up private access to Oracle services for your on-premises network, see this [known issue](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/known_issues_for_networking.htm#sgw-private-access).
## Transit Routing Options for Private Access to Oracle Services 🔗 
Two options exist for routing through the VCN for private access to Oracle services:
  * **Transit routing directly through gateways:** You route the traffic directly through the VCN, from one gateway to the other.
  * **Transit routing through a private IP:** You set up an instance in the VCN to filter or inspect the traffic between the on-premises network and Oracle Services Network, and route traffic through a private IP on the instance.


The examples shown in the following sections assume that the VCN contains no workloads that need to access the on-premises network or Oracle Services Network. The VCN is being used only for transit routing of traffic _through the VCN_.
[Transit routing directly through gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
In this example, you route directly through the two gateways on the VCN: the **Dynamic Routing Gateway (DRG)** and the **service gateway**. See the following diagram.
[![This image shows the route tables and rules required when setting up the scenario.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_detailed_layout.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_detailed_layout.svg)
The diagram callouts show two route tables, each associated with a different resource:
  * **DRG attachment:**
    * The VCN route table is associated with the DRG _attachment_. Why the attachment and not the DRG itself? Because the DRG is a standalone resource that you can attach to any VCN in the same region and tenancy as the DRG. The attachment itself identifies which VCN. 
    * The VCN route table routes the inbound traffic that is from the on-premises network and destined for a supported Oracle service. You configure the rule to send that traffic to the service gateway. 
Callout 1: VCN route table for the DRG attachment  Destination CIDR | Route Target  
---|---  
All OSN services in the region | Service Gateway  
  * **Service gateway:**
    * This VCN route table is associated with the service gateway.
    * The VCN route table routes response traffic that is from a supported Oracle service and destined for the on-premises network. You configure the rule to send that traffic to the DRG.
Callout 2: VCN route table for the service gateway Route Target | Route Target  
---|---  
172.16.0.0/12 | DRG  


[Transit routing through a private IP in the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
In this example, you set up an instance in the VCN to act as a firewall or intrusion detection system to filter or inspect the traffic between the on-premises network and Oracle Services Network. See the following diagram.
[![This image shows the route tables and rules required when setting up the scenario with a private IP in the hub VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_detailed_layout_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_detailed_layout_firewall.svg)
Callout 1: Route table associated with Subnet-Frontend Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
Callout 2: Route table associated with Subnet-Backend Destination CIDR | Route Target  
---|---  
All OSN services in the region | Service gateway  
Callout 3: Route table associated with DRG attachment Destination CIDR | Route Target  
---|---  
All OSN services in the region | 10.0.4.3  
Callout 4: Route table associated with service gateway Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | 10.0.8.3  
The instance has two VNICs, each with a private IP. One of the VNICs is in a subnet that faces the on-premises network (referred to here as the _frontend subnet_). The other VNIC is in a subnet that faces the Oracle Services Network (referred to here as the _backend subnet_). The frontend VNIC has private IP 10.0.4.3, and the backend VNIC has private IP 10.0.8.3.
The diagram shows four route tables, each associated with a different resource:
  * **DRG attachment:**
    * This VCN route table is associated with the DRG _attachment_. Why the attachment and not the DRG itself? Because the DRG is a standalone resource that you can attach to any VCN in the same region and tenancy as the DRG. The attachment itself identifies which VCN. 
    * The VCN route table routes the inbound traffic that is from the on-premises network and destined for a supported Oracle service. You configure the rule to send the traffic to the private IP in the frontend subnet.
  * **Service gateway:**
    * This VCN route table is associated with the service gateway.
    * The VCN route table routes response traffic that is from a supported Oracle service and destined for the on-premises network. You configure the rule to send that traffic to the private IP in the backend subnet.
  * **Subnet-frontend:**
    * This VCN route table is associated with Subnet-frontend. 
    * It includes a rule to enable traffic with the on-premises network.
  * **Subnet-backend:**
    * This VCN route table is associated with Subnet-backend. 
    * It includes a rule to enable traffic with the regional Oracle Services Network.


### Important Transit Routing Restrictions to Understand 🔗 
This section includes some additional important details about routing:
  * **Route table for the DRG attachment:**
    * A VCN route table that is associated with a DRG attachment can only have rules that target a service gateway, a private IP, or a local peering gateway. 
    * A DRG attachment always has a route table associated with it, but you can associate a _different_ route table, edit the table's rules, or delete some or all rules. 
  * **Route table for a service gateway:**
    * A VCN route table that is associated with a service gateway can only have rules that target a DRG or a private IP. 
    * A service gateway can exist without a route table associated with it. However, after you associate a route table with a service gateway, there must always be a route table associated with it. But, you can associate a different route table. You can also edit the table's rules, or delete some or all of the rules. 
  * **Traffic _transiting through_ the VCN:**The route tables discussed here are intended only for moving traffic _through_ the VCN between locations in the on-premises network and the Oracle Services Network. If you're using a private IP in the VCN, you configure the route tables so that the private IP is placed in that traffic path going _through_ the VCN. 
  * **Inbound traffic to the VCN:** Even though the preceding statement is true (about traffic _through_ the VCN), inbound traffic to subnets _within the VCN_ is always allowed. You do not need to set up explicit rules for this inbound traffic in the DRG attachment's route table or service gateway's route table. When this kind of inbound traffic reaches the DRG or the service gateway, the traffic is automatically routed to its destination in the VCN by the _VCN local routing_. Because of VCN local routing, for any route table belonging to a given VCN, you can't create a rule that lists that VCN's CIDR (or a subsection) as the rule's destination.
  * **VCN traffic when transit routing through a private IP:** The immediately preceding statement about VCN local routing means that you only use the VCN for _transit_ between the on-premises network and spoke VCNs. **Do not set up workloads in the VCN itself.** More explicitly, if you set up transit routing through a private IP in the VCN, you can't also route the _VCN's_ traffic through that private IP. Referring to the preceding diagram, if you were to change the route rule in the service gateway's route table so that the destination CIDR is 0.0.0.0/0 instead of 172.16.0.0/12, only traffic coming from the Oracle Services Network and destined for addresses _outside_ the VCN's CIDR block would be routed through the private IP. Because of VCN local routing, any traffic destined for addresses within the VCN is automatically routed directly to the destination IP address. The VCN local routing takes precedence over the service gateway's route table (in general, over _any_ of the VCN's route tables). 


## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
If you're a member of the Administrators group, you already have the required access to set up transit routing. Otherwise, you need access to the Networking service, and you need the ability to launch instances. See [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies).
## Setting Up Private Access to Oracle Services 🔗 
This section shows how to use the Console to set up transit routing with a VCN to give your on-premises network private access to Oracle services.
[For routing directly between gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
**Tip** You might already have many of the necessary Networking components and connections in this advanced scenario already set up. So you might be able to skip some of the following tasks. **If you already have a network layout with a VCN connected to your on-premises network, and a service gateway for that VCN, then Task 4 is the most important.** It enables traffic routing between your on-premises network and the Oracle Services Network. 
[Task 1: Set up the VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
[![This image shows task 1: setting up the VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task1.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task1.svg)
In this task, you set up the VCN. For this example, no subnet is required.
For more information and instructions: 
  * [VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure.")


[Task 2: Add a service gateway to the VCN ](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
[![This image shows task 2: adding a service gateway to the VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task2.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task2.svg)
In this task, you add a service gateway to the VCN and enable the gateway for the regional Oracle Services Network.
Notice that you do not yet create the route table that will be associated with the service gateway. That comes in a later task.
  1. In the Console, view the VCN's details.
  2. Under **Resources** , click **Service Gateways**.
  3. Click **Create Service Gateway**.
  4. Enter the following values: 
     * **Name:** A descriptive name for the service gateway. It doesn't have to be unique. Avoid entering confidential information.
     * **Create in compartment** : The compartment where you want to create the service gateway, if different from the compartment you're currently working in. 
     * **Services:** All <region> Services in Oracle Services Network.
  5. Click **Create Service Gateway**.
The service gateway is then created and displayed on the **Service Gateways** page in the compartment you chose.


[Task 3: Connect the VCN to your on-premises network](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
[![This image shows task 3: connecting the VCN to your on-premises network.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task3.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task3.svg)
In this task, you set up either FastConnect or Site-to-Site VPN between your VCN and your on-premises network. As part of this process, you attach a DRG to the VCN and set up routing between the VCN and your on-premises network. Do not create the route table associated with the DRG attachment yet. That comes in a later task. For more information and instructions: 
  * [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.")
  * [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).")
  * [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs)


**Important** If you're using Site-to-Site VPN with static routing, and the VCN is configured to give the on-premises network private access to Oracle services, you must configure an edge device with the routes for the Oracle Services Network public IP ranges advertised by the DRG over the private path (through the service gateway). For a list of those ranges, see [Public IP Addresses for VCNs and the Oracle Services Network](https://docs.oracle.com/iaas/Content/General/Concepts/addressranges.htm#osn-ranges)
[Task 4: Set up ingress routing for the DRG and service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
[![This image shows task 4: setting up ingress routing between the DRG and service gateway.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task4.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task4.svg)
Callout 1: Route table associated with DRG attachment Destination CIDR | Route Target  
---|---  
All OSN services in the region | Service Gateway  
Callout 2: Route table associated with service gateway Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
In this task, you set up the route tables for the DRG attachment and the service gateway.
Prerequisites: 
  * You already have a DRG attached to the VCN. 
  * You already have a service gateway. 


  1. Create a route table for the DRG attachment:
    1. In the Console, view the VCN's details.
    2. Under **Resources** , click **Route Tables** to view the VCN's route tables.
    3. Click **Create Route Table**. 
    4. Enter the following:
       * **Name:** A descriptive name for the route table. Example: VCN ingress route table . Avoid entering confidential information.
       * **Create in Compartment:** Leave as is. 
    5. Click **+ Additional Route Rule** , and enter this information for the route rule:
       * **Target Type:** Service gateway.
       * **Destination Service** : All <region> Services in Oracle Services Network.
       * **Compartment:** The compartment where the service gateway is located.
       * **Target:** The service gateway.
       * **Description:** An optional description of the rule.
    6. Click **Create Route Table**.
The route table is created and displayed in the list. 
  2. Associate the route table (called _VCN ingress route table_ in this example) with the VCN's DRG attachment:
    1. While still viewing the VCN's details, click **Dynamic Routing Gateways** to view the attached DRG.
    2. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Associate With Route Table**. 
    3. Enter the following:
       * **Route Table Compartment:** Select the compartment of the route table for the DRG attachment. 
       * **Route Table:** Select the route table for the DRG attachment.
    4. Click **Associate**.
The route table is associated with the DRG attachment. 
  3. Create a route table for the service gateway:
    1. While still viewing the VCN's details, click **Route Tables**.
    2. Click **Create Route Table**. 
    3. Enter the following:
       * **Create in Compartment:** Leave as is. 
       * **Name:** A descriptive name for the route table. Example: Service Gateway Route Table. Avoid entering confidential information.
    4. Click **+ Additional Route Rule** , and enter this information for the route rule:
       * **Target Type:** Dynamic Routing Gateway. The VCN's attached DRG is automatically selected as the target, and you don't have to specify the target yourself.
       * **Destination CIDR Block:** The on-premises network's CIDR (172.16.0.0/12 in the earlier example).
       * **Description:** An optional description of the rule.
    5. Click **Create Route Table**.
The route table is created and displayed in the list. 
  4. Associate the route table (called _Service Gateway Route Table_ in this example) with the service gateway:
    1. While still viewing the VCN's details, click **Service Gateways**.
    2. For the service gateway, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Associate With Route Table**. 
    3. Enter the following:
       * **Route Table Compartment:** Select the compartment of the route table for the service gateway. 
       * **Route Table:** Select the route table for the service gateway.
    4. Click **Associate**.
The route table is associated with the service gateway. 


[For routing through a private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/transitroutingoracleservices.htm)
**Tip** You might already have many of the necessary Networking components and connections in this advanced scenario already set up. So you might be able to skip some of the following tasks. **If you already have a network layout with a VCN connected to your on-premises network, and a service gateway for that VCN, then Tasks 4 and 5 are the most important.** They enable traffic to be routed between your on-premises network and the spoke VCN. 
Task 1: Set up the VCN 
[![This image shows task 1: setting up the VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task1_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task1_firewall.svg)
In this task, you set up the VCN. This example also has two subnets: one for the frontend VNIC on the instance, and one for the backend VNIC on the instance. Oracle recommends using regional _private_ subnets. 
For more information and instructions: 
  * [VCNs and Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNs.htm#VCNs_temp "A Virtual Cloud Network \(VCN\) is a customizable and private network set up in Oracle Cloud Infrastructure.")


Task 2: Add a service gateway to the VCN 
[![This image shows task 2: adding a service gateway to the VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task2_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task2_firewall.svg)
In this task, you add a service gateway to the VCN and enable the gateway for the regional Oracle Services Network.
Notice that you do not yet create the route table that will be associated with the service gateway. That comes in a later task.
  1. In the Console, view the VCN's details.
  2. Under **Resources** , click **Service Gateways**.
  3. Click **Create Service Gateway**.
  4. Enter the following values: 
     * **Name:** A descriptive name for the service gateway. It doesn't have to be unique. Avoid entering confidential information.
     * **Create in compartment** : The compartment where you want to create the service gateway, if different from the compartment you're currently working in. 
     * **Services:** All <region> Services in Oracle Services Network.
  5. Click **Create Service Gateway**.
The service gateway is then created and displayed on the **Service Gateways** page in the compartment you chose.


Task 3: Connect the VCN to your on-premises network 
[![This image shows task 3: connecting the VCN to your on-premises network.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task3.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task3.svg)
In this task, you set up either FastConnect or Site-to-Site VPN between your hub VCN and your on-premises network. As part of this process, you attach a DRG to the hub VCN and set up routing between the hub VCN and your on-premises network.Notice that you do not create the route table associated with the DRG attachment yet. That comes in a later step.For more information and instructions: 
  * [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.")
  * [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).")
  * [Dynamic Routing Gateways](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs)


**Important** If you're using Site-to-Site VPN with static routing, and the VCN is configured to give the on-premises network private access to Oracle services, you must configure an edge device with the routes for the Oracle Services Network public IP ranges advertised by the DRG over the private path (through the service gateway). For a list of those ranges, see [Public IP Addresses for VCNs and the Oracle Services Network](https://docs.oracle.com/iaas/Content/General/Concepts/addressranges.htm#osn-ranges)
Task 4: Set up the private IPs on an instance in the VCN 
[![This image shows task 4: setting up the instance in the VCN.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task4_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task4_firewall.svg)
In this task, you set up the instance to have two private IPs. Prerequisites: 
  * You already have a VCN with two subnets.
  * Review this information: [Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route).


  1. If you haven't already, create the instance in the VCN. See [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). The primary VNIC is created in the subnet you specify.
  2. Create a secondary VNIC for the other subnet and configure the OS to use it. See [Managing VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#console).
  3. Disable the source/destination check on each of the VNICs. See [Overview of VNICs and Physical NICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#overview).
  4. For each VNIC, determine which private IP you want to use as the routing target. If you want to use a secondary private IP instead of the VNIC's primary private IP, assign that secondary private IP and configure the OS to use it. See [Assigning a New Secondary Private IP to a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm#top "Assign a new secondary private IP address to a VNIC."). 
  5. For each of the private IPs you created, record the private IP address (for example: 10.0.4.3).
  6. Configure the instance as necessary for the job it performs (for example, configure the firewall or intrusion detection system on the instance). 


Task 5: Set up ingress routing for the DRG and service gateway 
[![This image shows task 5: setting up ingress routing between the DRG and service gateway.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task5_firewall.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_sgw_transit_task5_firewall.svg)
Callout 1: Route table associated with Subnet-Frontend Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | DRG  
Callout 2: Route table associated with Subnet-Backend Destination CIDR | Route Target  
---|---  
All OSN services in the region | Service gateway  
Callout 3: Route table associated with DRG attachment Destination CIDR | Route Target  
---|---  
All OSN services in the region | 10.0.4.3  
Callout 4: Route table associated with service gateway Destination CIDR | Route Target  
---|---  
172.16.0.0/12 | 10.0.8.3  
In this task, you set up the route tables for the DRG attachment and service gateway.
Prerequisites: 
  * You already have a DRG attached to the VCN. 
  * You already have a service gateway. 
  * You already have the two private IPs to use as the routing targets (see the preceding task).


  1. Create a route table for the DRG attachment:
    1. In the Console, view the VCN's details.
    2. Under **Resources** , click **Route Tables** to view the VCN's route tables.
    3. Click **Create Route Table**. 
    4. Enter the following:
       * **Name:** A descriptive name for the route table. Example: VCN ingress route table . Avoid entering confidential information.
       * **Create in Compartment:** Leave as is. 
    5. Click **+ Additional Route Rule** , and enter this information for the route rule:
       * **Target Type:** Private IP.
       * **Destination:** Service.
       * **Destination Service** : All <region> Services in Oracle Services Network
       * **Compartment:** The compartment where the frontend subnet's private IP is located.
       * **Target:** The frontend subnet's private IP, which you recorded in the previous task (10.0.4.3 in the example).
       * **Description:** An optional description of the rule.
    6. Click **Create Route Table**.
The route table is created and displayed in the list. 
  2. Associate the route table (called _VCN ingress route table_ in this example) with the VCN's DRG attachment:
    1. While still viewing the VCN's details, click **Dynamic Routing Gateways** to view the attached DRG.
    2. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Associate Route Table**. 
    3. Select the route table.
    4. Click **Associate Route Table**.
The route table is associated with the DRG attachment. 
  3. Create a route table for the service gateway:
    1. While still viewing the VCN's details, click **Route Tables**.
    2. Click **Create Route Table**. 
    3. Enter the following:
       * **Create in Compartment:** Leave as is. 
       * **Name:** A descriptive name for the route table. Example: Service Gateway Route Table. Avoid entering confidential information.
    4. Click **+ Additional Route Rule** , and enter this information for the route rule:
       * **Target Type:** Private IP.
       * **Destination:** CIDR Block.
       * **Destination CIDR Block** : The on-premises network's CIDR (172.16.0.0/12 in the earlier example).
       * **Compartment:** The compartment where the private IP is located.
       * **Target:** The backend subnet's private IP, which you recorded in the previous task (10.0.8.3 in the example).
       * **Description:** An optional description of the rule.
    5. Click **Create Route Table**.
The route table is created and displayed in the list. 
  4. Associate the route table (called _Service Gateway Route Table_ in this example) with the service gateway:
    1. While still viewing the VCN's details, click **Service Gateways**.
    2. For the service gateway, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Associate With Route Table**. 
    3. Enter the following:
       * **Route Table Compartment:** Select the compartment of the route table for the service gateway. 
       * **Route Table:** Select the route table for the service gateway.
    4. Click **Associate**.
The route table is associated with the service gateway. 


## Turning Off Transit Routing 🔗 
To turn off transit routing, remove the rules from:
  * The route table associated with the DRG attachment.
  * The route table associated with service gateway.


A route table can be associated with a resource but have no rules. Without at least one rule, a route table does nothing. 
A DRG attachment or service gateway can exist without a route table associated with it. However, after you associate a route table with a DRG attachment or service gateway, there must always be a route table associated with it. But, you can associate a _different_ route table. You can also edit the table's rules, or delete some or all rules.
Was this article helpful?
YesNo

