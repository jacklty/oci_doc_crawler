Updated 2025-02-11
# Child Tenancy Management
As the parent tenancy, you can create child tenancies or invite existing tenancies to your organization.
Child tenancies that you create consume from your organization's default subscription. If you want a new child tenancy to consume from another subscription, you can remap the created tenancy to another subscription on the **Subscription Mapping** page.
You can also attach [governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm#add_governance "Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy.") to the new child tenancy during creation, or you can come back later and attach rules. To attach governance rules during child tenancy creation, you can create the governance rules first on the **Governance Rules** page so that they're available for selection during child tenancy creation.
Created child tenancies inherit the current default limits of the parent tenancy. Child tenancies receive their own set of limits, which aren't shared with other tenancies.
**Note** Free Tier or Trial tenancies can't add new child tenancies, or be invited to be part of an organization, unless they're converted to paid first. For more information about upgrading, see [Account Upgrade Overview](https://docs.oracle.com/iaas/Content/Billing/Tasks/changingpaymentmethod.htm#Upgrade).
The following table describes the child tenancy creation and invitation actions that you can perform based on pricing model:
Pricing Model | Can Create Tenancies | Can Invite Tenancies | Can Be Invited  
---|---|---|---  
Pay As You Go | No | Yes | Yes  
Annual Commit | Yes | Yes | Yes  
Funded Allocation | Yes | Yes | Yes  
Custom  | Yes | Yes | Yes  
Trial/Free Tier | No | No | No  
For step-by-step instructions, see [Creating a Child Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-create.htm#child_tenancy_create "Create a child tenancy in your organization.").
Was this article helpful?
YesNo

