Updated 2025-01-14
# Enabling Provisioning for an App Catalog Application
User provisioning and synchronization are an important aspect of application management. Provisioning allows you to manage the lifecycle of accounts in applications like creating and deleting accounts using IAM. For example, when you grant the user access to an application such as Google Suite, then this user account is automatically created in Google Suite. This allows you to quickly add new users to multiple applications and de-provision users from those applications instantly when they change roles or leave your organization.
You can enable and configure provisioning for App Catalog applications either when adding the app or later when modifying it. When you enable provisioning by turning on the switch, the following steps appear:
  1. Configure the app connectivity.
Configure your app connectivity by providing values for the respective fields. Ensure you **Test connectivity** before moving to the next configuration.
  2. Configure the **Attribute mapping**.
Using **Attribute mapping** you can map IAM attributes to the attributes in your application account. You can verify the existing default mapping and, if necessary, change mappings by selecting appropriate values from the list for the required user attribute. You can add rows to map missed attributes and delete rows to exclude duplicate attribute mapping. To add a new attribute for provisioning, select **Add row** , specify the attributes in the **User** and your application account columns, and then select **Save changes**. For example, if you want to add the **External ID** field, enter `$(user.externalId)` in the **User** column, and then select the corresponding field from the list in the applications account column.
  3. Select the provisioning operations.
Any app that supports provisioning and synchronization can be an authoritative app. If **Authoritative Sync** is configured, you can automatically create, modify, delete, and activate or disable users based only on the corresponding data from the authoritative application. However, the regular provisioning operations aren't allowed while authorization sync is enabled. 
When authoritative sync is enabled, the following actions happen automatically:
     * If a user isn't present in IAM, then the user is automatically created.
     * If an authoritative synced user is deleted from the application, then the user is also deleted from IAM.
     * If attributes of an authoritative synced user are modified, then the attributes for the user are also modified in IAM.
When **Authoritative Sync** is enabled, then the provisioning operations aren't permitted from IAM to the target application. To manage users in the application using provisioning, clear the **Authoritative Sync** checkbox. The following provisioning operations appear:
     * **Create account** : Select to create an account when the app is granted to the user.
     * **Update account** : Select to update this account. 
     * **De-activate Account** : Select to deactivate a user who is assigned to an application.
     * **Delete account** : Select to delete the account in the app when the IAM user is deleted.


**Important** When you configure the connection between your app and IAM, check and verify any pre-filled username and password field entries as these might not be the credentials to access your application.
To configure provisioning and synchronization for your application, follow the specific application catalog instructions for the application.  After you have enabled Provisioning, you can perform the following actions:
  * Assign users or groups to your App Catalog application to start the user provisioning process for your application. See [Assigning Users to Custom Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/assign-users-custom-applications.htm#assign-users-custom-applications "Custom applications are non Oracle Public Cloud \(OPC\) services. You can modify custom applications by assigning users to them. Users can access the My Apps page to view these applications.") and [Assigning Groups to Custom Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/assign-groups-custom-applications.htm#assign-groups-custom-applications "You can modify custom applications by assigning groups to them. Users who are members of these groups can access the My Apps page to view these applications.").
  * Enable and configure synchronization. To enable and configure synchronization, see [Enable Synchronization for an App Catalog Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enable-synchronization-app-catalog-application.htm#enable-synchronization-app-catalog-application "User provisioning and synchronization is an important aspect of application management. After enabling provisioning, synchronization allows you to control how operations like creating and deleting accounts in Software as a Service \(SaaS\) applications are reflected in IAM.").


Was this article helpful?
YesNo

