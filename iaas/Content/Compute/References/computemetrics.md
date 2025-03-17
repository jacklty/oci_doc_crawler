Updated 2025-01-13
# Compute Instance Metrics
You can monitor the health, capacity, and performance of your compute instances by using [metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics), [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).
This topic describes the metrics emitted by the metric namespace `oci_computeagent` (the Compute Instance Monitoring plugin on compute instances).
You can view these metrics for individual compute instances, and for all the instances in an instance pool.
Resources: [Monitoring-enabled](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Enabling_Monitoring_for_Compute_Instances) compute instances.
## Overview of Metrics for an Instance and Related Resources 🔗 
This section gives an overall picture of the different types of metrics available for an instance and its storage and network devices. See the following diagram and table for a summary.
[![This image shows the types of metrics available for an instance and related components.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compute_instance_overall_monitoring_metrics.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compute_instance_overall_monitoring_metrics.png)
Metric Namespace | Resource ID | Where Measured | Available Metrics  
---|---|---|---  
`oci_computeagent` | Instance OCID | On the instance. The metrics in this namespace are aggregated across all the related resources on the instance. For example, `DiskBytesRead` is aggregated across all the instance's attached storage volumes, and `NetworkBytesIn` is aggregated across all the instance's attached VNICs. |  See [Available Metrics: oci_computeagent](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl).  
`oci_blockstore` | Boot or block volume OCID | By the Block Volume service. The metrics are for an individual volume (either boot volume or block volume). | See [Block Volume Metrics](https://docs.oracle.com/iaas/Content/Block/References/volumemetrics.htm).  
`oci_vcn` | VNIC OCID | By the Networking service. The metrics are for an individual VNIC. |  See [VNIC Metrics](https://docs.oracle.com/iaas/Content/Network/Reference/vnicmetrics.htm).  
## Before You Begin 🔗 
  * IAM policies: To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).
  * Metrics exist in Monitoring: The resources that you want to monitor must emit metrics to the Monitoring service. 
  * Compute instances: To emit metrics, the Compute Instance Monitoring plugin must be enabled on the instance, and plugins must be running. The instance must also have either a service gateway or a public IP address to send metrics to the Monitoring service. For more information, see [Enabling Monitoring for Compute Instances](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm). 


## Available Metrics: oci_computeagent 🔗 
The compute instance metrics help you measure activity level and throughput of compute instances. The metrics listed in the following table are available for any [monitoring-enabled ](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Enabling_Monitoring_for_Compute_Instances) compute instance. To get these metrics, enable monitoring on the instance.
The metrics in this namespace are aggregated across all the related resources on the instance. For example, `DiskBytesRead` is aggregated across all the instance's attached storage volumes, and `NetworkBytesIn` is aggregated across all the instance's attached VNICs. 
For metrics emitted by the metric namespace `oci_computeagent`, data points are sampled every ten seconds. A batch of six of data points is emitted every minute. Therefore, for every minute granularity, the aggregate count is always six, the aggregate sum is the sum of the six data points, and the aggregate average is the average of the six data points.
You also can use the Monitoring service to create [custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).
Each metric includes the following **dimensions** : 

availabilityDomain
    The **availability domain** where the instance resides. 

faultDomain
    The **fault domain** where the instance resides. 

imageId
    The OCID of the **image** for the instance.  

instancePoolId
    The [instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/Concepts/instancemanagement.htm#Instance) that the instance belongs to.  

region
    The **region** where the instance resides. 

resourceDisplayName
    The friendly name of the instance.  

resourceId
    The **OCID** of the instance. 

shape
    The **shape** of the instance. 
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`CpuUtilization` | **CPU Utilization** | percent |  Activity level from CPU. Expressed as a percentage of total time. For instance pools, the value is averaged across all instances in the pool. |  `availabilityDomain` `faultDomain` `imageId` `instancePoolId` `region` `resourceDisplayName` `resourceId` `shape`  
`DiskBytesRead`[1,](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote1) [3](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote3) | **Disk Read Bytes** | bytes | Read throughput. Expressed as bytes read per interval.  
`DiskBytesWritten`[1,](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote1) [3](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote3) | **Disk Write Bytes** | bytes | Write throughput. Expressed as bytes written per interval.  
`DiskIopsRead`[1,](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote1) [3](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote3) | **Disk Read I/O** | operations | Activity level from I/O reads. Expressed as reads per interval.  
`DiskIopsWritten`[1,](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote1) [3](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote3) | **Disk Write I/O** | operations | Activity level from I/O writes. Expressed as writes per interval.  
`LoadAverage` | **Load Average** | number of processes | Average system load calculated over a 1-minute period.  
`MemoryAllocationStalls` | **Memory Allocation Stalls** | number of stalls | Number of times page reclaim was called directly.  
`MemoryUtilization`[1](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote1) | **Memory Utilization** | percent |  Space currently in use. Measured by pages. Expressed as a percentage of used pages. For instance pools, the value is averaged across all instances in the pool.  
`NetworksBytesIn`[1,](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote1) [2](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote2) | **Network Receive Bytes** | bytes |  Network receipt throughput. Expressed as bytes received.  
`NetworksBytesOut`[1, ](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote1)[2](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm#Availabl__Footnote2) | **Network Transmit Bytes** | bytes | Network transmission throughput. Expressed as bytes transmitted.  
1This metric is a cumulative counter that shows monotonically increasing behavior for each session of the Oracle Cloud Agent software, resetting when the operating system is restarted. 2The Networking service provides more metrics (in the `oci_vcn` metric namespace) for each [VNIC](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm) on the instance. For more information, see [Networking Metrics](https://docs.oracle.com/iaas/Content/Network/Reference/networkmetrics.htm).  3The Block Volume service provides more metrics (in the `oci_blockstore` metric namespace) for each volume attached to the instance. For more information, see [Block Volume Metrics](https://docs.oracle.com/iaas/Content/Block/References/volumemetrics.htm).   
## Available Metrics: gpu_infrastructure_health 🔗 
The compute instance metrics help you measure the activity level and throughput of compute instances. The metrics listed in the following table are available for any [monitoring-enabled ](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Enabling_Monitoring_for_Compute_Instances) compute instance. To get these metrics, enable monitoring on the instance.
The metrics in this namespace are aggregated across all the related resources on the instance. For example, `DiskBytesRead` is aggregated across all the instance's attached storage volumes, and `NetworkBytesIn` is aggregated across all the instance's attached VNICs.
For metrics emitted by the metric namespace `gpu_infrastructure_health`, data points are sampled every ten seconds. A batch of six of data points is emitted every minute. Therefore, for every minute granularity, the aggregate count is always six, the aggregate sum is the sum of the six data points, and the aggregate average is the average of the six data points.
You also can use the Monitoring service to create [custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).
Each metric includes the following **dimensions** : 

component
    GPU or rdma_nic 

timestamp
    UTC time when the payload/heartbeat is emitted 

version
    The payload version number for compatibility
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`GpuUtilization` | **GPU utilization** | percent |  Activity level from GPU. Expressed as a percentage of total time. For instance pools, the value is averaged across all instances in the pool. |  `availabilityDomain` `faultDomain` `gpuId` `imageId` `instancePoolId` `region` `resourceDisplayName` `resourceId` `shape`  
`GpuMemoryUtilization` | **GPU memory utilization** | percent | The percentage of the GPU memory resource in use.  
`GpuPowerDraw` | **GPU power draw** | integer | The amount of GPU power used.  
`GpuTemperature` | **GPU temperature** | integer | The GPU temperature reported.  
`GpuEccSingleBitErrors` | **GPU single-bit errors** | integer | The number of GPU single bit ECC errors reported.  
`GpuEccDoubleBitErrors` | **GPU double-bit errors** | integer | The number of GPU double bit ECC errors reported.  
1This metric is a cumulative counter that shows monotonically increasing behavior for each session of the Oracle Cloud Agent software, resetting when the operating system is restarted. 2The Networking service provides more metrics (in the `oci_vcn` metric namespace) for each [VNIC](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm) on the instance. For more information, see [Networking Metrics](https://docs.oracle.com/iaas/Content/Network/Reference/networkmetrics.htm).  3The Block Volume service provides more metrics (in the `oci_blockstore` metric namespace) for each volume attached to the instance. For more information, see [Block Volume Metrics](https://docs.oracle.com/iaas/Content/Block/References/volumemetrics.htm).   
### Fault Metrics: gpu_infrastructure_health
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`Fault` | **GPU fault** | count |  If the value is 0, there are no faults. If the value is 1, faults are detected. |  `availabilityDomain` `faultCode` `faultDomain` `gpuId` `imageId` `instancePoolId` `pcieAddress` `region` `resourceDisplayName` `resourceId` `shape`  
1This metric is a cumulative counter that shows monotonically increasing behavior for each session of the Oracle Cloud Agent software, resetting when the operating system is restarted. 2The Networking service provides more metrics (in the `oci_vcn` metric namespace) for each [VNIC](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm) on the instance. For more information, see [Networking Metrics](https://docs.oracle.com/iaas/Content/Network/Reference/networkmetrics.htm).  3The Block Volume service provides more metrics (in the `oci_blockstore` metric namespace) for each volume attached to the instance. For more information, see [Block Volume Metrics](https://docs.oracle.com/iaas/Content/Block/References/volumemetrics.htm).   
## Available Metrics: rdma_infrastructure_health 🔗 
The compute instance metrics help you measure activity level and throughput of compute instances. The metrics listed in the following table are available for any [monitoring-enabled ](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Enabling_Monitoring_for_Compute_Instances) compute instance. To get these metrics, enable monitoring on the instance.
The metrics in this namespace are aggregated across all the related resources on the instance. For example, `DiskBytesRead` is aggregated across all the instance's attached storage volumes, and `NetworkBytesIn` is aggregated across all the instance's attached VNICs. 
For metrics emitted by the metric namespace `rdma_infrastructure_health`, data points are sampled every ten seconds. A batch of six of data points is emitted every minute. Therefore, for every minute granularity, the aggregate count is always six, the aggregate sum is the sum of the six data points, and the aggregate average is the average of the six data points.
You also can use the Monitoring service to create [custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).
Each metric includes the following **dimensions** : 

component
    GPU or rdma_nic 

timestamp
    UTC time when the payload/heartbeat is emitted 

version
    The payload version number for compatibility
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`RdmaTxBytes` | **RDMA aggregate network transmit bytes** | bytes | The bytes transmitted on the RDMA interface. |  `availabilityDomain` `faultDomain` `imageId` `instancePoolId` `rdmaId` `region` `resourceDisplayName` `resourceId` `shape`  
`RdmaRxBytes` | **RDMA aggregate network receive bytes** | bytes | The bytes received on the RDMA interface.  
`RdmaTxPackets` | **RDMA aggregate network transmit packets** | integer | The number of RDMA interface packets transmitted.  
`RdmaRxPackets` | **RDMA aggregate network receive packets** | integer | The number of RDMA interface packets received.  
1This metric is a cumulative counter that shows monotonically increasing behavior for each session of the Oracle Cloud Agent software, resetting when the operating system is restarted. 2The Networking service provides more metrics (in the `oci_vcn` metric namespace) for each [VNIC](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm) on the instance. For more information, see [Networking Metrics](https://docs.oracle.com/iaas/Content/Network/Reference/networkmetrics.htm).  3The Block Volume service provides more metrics (in the `oci_blockstore` metric namespace) for each volume attached to the instance. For more information, see [Block Volume Metrics](https://docs.oracle.com/iaas/Content/Block/References/volumemetrics.htm).   
### Fault Metrics: rdma_infrastructure_health
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`RdmaLinkSpeedFault` | **Faults** | count | Detects if a link speed fault is present. If the value is 0, there are no faults. If the value is 1, faults are detected. |  `availabilityDomain` `faultDomain` `imageId` `instancePoolId` `pcieAddress` `rdmaId` `region` `resourceDisplayName` `resourceId` `shape`  
`RdmaPcieAddressFault` | **Faults** | count | Detects if a PCIE address fault is present. If the value is 0, there are no faults. If the value is 1, faults are detected.  
`RdmaPcieBerCheckFault` | **Faults** | count | Detects if a PCIE BER fault is present. If the value is 0, there are no faults. If the value is 1, faults are detected.  
`RdmaPcieCableFlapFault` | **Faults** | count | Detects if a PCIE cable flap fault is present. If the value is 0, there are no faults. If the value is 1, faults are detected.  
`RdmaPcieCablePlugFault` | **Faults** | count | Detects if a PCIE cable plug fault is present. If the value is 0, there are no faults. If the value is 1, faults are detected.  
`RdmaPcieCableStateFault` | **Faults** | count | Detects if a PCIE cable state fault is present. If the value is 0, there are no faults. If the value is 1, faults are detected.  
1This metric is a cumulative counter that shows monotonically increasing behavior for each session of the Oracle Cloud Agent software, resetting when the operating system is restarted. 2The Networking service provides more metrics (in the `oci_vcn` metric namespace) for each [VNIC](https://docs.oracle.com/iaas/Content/Network/Tasks/managingVNICs.htm) on the instance. For more information, see [Networking Metrics](https://docs.oracle.com/iaas/Content/Network/Reference/networkmetrics.htm).  3The Block Volume service provides more metrics (in the `oci_blockstore` metric namespace) for each volume attached to the instance. For more information, see [Block Volume Metrics](https://docs.oracle.com/iaas/Content/Block/References/volumemetrics.htm).   
## Using the Console 🔗 
[To view default metric charts for a single compute instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Metrics**.
  4. In the **Metric namespace** list, select **oci_computeagent**.
The Metrics page displays a default set of charts for the current instance.
[Not seeing any metric charts for the instance?](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm)
If you don't see any metric charts, the instance might not be emitting metrics. See the following possible causes and resolutions.
Possible cause | How to check | Resolution  
---|---|---  
The Compute Instance Monitoring plugin is disabled on the instance or plugins are stopped. | Review the instance properties. | [Enable the Compute Instance Monitoring plugin and start all plugins](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm).  
The instance can't access the Monitoring service because its VCN doesn't use the internet. | Review the instance's IP address. If it's not public, then a service gateway is needed.  | [Set up a service gateway](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm#prerequisites).  
The instance doesn't use a supported image. | Review the [supported images](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Availability).  | Create an instance with a [supported image](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm#Availability).  
Older images and custom images: No Oracle Cloud Agent software exists on the instance.  | Connect to the instance and look for the software. | [Install the Oracle Cloud Agent software](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins.htm#install-agent).  
Something else is wrong with the Oracle Cloud Agent software. | (not applicable) | [Follow the troubleshooting steps for Oracle Cloud Agent](https://docs.oracle.com/iaas/Content/Compute/Tasks/manage-plugins-troubleshooting.htm).  
For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).


[To view default metric charts for resources related to a compute instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm)
  * **For an attached block volume:** While viewing the instance's details, under **Resources** , click **Attached block volumes** , and then click the volume that you're interested in. Under **Resources** , click **Metrics** to see the volume's charts. For more information about the emitted metrics, see [Block Volume Metrics](https://docs.oracle.com/iaas/Content/Block/References/volumemetrics.htm).
  * **For the attached boot volume:** While viewing the instance's details, under **Resources** , click **Boot volume** , and then click the volume that you're interested in. Under **Resources** , click **Metrics** to see the volume's charts. For more information about the emitted metrics, see [Block Volume Metrics](https://docs.oracle.com/iaas/Content/Block/References/volumemetrics.htm).
  * **For an attached VNIC:** While viewing the instance's details, under **Resources** , click **Attached VNICs** , and then click the VNIC that you're interested in. Under **Resources** , click **Metrics** to see the charts for the VNIC. For more information about the emitted metrics, see [Networking Metrics](https://docs.oracle.com/iaas/Content/Network/Reference/networkmetrics.htm).


[To view default metric charts for all compute instances in a compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. Select a compartment.
  3. For **Metric namespace** , select **oci_computeagent**.
The **Service Metrics** page dynamically updates the page to show charts for each metric that is emitted by the selected metric namespace.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
[To view default metric charts for the instances in an instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computemetrics.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
  2. Click the instance pool that you're interested in.
  3. Under **Resources** , click **Metrics**.
  4. In the **Metric namespace** list, select **oci_computeagent**.
The Metrics page displays a default set of charts for the current instance pool.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

