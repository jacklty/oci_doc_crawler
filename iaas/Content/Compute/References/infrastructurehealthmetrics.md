Updated 2025-01-13
# Infrastructure Health Metrics
You can monitor the health, capacity, and performance of the infrastructure for your compute virtual machine (VM) and bare metal instances by using [metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics), [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).
This topic describes the metrics emitted by the metric namespace `oci_compute_infrastructure_health`.
Resources: Compute instances.
## Overview of Metrics: oci_compute_infrastructure_health 🔗 
The compute infrastructure health metrics help you monitor the status and health of compute instances.
  * **Instance health (up/down) status:** The `instance_status` metric lets you check whether a VM instance is available (up) or unavailable (down) when in the running state. If the instance is unavailable for more than 30 minutes, [contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm).
  * **Instance maintenance status:** The `maintenance_status` metric lets you monitor whether a VM or bare metal instance is scheduled for [planned infrastructure maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#planned-maintenance__vm-planned-maintenance).
  * **Bare metal infrastructure health status:** The `health_status` metric helps you monitor the [health of the infrastructure](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm#Compute_Health_Monitoring_for_Bare_Metal_Instances) for bare metal instances, including hardware components such as the CPU and memory.


Based on the value of the metrics, you can proactively [move affected instances to healthy hardware](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#Moving_a_Compute_Instance_to_a_New_Host) and thereby minimize the impact on your applications.
### Required IAM Policy 🔗 
To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies). 
## Available Metrics: oci_compute_infrastructure_health 🔗 
The metrics listed in the following table are automatically available for your instances. You do not need to enable monitoring on the instance to get these metrics.
You also can use the Monitoring service to create [custom queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/query-metric.htm).
Depending on the metric, the following **dimensions** are available: 

faultClass
    
The type of hardware issue:
  * `CPU`: A fault has been detected in one or more CPUs.
  * `MEM-BOOT`: A fault in the memory subsystem was detected during instance launch or a recent reboot. 
  * `MEM-RUNTIME`: A fault in the memory subsystem was detected.
  * `MGMT-CONTROLLER`: A fault in the instance management controller has been detected.
  * `PCI`: A fault in the PCI subsystem has been detected.
  * `PCI-NIC`: A fault in the instance network interface card (NIC) has been detected.
**Important** The `PCI-NIC` fault class is [deprecated](https://docs.oracle.com/iaas/Content/servicechanges.htm#compute-pci-nic-fault-class). You should migrate to the `PCI` fault class for similar functionality.
  * `SDN-INTERFACE`: A fault in the instance software defined network interface has been detected.

    
For troubleshooting suggestions and more information about these hardware issues, see [Compute Health Monitoring for Bare Metal Instances](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computehealthmonitoringguidance.htm#Compute_Health_Monitoring_for_Bare_Metal_Instances). 

resourceDisplayName
    The friendly name of the instance. 

resourceId
    The **OCID** of the instance. 

maintenanceDueTime
    
The scheduled start time of the 24-hour maintenance window, in the format defined by [RFC3339](https://datatracker.ietf.org/doc/html/rfc3339). 

computeMaintenanceAction
    
The action that Oracle Cloud Infrastructure will perform on an instance during a [scheduled maintenance event](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructure-maintenance.htm#infrastructure-maintenance):
  * `REBOOT`: The instance is migrated from the physical host that needs maintenance to a healthy host. If live migration is not possible, then the instance is reboot migrated.
  * `REBUILD_IN_PLACE`: The instance is stopped, rebuilt on the same physical hardware, and restarted. A downtime of several hours occurs during the maintenance process.



recommendedAction
    
The action that you can take before the scheduled maintenance event, so that you can control how and when your applications experience downtime.
  * `REBOOT`: You can proactively reboot the instance before the scheduled maintenance time. When you [reboot migrate an instance for maintenance](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/movinganinstance.htm#reboot), the instance is stopped on the physical host that needs maintenance, and then restarted on a healthy host.


Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`health_status` | **Infrastructure Health Status** | Issues |  The number of health issues for an instance. Any non-zero value indicates a health defect. This metric is available only for bare metal instances. |  `faultClass` `resourceDisplayName` `resourceId`  
`instance_status` | **Instance Status** | Count |  The status of a running instance. A value of 0 indicates that the instance is available (up). A value of 1 indicates that the instance is not available (down) due to an infrastructure issue. If the instance is stopped, then the metric does not have a value. This metric is available only for VM instances. |  `resourceDisplayName` `resourceId`  
`maintenance_status` | **Maintenance Status** | Count |  The maintenance status of an instance. A value of 0 indicates that the instance is not scheduled for an infrastructure maintenance event. A value of 1 indicates that the instance is scheduled for an infrastructure maintenance event. This metric is available for both VM and bare metal instances. |  `maintenanceDueTime` `computeMaintenanceAction ` `recommendedAction` `resourceDisplayName` `resourceId`  
## Using the Console 🔗 
[To view infrastructure health metrics for a single compute instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructurehealthmetrics.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Metrics**.
  4. In the **Metric namespace** list, select **oci_compute_infrastructure_health**.
The Metrics page displays a default set of charts for the current instance.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
[To view infrastructure health metrics for all compute instances in a compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/References/infrastructurehealthmetrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. Select a compartment.
  3. For **Metric namespace** , select **oci_compute_infrastructure_health**.
The **Service Metrics** page dynamically updates to show charts for each metric that is emitted by the selected metric namespace.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

