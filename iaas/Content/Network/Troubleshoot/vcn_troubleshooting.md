Updated 2025-02-06
# VCN Troubleshooting
## Breaking API Changes
If anyone in your organization implements a regional subnet, you **might need to update any client code that works with Networking service subnets and private IPs**. There are possible breaking API changes. For more information, see the [regional subnet release note](https://docs.oracle.com/iaas/releasenotes/changes/08c01d20-c829-47f2-8d54-9e9958f50ba8/) . 
## DNS Resolver Endpoints
Network security groups (NSGs) act as a virtual firewall for your DNS resolver endpoints. An NSG consists of a set of ingress and egress [security rules](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securityrules.htm#Security_Rules) that apply only to the associated DNS resolver endpoints. 
## Secondary IP Address
If you assigned a secondary IP to a [secondary VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs), and you're using policy-based routing for the secondary VNIC, configure the route rules for the instance to look up the same route table for the secondary IP address, using the `ip rule add from <source address> lookup <table name>` command.
## DNS in Your VCN
You use the Domain Name Server DHCP option to specify the DNS Type for the associated subnet. If you change the option's value, either restart the DHCP client on the instance or reboot the instance. Otherwise, the change does not get picked up until the DHCP client refreshes the lease (within 24 hours).
By default, the Internet and VCN Resolver does not let instances resolve the hostnames of hosts in your on-premises network connected to your VCN by Site-to-Site VPN or FastConnect. That functionality can be achieved either by using a custom resolver or by configuring the VCN's [private DNS resolver](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns-topic-Private-resolver.htm#Private_resolver "A private DNS resolver answers DNS queries for a VCN per a configuration you create.").
## Requirements for DNS Labels and Hostnames 🔗 
  * VCN and subnet labels: Max 15 alphanumeric characters and must start with a letter. **Notice that hyphens and underscores are NOT allowed.** The value cannot be changed later.
  * Hostnames: Max 63 characters, letters and numbers are allowed. Hyphens are allowed. **Notice that periods are NOT allowed, hyphens aren't allowed at the beginning or end of the hostname, and the hostname can't be all numbers.** Hostnames must be compliant with RFCs [952](https://tools.ietf.org/html/rfc952) and [1123](https://tools.ietf.org/html/rfc1123). The value can be changed later.


Don't confuse the DNS label or hostname with the friendly name you can assign to the object (the _display name_), which doesn't have to be unique.
See [About the DNS Domains and Hostnames](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#About) for more information.
## Firewalls
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
## Outbound SMTP is blocked
Tenancies made after June 23, 2021 are by default not allowed to send e-mail through outbound TCP port 25 to the internet. Tenancies made before June 23, 2021 are unaffected. If you require the ability to send email from your tenancy, [open a service limits request](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti) to obtain an exemption.
## New connections to a compute instance are failing
Oracle uses connection tracking to allow responses for traffic that matches stateful rules. Each compute instance has a maximum number of concurrent connections that can be tracked, based on the instance's shape. If you reach the tracking limit for instance connections, any new connections to the instance are dropped.
To use the Console to see if new connections are dropping, check the instance VNIC metrics:
  1. Confirm you're viewing the compartment that contains the instance you're interested in.
  2. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  3. Click the instance to view its details. 
  4. Under **Resources** , click **Attached VNICs**.
The primary VNIC and any secondary VNICs attached to the instance are displayed.
  5. Click the VNIC that you're interested in.
  6. Under **Metrics** , four tables are relevant to connection tracking: 
     * INGRESS PACKETS DROPPED BY FULL CONNECTION TRACKING TABLE 
Any value other than zero indicates that the tracking table is full.
     * EGRESS PACKETS DROPPED BY FULL CONNECTION TRACKING TABLE 
Any value other than zero indicates that the tracking table is full.
     * CONNECTION TRACKING TABLE UTILIZATION 
A value of 100% indicates that the tracking table is full.
     * CONNECTION TRACKING TABLE FULL 
A value of 1/True indicates that the tracking table is full.


If the tracking table is full, you can resolve the problem of failed connections and dropped packets by implementing one of the following changes: 
  * Change stateful ingress rules to stateless rules (remember to create a corresponding stateless egress rule to allow replies)
  * Move to a larger compute shape that has [higher connection limit](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#computecapacityreservations)


## Subnet or VCN Deletion 🔗 
This topic covers reasons why deletion of a subnet or VCN might fail.
Remember:
  * To delete a VCN, it must first be empty and have no related resources or attached gateways (for example: no [internet gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingIGs.htm#Internet_Gateway), [dynamic routing gateway](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#Dynamic_Routing_Gateways_DRGs), and so on). 
  * To delete a VCN's subnets, they must first be empty (for example, no VNICs or resolver endpoints homed in the subnet).


### Delete All Option
The Console has an easy "Delete all" process that scans the chosen compartments then deletes a VCN and its related Networking resources (subnets, route tables, security lists, sets of DHCP options, internet gateway, and so on). If the VCN is attached to a Dynamic Routing Gateway (DRG), the process deletes the attachment, but the DRG remains. 
The "Delete All" process deletes one resource at a time. A VCN with many compartments and resources takes longer to delete than a VCN with only a few. A progress report is displayed to show the results of both the scan for resources and the deletion of those resources. 
**Note**
Before using the "Delete All" process, verify that no resources such as compute instances, [load balancers](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm), OCI database systems, or orphaned mount targets are present in any of the subnets. If any of these are present, the deletion process stalls when trying to delete the resource's subnet. Deleted VCN resources are irretrievable. For more information, see [Subnet or VCN Deletion](https://docs.oracle.com/en-us/iaas/Content/Network/Troubleshoot/vcn_troubleshooting.htm#Subnet_or_VCN_Deletion). 
If any subnet still contains resources, or if you don't have permission to delete a particular Networking resource, the "Delete All" process stops and returns an error message that includes the OCIDs of the blocking resources and subnets, which link to the details page for that resource. In some cases, you might need to contact your tenancy administrator to help you delete any remaining resources if you don't have the needed permissions. 
### The Subnet Isn't Empty 🔗 
The most common reason a subnet (and thus a VCN) can't be deleted is because the subnet contains one or more of these resources:
  * [Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Tasks/managingloadbalancer_topic-Terminating_Load_Balancers.htm)
  * [File storage orphaned mount target](https://docs.oracle.com/iaas/Content/File/Troubleshooting/orphanedmounttarget.htm)
  * [Bastion](https://docs.oracle.com/iaas/Content/Bastion/Tasks/delete-bastion.htm)
  * OCI database systems (Exadata Database Service on Dedicated Infrastructure, Autonomous Database on Dedicated Exadata Infrastructure, or Base Database systems)


**Note** When you create one of the preceding resources, you specify a VCN and subnet for it. The relevant service creates at least one [VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs) in the subnet and attaches the VNIC to the resource. The service manages the VNICs on your behalf, so they are not readily apparent to you in the Console. The VNIC enables the resource to communicate with other resources over the network. Although this documentation commonly talks about the resource itself being in the subnet, it's actually the resource's attached VNIC. This documentation uses the term _parent resource_ to refer to this type of resource. 
If the subnet _is_ empty when you try to delete it, its state changes to TERMINATING briefly and then to TERMINATED. 
If the subnet is not empty, you instead get an error indicating that there are still resources that you must delete first. The error includes the OCID of a VNIC that is in the subnet (there could be more, but the error returns only a single VNIC's OCID). 
You can use the [Oracle Cloud Infrastructure command line interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm) or another SDK or client to call the `GetVnic` operation with the VNIC OCID. The response includes the VNIC's _display name_. Depending on the type of parent resource, the display name can indicate which parent resource the VNIC belongs to. You can then delete that parent resource, or you can contact your administrator to determine who owns the resource. When the VNIC's parent resource is deleted, the attached VNIC is also deleted from the subnet. If there are remaining VNICs in the subnet, repeat the process of determining and deleting each parent resource until the subnet is empty. Then you can delete the subnet.
For example, if you're using the CLI, use this command to get information about the VNIC.
Command
CopyTry It
```
oci network vnic get --vnic-id <VNIC_OCID>
```

#### Load balancer example 🔗 
Here is an example CLI response for a VNIC that belongs to a load balancer. The display name shows the load balancer's OCID:
Copy
```
{
 "data": {
  "availability-domain": "fooD:PHX-AD-1", 
  "compartment-id": "ocid1.compartment.oc1..<unique_id_1>", 
  "defined-tags": {}, 
  "display-name": "VNIC for LB ocid1.loadbalancer.oc1.phx.<unique_id_2>", 
  "freeform-tags": {}, 
  "hostname-label": null, 
  "id": "ocid1.vnic.oc1.phx.<unique_id_3>", 
  "is-primary": false, 
  "lifecycle-state": "AVAILABLE", 
  "mac-address": "00:00:17:00:BB:CA", 
  "private-ip": "10.0.0.6", 
  "public-ip": null, 
  "skip-source-dest-check": false, 
  "subnet-id": "ocid1.subnet.oc1.phx.<unique_id_4>", 
  "time-created": "2019-05-11T04:28:31.950000+00:00"
 }, 
 "etag": "5d8213fa"
}

```

#### File Storage example 🔗 
Here's an example for a VNIC that belongs to a File Storage mount target:
Copy
```
"display-name": "fss-<integer>",
```

Although the display name does not include an OCID, the `fss` characters indicate that the resource is for the File Storage service. 
#### Database example 🔗 
Here's an example of the display name for a VNIC that belongs to a DB system:
Copy
```
"display-name": "ocid1.dbnode.oc1.phx.<unique_id>", 
```

### A Network Security Group Isn't Empty 🔗 
Another reason a VCN can't be deleted is because it contains a one or more [network security groups](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/networksecuritygroups.htm#Network_Security_Groups) (NSGs) that are not yet empty. To delete an NSG, it must not contain any VNICs (or parent resources with VNICs). You can determine what parent resources are in an NSG by using either the Console or REST API. For more information, see [Deleting an NSG](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/delete_nsg.htm#delete_nsg "Delete a network security group \(NSG\) from a Virtual Cloud Network \(VCN\).").
### There Are Resources in Compartments You Don't Have Access To 🔗 
You might not be able to see all the resources in a subnet or VCN. This is because subnets and VCNs can contain resources in multiple **compartments** , and you might not have access to all the compartments. For example, the subnet might contain instances that your team manages but also DB systems that another team manages. Another example: The VCN might have security lists or a gateway in a compartment that another team manages. You might need to contact your tenancy administrator to help you determine who owns the resources in the subnet or VCN. 
## Repurposing an LPG fails 🔗  

Details
    An LPG created for a specific local peering connection can't be repurposed to be used in a new and different local peering connection.      If you attempt to do this you might see the error message `The Local             Peering Gateway with ID <LPG_OCID> has already been connected` when: 
  1. LPG 1 in VCN 1 was once successfully connected to LPG 2 in VCN 2.
  2. VCN 1 (including LPG 1) is subsequently deleted. The LPG 2 peering status changes to revoked or destroyed.
  3. You try to connect LPG 2 to LPG 3.


You could also see a slightly different message (`A peering with               VCN <VCN_OCID> has already been established`) when: 
  1. LPG 1 in VCN 1 was once successfully connected to LPG 2 in VCN 2.
  2. LPG 2 is subsequently deleted. The LPG 1 peering status changes to revoked or destroyed.
  3. You try to connect LPG 1 to LPG 3 (which could be a new LPG in VCN 2 or any other VCN).



Suggested Solution
    Perform the following actions: 
  1. Delete the LPG you're attempting to repurpose. 
If this deletion errors out with `409 - Local Peering Gateway <LPG_OCID> is                   associated with one or more entities that are in use` the LPG is likely mentioned in route rules in one or more route tables. Review the route tables for your VCN and remove those routes from the relevant route tables, and then try again to delete the LPG.
  2. Create a new LPG and peer it with a fresh LPG in the desired VCN. 


## Other useful links 🔗 
  * [Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs)
  * [DNS in Your Virtual Cloud Network](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/dns.htm#DNS_in_Your_Virtual_Cloud_Network)
  * [IP Management](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/ipaddressesanddns.htm#top "Oracle Cloud Infrastructure IP management helps you streamline your cloud networking. It lets you control public and private IP addresses to manage resource exposure and internal communication within your Virtual Cloud Network \(VCN\). It also offers dynamic DHCP options, robust Network Address Translation \(NAT\) gateways, and customizable security lists for enhanced network integrity and security.")


Was this article helpful?
YesNo

