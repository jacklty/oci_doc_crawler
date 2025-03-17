Updated 2024-12-16
# Configuring Network Gateways
Learn about the different types of gateways you can configure on Compute Cloud@Customer.
This section describes the role and usage of each gateway type.
**Network Address Translation (NAT) Gateways**
A NAT gateway gives cloud resources without a public IP access to the on-premises network, which is an external public network from the point of view of a VCN, without exposing those resources. You create a NAT gateway in the context of a specific VCN, so the gateway is automatically attached to that VCN upon creation.
See [NAT Gateways](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/nat-gateway.htm#nat-gateway "On Compute Cloud@Customer, a NAT gateway gives cloud resources without a public IP access to the on-premises network, which is an external public network from the point of view of a VCN, without exposing those resources. You create a NAT gateway in the context of a specific VCN, so the gateway is automatically attached to that VCN upon creation.").
**Internet Gateways**
An internet gateway connects the edge of the VCN with the on-premises network. The ultimate target of the traffic routed through an internet gateway can be the internet.
See [Internet Gateways](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/internet-gateway.htm#internet-gateway "On Compute Cloud@Customer, an internet gateway connects the edge of the VCN with the on-premises network. The ultimate target of the traffic routed through an internet gateway can be the internet.").
**Local Peering Gateways**
VCN peering is the process of connecting multiple virtual cloud networks (VCNs) so that resources can communicate using private IP addresses. You can use VCN peering to divide your network into multiple VCNs, for example, based on departments or lines of business, with each VCN having direct private access to the others. You can also place shared resources into a single VCN that all the other VCNs can access privately.
See [Local Peering Gateways (LPGs)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/local-peering-gateway.htm#local-peering-gateway "On Compute Cloud@Customer, You can configure local peering gateways. VCN peering is the process of connecting multiple virtual cloud networks \(VCNs\) so that resources can communicate using private IP addresses.").
**Dynamic Routing Gateways (DRGs)**
a dynamic routing gateway, or DRG, provides a path for private network traffic between the VCN and an on-premises network. This traffic is routed to the data center network and on to its destination. 
See [Creating a Dynamic Routing Gateway](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/creating-a-dynamic-routing-gateway.htm#creating-a-dynamic-routing-gateway "On Compute Cloud@Customer, a DRG is the equivalent of a general purpose router. A DRG is used to connect a VCN to the data center's IP address space. The router is configured separately from the VCNs, at the compartment level and is not required to be in the same compartment as the VCN \(but it typically is\).").
**Service Gateways**
Service Gateway (SG). Some services are isolated on their own network for security and performance reasons. The service gateway (SG) allows a VCN with no external access to privately access Service Network services (such as object storage) in a private subnet. 
See [Service Gateways](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/service-gateway.htm#service-gateway "On Compute Cloud@Customer, a VCN can have only one service gateway. You create a service gateway in the context of a specific VCN, so the gateway is automatically attached to that VCN upon creation. A service gateway allows traffic to and from all subnets at the time of creation. There's no mechanism to block or disable this traffic.").
Was this article helpful?
YesNo

