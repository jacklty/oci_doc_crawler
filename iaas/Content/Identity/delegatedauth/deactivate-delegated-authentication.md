Updated 2025-01-14
# Deactivating Delegated Authentication
Deactivate delegated authentication for a Microsoft Active Directory (AD) Bridge associated with an AD domain. Users transferred into IAM through this bridge must use their IAM passwords to authenticate into the identity domain.
By deactivating delegated authentication, you can verify that the AD credentials from a user in that domain can be used to sign in to IAM before activating delegated authentication for the bridge.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Security**.
  4. Select **Delegated Authentication**.
  5. Expand the node to the right of the AD Bridge for which you want to deactivate delegated authentication.
  6. Turn off the **Activate Delegated Authentication** switch.
  7. In the **Deactivate Delegated Authentication** window:
    1. Select the **Send a Password Reset Notification (recommended)** option if you want users in the AD domain associated with the AD bridge to receive notifications to reset the passwords for their accounts. This is recommended for security purposes.
    2. Select the **Create a Password** option if you want to manually reset passwords for the users in the domain associated with the bridge. No notification is sent to users. Selecting this option means that the users in the domain, who were previously able to sign in using delegated authentication, can't sign in to the system. To allow them to sign in to the system, reset their passwords by using the reset passwords option on the **Users** tab. See [Resetting a User Password](https://docs.oracle.com/en-us/iaas/Content/Identity/users/reset-passwords-user-accounts.htm#top "Reset the password for a single account, for multiple accounts, or for all accounts in an OCI IAM identity domain.").
  8. Select **OK**.


Was this article helpful?
YesNo

