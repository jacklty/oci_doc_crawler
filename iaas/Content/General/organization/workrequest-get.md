Updated 2025-02-11
# Getting a Work Request's Details
Get the details of a work request in Organization Management.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/workrequest-get.htm)


  * You can view [work requests](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#Work_Requests "Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.") details for [sender tenancy invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm#sender_invitation_create "Create an invitation to join an organization and asynchronously send the invitation to the recipient."), governance rule opt-in join requests, [governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm#add_governance "Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy."), and [subscription mappings](https://docs.oracle.com/en-us/iaas/Content/General/organization/subscription-mapping-get.htm#subscription_mapping_get "Get the details of a subscription mapping."). 
To view sender (parent) tenancy invitation work requests details:
    1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Tenancies**.
    2. On the **Tenancies** list page, select the tenancy.
    3. On the tenancy details page, select **Work requests**.
    4. Under **Work requests** , select the invitation name to open the work request details page.
To view governance rule opt-in join requests on a child tenancy:
    1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Tenancies**. 
    2. On the **Tenancies** list page, select the tenancy.
    3. On the tenancy details page, select **Work requests**.
Under **Work requests** , select the request under **Operation** to open the work request details page.
To view governance rule attachment and detachment work request details:
    1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Governance Rules**.
    2. On the **Governance rules** list page, select the rule.
    3. On the governance rule details page, under **Tenancies** , select **View work requests** from the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the particular tenancy.
In the **Work requests** panel, the work request operations are listed.
    4. From the **Operation** field, select the work request to open the work request details page.
To view subscription mapping work requests:
    1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Subscription Mapping**.
    2. On the **Subscription Mapping** page, select the subscription name.
    3. On the subscription mapping detail page, select **Work requests**.
    4. From the **Operation** field, select the work request to open the work request details page. 
  * Use the [oci organizations work-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/work-request/get.html) command and required parameters to get the status of the work request with the particular ID:
Command
CopyTry It
```
oci organizations work-request get --work-request-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetWorkRequest](https://docs.oracle.com/iaas/api/#/en/organizations/latest/WorkRequest/GetWorkRequest) operation to get the status of the work request with the particular ID.


Was this article helpful?
YesNo

