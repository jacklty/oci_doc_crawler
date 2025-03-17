Updated 2025-02-18
# Unlocking a User
Unlock a user account in an OCI IAM identity domain.
After a consecutive number of unsuccessful sign-in attempts, a user account is locked. The user receives a notification with a link that they can use to reset their password and unlock their account. An administrator can unlock accounts without requiring a password reset using the **Unlock User** option on the user details page. If you don't have administrative rights, the **Unlock User** option isn't available.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**.
  3. Select the user account that you want to unlock.
  4. Select **More actions** , and select **Unlock User**.
  5. In the **Confirmation** window, select **OK**.


**Note** If a user account is locked and the user or an administrator doesn't unlock it, then IAM unlocks it automatically after a specified time period. An administrator can set this time period from 5 minutes to 24 hours.
Was this article helpful?
YesNo

