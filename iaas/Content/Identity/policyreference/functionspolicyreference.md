Updated 2024-06-06
# Details for Functions
This topic covers details for writing policies to control access to OCI Functions.
## Resource-Types 🔗 
### Aggregate Resource-Type
  * `functions-family`


### Individual Resource-Types
  * `fn-app`
  * `fn-function`
  * `fn-invocation`


### Comments
A policy that uses `<verb> functions-family` is equivalent to writing one with a separate `<verb> <individual resource-type>` statement for each of the individual resource-types.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/functionspolicyreference.htm#functionsverbresourcetypecombination) for details of the API operations covered by each verb, for each individual resource-type included in `functions-family`.
## Supported Variables 🔗 
OCI Functions supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for the `fn-app` resource-type includes the same permissions and API operations as the `inspect` verb, plus the FN_APP_READ permission and the `GetApp` API operation. In the case of the `fn-app` resource-type, the `use` verb covers no additional permissions or API operations compared to `read`. Lastly, `manage` covers more permissions and operations compared to `use`.
[fn-app](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/functionspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | FN_APP_LIST | `ListApp` | none  
read | INSPECT + FN_APP_READ | INSPECT + `GetApp` | none  
use | no extra | no extra | none  
manage | USE + FN_APP_CREATE FN_APP_DELETE FN_APP_UPDATE | USE + `CreateApp` `DeleteApp` `UpdateApp` | none  
[fn-function](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/functionspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | FN_FUNCTION_LIST | `ListFunctions` | none  
read | INSPECT + FN_FUNCTION_READ | INSPECT + `GetFunction` | none  
use | no extra | no extra | none  
manage | USE + FN_FUNCTION_CREATE FN_FUNCTION_DELETE FN_FUNCTION_UPDATE | USE + `CreateFunction` `DeleteFunction` `UpdateFunction` | none  
[fn-invocation](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/functionspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | none | none | none  
read | none | none | none  
use | FN_INVOCATION | `InvokeFunction` | none  
manage | no extra | no extra | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type. For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.").
API Operation | Permissions Required to Use the Operation  
---|---  
`CreateApp` | FN_APP_CREATE  
`DeleteApp` | FN_APP_DELETE  
`ListApp` | FN_APP_LIST  
`GetApp` | FN_APP_READ  
`UpdateApp` | FN_APP_UPDATE  
`CreateFunction` | FN_FUNCTION_CREATE  
`DeleteFunction` | FN_FUNCTION_DELETE  
`ListFunctions` | FN_FUNCTION_LIST  
`GetFunction` | FN_FUNCTION_READ  
`UpdateFunction` | FN_FUNCTION_UPDATE  
`InvokeFunction` | FN_INVOCATION  
Was this article helpful?
YesNo

