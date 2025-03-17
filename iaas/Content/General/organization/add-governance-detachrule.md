Updated 2025-02-11
# Detaching a Governance Rule from a Tenancy
Detach a governance rule from one or more target tenancies in an organization.
**Note** This process only detaches the governance rule. It doesn't opt the tenancy out of organization governance. See [Removing Governance from Tenancies](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm#remove_governance "Start a work request to opt a tenancy out of governance rules.").
  1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Governance Rules**.
  2. On the **Governance Rules** page, select the governance rule that you want to work with.
  3. On the details page, select one or more tenancies under **Tenancies** , and then select **Detach tenancies**.
A confirmation is displayed indicating that the rule will no longer be applied to the targeted tenancy, and the rule's associated resource in the target tenancy will be deleted.
  4. Select **Detach rule**.
The details page reloads and a new work request is started. You can select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the tenancy and select **View work requests** to view the status and progress. After the work request completes, the rule is no longer attached to the tenancy, and the **Rule Status** changes to **Detached**.


Was this article helpful?
YesNo

