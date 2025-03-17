Updated 2023-09-28
# Managing Public IP Addresses
On Compute Cloud@Customer, a public IP address enables communication outside the VCN, including to the data center network.
All of the following network configurations are required for an instance to communicate outside the VCN:
  * The instance must be in a public subnet, which is configured when the subnet is created. Private subnets can't have a public IP address assigned to instances in the subnet.
  * The instance must have a public IP address.
  * The instance's VCN must have an internet gateway configured.
  * The public subnet must have route table and security list entries that enable communications outside the VCN.


When you create an instance with a public IP address, the instance is assigned a public IP address from an address pool. Technically, the assignment is to a private IP object on the instance, and the VNIC that the private IP is assigned to must reside in a public subnet. An instance can have multiple secondary VNICs; each with a (primary) private IP. Consequently, you can assign an instance multiple public IPs across their VNICs.
The Networking service defines a public IP object, identified by an OCID, which consists of a private IPv4 address and additional properties that further define the public IP type and behavior. There are two types of public IPs: 
  * An **ephemeral** public IP is temporary and exists for the lifetime of the instance.
  * A **reserved** public IP is persistent and exists beyond the lifetime of the instance it is assigned to. It can be unassigned and then reassigned to another instance.


The following table summarizes the differences between both types of IP addresses:
Characteristics  |  Ephemeral Public IP |  Reserved Public IP  
---|---|---  
Allowed assignment |  to a VNIC primary private IP limits: one per VNIC, two per instance |  to a VNIC primary private IP limit: one per VNIC  
Creation |  Optionally created and assigned during instance creation or secondary VNIC creation. You can create and assign one later if the VNIC doesn't already have one. |  You create one at any time. You can then assign it when you like.  
Unassignment |  You can unassign it at any time, which deletes it. You might do this if whoever created the instance included a public IP, but you do not want the instance to have one. When you stop an instance, its ephemeral public IPs remain assigned to the instance. |  You can unassign it at any time, which returns it to the tenancy's pool of reserved public IPs.  
Moving to a different resource |  You can't move an ephemeral public IP to a different private IP. |  You can move it at any time by unassigning and then reassigning it to another private IP. Can be in a different VCN or availability domain.  
Automatic deletion |  Its lifetime is tied to the private IP lifetime. Automatically unassigned and deleted when:
  * its private IP is deleted
  * its VNIC is detached or deleted
  * its instance is deleted

|  Never. Exists until you delete it.  
Scope |  Availability domain |  Regional (can be assigned to a private IP in any availability domain in the region)  
Compartment and availability domain |  Same as the private IPs |  Can be different from the private IPs  
When you create an instance in a public subnet, the instance gets a public IP by default, unless you specify otherwise. After you create a public IP, you can't change which type it is. For example, if you create an instance that is assigned an ephemeral public IP with address 203.0.113.2, you can't convert the ephemeral public IP to a reserved public IP with address 203.0.113.2.
Resources that are designed to be directly publicly reachable automatically get a public IP address assigned from a pool upon creation. For NAT gateways, the assigned address is a regional ephemeral public IP. As with other ephemeral public IPs, it is automatically unassigned and deleted when you delete its assigned resource. However, unlike other ephemeral public IPs, you can't edit it or unassign it yourself.
Was this article helpful?
YesNo

