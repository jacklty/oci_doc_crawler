Updated 2025-03-10
# DNS Metrics
Learn about the metrics emitted by the metric namespace `oci_dns` (the DNS service).
You can monitor the health, capacity, and performance of DNS services by using [metrics](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics), [alarms](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms), and [Notifications](https://docs.oracle.com/iaas/Content/Notification/home.htm). 
This topic describes the metrics emitted by the metric namespace `oci_dns` (the DNS service). 
## Overview of DNS Service Metrics 🔗 
The DNS service metrics help you measure the number of queries and zone transfers for DNS **zones** and DNS zones with [Overview of Traffic Management](https://docs.oracle.com/en-us/iaas/Content/TrafficManagement/Concepts/overview.htm#overview "Traffic Management helps you guide traffic to endpoints based on various conditions, including endpoint health and the geographic origins of DNS requests.") policies attached.
## Prerequisites 🔗 
  * IAM policies: To monitor resources, you must be granted the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. The policy must give you access to both the monitoring services and the resources being monitored. If you try to perform an action and get a message that you don't have permission or are unauthorized, contact the administrator to find out what type of access you were granted and which **compartment** you need to work in. For more information about user authorizations for monitoring, see [IAM Policies](https://docs.oracle.com/iaas/Content/Security/Reference/monitoring_security.htm#iam-policies).


## Available Metrics: oci_dns 🔗 
The metrics listed in the following table are automatically available. You don't need to enable monitoring on the resource to get these metrics. 
Each metric includes one or more of the following dimensions:  

resourceID
    The **OCID** of the zone to which the metric applies. 

resourceName
    The name of the zone to which the metric applies.
Metric | Metric Display Name | Unit | Description | Dimensions  
---|---|---|---|---  
`DNSQueryCount ` | **DNSQueryCount** | count | The number of queries for a DNS zone.  |  `resourceID`  
`TrafficManagementQueryCount ` | **TrafficManagementQueryCount** | count | The number of queries for a zone with Traffic Management policies attached.  |  `resourceID`  
`ZoneTransferFailureCount` | **Zone Transfer Failure Count** | count | The number of zone transfers that failed in a specified interval. |  `resourceID, resourceName`  
`ZoneTransferSuccessCount` | **Zone Transfer Success Count** | count | The number of successful zone transfers in a specified interval. |  `resourceID, resourceName`  
`ZoneExpirationInHours` | **Zone Expiration Time in Hours** | hours |  The number of hours until an OCI DNS secondary zone expires. **Note:** This metric is only emitted at 72 hours, 24 hours, 6 hours, 3 hours, 2 hours and 1 hour until zone expiration. |  `resourceID, resourceName`  
`DaysUntilDnssecKeyVersionExpiration` | **Days Until DNSSEC Key Version Expiration** | count | The number of days until the current DNSSEC Key version expires. | `RequiresPromotion`  
### Metrics Tasks 🔗 
  * [Viewing Metrics for the DNS Service](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/view-dns-metrics.htm#view-metrics "View metrics for the DNS service.")
  * [Viewing Metrics for a Zone](https://docs.oracle.com/en-us/iaas/Content/DNS/Reference/dnsmetric_topic-view-zone-metrics.htm#view-zone-metrics "View metrics for a DNS zone.")


Was this article helpful?
YesNo

