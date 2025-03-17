Updated 2024-12-16
# Managing VCNs and Subnets
On Compute Cloud@Customer, 
## Virtual Cloud Network (VCN) Overview 🔗 
A virtual cloud network, or VCN, is a software-defined equivalent of a traditional network, with firewall rules and various types of communication gateways. A VCN resides in the single region of and covers one contiguous CIDR block of your choice.
The size of a VCN is /16 to /30. The CIDR block can **NOT** be changed after the VCN is created. The maximum number of private IPs within a VCN is 64,000. Oracle recommends using a private IP address range as specified in [RFC 1918](https://www.rfc-editor.org/rfc/rfc1918) (10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16). This documentation uses the term private IP address when referring to IP addresses in your VCN CIDR.
You can privately connect a VCN to another VCN so that traffic doesn't leave the secure network environment of Compute Cloud@Customer. However, the CIDRs of the two VCNs must not overlap. The concept of privately connecting VCNs is called _peering_. It involves setting up a type of virtual router known as a Local Peering Gateway. For more information about the use of gateways in VCNs, see [Configuring Network Gateways](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/network-gateways.htm#network-gateways "Learn about the different types of gateways you can configure on Compute Cloud@Customer.").
## Subnets 🔗 
A VCN is subdivided into subnets. Each subnet in a VCN consists of a contiguous range of IPv4 addresses that don't overlap with other subnets in the VCN. The first two IPv4 addresses and the last in the subnet CIDR are reserved by the Networking service. You can't change the size of the subnet after creation.
Subnets act as a unit of configuration: all instances in a particular subnet use the same route table, security lists, and DHCP options. Subnets can be either public or private. This is defined when the subnet is created, and can't be changed later. In a private subnet, instances can't be assigned a public IP address.
You can think of a compute instance as residing in a subnet. However, to be precise, each instance is attached to a virtual network interface card (VNIC), which in turn resides in the subnet and enables a network connection for that instance.
Was this article helpful?
YesNo

