Updated 2025-01-15
# VTAP Metrics
You can monitor the health, capacity, and performance of your VTAPs by using metrics, alarms, and notifications. 
For more information, see [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
This topic describes the metrics emitted by the metric namespaces `oci_vcn` or `oci_nlb`.
Resources: VNICs, load balancers
## Overview of Metrics 🔗 
Metrics are available for many resources in a VTAP. The metrics help you decide whether a VTAP is mirroring packets or not, how much data is flowing over the VTAP sources and targets, and whether packets are being dropped for unexpected errors.
VTAP metrics are only supported for Compute instance VNIC source types, and Network Load Balancer target types.
### Raw Data Point Frequency
For every 1-minute interval, the Networking service posts one raw data point to the Monitoring service. The Monitoring service charts show data points at 1-minute, 5-minute, 1-hour (60-minute), and 1-day intervals. Supported values for interval depend on the specified time range in the metric query (not applicable to alarm queries). More interval values are supported for smaller time ranges. For example, if you select one hour for the time range, then all interval values are supported. If you select 90 days for the time range, then only interval values between 1 hour and 1 day are supported. The available statistics are calculated by using the count of 1-minute data points in the select interval. For example, for a given metric:
  * The mean for each 5-minute interval is calculated over five raw data points.
  * The mean for each 60-minute interval is calculated over 60 raw data points.


### Required IAM Policy 🔗 
To monitor resources, you must be given the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, confirm with your administrator the type of access you've been granted and which **compartment** you should work in. For more information on user authorizations for monitoring, see the Authentication and Authorization section for the related service: [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/home.htm) or [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm)
## Available Metrics: oci_vcn 🔗 
The metrics listed in the following table are automatically available for VTAPs with an instance VNIC source type. You do not need to enable monitoring to get these metrics.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
Each metric includes the following dimensions: 
  * **resourceId:** The OCID of the source instance VNIC.


Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
` VnicFromNetworkMirrorPackets* ` |  **Mirrored packets from Network** |  packets |  Mirrored packets received at the VNIC from the network, after drops. |  `VNIC resourceId `  
`VnicFromNetworkMirrorBytes`*  |  **Mirrored bytes from Network** |  bytes |  Mirrored bytes received at the VNIC from the network, after drops.  
`VnicToNetworkMirrorPackets`*  |  **Mirrored packets to Network** |  packets |  Mirrored packets sent from the VNIC to the network, before drops.   
`VnicToNetworkMirrorBytes`*  |  **Mirrored Bytes to Network** |  bytes |  Mirrored bytes sent from the VNIC to the network, before drops.  
`VnicIngressMirrorDropsSecurityList` |  **Ingress Mirrored Packets Dropped by Security List** |  packets |  Mirrored packets received from the network, destined for the VNIC, dropped due to security rule violations.  
`VnicIngressMirrorDropsConntrackFull` | **Ingress Mirrored Packets Dropped by Full Connection Tracking Table** | packets |  Mirrored packets received from the network, destined for the VNIC, dropped due to full connection tracking table.  
`VnicIngressMirrorDropsThrottle` | **Throttled Egress Mirrored Packets** | packets |  Mirrored packets received from the network, destined for the VNIC, dropped due to throttling.  
`VnicEgressMirrorDropsThrottle` | **Throttled Egress Mirrored Packets** | packets |  Mirrored packets sent from the VNIC, destined for the network, dropped due to throttling.  
* The Compute service separately reports network-related metrics _as measured on the instance itself and aggregated across all the attached VNICs_. Those metrics are available in the `oci_computeagent` metric namespace. For more information, see [Compute Instance Metrics](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm). 
## Available Metrics: oci_nlb 🔗 
The metrics listed in the following table are automatically available for VTAPs with an Network Load Balancer target type. You do not need to enable monitoring to get these metrics.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
Each metric includes the following dimensions: 
  * **resourceId:** The OCID of the Target NLB.
  * **resourceName:** The displayName of the Target NLB.


Metric Names | Display Name | Unit | Description | Dimensions | Displayed by Default  
---|---|---|---|---|---  
`NLBVTAPFwdDrops` | **Mirrored Packets not Forwarded to NLB Back Ends** |  Packets |  Mirrored packets that are not forwarded to the NLB back ends due to issues such as:
  * No listener setup for the destination port in the overlay packet
  * No healthy backends found at that time
  * Packet dropped by security list

|  resourceId resourceName | No  
`NLBVTAPReceivedBytes` | **Mirrored Bytes to NLB** |  Bytes | Number of mirrored bytes sent from VTAP(s) to NLB. |  resourceId resourceName | Yes  
`NLBVTAPReceivedPackets` | **Mirrored Packets from VTAPs** |  Packets | Number of mirrored packets sent from VTAPs to NLB |  resourceId resourceName | No  
`NLBVTAPTransmittedBytes` | **Mirrored bytes transmitted to NLB back ends** |  Bytes | Number of mirrored bytes received from VTAPs transmitted to NLB back ends |  resourceId resourceName | Yes  
`NLBVTAPTransmittedPackets` | **Mirrored packets transmitted to NLB back ends** |  Packets | Number of mirrored packets received from VTAP(s) transmitted to NLB back ends |  resourceId resourceName | No  
## Using the Console 🔗 
[To view default metric charts for all VCNs or NLBs in a compartment](https://docs.oracle.com/en-us/iaas/Content/Network/Reference/vtapmetrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. In Compartment, select the compartment you're interested in.
  3. For Metric **Namespace** , select **oci_vcn** or **oci_nlb**.
  4. The **Service Metrics** page dynamically updates the page to show charts for each metric emitted by the selected metric namespace.


By default, the charts show a separate line for each resource in the compartment.
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

