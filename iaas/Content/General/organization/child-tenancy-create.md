Updated 2025-02-11
# Creating a Child Tenancy
Create a child tenancy in your organization.
To create a child tenancy, you provide the necessary information, such as tenancy name and designated administrator email. Then, sign-in instructions are provided in an email notification to the child tenancy administrator. The created (child) tenancy automatically consumes from the default subscription of the organization, so all usage is charged based on the **rate card** of the subscription. The parent tenancy is also responsible for the child tenancy's usage.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/child-tenancy-create.htm)


  *     1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Tenancies**.
    2. On the **Tenancies** list page, select **Create new tenancy.**
    3. In the **Create new tenancy** panel's **Tenancy details** step, enter a name for the child tenancy in **Tenancy name**.
The tenancy name must be unique and all lowercase without any special characters. Avoid entering confidential information.
    4. From **Home region** , select a region. The home region is one of the parent's subscribed regions.
    5. In **Administrator email** and **Confirm Email** , enter and confirm the email address of the tenancy administrator.
    6. In the **Subscription mapping** step, you can select the subscription that you want to be associated with the new created child tenancy.
The created child tenancy consumes from your organization's default subscription, unless you select a different subscription in this step. Only Oracle Universal Credits subscriptions appear as alternate subscription selections.
    7. Select **Next**. 
    8. In the **Governance rules** step, select [governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm#add_governance "Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy.") to attach to the tenancy, or skip this step and attach them later. You can [attach](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-attachruletenancy.htm#add_governance_attachruletenancy "Attach an existing governance rule to one or more tenancies.") or [detach](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance-detachrule.htm#add_governance_detachrule "Detach a governance rule from one or more target tenancies in an organization.") rules later, or [opt the tenancy out](https://docs.oracle.com/en-us/iaas/Content/General/organization/remove-governance.htm#remove_governance "Start a work request to opt a tenancy out of governance rules.") of organization governance in the future.
If you want to select governance rules now, select them from the table. You can filter the table by the rule type (tag, allowed regions, quotas), or the targeted tenancy. You can expand any rule entry and view its details.
Otherwise, if no governance rules are selected, a message indicates that you're choosing to skip attaching governance rules for now.
    9. Select **Next**.
    10. In the **Review summary** step, verify the child tenancy settings that you specified.
    11. Select **Create tenancy**.
A notification is displayed, indicating that you successfully requested to create a child tenancy. If the request completes successfully, then your authentication credentials are sent by email momentarily.
The child tenancy administrator receives instructions to activate the tenancy, and to set up a password and [MFA](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security_topic-IAM_MFA.htm).
  * Use the [oci organizations child-tenancy create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/child-tenancy/create.html) command and required parameters to create a child tenancy:
Command
CopyTry It
```
oci organizations child-tenancy create --admin-email [text] --compartment-id, -c [text] --home-region [text] --tenancy-name [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateChildTenancy](https://docs.oracle.com/iaas/api/#/en/organizations/latest/methods/CreateChildTenancy) operation to create a child tenancy.
**Note** When the **subscriptionId** attribute is specified for a created child tenancy, then more permissions are required. For more information see [CreateChildTenancyDetails Reference](https://docs.oracle.com/iaas/api/#/en/organizations/latest/datatypes/CreateChildTenancyDetails) and [Permissions Required for Each API Operation](https://docs.oracle.com/iaas/Content/Identity/Reference/organizationsreference.htm#organizationsreference_permissions_required_each_api_operation).


Was this article helpful?
YesNo

