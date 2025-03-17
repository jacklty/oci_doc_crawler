Updated 2024-08-06
# Security Lists
On Compute Cloud@Customer, a security list acts as a virtual firewall for an instance, with ingress and egress rules that specify the types of traffic allowed in and out.
Each security list is enforced at the VNIC level. However, you configure your security lists at the subnet level, which means that all VNICs in a particular subnet are subject to the same set of security lists.
The security lists apply to a particular VNIC whether it's communicating with another instance in the VCN or a host outside the VCN. Each subnet can have multiple security lists associated with it, and each list can have multiple rules.
Each VCN comes with a default security list. If you don't specify a custom security list for a subnet, the default security list is automatically used with that subnet. You can add and remove rules in the default security list. It has an initial set of stateful rules, which should be changed to only allow inbound traffic from authorized subnets. The default rules are:
  * **Stateful ingress:** Allow TCP traffic on destination port 22 (SSH) from authorized source IP addresses and any source port.
This rule enables you to create a new cloud network and public subnet, create a Linux instance, and then immediately use SSH to connect to that instance without needing to write any security list rules yourself.
The default security list doesn't include a rule to allow Remote Desktop Protocol (RDP) access. If you're using Compute Cloud@Customer images, add a stateful ingress rule for TCP traffic on destination port 3389 from authorized source IP addresses and any source port.
  * **Stateful ingress:** Allow ICMP traffic type 3 code 4 from authorized source IP addresses.
This rule enables instances to receive Path MTU Discovery fragmentation messages.
  * **Stateful ingress:** Allow ICMP traffic type 3 (all codes) from your VCN CIDR block.
This rule enables instances to receive connectivity error messages from other instances within the VCN.
  * **Stateful egress:** Allow all traffic.
This allows instances to initiate traffic of any kind to any destination. This implies that instances with public IP addresses can talk to any internet IP address if the VCN has a configured internet gateway. And because stateful security rules use connection tracking, the response traffic is automatically allowed regardless of any ingress rules.


The general process for working with security lists is as follows:
  1. Create a security list.
  2. Add security rules to the security list.
  3. Associate the security list with one or more subnets.
  4. Create resources, such as compute instances, in the subnet.
The security rules apply to all the VNICs in that subnet.


When you create a subnet, you must associate at least one security list with it. It can be either the VCN default security list or one or more other security lists that you already created. You can change which security lists the subnet uses at any time. You can add and remove rules in the security list. It's possible for a security list to contain no rules.
Was this article helpful?
YesNo

