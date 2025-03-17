Updated 2025-02-21
# Managing Private IP Addresses
On Compute Cloud@Customer, a private IP address enables communication with resources on the VCN. 
Each instance has at least one private IP address, and optionally, one or more public IP addresses.
The Networking service defines a private IP object, identified by an OCID, which consists of a private IPv4 address and optional host name for DNS. Each instance receives a primary private IP object during creation. The Networking service uses DHCP to assign a private IP address. This address doesn't change during the instance's lifetime and can't be removed from the instance. The private IP object is deleted when the instance is deleted.
If an instance has any secondary VNICs attached, each of those VNICs also has a primary private IP. A private IP can have a public IP assigned to it at your discretion. You can't use a private IP as the target of a route rule in a VCN.
## Secondary Private IPs 🔗 
After an instance is created, you can add a _secondary private IP_ to one of its VNICs. You can add it to either the primary VNIC or a secondary VNIC on the instance. The secondary private IP address must be in the subnet to which the VNIC belongs. You can move a secondary private IP from a VNIC on one instance to a VNIC on another instance on condition that both VNICs belong to the same subnet. 
Typical use cases for a secondary private IP include:
  * **Instance failover:** You assign a secondary private IP to an instance. If a problem occurs with the instance, you can easily reassign its secondary private IP to a standby instance in the same subnet. In addition, if the secondary private IP has an associated public IP, that public IP moves along with the private IP. 
  * **Running multiple services or endpoints on a single instance:** For example, you could have an instance that runs multiple container pods, where each pod uses its own IP address from the VCN CIDR. The containers have direct connectivity to other instances and services in the VCN. Another example: you could run multiple SSL web servers with each one using its own IP address.


Secondary private IP addresses have the following properties:
  * They're supported for all shapes and OS types.
  * They can be assigned only after the instance is created, or the secondary VNIC is created and attached.
  * They're automatically deleted when you delete the instance or detach and delete the secondary VNIC. 
  * Deleting a secondary private IP from a VNIC returns the address to the pool of available addresses in the subnet.
  * A VNIC can have a maximum of 32 secondary private IPs.
  * The instance's bandwidth is fixed regardless of the number of private IP addresses attached. You can't specify a bandwidth limit for a particular IP address on an instance.
  * A secondary private IP can have a reserved public IP associated with it at your discretion.


**Note**
After assigning a secondary private IP to a VNIC, you must configure the instance OS to use it. See [Configuring the Instance OS for a Secondary IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/configuring-the-instance-os-for-a-secondary-ip-address.htm#configuring-the-instance-os-for-a-secondary-ip-address "On Compute Cloud@Customer, after you create a secondary private IP address on a VNIC, sign in to the instance to configure the instance OS to use the new IP address.")
Was this article helpful?
YesNo

