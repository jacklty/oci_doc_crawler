Updated 2024-06-06
# Details for Oracle Cloud VMware Solution
This topic covers details for writing policies to control access to Oracle Cloud VMware Solution resources.
## Resource-Types 🔗 
`sddcs`
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for sddcs includes the same permissions and API operations as the `inspect` verb, plus the SDDC_READ permission and a number of API operations (e.g., `GetSddc`, `ListWorkRequests`, etc.). The `use` verb covers two more permissions and set of API operations compared to `read`. And `manage` covers five more permissions and operations compared to `use`.
### sddcs
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | SDDC_INSPECT | `ListSddcs` `ListWorkRequests` | none  
read | INSPECT + SDDC_READ | INSPECT + `GetSddc` `GetWorkRequest` | none  
use | READ + SDDC_UPDATE SDDC_UPDATE_ESXI_HOST | READ + `UpdateSddc` `UpdateEsxiHost` | none  
manage | USE + SDDC_CREATE SDDC_MOVE SDDC_ADD_ESXI_HOST SDDC_DELETE_ESXI_HOST SDDC_DELETE | USE + `ChangeSddcCompartment` | `CreateSddc` (also need `manage instances`, `manage vcns`, `use subnets`, `use vnics`, `use vlans`, `use private-ips`, `inspect security-lists`, `use network-security-groups`) `DeleteSddc`, `CreateEsxiHost`, `DeleteEsxiHost` (also need `manage instances`, `manage vcns`, `use subnets`, `use vnics`, `use vlans`, `use private-ips`)  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListSddcs` | SDDC_INSPECT  
`GetSddc` | SDDC_READ  
`CreateSddc` | SDDC_CREATE & INSTANCE_CREATE & INSTANCE_ATTACH_SECONDARY_VNIC & VCN_READ & VCN_ATTACH & SUBNET_READ & SUBNET_ATTACH & VNIC_READ & VNIC_CREATE & VLAN_READ & VLAN_ATTACH & PRIVATE_IP_CREATE & PRIVATE_IP_ASSIGN & SECURITY_LIST_READ & NETWORK_SECURITY_GROUP_LIST_SECURITY_RULES  
`ListWorkRequests` | SDDC_INSPECT  
`GetWorkRequest` | SDDC_READ  
`ChangeSddcCompartment` | SDDC_MOVE  
`UpdateSddc` | SDDC_UPDATE  
`DeleteSddc` | SDDC_DELETE & INSTANCE_DELETE & INSTANCE_DETACH_SECONDARY_VNIC & VCN_DETACH & SUBNET_DETACH & VLAN_DETACH & VNIC_READ & VNIC_DELETE & PRIVATE_IP_DELETE & PRIVATE_IP_UNASSIGN  
`ListEsxiHosts` | SDDC_INSPECT  
`CreateEsxiHost` |  SDDC_ADD_ESXI_HOST & INSTANCE_CREATE & INSTANCE_ATTACH_SECONDARY_VNIC & VCN_READ & VCN_ATTACH & SUBNET_READ & SUBNET_ATTACH & VLAN_READ & VLAN_ATTACH & VNIC_READ & VNIC_CREATE & PRIVATE_IP_CREATE & PRIVATE_IP_ASSIGN  
`UpdateEsxiHost	` | SDDC_UPDATE_ESXI_HOST  
`DeleteEsxiHost` | SDDC_DELETE_ESXI_HOST & INSTANCE_DELETE & INSTANCE_DETACH_SECONDARY_VNIC & VCN_DETACH & SUBNET_DETACH & VLAN_DETACH & VNIC_READ & VNIC_DELETE & PRIVATE_IP_DELETE & PRIVATE_IP_UNASSIGN  
Was this article helpful?
YesNo

