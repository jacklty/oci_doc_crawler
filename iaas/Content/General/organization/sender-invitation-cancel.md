Updated 2025-02-11
# Canceling a Sender Invitation
Cancel an invitation sent to a tenancy to join an organization.
A parent tenancy that sends an invitation to another tenancy to join the organization can decide to later revoke the invitation.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-cancel.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-cancel.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-cancel.htm)


  *     1. Sign in to the parent tenancy as a user who has permissions to manage invitations and subscription sharing.
    2. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Invitations**.
    3. On the **Invitations** list page, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the invitation you want to revoke and select **Revoke Invitation**.
    4. Confirm the revocation.
On the **Invitations** list page, the invitation's status changes to **Canceled**.
  * Use the [oci organizations sender-invitation cancel](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/sender-invitation/cancel.html) command and required parameters to cancel a sender tenancy invitation:
Command
CopyTry It
```
oci organizations sender-invitation cancel --sender-invitation-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CancelSenderInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SenderInvitation/CancelSenderInvitation) operation to cancel a sender tenancy invitation.


Was this article helpful?
YesNo

