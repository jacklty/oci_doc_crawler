Updated 2024-06-06
# Details for the Quotas Service
This topic covers details for writing policies to control access to the Quotas service.
## Resource-Types 🔗 
`quota`
## Supported Variables 🔗 
The Quotas service supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)) plus the following:
Variable | Variable Type | Source  
---|---|---  
`target.quota.id` | Entity (OCID) | Request  
`target.quota.name` | String | Request/Stored  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.
[quotas](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/quotaspolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | QUOTA_INSPECT | `listQuotas` | none  
read | QUOTA_READ | `getQuota` | none  
use | _no extra_ | _no extra_ | none  
manage | USE + QUOTA_CREATE QUOTA_DELETE QUOTA_UPDATE | `createQuota` `deleteQuota` `updateQuota` | none  
## Permissions Required for Each API Operation 🔗 
API Operation | Permissions Required to Use the Operation  
---|---  
`listQuotas` | QUOTA_INSPECT  
`createQuota` | QUOTA_CREATE  
`getQuota` | QUOTA_READ  
`deleteQuota` | QUOTA_DELETE  
`updateQuota` | QUOTA_UPDATE  
Was this article helpful?
YesNo

