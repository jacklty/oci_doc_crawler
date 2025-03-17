Updated 2025-02-13
# Deleting Links to Invited Child Tenancies
Use the link termination workflow to remove an invited child tenancy.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/link-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/link-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/link-delete.htm)


  * As a parent tenancy, you can remove an invited child tenancy from the organization. Only invited child tenancies can be removed.
Removing an invited child tenancy unlinks the tenancy from the organization so that the parent doesn't have cost or governance access. For _created_ child tenancies, you can transfer the tenancy to another organization by using the CLI. For more information about using the [oci organizations organization-tenancy approve-organization-tenancy-for-transfer](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/organization-tenancy/approve-organization-tenancy-for-transfer.html) and [oci organizations organization-tenancy unapprove-organization-tenancy-for-transfer](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/organization-tenancy/unapprove-organization-tenancy-for-transfer.html) commands, see [Approving a Created Child Tenancy for Transfer](https://docs.oracle.com/en-us/iaas/Content/General/organization/approve-createdchildtenancy-for-transfer.htm#approve_createdchildtenancy_for_transfer "Approve an organization's created child tenancy for transfer.").
By removing the invited child tenancy, the parent tenancy can no longer manage it. The parent tenancy can't view the invited child tenancy's future cost and usage information, nor manage its subscription mapping. If you want the child tenancy to consume from another subscription that's within the organization, you don't need to remove the tenancy. Instead, you can use [subscription mapping](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-management.htm#subscription_mapping_management "Learn about subscription mapping management.") to map the tenancy to another subscription.
To remove an _invited_ child tenancy, you first need to [remove it from organization governance](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm#remove_governance "Start a work request to opt a tenancy out of governance rules."), use the **Subscription Mapping** page to [assign the tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-create.htm#subscription_mapping_create "Map tenancies to subscriptions within Organization Management.") back to its original subscription, and then remove the tenancy from the **Tenancies** page after the tenancy has been remapped to its original subscription.
To remove an invited child tenancy, follow these steps:
    1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Tenancies**.
    2. On the **Tenancies** list page under **Tenancy name** , select the invited tenancy that you want to remove.
    3. On the details page, remove the tenancy from [organization governance](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm#add_governance "Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy.") by selecting **Remove from organization governance** and then confirming the removal. For more information about removing governance rules, see [Removing Governance from Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm#remove_governance "Start a work request to opt a tenancy out of governance rules."). For information about opting into and out of organization governance, see [Opting In Tenancies to Use Governance Rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-optinuserules.htm#add_governance_optinuserules "Certain types of tenancies that are already part of the organization can opt in to use governance rules.") and [Removing Governance from Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm#remove_governance "Start a work request to opt a tenancy out of governance rules.").
    4. Back on the **Tenancies** list page, under **Organization Management** on the left side of the page, select **Subscription Mapping**.
    5. On the **Subscription Mapping** list page, select the child tenancy's original Universal Credits subscription in the **Subscription ID** column.
    6. On the subscription mapping details page, under **Mapped Tenancies** , select **Map subscription**.
    7. In the **Map subscription** panel, select **Map subscription** and select the child tenancy to map back to this subscription. Select **Map subscription**. A notification message is displayed informing you that you successfully mapped the subscription to the tenancy. The tenancy then appears under **Mapped Tenancies** on the subscription mapping details page.
**Note** If other tenancies are mapped to this subscription, you must unmap any other tenancies from the subscription. See [Unmapping a Subscription from a Tenancy](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-delete.htm#subscription_mapping_delete "Unmap a subscription from a tenancy to revert the tenancy back to the default Oracle Universal Credits subscription.").
    8. Back on the **Subscription Mapping** list page, under **Organization Management** on the left side of the page, select **Tenancies**.
    9. On the **Tenancies** list page, open the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the tenancy that you want to remove and select **Remove Tenancy**.
Confirm that you do want to remove the tenancy. 
Any subscriptions mapped to this tenancy move with the tenancy and are no longer associated with your organization. You might also need to reload the **Tenancies** page to verify that the invited tenancy has been removed.
If you see the following error message in the **Remove Tenancy** dialog box, it means that you haven't yet mapped the child tenancy back to its own Oracle Universal Credits subscription:
"Child isn't consuming from its own UCM subscription, ocid1.tenancy.oc1..<unique_ID>"
The child tenancy is removed from the organization with its original subscription. Because you mapped the child tenancy back to its original subscription, the tenancy now consumes from its own subscription, and is responsible for paying for the subscription usage. Furthermore, because the tenancy has been removed from the organization, it now becomes a standalone parent tenancy of its own, which is indicated on the removed tenancy's own **Tenancies** page (under **Tenancy name** , **Parent tenancy** is indicated).
  * Use the [oci organizations link delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/link/delete.html) command and required parameters to start a link termination workflow:
Command
CopyTry It
```
oci organizations link delete --link-id [test] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteLink](https://docs.oracle.com/iaas/api/#/en/organizations/latest/Link/DeleteLink) operation to start a link termination workflow.


Was this article helpful?
YesNo

