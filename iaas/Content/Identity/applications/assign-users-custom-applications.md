Updated 2025-01-14
# Assigning Users to Custom Applications
Custom applications are non Oracle Public Cloud (OPC) services. You can modify custom applications by assigning users to them. Users can access the **My Apps** page to view these applications.
  * The application must be activated.
  * The application must be assigned to the current user who is accessing the **My Apps** page
  * The **Display in My Apps** checkbox must be selected in the **Details** tab in the applications.


  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select the application that you want to modify.
  4. Select **Users**.
  5. Select **Assign users**.
  6. In the **Assign users** window, do one of the following:
    1. Select the checkbox for each user that you want to assign to the application.
    2. For a provisioned application, select **Assign** next to the user that you want to assign to the application. Enter the required values for the form, and then select **Save**.
**Note** If the form contains multi-valued attributes, then an **Add** button appears to the right of each attribute. Select **Add** , and then in the **Allowed values** window, select the values for the attribute, and select **OK**.
  7. Select **Assign**.


**Note**
If you assigned a provisioned application to the user, then you can modify the values of the application form. To do this, select the **Actions** menu, select **Edit** , change the appropriate values, and then select **Save**.
You can activate or deactivate a user's account assigned to a synchronized app that's created from the App Catalog. To do so:
  1. Select the **Actions** menu to the right of the user account that you assigned to the application.
  2. Select **Activate** or **Deactivate**.
  3. In the **Activate account?** or **Deactivate account?** window, select **OK**. 


See [Enabling Provisioning for an App Catalog Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enable-provisioning-app-catalog-application.htm#enable-provisioning-app-catalog-application "User provisioning and synchronization are an important aspect of application management. Provisioning allows you to manage the lifecycle of accounts in applications like creating and deleting accounts using IAM. For example, when you grant the user access to an application such as Google Suite, then this user account is automatically created in Google Suite. This allows you to quickly add new users to multiple applications and de-provision users from those applications instantly when they change roles or leave your organization.") for more information about configuring provisioning for an application to manage the lifecycle of users in the application.
Was this article helpful?
YesNo

