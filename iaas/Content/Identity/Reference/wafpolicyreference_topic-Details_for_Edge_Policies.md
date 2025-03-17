Updated 2024-06-06
# Policy Details for Edge Policies
Policy Details for Edge Policies
This topic covers details for writing [policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#How_Policies_Work) for the Edge Policies.
## Aggregate Resource-Type 🔗 
`waas-family`
## Individual Resource-Types 🔗 
`waas-policy`
`waas-certificate`
`waas-work-request`
`waas-metering`
`waas-custom-protection-rule`
`waas-address-list`
`http-redirects`
### Comments
A policy that uses `<verb> waas` is equivalent to writing one with a separate `<verb> <individual resource-type>` statement for each of the individual resource-types.
See the table in [Details for Verb + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_Edge_Policies.htm#Details) for details of the API operations covered by each verb, for each individual resource-type included in `waas`.
## Supported Variables 🔗 
The WAF Service supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)), plus the ones listed here.
Variable | Variable Type | Comments  
---|---|---  
`target.waas-policy.id` | Entity (OCID) | Use this variable to control access to specific WAAS policies by OCID.  
`target.waf-rule-key` | String | Use this variable to control access to specific WAF rules by name.  
`target.waas-work-request.id` | Entity (OCID) |  The OCID of WAAS work requests.  
`target.waas-policy-certificate.id` | Entity (OCID) |  The OCID of SSL certificates configured in a WAAS policy.  
`target.certificate.destination-compartment.id` | Entity (OCID) |  The OCID of a compartment.  
`target.certificate.source-compartment.id` | Entity (OCID) |  The OCID of a compartment.  
`target.waas-policy.destination-compartment.id` | Entity (OCID) |  The OCID of a compartment.  
`target.waas-policy.source-compartment.id	` | Entity (OCID) |  The OCID of a compartment.  
`target.waas-custom-protection-rule.id	` | Entity (OCID) |  The OCID of a custom protection rule.  
`target.waas-custom-protection-rule.source-compartment.id` | Entity (OCID) |  The OCID of a compartment.  
`target.waas-custom-protection-rule.destination-compartment.id` | Entity (OCID) |  The OCID of a compartment.  
`target.waas-address-list.id` | Entity (OCID) |  The OCID of an address list.  
`target.waas-address-list.source-compartment.id ` | Entity (OCID) |  The OCID of a compartment.  
`target.waas-address-list.destination-compartment.id` | Entity (OCID) |  The OCID of a compartment.  
`target.http-redirects.id` | Entity (OCID) |  The OCID of an HTTP redirect.  
`target.http-redirects.source-compartment.id` | Entity (OCID) |  The OCID of a compartment.  
`target.http-redirects.destination-compartment.id` | Entity (OCID) |  The OCID of a compartment.  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `use` and `manage` verbs for the `waas-policy` resource-type cover no extra permissions or API operations compared to the `read` verb.
[waas-policy](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_Edge_Policies.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | WAAS_POLICY_INSPECT | `ListWaasPolicies` `ListWaasOriginRequestCidrs` `ListReports` `ListWafReports` `ListWafRules` | none  
read | INSPECT + WAAS_POLICY_READ | INSPECT + `GetWaasPolicy` `GetWafTraffic` `GetWafBlocked` `GetWafRequests` `GetWafSettings` `GetAccessRules` `GetCaptchas` `GetDeviceFingerprintChallenge` `GetHumanInteractionChallenge` `GetJSChallenge` `GetIpRateLimiting` `GetGoodBots` `GetWafWhitelists` `GetWafRecommendations` `GetWafRule` `GetThreatFeeds` `GetAlerts` | none  
use | READ + WAAS_POLICY_UPDATE | READ + `UpdateWaasPolicy` `UpdateWafSettings` `UpdateAccessRules` `UpdateCaptchas` `UpdateDeviceFingerprintChallenge` `UpdateHumanInteractionChallenge` `UpdateJSChallenge` `UpdateIpRateLimiting` `UpdateGoodBots` `UpdateWafWhitelists` `AcceptWafRecommendations` `UpdateWafRuleActions` `UpdateThreatFeedAction` | none  
manage | USE + WAAS_POLICY_CREATE WAAS_POLICY_DELETE WAAS_POLICY_MOVE | USE + `CreateWaasPolicy` `DeleteWaasPolicy` `ChangeWaasPolicyCompartment` | none  
[waas-certificate](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_Edge_Policies.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | WAAS_CERTIFICATE_INSPECT | `ListCertificates` | none  
read | INSPECT + WAAS_CERTIFICATE_READ | INSPECT + `GetCertificate` | none  
use | no extra | no extra | none  
manage | USE + WAAS_CERTIFICATE_CREATE WAAS_CERTFICATE_DELETE WAAS_CERTFICATE_MOVE | USE + `DeleteCertificate` `CreateCertificate` `ChangeCertificateCompartment` | none  
[waas-work-request](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_Edge_Policies.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | WAAS_WORK_REQUEST_INSPECT | `ListWorkRequests` | none  
read | INSPECT + WAAS_WORK_REQUEST_READ | INSPECT + `GetWorkRequestDetails` | none  
use | no extra | no extra | none  
manage | USE + WAAS_WORK_REQUEST_DELETE | USE + `DeleteWorkRequest` | none  
[waas-metering](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_Edge_Policies.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
read | WAAS_METERING_READ | `GetWafReport` | none  
[waas-custom-protection-rule](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_Edge_Policies.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | WAAS_CUSTOM_PROTECTION_RULE_INSPECT | `ListCustomProtectionRules` | none  
read | INSPECT + WAAS_CUSTOM_PROTECTION_RULE_READ | INSPECT + `GetCustomProtectionRule` | none  
use | READ + WAAS_CUSTOM_PROTECTION_RULE_UPDATE WAAS_CUSTOM_PROTECTION_RULE_USE | READ + `UpdateCustomProtectionRule` | none  
manage | USE + WAAS_CUSTOM_PROTECTION_RULE_CREATE WAAS_CUSTOM_PROTECTION_RULE_DELETE WAAS_CUSTOM_PROTECTION_RULE_MOVE | USE + `CreateCustomProtectionRule` `DeleteCustomProtectionRule` `ChangeCustomProtectionRuleCompartment` | none  
[waas-address-list](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_Edge_Policies.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | WAAS_ADDRESS_LIST_INSPECT | `ListAddressLists` | none  
read | INSPECT + WAAS_ADDRESS_LIST_READ | INSPECT + `GetAddressList` | none  
use | READ + WAAS_ADDRESS_LIST_UPDATE WAAS_ADDRESS_LIST_USE | READ + `UpdateAddressList` | none  
manage | USE + WAAS_ADDRESS_LIST_CREATE WAAS_ADDRESS_LIST_DELETE WAAS_ADDRESS_LIST_MOVE | USE + `CreateAddressList` `DeleteAddressList` `ChangeAddressListCompartment` | none  
[http-redirects](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/wafpolicyreference_topic-Details_for_Edge_Policies.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | HTTPREDIRECT_INSPECT | `ListHttpRedirects` | none  
read | INSPECT + HTTPREDIRECT_READ | INSPECT + `GetHttpRedirect` | none  
use | READ + HTTPREDIRECT_UPDATE | READ + `UpdateHttpRedirect` | none  
manage | USE + HTTPREDIRECT_CREATE HTTPREDIRECT_DELETE HTTPREDIRECT_MOVE | USE + `CreateHttpRedirect` `DeleteHttpRedirect` `ChangeHttpRedirectCompartment` | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
`CreateWaasPolicy` | WAAS_POLICY_CREATE  
`ListWaasPolcies` | WAAS_POLICY_INSPECT  
`GetWaasPolicy` | WAAS_POLICY_READ  
`UpdateWaasPolicy` | WAAS_POLICY_UPDATE  
`DeleteWaasPolicy` | WAAS_POLICY_DELETE  
`ChangeWaasPolicyCompartment` | WAAS_POLICY_MOVE  
`ListReports` | WAAS_POLICY_INSPECT  
`ListWafReports` | WAAS_POLICY_INSPECT  
`GetWafTraffic` | WAAS_POLICY_READ  
`GetWafBlocked` | WAAS_POLICY_READ  
`GetWafRequests` | WAAS_POLICY_READ  
`GetWafSettings` | WAAS_POLICY_READ  
`UpdateWafSettings` | WAAS_POLICY_UPDATE  
`GetAccessRules` | WAAS_POLICY_READ  
`UpdateAccessRules` | WAAS_POLICY_UPDATE  
`GetCaptchas` | WAAS_POLICY_READ  
`UpdateCaptchas` | WAAS_POLICY_UPDATE  
`GetDeviceFingerprintChallenge` | WAAS_POLICY_READ  
`UpdateDeviceFingerprintChallenge` | WAAS_POLICY_UPDATE  
`GetHumanInteractionChallenge` | WAAS_POLICY_READ  
`UpdateHumanInteractionChallenge` | WAAS_POLICY_UPDATE  
`GetJsChallenge` | WAAS_POLICY_READ  
`UpdateJsChallenge` | WAAS_POLICY_UPDATE  
`GetIpRateLimiting` | WAAS_POLICY_READ  
`UpdateIpRateLimiting` | WAAS_POLICY_UPDATE  
`GetGoodBots` | WAAS_POLICY_READ  
`UpdateGoodBots` | WAAS_POLICY_UPDATE  
`GetWafWhitelists` | WAAS_POLICY_READ  
`UpdateWafWhitelists` | WAAS_POLICY_UPDATE  
`GetWafRecommendations` | WAAS_POLICY_READ  
`AcceptWafRecommendations` | WAAS_POLICY_UPDATE  
`ListWafRules` | WAAS_POLICY_INSPECT  
`UpdateWafRuleActions` | WAAS_POLICY_UPDATE  
`GetWafRule` | WAAS_POLICY_READ  
`GetThreatFeeds` | WAAS_POLICY_READ  
`UpdateThreatFeedAction` | WAAS_POLICY_UPDATE  
`GetAlerts` | WAAS_POLICY_READ  
`ListWorkRequests` | WAAS_WORK_REQUEST_INSPECT  
`ListWaasOriginRequestCidrs` | WAAS_POLICY_INSPECT  
`GetWorkRequestDetails` | WAAS_WORK_REQUEST_READ  
`DeleteWorkRequest` | WAAS_WORK_REQUEST_DELETE  
`CreateCertificate` | WAAS_CERTIFICATE_CREATE  
`ListCertificates` | WAAS_CERTIFICATE_INSPECT  
`GetCertificate` | WAAS_CERTIFICATE_READ  
`DeleteCertificate` | WAAS_CERTIFICATE_DELETE  
`ChangeCertificateCompartment` | WAAS_CERTIFICATE_MOVE  
`GetWafReport` | WAAS_METERING_READ  
`CreateCustomProtectionRule` | WAAS_CUSTOM_PROTECTION_RULE_CREATE  
`ListCustomProtectionRules` | WAAS_CUSTOM_PROTECTION_RULE_INSPECT   
`GetCustomProtectionRule` | WAAS_CUSTOM_PROTECTION_RULE_READ  
`UpdateCustomProtectionRule` | WAAS_CUSTOM_PROTECTION_RULE_UPDATE  
`DeleteCustomProtectionRule` | WAAS_CUSTOM_PROTECTION_RULE_DELETE  
`ChangeCustomProtectionRuleCompartment` | WAAS_CUSTOM_PROTECTION_RULE_MOVE  
`CreateAddressList` | WAAS_ADDRESS_LIST_CREATE  
`GetAddressList` | WAAS_ADDRESS_LIST_READ  
`ListAddressLists` | WAAS_ADDRESS_LIST_INSPECT  
`ChangeAddressListCompartment` | WAAS_ADDRESS_LIST_MOVE  
`UpdateAddressList` | WAAS_ADDRESS_LIST_UPDATE  
`DeleteAddressList` | WAAS_ADDRESS_LIST_DELETE  
`ListHttpRedirects` | HTTPREDIRECT_INSPECT  
`GetHttpRedirect` | HTTPREDIRECT_READ  
`CreateHttpRedirect` | HTTPREDIRECT_CREATE  
`UpdateHttpRedirect` | HTTPREDIRECT_UPDATE  
`DeleteHttpRedirect` | HTTPREDIRECT_DELETE  
`ChangeHttpRedirectCompartment` | HTTPREDIRECT_MOVE  
Was this article helpful?
YesNo

