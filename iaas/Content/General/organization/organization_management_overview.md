Updated 2024-10-30
# Overview
Use Organization Management to centrally manage many tenancies, invite and create child tenancies, view and map subscriptions, and create and attach governance rules to tenancies in an organization.
With Organization Management, you can add tenancies to an organization, and have those tenancies consume from the primary funded subscription. You can create an isolated tenancy to build workloads, without needing to book a new order. 
Two types of tenancies are involved when mapping and using a subscription in Organization Management:
  * **Parent** : Tenancy that's associated with the primary funded subscription. 
  * **Child** : Tenancies that join an organization, whereby the parent manages the child's cost and governance. Child tenancies can either be created as entirely new tenancies, or, existing tenancies can be invited to join the same organization and to change your default subscription.


An organization can have _multiple_ child tenancies, which are managed by the parent tenancy. The parent tenancy can use [Subscription Mapping](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm#subscription_mapping_management "Learn about subscription mapping management.") to assign subscriptions to any child tenancy in the organization.
Benefits of Organization Management include the following:
  * Share a single commitment to help avoid cost overages and [enable multitenancy cost management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_cost_reporting.htm#organization_management_cost_reporting "You can use the Oracle billing and cost reporting features to centrally manage the cost and usage information across all tenancies in your organization."). You can analyze, report, and monitor across all linked tenancies in an organization. The parent tenancy can analyze and report across each of its tenancies through [Cost Analysis](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm) and [Cost and usage reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm), and you can receive alerts through [Budgets](https://docs.oracle.com/iaas/Content/Billing/Concepts/budgetsoverview.htm).
  * Customers with strict data isolation requirements can use a multitenancy strategy to isolate data and restrict resources across their tenancies.
  * Use [governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm#add_governance "Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy.") to enforce and govern resources on specific child tenancies, or the entire organization.


**Important** SaaS subscription services can be provisioned in the tenancy where the SaaS subscription was activated, which also includes child tenancies.
The remainder of this topic provides an overview of how to use Organization Management to create child tenancies, invite existing tenancies, view and revoke invitations, and how to remap subscriptions to tenancies. Cost reporting features are also described, which you can use to centrally manage cost and usage information across all tenancies in an organization. Using these features you can better manage a multitenancy environment.
To learn more about Organization Management, see the following:
  * [Planning Considerations](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_planning.htm#organization_management_planning "Before you add more tenancies, evaluate your needs to ensure that a multi-tenancy approach is best for your workloads. The main reason to have multiple tenancies is for strong isolation, to help isolating workloads.")
  * [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_required_iam_policy.htm#organization_management_required_iam_policy "Learn about Organization Management required IAM policies.")
  * [Assigned Subscription Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/assigned-subscription-management.htm#assigned_subscription_management "Learn about assigned subscription management.")
  * [Child Tenancy Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-management.htm#child_tenancy_management "As the parent tenancy, you can create child tenancies or invite existing tenancies to your organization.")
  * [Link Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/link-management.htm#governance_management "Learn about link management.")
  * [Order Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/order-management.htm#order_management "Learn about order management.")
  * [Organization Entity Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-entitymanagement.htm#organization_entitymanagement "Learn about organization entity management.")
  * [Organization Tenancy Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-tenancy-management.htm#organization_tenancy_management "Learn about organization tenancy management.")
  * [Sender Invitation Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-management.htm#sender_invitation_management "Learn about sender invitation management.")
  * [Recipient Invitation Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-management.htm#recipient_invitation_management "Learn about recipient invitation management.")
  * [Subscription Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-management.htm#subscription_management "Learn about subscription management.")
  * [Subscription Line Item Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-lineitem-management.htm#subscription_lineitem_management "Learn about subscription line item management.")
  * [Subscription Mapping Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm#subscription_mapping_management "Learn about subscription mapping management.")
  * [Work Request Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-management.htm#workrequest_management "Learn about work request, work request error, and work request log management.")
  * [Cost Reporting Integration](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization_cost_reporting.htm#organization_management_cost_reporting "You can use the Oracle billing and cost reporting features to centrally manage the cost and usage information across all tenancies in your organization.")
  * [Support](https://docs.oracle.com/en-us/iaas/Content/General/organization/organizations_support.htm#organization_management_support "Depending on how you created your tenancy, you have separate CSI \(Customer Support Identifier\) numbers, and support accounts for each tenancy. Created child tenancies inherit the parent subscription CSI.")
  * [Troubleshooting Organization Management](https://docs.oracle.com/en-us/iaas/Content/General/organization/organization-troubleshooting.htm#organization_troubleshooting "Use troubleshooting information to identify and address common issues that can occur while working with Organization Management.")


Was this article helpful?
YesNo

