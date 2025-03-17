Updated 2025-03-04
# Public IP Addresses
This topic describes how to manage public IPv4 addresses on instances in a Virtual Cloud Network (VCN).
IPv6 addressing is supported for all commercial and government regions. For more information, see [IPv6 Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipv6.htm#IPv6_Addresses). 
## Overview of Public IP Addresses 🔗 
A public IP address is an IPv4 address that is reachable from the internet. If a resource in your tenancy needs to be directly reachable from the internet, it must have a public IP address. Depending on the type of resource, there might be other requirements.
Certain types of resources in your tenancy are designed to be directly reachable from the internet and therefore automatically come with a public IP address. For example: a NAT gateway or a public load balancer. Other types of resources are directly reachable only if you configure them to be. For example: instances in your VCN.
This topic focuses on these subjects:
  * The types of public IP addresses and their characteristics
  * How to control whether an instance has a public IP address


For more information about resources that automatically get a public IP address, see [Resources That Always Get a Public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#overview__Resource).
### Instances and Public IP Addresses
You can assign a public IP address to an instance to enable communication with the internet. The instance is assigned a public IP address from the Oracle Cloud Infrastructure address pool. 
The assignment is actually to a [private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#Private_IP_Addresses) object linked to the instance's VNIC. The [VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs) that the private IP is assigned to must be in a [public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Public). A given instance can have multiple secondary VNICs, and a given VNIC can have multiple secondary private IP addresses. So you can assign a given instance multiple public IP objects across one or more VNICs if you like.
For an instance to communicate directly with the internet, all of the following are required:
  * The instance must be in a [public subnet](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/overview.htm#Public).
  * The instance must have a reserved or ephemeral public IP address.
  * The instance's VCN must have an [internet gateway.](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway)
  * The public subnet must have [route tables](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2) and [security lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) configured accordingly. 


**Tip** Oracle Cloud Infrastructure FastConnect public peering lets your on-premises network access the public IP addresses of resources in Oracle Cloud Infrastructure _without the traffic traversing the internet_. For more information, see [FastConnect](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnect.htm#FC_landing "Oracle Cloud Infrastructure FastConnect provides an easy way to create a dedicated, private connection between your data center and Oracle Cloud Infrastructure.").
### The Public IP Object
The Networking service defines an object called a _public IP_ , which has these attributes:
  * Public IPv4 address (chosen by Oracle)
  * Properties that further define the object's type and behavior. For example, each public IP object has an Oracle-assigned OCID (see [Resource Identifiers](https://docs.oracle.com/iaas/Content/General/Concepts/identifiers.htm)). 
  * An assignment to a private IP address used by an instance VNIC.
  * Optional association of a public IP address with a custom route table (see [Per-resource Routing](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Overview_of_Routing_for_Your_VCN__source_routing)).
  * If you're using the API, you can also assign each public IP object a descriptive name.


The term _public IP_ as used here usually refers to the object and not merely to the IP address it contains.
### Types of Public IPs 🔗 
A public IP can have one of two types:
  * **Ephemeral:** The object is temporary and exists only for the lifetime of the instance.
  * **Reserved:** The object is persistent and exists beyond the lifetime of the instance it's assigned to. You can unassign it and then reassign it to another instance whenever you like. An exception is a reserved public IP on a public load balancers. See [Overview of Public IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingpublicIPs.htm#overview).


The following table summarizes the differences between the two types.
Characteristic | Ephemeral Public IPs | Reserved Public IPs  
---|---|---  
**Allowed assignment** |  To a VNIC's [primary private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#Private_IP_Addresses) only Limits: 
  * One per [VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs)
  * Two per VM instance, and 16 per bare metal instance

|  To either a primary or [secondary private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIPaddresses.htm#overview) Limit: 32 per [VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs)  
**Creation** |  Optionally created and assigned during instance launch or secondary VNIC creation. You can create and assign one later if the VNIC doesn't already have one.  |  You create one at any time. You can then assign it when you like. Limit: You can create 50 per region  
**Unassignment** |  You can unassign it at any time, which deletes it. You might do this if whoever launched the instance included a public IP, but you don't want the instance to have one. When you stop an instance, its ephemeral public IPs remain assigned to the instance. | You can unassign it at any time, which returns it to your tenancy's pool of reserved public IPs.   
**Moving to a different resource** |  You cannot move an ephemeral public IP to a different private IP. |  If assigned to a secondary private IP: If you move the private IP to a different VNIC (must be in the same subnet), the reserved public IP goes with it.  You can move it (unassign and then reassign it) at any time to another private IP in the same region. Can be in a different VCN or availability domain.   
**Automatic deletion** |  Its lifetime is tied to the private IP's lifetime. Automatically unassigned and deleted when:
  * Its private IP is deleted
  * Its VNIC is detached or terminated
  * Its instance is terminated

|  Never. Exists until you delete it.  
**Scope** | Availability domain  | Regional (can be assigned to a private IP in any availability domain in the region)   
**Compartment and availability domain** | Same as the private IPs | Can be different from the private IPs  
When you launch an instance in a public subnet, by default, the instance gets a public IP unless you say otherwise. See [Choosing Whether an Ephemeral Public IP is Assigned at Instance Creation](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm#top "You can choose whether to assign an ephemeral public IP address to an instance when you create it."). 
After you create a given public IP object, you can't change which type it is. Therefore, if you launch an instance and assign it an ephemeral public IP with address 203.0.113.2, you can't convert the ephemeral public IP to a reserved public IP with address 203.0.113.2. 
The preceding table notes the public IP limits per VNIC and instance. If you try to perform any operation that assigns or moves a public IP to a VNIC or instance that has already reached its public IP limit, an error is returned. The operations include:
  * Assigning a public IP
  * Creating a new secondary VNIC with a public IP
  * Moving a private IP with a public IP to another VNIC
  * Moving a public IP to another private IP


### Resources That Always Get a Public IP 🔗 
As mentioned earlier, certain types of resources are designed to be directly reachable from the internet. Examples: a NAT gateway or a public load balancer. These resources automatically get a public IP address upon creation. Oracle chooses the public IP address from the Oracle pool. You can't remove or change the address. 
For public load balancers, the address can be either a regional reserved public IP address that you create from a pool and assign to the load balancer at creation time, or an ephemeral public IP address assigned by Oracle for the life of the load balancer. When the load balancer is no longer needed, the ephemeral IP address is returned to the pool of available addresses, but the reserved IP address can be moved to a different resource. While active, this public IP appears in the list of your tenancy's reserved public IPs, which [you can view in the Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-reserved-public-ip.htm#top "View a list of all reserved public IP addresses in a compartment.").
For NAT gateways, the address is a regional ephemeral public IP that is assigned to the NAT gateway. Like other ephemeral public IPs, it's automatically unassigned and deleted when you terminate its assigned resource (the NAT gateway). However, unlike other ephemeral public IPs, you can't edit it or unassign it yourself.
### Required IAM Policy
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 
## Public IP Tasks 🔗 
### Ephemeral Public IPs
  * [Choosing Whether an Ephemeral Public IP is Assigned at Instance Creation](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-public-ip-instance-launch.htm#top "You can choose whether to assign an ephemeral public IP address to an instance when you create it.")
  * [Assigning an Ephemeral Public IP When Creating a Secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assign-ephermal-ip-secondary-vnic.htm#top "When you add a secondary VNIC to an instance, you choose whether the primary private IP on the new VNIC gets an ephemeral public IP.")
  * [Assigning an Ephemeral Public IP to an Existing Primary Private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/assigning-ephemeral-public-existing-private-ip.htm#top "Assign an ephemeral public IP address to an instance to enable communication with the internet.")
  * [Changing the Display Name for an Ephemeral Public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/change-display-ephermal-ip.htm#top "You can change the display name of an ephemeral public IP.")
  * [Deleting an Ephemeral Public IP From an Instance](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/deleting-ephemeral-public-ip-from-instance.htm#top "Deleting an ephemeral public IP automatically unassigns it from its private IP.")


### Reserved Public IPs
  * [Viewing Reserved Public IP Addresses](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/view-reserved-public-ip.htm#top "View a list of all reserved public IP addresses in a compartment.")
  * [Creating a Reserved Public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-create.htm#top "Create a reserved public IP object in a pool of reserved public IP addresses in Oracle Cloud Infrastructure.")
  * [Deleting a Reserved Public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-delete.htm#top "Delete a reserved public IP object in Oracle Cloud Infrastructure.")
  * [Assigning a Reserved Public IP to a Private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-assign.htm#top "Assign a reserved public IP object to a private IP address in Oracle Cloud Infrastructure.")
  * [Unassigning a Reserved Public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-unassign.htm#top "Unassign a reserved public IP object in Oracle Cloud Infrastructure.")
  * [Reassigning a Reserved Public IP to a Different Private IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-reassign.htm#top "Move a reserved public IP object from one private IP address to another.")
  * [Changing the Display Name of a Reserved Public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-change-display-name.htm#top "Change the display name of a reserved public IP object in Oracle Cloud Infrastructure.")
  * [Managing Tags for a Reserved Public IP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-manage-tags.htm#top "Update the tag information for a reserved public IP address.")
  * [Moving a Reserved Public IP to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/reserved-public-ip-move.htm#top "Move a reserved public IP address from one compartment to another. When you move a reserved public IP to a new compartment, inherent policies apply immediately.")


Was this article helpful?
YesNo

