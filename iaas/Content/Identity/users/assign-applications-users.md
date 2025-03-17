Updated 2025-02-18
# Assigning Applications to a User
Assign applications to a user in an OCI IAM identity domain.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**.
  3. Select the user account that you want to modify.
  4. Select **Applications**.
  5. Select **Assign applications**.
  6. In the **Assign applications** window, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Assign** for each application that you want to assign to the user account.
  7. If you're assigning a managed application to the user account, then an **Assign Application** window appears, containing a form for the application. To populate this form:
    1. Enter the required values for the form.
    2. If the form contains multi valued attributes, then an **Add** button appears to the right of each attribute. Select **Add** , and then in the **Allowed Values** window, select the values for the attribute, and select **OK**.
**Tip** To remove an existing value from the attribute, select the **X** button to the right of the value.
    3. Select **Save**.
**Note**
The **Active** icon for each application in the **Access** tab represents the active status of the user account and not the application status. The status remains active as long as the user account is active, regardless of whether the application is active or inactive.
  8. Select **Finish**.
**Note**
If you assigned a managed application to the user account, then you can modify the values of the application form. To do this, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) then select **Edit** , change the appropriate values, and then select **Save**.
Also, if you have enabled and configured synchronization for an App Catalog app, and assigned the app to a user account, then you can activate or deactivate the user's account with the app. To do so:
    1. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the App Catalog app that you assigned to the user.
    2. Select **Activate** or **Deactivate**.
    3. In the **Confirmation** window, select **OK**.


Was this article helpful?
YesNo

