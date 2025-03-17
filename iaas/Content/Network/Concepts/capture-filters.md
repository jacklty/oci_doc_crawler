Updated 2025-02-21
# Capture Filters
Use capture filters to select what traffic to include in flow logs or VTAPs. 
You can create two types of capture filters: **Flow log** capture filters and **VTAP** capture filters. Both types use rules to include or exclude packets. Flow log capture filters also let you to specify a sampling rate.
Capture filters can be used by many VTAPs or flow logs. When you change the configuration for a capture filter, then all the resources that use that capture filter are impacted. You can only use capture filters of the appropriate type with a resource. For example, you can't use a VTAP capture filter with a flow log.
For more information, see [Flow Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/vcn-flow-logs.htm#vcn_flow_logs "Use VCN flow logs to capture network traffic information to support monitoring and security needs.") and [Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap "A Virtual Test Access Point \(VTAP\) provides a way to mirror traffic from a selected source to a selected target to help in troubleshooting, security analysis, and data monitoring.").
## Sampling Rate
When you create a flow log capture filter, you can specify a sampling rate. The capture filter sampling rate controls the percentage of network flows you want the flow log to capture. Then, rules are applied by the capture filter to include or exclude packets in the flow from logging.
## Rules
A capture filter must have at least one rule, and can have up to 10 rules. Capture filter rules are examined in the sequence order you define. When a match is found, that rule is applied. If no match is found on a particular rule, the next rule in the sequence is evaluated and run if matched. Reordering the rules can change the capture filter behavior. A capture filter can take an action (either include or exclude a packet) based on the following types of criteria: 
  * The packet is part of ingress or egress traffic
  * The packet is bound for or coming from a specific source or destination IPv4 CIDR block or IPv6 prefix 
  * The packet uses a specific IP protocol parameter (TCP or UDP port range, [ICMP](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml) , [ICMPv6](https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml)) used by the traffic, or any protocols (using the default, **All**)


If a rule doesn't specify a CIDR block or prefix or IP protocol, all IP addresses or IP protocols are accepted for that rule.
Here's a working example of how you might structure a set of rules. The intent is that all traffic from 10.1.0.0/16 is included except 10.1.1.1, which is excluded: 
  1. Source CIDR: 10.1.1.1/32, Exclude
  2. Source CIDR: 10.1.0.0/16, Include
  3. Source CIDR: 10.1.1.0/24, Include


The capture filter evaluates each packet in the traffic against the rules in the defined sequence order. A packet from 10.1.1.1 matches the first rule and is excluded from the mirrored traffic. The packet is not compared against the other rules in the set. The rule set works as intended.
If the first rule is moved to be third in the sequence order, the set of rules no longer works as intended: 
  1. Source CIDR: 10.1.0.0/16, Include
  2. Source CIDR: 10.1.1.0/24, Include
  3. Source CIDR: 10.1.1.1/32, Exclude


Because the capture filter rules evaluate each packet in the traffic in the defined sequence order, a packet from 10.1.1.1 now matches the first rule and is included in the mirrored traffic. Further rule evaluations are skipped. This example uses CIDR blocks, but rules are evaluated the same way no matter which source type you select.
If a packet doesn't match any rule, then it's ignored and it isn't included in the log. If you want packets that aren't otherwise specified in a rule to be included in a log, you can create an Include rule for the source CIDR of 0.0.0.0/0. This captures any 'leftover' packets in a log that aren't captured in a previous rule. 
Here's an example: The intent is that all traffic from 10.1.1.1 is excluded, and everything else is included.
  1. Source CIDR: 10.1.1.1/32, Exclude
  2. Source CIDR: 0.0.0.0/0, Include


**Note** Using 0.0.0.0/0 to log packets can produce a large amount of log data.
## Capture Filter Tasks
  * [Creating a Capture Filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-create.htm#top "Create a capture filter that you can use with a Virtual Test Access Point \(VTAP\) or a VCN flow log.")
  * [Updating a Capture Filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-update.htm#top "Update the information for a capture filter.")
  * [Moving a Capture Filter to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm#top "Move a capture filter from one compartment to another.")
  * [Deleting a Capture Filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm#top "Delete a capture filter.")


Was this article helpful?
YesNo

