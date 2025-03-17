Updated 2024-08-21
# Internet Gateway
This topic describes how to set up and manage an internet gateway to give your VCN internet access.
**Tip** Oracle also offers a [NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm#NAT_Gateway), which is recommended for subnets in your VCN that do not require externally initiated connections from the internet..
## Highlights 🔗 
  * An internet gateway is an optional gateway you can add to your VCN to enable direct connectivity to the internet.
  * The gateway supports connections initiated from within the VCN (egress) and connections initiated from the internet (ingress).
  * Resources that need to use the gateway for internet access must be in a [public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Public) and have [public IP addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#Public_IP_Addresses). Resources that have private IP addresses can instead use a [NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm#NAT_Gateway) to initiate connections to the internet.
  * Each public subnet that needs to use the internet gateway must have a [route table rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) that specifies the gateway as the target. 
  * You use [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) to control the types of traffic allowed in and out of resources in that subnet. Make sure to allow only the desired types of internet traffic.
  * The internet gateway can be used only by resources in the gateway's VCN. Hosts in the connected on-premises network or in a [peered VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Access_to_Other_VCNs_Peering) cannot use that internet gateway. 
  * You can't add or move an internet gateway to a VCN within a [security zone](https://docs.oracle.com/iaas/security-zone/using/security-zones.htm). Security zones do not permit [public subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Public).
  * Only one internet gateway is needed for each VCN. All public subnets within a VCN have access to the internet gateway, provided security rules and route table rules allow that access.


## Overview of Internet Gateways 🔗 
Before continuing, make sure you've read [Access to the Internet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Private) and also understand how to set up [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) for the resources in a subnet.
An internet gateway as an optional virtual router that connects the edge of the VCN with the internet. To use the gateway, the hosts on both ends of the connection must have public IP addresses for routing. Connections that originate in your VCN and are destined for a public IP address (either inside or outside the VCN) go through the internet gateway. Connections that originate outside the VCN and are destined for a public IP address inside the VCN go through the internet gateway. 
A given VCN can have only one internet gateway. You control which public subnets in the VCN can use the gateway by configuring the subnet's associated route table. You use security rules to control the types of traffic allowed in and out of resources in those public subnets.
The following diagram illustrates a simple VCN setup with a single public subnet. The VCN has an internet gateway, and the public subnet is configured to use the VCN's default route table. The table has a route rule that sends all egress traffic from the subnets to the internet gateway. The gateway allows any ingress connections from the internet with a destination IP address equal to the public IP address of a resource in the VCN. However, the public subnet's security list rules ultimately determine the specific _types_ of traffic that are allowed in and out of the resources in the subnet. Those specific security rules are not shown. 
[![This image shows a simple layout of a VCN with a public subnet that uses an internet gateway.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_internet_gateway.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_internet_gateway.svg)
Callout 1: VCN Default Route Table Destination CIDR | Route Target  
---|---  
0.0.0.0/0 | Internet Gateway  
**Tip** Traffic between a VCN and a public IP address _that is part of Oracle Cloud Infrastructure_ (such as Object Storage) should be routed through a service gateway instead of an internet gateway. 
## Working with Internet Gateways 🔗 
You create an internet gateway in the context of a specific VCN. In other words, the internet gateway is always attached to a VCN. However, you can disable and re-enable the internet gateway at any time. Compare this with a [dynamic routing gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs) (DRG), which you create as a standalone object that you then _attach_ to a particular VCN. DRGs use a different model because they're intended to be modular building blocks for privately connecting VCNs to your on-premises network.
For traffic to flow from a public subnet to the Internet, you must create a corresponding route rule in the subnet's route table. For example, destination CIDR = 0.0.0.0/0 and target = internet gateway; if you want to route the traffic through a firewall, the target can be the private IP address of the firewall. The firewall subnet will then need a route, usually 0.0.0.0/0, to reach the Internet with the internet gateway as the target. 
For traffic flowing from the internet to a destination in a public subnet, the internet gateway routes the traffic directly to the destination by default. You can associate a route table with the internet gateway and define route rules that route ingress public traffic to destinations in the VCN. For example, if you want the internet gateway to route the traffic to a firewall in the VCN first, you can create a route rule for the destination subnet CIDR with the firewall private IP address as the target. Route rules to destinations outside the VCN in an internet gateway route table are not supported.
Only one internet gateway is needed for each VCN. All public subnets within a VCN have access to the internet gateway provided security rules and route table rules allow that access.
For the purposes of access control, you must specify the compartment where you want the internet gateway to reside. If you're not sure which compartment to use, put the internet gateway in the same compartment as the cloud network. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
You may optionally assign a friendly name to the internet gateway. It doesn't have to be unique, and you can change it later. Oracle automatically assigns the internet gateway a unique identifier called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm). 
To delete an internet gateway, it does not have to be disabled, but there must not be a route table that lists it as a target.
See [Gateway Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#gateway_limits) and [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti) for limits-related information.
## Internet Gateway Setup 🔗 
Prerequisites: 
  * You've determined which subnets in the VCN need access to the internet, and you've created those public subnets.
Only one internet gateway is needed for each VCN. All public subnets within a VCN have access to the internet gateway provided security rules and route table rules allow that access.
  * You've determined the types of ingress and egress internet traffic that you want to enable for the resources in each public subnet (examples: ingress HTTPS connections, ingress ICMP ping connections).
  * The required IAM policy is in place to allow you to work with Networking service resources. For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 


**Important**
If you've configured the public subnet to use the [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default), remember that the list includes several helpful default rules that enable basic required access (examples: ingress SSH, egress access to all destinations). Oracle recommends that you become familiar with the basic access that these default rules provide. If you choose not to use the default security list, make sure to provide this basic access by implementing these security rules either in [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) (NSGs) or custom [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists).
The following procedure uses security lists, but you could instead implement the security rules in a network security group and then create all of the subnet's resources in that NSG.
  1. For each public subnet that needs to use the internet gateway, [set up the subnet's security list rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/update-securitylist.htm#update-securitylist "Update the rules used in a security list in a Virtual Cloud Network \(VCN\).") to allow the desired internet traffic. Refer to the following example settings: 
Imagine you have web servers in the public subnet. This example shows how to add an ingress rule for HTTPS connections (TCP port 443) coming from the internet to the web server. Without this rule, inbound HTTPS connections are not allowed.
    1. Leave the **Stateless** checkbox unselected.
    2. **Source Type:** CIDR
    3. **Source CIDR:** 0.0.0.0/0
    4. **IP Protocol:** Leave as TCP. 
    5. **Source Port Range:** Leave as All.
    6. **Destination Port Range** : Enter 443.
    7. **Description:** An optional description of the rule.
  2. [Create the VCN's internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/create-ig.htm#create-ig "Create an internet gateway \(IGW\) in a Virtual Cloud Network \(VCN\) in Networking."). 
After the internet gateway is created and displayed on the **Internet Gateways** page of the VCN you chose, it's already enabled but you still need to add a route rule that allows traffic to flow to the gateway.
  3. For each public subnet that needs to use the internet gateway, [update the subnet's route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.") using the following example settings:
     * **Target Type:** Internet Gateway
     * **Destination CIDR block:** 0.0.0.0/0 (which means that all non-intra-VCN traffic that is not already covered by other rules in the route table will go to the target specified in this rule)
     * **Compartment:** The compartment where the internet gateway is located.
     * **Target:** The internet gateway you just created.
     * **Description:** An optional description of the rule.


The internet gateway is now enabled and working for your cloud network.
Was this article helpful?
YesNo

