Updated 2024-06-06
# Details for IAM with Identity Domains
This topic covers details for writing policies to control access to IAM (for tenancies that have identity domains).
## Resource-Types 🔗 
`authentication-policies`
`compartments`
`credentials`
`domains`
`dynamic-groups`
`groups`
`iamworkrequest`
`identity-providers`
`network-sources`
`policies`
`tag-defaults`
`tag-namespaces`
`tenancies`
`users`
`workrequest`
## Supported Variables 🔗 
IAM supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")), plus additional ones listed here:
Operations for This Resource-Type... | Can Use These Variables... | Variable Type | Comments  
---|---|---|---  
`users` | `target.user.id` | Entity (OCID) | Not available to use with [CreateUser](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/CreateUser) or [ListUsers](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/ListUsers).  
`target.user.name` | String | Not available to use with [ListUsers](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/ListUsers).  
`target.resource.domain.id` | Entity (OCID)  
`target.resource.domain.name` | String  
`groups` | `target.group.id` | Entity (OCID) | Not available to use with [CreateGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/CreateGroup) or [ListGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/ListGroups).  
`target.group.name` | String | Not available to use with [ListGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/ListGroups).  
`target.group.member` | Boolean |  True if request.user is a member of target.group. False if the service is creating the target.group. Not available to use with [ListGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/ListGroups).  
`target.resource.domain.id` | Entity (OCID)  
`target.resource.domain.name` | String  
`dynamic-groups` | `target.dynamicgroup.id` | Entity (OCID) | Not available to use with [CreateDynamicGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/CreateDynamicGroup) or [ListDynamicGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/ListDynamicGroups).  
`target.dynamicgroup.name` | String | Not available to use with [CreateDynamicGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/CreateDynamicGroup) or [ListDynamicGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/ListDynamicGroups).  
`target.resource.domain.id` | Entity (OCID)  
`target.resource.domain.name` | String  
`policies` |  `target.policy.id` | Entity (OCID) | Not available to use with [CreatePolicy](https://docs.oracle.com/iaas/api/#/en/identity/latest/Policy/CreatePolicy) or [ListPolicies](https://docs.oracle.com/iaas/api/#/en/identity/latest/Policy/ListPolicies).  
`target.policy.name` | String | Not available to use with [ListPolicies](https://docs.oracle.com/iaas/api/#/en/identity/latest/Policy/ListPolicies).  
`target.policy.autoupdate` | Boolean | Not available to use with [ListPolicies](https://docs.oracle.com/iaas/api/#/en/identity/latest/Policy/ListPolicies).  
`compartments` |  `target.compartment.id` | Entity (OCID) |  This is a universal variable available to use with any request across all services (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")), except it's not available to use with [ListCompartments](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/ListCompartments). For [CreateCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/CreateCompartment), this will be the value of the parent compartment (for example, the root compartment).  
`target.compartment.name` | String | This is a universal variable available to use with any request across all services (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/policyreference_topic-General_Variables_for_All_Requests.htm "Use the following general variables for all requests")), except it's not available to use with [ListCompartments](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/ListCompartments).  
`credentials` | `target.credential.type` | String | For example, "smtp", "switft", "secretkey".  
`target.user.id` | Entity (OCID)  
`target.user.name` | String  
`target.resource.domain.id` | Entity (OCID)  
`target.resource.domain.name` | String  
`domain` |  `target.domain.id` | Entity (OCID) | Not available to use with [CreateDomain](https://docs.oracle.com/iaas/api/#/en/identity/latest/Domain/CreateDomain) or [ListDomains](https://docs.oracle.com/iaas/api/#/en/identity/latest/DomainSummary/ListDomains).  
`target.domain.name` | String |  Not available to use with [ListDomains](https://docs.oracle.com/iaas/api/#/en/identity/latest/DomainSummary/ListDomains).   
`tag-namespace` |  `target.tag-namespace.id` | Entity (OCID) |  This variable is supported only in statements granting permissions for the `tag-namespaces` resource-type. For an example, see [Tags and Tag Namespace Concepts](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm). Not available to use with [CreateTagNamespace](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespace/CreateTagNamespace) or [ListTagNamespaces](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespaceSummary/ListTagNamespaces).   
`target.tag-namespace.name` | String |  Not available to use with [ListTagNamespaces](https://docs.oracle.com/iaas/api/#/en/identity/latest/TagNamespaceSummary/ListTagNamespaces).   
## Details for Verbs + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access. 
For example, the `read` verb for compartments covers no extra permissions or API operations compared to the `inspect` verb. The `use` verb includes the same ones as the `read` verb, plus the COMPARTMENT_UPDATE permission and `UpdateCompartment` API operation. The `manage` verb includes the same permissions and API operations as the `use` verb, plus the COMPARTMENT_CREATE permission and two API operations: `CreateCompartment` and `DeleteCompartment`
[authentication-policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | AUTHENTICATION_POLICY_INSPECT | `GetAuthenticationPolicy` | none  
read | no extra | no extra | none  
use | no extra | no extra | none  
manage | USE + AUTHENTICATION_POLICY_UPDATE | USE + `UpdateAuthenticationPolicy` | none  
[compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
To move a compartment (that is, use the `MoveCompartment` operation) you must belong to a group that has `manage all-resources` permissions on the lowest shared parent compartment of the current compartment and the destination compartment.
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | COMPARTMENT_INSPECT | `ListCompartments` `GetCompartment` `ListAvailabilityDomains` `ListFaultDomains` | none  
read | no extra | no extra | none  
use | READ + COMPARTMENT_UPDATE | READ + `UpdateCompartment` `GetWorkRequest` | none  
manage | USE + COMPARTMENT_CREATE COMPARTMENT_DELETE COMPARTMENT_RECOVER | USE + `CreateCompartment` `DeleteCompartment` `RecoverCompartment` | none  
[credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
The `credentials` resource type refers to only the [SMTP credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/access/working-with-smtp-credentials.htm#SMTP "Simple Mail Transfer Protocol \(SMTP\) credentials are needed in order to send email through the Email Delivery service."). Permissions to work with other credentials that can be added to a user (such as auth tokens, API keys, and customer secret keys) are included with [`users`](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm#users) resource permissions. 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | CREDENTIAL_INSPECT | `ListSmtpCredentials` | none  
read | no extra | no extra | none  
use | no extra | no extra | none  
manage | USE + CREDENTIAL_ADD CREDENTIAL_UPDATE CREDENTIAL_REMOVE | USE + `CreateSmtpCredential` `UpdateSmtpCredential` `DeleteSmtpCredential` | none  
[domains](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  DOMAIN_INSPECT |  `ListDomains` |  none  
read |  INSPECT + DOMAIN_READ DOMAIN_LICENSETYPE_READ |  `GetDomain` `GetDomainLicenseTypes` |  none  
use |  READ + DOMAIN_UPDATE IAM_WORKREQUEST_READ |  READ + `UpdateDomain` `GetIamWorkRequest` |  none  
manage |  USE + DOMAIN_CREATE DOMAIN_DELETE DOMAIN_MOVE DOMAIN_REPLICATE DOMAIN_ACTIVATE DOMAIN_DEACTIVATE |  USE + `CreateDomain` `DeleteDomain` `ChangeDomainCompartment` `ChangeSku` `ReplicateDomainRegion` `ActivateDomain` `DeactivateDomain` |  none  
[dynamic-groups](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | DYNAMIC_GROUP_INSPECT | `ListDynamicGroups` `GetDynamicGroup` | _No extra_  
read | no extra | no extra | no extra  
use | READ + DYNAMIC_GROUP_UPDATE | READ + `UpdateDynamicGroup` | No extra  
manage | USE + DYNAMIC_GROUP_CREATE DYNAMIC_GROUP_DELETE | USE + `CreateDynamicGroup` `DeleteDynamicGroup` | no extra  
[groups](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | GROUP_INSPECT | `ListGroups` `GetGroup` | `GetUserGroupMembership `(also need `inspect users`) `ListIdpGroupMappings`, `GetIdpGroupMapping` (both also need `inspect identity-providers`)  
read | no extra | no extra | no extra  
use | READ + GROUP_UPDATE | READ + `UpdateGroup` | READ + `AddUserToGroup` (also need `use users`) `RemoveUserFromGroup` (also need `use users`) `AddIdpGroupMapping`, `DeleteIdpGroupMapping` (both also need `manage identity-providers`)  
manage | USE + GROUP_CREATE GROUP_DELETE | USE + `CreateGroup` `DeleteGroup` | no extra  
[identity-providers](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | IDENTITY_PROVIDER_INSPECT | `ListIdentityProviders` `GetIdentityProvider` | `ListIdpGroupMappings`, `GetIdpGroupMapping` (both also need `inspect groups`)   
read | no extra | no extra | no extra  
use | no extra | no extra | no extra  
manage | USE + IDENTITY_PROVIDER_UPDATE IDENTITY_PROVIDER_CREATE IDENTITY_PROVIDER_DELETE | USE + `UpdateIdentityProvider` `CreateIdentityProvider` `DeleteIdentityProvider` | USE + `AddIdpGroupMapping`, `DeleteIdpGroupMapping` (both also need `use groups`)  
[network-sources](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | NETWORK_SOURCE_INSPECT | `ListNetworkSources` `GetNetworkSource` | _No extra_  
read | no extra | no extra | no extra  
use | READ + NETWORK_SOURCE_UPDATE | READ + `UpdateNetworkSource` | No extra  
manage | USE + NETWORK_SOURCE_CREATE NETWORK_SOURCE_DELETE | USE + `CreateNetworkSource` `DeleteNetworkSource` | no extra  
[policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | POLICY_READ | `ListPolicies` `GetPolicy` | none  
read | no extra | no extra | none  
use | no extra | no extra **Note:** The ability to update policies is available only with `manage policies`. | none  
manage | USE + POLICY_UPDATE POLICY_CREATE POLICY_DELETE | USE + `UpdatePolicy` `CreatePolicy` `DeletePolicy` | none  
[tag-namespaces](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | TAG_NAMESPACE_INSPECT | `BulkEditTags` `ListTagNamespaces` `GetTagNamespace` `ListTags` `ListCostTrackingTags` `GetTag` `GetTaggingWorkRequest` `ListTaggingWorkRequest` `ListTaggingWorkRequestErrors` `ListTaggingWorkRequestLogs` | none  
read | no extra | no extra | none  
use | READ + TAG_NAMESPACE_USE **Note** : To apply, update, or remove defined tags for a resource, a user must be granted permissions on the resource and permissions to use the tag namespace. | READ + `CreateTag` `UpdateTag` | none  
manage | USE + TAG_NAMESPACE_UPDATE TAG_NAMESPACE_CREATE TAG_NAMESPACE_MOVE TAG_NAMESPACE_DELETE | USE + `UpdateTagNamespace` `CreateTagNamespace` `ChangeTagNamespaceCompartment` `CascadeDeleteTagNamespace` `DeleteTagNamespace` `DeleteTag` `BulkDeleteTags` | none  
[tag-defaults](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect |  TAG_DEFAULT_INSPECT TAG_NAMESPACE_READ (Use both permissions) | `ListTagDefaults` `GetTagDefault` |  none  
read | no extra | no extra |  none  
use | no extra | no extra | none  
manage | INSPECT + TAG_DEFAULT_CREATE TAG_DEFAULT_UPDATE TAG_DEFAULT_DELETE | USE + `CreateTagDefault` `UpdateTagDefault` `DeleteTagDefault` | none  
[tenancies](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | TENANCY_INSPECT | `ListRegionSubscriptions` `GetTenancy` `ListRegions` | none  
read | no extra | no extra | none  
use | READ + TENANCY_UPDATE | no extra | none  
manage | USE + TENANCY_UPDATE | USE + `CreateRegionSubscription` | none  
[users](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm)
Note that to work with the SMTP credentials for a user, you must have permissions for the `credentials[](https://docs.oracle.com/en-us/iaas/Content/Identity/policyreference/iampolicyreference.htm#credenti)` resource type. 
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
inspect | USER_INSPECT | `ListUsers` `GetUser` | `GetUserGroupMembership `(also need `inspect groups`)   
read | INSPECT + USER_READ | INSPECT + `ListApiKeys` `ListSwiftPasswords` `ListAuthTokens` `ListCustomerSecretKeys` `ListOAuthClientCredentials` `ListMfaTotpDevices` | no extra  
use | READ + USER_UPDATE | READ + `UpdateUser` | READ + `AddUserToGroup` (also need `use groups`) `RemoveUserFromGroup` (also need `use groups`)  
manage | USE + USER_CREATE USER_DELETE USER_UNBLOCK USER_APIKEY_ADD USER_APIKEY_REMOVE USER_UIPASS_SET USER_UIPASS_RESET USER_SWIFTPASS_SET USER_SWIFTPASS_RESET USER_SWIFTPASS_REMOVE USER_AUTHTOKEN_SET USER_AUTHTOKEN_RESET USER_AUTHTOKEN_REMOVE USER_OAUTH2_CLIENT_CRED_CREATE USER_OAUTH2_CLIENT_CRED_UPDATE USER_OAUTH2_CLIENT_CRED_REMOVE USER_SECRETKEY_ADD USER_SECRETKEY_UPDATE USER_SECRETKEY_REMOVE  USER_SUPPORT_ACCOUNT_LINK USER_SUPPORT_ACCOUNT_UNLINK USER_TOTPDEVICE_ADD USER_TOTPDEVICE_REMOVE USER_TOTPDEVICE_UPDATE | USE + `CreateUser` `DeleteUser` `UpdateUserState` `UploadApiKey` `DeleteApiKey` `CreateOrResetUIPassword` `UpdateSwiftPassword` `CreateSwiftPassword` `DeleteSwiftPassword` `UpdateAuthToken` `CreateAuthToken` `DeleteAuthToken` `CreateOAuthClientCredential` `UpdateOAuthClientCredential` `DeleteOAuthClientCredential` `CreateSecretKey` `UpdateCustomerSecretKey` `DeleteCustomerSecretKey` `CreateOAuthClientCredential` `UpdateAuthClientCredential` `DeleteOAuthClientCredential` `LinkSupportAccount` `UnlinkSupportAccount` `CreateMfaTotpDevice` `ActivateMfaTotpDevice` `DeleteMfaTotpDevice` | no extra  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type.
For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/policies/permissions.htm#permissions "Permissions are the atomic units of authorization that control a user's ability to perform operations on resources. Oracle defines all the permissions in the policy language.").
API Operation | Permissions Required to Use the Operation  
---|---  
`ListRegions` | TENANCY_INSPECT  
`ListRegionSubscriptions` | TENANCY_INSPECT  
`CreateRegionSubscription` | TENANCY_UPDATE  
`GetTenancy` | TENANCY_INSPECT  
`ListDomains` | DOMAIN_INSPECT  
`GetDomain` | DOMAIN_READ  
`CreateDomain` | DOMAIN_CREATE  
`ActivateDomain` | DOMAIN_ACTIVATE  
`UpdateDomain` | DOMAIN_UPDATE  
`ReplicateDomainRegion` | DOMAIN_REPLICATE  
`ChangeDomainCompartment` | DOMAIN_MOVE  
`GetDomainLicenseTypes` | DOMAIN_LICENSETYPE_READ  
`ChangeSku` | DOMAIN_MOVE  
`DeactivateDomain` | DOMAIN_DEACTIVATE  
`DeleteDomain` | DOMAIN_DELETE  
`GetAuthenticationPolicy` | AUTHENTICATION_POLICY_INSPECT  
`UpdateAuthenticationPolicy` | AUTHENTICATION_POLICY_UPDATE  
`ListAvailabilityDomains` | COMPARTMENT_INSPECT  
`ListFaultDomains` | COMPARTMENT_INSPECT  
`ListCompartments` | COMPARTMENT_INSPECT  
`GetCompartment` | COMPARTMENT_INSPECT  
`UpdateCompartment` | COMPARTMENT_UPDATE  
`CreateCompartment` | COMPARTMENT_CREATE  
`RecoverCompartment` | COMPARTMENT_RECOVER  
`DeleteCompartment` | COMPARTMENT_DELETE  
`MoveCompartment` | There is not a single permission associated with the `MoveCompartment` operation. This operation requires `manage all-resources` permissions on the lowest shared parent compartment of the current compartment and the destination compartment.  
`GetWorkRequest` | COMPARTMENT_READ  
`ListUsers` | USER_INSPECT  
`GetUser` | USER_INSPECT   
`UpdateUser` | USER_UPDATE  
`UpdateUserState` | USER_UPDATE and USER_UNBLOCK  
`CreateUser` |  USER_CREATE  
`DeleteUser` | USER_DELETE  
`CreateOrResetUIPassword` | USER_UPDATE and USER_UIPASS_RESET  
`ListApiKeys` | USER_READ  
`UploadApiKey` |  USER_UPDATE and USER_APIKEY_ADD   
`DeleteApiKey` | USER_UPDATE and USER_APIKEY_REMOVE   
`ListAuthTokens` | USER_READ  
`UpdateAuthToken` | USER_UPDATE and USER_AUTHTOKEN_RESET  
`CreateAuthToken` | USER_UPDATE and USER_AUTHTOKEN_SET  
`DeleteAuthToken` | USER_UPDATE and USER_AUTHTOKEN_REMOVE  
`ListSwiftPasswords` | USER_READ  
`UpdateSwiftPassword` | USER_UPDATE and USER_SWIFTPASS_RESET  
`CreateSwiftPassword` | USER_UPDATE and USER_SWIFTPASS_SET  
`DeleteSwiftPassword` | USER_UPDATE and USER_SWIFTPASS_REMOVE  
`ListCustomerSecretKeys` | USER_READ  
`CreateSecretKey` | USER_UPDATE and USER_SECRETKEY_ADD  
`UpdateCustomerSecretKey` | USER_UPDATE and USER_SECRETKEY_UPDATE  
`DeleteCustomerSecretKey` | USER_UPDATE and USER_SECRETKEY_REMOVE  
`CreateOAuthClientCredential` | USER_UPDATE and USER_OAUTH2_CLIENT_CRED_CREATE  
`UpdateOAuthClientCredential` | USER_UPDATE and USER_OAUTH2_CLIENT_CRED_UPDATE  
`ListOAuthClientCredentials` | USER_READ  
`DeleteOAuthClientCredential` | USER_UPDATE and USER_OAUTH2_CLIENT_CRED_REMOVE  
`LinkSupportAccount` | USER_SUPPORT_ACCOUNT_LINK  
`UnlinkSupportAccount` | USER_SUPPORT_ACCOUNT_UNLINK  
`CreateSmtpCredential` | CREDENTIAL_ADD  
`ListSmtpCredentials` | CREDENTIAL_INSPECT  
`UpdateSmtpCredential` | CREDENTIAL_UPDATE  
`DeleteSmtpCredential` | CREDENTIAL_REMOVE  
`ListUserGroupMemberships` | GROUP_INSPECT and USER_INSPECT  
`GetUserGroupMembership` | USER_INSPECT and GROUP_INSPECT   
`AddUserToGroup` | GROUP_UPDATE and USER_UPDATE  
`RemoveUserFromGroup` | GROUP_UPDATE and USER_UPDATE  
`ListGroups` | GROUP_INSPECT  
`GetGroup` | GROUP_INSPECT  
`UpdateGroup` | GROUP_UPDATE  
`CreateGroup` | GROUP_CREATE  
`DeleteGroup` | GROUP_DELETE  
`ListDynamicGroups` | DYNAMIC_GROUP_INSPECT  
`GetDynamicGroup` | DYNAMIC_GROUP_INSPECT  
`UpdateDynamicGroup` | DYNAMIC_GROUP_UPDATE  
`CreateDynamicGroup` | DYNAMIC_GROUP_CREATE  
`DeleteDynamicGroup` | DYNAMIC_GROUP_DELETE  
`GetNetworkSource` | NETWORK_SOURCE_INSPECT  
`ListNetworkSources` | NETWORK_SOURCE_INSPECT  
`CreateNetworkSource` | NETWORK_SOURCE_CREATE  
`UpdateNetworkSource` | NETWORK_SOURCE_UPDATE  
`DeleteNetworkSource` | NETWORK_SOURCE_DELETE  
`ListPolicies` | POLICY_READ  
`GetPolicy` | POLICY_READ  
`UpdatePolicy` | POLICY_UPDATE  
`CreatePolicy` | POLICY_CREATE  
`DeletePolicy` | POLICY_DELETE  
`ListIdentityProviders` | IDENTITY_PROVIDER_INSPECT  
`GetIdentityProvider` | IDENTITY_PROVIDER_INSPECT  
`UpdateIdentityProvider` | IDENTITY_PROVIDER_UPDATE  
`CreateIdentityProvider` | IDENTITY_PROVIDER_CREATE  
`DeleteIdentityProvider` | IDENTITY_PROVIDER_DELETE  
`ListIdpGroupMappings` | IDENTITY_PROVIDER_INSPECT and GROUP_INSPECT  
`GetIdpGroupMapping` | IDENTITY_PROVIDER_INSPECT and GROUP_INSPECT  
`AddIdpGroupMapping` | IDENTITY_PROVIDER_UPDATE and GROUP_UPDATE  
`DeleteIdpGroupMapping` | IDENTITY_PROVIDER_UPDATE and GROUP_UPDATE  
`ListIamWorkRequests` | IAM_WORKREQUEST_INSPECT  
`GetIamWorkRequest` | IAM_WORKREQUEST_READ  
`ListWorkRequestErrors` | IAM_WORKREQUEST_INSPECT  
`ListIamWorkRequestLogs` | IAM_WORKREQUEST_INSPECT  
`ListTagNamespaces` | TAG_NAMESPACE_INSPECT  
`ListTaggingWorkRequest` | TAG_NAMESPACE_INSPECT  
`ListTaggingWorkRequestErrors` | TAG_NAMESPACE_INSPECT  
`ListTaggingWorkRequestLogs` | TAG_NAMESPACE_INSPECT  
`GetTaggingWorkRequest` | TAG_NAMESPACE_INSPECT  
`GetTagNamespace` | TAG_NAMESPACE_INSPECT  
`CreateTagNamespace` | TAG_NAMESPACE_CREATE  
`UpdateTagNamespace` | TAG_NAMESPACE_UPDATE  
`ChangeTagNamespaceCompartment` | TAG_NAMESPACE_MOVE  
`CascadeDeleteTagNamespace` |  TAG_NAMESPACE_DELETE  
`DeleteTagNamespace` |  TAG_NAMESPACE_DELETE  
`ListTags` | TAG_NAMESPACE_INSPECT  
`BulkEditTags` | TAG_NAMESPACE_INSPECT  
`ListCostTrackingTags` | TAG_NAMESPACE_INSPECT  
`GetTag` | TAG_NAMESPACE_INSPECT  
`CreateTag` | TAG_NAMESPACE_USE  
`UpdateTag` | TAG_NAMESPACE_USE  
`DeleteTag` | TAG_NAMESPACE_DELETE  
`BulkDeleteTags` |  TAG_NAMESPACE_DELETE  
`ListTagDefaults` | TAG_DEFAULT_INSPECT  
`GetTagDefault` | TAG_DEFAULT_INSPECT  
`CreateTagDefault` | TAG_DEFAULT_MANAGE  
`UpdateTagDefault` | TAG_DEFAULT_MANAGE  
`DeleteTagDefault` | TAG_DEFAULT_MANAGE  
Was this article helpful?
YesNo

