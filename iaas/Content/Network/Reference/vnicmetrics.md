Updated 2025-01-15
# VNIC Metrics
You can monitor the health, capacity, and performance of your Networking service VNICs by using [metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics), [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
This topic describes the metrics emitted by the metric namespace `oci_vcn` (the Networking service).
Resources: virtual network interface cards (VNICs). 
## Overview of Metrics for an Instance and Its Network Devices 🔗 
If you're not already familiar with the different types of metrics available for an instance and its storage and network devices, see [Compute Instance Metrics](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm).
## Overview of Metrics: oci_vcn 🔗 
Each compute instance has one or more Networking service [VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingVNICs.htm#Virtual_Network_Interface_Cards_VNICs). A VNIC connects the instance to a subnet in a Virtual Cloud Network (VCN). A given VNIC controls how the instance communicates with endpoints inside the VCN (other instances) and endpoints outside the VCN (hosts on the internet, in your on-premises network, in another VCN, and so on).
With the Networking service metrics (in metric namespace `oci_vcn`), you can get this information for a VNIC:
  * **Traffic to and from the network:** Per-VNIC traffic levels (packets and bytes), which can help you identify meaningful increases or decreases in traffic coming in and out of your instances
  * **Packets dropped due to security list violations:** Per-VNIC _drops_ (dropped packets), which can help you identify changes in traffic caused by security list changes


The following diagram illustrates the general concept. A given instance resides in a subnet within a VCN that has one or more gateways to communicate with other networks. The instance is enlarged to show its VNIC, which the instance uses to communicate with the network. In this context, the term _network_ means both the other instances in the VCN and hosts outside the VCN available through the gateways. 
The VNIC receives traffic from the network and sends traffic to the network. The Networking service drops packets according to security list rules you set up for the instance's subnet. Traffic coming to the VNIC from the network is measured _after_ the Networking service drops the packets that violate the subnet's security list rules. Traffic leaving the VNIC is measured _before_ the Networking service drops the packets that violate the subnet's security list rules.
[![This image shows instances in a VCN, and a single instance enlarged with the VNIC and traffic following in and out.](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_telemetry_metrics_overview.svg)](https://docs.oracle.com/en-us/iaas/Content/Network/Images/network_telemetry_metrics_overview.svg)
The Compute service separately reports network-related metrics _as measured on the instance itself and aggregated across all the attached VNICs_. Those metrics are available in the `oci_computeagent` metric namespace. For more information, see [Compute Instance Metrics](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm). 
## Raw Data Point Frequency 🔗 
For every 1-minute interval, the Networking service posts one raw data point to the Monitoring service. The Monitoring service charts show data points at 1-minute, 5-minute, 1-hour (60-minute), and 1-day intervals. Supported values for interval depend on the specified time range in the metric query (not applicable to alarm queries). More interval values are supported for smaller time ranges. For example, if you select one hour for the time range, then all interval values are supported. If you select 90 days for the time range, then only interval values between 1 hour and 1 day are supported. The available statistics are calculated by using the count of 1-minute data points in the select interval. For example, for a given metric:
  * The mean for each 5-minute interval is calculated over five raw data points.
  * The mean for each 60-minute interval is calculated over 60 raw data points.


## Required IAM Policy 🔗 
When writing an IAM policy for viewing VNIC metrics, it's important to remember that:
  * The VNIC and the VNIC's metrics (emitted by the `oci_vcn` metric namespace) reside in the _subnet's compartment_ , and not the instance's compartment.
  * The _VNIC attachment_ (which is an object different from the VNIC itself) resides in the _instance's compartment_.


If the instance and subnet are in the same compartment, these details aren't so important when you write the IAM policy. 
[Minimum required policy for getting VNIC metrics](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/vnicmetrics.htm)
The following policy contains the one statement required to get VNIC metrics, which are part of the `oci_vcn` metric namespace.
If you're using the Console, this policy lets you go to the **Monitoring** tab in the Console and view the metrics for one or more VNICs in the specified compartment. The policy uses an example group called VnicMetricReaders. The condition at the end (`where target.metrics.namespace='oci_vcn'`) allows the group to view only the metrics in the `oci_vcn` metric namespace. 
Copy
```
Allow group VnicMetricReaders to read metrics in compartment <subnet_compartment> where target.metrics.namespace='oci_vcn'
```

[Policy for viewing a VNIC's details and metrics in the Console](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/vnicmetrics.htm)
The following policy lets you view an instance in the Console, click through to a specific VNIC, and then view that VNIC's details and metrics. 
Copy
```
Allow group VnicMetricReaders to read metrics in compartment <subnet_compartment> where target.metrics.namespace='oci_vcn'
Allow group VnicMetricReaders to read instance-family in compartment <instance_compartment>
Allow group VnicMetricReaders to inspect virtual-network-family in compartment <subnet_compartment>
```

The second and third statements let you view the instance's details and the VNIC's details, respectively. 
## Available Metrics: oci_vcn 🔗 
The `Vnic` metrics listed in the following table are automatically available for any VNIC on any instance you create. You do not need to enable monitoring on the instance to get these metrics for the VNIC or VNICs on the instance. 
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
Each metric includes the following dimension:  

RESOURCEID
    The **OCID** of the VNIC. 
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`VnicEgressDropsSecurityList` |  **Egress Packets Dropped by Security List** |  packets |  Packets sent by the VNIC, destined for the network, dropped due to security rule violations. |  `resourceId `  
`VnicIngressDropsSecurityList` |  **Ingress Packets Dropped by Security List** |  packets |  Packets received from the network, destined for the VNIC, dropped due to security rule violations.  
`VnicFromNetworkBytes`*  |  **Bytes from Network** |  bytes |  Bytes received at the VNIC from the network, after drops.  
`VnicFromNetworkPackets`*  |  **Packets from Network** |  packets |  Packets received at the VNIC from the network, after drops.  
`VnicToNetworkBytes`*  |  **Bytes to Network** |  bytes |  Bytes sent from the VNIC to the network, before drops.  
`VnicToNetworkPackets`*  |  **Packets to Network** |  packets |  Packets sent from the VNIC to the network, before drops.   
`VnicIngressDropsThrottle` | **Throttled Ingress Packets** | packets |  Packets received from the network, destined for the VNIC, dropped due to throttling.  
`VnicEgressDropsThrottle` | **Throttled Egress Packets** | packets |  Packets sent from the VNIC, destined for the network, dropped due to throttling.  
`VnicIngressDropsConntrackFull` | **Ingress Packets Dropped by Full Connection Tracking Table** | packets |  Packets received from the network, destined for the VNIC, dropped due to full connection tracking table.  
`VnicEgressDropsConntrackFull` | **Egress Packets Dropped by Full Connection Tracking Table** | packets |  Packets sent from the VNIC, destined for the network, dropped due to full connection tracking table.  
`VnicConntrackUtilPercent` | **Connection Tracking Table Utilization** | percentage |  Total utilization percentage (0-100%) of the connection tracking table.  
`VnicConntrackIsFull` | **Connection Tracking Table Full** | boolean |  Boolean (0/false, 1/true) that indicates the connection tracking table is full.  
`SmartnicBufferDropsFromNetwork` **  | **Smartnic Buffer Drops from Network** | packets | Number of packets dropped in SmartNIC from network due to buffer exhaustion.  
`SmartnicBufferDropsFromHost` **  | **Smartnic Buffer Drops from Host** | packets | Number of packets dropped in SmartNIC from host due to buffer exhaustion.  
* The Compute service separately reports network-related metrics _as measured on the instance itself and aggregated across all the attached VNICs_. Those metrics are available in the `oci_computeagent` metric namespace. For more information, see [Compute Instance Metrics](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm). 
** The `SmartnicBufferDropsFromNetwork` and `SmartnicBufferDropsFromHost` metrics are available only for Bare Metal Instances. For VMs, these metric values are zero.
## Tips for Working with VNIC Metrics 🔗 
Here are some tips to help you use VNIC metrics.
### Default Metric Charts for One VNIC Versus Multiple VNICs
The default charts for VNIC metrics use these default settings:
  * Time range = the last hour
  * Interval = 1 minute
  * Statistic displayed: Sum
  * Aggregation of metric streams = not selected (which means each VNIC is displayed as a separate line on the chart)


You can [view the default charts with _data for only a single VNIC_](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/vnicmetrics.htm#single_vnic) by viewing the VNIC's details in the Console. When looking at a single VNIC, these statistics are the most useful: sum, mean, max, and min.
You can [view the default charts with _data for multiple VNICs_](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/vnicmetrics.htm#multiple_vnics) by going to the **Service Metrics** page in the Console. Select the necessary compartment and metric namespace (`oci_vcn`) at the top of the page. For all the charts, you can either show each VNIC as a separate line, or show a single line that aggregates the data for all the VNICs in your selected compartment. To aggregate the data, select **Aggregate Metric Streams**.
When viewing aggregated data, you can use the P90 - P99.9 statistics to help identify typical behavior of your instance fleet and outliers. To view these statistics over an even larger number of data points, expand the chart's start and end time (for example, view the last 7 days instead of the last hour), and set the interval to 1 hour.
For general information about how to work with and modify the default metric charts, see [Viewing Default Metric Charts](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/viewingcharts.htm).
### Alarms for VNIC Metrics
You can set up [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/managingalarms.htm) for a given metric. For VNICs, an alarm makes the most sense for the egress security list drops metric (`VnicEgressDropsSecurityList`). In a normal situation, you shouldn't have egress security list drops. If you do, it might be due to one of the following causes:
  * An application is behaving in an unexpected manner
  * Your security list is incorrectly configured 


In either case, an alarm is warranted.
## Using the Console 🔗 
[To view default metric charts for a single VNIC](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/vnicmetrics.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance to view its details.
  3. Under **Resources** , click **Attached VNICs**. 
  4. Click the VNIC to view its details.
  5. Under **Resources** , click **Metrics**.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
[To view default metric charts for multiple VNICs](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/vnicmetrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. For **Compartment** , select the compartment that contains the VNICs you're interested in. Remember that a given VNIC resides in its _subnet's_ compartment.
  3. For **Metric namespace** , select **oci_vcn**.
The **Service Metrics** page dynamically updates the page to show charts for each metric emitted by the selected metric namespace. 


**Tip** If the compartment has multiple VNICs, the charts default to show a separate line for each VNIC. By selecting **Aggregate Metric Streams** on the right side of the page, you can show a single line aggregated across all the VNICs.
For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

