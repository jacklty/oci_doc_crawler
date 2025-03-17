Updated 2024-12-10
# Security Rules
The Networking service offers two virtual firewall features that both use _security rules_ to control traffic at the packet level. The two features are:
  * **Security lists:** The original virtual firewall feature from the Networking service.
  * **Network security groups (NSGs):** A subsequent feature designed for application components that have different security postures. NSGs are supported only for [specific services](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#support).


These two features offer different ways to apply security rules to a set of **virtual network interface cards (VNICs)** in the Virtual Cloud Network (VCN).
This topic summarizes basic differences between the two features. It also explains important security rule concepts that you need to understand. How you create, manage, and apply security rules varies between security lists and network security groups. For implementation details, see these related topics:
  * [Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists)
  * [Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups)


**Note** You can use Zero Trust Packet Routing (ZPR) along with or in place of network security groups to control network access to OCI **resources** by applying security attributes to them and creating ZPR policies to control communication among them. For more information, see [Zero Trust Packet Routing](https://docs.oracle.com/iaas/Content/zero-trust-packet-routing/home.htm). 
**Caution** If an endpoint has a ZPR security attribute, traffic to the endpoint must satisfy ZPR rules as well as all NSG and security list rules. For example, if you're already using NSGs and you apply a security attribute to an endpoint, as soon as the attribute is applied, all traffic to the endpoint is blocked. From then onward, a ZPR policy must allow traffic to the endpoint.
## Comparison of Security Lists and Network Security Groups 🔗 
_Security lists_ let you define a set of security rules that applies to all the VNICs in an entire _subnet_. To use a given security list with a particular subnet, you _associate_ the security list with the subnet either during subnet creation or later. A subnet can be associated with a maximum of five security lists. Any VNICs that are created in that subnet are subject to the security lists associated with the subnet.
_Network security groups_ (NSGs) let you define a set of security rules that applies to a _group of VNICs of your choice_ (or the VNICs' [parent resources such as load balancers or DB systems](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison)). For example: the VNICs that belong to a set of compute instances that all have the same security posture. To use a given NSG, you add the VNICs of interest to the group. Any VNICs added to that group are subject to that group's security rules. A VNIC can be added to a maximum of five NSGs.
The following table summarizes the differences.
Security tool | Applies to  | To enable | Limitations  
---|---|---|---  
Security lists | All VNICs in a subnet using that security list | Associate the security list with the subnet | Maximum five security lists per subnet  
Network security groups | Chosen VNICs in the same VCN  | Add specific VNICs to the NSG | Maximum five NSGs per VNIC   
**Oracle recommends using NSGs instead of security lists because NSGs let you separate the VCN's subnet architecture from your application security requirements.**
However, you can use both security lists and NSGs together if you want. For more information, see [If You Use Both Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#use_both).
### About VNICs and Parent Resources 🔗 
A [VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs) is a Networking service component that enables a networked resource such as a compute instance to connect to a Virtual Cloud Network (VCN). The VNIC determines how the instance connects with endpoints inside and outside the VCN. Each VNIC resides in a subnet in a VCN.
When you create a compute instance, a VNIC is automatically created for the instance in the instance's subnet. The instance is considered to be the _parent resource_ for the VNIC. You can add more (secondary) VNICs to a compute instance. For this reason, an instance's VNICs are displayed prominently as part of a compute instance's related resources in the Console.
There are other types of parent resources that you can create that also result in a VNIC automatically being created. For example: when you create a load balancer, the Load Balancer service automatically creates VNICs for balancing traffic across the backend set. Also, when you create a DB system, the Database service automatically creates VNICs as DB system nodes. Those services create and manage those VNICs for you. For this reason, those VNICs are not readily apparent in the Console the same way VNICs are for compute instances. 
To use an NSG, you put VNICs of your choice into the group. However, you typically work _with the parent resource_ when you add a VNIC to the group, not the VNIC itself. For example, when you create a compute instance, you can optionally specify an NSG for the instance. Although you conceptually put the instance in the group, you're actually putting the instance's _primary VNIC_ in the network security group. The group's security rules apply to that VNIC, not the instance. Also, if you add a secondary VNIC to the instance, you can optionally specify an NSG for that VNIC, and the rules apply to that VNIC, not the instance. Note that all the VNICs in a given NSG must be in the VCN that the NSG belongs to.
Likewise, when you put a load balancer in a network security group, you conceptually put the load balancer in the group. But you're actually putting VNICs managed by the Load Balancer service into the network security group.
You manage the VNIC membership of an NSG _at the parent resource_ , and not at the NSG itself. In other words, to add a parent resource to an NSG, you execute the action on the _parent resource_ (by specifying which NSGs the parent resource should be added to). You do not execute the action on the NSG (by specifying which VNICs or parent resources should be added to the NSG). Similarly, to remove a VNIC from an NSG, you execute that action by updating the parent resource, not the NSG. For example, to add an existing compute instance's VNIC to an NSG, you update that VNIC's properties and specify the NSG. For example, with the REST API, you call `UpdateVnic`. In the Console, you view the instance and then the VNIC of interest, and then edit the VNIC's properties there.
For a list of parent resources that support the use of NSGs, see [Support for Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#support).
### Network Security Group as Source or Destination of a Rule 🔗 
There's an important difference in how you can write security rules for NSGs compared to security lists.
When writing rules for an NSG, you can specify an _NSG_ as the source of traffic (for ingress rules) or the traffic's destination (for egress rules). Contrast this with security list rules, where you specify a _CIDR_ as the source or destination. 
The ability to specify an NSG means that you can easily write rules to control traffic between two different NSGs. The NSGs must be in the same VCN.
Also, if you want to control traffic between _VNICs in a specific NSG_ , you can write rules that specify the _rule's own NSG_ as the source (for ingress rules) or destination (for egress rules). 
For more information, see [Overview of Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#overview).
### REST API Differences
There are a few basic differences in the REST API model for NSGs compared to security lists. For more information, see [Using the API](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#api).
### Default Rules
Your VCN automatically comes with a [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) that contains several default security rules to help you get started using the Networking service. When you create a subnet, the default security list is associated with the subnet unless you specify a custom security list that you've already created in the VCN. 
For comparison, the VCN does NOT have a default network security group.
### Limits 🔗 
The two features have different limits. See [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm) for a list of applicable limits and instructions for requesting a limit increase.
[Security List Limits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)
Resource |  Scope |  Oracle Universal Credits |  Pay As You Go or Trial  
---|---|---|---  
Security lists | VCN | 300 | 300  
Security lists | Subnet | 5* | 5*  
Security rules | Security list |  200 ingress rules* and 200 egress rules* |  200 ingress rules* and 200 egress rules*  
* Limit for this resource cannot be increased  
[Network Security Group Limits](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm)
Resource | Scope | Oracle Universal Credits | Pay As You Go or Trial  
---|---|---|---  
Network security groups | VCN | 1000 | 1000  
VNICs | Network security group |  A given network security group can have as many VNICs as are in the VCN. A given VNIC can belong to a maximum of 5 network security groups.* |  A given network security group can have as many VNICs as are in the VCN. A given VNIC can belong to a maximum of 5 network security groups.*  
Security rules | Network security group |  120 (total ingress plus egress) |  120 (total ingress plus egress)  
* Limit for this resource cannot be increased  
## Best Practices for Security Rules 🔗 
### Use Network Security Groups
Oracle recommends using NSGs for components that all have the same security posture. For example, in a multi-tier architecture, you would have a separate NSG for each tier. A given tier's VNICs would all belong to that tier's NSG. Within a given tier, you might have a particular subset of the tier's VNICs that have additional, special security requirements. Therefore you would create another NSG for those additional rules, and place that subset of VNICs into both the tier's NSG and the additional NSG.
Oracle also recommends using NSGs because Oracle will prioritize NSGs over security lists when implementing future enhancements. 
### Get Familiar with the Default Security List Rules
Your VCN automatically comes with a [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) that contains several default security rules to help you get started using the Networking service. Those rules exist because they enable basic connectivity. Even if you choose not to use security lists or the default security list, get familiar with the rules so you better understand the types of traffic that your networked cloud resources require. You might want to use those rules in your NSGs or any custom security lists that you set up.
The default security list does not include rules to enable ping. If you need to use ping, see [Rules to Enable Ping](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#ping).
### Don't Delete Default Security Rules Indiscriminately
Your VCN might have subnets that use the default security list by default. Do not delete any of the list's default security rules unless you've first confirmed that resources in your VCN do not require them. Otherwise, you might disrupt your VCN's connectivity.
### Confirm That Your OS Firewall Rules Align with Your Security Rules
Your instances running [platform images](https://docs.oracle.com/iaas/Content/Compute/References/images.htm) also have OS firewall rules that control access to the instance. When troubleshooting access to an instance, ensure that all of the following items are set correctly:
  * The rules in the network security groups that the instance is in
  * The rules in the security lists associated with the instance's subnet
  * The instance's OS firewall rules


If your instance is running Oracle Autonomous Linux 8.x, Oracle Autonomous Linux 7, Oracle Linux 8, Oracle Linux 7, or Oracle Linux Cloud Developer 8, you need to use [firewalld](https://oracle-base.com/articles/linux/linux-firewall-firewalld) to interact with the iptables rules. For your reference, here are commands for opening a port (1521 in this example):
Copy
```
sudo firewall-cmd --zone=public --permanent --add-port=1521/tcp
								
sudo firewall-cmd --reload
```

For instances with an iSCSI boot volume, the preceding `--reload` command can cause problems. For details and a workaround, see [Instances experience system hang after running firewall-cmd --reload](https://docs.oracle.com/iaas/Content/Compute/known-issues.htm#firewallReload).
### Use VNIC Metrics to Troubleshoot Packets Dropped Because of Security Rules
The Networking service offers [metrics for VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/networkmetrics.htm#Networking_Metrics), which show the levels of VNIC traffic (packets and bytes). Two of the metrics are for ingress and egress packets that violate security rules and are therefore dropped. You can use these metrics to help you troubleshoot issues related to security rules and whether your VNICs are receiving the desired traffic.
## If You Use Both Security Lists and Network Security Groups 🔗 
You can use security lists alone, network security groups alone, or both together. It depends on your particular security needs.
If you have security rules that you want to enforce for _all VNICs in a VCN_ : the easiest solution is to put the rules in one security list, and then associate that security list with all subnets in the VCN. This way you can ensure that the rules are applied, regardless of who in your organization creates a VNIC in the VCN. If you like, you can use the VCN's [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default), which automatically comes with the VCN and contains a set of essential rules by default. 
If you choose to use _both_ security lists and network security groups, the set of rules that applies to a given VNIC is the union of these items:
  * The security rules in the security lists associated with the VNIC's subnet
  * The security rules in all NSGs that the VNIC is in


The following diagram is a simple illustration of the idea.
[![A VNIC is subject to the rules in all the network security groups it's in and all the security lists associated with its subnet.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_nsg_vnic_view.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_nsg_vnic_view.svg)
A packet in question is allowed if _any rule in any of the relevant lists and groups_ allows the traffic (or if the traffic is part of an existing [connection being tracked](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful)). There's a caveat if the lists happen to contain both stateful and stateless rules that cover the same traffic. For more information, see [Stateful Versus Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful).
## Parts of a Security Rule 🔗 
A security rule **allows** a particular type of traffic in or out of a VNIC. For example, a commonly used security rule allows ingress TCP port 22 traffic for establishing SSH connections to the instance (more specifically to the instance's VNICs). Without security rules, no traffic is allowed in and out of VNICs in the VCN.
**Note** Security rules aren't enforced for traffic involving the 169.254.0.0/16 CIDR block, which includes services such as iSCSI and instance metadata.
Each security rule specifies the following items:
  * **Direction (ingress or egress):** Ingress is inbound traffic to the VNIC, and egress is outbound traffic from the VNIC. The REST API model for security lists is different from network security groups. Security lists have an `IngressSecurityRule` object and a separate `EgressSecurityRule` object. Network security groups have only a `SecurityRule` object, and the object's `direction` attribute determines whether the rule is for ingress or egress traffic.
  * **Stateful or stateless:** If stateful, connection tracking is used for traffic matching the rule. If stateless, no connection tracking is used. See [Stateful Versus Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful).
  * **Source type and source (ingress rules only):** The source you provide for an ingress rule depends on the source type you select. 
Allowed source types 
Source Type | Allowed Source  
---|---  
CIDR | The CIDR block where the traffic originates from. Use 0.0.0.0/0 to indicate all IP addresses. The prefix is required (for example, include the /32 if specifying an individual IP address). For more information about CIDR notation, see [RFC1817](https://datatracker.ietf.org/doc/html/rfc1817) and [RFC1519](https://datatracker.ietf.org/doc/html/rfc1519).  
Network Security Group |  An NSG in the same VCN as this rule's NSG. This source type is available only if the rule belongs to an NSG and not a security list.  
Service |  Only for packets coming from an Oracle service through a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway). If a service gateway isn't present in your VCN, traffic coming from the public IP of an OSN endpoint can route to a VCN via a NAT gateway or an internet gateway. The traffic still traverses the OCI backbone to your VCN. The source service is the [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that you're interested in.  
  * **Destination type and destination (egress rules only):** The destination you provide for an egress rule depends on the destination type you choose.
Allowed destination types 
Destination Type | Allowed Destination  
---|---  
CIDR | The CIDR block where the traffic is destined to. Use 0.0.0.0/0 to indicate all IP addresses. The prefix is required (for example, include the /32 if specifying an individual IP address). For more information about CIDR notation, see [RFC1817](https://datatracker.ietf.org/doc/html/rfc1817) and [RFC1519](https://datatracker.ietf.org/doc/html/rfc1519).  
Network Security Group |  An NSG that is in the same VCN as this rule's NSG. This destination type is available only if the rule belongs to an NSG and not a security list.  
Service |  Only for packets going to an Oracle service (such as object storage) through a [service gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#Access_to_Oracle_Services_Service_Gateway). If a service gateway isn't present in your VCN, traffic destined to the public IP of an OSN endpoint can route to OSN via a NAT gateway or an internet gateway. Routing through a service gateway allows you to select which Oracle Services Network (OSN) endpoints you want to route traffic to (choose from **Only Object Storage** or **All Services**). The destination service is the OSN [service CIDR label](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/servicegateway.htm#overview) that you're interested in.  
  * **IP Protocol:** Either a single [IPv4 protocol](http://www.iana.org/assignments/protocol-numbers/protocol-numbers.xhtml) or "all" to cover all protocols. 
  * **Source port:** The port where the traffic originates from. For TCP or UDP, you can specify all source ports, or optionally specify a single source [port number](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), or a range. 
  * **Destination port:** The port where the traffic is destined to. For TCP or UDP, you can specify all destination ports, or optionally specify a single destination [port number](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml), or a range. 
  * **ICMP type and code:** For ICMP, you can specify all types and codes, or optionally specify a single [ICMP type](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) with an optional code. If the type has multiple codes, create a separate rule for each code you want to allow. 
  * **Description** (NSG rules only): NSG security rules include an optional attribute where you can provide a friendly description of the rule. This is currently not supported for security list rules.


For examples of security rules, see [Networking Scenarios](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/scenarios.htm#networking_scenarios).
For the limit on the number of rules you can have, see [Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison).
**Note** If you're using NSGs, and two VNICs that are in the same VCN need to communicate _using their public IP addresses_ , you must use the VNIC's public IP address and not the VNIC's NSG as the source (for ingress) or destination (for egress) in the relevant security rules. The packet is routed to the VCN's internet gateway, and at that point, the VNIC's NSG information is not available. Therefore a security rule that specifies the NSG as the source or destination will be ineffective in allowing that specific type of traffic.
## Stateful Versus Stateless Rules 🔗 
When you create a security rule, you choose whether it's _stateful_ or _stateless_. The difference is described in the next sections. The default is stateful. Stateless rules are recommended if you have a high-volume internet-facing website (for the HTTP/HTTPS traffic).
This section refers specifically to compute instances and their traffic. However, the discussion is applicable to all types of resources with VNICs. See [Comparison of Security Lists and Network Security Groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#comparison).
### Stateful Rules
Marking a security rule as stateful indicates that you want to use connection tracking for any traffic that matches that rule. This means that when an instance receives traffic matching the stateful ingress rule, the response is tracked and automatically allowed back to the originating host, regardless of any egress rules applicable to the instance. And when an instance sends traffic that matches a stateful egress rule, the incoming response is automatically allowed, regardless of any ingress rules. 
For example, you could have a stateful ingress security rule for an instance (Instance A) that needs to receive and respond to HTTP traffic from Host B. Host B could be any host, whether an instance or not. Instance A and Host B are communicating because the stateful ingress rule allows traffic from any source IP address (0.0.0.0/0) to destination port 80 only (TCP protocol). No egress rule is required to allow the response traffic since responses are automatically tracked and allowed. 
[![Stateful ingress rule allowing incoming HTTP traffic and response](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_stateful_sec_list.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_stateful_sec_list.svg)
**Note**
Stateful rules store information in a connection tracking table on each compute instance. The size of that table is specific to the compute shape being used (see the service limits page for [Connection Tracking](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#connection-tracking)). When the connection tracking table is full, new state information can't be added and new connections will experience packet loss. Using a larger compute shape will allow you to have a larger table, but that may not be enough to prevent packet loss when using stateful rules. 
If your subnet has a high traffic volume, Oracle recommends using stateless rules instead of stateful rules.
### Stateless Rules
Marking a security rule as stateless indicates that you do NOT want to use connection tracking for any traffic that matches that rule. This means that response traffic is not automatically allowed. To allow the response traffic for a stateless ingress rule, you must create a corresponding stateless egress rule. 
The next figure shows Instance A and Host B as before, but now with stateless security rules. As with the stateful rule in the preceding section, the stateless ingress rule allows traffic from all IP addresses and any ports, on destination port 80 only (using the TCP protocol). To allow the response traffic, there needs to be a corresponding stateless egress rule that allows traffic to any destination IP address (0.0.0.0/0) and any ports, from source port 80 only (using the TCP protocol). 
[![Stateless ingress and egress rules allowing incoming HTTP traffic and response](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_stateless_sec_list_receive.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_stateless_sec_list_receive.svg)
If Instance A needs instead to _initiate_ HTTP traffic and get the response, then a different set of stateless rules are required. As the next figure shows, the egress rule would have source port = all and destination port = 80 (HTTP). The ingress rule would then have source port 80 and destination port = all. 
[![Stateless ingress and egress rules allowing instance to initiate HTTP traffic and get response](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_stateless_sec_list_initiate.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_stateless_sec_list_initiate.svg)
If you were to use port binding on Instance A to specify exactly which port the HTTP traffic would come from, you could specify that as the source port in the egress rule and the destination port in the ingress rule. 
**Note**
If for some reason you use both stateful and stateless rules, and there's traffic that matches both a stateful and stateless rule in a particular direction (for example, ingress), the stateless rule takes precedence and the connection is not tracked. You would need a corresponding rule in the other direction (for example, egress, either stateless or stateful) for the response traffic to be allowed.
### Connection Tracking Details for Stateful Rules 🔗 
Oracle uses connection tracking to allow responses for traffic that matches stateful rules (see [Stateful Versus Stateless Rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#stateful)). Each instance has a [maximum number of concurrent connections](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#connection-tracking) that can be tracked, based on the instance's **shape**. 
To determine response traffic for TCP, UDP, and ICMP, Oracle performs connection tracking on these items for the packet:
  * Protocol
  * Source and destination IP addresses
  * Source and destination ports (for TCP and UDP only)


**Note**
For other protocols, Oracle tracks only the protocol and IP addresses, and not the ports. This means that when an instance initiates traffic to another host and that traffic is allowed by egress security rules, any traffic that the instance receives later from that host for a period is considered response traffic and is allowed.
Tracked connections are maintained as long as traffic is received for the connection. If a connection idles long enough, it will timeout and be removed. Once removed, responses for a stateful security rule will be dropped. The following table shows the default idle timeouts: 
Idle timeouts Protocol | State | Idle timeout  
---|---|---  
TCP | Established | 1 day  
TCP | Setup | 1 minute  
TCP | Closure | 2 minutes  
UDP | Established (this means a packet received in both directions) | 3 minutes  
UDP | Not established (packet received only in one direction) | 30 seconds  
ICMP | N/A | 15 seconds  
Other | N/A | 5 minutes  
### Enabling Path MTU Discovery Messages for Stateless Rules 🔗 
If you decide to use stateless security rules to allow traffic to/from endpoints outside the VCN, it's important to add a security rule that allows ingress ICMP traffic type 3 code 4 from source 0.0.0.0/0 and any source port. This rule enables your instances to receive Path MTU Discovery fragmentation messages. This rule is critical for establishing a connection to your instances. Without it, you can experience connectivity issues. For more information, see [Hanging Connection](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/connectionhang.htm#Hanging_Connection).
## Rules to Enable Ping 🔗 
The VCN's [default security list](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Default) contains several default rules, but not one to allow ping requests. If you want to ping an instance, ensure that the instance's applicable security lists or NSGs include an _additional_ stateful ingress rule to specifically allow ICMP traffic type 8 from the source network you plan to ping from. To allow ping access from the internet, use 0.0.0.0/0 for the source. Note that this rule for pinging is separate from the default ICMP-related rules in the default security list. Do not remove those rules.
## Rules to Handle Fragmented UDP Packets 🔗 
Instances can send or receive UDP traffic. If a UDP packet is too large for the connection, it is fragmented. However, only the first fragment from the packet contains the protocol and port information. If the security rules that allow this ingress or egress traffic specify a particular port number (source or destination), the fragments after the first one are dropped. If you expect your instances to send or receive large UDP packets, set both the source and destination ports for the applicable security rules to ALL (instead of a particular port number).
Was this article helpful?
YesNo

