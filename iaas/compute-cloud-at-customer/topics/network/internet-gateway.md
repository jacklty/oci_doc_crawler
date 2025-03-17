Updated 2024-12-16
# Internet Gateways
On Compute Cloud@Customer, an internet gateway connects the edge of the VCN with the on-premises network. The ultimate target of the traffic routed through an internet gateway can be the internet.
However, on Compute Cloud@Customer, the internet gateway routes traffic to the on-premises network. Traffic to and from the internet is then managed by the routing configuration in the on-premises network.
You create an internet gateway in the context of a specific VCN, so the gateway is automatically attached to that VCN upon creation. To use the gateway, the hosts on both ends of the connection must have public IP addresses for routing. Connections that originate in the VCN and are destined for a public IP address, either inside or outside the VCN, go through the internet gateway. Connections that originate outside the VCN and are destined for a public IP address inside the VCN also go through the internet gateway.
A VCN can have only one internet gateway. You control which public subnets in the VCN can use the gateway by configuring the subnet's associated route table. The public subnet security list rules determine the specific types of traffic that are allowed to and from the resources in the subnet. An internet gateway can be disabled, meaning no traffic flows to or from the internet, regardless of any existing route rules that enable such traffic.
For the purpose of access control, when creating an internet gateway, you must specify the compartment where you want the gateway to reside. If you're not sure which compartment to use, put the gateway in the same compartment as the VCN.
To configure an Internet gateway, see [Configuring an Internet Gateway](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-an-internet-gateway.htm#configuring-an-internet-gateway "On Compute Cloud@Customer, you can configure an Internet Gateway \(IGW\) which provides the VCN with outside access through the on-premises data center network.").
Was this article helpful?
YesNo

