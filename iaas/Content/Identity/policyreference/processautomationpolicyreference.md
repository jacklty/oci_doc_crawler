Updated 2024-06-06
# Details for Process Automation
This topic covers details for writing policies to control access to the Process Automation service.
## Resource-Type 🔗 
`process-automation-instance`
## Supported Variables 🔗 
Process Automation supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")), plus the ones listed here.
Supported Variables | Variable | Variable Type | Description  
---|---|---|---  
**Required Variables Supplied by the Service for Every Request** | `target.compartment.id` | ENTITY |  The OCID of the primary resource for the request.  
`request.operation` | STRING | The operation ID (for example, 'GetUser') for the request.  
`target.resource.kind` | STRING |  The resource kind name of the primary resource for the request.  
**Automatic Variables Supplied by the SDK for Every Request** | `request.user.id` | ENTITY |  For user-initiated requests. The OCID of the calling user.  
`request.groups.id` | LIST (ENTITY) |  For user-initiated requests. The OCIDs of the groups of `request.user.id`.  
`target.compartment.name` | STRING |  The name of the compartment specified in `target.compartment.id.`  
`target.tenant.id` | ENTITY |  The OCID of the target tenant ID.  
**Dynamic Variables Computed Implicitly by IAM Authorization** | `request.principal.group.tag.<tagNS>.<tagKey>` | STRING |  The value of each tag on a group of which the principal is a member.  
`request.principal.compartment.tag.<tagNS>.<tagKey>` | STRING |  The value of each tag on the compartment that contains the principal.  
`target.resource.tag.<tagNS>.<tagKey>` | STRING |  The value of each tag on the target resource. (Computed based on tagSlug supplied by service on each request.)  
`target.resource.compartment.tag.<tagNS>.<tagKey>` | STRING |  The value of each tag on the compartment that contains the target resource. (Computed based on tagSlug supplied by service on each request.)  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.. 
### process-automation-instance 🔗 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  PROCESS_AUTOMATION_INSTANCE_INSPECT |  `ListProcessInstances` `ListWorkRequests` |  none  
read |  INSPECT + PROCESS_AUTOMATION_INSTANCE_READ |  INSPECT + `GetProcessInstance ` `GetWorkRequest` |  none  
use |  READ + PROCESS_AUTOMATION_INSTANCE_UPDATE |  READ + `UpdateProcessInstances` |  none  
manage |  USE + PROCESS_AUTOMATION_INSTANCE_CREATE PROCESS_AUTOMATION_INSTANCE_DELETE PROCESS_AUTOMATION_INSTANCE_MOVE |  USE + `CreateProcessInstance` `DeleteProcessInstance` `ChangeProcessCompartment` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in alphabetical order.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ChangeProcessCompartment` | PROCESS_AUTOMATION_INSTANCE_MOVE  
`CreateProcessInstance` | PROCESS_AUTOMATION_INSTANCE_CREATE  
`DeleteProcessInstance` | PROCESS_AUTOMATION_INSTANCE_DELETE  
`GetProcessInstance` | PROCESS_AUTOMATION_INSTANCE_READ  
`GetWorkRequest` | PROCESS_AUTOMATION_INSTANCE_READ  
`ListProcessInstances` | PROCESS_AUTOMATION_INSTANCE_INSPECT  
Was this article helpful?
YesNo

