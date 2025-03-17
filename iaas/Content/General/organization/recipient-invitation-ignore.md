Updated 2025-02-11
# Declining an Invitation to Join an Organization
Decline an invitation from a parent tenancy to join an organization.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-ignore.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-ignore.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/recipient-invitation-ignore.htm)


  *     1. Open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Invitations**.
    2. On the **Invitations** list page, select the invitation that you want to decline.
    3. On the details page, select **Decline**.
    4. Confirm that you want to decline the invitation.
On the prospective child tenancy, the received invitation details page reloads and updates the status to **Ignored**.
  * Use the [oci organizations recipient-invitation ignore](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/recipient-invitation/ignore.html) command and required parameters to decline a recipient child tenancy invitation:
Command
CopyTry It
```
oci organizations recipient-invitation ignore --recipient-invitation-id [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [IgnoreRecipientInvitation](https://docs.oracle.com/iaas/api/#/en/organizations/latest/RecipientInvitation/IgnoreRecipientInvitation) operation to decline a recipient child tenancy invitation.


Was this article helpful?
YesNo

