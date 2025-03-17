Updated 2024-03-22
# Block Volume Metrics
You can monitor the performance and replication status for your Block Volume resources by using **metrics** , **alarms** , and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
This topic describes the metrics emitted by the metric namespace `oci_blockstore` (the Block Volume service)
Resources:
  * Block volumes
  * Boot volumes
  * Block volume replicas
  * Boot volume replicas
  * Volume group replicas


## Overview of Metrics for an Instance and Its Storage Devices 🔗 
If you're not already familiar with the different types of metrics available for an instance and its storage and network devices, see [Compute Instance Metrics](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm).
## Available Metrics: oci_blockstore 🔗 
The Block Volume service includes metrics related to volume [performance](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm#perfmetrics) and metrics related to volume [replication](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm#replicatmetrics).
### Performance Metrics 🔗 
The Block Volume service emits metrics to help you measure volume operations and throughput related to compute instances. 
The metrics listed in the following table are automatically available for any block volume or boot volume, regardless of whether the attached instance has [monitoring enabled](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm). You do not need to enable monitoring on the volumes to get these metrics.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
Each metric includes at least one of the following **dimensions** : 

ATTACHMENTID
    The **OCID** of the volume attachment.  

RESOURCEID
    The **OCID** of the volume. 
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`VolumeReadThroughput`*  | **Volume Read Throughput** | bytes | Read throughput. Expressed as bytes read per interval. |  `attachmentId` `resourceId`  
`VolumeWriteThroughput`*  | **Volume Write Throughput** | bytes | Write throughput. Expressed as bytes written per interval.  
`VolumeReadOps`*  | **Volume Read Operations** | reads | Activity level from I/O reads. Expressed as reads per interval.  
`VolumeWriteOps`*  | **Volume Write Operations** | writes | Activity level from I/O writes. Expressed as writes per interval.  
`VolumeThrottledIOs`* | **Volume Throttled Operations** | sum | Total sum of all the I/O operations that were throttled during a given time interval.  
`VolumeGuaranteedVPUsPerGB`* | **Volume Guaranteed VPUs/GB** | VPUs | Rate of change for currently active VPUs/GB. Expressed as the average of active VPUs/GB during a given time interval. |  `resourceId`  
`VolumeGuaranteedIOPS`* | **Volume Guaranteed IOPS** | IOPS | Rate of change for guaranteed IOPS per SLA. Expressed as the average of guaranteed IOPS during a given time interval.  
`VolumeGuaranteedThroughput`* | **Volume Guaranteed Throughput** | megabytes | Rate of change for guaranteed throughput per SLA. Expressed as megabytes per interval.  
* The Compute service separately reports network-related metrics _as measured on the instance itself and aggregated across all the attached volumes_. Those metrics are available in the `oci_computeagent` metric namespace. For more information, see [Compute Instance Metrics](https://docs.oracle.com/iaas/Content/Compute/References/computemetrics.htm). 
### Replication Metrics 🔗 
The Block Volume service emits metrics to help you track volume replication operations. The metric emitted is determined by the resource type, either a [volume resource](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm#replicatmetrics__volumeresources) or a [replica resource](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm#replicatmetrics__replicationresources).
Each metric includes the following **dimension** : 

RESOURCEID
    The **OCID** of the replica resource or cross region replication enabled-volume resource.
#### Volume Resources 🔗 
The metric listed in the following table is automatically available for any volume resource with cross region replication enabled. This includes block volumes, boot volumes, and volume groups. You do not need to enable monitoring on volumes.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
Each metric includes the following **dimension** :
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`VolumeReplicationSecondsSinceLastUpload` | **Time since last cross region replica upload** | seconds | Time elapsed since the last cross region replica was uploaded. Expressed in seconds. |  `resourceId`  
#### Replica Resources 🔗 
The metric listed in the following table is automatically available for any replica resource, including block volume replicas, boot volume replicas, or volume group replicas. You do not need to enable monitoring on replicas to get these metrics.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
Each metric includes the following **dimension** : 

RESOURCEID
    The **OCID** of the replica or cross region replication enabled-volume. 
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`VolumeReplicationSecondsSinceLastSync` | **Time since last cross region replica was synced** | seconds | Time elapsed since the last synced cross region replica. Expressed in seconds. |  `resourceId`  
## Using the Console 🔗 
[To view default metric charts for a single volume](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm)
  1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
  2. Click the instance to view its details.
  3. Under **Resources** , click either **Attached Block Volumes** or **Boot Volume** to view the volume you're interested in. 
  4. Click the volume to view its details.
  5. Under **Resources** , click **Metrics**.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
[To view the default metric chart for a single replica](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Replicas**. 
  2. Click the replica to view its details.
  3. Under **Resources** , click **Metrics**.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
[To view default metric charts for multiple volumes](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm)
  1. Open the navigation menu and click **Observability & Management**. Under **Monitoring** , click **Service Metrics**. 
  2. For **Compartment** , select the compartment that contains the volumes you're interested in.
  3. For **Metric namespace** , select **oci_blockstore**.
The **Service Metrics** page dynamically updates the page to show charts for each metric that is emitted by the selected metric namespace. 


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

