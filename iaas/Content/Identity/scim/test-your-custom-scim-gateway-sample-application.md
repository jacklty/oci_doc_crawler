Updated 2025-01-14
# Testing Your Custom SCIM Gateway Sample Application
Test your custom SCIM gateway sample application in an OCI IAM identity domain by provisioning users in an identity domain with it.
  1. In the **Applications** page, select your application, and then select it to open the **Users** tab.
  2. In the **Users** tab, select **Assign**.
  3. In the **Assign Users** window, choose a user, and then select **Assign**.
  4. In the **Assign Application** window, populate the **Username** , **Full Name** , **Family Name** , **Given Name** , **Display Name** , and **Primary Email** form fields with values, and then select **Save**.
  5. In the **Assign Users** window, select **OK**.
IAM creates a user account in the `userdb.json` file of your application.
  6. Open the `userdb.json` file and verify that a user account has been created. Then, close the file.
  7. In the **Users** tab, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the user, and then select **Deactivate**.
  8. After one minute, open the `userdb.json` file and verify that the corresponding user account has a `false` value for the `active` attribute. Then, close the file.
  9. In the **Users** tab, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the user, then select **Activate**.
  10. After one minute, open the `userdb.json` file and verify that the corresponding user account has a `true` value for the `active` attribute. Then, close the file.
  11. In the **Users** tab, select the user, and then select **Revoke**.
  12. In the **Confirmation** window, select **OK**.
  13. After the **Confirmation** window closes, open the `userdb.json` file and verify that the corresponding user account has been removed. Then, close the file.


Was this article helpful?
YesNo

