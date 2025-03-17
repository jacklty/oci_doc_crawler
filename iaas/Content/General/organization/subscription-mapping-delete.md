Updated 2025-02-11
# Unmapping a Subscription from a Tenancy
Unmap a subscription from a tenancy to revert the tenancy back to the default Oracle Universal Credits subscription. 
**Note** This operation is valid only from the parent tenancy for a second, non-default Oracle Universal Credits subscription. The default Oracle Universal Credits subscription can't be unmapped. Unmapping a subscription from a tenancy reverts the tenancy back to the default Oracle Universal Credits subscription. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-delete.htm)


  * To unmap a subscription, follow these steps:
    1. From the parent tenancy, open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Subscription Mapping**.
    2. On the **Subscription Mapping** list page, select the subscription that you want to unmap.
    3. On the subscription mapping details page, under **Mapped tenancies** , select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the tenancy whose subscription that you want to unmap, and select **Unmap subscription from tenancy**.
    4. Confirm the action. A notification is displayed that the unmapping operation was successful.
  * Use the [oci organizations subscription-mapping delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/subscription-mapping/delete.html) command and required parameters to unmap a subscription by the subscription mapping ID:
Command
CopyTry It
```
oci organizations subscription-mapping delete --subscription-mapping-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteSubscriptionMapping](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SubscriptionMapping/DeleteSubscriptionMapping) operation to unmap a subscription by the subscription mapping ID.


Was this article helpful?
YesNo

