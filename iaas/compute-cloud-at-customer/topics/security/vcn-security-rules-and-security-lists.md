Updated 2024-10-07
# VCN Security Rules and Security Lists
On Compute Cloud@Customer, VCN security involves creating and using rules that are gathered into security lists or network security groups (NSGs).
The rules can be stateful or stateless. Stateful rules presume various things about an instance interaction. For example, a stateful rule that applies to a request to an instance assumes that there is a response and automatically allows this response. In contrast, stateless rules don't presume anything about any interactions. Stateless rules are messages from one instance to another, and apply to everything regardless of what has gone before. Stateful rules require overhead processing to track states that stateless rules don't. Instances with heavy and widely varied traffic, such as web sites, should use stateless rules where possible to minimize system loads.
**Note**
Care is needed when creating stateless and stateful rules. When a message appears that fits both stateful and stateless rule criteria, the stateless rule is applied. This results in responses being blocked to requests that seemingly should be allowed.
Your VCN might have subnets that use the default security list. Don't delete any of the list's default security rules unless you've first confirmed that resources in your VCN don't require them. Otherwise, you might disrupt VCN connectivity.
Remember that:
  * A security rule is stateful by default, but can also be configured to be stateless. A common practice is to use stateless rules for high-performance applications. In a case where network traffic matches both stateful and stateless security lists, the stateless rule takes precedence. For more information about configuring VCN security rules, see [Security Rules](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules).
  * To prevent unauthorized access or attacks on Compute instances, we recommend that you use a VCN security rule to allow SSH or RDP access only from authorized CIDR blocks rather than leave them open to the internet (0.0.0.0/0). For additional security, you can temporarily enable SSH (port 22) or RDP (port 3389) access on an as-needed basis using the VCN API [`UpdateNetworkSecurityGroupRules`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityRule/UpdateNetworkSecurityGroupSecurityRules) (if you're using network security groups) or [`UpdateSecurityList`](https://docs.oracle.com/iaas/api/#/en/iaas/latest/SecurityList/UpdateSecurityList)(if you're using security lists). 
For more information about enabling RDP access, see **To enable RDP access** in [Recommended Networking Launch Types](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm#networking). 
For performing instance health checks, we recommend that you configure VCN security rules to allow ICMP pings. For more information, see [Rules to Enable Ping](https://docs.oracle.com/iaas/Content/Network/Concepts/securityrules.htm#ping).


VCN network security groups (NSGs) and security lists enable security-critical network access control to Compute instances, and it's important to prevent any unintended or unauthorized changes to NSGs and security lists. To prevent unauthorized changes, we recommend that you use IAM policies to allow only network administrators to make NSG and security list changes.
The default security list for a VCN comes without stateless rules: all the default security list rules are stateful. In most cases, the default rules should be changed to allow only inbound traffic from authorized subnets.
## Default Security List Rules 🔗 
  * **Stateful ingress:** Allow TCP traffic on destination port 22 (SSH) from authorized source IP addresses and any source port. This rule makes it easy for you to create a new cloud network and public subnet, open a Linux instance, and then immediately use SSH to connect to that instance without needing to write any security list rules yourself.
  * **Stateful ingress:** Allow ICMP traffic type 3 code 4 from authorized source IP addresses. This rule enables instances to receive Path MTU Discovery fragmentation messages.
  * **Stateful ingress:** Allow ICMP traffic type 3 (all codes) from your VCN CIDR block. This rule makes it easy for your instances to receive connectivity error messages from other instances within the VCN.
  * **Stateful egress:** Allow all traffic. This allows instances to initiate traffic of any kind to any destination. Notice that this means the instances with public IP addresses can talk to any internet IP address if the VCN has a configured internet gateway. And because stateful security rules use connection tracking, the response traffic is automatically allowed regardless of any ingress rules.


## Security List Rule Modifications 🔗 
**RDP**
The default security list doesn't include a rule to allow Remote Desktop Protocol (RDP) access. If you're using Microsoft Windows images, ensure to add a stateful ingress rule for TCP traffic on destination port 3389 from authorized source IP addresses and any source port.
**Instance Pings**
The default security list doesn't include a rule to allow ping requests. If you plan to ping an instance, ensure that the instance's applicable security list includes an additional stateful ingress rule to allow ICMP traffic type 8 from the source network you plan to ping from. To allow ping access from the data center, use `0.0.0.0/0` for the source. Note that this rule for pinging is separate from the default ICMP-related rules in the default security list. Don't remove those rules.
**Path MTU Discovery Fragmentation Messages**
If you decide to use stateless security rules to allow traffic to and from endpoints outside the VCN, it's important to add a security rule that allows ingress ICMP traffic type 3 code 4 from source `0.0.0.0/0` and any source port. This rule enables instances to receive Path MTU Discovery fragmentation messages. This rule is critical for establishing a connection to instances. Without it, you can experience connectivity issues.
**UDP**
Instances can send and receive UDP traffic. In some cases, UDP packets might be fragmented on links with smaller MTU sizes. If a UDP packet is too large for the connection size limit, it's fragmented. However, only the first fragment from the packet contains the protocol and port information. If the security rules that allow this ingress or egress traffic specify a particular port number (source or destination), then the fragments after the first one are dropped. If you expect your instances to send or receive large UDP packets, set both the source and destination ports for the applicable security rules to ALL (instead of a particular port number).
**Subnets and Security Rules**
On their own, security lists define a set of security rules that apply to all the VNICs in an entire subnet. To use a specific security list with a particular subnet, associate the security list with the subnet either during subnet creation or later. A subnet can be associated with a maximum of five security lists. Any VNICs that are created in that subnet are subject to the security lists associated with the subnet.
Was this article helpful?
YesNo

