Updated 2025-01-13
# Compute Instance Health Metrics
You can monitor the health, capacity, and performance of your compute virtual machine (VM) instances by using [metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics), [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).
This topic describes the metrics emitted by the metric namespace `oci_compute_instance_health`.
Resources: Compute VM instances.
## Overview of Metrics: oci_compute_instance_health 🔗 
The following compute instance health metric helps you monitor the status, health, and accessibility of compute instances.
**Instance accessibility status:** The `instance_accessibility_status` metric lets you monitor whether a VM instance is unresponsive. Compute sends an Address Resolution Protocol (ARP) request to the instance's virtual network interface card (VNIC). If the ARP ping fails, the metric shows that the instance is unresponsive.
**Note** The `instance_accessibility_status` metric doesn't determine or report the specific reason for the instance's unresponsiveness. The ARP test provides no insight into the possible issues with the instance's OS.
**Instance File System Status:** The `instance_file_system_status` metric lets you monitor whether a VM instance has file system anomaly issue. Compute analyzes VM kernel logs to determine volume status. If the volume is in anomaly status, the metric shows the type and volume of the issue.
**Note** The `instance_file_system_status` metric does not determine or report the specific reason for the file system issue of the instance or issues with the OS or volumes of the instance.
[Using MQL to view instance_file_system_status](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-health-metrics.htm)
```
// The query does not specify the volume type, it can be used for general monitoring purpose of read-only volume issues. Users can get volumeType info by inspecting the "volumeType" dimension of the metrics. 
InstanceFileSystemStatus[5m]{resourceId = "YOUR-VM-OCID-IN-TENANCY"}.max()
// The queries below specify the volume type, they can be used for specific monitoring purposes
InstanceFileSystemStatus[5m]{resourceId = "YOUR-VM-OCID-IN-TENANCY", volumeType = BOOT_VOLUME}.max()
InstanceFileSystemStatus[5m]{resourceId = "YOUR-VM-OCID-IN-TENANCY", volumeType = DATA_VOLUME}.max()
InstanceFileSystemStatus[5m]{resourceId = "YOUR-VM-OCID-IN-TENANCY", volumeType = UNKNOWN}.max()
```

[Troubleshooting an unresponsive VM instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-health-metrics.htm)
  1. Check the [infrastructure health metrics](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructurehealthmetrics.htm#Infrastructure_Health_Metrics) to determine whether there is an ongoing infrastructure issue. If there is an ongoing infrastructure issue, then wait until Oracle Cloud Infrastructure resolves the issue, and then check the `instance_accessibility_status` metric again.
  2. If there isn't an ongoing infrastructure issue, then the instance probably has a software issue or a network misconfiguration that you must resolve yourself. Confirm that the OS and network are configured correctly. See the [Compute troubleshooting suggestions](https://docs.oracle.com/en-us/iaas/Content/Compute/References/troubleshooting-compute-instances.htm#troubleshooting-compute-instances) and [Networking troubleshooting suggestions](https://docs.oracle.com/iaas/Content/Network/Concepts/troubleshooting.htm).
  3. If the Compute and Networking troubleshooting steps aren't successful, then you can use a [diagnostic reboot](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/diagnostic-reboot.htm#diagnostic-reboot) to rebuild an unreachable instance.


### Required IAM Policy 🔗 
To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies). 
## Available Metrics: oci_compute_instance_health 🔗 
The metrics listed in the following table is automatically available for your instances. You do not need to enable monitoring on the instance to get these metrics.
You also can use the Monitoring service to create [custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).
The metrics includes the following **dimensions** : 

resourceDisplayName
    The friendly name of the instance. 

resourceId
    The **OCID** of the instance. 

volumeType
    The type of volume that has an issue. The values are among `BOOT_VOLUME, DATA_VOLUME,` and `UNKNOWN`. When the value is `UNKNOWN`, the type of volume with an issue cannot be determined. 

issueType
    The type of file system issue. The value is `READ_ONLY` when the instance volume is in `READ_ONLY` mode.
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`instance_accessibility_status` | **Instance accessibility status** | Count | The accessibility status of a VM instance. A value of 1 indicates that the instance is unresponsive due to an issue with the infrastructure or the instance itself. A value of 0 indicates that an accessibility issue has not been detected. If the instance is stopped, then the metric does not have a value. |  `resourceDisplayName` `resourceId`  
`instance_file_system_status` | **Instance file system status** | Count |  The file system status of a VM instance. A value of 1 indicates that the instance has file system issue due to the infrastructure or the instance itself. A value of 0 indicates that the file system issue has not been detected. If the instance is stopped, then the metric does not have a value. |  `resourceDisplayName` `resourceId` `volumeType` `issueType`  
## Using the Console 🔗 
[To view compute health metrics for a single instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-health-metrics.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Metrics**.
  4. In the **Metric namespace** list, select **oci_compute_instance_health**.
The Metrics page displays a default set of charts for the current instance.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
[To view compute health metrics for all instances in a compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-health-metrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. Select a compartment.
  3. For **Metric namespace** , select **oci_compute_instance_health**.
The **Service Metrics** page dynamically updates to show charts for each metric that is emitted by the selected metric namespace.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

