Updated 2024-06-06
# Details for the Web Application Acceleration Service
Details for the Web Application Acceleration Service
This topic covers details for writing policies to control access to the Web Application Acceleration service.
## Aggregate Resource-Type 🔗 
`waa-family`
## Individual Resource-Types 🔗 
`waa-policy`
`web-app-acceleration`
### Comments
A policy that uses `<verb> waa-family` is equivalent to writing one with a separate `<verb> <individual resource-type>` statement for each of the individual resource-types.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/waapolicyreference.htm#Details) for details of the API operations covered by each verb, for each individual resource-type included in `waa-family`.
## Supported Variables 🔗 
The Web Application Acceleration Service supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `use` and `manage` verbs for the `waa-policy` resource-type cover no extra permissions or API operations compared to the `read` verb.
[waa-policy](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/waapolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  WAA_POLICY_INSPECT |  `ListWebAppAccelerationPolicies` |  `ListWorkRequests` `ListWorkRequestErrors` `ListWorkRequestLogs`  
read |  INSPECT + WAA_POLICY_READ |  INSPECT + `GetWebAppAccelerationPolicy` |  `GetWorkRequest`  
use |  READ + WAA_POLICY_ATTACH WAA_POLICY_DETACH WAA_POLICY_UPDATE |  READ + `UpdateWebAppAccelerationPolicy` |  `CreateWebAppAcceleration` `UpdateWebAppAcceleration` `DeleteWebAppAcceleration`  
manage |  USE + WAA_POLICY_CREATE WAA_POLICY_DELETE WAA_POLICY_MOVE |  USE + `CreateWebAppAccelerationPolicy` `DeleteWebAppAccelerationPolicy` `ChangeWebAppAccelerationPolicyCompartment` |  none  
[web-app-acceleration](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/waapolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  WEB_APP_ACCELERATION_INSPECT |  `ListWebAppAccelerations` |  `ListWorkRequests` `ListWorkRequestErrors` `ListWorkRequestLogs`  
read |  INSPECT + WEB_APP_ACCELERATION_READ |  INSPECT + `GetWebAppAcceleration` `GetLogging` |  `GetWorkRequest`  
use |  READ + WEB_APP_ACCELERATION_UPDATE |  READ + `PurgeWebAppAccelerationCache` `StartLogging` `UpdateLogging` `StopLogging` |  none  
manage |  USE + WEB_APP_ACCELERATION_CREATE WEB_APP_ACCELERATION_DELETE WEB_APP_ACCELERATION_MOVE |  USE + `ChangeWebAppAccelerationCompartment` |  `CreateWebAppAcceleration` `DeleteWebAppAcceleration`  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListWebAppAccelerationPolicies` | WAA_POLICY_INSPECT  
`CreateWebAppAccelerationPolicy` | WAA_POLICY_CREATE  
`GetWebAppAccelerationPolicy` | WAA_POLICY_READ  
`UpdateWebAppAccelerationPolicy` | WAA_POLICY_UPDATE  
`DeleteWebAppAccelerationPolicy` | WAA_POLICY_DELETE  
`ChangeWebAppAccelerationPolicyCompartment` | WAA_POLICY_MOVE  
`ListWebAppAccelerations` | WEB_APP_ACCELERATION_INSPECT  
`CreateWebAppAcceleration` |  WEB_APP_ACCELERATION_CREATE + WAA_POLICY_ATTACH + LOAD_BALANCER_UPDATE  
`GetWebAppAcceleration` | WEB_APP_ACCELERATION_READ  
`UpdateWebAppAcceleration` |  WEB_APP_ACCELERATION_UPDATE + WAA_POLICY_ATTACH + WAA_POLICY_DETACH + LOAD_BALANCER_UPDATE  
`DeleteWebAppAcceleration` |  WEB_APP_ACCELERATION_DELETE + WAA_POLICY_DETACH + LOAD_BALANCER_UPDATE  
`ChangeWebAppAccelerationCompartment` | WEB_APP_ACCELERATION_MOVE  
`PurgeWebAppAccelerationCache` | WEB_APP_ACCELERATION_UPDATE  
`ListWorkRequests` |  WEB_APP_ACCELERATION_INSPECT + WAA_POLICY_INSPECT  
`GetWorkRequest` |  WAA_POLICY_READ + WEB_APP_ACCELERATION_READ  
`ListWorkRequestErrors` |  WEB_APP_ACCELERATION_INSPECT + WAA_POLICY_INSPECT  
`ListWorkRequestLogs` |  WEB_APP_ACCELERATION_INSPECT + WAA_POLICY_INSPECT  
`StartLogging` | WEB_APP_ACCELERATION_UPDATE  
`UpdateLogging` | WEB_APP_ACCELERATION_UPDATE  
`GetLogging` | WEB_APP_ACCELERATION_READ  
`StopLogging` | WEB_APP_ACCELERATION_UPDATE  
Was this article helpful?
YesNo

