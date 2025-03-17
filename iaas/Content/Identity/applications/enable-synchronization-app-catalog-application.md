Updated 2025-01-14
# Enabling Synchronization for an App Catalog Application
User provisioning and synchronization is an important aspect of application management. After enabling provisioning, synchronization allows you to control how operations like creating and deleting accounts in Software as a Service (SaaS) applications are reflected in IAM.
You can enable and configure synchronization for App Catalog applications either when adding the app or later when modifying it. You can only enable synchronization after enabling provisioning. To enable provisioning, see [Enabling Provisioning for an App Catalog Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enable-provisioning-app-catalog-application.htm#enable-provisioning-app-catalog-application "User provisioning and synchronization are an important aspect of application management. Provisioning allows you to manage the lifecycle of accounts in applications like creating and deleting accounts using IAM. For example, when you grant the user access to an application such as Google Suite, then this user account is automatically created in Google Suite. This allows you to quickly add new users to multiple applications and de-provision users from those applications instantly when they change roles or leave your organization."). Follow the application catalog instructions for your specific SaaS app to enable and configure synchronization. 
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  3. Select the name of the SaaS app that you want to configure.
  4. Under **Resources** , select **Provisioning** , and then turn on the **Enable synchronization** switch. 
  5. In the **Configure synchronization** section, modify the attributes following the application catalog instructions for your specific SaaS application. 
  6. Select **Save changes**.


Enable synchronization to import users from your SaaS app.
**Note** If the number of created objects (users) and deleted recorded objects (synced users) exceeds the maximum number allowed, the sync job quits. The maximum number of objects created or recorded objects deleted is an approximate maximum limit, not a precise limit because of the parallel processing of synced objects.
See [Importing User Accounts from a Software as a Service Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/import-user-accounts-software-service-application.htm#import-user-accounts-software-service-application "After enabling provisioning and synchronization for your App Catalog app, you might want to import the existing users from your Software as a Service \(SaaS\) applications and link them to IAM users.").
Was this article helpful?
YesNo

