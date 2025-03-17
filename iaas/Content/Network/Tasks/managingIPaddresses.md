Updated 2025-03-04
# Private IP Addresses
This topic describes how to manage the IPv4 addresses assigned to an instance in a Virtual Cloud Network (VCN).
IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses). 
## Overview of IP Addresses 🔗 
Instances use IP addresses for communication. Each instance has at least one private IP address and optionally one or more public IP addresses. A private IP address lets the instance communicate with other instances inside the VCN, or with hosts in an on-premises network (by using Site-to-Site VPN or Oracle Cloud Infrastructure FastConnect). A public IP address lets the instance communicate with hosts on the internet. For more information, see these related topics:
  * [Public vs. Private Subnets](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Public)
  * [How IP Addresses Are Assigned](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#How)
  * [Public IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#Public_IP_Addresses)


### About the Private IP Object
The Networking service defines an object called a _private IP_ , which consists of:
  * Private IPv4 address, assigned by either you or Oracle.
  * Optional hostname for DNS (see [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network)).
  * Optional association of a private IP address with a custom route table (see [Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing)).


Each private IP object has an Oracle-assigned OCID (see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)). If you're using the API, you can also assign each private IP object a friendly name.
Each instance receives a _primary private IP_ object during instance creation. The Networking service uses the Dynamic Host Configuration Protocol (DHCP) to pass the object's private IP address to the instance. This address doesn't change during the instance's lifetime and can't be removed from the instance. The private IP object is terminated when the instance is terminated. 
If an instance has any [secondary VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs) attached, each of those VNICs also has a primary private IP. 
A private IP can optionally have a [public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#Public_IP_Addresses) assigned to it. 
A private IP can be the target of a route rule in a VCN. For more information, see [Using a Private IP as a Route Target](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route). 
### About Secondary Private IP Addresses 🔗 
You can add a _secondary private IP_ to a compute instance after its creation. You can add it to either the primary VNIC or a secondary VNIC on the instance. The secondary private IP address must come from the CIDR of the VNIC's subnet. You can move a secondary private IP from a VNIC on one instance to a VNIC on another instance if both VNICs belong to the same subnet. 
Here are a few reasons why you might use secondary private IPs:
  * **Instance failover:** You assign a secondary private IP to an instance. Then if the instance has problems, you can easily reassign that secondary private IP to a standby instance in the same subnet. If the secondary private IP has a public IP assigned to it, that public IP moves along with the private IP. 
  * **Running several services or endpoints on a single instance:** For example, you could have several container pods running on a single instance, and each uses an IP address from the VCN's CIDR. The containers have direct connectivity to other instances and services in the VCN. Another example: you could run several SSL websites with each one using its own IP address. 


Here are more details about secondary private IP addresses:
  * They're supported for all Compute shapes and OS types, for both bare metal and VM instances.
  * A VNIC can have a maximum of 64 private IPv4 addresses: 1 primary private IP address and 63 secondary private IP addresses. A VNIC can also have 32 secondary IPv6 addresses. A VNIC's primary address can be either IPv4 or IPv6 if the subnet is configured for IPv6 addressing.
  * They can be assigned only after the instance is created (or the secondary VNIC is created/attached).
  * A secondary private IP assigned to a VNIC in a [regional subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/Overview_of_VCNs_and_Subnets.htm#Overview "Learn about virtual cloud networks \(VCNs\) and subnets in OCI.") has a null availability domain attribute. Compare this with the VNIC's _primary_ private IP, which always has its availability domain attribute set to the instance's availability domain, regardless of whether the instance's subnet is regional or AD-specific.
  * Deleting a secondary private IP from a VNIC returns the address to the pool of available addresses in the subnet.
  * They're automatically deleted when you terminate the instance (or detach/delete the secondary VNIC). 
  * The instance's bandwidth is fixed regardless of the number of private IP addresses attached. You can't specify a bandwidth limit for a particular IP address on an instance.
  * A secondary private IP can have a [reserved public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#Public_IP_Addresses) assigned to it. 


### IP Address Information in the Instance Metadata
The [instance metadata](https://docs.oracle.com/iaas/Content/Compute/Tasks/gettingmetadata.htm) includes information about the private IP addresses at this URL:
Copy
```
http://169.254.169.254/opc/v1/vnics/
```

Here's an example response:
Copy
```
[ {
 "vnicId" : "ocid1.vnic.oc1.sea.<unique_ID>",
 "privateIp" : "10.0.3.6",
 "vlanTag" : 11,
 "macAddr" : "00:00:00:00:00:01",
 "virtualRouterIp" : "10.0.3.1",
 "subnetCidrBlock" : "10.0.3.0/24"
}, {
 "vnicId" : "ocid1.vnic.oc1.sea.<unique_ID>",
 "privateIp" : "10.0.4.3",
 "vlanTag" : 12,
 "macAddr" : "00:00:00:00:00:01",
 "virtualRouterIp" : "10.0.4.1",
 "subnetCidrBlock" : "10.0.4.0/24"
} ]
```

### Required IAM Policy
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 
## Private IP Tasks 🔗 
You can perform the following tasks with private IP addresses:
  * [Assigning a New Secondary Private IP to a VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-create.htm#top "Assign a new secondary private IP address to a VNIC.")
  * [Configuring Linux to Use a Secondary Private IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Linux_Details_about_Secondary_IP_Addresses.htm#Linux "Configure Linux to use a secondary private IP address.")
  * [Configuring Windows to Use a Secondary IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses_topic-Windows_Details_about_Secondary_IP_Addresses.htm#Windows "Configure the Windows OS to use a secondary private IP.")
  * [Moving a Secondary Private IP Address to a Different VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-move-vnic.htm#top "Move a secondary private IP address to another VNIC in the same subnet.")
  * [Listing Private IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-list.htm#top "View a list of all private IP addresses for an instance.")
  * [Getting a Private IP Address's Details](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-address-get.htm#top "View details about a private IP address.")
  * [Editing Private IP Address Information](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-update.htm#top "Update information for a private IP address such as hostname or associated IP type.")
  * [Managing Tags For a Private IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-manage-tags.htm#top "Update tag information for a private IP address.")
  * [Deleting a Private IP Address](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/private-ip-delete.htm#top "Delete a private IP address from a VNIC.")


Was this article helpful?
YesNo

