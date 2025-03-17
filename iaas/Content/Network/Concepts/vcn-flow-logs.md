Updated 2025-02-21
# Flow Logs
Use VCN flow logs to capture network traffic information to support monitoring and security needs.
## Highlights
  * VCN flow logs show details about traffic that passes through a VCN.
  * VCN flow logs help you audit traffic and troubleshoot security lists.
  * Enable and manage flow logs from the Network Command Center.
  * Use capture filters to evaluate and select traffic to include in the flow log.
  * Flow logs leverage the Logging service to send log information to a specified log group. For more information, see [Logging Overview](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm).
  * Enable flow logs for all VNICs in a VCN or subnet, or target specific instances, network load balancers, or resource VNICs as enablement points.


## Overview
Each resource in a VCN has one or more [Virtual Network Interface Cards (VNICs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs). The Networking service uses [Security Lists](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/securitylists.htm#Security_Lists) to decide what traffic is allowed through a particular VNIC. The VNIC is subject to all rules in all security lists associated with the VNIC's subnet.
To help you troubleshoot security lists or audit the traffic in and out of VNICs, you can set up _VCN flow logs_. Flow logs record details about traffic that has been accepted or rejected based on the security list rules.
## How Flow Logs Are Enabled and Delivered
Flow logs are enabled in the Network Command Center, and leverage the [Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm) to store flow logs in a log group. Log groups are logical containers that you use to manage and organize flow logs.
You can select from four types of enablement points:
  * **Virtual Cloud Network (VCN):** Traffic is logged for existing and future VNICs in all subnets in the VCN.
  * **Subnet:** Traffic is logged for existing and future VNICs in that subnet.
  * **VNIC:** Traffic is logged for specific VNICs in a VCN.
  * **Resources:** Traffic is logged for a targeted instance or network load balancer in a VCN.

Each flow log record contains information about traffic for a single VNIC.
Flow logs use capture filters to select what is included in the logged traffic. Using a capture filter, you can specify the percentage of network flows to capture (sampling rate). You can also create rules to include or exclude packet based on criteria you specify. A capture filter must have at least one rule, and can have up to 10 rules. Capture filter rules are examined in the sequence order you define. When a match is found, that rule is applied. If no match is found on a particular rule, the next rule in the sequence is evaluated and run if matched. Reordering the rules can change the capture filter behavior. For more information, see [Capture Filters](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/capture-filters.htm#capture-filters "Use capture filters to select what traffic to include in flow logs or VTAPs.").
After flow logs are enabled, a batch of flow logs for each VNIC is collected at the sampling rate you specify in the log's capture filter.
You can view flow log contents and manage flow logs and log groups from the Network Command Center or from the [Logging service](https://docs.oracle.com/iaas/Content/Logging/Concepts/loggingoverview.htm) page. You can view and manage capture filters from the Network Command Center.
## Flow Log Contents 🔗 
Each flow log record reflects logged traffic _in one direction_ of a connection between two endpoints. For example, for a single TCP connection, you might have two records in the capture window: one for ingress traffic, and the other for egress traffic. 
For more information about flow log contents, examples, and limitations and other considerations, see [Details for VCN Flow Logs](https://docs.oracle.com/iaas/Content/Logging/Reference/details_for_vcn_flow_logs.htm).
## Flow Logs Tasks 🔗 
### Flow Logs
  * [Enabling Flow Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-enable.htm#vcn-flow-logs-enable "Enable VCN Flow Logs for subnets, instances, load balancers, or network load balancers.")
  * [Editing a Flow Log](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-update.htm#vcn-flow-logs-update "Change the configuration information for a VCN flow log.")
  * [Deleting a Flow Log](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-delete.htm#vcn-flow-logs-delete "Delete a VCN flow log.")
  * [Bulk Deleting Flow Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vcn-flow-logs-bulk-delete.htm#vcn-flow-logs-bulk-delete "Delete many VCN flow logs at one time.")


### Capture Filters
  * [Creating a Capture Filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-create.htm#top "Create a capture filter that you can use with a Virtual Test Access Point \(VTAP\) or a VCN flow log.")
  * [Updating a Capture Filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-update.htm#top "Update the information for a capture filter.")
  * [Moving a Capture Filter to a Different Compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-move.htm#top "Move a capture filter from one compartment to another.")
  * [Deleting a Capture Filter](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-delete.htm#top "Delete a capture filter.")


Was this article helpful?
YesNo

