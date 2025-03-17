Updated 2024-12-16
# NAT Gateways
On Compute Cloud@Customer, a NAT gateway gives cloud resources without a public IP access to the on-premises network, which is an external public network from the point of view of a VCN, without exposing those resources. You create a NAT gateway in the context of a specific VCN, so the gateway is automatically attached to that VCN upon creation.
A NAT gateway is used to translate IP addresses as traffic passes from one part of an IP network to another. This prevents sources and destinations from having identical IP addresses, and allows RFC 1918 private addresses used in Compute Cloud@Customer traffic to communicate with on-premises data center networks. 
The gateway allows hosts to initiate connections to the on-premises network and receive responses, but prevents them from receiving inbound connections initiated from the on-premises network. NAT gateways are highly available and support TCP, UDP, and ICMP ping traffic. The Networking service automatically assigns a public IP address to the NAT gateway. You can't choose its public IP address.
When a host in the private network initiates a connection to the on-premises network, the NAT device's public IP address becomes the source IP address for the outbound traffic. The response traffic from the on-premises network therefore uses that public IP address as the destination IP address. The NAT device then routes the response back to the private network, to the host that initiated the connection.
VCN routing is controlled at the subnet level, so you can specify which subnets use a NAT gateway. You can only configure one NAT gateway per VCN.
For the purpose of access control, when creating a NAT gateway, you must specify the compartment where you want the gateway to reside. If you're not sure which compartment to use, put the gateway in the same compartment as the VCN.
By default, a NAT gateway allows traffic at the time of creation. However, you can block or allow traffic through the gateway at any time. Blocking a NAT gateway prevents all traffic, regardless of any existing route rules or security rules in the VCN.
Was this article helpful?
YesNo

