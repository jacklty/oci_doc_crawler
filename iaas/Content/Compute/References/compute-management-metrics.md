Updated 2025-01-13
# Compute Management Metrics
You can monitor requests to the instance metadata service on compute virtual machine (VM) and bare metal instances by using [metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics), [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and [notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm).
This topic describes the metrics emitted by the metric namespace `oci_compute`.
Resources: compute instances.
## Overview of Metrics: oci_compute 🔗 
The [instance metadata service (IMDS)](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#Getting_Instance_Metadata) provides metadata about an instance, its attached VNICs, and custom metadata that you supply. IMDS is available in two versions, version 1 and version 2. IMDSv2 offers increased security compared to the legacy v1.
Use the Compute management metric to identify requests to the legacy v1 endpoints. After you migrate any applications to support the v2 endpoints, you can [disable all requests to the legacy v1 endpoints](https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/gettingmetadata.htm#upgrading-v2__disable-legacy).
### Required IAM Policy 🔗 
To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to the monitoring services as well as the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies). 
## Available Metrics: oci_compute 🔗 
The metric listed in the following table is automatically available for your instances. You do not need to enable monitoring on the instance to get this metric.
You also can use the Monitoring service to create custom queries. See [Building Metric Queries](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
The metric includes the following **dimensions** : 

metadataVersion
    The version of the instance metadata service that requests were made to. 

path
    The URL path that instance metadata requests were made to. 

resourceId
    The **OCID** of the instance. 

userAgent
    The source of the instance metadata request. 

status
    The HTTP response code for requests to instance metadata service.
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`InstanceMetadataRequests` | **Instance Metadata Requests V1 Versus V2** | Sum | The number of requests to the instance metadata service, comparing the version 1 and version 2 endpoints. |  `metadataVersion` `path` `resourceId` `userAgent` `status`  
## Using the Console 🔗 
[To view management metrics for a single compute instance](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-management-metrics.htm)
  1. Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Click the instance that you're interested in.
  3. Under **Resources** , click **Metrics**.
  4. In the **Metric namespace** list, select **oci_compute**.
The Metrics page displays a default set of charts for the current instance.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
[To view management metrics for all compute instances in a compartment](https://docs.oracle.com/en-us/iaas/Content/Compute/References/compute-management-metrics.htm)
  1. Open the **navigation menu** and select **Observability & Management**. Under **Monitoring** , select **Service Metrics**. 
  2. Select a compartment.
  3. For **Metric namespace** , select **oci_compute**.
The **Service Metrics** page dynamically updates to show charts for each metric that is emitted by the selected metric namespace.


For more information about monitoring metrics and using alarms, see [Overview of Monitoring](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm). For information about notifications for alarms, see [Overview of Notifications](https://docs.oracle.com/iaas/Content/Notification/Concepts/notificationoverview.htm).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following APIs for monitoring:
  * [Monitoring API](https://docs.oracle.com/iaas/api/#/en/monitoring/latest/) for metrics and alarms 
  * [Notifications API](https://docs.oracle.com/iaas/api/#/en/notification/latest/) for notifications (used with alarms)


Was this article helpful?
YesNo

