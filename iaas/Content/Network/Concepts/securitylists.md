Updated 2025-02-06
# Security Lists
The Networking service offers two virtual firewall features to control traffic at the packet level:
  * **Security lists:** Covered in this topic. This is the original type of virtual firewall offered by the Networking service. 
  * **Network security groups:** Another type of virtual firewall that Oracle recommends over security lists. See [Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups).


Both of these features use _security rules_. For important information about how security rules work, and a general comparison of security lists and network security groups, see [Security Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules). 
## Highlights 🔗 
  * Security lists act as virtual firewalls for your compute instances and [other kinds of resources](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison). A security list consists of a set of ingress and egress [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) that apply to all the VNICs _in any subnet that the security list is associated with_. This means that all the VNICs in a given subnet are subject to the same set of security lists. See [Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison).
  * Security list rules function the same as network security group rules. For a discussion of rule parameters, see [Parts of a Security Rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#sec_rules_parts).
  * Each VCN comes with a [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) that has several default rules for essential traffic. If you don't specify a custom security list for a subnet, the default security list is automatically used with that subnet. You can add and remove rules from the default security list.
  * Security lists have separate and different limits compared to network security groups. See [Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison).


## Overview of Security Lists 🔗 
A security list acts as a virtual firewall for an instance, with ingress and egress rules that specify the types of traffic allowed in and out. Each security list is enforced at the VNIC level. However, you configure your security lists _at the subnet level_ , which means that all VNICs in a given subnet are subject to the same set of security lists. The security lists apply to a given VNIC whether it's communicating with another instance in the VCN or a host outside the VCN. 
Each subnet can have multiple security lists associated with it, and each list can have multiple rules (for the maximum number, see [Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison)). A packet in question is allowed if _any rule in any of the lists_ allows the traffic (or if the traffic is part of an existing connection being tracked). There's a caveat if the lists happen to contain both stateful and stateless rules that cover the same traffic. For more information, see [Stateful Versus Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful).
Security lists are regional entities. For limits related to security lists, see [Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison).
Security lists can control both IPv4 and IPv6 traffic. IPv6 addressing and related security list rules are supported in all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses). 
See [Security List Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#sec_list_limits) and [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti) for limits-related information.
## Default Security List 🔗 
Unlike other security lists, the default security list comes with an initial set of stateful rules, which should in most cases be changed to only allow inbound traffic from authorized subnets relevant to the region that homes that VCN or subnet. A list of authorized subnet ranges relevant to each region can be found at [https://docs.cloud.oracle.com/iaas/tools/public_ip_ranges.json](https://docs.oracle.com/iaas/tools/public_ip_ranges.json).
  * **Stateful ingress:** Allow TCP traffic on destination port 22 (SSH) from authorized source IP addresses and any source port. This rule makes it easy for you to create a new cloud network and public subnet, launch a Linux instance, and then immediately use SSH to connect to that instance without needing to write any security list rules yourself. 
**Important**
The default security list doesn't include a rule to allow Remote Desktop Protocol (RDP) access. If you're using [Windows images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm), make sure to add a stateful ingress rule for TCP traffic on destination port 3389 from authorized source IP addresses and any source port.
See [To enable RDP access](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm#prerequisites__enablerdp) for more information.
  * **Stateful ingress:** Allow ICMP traffic type 3 code 4 from authorized source IP addresses. This rule enables your instances to receive Path MTU Discovery fragmentation messages. 
  * **Stateful ingress:** Allow ICMP traffic type 3 (all codes) from your VCN's CIDR block. This rule makes it easy for your instances to receive connectivity error messages from other instances within the VCN.
  * **Stateful egress:** Allow all traffic. This lets instances initiate traffic of any kind to any destination. Notice that this means the instances with public IP addresses can talk to any internet IP address if the VCN has a configured internet gateway. And because stateful security rules use connection tracking, the response traffic is automatically allowed regardless of any ingress rules. For more information, see [Stateful Versus Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful).


The default security list comes with no stateless rules. However, you can always add or remove rules from the default security list.
If your VCN is enabled for IPv6 addressing the default security list contains some default rules for IPv6 traffic. For more information, see [Security Rules for IPv6 Traffic](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#security_lists). 
### Enabling Ping 🔗 
The default security list does not include a rule to allow ping requests. If you plan to ping an instance, see [Rules to Handle Fragmented UDP Packets](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#fragudp).
### Security Rules for IPv6 Traffic 🔗 
The VCN's [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) and [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) support both IPv4 and IPv6 [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules). For example, a network security group or security list could have these security rules:
  * Rule to allow SSH traffic from the on-premises network's IPv4 CIDR
  * Rule to allow ping traffic from the on-premises network's IPv4 CIDR
  * Rule to allow SSH traffic from the on-premises network's **IPv6** prefix
  * Rule to allow ping traffic from the on-premises network's **IPv6** prefix


The [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) in an IPv6-enabled VCN includes default IPv4 rules and the following default IPv6 rules: 
  * **Stateful ingress:** Allow IPv6 TCP traffic on destination port 22 (SSH) from source ::/0 and any source port. This rule makes it easy for you to create a VCN with a public subnet and internet gateway, create a Linux instance, add an internet-access-enabled IPv6, and then immediately connect with SSH to that instance without needing to write any security rules yourself. 
**Important**
The default security list doesn't include a rule to allow Remote Desktop Protocol (RDP) access. If you're using [Windows images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm), add a stateful ingress rule for TCP traffic on destination port 3389 from source ::/0 and any source port.
See [To enable RDP access](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm#prerequisites__enablerdp) for more information.
  * **Stateful ingress:** Allow ICMPv6 traffic type 2 code 0 (Packet Too Big) from source ::/0 and any source port. This rule lets instances to receive Path MTU Discovery fragmentation messages.
  * **Stateful egress:** Choosing to allow all IPv6 traffic lets instances initiate IPv6 traffic of any kind to any destination. Notice that instances with an internet-access-enabled IPv6 can talk to any internet IPv6 address if the VCN has a configured internet gateway. And because stateful security rules use connection tracking, the response traffic is automatically allowed regardless of any ingress rules. For more information, see [Stateful Versus Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful).


## Security Rules 🔗 
If you're not yet familiar with the basics of security rules, see these sections in the security rules topic:
  * [Parts of a Security Rule](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#sec_rules_parts)
  * [Stateful Versus Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful)


Was this article helpful?
YesNo

