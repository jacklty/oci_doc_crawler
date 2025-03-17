Updated 2025-02-13
# Accepting an Invitation to Join an Organization
Accept an invitation from a parent tenancy to join an organization.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-accept.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-accept.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-accept.htm)


  * To accept an invitation, follow these steps:
    1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Invitations**.
On the **Invitations** page, the invitation from the tenancy that sent the invite is displayed in the **Invitations** page list. For more information on the **Invitations** page fields, see [Listing Sender Invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm#sender_invitation_list "View a list of invitations sent to tenancies inviting them to join an organization.") for a sender, and [Listing Recipient Invitations](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-list.htm#recipient_invitation_list "View a list of invitations that a tenancy has received to join an organization.") for a recipient.
    2. On the **Invitations** page, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the received invitation and select **Accept Invitation**. An **Accept Invitation** confirmation message is displayed, indicating that you're about to accept an invitation from the tenancy.
By joining the organization, the parent tenancy can manage cost management and reporting (oversee spending), governance rules (create and attach governance rules to the tenancy), and subscription mapping (map and unmap subscriptions to the tenancy).
See the final step of the [Inviting a Tenancy to Join an Organization](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-create.htm#sender_invitation_create "Create an invitation to join an organization and asynchronously send the invitation to the recipient.") Console topic for more information on the invitation acceptance process.
  * Use the [oci organizations recipient-invitation accept](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/recipient-invitation/accept.html) command and required parameters to accept a recipient tenancy:
Command
CopyTry It
```
oci organizations recipient-invitation accept --recipient-invitation-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [AcceptRecipientInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/RecipientInvitation/AcceptRecipientInvitation) operation to accept a recipient tenancy.


Was this article helpful?
YesNo

