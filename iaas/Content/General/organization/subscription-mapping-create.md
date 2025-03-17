Updated 2025-02-11
# Mapping Subscriptions to Tenancies
Map tenancies to subscriptions within Organization Management.
An organization can have _multiple_ subscriptions, which are managed by the parent tenancy. For example, an organization always starts out with only a single subscription (subscription A), but a child tenancy that later joins the organization can bring its own subscription (subscription B). The parent tenancy can then use **Subscription Mapping** to map subscription B to other tenancies in the organization. As a result, an organization's subscriptions can be mapped to any tenancy in the organization.
Tenancies mapped to a subscription consume from the subscription's credits (for Universal Credits Commitment subscriptions) and use its **rate card**. By remapping a tenancy to a subscription, the tenancy's usage applies to the terms and conditions of the subscription, including its rate card, credit consumption, and other agreements within the subscription's contract.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-create.htm)


  * To map subscriptions to tenancies, follow these steps: 
    1. From the parent tenancy, open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Subscription Mapping**.
    2. On the **Subscription Mapping** list page, select the subscription that you want to map.
    3. Under **Mapped tenancies** , select **Map subscription**.
    4. In the **Map subscription** panel, add other tenancies to be mapped to this subscription. When you map the selected subscription to a tenancy, the tenancy stops consuming from the previously mapped subscription.
    5. Select **Map subscription**.
  * Use the [oci organizations subscription-mapping create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/subscription-mapping/create.html) command and required parameters to assign the tenancy record identified by the compartment ID to the given subscription ID:
Command
CopyTry It
```
oci organizations subscription-mapping create --compartment-id, -c [text] --subscription-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateSubscriptionMapping](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SubscriptionMapping/CreateSubscriptionMapping) operation to assign the tenancy record identified by the compartment ID to the given subscription ID.


Was this article helpful?
YesNo

