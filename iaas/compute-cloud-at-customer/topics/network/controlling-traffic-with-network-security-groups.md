Updated 2024-04-02
# Controlling Traffic with Network Security Groups
On Compute Cloud@Customer, both network security groups (NSGs) and security lists are types of virtual firewalls for your compute instances. Both NSGs and security lists define network security rules that decide which types of traffic are allowed in and out of instances (VNICs).
NSGs provide virtual firewall rules for a set of VNICs of your choice in a VCN. To provide a set of firewall rules for all VNICs in a subnet, you can create a security list. See [Controlling Traffic with Security Lists](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-security-lists.htm#controlling-traffic-with-security-lists "On Compute Cloud@Customer, both security lists and network security groups \(NSGs\) are types of virtual firewalls for your compute instances. Both security lists and NSGs define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).").
NSGs enable you to define network security rules for groups of instances, which can be in different subnets. For example, an NSG can apply to all the database servers, or to all the application servers running a certain application. Instead of applying security to a particular subnet, you create an NSG and then add the appropriate instances (VNICs) to the NSG.
When you create a VCN, a default security list is created. No default NSG is created because you must choose which VNICs to include in the group.
If you use both security lists and NSGs, traffic in or out of a particular VNIC is allowed if any rule in any applicable security list or NSG allows the traffic:
  * Any rule in any security list that's associated with the VNIC subnet
  * Any rule in any NSG that the VNIC is in


Was this article helpful?
YesNo

