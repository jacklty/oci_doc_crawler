Updated 2025-02-11
# Getting a Recipient Invitation's Details
Get information about an invitation sent to a tenancy inviting it to join an organization.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-get.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-get.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-get.htm)


  * You can view recipient invitation details from both the parent tenancy that sent the invitation and the recipient tenancy that's been invited to join the organization as a child tenancy.
    1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Invitations**.
    2. On the **Invitations** list page, select the invitation that you want to work with.
The invitation details page displays the invitation status, along with the following details on the **Invitation Information** tab:
       * **Sent from tenancy OCID**
       * **Type** : This field shows both _invitations_ (a parent tenancy wants another tenancy to become a child tenancy in the organization), or _requests_ (to use [governance rules](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm#add_governance "Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy.")). For invitations received from a parent tenancy inviting a child tenancy, **Received invitation** is displayed.
       * **Status**
       * **Sent date**
       * **Request** (governance requests only)
       * **Cost Management** (tenancy invitations only)
       * **Organization governance** (tenancy invitations only)
       * **Subscription mapping** (tenancy invitations only)
You can also view tagging information on the **Tags** tab. See [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags).
  * Use the [oci organizations recipient-invitation get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/recipient-invitation/get.html) command and required parameters to get the details of a recipient child tenancy invitation:
Command
CopyTry It
```
oci organizations recipient-invitation get --recipient-invitation-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetRecipientInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/RecipientInvitation/GetRecipientInvitation) operation to get the details of a recipient child tenancy invitation.


Was this article helpful?
YesNo

