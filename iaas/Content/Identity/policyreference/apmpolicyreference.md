Updated 2023-06-05
# Details for Application Performance Monitoring
Details for Application Performance Monitoring
This topic covers details for writing policies to control access to the Application Performance Monitoring (APM) service.
## Resource-Types 🔗 
`apm-domains`
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")).
## Details for Verb + Resource-Type Combinations 🔗 
The following table shows the [permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.") and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.
For example, the `use` and `manage` verbs for the `apm-domains` resource-type cover no extra permissions or API operations compared to the `read` verb.
### apm-domains
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  APM_DOMAIN_LIST |  `ListApmDomains` `ListWorkRequests` `ListWorkRequestErrors` `ListWorkRequestLogs` |  none  
read |  INSPECT + APM_DOMAIN_READ |  `GetApmDomain` `ListApmDomainWorkRequests` `GetWorkRequest` `GetMonitor` `GetMonitorResult` `ListMonitors` `ListPublicVantagePoints` `GetScript` `ListScripts` `ListQuickPicks` `Query` `GetSpan` `GetTrace` |  none  
use |  READ + APM_DOMAIN_UPDATE |  `UpdateApmDomain` `ListDataKeys` `GenerateDataKeys` `RemoveDataKeys` `CreateMonitor` `DeleteMonitor` `UpdateMonitor` `CreateScript` `DeleteScript` `UpdateScript` |  none  
manage |  USE + APM_DOMAIN_CREATE APM_DOMAIN_DELETE APM_DOMAIN_MOVE |  `CreateApmDomain` `DeleteApmDomain` `ChangeApmDomainCompartment` |  none  
## Permissions Required for Each API Operation 🔗 
The following tables list the API operations and the permissions required to use the operations. For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.").
### Application Performance Monitoring Control Plane API Operations 🔗 
The following table lists the [APM Control Plane API](https://docs.oracle.com/iaas/api/#/en/apm-control-plane/latest/) operations in alphabetical order, grouped by resource. Permissions for `WorkRequests` operations are based on the permissions for the APM domain.
API Operation | Permissions Required to Use the Operation  
---|---  
`ChangeApmDomainCompartment` | APM_DOMAIN_MOVE permission on both the source and the destination compartments  
`CreateApmDomain` | APM_DOMAIN_CREATE  
`DeleteApmDomain` | APM_DOMAIN_DELETE  
`GenerateDataKeys` | APM_DOMAIN_UPDATE  
`GetApmDomain` | APM_DOMAIN_READ  
`ListApmDomains` | APM_DOMAIN_LIST  
`ListApmDomainWorkRequests` | APM_DOMAIN_READ  
`ListDataKeys` | APM_DOMAIN_UPDATE  
`RemoveDataKeys` | APM_DOMAIN_UPDATE  
`UpdateApmDomain` | APM_DOMAIN_UPDATE  
`GetWorkRequest` | APM_DOMAIN_READ  
`ListWorkRequests` | APM_DOMAIN_LIST  
`ListWorkRequestErrors` | APM_DOMAIN_LIST  
`ListWorkRequestLogs` | APM_DOMAIN_LIST  
### Application Performance Monitoring Synthetic Monitoring API Operations 🔗 
The following table lists the [APM Synthetic Monitoring API](https://docs.oracle.com/iaas/api/#/en/apm-synthetic-monitoring/latest/) operations in alphabetical order, grouped by resource. Permissions for the Synthetic Monitoring operations are based on the enclosing APM domain.
API Operation | Permissions Required to Use the Operation  
---|---  
`CreateMonitor` | APM_DOMAIN_UPDATE  
`DeleteMonitor` | APM_DOMAIN_UPDATE  
`GetMonitor` | APM_DOMAIN_READ  
`GetMonitorResult` | APM_DOMAIN_READ  
`ListMonitors` | APM_DOMAIN_READ  
`UpdateMonitor` | APM_DOMAIN_UPDATE  
`ListPublicVantagePoints` | APM_DOMAIN_READ  
`CreateScript` | APM_DOMAIN_UPDATE  
`DeleteScript` | APM_DOMAIN_UPDATE  
`GetScript` | APM_DOMAIN_READ  
`ListScripts` | APM_DOMAIN_READ  
`UpdateScript` | APM_DOMAIN_UPDATE  
### Application Performance Monitoring Trace Explorer API Operations 🔗 
The following table lists the [APM Trace Explorer API](https://docs.oracle.com/iaas/api/#/en/apm-trace-explorer/latest/) operations in alphabetical order, grouped by resource. Permissions for the Trace Explorer operations are based on the enclosing APM domain.
API Operation | Permissions Required to Use the Operation  
---|---  
`GetSpan` | APM_DOMAIN_READ  
`GetTrace` | APM_DOMAIN_READ  
`ListQuickPicks` | APM_DOMAIN_READ  
`Query` | APM_DOMAIN_READ  
Was this article helpful?
YesNo

