Updated 2025-01-30
# Details for Organization Management
This topic covers details for writing policies to control access to Organization Management.
## Resource-Types 🔗 
  * `organizations-family`
  * `organizations-link`
  * `organizations-recipient-invitation`
  * `organizations-sender-invitation`
  * `organizations-invitation`
  * `organizations-domain`
  * `organizations-domain-governance`
  * `organizations-entity`
  * `organizations-tenancy`
  * `organizations-order`
  * `organizations-subscription`
  * `organizations-subscription-mapping`
  * `organizations-assigned-subscription`
  * `organizations-subscription-region`
  * `organizations-governance-rules`
  * `organizations-enforced-governance-rules`


## Supported Variables 🔗 
Organization Management supports all the general variables (see [General Variables for All Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#General)), plus additional ones listed here:
**Required variables** (supplied by service for every request):
Variable | Variable Type | Comments  
---|---|---  
`target.resource.kind` | String | The resource kind name of the primary resource for the request.  
**Automatic Variables** (supplied by the SDK for every request):
Variable | Variable Type | Comments  
---|---|---  
`target.tenant.id` | Entity (OCID) | The OCID of the target tenant ID.  
## Details for Verb + Resource-Type Combinations 🔗 
The following tables show the [permissions](https://docs.oracle.com/iaas/Content/Identity/policies/permissions.htm) and API operations covered by each verb. The level of access is cumulative as you go from `inspect` > `read` > `use` > `manage`. For example, a group that can use a resource can also inspect and read that resource. A plus sign (+) in a table cell indicates incremental access compared to the cell directly above it, whereas "no extra" indicates no incremental access.
[organizations-family](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_LINK_INSPECTORGANIZATIONS_RECIPIENT_INVITATION_INSPECTORGANIZATIONS_SENDER_INVITATION_INSPECTORGANIZATIONS_DOMAIN_INSPECTORGANIZATIONS_DOMAIN_GOVERNANCE_INSPECTORGANIZATIONS_TENANCY_INSPECTORGANIZATIONS_SUBSCRIPTION_INSPECTORGANIZATIONS_SUBSCRIPTION_MAPPING_INSPECTORGANIZATIONS_ASSIGNED_SUBSCRIPTION_INSPECTORGANIZATIONS_SUBSCRIPTION_REGION_INSPECTGOVERNANCE_RULE_INSPECTORGANIZATIONS_ENTITY_INSPECTORGANIZATIONS_TENANCY_INSPECT | `ListLinks` `ListRecipientInvitations` `ListSenderInvitations` `ListDomains` `ListDomainGovernances``ListOrganizationTenancies``ListSubscriptions``ListSubscriptionMappings``ListAssignedSubscriptions``ListAvailableRegions``ListGovernanceRules``ListOrganizations` | none  
READ | _INSPECT_ + ORGANIZATIONS_LINK_READORGANIZATIONS_RECIPIENT_INVITATION_READORGANIZATIONS_SENDER_INVITATION_READORGANIZATIONS_DOMAIN_READORGANIZATIONS_DOMAIN_GOVERNANCE_READORGANIZATIONS_ENTITY_READORGANIZATIONS_TENANCY_READORGANIZATIONS_SUBSCRIPTION_READORGANIZATIONS_SUBSCRIPTION_MAPPING_READORGANIZATIONS_ASSIGNED_SUBSCRIPTION_READGOVERNANCE_RULE_READ | _INSPECT_ + `GetLink``GetRecipientInvitation``GetSenderInvitation``GetDomain``GetDomainGovernance``GetOrganizationTenancy``GetSubscriptionMapping ``GetAssignedSubscription``GetGovernanceRule``ListTenancyAttachments``GetTenancyAttachment` | none  
USE | _READ_ + ORGANIZATIONS_RECIPIENT_INVITATION_UPDATEORGANIZATIONS_DOMAIN_UPDATEORGANIZATIONS_DOMAIN_GOVERNANCE_UPDATEORGANIZATIONS_ENTITY_UPDATEORGANIZATIONS_SENDER_INVITATION_UPDATEGOVERNANCE_RULE_UPDATEGOVERNANCE_RULE_RETRY | _READ_ + `AcceptRecipientInvitation``IgnoreRecipientInvitation``CancelSenderInvitation``UpdateSenderInvitation``UpdateDomain``UpdateDomainGovernance``UpdateOrganization``GetGovernanceRule``DeleteInclusionCriterion``RetryGovernanceRule``RetryTenancyAttachment` | none  
MANAGE | _USE_ + ORGANIZATIONS_LINK_PARENT_DELETEORGANIZATIONS_LINK_CHILD_DELETEORGANIZATIONS_SUBSCRIPTION_MAPPING_CREATEORGANIZATIONS_SENDER_INVITATION_CREATEORGANIZATIONS_DOMAIN_CREATEORGANIZATIONS_DOMAIN_DELETEORGANIZATIONS_ORDER_ACTIVATEORGANIZATIONS_DOMAIN_GOVERNANCE_CREATEORGANIZATIONS_DOMAIN_GOVERNANCE_DELETEORGANIZATIONS_ENTITY_UPDATEORGANIZATIONS_TENANCY_CREATEORGANIZATIONS_SUBSCRIPTION_MAPPING_DELETEORGANIZATIONS_TENANCY_DELETEORGANIZATIONS_TENANCY_RESTOREGOVERNANCE_RULE_CREATEGOVERNANCE_RULE_DELETE | _USE_ + `DeleteLink``CreateSenderInvitation``CreateDomain``DeleteDomain``ActivateOrder``CreateDomainGovernance``DeleteDomainGovernance``UpdateOrganization``CreateChildTenancy ``DeleteSubscriptionMapping ``DeleteOrganizationTenancy``RestoreOrganizationTenancy``CreateSubscriptionMapping``CreateGovernanceRule``DeleteGovernanceRule` | none  
[organizations-link](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_LINK_INSPECT | `ListLinks` | none  
READ, USE | _INSPECT_ + ORGANIZATIONS_LINK_READ | _INSPECT_ + `GetLink` | none  
MANAGE | _USE_ + ORGANIZATIONS_LINK_PARENT_DELETEORGANIZATIONS_LINK_CHILD_DELETE | _USE_ + `DeleteLink` | none  
[organizations-recipient-invitation](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_RECIPIENT_INVITATION_INSPECT | `ListRecipientInvitations` | none  
READ | _INSPECT_ + ORGANIZATIONS_RECIPIENT_INVITATION_READ | _INSPECT_ + `GetRecipientInvitation` | none  
USE, MANAGE | _READ_ + ORGANIZATIONS_RECIPIENT_INVITATION_UPDATE | _READ_ + `AcceptRecipientInvitation``IgnoreRecipientInvitation``UpdateRecipientInvitation` | none  
[organizations-sender-invitation](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_SENDER_INVITATION_INSPECT | `ListRecipientInvitations` | none  
READ | _INSPECT_ + ORGANIZATIONS_SENDER_INVITATION_READ | _INSPECT_ + `GetSenderInvitation` | none  
USE | _READ_ + ORGANIZATIONS_SENDER_INVITATION_UPDATE | _READ_ + `UpdateSenderInvitation``CancelSenderInvitation` | none  
MANAGE | _USE_ + ORGANIZATIONS_SENDER_INVITATION_CREATE | _USE_ + `CreateSenderInvitation` | none  
[organizations-invitation](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_RECIPIENT_INVITATION_INSPECTORGANIZATIONS_SENDER_INVITATION_INSPECT | `ListRecipientInvitations``ListSenderInvitations` | none  
READ | _INSPECT_ + ORGANIZATIONS_RECIPIENT_INVITATION_READORGANIZATIONS_SENDER_INVITATION_READ | _INSPECT_ + `GetRecipientInvitation``GetSenderInvitation` | none  
USE | _READ_ + ORGANIZATIONS_RECIPIENT_INVITATION_UPDATEORGANIZATIONS_SENDER_INVITATION_UPDATE | _READ_ + `AcceptRecipientInvitation``UpdateRecipientInvitation``UpdateSenderInvitation``CancelSenderInvitation` | none  
MANAGE | _USE_ + ORGANIZATIONS_SENDER_INVITATION_CREATE | _USE_ + `CreateSenderInvitation` | none  
[organizations-domain](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_DOMAIN_INSPECT | `ListDomains` | none  
READ | _INSPECT_ + ORGANIZATIONS_DOMAIN_READ | _INSPECT_ + `GetDomain` | none  
USE | _READ_ + ORGANIZATIONS_DOMAIN_UPDATE | _READ_ + `UpdateDomain` | none  
MANAGE | _USE_ + ORGANIZATIONS_DOMAIN_CREATEORGANIZATIONS_DOMAIN_DELETE | _USE_ + `CreateDomain``DeleteDomain` | none  
[organizations-domain-governance](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_DOMAIN_GOVERNANCE_INSPECT | `ListDomainGovernances` | none  
READ | _INSPECT_ + ORGANIZATIONS_DOMAIN_GOVERNANCE_READ | _INSPECT_ + `GetDomainGovernance` | none  
USE | _READ_ + ORGANIZATIONS_DOMAIN_GOVERNANCE_UPDATE | _READ_ + `UpdateDomainGovernance` | none  
MANAGE | _USE_ + ORGANIZATIONS_DOMAIN_GOVERNANCE_CREATEORGANIZATIONS_DOMAIN_GOVERNANCE_DELETE | _USE_ + `CreateDomainGovernance``DeleteDomainGovernance` | none  
[organizations-entity](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_ENTITY_INSPECT | `ListOrganizations ` | none  
READ | _INSPECT_ + ORGANIZATIONS_ENTITY_READ | _INSPECT_ + `GetOrganization` | none  
USE | _READ_ + ORGANIZATIONS_ENTITY_UPDATE | _READ_ + `UpdateOrganization` | none  
MANAGE | - | - | none  
[organizations-tenancy](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_TENANCY_INSPECT | `ListOrganizationTenancies ` | none  
READ, USE | _INSPECT_ + ORGANIZATIONS_TENANCY_READ | _INSPECT_ + `GetOrganizationTenancy` | none  
MANAGE | _USE_ + ORGANIZATIONS_TENANCY_CREATEORGANIZATIONS_TENANCY_DELETEORGANIZATIONS_TENANCY_RESTORE | _USE_ + `CreateChildTenancy``DeleteOrganizationTenancy``RestoreOrganizationTenancy` | none  
[organizations-order](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | - | - | none  
READ | - | - | none  
USE | - | - | none  
MANAGE | ORGANIZATIONS_ORDER_ACTIVATE | `ActivateOrder` | none  
[organizations-subscription](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_SUBSCRIPTION_INSPECT | `ListSubscriptions` | none  
READ | _INSPECT_ + ORGANIZATIONS_SUBSCRIPTION_READ | _INSPECT_ + `GetSubscription` | none  
USE, MANAGE | _USE_ + ORGANIZATIONS_SUBSCRIPTION_ASSIGNORGANIZATIONS_SUBSCRIPTION_DELETEORGANIZATIONS_SUBSCRIPTION_MAPPING_CREATE | _USE_ + `AssignTenancySubscription ``AssignDefaultSubscription ``CreateSubscriptionMapping` | none  
[organizations-subscription-mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_SUBSCRIPTION_MAPPING_INSPECT | `ListSubscriptionMappings ` | none  
READ | _INSPECT_ + ORGANIZATIONS_SUBSCRIPTION_MAPPING_READ | _INSPECT_ + `GetSubscriptionMapping` | none  
USE, MANAGE | _USE_ + ORGANIZATIONS_SUBSCRIPTION_MAPPING_DELETEORGANIZATIONS_SUBSCRIPTION_MAPPING_CREATE | _USE_ + `DeleteSubscriptionMapping ``CreateSubscriptionMapping` | none  
[organizations-assigned-subscription](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_ASSIGNED_SUBSCRIPTION_INSPECT | `ListAssignedSubscriptions` | none  
READ | _INSPECT_ + ORGANIZATIONS_ASSIGNED_SUBSCRIPTION_READ | _INSPECT_ + `GetAssignedSubscription` | none  
USE | - | - | none  
MANAGE | - | - | none  
[organizations-subscription-region](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | ORGANIZATIONS_SUBSCRIPTION_REGION_INSPECT | `ListAvailableRegions` | none  
READ | - | - | none  
USE | -  | - | none  
MANAGE | -  | - | none  
[organizations-governance-rules](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | GOVERNANCE_RULE_INSPECT | `ListGovernanceRules``ListOrganizations ``ListOrganizationTenancies ` | none  
READ | _INSPECT_ + GOVERNANCE_RULE_READ | _INSPECT_ + `GetGovernanceRule``ListTenancyAttachments``GetTenancyAttachment` | none  
USE | _READ_ + GOVERNANCE_RULE_UPDATEGOVERNANCE_RULE_RETRY | _READ_ + `GetGovernanceRule``DeleteInclusionCriterion``RetryGovernanceRule``RetryTenancyAttachment` | none  
MANAGE | _USE_ + GOVERNANCE_RULE_CREATEGOVERNANCE_RULE_DELETE | _USE_ + `CreateGovernanceRule``DeleteGovernanceRule` | none  
[organizations-enforced-governance-rules](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/organizationsreference.htm)
Verbs | Permissions | APIs Fully Covered | APIs Partially Covered  
---|---|---|---  
INSPECT | GOVERNANCE_RULE_ENFORCED_INSPECT | `ListEnforcedGovernanceRules` `ListOrganizations ``ListOrganizationTenancies ` | none  
READ | _INSPECT_ + GOVERNANCE_RULE_ENFORCED_READ | _INSPECT_ + `GetEnforcedGovernanceRule` | none  
USE | - | - | none  
MANAGE | -  | - | none  
## Permissions Required for Each API Operation 🔗 
The following table lists the API operations in a logical order, grouped by resource type. For information about permissions, see [Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Permissi).
API Operation | Permissions Required to Use the Operation  
---|---  
GetLink | ORGANIZATIONS_LINK_READ  
ListLinks | ORGANIZATIONS_LINK_INSPECT  
DeleteLink | ORGANIZATIONS_LINK_CHILD_DELETEORGANIZATIONS_LINK_PARENT_DELETE  
GetRecipientInvitation | ORGANIZATIONS_RECIPIENT_INVITATION_READ  
AcceptRecipientInvitation | ORGANIZATIONS_RECIPIENT_INVITATION_UPDATE  
IgnoreRecipientInvitation | ORGANIZATIONS_RECIPIENT_INVITATION_UPDATE  
UpdateRecipientInvitation | ORGANIZATIONS_RECIPIENT_INVITATION_UPDATE  
ListRecipientInvitations | ORGANIZATIONS_RECIPIENT_INVITATION_INSPECT  
CreateSenderInvitation | ORGANIZATIONS_SENDER_INVITATION_CREATE  
GetSenderInvitation | ORGANIZATIONS_SENDER_INVITATION_READ  
ListSenderInvitations | ORGANIZATIONS_SENDER_INVITATION_INSPECT  
CancelSenderInvitation | ORGANIZATIONS_SENDER_INVITATION_UPDATE  
UpdateSenderInvitation | ORGANIZATIONS_SENDER_INVITATION_UPDATE  
UpdateSenderInvitation | ORGANIZATIONS_DOMAIN_READ  
ListDomains | ORGANIZATIONS_DOMAIN_INSPECT  
CreateDomain | ORGANIZATIONS_DOMAIN_CREATE  
UpdateDomain | ORGANIZATIONS_DOMAIN_UPDATE  
DeleteDomain | ORGANIZATIONS_DOMAIN_DELETE  
GetDomainGovernance | ORGANIZATIONS_DOMAIN_GOVERNANCE_READ  
ListDomainGovernances | ORGANIZATIONS_DOMAIN_GOVERNANCE_INSPECT  
CreateDomainGovernance | ORGANIZATIONS_DOMAIN_GOVERNANCE_CREATE  
UpdateDomainGovernance | ORGANIZATIONS_DOMAIN_GOVERNANCE_UPDATE  
DeleteDomainGovernance | ORGANIZATIONS_DOMAIN_GOVERNANCE_DELETE  
GetOrganization  | ORGANIZATIONS_ENTITY_READ  
ListOrganizations  | ORGANIZATIONS_ENTITY_INSPECT  
UpdateOrganization | ORGANIZATIONS_ENTITY_UPDATE  
GetOrganizationTenancy | ORGANIZATIONS_TENANCY_READ  
ListOrganizationTenancies  | ORGANIZATIONS_TENANCY_INSPECT  
approveForTransfer/unapproveForTransfer  | ORGANIZATIONS_TENANCY_TRANSFER_APPROVAL_UPDATE  
CreateChildTenancy  | ORGANIZATIONS_TENANCY_CREATE**Note** : When the **subscriptionId** attribute is specified for a created child tenancy, then ORGANIZATIONS_SUBSCRIPTION_MAPPING_CREATE is also required. For more information see [CreateChildTenancyDetails Reference](https://docs.oracle.com/iaas/api/#/en/organizations/latest/datatypes/CreateChildTenancyDetails).  
DeleteOrganizationTenancy | ORGANIZATIONS_TENANCY_DELETE  
RestoreOrganizationTenancy | ORGANIZATIONS_TENANCY_RESTORE  
ActivateOrder  | ORGANIZATIONS_ORDER_ACTIVATE  
ListSubscriptions  | ORGANIZATIONS_SUBSCRIPTION_INSPECT  
ListSubscriptionMappings  | ORGANIZATIONS_SUBSCRIPTION_MAPPING_INSPECT  
GetSubscription  | ORGANIZATIONS_SUBSCRIPTION_READ  
GetSubscriptionMapping  | ORGANIZATIONS_SUBSCRIPTION_MAPPING_READ  
AssignTenancySubscription  | ORGANIZATIONS_SUBSCRIPTION_ASSIGN  
AssignDefaultSubscription  | ORGANIZATIONS_SUBSCRIPTION_ASSIGN  
DeleteSubscriptionMapping  | ORGANIZATIONS_SUBSCRIPTION_MAPPING_DELETE  
CreateSubscriptionMapping | ORGANIZATIONS_SUBSCRIPTION_MAPPING_CREATE  
ListAssignedSubscriptions | ORGANIZATIONS_ASSIGNED_SUBSCRIPTION_INSPECT  
GetAssignedSubscription | ORGANIZATIONS_ASSIGNED_SUBSCRIPTION_READ  
ListAvailableRegions | ORGANIZATIONS_SUBSCRIPTION_REGION_INSPECT  
ListGovernanceRules | GOVERNANCE_RULE_INSPECT  
GetGovernanceRule | GOVERNANCE_RULE_READ  
CreateGovernanceRule | GOVERNANCE_RULE_CREATE  
UpdateGovernanceRule | GOVERNANCE_RULE_UPDATE  
DeleteGovernanceRule | GOVERNANCE_RULE_DELETE  
RetryGovernanceRule | GOVERNANCE_RULE_RETRY  
CreateInclusionCriterion | GOVERNANCE_RULE_UPDATE  
DeleteInclusionCriterion | GOVERNANCE_RULE_UPDATE  
ListTenancyAttachments | GOVERNANCE_RULE_READ  
GetTenancyAttachment | GOVERNANCE_RULE_READ  
RetryTenancyAttachment | GOVERNANCE_RULE_RETRY  
ListEnforcedGovernanceRules | GOVERNANCE_RULE_ENFORCED_INSPECT  
GetEnforcedGovernanceRule | GOVERNANCE_RULE_ENFORCED_READ  
Was this article helpful?
YesNo

