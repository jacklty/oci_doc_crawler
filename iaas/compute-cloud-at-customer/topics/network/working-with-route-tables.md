Updated 2024-08-06
# Working with Route Tables
On Compute Cloud@Customer, 
Each VCN automatically comes with an empty default route table. Subnets use the default route table of the parent VCN, unless you explicitly assign them a different route table. When you add route rules to a VCN, you can add them to the default table if that suits your needs. However, if you need both a public subnet and a private subnet, you instead create a separate custom route table for each subnet. 
The primary routing scenario is for sending subnet traffic to destinations outside the VCN. A subnet has a single route table of your choice associated with it at the time of creation. All VNICs in that subnet are subject to the rules in the route table. Traffic within the VCN is automatically handled by the VCN internal routing. No route rules are required to enable that traffic. You can change which route table the subnet uses at any time. You can also edit a route table's rules, or remove all the rules from the table. 
A route rule specifies a destination CIDR block and the target, or the next hop, for any traffic that matches that CIDR. When selecting the target you also specify its compartment. Supported target types for a route rule are the different VCN gateways.
Route rules must be configured carefully to ensure that the network traffic reaches the intended destination and isn't dropped. Moving route rules between compartments is not supported.
Was this article helpful?
YesNo

