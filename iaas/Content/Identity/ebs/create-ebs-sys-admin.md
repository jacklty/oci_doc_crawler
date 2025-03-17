Updated 2025-01-14
# Creating Oracle E-Business Suite's System Administrator in IAM
Create a user in IAM that corresponds to the System Administrator in your Oracle E-Business Suite. This user is necessary otherwise the system administrator won't be able to sign in to the Oracle E-Business Suite console after Oracle E-Business Suite is configured to use IAM for authentication.
  1. Sign in to IAM to access the IAM Console.
  2. In the IAM Console, expand the **Navigation Drawer** , select **Users** , and then select **Add** in the **Users** page.
  3. In the **Add User** window, provide the following values, and then select **Finish** :
     * **First Name** : `EBS`
     * **Last Name** : `Sysadmin`
     * Uncheck `Use the email address as the                          username`.
     * **Username** : `sysadmin`
     * **Email** : If the sysadmin user in your Oracle E-Business Suite is configured with an email address, provide this email address. Otherwise, provide an email address and then update Oracle E-Business Suite's System Administrator email address with this same value.

IAM sends a **Welcome** notification email to the email you provided with the procedures to reset the password of the `sysadmin` user.
Was this article helpful?
YesNo

