Updated 2025-01-28
# Planning Considerations
Before you add more tenancies, evaluate your needs to ensure that a multi-tenancy approach is best for your workloads. The main reason to have multiple tenancies is for strong isolation, to help isolating workloads.
Because managing multiple tenancies can create extra management overhead, ensure that the isolation is worth it. If you don't require a strong level of isolation, you can instead consider using [compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm#Managing_Compartments) to separate workloads. 
By default, each parent and child tenancy comes with:
  * A distinct set of IAM users (which can be federated to another identity system).
  * A distinct set of [IAM policies (permissions)](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
  * A distinct tenancy administrator.
  * Its own [service limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase.").
  * Isolated Virtual Cloud Networks (VCNs).
  * Separate security and governance settings.


A tenancy can be a parent tenancy, and add child tenancies if the tenancy meets the following criteria:
  * The parent has enough organization child tenancy limits. These limits are initially granted based on the subscription the parent was activated with. By default, Oracle Universal Credits annual commit and funded allocation subscriptions are enabled for creating or inviting extra tenancies. Pay As You Go or Trial subscriptions have a limit of 0 child tenancies. If you need a service limit increase, these can be requested through a support ticket. For more information, see [Organizations Service Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#organizations-limits) and [Requesting a Service Limit Increase](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Requesti). 
  * The parent tenancy must be subscribed to the superset of child-subscribed regions.
  * Despite whatever region will be assigned as the home region to a child tenancy, the parent tenancy must be signed in to their home region to create a child tenancy, regardless of how many regions the parent tenancy is already subscribed to. The child tenancy home region selection can be any of multiple (if multiple exist) parent subscribed regions.


Invited tenancies can be a child of an organization if they meet the following criteria:
  * The invited tenancy must have a paid subscription, such as Oracle Universal Credits, Pay As You Go, commit, or funded allocation.
  * The invited tenancy can't be Free Tier or Trial.
  * The invited tenancy must have a home region within the same [realm](https://docs.oracle.com/iaas/Content/GSG/Concepts/concepts-physical.htm#concepts-realm).
  * The invited tenancy must be standalone (it can't be a parent tenancy or be part of another organization).
  * The invited tenancy can be a SaaS standalone tenancy, but only Oracle Universal Credits subscriptions can be [remapped](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-create.htm#subscription_mapping_create "Map tenancies to subscriptions within Organization Management.") with [Subscription Mapping](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm#subscription_mapping_management "Learn about subscription mapping management.").


In regards to sharing a subscription in the organization:
  * Oracle Universal Credits subscriptions can be shared across multiple tenancies, while SaaS subscriptions can't be shared.
  * When a subscription is shared, the tenancy usage is metered against the subscription. Usage costs are computed based on the subscription's **rate card** and currency. Costs are consumed from the subscriptions credits.
  * Subscriptions can be shared regardless of the contractual country.
  * Using [Subscription Mapping](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm#subscription_mapping_management "Learn about subscription mapping management."), you can map a particular subscription to one or multiple tenancies.


Was this article helpful?
YesNo

