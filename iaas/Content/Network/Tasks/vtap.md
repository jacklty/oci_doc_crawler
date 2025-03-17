Updated 2025-02-21
# Virtual Test Access Points (VTAPs)
A Virtual Test Access Point (VTAP) provides a way to mirror traffic from a selected _source_ to a selected _target_ to help in troubleshooting, security analysis, and data monitoring.
The VTAP uses a _capture filter_ , which contains a set of _rules_ governing what traffic a VTAP mirrors. A VTAP is `STOPPED` by default at creation, so you need to click the **Start VTAP** before it mirrors traffic as intended. 
You can create a capture filter while you create a VTAP, or assign an existing capture filter to a new VTAP. 
## VTAP sources and targets 🔗 
The VTAP _source_ is the resource the VTAP monitors. Traffic on this resource is mirrored and sent to a chosen target. The VTAP source and target must be hosted in the same VCN. They can be in different compartments or subnets provided you have the required permissions to view and work with these resources. VTAP _sources_ can be:
  * A single [Compute](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm) instance [VNIC](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm) in a subnet
  * A [Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Concepts/balanceoverview.htm)
  * A [Database](https://docs.oracle.com/en/cloud/paas/base-database/index.html) system
  * An [Exadata VM Cluster](https://docs.oracle.com/iaas/exadatacloud/index.html)
  * An [Autonomous Database for Analytics and Data Warehousing](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html) instance using a private endpoint


For Compute instances, specify the OCID of the attached VNIC. For the other source types, specify the service resource's OCID. 
​The target is the resource that receives traffic mirrored from a VTAP. VTAP _targets_ can be: 
  * A [Network Load Balancer](https://docs.oracle.com/iaas/Content/NetworkLoadBalancer/introducton.htm#NetworkLoadBalancerTypes)


**Note** When a resource used as a VTAP's source or target is deleted, the VTAP can no longer function and the Console puts the VTAP in the stopped state. To restart the VTAP, choose a new resource to replace the missing resource. 
This diagram shows a sample implementation of a VTAP. 
[![Diagram showing a VTAP with a source and a target.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vtap.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_vtap.svg)
In this example, the virtual machine in Subnet-A is sending traffic to another virtual machine in Subnet-B. The VTAP in Subnet-A checks traffic leaving the virtual machine. Because this traffic matches the capture filter in use, the VTAP mirrors the traffic to the target (in this case a network load balancer in Subnet-C). The backend set can then perform the appropriate analysis on the mirrored traffic.
## Capture filters and rules 🔗 
Capture filter rules select what is included in the traffic mirrored from the source to the target. Many VTAPs can use the same capture filter, so changing a capture filter's rules impacts all VTAPs that use that capture filter. A capture filter must have at least one rule, and can have up to 10 rules. Capture filter rules are examined in the sequence order you define. When a match is found, that rule is applied. If no match is found on a particular rule, the next rule in the sequence is evaluated and run if matched. Reordering the rules can change the capture filter behavior.
A capture filter can take an action (either include or exclude a packet) based on the following types of criteria: 
  * The packet is part of ingress or egress traffic
  * The packet is bound for or coming from a specific source or destination IPv4 CIDR block or IPv6 prefix 
  * The packet uses a specific IP protocol parameter (TCP or UDP port range, [ICMP](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml), [ICMPv6](https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml)) used by the traffic, or any protocols (using the default, **All**)


If a rule doesn't specify a CIDR block or prefix or IP protocol, all IP addresses or IP protocols are accepted for that rule.
Here's a working example of how you might structure a set of rules. The intent is that all traffic from 10.1.0.0/16 is included except 10.1.1.1, which is excluded: 
  1. Source CIDR: 10.1.1.1/32, Exclude
  2. Source CIDR: 10.1.0.0/16, Include
  3. Source CIDR: 10.1.1.0/24, Include


The capture filter evaluates each packet in the traffic against the rules in the defined sequence order. A packet from 10.1.1.1 matches the first rule and is excluded from the mirrored traffic. The packet isn't compared against the other rules in the set. The rule set works as intended.
If the first rule is moved to be third in the sequence order, the set of rules no longer works as intended: 
  1. Source CIDR: 10.1.0.0/16, Include
  2. Source CIDR: 10.1.1.0/24, Include
  3. Source CIDR: 10.1.1.1/32, Exclude


Because the capture filter rules evaluate each packet in the traffic in the defined sequence order, a packet from 10.1.1.1 now matches the first rule and is included in the mirrored traffic. Further rule evaluations are skipped. This example uses CIDR blocks, but rules are evaluated the same way no matter which source type you select.
For more information, see [Capture Filters](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/capture-filters.htm#capture-filters "Use capture filters to select what traffic to include in flow logs or VTAPs.").
## Advanced VTAP Features
**VXLAN network identifier (VNI):** Enter a VNI to uniquely identify the VXLAN encapsulation tunnel. If you don't specify a VNI, one is automatically generated for you. 
**Max packet size:** You can specify a maximum packet size from 64 to 9000 bytes. For better performance or efficient ingestion at the target, you can truncate the mirrored packets to a smaller length. A VTAP works with the MTU of 9000 bytes set on all instance NICs. However, because of VTAP encapsulation (VxLAN) overhead the MTU on instance VNICs that are VTAP sources must consider the target MTU minus the VTAP encapsulation overhead. To avoid any packet truncation in VTAP captured packets, source instance interfaces must have their MTU set to 8950 or lower for IPv4, or 8930 or lower for IPv6. We recommend that all target instances have their NICs set to use a 9000 byte MTU (the default in standard Oracle images).
**Note** If a VTAP is enabled on a particular supported source, the overhead generated by the mirroring of packets consumes network bandwidth. Network bandwidth capacity is decided by the underlying shape of the instance to which a VNIC is attached. A VTAP is implemented on the VNIC.
If you're using greater than 30% of the available network bandwidth supported by the service and you want to enable a VTAP, we recommend that you upgrade the underlying service shape.
Alternately, you can specify a smaller max packet size when you configure a VTAP to use an MTU of 1500 or smaller to achieve better overall performance and bandwidth usage.
For truncated mirrored packets, packet header parameters of the payload such as length and checksum aren't updated.
**Priority mode:** Using this option gives equal priority to monitored and mirrored traffic when there is congestion at the source. By default, production traffic is prioritized ahead of VTAP mirrored traffic. When you enable priority mode, monitored traffic and VTAP mirrored traffic are assigned equal priority. When this option is selected, mirrored traffic might cause some monitored traffic to be dropped whenever the source is congested. If this packet loss is detected you can either disable priority mode or upgrade the source shapes to accommodate more bandwidth.
## Requirements and Preparation 🔗 
Implementing a VTAP requires at least one valid source and one valid target, both in the same VCN. These resources must exist before you create a VTAP. The target can be in different subnet than the source.
## Dependencies 🔗 
Working with VTAPs requires understanding some crucial dependencies: 
  * A VTAP must always have a source, a target, and an associated capture filter.
  * A capture filter must always have at least one associated rule.
  * A VNIC can't ever be a source for more than one VTAP. See [VTAP sources and targets](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap__sources_targets) for more details.


You could see the following expected behaviors: 
  * You can't create a VTAP without choosing a source and target and associating it with an existing capture filter. You can edit which capture filter is associated with the VTAP. You can't ever have a VTAP that doesn't have an associated capture filter. 
  * You're prevented from deleting a capture filter associated with a VTAP. To delete a capture filter that one or more VTAPs use, you need to associate a different capture filter to those VTAPs before you delete the capture filter.
  * You're prevented from creating an empty capture filter or editing a capture filter to no longer contain any rules.
  * If a VTAP source or target is deleted, the VTAP is automatically put into the `STOPPED` state. To restart a VTAP stopped for this reason, edit the VTAP to assign a new valid source or target, which causes the VTAP to be put back in the `RUNNING` state.


## Required IAM Policy
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: see [IAM Policies for Networking](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Policies). 
## Limits on IAM Resources 🔗 
For a list of applicable limits and [instructions for requesting a limit increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti), see [Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm). To set compartment-specific limits on a resource or resource family, administrators can use [compartment quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm). 
See [VTAP Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#vtap) for a list of limits specific to this service. 
## Validated Oracle Partner Solutions 🔗 
Some members of the Oracle Partner Network (OPN) have verified solutions available in the Oracle Marketplace that function with a VTAP. You can deploy these solutions when you use a VTAP to send mirrored traffic to a Network Load Balancer target.
**Note** You can use other solutions with VTAP, but these solutions are validated by Oracle.
  * [Accedian](https://cloudmarketplace.oracle.com/marketplace/en_US/adf.task-flow?adf.tfId=adhtf&adf.tfDoc=/WEB-INF/taskflow/adhtf.xml&application_id=125193985)
  * [Netscout](https://cloudmarketplace.oracle.com/marketplace/en_US/partners/47052923)
  * [Palo Alto Networks](https://cloudmarketplace.oracle.com/marketplace/listing/71285857)


## VTAP Tasks 🔗 
You can perform the following tasks using the VTAP service:
### VTAPs
  * [Creating a VTAP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-create.htm#top "Create a Virtual Test Access Point \(VTAP\) to mirror traffic from a chosen source to a selected target to help troubleshooting, security analysis, and data monitoring.")
  * [Listing VTAPs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-list.htm#top "List all Virtual Test Access Point \(VTAPs\) in a compartment.")
  * [Updating a VTAP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-update.htm#top "Update the information for a Virtual Test Access Point \(VTAP\).")
  * [Starting or Stopping a VTAP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-turning-vtap-on-or-off.htm#top "Start or stop a Virtual Test Access Point \(VTAP\).")
  * [Moving a VTAP to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-move.htm#top "You can move a Virtual Test Access Point \(VTAP\) from one compartment to another.")
  * [Deleting a VTAP](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap-delete.htm#top "Delete a Virtual Test Access Point \(VTAP\).")


### Capture Filters
  * [Creating a Capture Filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-create.htm#top "Create a capture filter that you can use with a Virtual Test Access Point \(VTAP\) or a VCN flow log.")
  * [Updating a Capture Filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-update.htm#top "Update the information for a capture filter.")
  * [Moving a Capture Filter to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm#top "Move a capture filter from one compartment to another.")
  * [Deleting a Capture Filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm#top "Delete a capture filter.")


Was this article helpful?
YesNo

