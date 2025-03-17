Updated 2023-09-26
# Configuring VNICs
On Compute Cloud@Customer, the compute nodes have physical network interface cards (NICs). When you create a compute instance, the Networking service ensures that a VNIC is created on top of a physical interface, so that the instance can communicate over the network.
Each instance has a primary VNIC that's automatically created and attached. The primary VNIC resides in the subnet you specify when creating the instance. It can't be removed from the instance.
A VNIC enables an instance to connect to a VCN and determines how the instance communicates with endpoints inside and outside of the VCN. Each VNIC resides in a subnet within a VCN and includes these items:
  * One primary private IPv4 address from the subnet the VNIC is in.
  * Up to 31 optional private IPv4 addresses from the subnet the VNIC is in.
  * An optional public IPv4 address for each private IP, assigned at your discretion.
  * An optional host name for DNS for each private IP address.
  * A MAC address.
  * A flag to enable or disable the source/destination check on the VNIC network traffic.
  * Optional membership of one or more network security groups (NSGs).
  * An Oracle-assigned identifier (OCID).
  * An optional friendly name you can choose and assign.


You can add secondary VNICs to an instance after the instance is created. To be able to use a secondary VNIC, you must also configure the instance OS for it. The maximum number of VNICs for an instance varies by shape. Each secondary VNIC can be in a different subnet than the primary VNIC, either within the same VCN or a different one. A secondary VNIC can also be in the same subnet as the primary VNIC. However, attaching multiple VNICs from the same subnet CIDR block to an instance can introduce asymmetric routing, especially on Linux instances.
**Note**
To avoid asymmetric routing in a configuration with multiple IP addresses from the same subnet, Oracle recommends assigning multiple private IP addresses to one VNIC, or using policy-based routing.
If traffic comes in to a service on the instance through a secondary VNIC and the service replies, the reply packets automatically have that VNIC IP address as the source IP address. Policy-based routing is required for that reply to go back out on the same interface and find the correct default gateway.
Secondary VNICs must always be attached to an instance and can't be moved. The process of creating a secondary VNIC automatically attaches it to the instance. The process of detaching a secondary VNIC automatically deletes it. They're automatically detached and deleted when you delete the instance. An instance's bandwidth is fixed regardless of the number of VNICs attached. You can't specify a bandwidth limit for a particular VNIC on an instance.
By default, every VNIC performs the source/destination check on its network traffic. The VNIC looks at the source and destination listed in the header of each network packet. If the VNIC isn't the source or destination, then the packet is dropped. If the VNIC needs to forward traffic – for example, if it needs to perform Network Address Translation (NAT) – you must disable the source/destination check on the VNIC.
VNICs reside in a subnet but attach to an instance. The VNIC attachment to the instance is a separate object from the VNIC or the instance itself. The VNIC and subnet always exist together in the same compartment, but the VNIC attachment to the instance always exists in the instance's compartment. This distinction affects your IAM policies if you set up an access control scenario where network administrators manage the network and other users manage instances.
VNICs are rate limited to prevent very active applications from reducing the available bandwidth of other applications to unacceptable levels. Rate limiting applies to each instance’s VNIC interface. 
The rate is limited to a value below the maximum network bandwidth associated with each instance shape. Generally, the bandwidth limit increases with the maximum number of VNICs a shape uses, but there is no maximum bandwidth guarantee. 
You can't specify the bandwidth limits directly. Rate limiting is a system function. The rate applied to each VNIC is based on the shape option during instance creation. 
Was this article helpful?
YesNo

