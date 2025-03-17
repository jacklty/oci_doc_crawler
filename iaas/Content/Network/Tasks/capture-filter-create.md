Updated 2025-02-21
# Creating a Capture Filter
Create a capture filter that you can use with a Virtual Test Access Point (VTAP) or a VCN flow log.
You can also define a capture filter when you create a VTAP or VCN flow log. This procedure assumes that you're creating a capture filter independently. 
For more information about capture filters and feature overviews, see [Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap "A Virtual Test Access Point \(VTAP\) provides a way to mirror traffic from a selected source to a selected target to help in troubleshooting, security analysis, and data monitoring.") and [Flow Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/vcn-flow-logs.htm#vcn_flow_logs "Use VCN flow logs to capture network traffic information to support monitoring and security needs.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/capture-filter-create.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Network Command Center** , select **Capture filters**.
    2. Select **Create capture filter**.
    3. Enter the following information:
       * **Name:** Enter a descriptive name for the capture filter. It doesn't have to be unique, and you can't change it later in the Console (but you can change it with the API).
       * **Compartment:** Select the compartment that you want to create the capture filter in.
       * **Filter type:** Select the type of filter to create. The type must match its intended purpose. For example, if you intend to use the capture filter with a flow log, select **Flow log capture filter**. For more information, see [Flow Logs](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/vcn-flow-logs.htm#vcn_flow_logs "Use VCN flow logs to capture network traffic information to support monitoring and security needs.") and [Virtual Test Access Points (VTAPs)](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap "A Virtual Test Access Point \(VTAP\) provides a way to mirror traffic from a selected source to a selected target to help in troubleshooting, security analysis, and data monitoring.").
       * **Sampling rate:** For flow log capture filters, select a sampling rate. Sampling rate is expressed as a percentage of the network flow to capture.
       * **Rules:** Create at least one rule. Capture filter rules are examined in order and run when matched. When the first match is found, remaining rules aren't examined or run. If you reorder the rules the capture filter behavior changes. Each capture filter can have a maximum of 10 rules. See [Capture filters and rules](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/vtap.htm#vtap__capture_filters) for examples of rule behavior.
Each rule can state whether to include or exclude packets based on the traffic direction (ingress or egress), source or destination IPv4 CIDR or Ipv6 prefix of the traffic, or the IP protocol used for the packet (TCP, UDP, [ICMP](https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml), [ICMPv6](https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xhtml)). Each protocol type offers further options appropriate for that protocol.
    4. (Optional) To apply one or more tags to the filter, select **Show advanced options**.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    5. Select **Create Capture Filter**.
  * Use the [capture-filter create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/capture-filter/create.html) command and required parameters to create a capture filter:
Command
CopyTry It
```
oci network capture-filter create --compartment-id compartment_OCID --filter-type VTAP or FLOWLOG ... [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateCaptureFilter](https://docs.oracle.com/iaas/api/#/en/iaas/latest/CaptureFilter/CreateCaptureFilter) operation to create a capture filter.


Was this article helpful?
YesNo

