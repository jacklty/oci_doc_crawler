Updated 2025-03-11
# Details for Stack Monitoring
This topic covers details for writing policies to control access to the Stack Monitoring service.
## Individual Resource-Types 🔗 
`appmgmt-monitored-instance`
`appmgmt-work-request`
`stack-monitoring-resource`
`stack-monitoring-resource-type `
`stack-monitoring-task`
`stack-monitoring-discovery-job`
`stack-monitoring-work-request`
`stack-monitoring-metric-extension `
`stack-monitoring-config`
`stack-monitoring-baselineable-metric`
`stack-monitoring-process-set`
`stack-monitoring-monitoring-template`
`stack-monitoring-defined-monitoring-template`
## Aggregate Resource-Types 🔗 
`appmgmt-family`
`stack-monitoring-family`
### Comments
See the table in [Permissions Required for each API Operation](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm#stackmonitoringpolicyreference_topic-Permissions_Required_for_Each_API_Operation) for details of the API operations covered by each verb, for each individual resource-type.
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)). 
## Details for Verb + Resource-Type Combinations 🔗 
The following tables shows the [permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.
[appmgmt-monitored-instance](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | APPMGMT_MONITORED_INSTANCE_INSPECT | `ListMonitoredInstances` | _none_  
read | _INSPECT +_ APPMGMT_MONITORED_INSTANCE_READ | `GetMonitoredInstance` | _none_  
use | _READ +_ APPMGMT_MONITORED_INSTANCE_PROCESS_PUBLISH | `PublishTopProcessesMetrics` | _none_  
manage | _USE +_ APPMGMT_MONITORED_INSTANCE_ACTIVATE | `ActivateMonitoringPlugin` | _none_  
[appmgmt-work-request](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | APPMGMT_WORK_REQUEST_INSPECT | `ListWorkRequests ``ListWorkRequestErrors``ListWorkRequestLogs` | _none_  
read | _INSPECT+_ APPMGMT_WORK_REQUEST_READ | `GetWorkRequest` | _none_  
[appmgmt-family](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  APPMGMT_MONITORED_INSTANCE_INSPECT APPMGMT_WORK_REQUEST_INSPECT | `ListMonitoredInstances ``ListWorkRequests``ListWorkRequestErrors``ListWorkRequestLogs` | _none_  
read | _INSPECT +_ APPMGMT_MONITORED_INSTANCE_READAPPMGMT_WORK_REQUEST_READ | `GetMonitoredInstance``GetWorkRequest` | _none_  
use | _READ +_ APPMGMT_MONITORED_INSTANCE_PROCESS_PUBLISH | `PublishTopProcessesMetrics` | _none_  
manage | _USE +_ APPMGMT_MONITORED_INSTANCE_ACTIVATE | `ActivateMonitoringPlugin` | _none_  
[stack-monitoring-resource](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  STACK_MONITORING_RESOURCE_INSPECT STACK_MONITORING_RESOURCE_ASSOC_INSPECT | `SearchMonitoredResources``SearchMonitoredResourceMembers``SearchMonitoredResourceAssociations` | _none_  
read | _INSPECT +_ STACK_MONITORING_RESOURCE_READ | `GetMonitoredResource` | _none_  
use | _READ +_ | _none_ | _none_  
manage | _USE +_ STACK_MONITORING_RESOURCE_CREATESTACK_MONITORING_RESOURCE_UPDATESTACK_MONITORING_RESOURCE_DELETESTACK_MONITORING_RESOURCE_MOVESTACK_MONITORING_RESOURCE_ASSOC_CREATESTACK_MONITORING_RESOURCE_ASSOC_DELETE | `CreateMonitoredResource``UpdateMonitoredResource` `DeleteMonitoredResource ``ChangeMonitoredResourceCompartment ``DisableExternalDatabase` `AssociateMonitoredResources ``DisassociateMonitoredResources` | _none_  
[stack-monitoring-resource-type](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STACK_MONITORING_RESOURCE_TYPE_INSPECT | `ListMonitoredResourceTypes` | _none_  
read | _INSPECT +_ STACK_MONITORING_RESOURCE_TYPE_READ | `GetMonitoredResourceType` | _none_  
use | _READ +_ | _none_ | _none_  
manage | _USE +_ STACK_MONITORING_RESOURCE_TYPE_CREATESTACK_MONITORING_RESOURCE_TYPE_UPDATESTACK_MONITORING_RESOURCE_TYPE_DELETE | `CreateMonitoredResourceType` `UpdateMonitoredResourceType` `DeleteMonitoredResourceType` | _none_  
[stack-monitoring-task](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STACK_MONITORING_TASK_INSPECT | `ListTasks` | _none_  
read | _INSPECT +_ STACK_MONITORING_TASK_READ | `GetTask` | _none_  
use | _READ +_ | _none_ | _none_  
manage | _USE +_ STACK_MONITORING_TASK_CREATESTACK_MONITORING_TASK_UPDATE STACK_MONITORING_TASK_DELETE STACK_MONITORING_TASK_MOVE | `CreateTask``UpdateTask``DeleteTask` `MoveTask` | _none_  
[stack-monitoring-discovery-job](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verb | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STACK_MONITORING_DISCOVERY_JOB_INSPECT | `ListDiscoveryJobs` | _none_  
read | _INSPECT +_ STACK_MONITORING_DISCOVERY_JOB_READ | `GetDiscoveryJob` | _none_  
use | _READ +_ | _none_ | _none_  
manage | _USE +_ STACK_MONITORING_DISCOVERY_JOB_CREATESTACK_MONITORING_DISCOVERY_JOB_DELETESTACK_MONITORING_DISCOVERY_JOB_RESULT_SUBMI T | `CreateDiscoveryJob``DeleteDiscoveryJob``SubmitDiscoveryJobResult``SubmitDiscoveryJobFailure` | _none_  
[stack-monitoring-work-request](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STACK_MONITORING_WORK_REQUEST_INSPECT | `ListWorkRequests``ListWorkRequestErrors``ListWorkRequestLogs` | _none_  
read | _INSPECT +_ STACK_MONITORING_WORK_REQUEST_READ | `GetWorkRequest` | _none_  
[stack-monitoring-metric-extension](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STACK_MONITORING_METRIC_EXTENSION_INSPECT | `ListMetricExtensions` | _none_  
read | _INSPECT +_ STACK_MONITORING_METRIC_EXTENSION_READ | `GetMetricExtension` | _none_  
use | _READ +_ STACK_MONITORING_METRIC_EXTENSION_ENABLESTACK_MONITORING_METRIC_EXTENSION_DISABLE | `EnableMetricExtension``DisableMetricExtension` | _none_  
manage | _USE +_ STACK_MONITORING_METRIC_EXTENSION_CREATESTACK_MONITORING_METRIC_EXTENSION_UPDATESTACK_MONITORING_METRIC_EXTENSION_DELETESTACK_MONITORING_METRIC_EXTENSION_TESTSTACK_MONITORING_METRIC_EXTENSION_PUBLISHSTACK_MONITORING_METRIC_EXTENSION_MOVE | `CreateMetricExtension``UpdateMetricExtension` `DeleteMetricExtension` `TestMetricExtension` `PublishMetricExtension` `ChangeMetricExtensionCompartment` | _none_  
[stack-monitoring-config](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STACK_MONITORING_CONFIG_INSPECT | `ListConfigs` | _none_  
read | _INSPECT +_ STACK_MONITORING_CONFIG_READ | `GetConfig` | _none_  
use | _READ +_ | _none_ | _none_  
manage | _USE +_ STACK_MONITORING_CONFIG_CREATESTACK_MONITORING_CONFIG_UPDATESTACK_MONITORING_CONFIG_DELETESTACK_MONITORING_CONFIG_MOVE | `CreateConfig``UpdateConfig` `DeleteConfig``ChangeConfigCompartment` | _none_  
[stack-monitoring-baselineable-metric](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STACK_MONITORING_BASELINEABLE_METRIC_INSPECT | `ListBaselineableMetrics` | _none_  
read | _INSPECT +_ STACK_MONITORING_BASELINEABLE_METRIC_READ | `GetBaselineableMetric` | _none_  
use | _READ +_ STACK_MONITORING_BASELINEABLE_METRIC_EVALUAT E | `EvaluateBaselineableMetric` | _none_  
manage | _USE +_ STACK_MONITORING_BASELINEABLE_METRIC_CREATESTACK_MONITORING_BASELINEABLE_METRIC_UPDATESTACK_MONITORING_BASELINEABLE_METRIC_DELETE |  `CreateBaselineableMetric` `UpdateBaselineableMetric` `DeleteBaselineableMetric` | _none_  
[stack-monitoring-process-set](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STACK_MONITORING_PROCESS_SET_INSPECT | `ListProcessSets` | _none_  
read | _INSPECT +_ STACK_MONITORING_PROCESS_SET_READ | `GetProcessSet` | _none_  
use | _READ +_ | _none_ | _none_  
_USE +_ STACK_MONITORING_PROCESS_SET_CREATESTACK_MONITORING_PROCESS_SET_UPDATESTACK_MONITORING_PROCESS_SET_DELETESTACK_MONITORING_PROCESS_SET_MOVE | `CreateProcessSet``UpdateProcessSet` `DeleteProcessSet` `ChangeProcessSetCompartment` | _none_  
[stack-monitoring-monitoring-template](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  STACK_MONITORING_MONITORING_TEMPLATE_INSPECT STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_INSPECT |  `ListMonitoringTemplates` `ListAlarmConditions` | _none_  
read | _INSPECT +_ STACK_MONITORING_MONITORING_TEMPLATE_READSTACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_READ |  `GetMonitoringTemplate` `GetAlarmCondition` | _none_  
use | _READ +_ STACK_MONITORING_MONITORING_TEMPLATE_APPLYSTACK_MONITORING_MONITORING_TEMPLATE_UNAPPLY |  `ApplyMonitoringTemplate` `UnapplyMonitoringTemplate` | _none_  
manage | _USE +_ STACK_MONITORING_MONITORING_TEMPLATE_CREATESTACK_MONITORING_MONITORING_TEMPLATE_UPDATESTACK_MONITORING_MONITORING_TEMPLATE_DELETESTACK_MONITORING_MONITORING_TEMPLATE_EXPORTSTACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_CREATESTACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_UPDATESTACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_DELETE |  `CreateMonitoringTemplate` `UpdateMonitoringTemplate` `DeleteMonitoringTemplate` `ExportMonitoringTemplate` `CreateAlarmCondition` `UpdateAlarmCondition` `DeleteAlarmCondition` | _none_  
[stack-monitoring-defined-monitoring-template](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  STACK_MONITORING_DEFINED_MONITORING_TEMPLATE_INSPECT | `ListDefinedMonitoringTemplates` | _none_  
[stack-monitoring-family](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/stackmonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | STACK_MONITORING_RESOURCE_INSPECTSTACK_MONITORING_RESOURCE_ASSOC_INSPECTSTACK_MONITORING_RESOURCE_TYPE_INSPECTSTACK_MONITORING_PROCESS_SET_INSPECTSTACK_MONITORING_BASELINEABLE_METRIC_INSPECTSTACK_MONITORING_CONFIG_INSPECTSTACK_MONITORING_METRIC_EXTENSION_INSPECTSTACK_MONITORING_WORK_REQUEST_INSPECTSTACK_MONITORING_DISCOVERY_JOB_INSPECTSTACK_MONITORING_TASK_INSPECTSTACK_MONITORING_MONITORING_TEMPLATE_INSPECTSTACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_INSPECTSTACK_MONITORING_DEFINED_MONITORING_TEMPLATE_INSPECT | `SearchMonitoredResources``SearchMonitoredResourceMembers``SearchMonitoredResourceAssociations``ListMonitoredResourceTypes` `ListTasks``ListDiscoveryJobs``ListWorkRequests``ListWorkRequestErrors``ListWorkRequestLogs``ListMetricExtensionsListConfigs``ListBaselineableMetrics``ListProcessSets``ListMonitoringTemplates``ListAlarmConditions``ListDefinedMonitoringTemplates` | _none_  
read | _INSPECT +_ STACK_MONITORING_RESOURCE_READ STACK_MONITORING_RESOURCE_TYPE_READSTACK_MONITORING_TASK_READSTACK_MONITORING_DISCOVERY_JOB_READ STACK_MONITORING_WORK_REQUEST_READSTACK_MONITORING_METRIC_EXTENSION_READSTACK_MONITORING_CONFIG_READSTACK_MONITORING_BASELINEABLE_METRIC_READSTACK_MONITORING_PROCESS_SET_READSTACK_MONITORING_MONITORING_TEMPLATE_READSTACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_READ | `GetMonitoredResource``GetMonitoredResourceType``GetTask``GetDiscoveryJob``GetWorkRequest` `GetMetricExtension``GetConfig` `GetBaselineableMetric``GetProcessSet``GetMonitoringTemplate``GetAlarmCondition` | _none_  
use | _READ +_ STACK_MONITORING_METRIC_EXTENSION_ENABLESTACK_MONITORING_METRIC_EXTENSION_DISABLESTACK_MONITORING_BASELINEABLE_METRIC_EVALUATESTACK_MONITORING_MONITORING_TEMPLATE_APPLYSTACK_MONITORING_MONITORING_TEMPLATE_UNAPPLY | `EnableMetricExtension``DisableMetricExtension``EvaluateBaselineableMetric``ApplyMonitoringTemplate``UnapplyMonitoringTemplate` | _none_  
manage | _USE +_ STACK_MONITORING_RESOURCE_CREATESTACK_MONITORING_RESOURCE_UPDATESTACK_MONITORING_RESOURCE_DELETE STACK_MONITORING_RESOURCE_MOVESTACK_MONITORING_RESOURCE_ASSOC_CREATE STACK_MONITORING_RESOURCE_ASSOC_DELETE STACK_MONITORING_RESOURCE_TYPE_CREATE STACK_MONITORING_RESOURCE_TYPE_UPDATESTACK_MONITORING_RESOURCE_TYPE_DELETE STACK_MONITORING_TASK_CREATESTACK_MONITORING_TASK_UPDATE STACK_MONITORING_TASK_DELETE STACK_MONITORING_TASK_MOVESTACK_MONITORING_DISCOVERY_JOB_CREATE STACK_MONITORING_DISCOVERY_JOB_DELETE STACK_MONITORING_DISCOVERY_JOB_RESULT_SUBMITSTACK_MONITORING_METRIC_EXTENSION_CREATESTACK_MONITORING_METRIC_EXTENSION_UPDATESTACK_MONITORING_METRIC_EXTENSION_DELETESTACK_MONITORING_METRIC_EXTENSION_TESTSTACK_MONITORING_METRIC_EXTENSION_PUBLISHSTACK_MONITORING_METRIC_EXTENSION_MOVE STACK_MONITORING_CONFIG_CREATE STACK_MONITORING_CONFIG_UPDATE STACK_MONITORING_CONFIG_DELETE STACK_MONITORING_CONFIG_MOVE STACK_MONITORING_BASELINEABLE_METRIC_CREATE STACK_MONITORING_BASELINEABLE_METRIC_UPDATESTACK_MONITORING_BASELINEABLE_METRIC_DELETESTACK_MONITORING_PROCESS_SET_CREATESTACK_MONITORING_PROCESS_SET_UPDATE STACK_MONITORING_PROCESS_SET_DELETESTACK_MONITORING_PROCESS_SET_MOVESTACK_MONITORING_MONITORING_TEMPLATE_CREATESTACK_MONITORING_MONITORING_TEMPLATE_UPDATESTACK_MONITORING_MONITORING_TEMPLATE_DELETESTACK_MONITORING_MONITORING_TEMPLATE_EXPORTSTACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_CREATESTACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_UPDATESTACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_DELETE | `CreateMonitoredResource``UpdateMonitoredResource``DeleteMonitoredResource``ChangeMonitoredResourceCompartment``DisableExternalDatabase` `AssociateMonitoredResources` `DisassociateMonitoredResources` `CreateMonitoredResourceType` `UpdateMonitoredResourceType` `DeleteMonitoredResourceType` `CreateTask``UpdateTask` `DeleteTask` `MoveTask` `CreateDiscoveryJob` `DeleteDiscoveryJob``SubmitDiscoveryJobResult` `SubmitDiscoveryJobFailure` `CreateMetricExtension` `UpdateMetricExtension` `DeleteMetricExtension` `TestMetricExtension` `PublishMetricExtension` `ChangeMetricExtensionCompartment` `CreateConfig``UpdateConfig` `DeleteConfig``ChangeConfigCompartment``CreateBaselineableMetric` `UpdateBaselineableMetric``DeleteBaselineableMetric``CreateProcessSet``UpdateProcessSet``DeleteProcessSet``ChangeProcessSetCompartment``CreateMonitoringTemplate``UpdateMonitoringTemplate``DeleteMonitoringTemplate``ExportMonitoringTemplate``CreateAlarmCondition``UpdateAlarmCondition``DeleteAlarmCondition` | _none_  
## Permissions Required for each API Operation 🔗 
The following tables list the API operations in alphabetical order. For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
### Appmgmt (Control Plane)
API Operation | Permissions Required to Use the Operation  
---|---  
`ListMonitoredInstances` | APPMGMT_MONITORED_INSTANCE_INSPECT  
`GetMonitoredInstance` | APPMGMT_MONITORED_INSTANCE_READ  
`ActivateMonitoringPlugin` | APPMGMT_MONITORED_INSTANCE_ACTIVATE  
`PublishTopProcessesMetrics` | APPMGMT_MONITORED_INSTANCE_PROCESS_PUBLISH  
`ListWorkRequests` | APPMGMT_WORK_REQUEST_INSPECT  
`GetWorkRequest` | APPMGMT_WORK_REQUEST_READ  
`ListWorkRequestErrors` | APPMGMT_WORK_REQUEST_READ  
`ListWorkRequestLogs` | APPMGMT_WORK_REQUEST_READ  
### Stack Monitoring (Data Plane)
API Operation | PermissionsRequired to Use the Operation  
---|---  
`CreateMonitoredResourceType` | STACK_MONITORING_RESOURCE_TYPE_CREATE  
`GetMonitoredResourceType` | STACK_MONITORING_RESOURCE_TYPE_READ  
`UpdateMonitoredResourceType` | STACK_MONITORING_RESOURCE_TYPE_UPDATE  
`DeleteMonitoredResourceType` | STACK_MONITORING_RESOURCE_TYPE_DELETE  
`ListMonitoredResourceTypes` | STACK_MONITORING_RESOURCE_TYPE_INSPECT  
`CreateTask` | STACK_MONITORING_TASK_CREATE  
`GetTask` | STACK_MONITORING_TASK_READ  
`UpdateTask` | STACK_MONITORING_TASK_UPDATE  
`DeleteTask` | STACK_MONITORING_TASK_DELETE  
`ListTasks` | STACK_MONITORING_TASK_INSPECT  
`MoveTask` | STACK_MONITORING_TASK_MOVE  
`CreateMonitoredResource` | STACK_MONITORING_RESOURCE_CREATE  
`GetMonitoredResource` | STACK_MONITORING_RESOURCE_READ  
`UpdateMonitoredResource` | STACK_MONITORING_RESOURCE_UPDATE  
`DeleteMonitoredResource` | STACK_MONITORING_RESOURCE_DELETE  
`SearchMonitoredResources` | STACK_MONITORING_RESOURCE_INSPECT  
`SearchMonitoredResourceMembers` | STACK_MONITORING_RESOURCE_INSPECT  
`ChangeMonitoredResourceCompartment` | STACK_MONITORING_RESOURCE_MOVE  
`AssociateMonitoredResources` | STACK_MONITORING_RESOURCE_ASSOC_CREATE  
`DisassociateMonitoredResources` | STACK_MONITORING_RESOURCE_ASSOC_DELETE  
`SearchMonitoredResourceAssociations` | STACK_MONITORING_RESOURCE_ASSOC_INSPECT  
`DisableExternalDatabase` | STACK_MONITORING_RESOURCE_UPDATE  
`ListDiscoveryResourceTypes` | STACK_MONITORING_DISCOVERY_RESOURCE_TYPE_INSPECT  
`ListWorkRequests` | STACK_MONITORING_WORK_REQUEST_INSPECT  
`GetWorkRequest` | STACK_MONITORING_WORK_REQUEST_READ  
`ListWorkRequestErrors` | STACK_MONITORING_WORK_REQUEST_READ  
`ListWorkRequestLogs` | STACK_MONITORING_WORK_REQUEST_READ  
`CreateDiscoveryJob` | STACK_MONITORING_DISCOVERY_JOB_CREATE  
`ListDiscoveryJobs` | STACK_MONITORING_DISCOVERY_JOB_INSPECT  
`GetDiscoveryJob` | STACK_MONITORING_DISCOVERY_JOB_READ  
`DeleteDiscoveryJob` | STACK_MONITORING_DISCOVERY_JOB_DELETE  
`SubmitDiscoveryJobResult` | STACK_MONITORING_DISCOVERY_JOB_RESULT_SUBMIT  
`SubmitDiscoveryJobFailure` | STACK_MONITORING_DISCOVERY_JOB_RESULT_SUBMIT  
`ListMetricExtensions` | STACK_MONITORING_METRIC_EXTENSION_INSPECT  
`CreateMetricExtension` | STACK_MONITORING_METRIC_EXTENSION_CREATE  
`GetMetricExtension` | STACK_MONITORING_METRIC_EXTENSION_READ  
`UpdateMetricExtension` | STACK_MONITORING_METRIC_EXTENSION_UPDATE  
`DeleteMetricExtension` | STACK_MONITORING_METRIC_EXTENSION_DELETE  
`TestMetricExtension` | STACK_MONITORING_METRIC_EXTENSION_TEST  
`PublishMetricExtension` | STACK_MONITORING_METRIC_EXTENSION_PUBLISH  
`EnableMetricExtension` | STACK_MONITORING_METRIC_EXTENSION_ENABLE  
`DisableMetricExtension` | STACK_MONITORING_METRIC_EXTENSION_DISABLE  
`ChangeMetricExtensionCompartment` | STACK_MONITORING_METRIC_EXTENSION_MOVE  
`ListConfigs` | STACK_MONITORING_CONFIG_INSPECT  
`CreateConfig` | STACK_MONITORING_CONFIG_CREATE  
`GetConfig` | STACK_MONITORING_CONFIG_READ  
`UpdateConfig` | STACK_MONITORING_CONFIG_UPDATE  
`DeleteConfig` | STACK_MONITORING_CONFIG_DELETE  
`ChangeConfigCompartment` | STACK_MONITORING_CONFIG_MOVE  
`ListBaselineableMetrics` | STACK_MONITORING_BASELINEABLE_METRIC_INSPECT  
`CreateBaselineableMetric` | STACK_MONITORING_BASELINEABLE_METRIC_CREATE  
`GetBaselineableMetric` | STACK_MONITORING_BASELINEABLE_METRIC_READ  
`UpdateBaselineableMetric` | STACK_MONITORING_BASELINEABLE_METRIC_UPDATE  
`DeleteBaselineableMetric` | STACK_MONITORING_BASELINEABLE_METRIC_DELETE  
`EvaluateBaselineableMetric` | STACK_MONITORING_BASELINEABLE_METRIC_EVALUATE  
`CreateProcessSet` | STACK_MONITORING_PROCESS_SET_CREATE  
`ListProcessSets` | STACK_MONITORING_PROCESS_SET_INSPECT  
`GetProcessSet` | STACK_MONITORING_PROCESS_SET_READ  
`DeleteProcessSet` | STACK_MONITORING_PROCESS_SET_DELETE  
`UpdateProcessSet` | STACK_MONITORING_PROCESS_SET_UPDATE  
`ChangeProcessSetCompartment` | STACK_MONITORING_PROCESS_SET_MOVE  
`GetMonitoringTemplate` | STACK_MONITORING_MONITORING_TEMPLATE_READ  
`CreateMonitoringTemplate` | STACK_MONITORING_MONITORING_TEMPLATE_CREATE  
`UpdateMonitoringTemplate` | STACK_MONITORING_MONITORING_TEMPLATE_UPDATE  
`DeleteMonitoringTemplate` | STACK_MONITORING_MONITORING_TEMPLATE_DELETE  
`ExportMonitoringTemplate` | STACK_MONITORING_MONITORING_TEMPLATE_EXPORT  
`ListMonitoringTemplates` | STACK_MONITORING_MONITORING_TEMPLATE_INSPECT  
`GetAlarmCondition` | STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_READ  
`CreateAlarmCondition` | STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_CREATE  
`UpdateAlarmCondition` | STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_UPDATE  
`DeleteAlarmCondition` | STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_DELETE  
`ListAlarmConditions` | STACK_MONITORING_MONITORING_TEMPLATE_ALARM_CONDITION_INSPECT  
`ApplyMonitoringTemplate` | STACK_MONITORING_MONITORING_TEMPLATE_APPLY  
`UnapplyMonitoringTemplate` | STACK_MONITORING_MONITORING_TEMPLATE_UNAPPLY  
Was this article helpful?
YesNo

