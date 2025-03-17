Updated 2023-09-28
# Virtual Firewall
On Compute Cloud@Customer, the Networking service offers two virtual firewall features that both use security rules to control traffic at the packet level – security lists and network security groups (NSGs). They offer different ways to apply security rules to a set of virtual network interface cards (VNICs).
  * **Security lists:**
A security list defines security rules at the subnet level, which means that all VNICs in a particular subnet are subject to the same rules. Each VCN comes with a default security containing default rules for essential traffic. The default security list is automatically used with all subnets, unless a custom security list is specified. A subnet can have up to five associated security lists.
  * **Network security groups (NSGs):**
A network security group defines security rules based on membership. Its security rules apply to resources that are explicitly added to the NSG. A VNIC can be added to a maximum of five NSGs. An NSG is intended to provide a virtual firewall for a set of cloud resources with the same security posture. For example: a group of instances that perform the same tasks and thus need to use the same set of ports.


Oracle recommends using NSGs instead of security lists because NSGs let you separate the VCN subnet architecture from your application security requirements. However, NSGs are only supported for specific services. It is possible to use both security lists and NSGs together, depending on your particular security needs.
If you have security rules that you want to enforce for all VNICs in a VCN, the easiest solution is to put the rules in one security list, and then associate that security list with all subnets in the VCN. This way you can ensure that the rules are applied, regardless of who in your organization creates a VNIC in the VCN. Or, you can add the required security rules to the VCN default security list.
If you choose to combine security lists and network security groups, the set of rules that applies to a particular VNIC is the union of these items:
  * The security rules in the security lists associated with the VNIC subnet
  * The security rules in all NSGs that the VNIC is in


A packet in question is allowed if _any rule_ in any of the relevant lists and groups allows the traffic, or if the traffic is part of an existing connection being tracked because of a stateful rule.
Was this article helpful?
YesNo

