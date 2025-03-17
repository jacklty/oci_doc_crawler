Updated 2023-09-28
# Security Rules
On Compute Cloud@Customer, you can configure security rules for security lists and network security groups (NSGs).
This section explains important aspects of security rules that you need to understand to implement them. How you create, manage, and apply security rules varies between security lists and network security groups. 
## Parts of a Security Rule 🔗 
A security rule allows a particular type of traffic into or out of a VNIC. For example, a commonly used security rule allows ingress TCP port 22 traffic for establishing SSH connections to the instance. Without security rules, no traffic is allowed into and out of VNICs in the VCN.
Each security rule specifies the following items:
  * **Direction (ingress or egress):** Ingress is inbound traffic to the VNIC; egress is outbound traffic from the VNIC.
The REST API model for security lists is different from network security groups. With security lists, there is an `IngressSecurityRule` object and a separate `EgressSecurityRule` object. With network security groups, there is only a `SecurityRule` object, and the object's `direction` attribute determines whether the rule is for ingress or egress traffic.
  * **Stateful or stateless:** If stateful, connection tracking is used for traffic matching the rule. If stateless, no connection tracking is used. See Stateful and Stateless Rules in this section.
  * **Source type and source:** For ingress rules only; the source you provide depends on the source type you choose. These source types are allowed:
Source Type  |  Allowed Source  
---|---  
CIDR |  The CIDR block where the traffic originates from. Use 0.0.0.0/0 to indicate all IP addresses. The prefix is required. For example, include the /32 if specifying an individual IP address.  
  * **Destination type and destination:** For egress rules only; the destination you provide depends on the destination type you choose. These destination types are allowed:
Destination Type  |  Allowed Destination  
---|---  
CIDR |  The CIDR block that the traffic is destined for. Use 0.0.0.0/0 to indicate all IP addresses. The prefix is required. For example, include the /32 if specifying an individual IP address.  
  * **IP Protocol:** Either a single [IPv4 protocol](https://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) or "all" to cover all protocols.
  * **Source port:** The port where the traffic originates from. For TCP or UDP, you can specify all source ports, or optionally specify a single source [port number](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), or a range.
  * **Destination port:** The port where the traffic is destined to. For TCP or UDP, you can specify all destination ports, or optionally specify a single destination [port number](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), or a range.
  * **ICMP type and code:** For ICMP, you can specify all types and codes, or optionally specify a single [type](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) with an optional code. If the type has multiple codes, create a separate rule for each code you want to allow.
  * **Description:** NSG security rules contain an optional attribute to include a description of the rule. This is currently not supported for security list rules.


## Stateful and Stateless Rules 🔗 
When you create a security rule, you choose whether it is stateful or stateless. The default is stateful. Stateless rules are recommended if you have a high-volume internet-facing website, for the HTTP/HTTPS traffic.
Marking a security rule as **stateful** indicates that you want to use connection tracking for any traffic that matches that rule. This means that when an instance receives traffic matching the stateful ingress rule, the response is tracked and automatically allowed back to the originating host, regardless of any egress rules applicable to the instance. And when an instance sends traffic that matches a stateful egress rule, the incoming response is automatically allowed, regardless of any ingress rules.
Marking a security rule as **stateless** indicates that you do NOT want to use connection tracking for any traffic that matches that rule. This means that response traffic is not automatically allowed. To allow the response traffic for a stateless ingress rule, you must create a corresponding stateless egress rule.
If you use both stateful and stateless rules, and there is traffic that matches both a stateful and stateless rule in a particular direction, the stateless rule takes precedence and the connection is not tracked. You would need a corresponding rule in the other direction, either stateless or stateful, for the response traffic to be allowed.
If you decide to use stateless security rules to allow traffic to/from endpoints outside the VCN, it is important to add a security rule that allows ingress ICMP traffic type 3 code 4 from source 0.0.0.0/0 and any source port. This rule enables your instances to receive Path MTU Discovery fragmentation messages. This rule is critical for establishing a connection to your instances. Without it, you can experience connectivity issues.
## Best Practices for Security Rules 🔗 
  * **Use network security groups**
Oracle recommends using NSGs for components that all have the same security posture. For example, in a multitier architecture, you would have a separate NSG for each tier. A tier's VNICs would all belong to that tier's NSG.
Within a tier, you might have a particular subset of the tier's VNICs that have additional, special security requirements. Therefore you would create another NSG for those additional rules, and place that subset of VNICs into both the tier's NSG and the NSG with additional rules.
  * **Understand default security list rules**
Each VCN automatically comes with a default security list that contains several default security rules to help you get started using the Networking service. Those rules exist because they enable basic connectivity.
Even if you choose not to use security lists or the default security list, get familiar with the rules so you better understand the types of traffic that your networked cloud resources require. You might want to use those rules in your NSGs or any custom security lists that you set up.
There is no default rule to allow ping requests. If you want to ping an instance, add a stateful ingress rule to specifically allow ICMP traffic type 8 from the source network you plan to ping from. To allow ping access from the internet, use 0.0.0.0/0 for the source. Note that this rule for pinging is separate from the default ICMP-related rules in the default security list. Don't remove those rules.
  * **Do not delete default security rules indiscriminately**
Your VCN might have subnets that use the default security list by default. Don't delete any of the list's default security rules unless you have first confirmed that resources in your VCN don't require them. Otherwise, you might disrupt your VCN connectivity.
  * **If necessary, add rules to allow ping requests**
There is no default rule to allow ping requests. If you want to ping an instance, add a stateful ingress rule to specifically allow ICMP traffic type 8 from the source network you plan to ping from. To allow ping access from the internet, use 0.0.0.0/0 for the source. Note that this rule for pinging is separate from the default ICMP-related rules in the default security list. Don't remove those rules.
  * **If necessary, add rules to handle fragmented UDP packets**
Instances can send or receive UDP traffic. If a UDP packet is too large for the connection, it's fragmented. However, only the first fragment from the packet contains the protocol and port information. If the security rules that allow this ingress or egress traffic specify a particular (source or destination) port number, the fragments after the first one are dropped. If you expect your instances to send or receive large UDP packets, set both the source and destination ports for the applicable security rules to ALL instead of a particular port number.
  * **Align OS firewall rules with security rules**
Your instances running images provided with Compute Cloud@Customer also have OS firewall rules that control access to the instance. When troubleshooting access to an instance, ensure that all the following items are set correctly:
    * The rules in the network security groups that the instance is in
    * The rules in the security lists associated with the instance's subnet
    * The instance's OS firewall rules


Was this article helpful?
YesNo

