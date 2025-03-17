Updated 2024-06-06
# Details for Connector Hub
Review details for writing policies to control access to the Connector Hub service.
## Individual Resource-Types 🔗 
`serviceconnectors`
## Supported Variables 🔗 
Connector Hub supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")), plus the ones listed here.
The `serviceconnectors` resource type can use the following variables. 
Variable | Variable Type | Comments  
---|---|---  
`target.serviceconnector.id` | OCID |  Use this variable to control access for connectors.  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
[serviceconnectors](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/serviceconnectorhubpolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  SERVICE_CONNECTOR_INSPECT |  `GetWorkRequest` `ListServiceConnectors` `ListWorkRequestErrors` `ListWorkRequestLogs` `ListWorkRequests` |  none  
read |  INSPECT + SERVICE_CONNECTOR_READ |  `GetServiceConnector` |  none  
use |  READ + SERVICE_CONNECTOR_UPDATE |  `ActivateServiceConnector` `DeactivateServiceConnector` `UpdateServiceConnector` |  none  
manage |  USE + SERVICE_CONNECTOR_CREATE SERVICE_CONNECTOR_DELETE SERVICE_CONNECTOR_MOVE |  `ChangeServiceConnectorCompartment` `CreateServiceConnector` `DeleteServiceConnector` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists API operations in alphabetical order.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.").
API Operation | Permissions Required to Use the Operation  
---|---  
`ActivateServiceConnector` | SERVICE_CONNECTOR_UPDATE  
`ChangeServiceConnectorCompartment` | SERVICE_CONNECTOR_MOVE  
`CreateServiceConnector` | SERVICE_CONNECTOR_CREATE  
`DeactivateServiceConnector` | SERVICE_CONNECTOR_UPDATE  
`DeleteServiceConnector` | SERVICE_CONNECTOR_DELETE  
`GetConnectorPlugin` | No permissions required  
`GetServiceConnector` | SERVICE_CONNECTOR_READ  
`GetWorkRequest` | SERVICE_CONNECTOR_INSPECT  
`ListConnectorPlugins` | No permissions required  
`ListServiceConnectors` | SERVICE_CONNECTOR_INSPECT  
`ListWorkRequestErrors` | SERVICE_CONNECTOR_INSPECT  
`ListWorkRequestLogs` | SERVICE_CONNECTOR_INSPECT  
`ListWorkRequests` | SERVICE_CONNECTOR_INSPECT  
`UpdateServiceConnector` | SERVICE_CONNECTOR_UPDATE  
Was this article helpful?
YesNo

