Updated 2024-06-06
# Details for the Network Monitoring Service
This topic covers details for writing policies to control access to the Network Monitoring service.
## Resource-Types
**Individual Resource-Types**
`path-analyzer-test`
## For path-analyzer-test Resource Types
The following table lists the permissions and API operations covered by each of the individual resource-types included in this API.
## Supported Variables
This API supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).
## Details for Verb + Resource-Type Combinations
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` and `use` verbs for the `path-analyzer-test` resource-type cover no extra permissions or API operations compared to the `inspect` verb. However, the `manage` verb includes several extra permissions and API operations.
[path-analyzer-test](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/VnMonitoringpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  VNPA_INSPECT |  `ListPathAnalyzerTests` `ListWorkRequests` `ListWorkRequestLogs` `ListWorkRequestErrors` `ListWorkRequestResults` |  none  
read |  INSPECT+ VNPA_READ |  `GetPathAnalysis` `GetPathAnalyzerTest` `GetWorkRequest` |  none  
use |  READ + VNPA_UPDATE | UpdatePathAnalyzerTest |  none  
manage |  USE + VNPA_CREATE VNPA_DELETE VNPA_MOVE |  `CreatePathAnalyzerTest` `DeletePathAnalyzerTest` `ChangePathAnalyzerTestCompartment` |  none  
## Permissions Required for Each API Operation 🔗 
The following tables list the API operations grouped by resource type. The resource types are listed in alphabetical order.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
### Network Monitoring Operations
API Operation | Permissions Required to Use the Operation  
---|---  
`ChangePathAnalyzerTestCompartment ` | VNPA_MOVE  
`CreatePathAnalyzerTest` | VNPA_CREATE  
`DeletePathAnalyzerTest` | VNPA_DELETE  
`GetPathAnalysis` | VNPA_READ  
`GetPathAnalyzerTest` | VNPA_READ  
`GetWorkRequest` | VNPA_READ  
`ListPathAnalyzerTests` | VNPA_INSPECT  
`ListWorkRequestErrors` | VNPA_INSPECT  
`ListWorkRequestLogs` | VNPA_INSPECT  
`ListWorkRequestResults` | VNPA_INSPECT  
`ListWorkRequests` | VNPA_INSPECT  
`UpdatePathAnalyzerTest` | VNPA_UPDATE  
Was this article helpful?
YesNo

