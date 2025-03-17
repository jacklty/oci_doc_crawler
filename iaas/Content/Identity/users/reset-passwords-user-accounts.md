Updated 2025-02-28
# Resetting a User Password
Reset the password for a single account, for multiple accounts, or for all accounts in an OCI IAM identity domain.
When you request a password change, a notification is sent to the user or users so that they can provide a new password for the account. The user clicks the link in the notification to open a form where they provide a new password. The new password must conform to the password policy as [defined by an administrator](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/Managing-Password-Policies.htm#topic_g2w_wms_l4b "Create and manage group-based password policies for an identity domain in IAM.").
You can't reset the passwords for deactivated user accounts. To activate one or more deactivated accounts, search for accounts with a status of _Inactive_. Then, select individual accounts to activate, or select them all.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**.
  3. Select the checkbox for each user account for which you want to reset the password.
**Tip** To reset the passwords for all user accounts, don't select any checkboxes, and skip to the next step.
  4. Select **More actions** , and then perform one of the following actions:
     * If you selected one or more user accounts, select **Reset password**. Then, in the Reset password dialog box, select **Reset password**.
     * If you want to reset the passwords for all accounts, select **Reset all passwords**. Then, in the Reset all passwords dialog box, select **Reset all passwords**.


**Note** For information about managing users and passwords on Oracle Autonomous Database Serverless, see the section on creating users in _[Using Oracle Autonomous Database Serverless](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/manage-users-create.html#GUID-B5846072-995B-4B81-BDCB-AF530BC42847)_.
Was this article helpful?
YesNo

