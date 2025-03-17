Updated 2025-01-13
# Instance Pool Metrics
You can monitor the health, capacity, and performance of your Compute instance pools by using [metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics), [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).
This topic describes the metrics emitted by the metric namespace `oci_instancepools`.
Resources: Compute [instance pools](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/creatinginstancepool.htm#Creating_an_Instance_Pool).
## Overview of Metrics: oci_instancepools 🔗 
The instance pool metrics help you monitor the lifecycle state of instances in your instance pools.
### Required IAM Policy 🔗 
To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies). 
## Available Metrics: oci_instancepools 🔗 
The metrics listed in the following table are automatically available for each instance pool that you create. You do not need to enable monitoring on the instances in the pool to get these metrics.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
Depending on the metric, the following **dimensions** are available: 

AvailabilityDomain
    The **availability domain** where the instance pool resides. 

DisplayName
    The friendly name of the instance pool. 

FaultDomain
    The **fault domain** where the instance pool resides. 

region
    The **region** where the instance pool resides. 

resourceId
    The **OCID** of the instance pool.
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`InstancePoolSize` | **Instance Pool Size** | instances | Number of instances in the pool. |  `DisplayName` `region` `resourceId`  
`ProvisioningInstances` | **Instances Provisioning** | instances | Number of instances in the pool that are provisioning. |  `AvailabilityDomain` `DisplayName` `FaultDomain` `region` `resourceId`  
`RunningInstances` | **Instances Running** | instances | Number of running instances in the pool. |  `AvailabilityDomain` `DisplayName` `FaultDomain` `region` `resourceId`  
`TerminatedInstances` | **Instances Terminated** | instances | Number of instances in the pool that are terminating or terminated. |  `AvailabilityDomain` `DisplayName` `FaultDomain` `region` `resourceId`  
## Using the Console 🔗 
[To view default metric charts for a single instance pool](https://docs.oracle.com/en-us/iaas/Content/Compute/References/instancepoolmetrics.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instance Pools**.
  2. Click the instance pool that you're interested in.
  3. Under **Resources** , click **Metrics**.
  4. In the **Metric namespace** list, select **oci_instancepools**.
The Metrics page displays a default set of charts for the current instance pool.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
[To view default metric charts for all instance pools in a compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/References/instancepoolmetrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. Select a compartment.
  3. For **Metric namespace** , select `oci_instancepools`.
The **Service Metrics** page dynamically updates the page to show charts for each metric that is emitted by the selected metric namespace.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

