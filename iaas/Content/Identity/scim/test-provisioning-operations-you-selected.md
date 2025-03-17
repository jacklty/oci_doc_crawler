Updated 2025-01-14
# Testing the Provisioning Operations You Selected
After you use the Generic SCIM App Template to configure an application in an OCI IAM identity domain, you must test the provisioning operations you selected to verify that they are operable.
  1. In the **Applications** page, select and activate your application, and then select it to open the **Details** tab.
  2. Select the **Users** tab, and then select **Assign users**.
  3. In the **Assign users** window, choose a user, and then select **Assign**.
  4. In the **Assign application** window, populate any form fields needed to provision a user account to your application, and then select **Save**. IAM starts the provisioning operation to create a user account in your application.
  5. Verify that the user account has been created in your application.
  6. In the **Users** tab, deactivate the user, activate the user again, and remove the user from your application. Each change you make is reflected in the user account for your application.
  7. Select the **Import** tab, and then select **Import**.
IAM communicates with your application's SCIM REST API to get a list of all user accounts. IAM tries to match each user account with an existing user in an identity domain. If a user exists, then the user is assigned to your application. If the user doesn't exist, then you can perform one of the following actions manually:
     * **Assign existing user:** Assign the user account to any user in IAM.
     * **Create new user and link:** Add a new user to IAM, and then assign the user account to this newly created user.


Was this article helpful?
YesNo

