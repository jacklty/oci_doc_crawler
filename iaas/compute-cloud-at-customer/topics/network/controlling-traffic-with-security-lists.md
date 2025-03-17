Updated 2024-04-02
# Controlling Traffic with Security Lists
On Compute Cloud@Customer, both security lists and network security groups (NSGs) are types of virtual firewalls for your compute instances. Both security lists and NSGs define network security rules that decide which types of traffic are allowed in and out of instances (VNICs).
Security lists provide virtual firewall rules to all the VNICs in a subnet. To provide a set of firewall rules for a set of VNICs of your choice in a VCN, you can create an NSG. See [Controlling Traffic with Network Security Groups](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-network-security-groups.htm#controlling-traffic-with-network-security-groups "On Compute Cloud@Customer, both network security groups \(NSGs\) and security lists are types of virtual firewalls for your compute instances. Both NSGs and security lists define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).").
Security lists enable you to define network security rules that apply to all VNICs in a subnet. A default security list is automatically created for each VCN. That default security list is assigned to each subnet in the VCN if you don't assign a different security list. Up to five security lists can be associated with a subnet.
If you use both security lists and NSGs, traffic in or out of a given VNIC is allowed if any rule in any applicable security list or NSG allows the traffic:
  * Any rule in any security list that's associated with the VNIC subnet
  * Any rule in any NSG that the VNIC is in


Was this article helpful?
YesNo

