Updated 2025-02-18
# Resending an Invitation to a User to Activate their Account
Resend an invitation to a user so that they can activate their user account in an OCI IAM identity domain.
After a user account is created, it must be activated before it can be used. A welcome email is sent to the user, inviting them to activate the account. The invitation is valid for a set time period designated in the [email configuration tab](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-email-settings.htm#configure-email-settings "Configure settings in an identity domain in IAM to send a one-time passcode \(OTP\) to a user's primary email address.") of the two-factor authentication preferences.
If the user account isn't activated after the designated time period, then the identity domain administrator can send another invitation to the user to activate the account.
You can't resend an invitation to a user who has already activated their account, or whose account is inactive. In these cases, **Resend invitation** is unavailable. Reactivating an account will automatically send a new email invitation.
If you select several users and select **Resend invitation** , a confirmation message tells you how many users were sent the invitation and that other selected users are either verified or inactive.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**.
  3. Select the checkbox for each user account to which you want to send an invitation.
**Tip** To send invitations to all user accounts, select the checkbox in the header row of the **Users** table to select all.
  4. Select **More actions** , and then select **Resend invitation**.
  5. In the **Confirmation** window, select **Send invitation**.


Was this article helpful?
YesNo

