Updated 2025-02-12
# NAT Gateway
This topic describes how to set up and manage a Network Address Translation (NAT) gateway. A **NAT gateway** gives cloud resources without public IP addresses access to the internet without exposing those resources to incoming internet connections.
## Highlights 🔗 
  * You can add a NAT gateway to your VCN to give instances in a private subnet access to the internet. 
  * Instances in a private subnet don't have public IP addresses. With the NAT gateway, they can initiate connections to the internet and receive responses, but not receive inbound connections initiated from the internet.
  * NAT gateways are highly available and support TCP, UDP, and ICMP ping traffic.


## Overview of NAT 🔗 
NAT is a networking technique commonly used to give an entire private network access to the internet without assigning each host a public IPv4 address. The hosts can initiate connections to the internet and receive responses, but not receive inbound connections initiated from the internet. 
When a host in the private network initiates an internet-bound connection, the NAT device's public IP address becomes the source IP address for the outbound traffic. The response traffic from the internet therefore uses that public IP address as the destination IP address. The NAT device then routes the response to the host in the private network that initiated the connection.
## Overview of NAT Gateways 🔗 
The Networking service offers a reliable and highly available NAT solution for your VCN in the form of a NAT gateway. 
Example scenario: Imagine you have resources that need to receive inbound traffic from the internet (for example, web servers). You also have private resources that need to be protected from inbound traffic from the internet. All of these resources need to initiate connections to the internet to request software updates from sites on the internet. 
You set up a VCN and add a public subnet to hold the web servers. When launching the instances, you assign public IP addresses to them so they can receive inbound internet traffic. You also add a private subnet to hold the private instances. They cannot have public IP addresses because they are in a private subnet.
You add an internet gateway to the VCN. You also add a route rule in the public subnet's route table that directs internet-bound traffic to the internet gateway. The public subnet's instances can now initiate connections to the internet and also receive inbound connections initiated from the internet. Remember that you can use [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) to control the types of traffic that are allowed in and out of the instances at the packet level. 
You add a NAT gateway to the VCN. You also add a route rule in the private subnet's route table that directs internet-bound traffic to the NAT gateway. The private subnet's instances can now initiate connections to the internet. The NAT gateway allows responses, but it does not allow connections that are _initiated from the internet_. Without that NAT gateway, the private instances would instead need to be in the public subnet and have public IP addresses to get their software updates. 
When routing the response traffic from the internet back to the subnet, by default a NAT gateway routes the traffic to the destination directly. You can associate a route table with the NAT gateway, and define route rules for NAT gateway ingress routing in that route table. For example, if you want the NAT gateway to route the response traffic to a firewall first, you can create a route rule for the destination subnet CIDR with the firewall private IP as the target in the NAT gateway route table. 
The following diagram illustrates the basic network layout for the example. The arrows indicate whether connections can be initiated in only one direction or both. 
[![This image shows the basic layout of a VCN with a NAT gateway and internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_nat_gateway.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_nat_gateway.svg)
Callout 1: Public Subnet Route Table Destination CIDR | Route Target  
---|---  
0.0.0.0/0 | Internet Gateway  
Callout 2: Private Subnet Route Table Route Target | Route Target  
---|---  
0.0.0.0/0 | NAT Gateway  
**Note**
A NAT gateway can be used only by resources in the gateway's own VCN. If the VCN is [peered with another](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/VCNpeering.htm#Access_to_Other_VCNs_Peering), resources in the other VCN cannot access the NAT gateway.
Also, resources in an on-premises network connected to the NAT gateway's VCN with [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.") or an [Site-to-Site VPN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPsec.htm#managingIPSec "Site-to-Site VPN provides an IPSec connection between an on-premises network and a Virtual Cloud Network \(VCN\).") cannot use the NAT gateway. 
Here are a few basics about NAT gateways: 
  * The NAT gateway supports TCP, UDP, and ICMP ping traffic.
  * The gateway supports a maximum of approximately 20,000 concurrent connections to a single destination address and port. 
  * The Networking service can either allocate a new public IP address for a new NAT Gateway, or you can specify a specific existing reserved public IP to use for a newly created NAT Gateway. 
  * There's a limit on the number of NAT gateways per VCN, but your VCN will most likely only need one NAT gateway. You can request an increase to that limit. See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase..


### Routing for a NAT Gateway
You control routing in your VCN at the subnet level, so you can specify which subnets in your VCN use a NAT gateway. You can have more than one NAT gateway on a VCN (although you must [request an increase in your limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm)). For example, if you want an external application to distinguish traffic from the VCN's different subnets, you could set up a different NAT gateway (and thus a different public IP address) for each subnet. A given subnet can route traffic to only a single NAT gateway. 
### Blocking Traffic Through a NAT Gateway
You create a NAT gateway in the context of a specific VCN. In other words, the NAT gateway is automatically always attached to only one VCN of your choice. However, you can block or allow traffic through the NAT gateway at any time. By default, the gateway allows traffic upon creation. Blocking the NAT gateway prevents all traffic from flowing, regardless of any existing route rules or security rules in your VCN. For instructions on how to block traffic, see [Blocking or Allowing Traffic for a NAT Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm#nat-block "Block or allow traffic for a NAT gateway.").
### Transitioning to a NAT Gateway
If you're switching from using a [NAT instance in your VCN](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route) to a NAT gateway, consider that the public IP address for your NAT device will change.
If you're switching from using an internet gateway to a NAT gateway, the instances with access to the NAT gateway no longer need public IP addresses to reach the internet. Also, the instances no longer need to be in a public subnet. You can't switch a subnet from [public to private](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Public). However, you can [delete the ephemeral public IPs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm#top "Deleting an ephemeral public IP automatically unassigns it from its private IP.") from your instances if you like.
### Deleting a NAT Gateway
To delete a NAT gateway, its traffic does not have to be blocked, but there must not be a route table that lists it as a target. For instructions, see [Deleting a NAT Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-delete.htm#nat-delete "Delete a NAT gateway from a Virtual Cloud Network \(VCN\) in Networking."). 
### Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 
## Setting Up a NAT Gateway 🔗 
[Task 1: Create the NAT gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm)
See the instructions in [Creating a NAT Gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-create.htm#nat-create "Create a NAT gateway in a virtual cloud network \(VCN\) in Networking."). 
[Task 2: Update routing for the subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/NATgateway.htm)
When you create a NAT gateway, you must also create a route rule that directs the desired traffic from the subnet to the NAT gateway. You do this for each subnet that needs to access the gateway.
  1. Determine which subnets in your VCN need access to the NAT gateway. 
  2. For each of those subnets, [update the subnet's route table](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/update-rules-routetable.htm#update-rules-routetable "Add, edit, or delete rules for a Virtual Cloud Network \(VCN\) route table.") to include a new rule using the following settings: 
     * **Target Type:** NAT Gateway.
     * **Destination CIDR Block:** 0.0.0.0/0
     * **Compartment:** The compartment where the NAT gateway is located.
     * **Target NAT Gateway:** The NAT gateway.
     * **Description:** An optional description of the rule.


Any subnet traffic with a destination that matches the rule is routed to the NAT gateway. For more information about setting up route rules, see [VCN Route Tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).
Later, if you no longer need the NAT gateway and want to delete it, you must first delete all the route rules in your VCN that specify the NAT gateway as the target.
**Tip** Without the required routing, traffic doesn't flow over the NAT gateway. If a situation occurs where you need to temporarily stop the traffic flow over the gateway, you can simply remove the route rule that enables traffic. Or you can [block traffic through the gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/nat-block.htm#nat-block "Block or allow traffic for a NAT gateway.") entirely. You do not need to delete it.
Was this article helpful?
YesNo

