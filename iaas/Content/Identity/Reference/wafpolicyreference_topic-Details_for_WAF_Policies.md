Updated 2024-06-06
# Policy Details for Web Application Firewall
Web Application Firewall Policy details.
This topic covers details for writing [policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#How_Policies_Work) to control access to the Web Application Firewall service.
## Aggregate Resource-Type 🔗 
`waf-family`
## Individual Resource-Types 🔗 
`waf-policy`
`web-app-firewall`
`waf-network-address-list`
### Comments
A policy that uses `<verb> waf-family` is equivalent to writing one with a separate `<verb> <individual resource-type> `statement for each of the individual resource-types. 
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_WAF_Policies.htm#details) for details of the API operations covered by each verb, for each resource-type included in `waf-family`. 
## Supported Variables 🔗 
Only the general variables are supported. See [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General).
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for the `waf-policy` resource-type includes the same permissions and API operations as the `inspect` verb, plus the WAF_POLICY_READ permission and additional API operation GetWebAppFirewallPolicy.
[waf-policy](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_WAF_Policies.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  WAF_POLICY_INSPECT |  `ListWebAppFirewallPolicies` `ListProtectionCapabilities` `ListProtectionCapabilityGroupTags` |  ListWorkRequests GetWorkRequest ListWorkRequestErrors ListWorkRequestLogs  
read |  INSPECT + WAF_POLICY_READ |  INSPECT + `GetWebAppFirewallPolicy` |  none  
use |  READ + WAF_POLICY_ATTACH WAF_POLICY_DETACH WAF_POLICY_UPDATE |  READ + `UpdateWebAppFirewallPolicy` |  CreateWebAppFirewall UpdateWebAppFirewall DeleteWebAppFirewall  
manage |  USE + WAF_POLICY_CREATE WAF_POLICY_DELETE WAF_POLICY_MOVE WEB_APP_FIREWALL_CREATE |  USE + `CreateWebAppFirewallPolicy` `DeleteWebAppFirewallPolicy` `ChangeWebAppFirewallPolicyCompartment` |  CreateWebAppFirewall  
[web-app-firewall](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_WAF_Policies.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  WEB_APP_FIREWALL_INSPECT | `ListWebAppFirwewalls` |  ListWorkRequests GetWorkRequest ListWorkRequestErrors ListWorkRequestLogs  
read |  INSPECT + WEB_APP_FIREWALL_READ |  INSPECT + `GetWebAppFirewall` `GetLogging` |  none  
use |  READ + WEB_APP_FIREWALL_UPDATE |  READ + StartLogging UpdateLogging StopLogging |  UpdateWebAppFirewall  
manage |  USE + WEB_APP_FIREWALL_CREATE WEB_APP_FIREWALL_DELETE WEB_APP_FIREWALL_MOVE |  USE + `ChangeWebAppFirewallCompartment` |  CreateWebAppFirewall DeleteWebAppFirewall  
[waf-network-address-list](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_WAF_Policies.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  WAF_NETWORK_ADDRESS_LIST_INSPECT | `ListNetworkAdressLists` |  ListWorkRequests GetWorkRequest ListWorkRequestErrors ListWorkRequestLogs  
read |  INSPECT + WAF_NETWORK_ADDRESS_LIST_READ |  INSPECT + `GetNetworkAddressList` |  none  
use |  READ + WAF_NETWORK_ADDRESS_LIST_UPDATE WAF_NETWORK_ADDRESS_LIST_USE |  READ + UpdateNetwokAddressList |  none  
manage |  USE + WAF_NETWORK_ADDRESS_LIST_CREATE WAF_NETWORK_ADDRESS_LIST_DELETE WAF_NETWORK_ADDRESS_LIST_MOVE |  USE + `CreateNetworkAddressList` `DeleteNetworkAddressList` `ChangeNetworkAddressListCompartment` |  none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`ListWebAppFirewallPolicies` | WAF_POLICY_INSPECT  
`CreateWebAppFirewallPolicy` | WAF_POLICY_CREATE   
`GetWebAppFirewallPolicy` | WAF_POLICY_READ  
`UpdateWebAppFirewallPolicy` | WAF_POLICY_UPDATE  
`DeleteWebAppFirewallPolicy` | WAF_POLICY_DELETE  
`ChangeWebAppFirewallPolicyCompartment` | WAF_POLICY_MOVE  
`ListWorkRequests` | WAF_POLICY_INSPECT + WEB_APP_FIREWALL_INSPECT +WAF_NETWORK_ADDRESS_LIST_INSPECT  
`GetWorkRequest` |  WAF_POLICY_INSPECT +  WEB_APP_FIREWALL_INSPECT + WAF_NETWORK_ADDRESS_LIST_INSPECT  
`ListWorkRequestErrors` |  WAF_POLICY_INSPECT +  WEB_APP_FIREWALL_INSPECT + WAF_NETWORK_ADDRESS_LIST_INSPECT  
`ListWorkRequestLogs` |  WAF_POLICY_INSPECT +  WEB_APP_FIREWALL_INSPECT + WAF_NETWORK_ADDRESS_LIST_INSPECT  
`ListNetworkAddressLists` | WAF_NETWORK_ADDRESS_LIST_INSPECT  
`CreateNetworkAddressList` | WAF_NETWORK_ADDRESS_LIST_CREATE  
`GetNetworkAddressList` | WAF_NETWORK_ADDRESS_LIST_READ  
`UpdateNetworkAddressList` | WAF_NETWORK_ADDRESS_LIST_UPDATE  
`DeleteNetworkAddressList` | WAF_NETWORK_ADDRESS_LIST_DELETE  
`ChangeNetworkAddressListCompartment` | WAF_NETWORK_ADDRESS_LIST_MOVE  
`ListProtectionCapabilities` | WAF_POLICY_INSPECT  
`ListProtectionCapabilityGroupTags` | WAF_POLICY_INSPECT  
`ListWebAppFirewalls` | WEB_APP_FIREWALL_INSPECT  
`CreateWebAppFirewall` |  WEB_APP_FIREWALL_CREATE +  WAF_POLICY_ATTACH + LOAD_BALANCER_UPDATE  
`GetWebAppFirewall ` | WEB_APP_FIREWALL_READ  
`UpdateWebAppFirewall` |  WEB_APP_FIREWALL_UPDATE +  WAF_POLICY_ATTACH + WAF_POLICY_DETACH + LOAD_BALANCER_UPDATE  
`DeleteWebAppFirewall` |  WEB_APP_FIREWALL_DELETE + WAF_POLICY_DETACH + LOAD_BALANCER_UPDATE  
`ChangeWebAppFirewallCompartment` | WEB_APP_FIREWALL_MOVE  
`StartLogging` | WEB_APP_FIREWALL_UPDATE  
`UpdateLogging` | WEB_APP_FIREWALL_UPDATE  
`GetLogging` | WEB_APP_FIREWALL_READ  
`StopLogging` | WEB_APP_FIREWALL_UPDATE  
Was this article helpful?
YesNo

