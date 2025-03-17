Updated 2025-02-03
# Creating a Secure Form Fill App
After you create a configuration file in the Oracle Enterprise Single Sign-On (ESSO) Administrative Console, the next step is to create a secure form fill app.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  2. Select **Add application** , and then select **Application Catalog**.
  3. In the Filters section for the Type of integration, select **Secure form fill** , locate **Generic Secure FormFill App Template** , and then select it.
  4. Complete the application details by entering a **Name** , **Description** , and **Application URL**.
**Important**
The application name must match the file name of the `.ini` file created in the ESSO Administrative Console.
  5. In the URLs section, add any necessary URLs. 
  6. In the **Display settings** section, select **Display in My Apps**.
**Important** If you do not select **Display in My Apps** , the application does not display in the **My Apps** page for users.
When you select the **Display in My Apps** checkbox in applications, the app is then visible in the **My Apps** page, but selecting this checkbox doesn't enable or disable SSO to the app.
  7. Select the **User can request access** checkbox, if you want the app to be listed in the **Catalog**. This option allows end users to request access to applications from their **My Apps** page by selecting **Add** and then selecting the app from the **Catalog**. 
  8. Select **User can view their credentials** if you want users to view their credentials in **User settings** or **My profile**.
  9. Select **Create application**.
  10. Select **Import** to import the secure form fill configuration file that you created in the ESSO Administrative Console.
The application has been added in deactivate state. To activate your application, select **Activate** next to the app name.
  11. To assign users to the application, select **Users**.
**Tip** Assign the application to yourself or a test user. This saves you time when testing the secure form fill app.
  12. To assign groups to the application, select **Groups**.

The applications you assign to the user or group displays on the **My Apps** page. Newly assigned applications and applications that a user has not yet accessed appear first in the application list and have an asterisk icon in the application tile. The icon appears on the tile until the user accesses the application.
Was this article helpful?
YesNo

