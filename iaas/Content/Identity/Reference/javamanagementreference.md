Updated 2024-06-06
# Details for the Java Management Service
This topic covers details for writing policies to control access to the Java Management service.
## Resource-Types 🔗 
`fleet`
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
[fleet](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/javamanagementreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  FLEET_INSPECT |  `ListFleets` `ListWorkRequest` `ListWorkRequestErrors` `ListWorkRequestLogs` |  none  
read |  INSPECT + FLEET_READ FLEET_QUERY_RESOURCES |  `GetFleet` `GetWorkRequest` `SummarizeJres` `RequestSummarizedJres` `SummarizeApplications` `RequestSummarizedApplications` `SummarizeInstallations` `RequestSummarizedInstallations` `SummarizeManagedInstances` `RequestSummarizedManagedInstances` `GetFleetAdvancedFeatureConfiguration` |  none  
use |  READ + FLEET_UPDATE | `UpdateFleet` |  none  
manage |  USE + FLEET_CREATE FLEET_DELETE FLEET_MOVE FLEET_ADVANCED_FEATURES_UPDATE  |  `CreateFleet` `DeleteFleet` `ChangeFleetCompartment` `UpdateFleetAdvancedFeatureConfiguration` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in alphabetical order.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListFleets` | FLEET_INSPECT  
`GetFleet` | FLEET_READ  
`UpdateFleet` |  FLEET_UPDATE  
`ChangeFleetCompartment` | FLEET_MOVE  
`CreateFleet` | FLEET_CREATE  
`DeleteFleet` |  FLEET_DELETE  
`SummarizeJres` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedJres` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeApplications` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedApplications` | FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeInstallations` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedInstallations` |  FLEET_READ and FLEET_QUERY_RESOURCES  
`SummarizeManagedInstances` | FLEET_READ and FLEET_QUERY_RESOURCES  
`RequestSummarizedManagedInstances` | FLEET_READ and FLEET_QUERY_RESOURCES  
`ListWorkRequest` | FLEET_INSPECT  
`GetWorkRequest` | FLEET_READ  
`ListWorkRequestErrors` | FLEET_INSPECT  
`ListWorkRequestLogs` | FLEET_INSPECT  
`GetFleetAdvancedFeatureConfiguration` | FLEET_READ  
`UpdateFleetAdvancedFeatureConfiguration` | FLEET_ADVANCED_FEATURES_UPDATE  
Was this article helpful?
YesNo

