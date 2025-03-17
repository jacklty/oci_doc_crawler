Updated 2024-06-06
# Details for Network Load Balancer
This topic covers details for writing policies to control access to the Network Load Balancer service.
## Resource-Types 🔗 
`network-load-balancers`
## Supported Variables 🔗 
Only the general variables are supported (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for network-load-balancers includes the same permissions and API operations as the `inspect` verb, plus the NETWORK_LOAD_BALANCER_READ permission and various API operations (e.g., `GetNetworkLoadBalancer`, `ListWorkRequests`, and so forth.). The `use` verb covers more permissions and sets of API operations compared to `read`. And `manage` covers more permissions and API operations compared to `use`.
### network-load-balancers
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | NETWORK_LOAD_BALANCER_INSPECT | `ListNetworkLoadBalancers` | none  
read | INSPECT + NETWORK_LOAD_BALANCER_READ | INSPECT + `GetNetworkLoadBalancer` `ListListeners` `GetListener` `ListBackendSets` `GetBackendSet` `ListBackends` `GetBackend` `GetHealthChecker` `ListNetworkLoadBalancersHealth` `GetNetworkLoadBalancersHealth` `GetBackendSetHealth` `GetBackendHealth` `ListPolicies` `ListProtocols` `ListWorkRequests` `GetWorkRequest` `ListWorkRequestErrors` `ListWorkRequestLogs` | none  
use | READ + NETWORK_LOAD_BALANCER_UPDATE | READ + `UpdateNetworkLoadBalancer` `UpdateNetworkSecurityGroups` `UpdateListener` `UpdateBackendSet` `UpdateBackend` `UpdateHealthChecker` | none  
manage | USE + NETWORK_LOAD_BALANCER_CREATE NETWORK_LOAD_BALANCER_DELETE NETWORK_LOAD_BALANCER_MOVE | USE + `CreateNetworkLoadBalancer` `DeleteNetworkLoadBalancer` `ChangeNetworkLoadBalancerCompartment` `CreateListener` `DeleteListener` `CreateBackendSet` `DeleteBackendSet` `CreateBackend` `DeleteBackend` | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListNetworkLoadBalancers` | NETWORK_LOAD_BALANCER_INSPECT   
`CreateNetworkLoadBalancer` | NETWORK_LOAD_BALANCER_CREATE  
`GetNetworkLoadBalancer` | NETWORK_LOAD_BALANCER_READ  
`UpdateNetworkLoadBalancer` | NETWORK_LOAD_BALANCER_UPDATE  
`DeleteNetworkLoadBalancer` | NETWORK_LOAD_BALANCER_DELETE  
`ChangeNetworkLoadBalancerCompartment` | NETWORK_LOAD_BALANCER_MOVE  
`UpdateNetworkSecurityGroups` | NETWORK_LOAD_BALANCER_UPDATE  
`ListListeners` | NETWORK_LOAD_BALANCER_READ  
`CreateListener` | NETWORK_LOAD_BALANCER_UPDATE  
`GetListener` | NETWORK_LOAD_BALANCER_READ  
`UpdateListener` | NETWORK_LOAD_BALANCER_UPDATE  
`DeleteListener` | NETWORK_LOAD_BALANCER_UPDATE  
`ListBackendSets` | NETWORK_LOAD_BALANCER_READ  
`CreateBackendSet` | NETWORK_LOAD_BALANCER_UPDATE  
`GetBackendSet` | NETWORK_LOAD_BALANCER_READ  
`UpdateBackendSet` | NETWORK_LOAD_BALANCER_UPDATE  
`DeleteBackendSet` | NETWORK_LOAD_BALANCER_UPDATE  
`ListBackends` | NETWORK_LOAD_BALANCER_READ  
`CreateBackend` | NETWORK_LOAD_BALANCER_UPDATE  
`GetBackend` | NETWORK_LOAD_BALANCER_READ  
`UpdateBackend` | NETWORK_LOAD_BALANCER_UPDATE  
`DeleteBackend` | NETWORK_LOAD_BALANCER_UPDATE  
`GetHealthChecker` | NETWORK_LOAD_BALANCER_READ  
`UpdateHealthChecker` | NETWORK_LOAD_BALANCER_UPDATE  
`ListNetworkLoadBalancersHealth` | NETWORK_LOAD_BALANCER_READ  
`GetNetworkLoadBalancersHealth` | NETWORK_LOAD_BALANCER_READ  
`GetBackendSetHealth` | NETWORK_LOAD_BALANCER_READ  
`GetBackendHealth` | NETWORK_LOAD_BALANCER_READ  
`GetWorkRequest` | NETWORK_LOAD_BALANCER_READ  
`ListPolicies` | NETWORK_LOAD_BALANCER_INSPECT  
`ListProtocols` | NETWORK_LOAD_BALANCER_INSPECT  
`ListWorkRequests` | NETWORK_LOAD_BALANCER_READ  
`GetWorkRequest` | NETWORK_LOAD_BALANCER_READ  
`ListWorkRequestErrors` | NETWORK_LOAD_BALANCER_READ  
`ListWorkRequestLogs` | NETWORK_LOAD_BALANCER_READ  
Was this article helpful?
YesNo

