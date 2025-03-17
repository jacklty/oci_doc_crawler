Updated 2025-02-11
# Agentless Compute Metrics
This topic describes the metrics emitted by the private agentless metric namespace `oci_vmi_resource_utilization`.
You can monitor the health, capacity, and performance of your compute virtual machine (VM) instances by using [metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics), [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).
**Note** If the [Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics) service is down, data may be lost until the service is restored.
## Overview of Metrics: oci_vmi_resource_utilization 🔗 
The following agentless compute metric helps you monitor the status of compute instances without the use of Oracle Cloud Agent. Instead, this metric pulls from hypervisor. 
Hypervisor (also known as the VMM) measures CPU utilization as it allocates CPU resources to the virtual machines (VMs) running on it. The Oracle Cloud Agent metrics offer detailed information and update every few seconds, while hypervisor metrics provide broader data, that average over several minutes. Because there are multiple sources that collect the metrics by using different methods, the values may differ. To monitor CPU usage with minute-level accuracy, you can use the hypervisor metric instead of installing the Oracle Cloud Agent monitoring tools.
### Required IAM Policy 🔗 
To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies). 
## Available Metrics: oci_vmi_resource_utilization 🔗 
The metrics listed in the following table is automatically available for your instances. You do not need to enable monitoring on the instance to get these metrics. When you use the metric from hypervisor, it does not impact the use of Oracle Cloud Agent metrics.
**Note** Hypervisor runs in the background even when the VM is in a stopped state. This can cause some CPU utilization to display on a VM in a stopped state. 
The metric includes the following **dimensions** : 

resourceId
    The **OCID** of the instance.
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`CpuUtilization` | **CPU Utilization** | percent |  Activity level from CPU. Expressed as a percentage of total time. For instance pools, the value is averaged across all instances in the pool. |  `resourceId`  
### Private and public namespace metrics
The metric available with a private namespace (`oci_vmi_resource_utilization`) has a different granularity and resolution intervals than the metrics available with a public namespace. For example, you can also get the metric of `CPU Utilization` from `oci_computeagent`, however, how that metric is collected is different and will not be identical to the `CPU Utilization` collected with `oci_vmi_resource_utilization`.
**Note** Because there are multiple sources that collect the metrics by using different methods, the values may differ. To monitor CPU usage with minute-level accuracy, you can use the hypervisor metric instead of installing the Oracle Cloud Agent monitoring tools.
The table below is an example of metrics and their differing support and means of collection. 
Metric | Source | Granularity | Resolution Interval | Console Support | Terraform Support  
---|---|---|---|---|---  
`CPU Utilization` | Hypervisor  | `CPU Utilization (User)` | Every 3-4 minutes | Yes | Yes  
`CPU Utilization` | OCA | `CPU Utilization (User)``Idle``Wait``System` | Every 60 seconds | Yes | Yes  
`Memory Utilization` | OCA | `Total``Used``Free``Shared``Cached``Available` | Every 60 seconds | Yes | Yes  
`Disk Utilization` | OCA | `Utilization across mount points and infrastructure`This is not the same as the `df` and `du` command output at the individual host level. | Every 60 seconds | Yes | Yes  
`Disk I/O` |  OCA |  `Reads/writes ops` `Reads/writes bytes` `Reads/writes times` | Every 60 seconds | Yes | Yes  
`VNIC` | VNIC |  `Byte traversal` `Packet traversal` `Protocol distribution` `Connection tracking ` | Every 60 seconds | Yes | Yes  
Was this article helpful?
YesNo

