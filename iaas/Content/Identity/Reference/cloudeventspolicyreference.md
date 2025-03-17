Updated 2024-06-06
# Details for the Events Service
This topic covers details for writing user IAM policies that control access to rules for the Events service. 
## Resource-Types 🔗 
`cloudevents-rules`
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for cloudevents-rules includes the same permissions and API operations as the `inspect` verb, plus the EVENTRULE_READ permissions and the corresponding API operation `GetEventRule`. The `use` verb adds no extra permissions or API operations compared to `read`. However, `manage` adds more permissions and operations compared to `use`.
### cloudevents-rules
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | EVENTRULE_LIST | `ListRules` | none  
read | INSPECT + EVENTRULE_READ | INSPECT + `GetRule` | none  
use | no extra | no extra | none  
manage | USE + EVENTRULE_CREATE  EVENTRULE_DELETE EVENTRULE_MODIFY | USE + `CreateRule` `DeleteRule` `UpdateRule` `ChangeRuleCompartment` | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListRules` | EVENTRULE_LIST  
`CreateRule` |  EVENTRULE_CREATE  
`GetRule` | EVENTRULE_READ  
`DeleteRule` | EVENTRULE_DELETE  
`UpdateRule` | EVENTRULE_MODIFY  
`ChangeRuleCompartment` | EVENTRULE_MODIFY  
Was this article helpful?
YesNo

