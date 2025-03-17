Updated 2024-06-06
# Details for Monitoring
This topic covers details for writing policies to control access to the Monitoring service.
## Resource-Types 🔗 
`alarms`
`metrics`
## Supported Variables 🔗 
Monitoring supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")), plus the one listed here:
Operations for This Resource-Type... | Can Use This Variable | Variable Type | Comments  
---|---|---|---  
`metrics` | `target.metrics.namespace` | String |  Use this variable to control access to specific resource types. Surround the namespace value with single quotes. For example, to control access to metrics for compute instances, use the following phrase: `where target.metrics.namespace='oci_computeagent'` For an example policy, see [Restrict user access to a specific metric namespace](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm#metrics-computeonly). For valid namespace values, see [Supported Services](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices).  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
[alarms](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/monitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | ALARM_INSPECT | `ListAlarms` `ListAlarmsStatus` `RetrieveDimensionStates` | none  
read | INSPECT + ALARM_READ | `GetAlarmHistory` | `GetAlarm` (also need `METRIC_READ` for the metric compartment and metric namespace)   
use | READ + no extra | no extra | none  
manage | USE + ALARM_CREATE ALARM_UPDATE ALARM_DELETE ALARM_MOVE | `ChangeAlarmCompartment` `DeleteAlarm` `RemoveAlarmSuppression` | `CreateAlarm` (also need `METRIC_READ` for the metric compartment and metric namespace) `UpdateAlarm` (also need `METRIC_READ` for the metric compartment and metric namespace)  
[metrics](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/monitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | METRIC_INSPECT | `ListMetrics` | none  
read | INSPECT + METRIC_READ | `SummarizeMetricsData` | none  
use | READ + METRIC_WRITE | `PostMetricData` | none  
manage | USE + no extra | no extra | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.").
API Operation | Permissions Required to Use the Operation  
---|---  
`ListMetrics` | METRIC_INSPECT  
`SummarizeMetricsData` | METRIC_INSPECT and METRIC_READ  
`PostMetricData` | METRIC_WRITE  
`ListAlarms` | ALARM_INSPECT  
`ListAlarmsStatus` | ALARM_INSPECT  
`GetAlarm` | ALARM_READ and METRIC_READ  
`GetAlarmHistory` | ALARM_READ  
`CreateAlarm` | ALARM_CREATE and METRIC_READ  
`ChangeAlarmCompartment` | ALARM_MOVE  
`UpdateAlarm` | ALARM_UPDATE and METRIC_READ  
`RemoveAlarmSuppression` | ALARM_UPDATE  
`DeleteAlarm` | ALARM_DELETE  
`RetrieveDimensionStates` | ALARM_INSPECT  
Was this article helpful?
YesNo

