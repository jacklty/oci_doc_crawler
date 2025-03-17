Updated 2024-06-06
# Details for the Audit Service
This topic covers details for writing policies to control access to the Audit service.
## Resource-Types 🔗 
`audit-events`
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `use` and `manage` verbs for the `audit-events` resource-type cover no extra permissions or API operations compared to the `read` verb.
### audit-events
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | none | none | none  
read | AUDIT_EVENT_READ | `ListEvents` | none  
use | no extra | no extra | none  
manage | no extra | no extra | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListEvents` | AUDIT_EVENT_READ  
`Configuration` | AUDIT_CONFIGURATION  
Was this article helpful?
YesNo

