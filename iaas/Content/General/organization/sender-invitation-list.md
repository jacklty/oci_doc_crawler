Updated 2025-02-11
# Listing Sender Invitations
View a list of invitations sent to tenancies inviting them to join an organization.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/General/organization/sender-invitation-list.htm)


  * You can view sender invitations from both the parent tenancy that sent the invitation and the recipient tenancy that's been invited to join the organization as a child tenancy.
To view sent invitations, open the navigation menu and select **Governance & Administration**. Under **Organization Management** , select **Invitations**.
The **Invitations** list page displays the following information:
    * **Invitation Name** : Select the invitation name to go to the invitation details page.
    * **Status** : Displays the invitation status. For example, the status is **Active** when the invitation is received but not yet accepted, and **Pending** for an invitation that has been sent but not yet accepted.
Following are the possible status states for a sender and recipient invitation:
      * Active
      * Pending
      * Canceled
      * Accepted
      * Expired
      * Failed
    * **Type** : Displays **Sent invitation** for invitations to join an organization. **Sent request** or **Received request** indicates that a request to join [organization governance](https://docs.oracle.com/en-us/iaas/Content/General/organization/add-governance.htm#add_governance "Use governance rules to configure and attach controls to tenancies in your organization. When a governance rule is attached to a tenancy, a corresponding resource is created and then locked in the target tenancy.") was sent or received.
    * **Created** : The UTC creation date and time of the invitation.
  * Use the [oci organizations sender-invitation list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/organizations/sender-invitation/list.html) command and required parameters to view the list of sender tenancy invitations:
Command
CopyTry It
```
oci organizations sender-invitation list --compartment-id, -c [text] [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListSenderInvitations](https://docs.oracle.com/iaas/api/#/en/organizations/latest/SenderInvitation/ListSenderInvitations) operation to view the list of sender tenancy invitations.


Was this article helpful?
YesNo

