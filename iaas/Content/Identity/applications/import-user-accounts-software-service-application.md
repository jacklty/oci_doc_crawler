Updated 2025-01-14
# Importing Users from a SaaS Application
After enabling provisioning and synchronization for your App Catalog app, you might want to import the existing users from your Software as a Service (SaaS) applications and link them to IAM users. 
**Before You Begin:**
Before you import your SaaS users, verify that:
  * The app is activated. To activate your app, see [Activating Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/activate-applications.htm#activate-applications "Activate an application in an identity domain in IAM to reinstate the access rights to the application for users and groups.").
  * Provisioning is enabled. See [Enabling Provisioning for an App Catalog Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enable-provisioning-app-catalog-application.htm#enable-provisioning-app-catalog-application "User provisioning and synchronization are an important aspect of application management. Provisioning allows you to manage the lifecycle of accounts in applications like creating and deleting accounts using IAM. For example, when you grant the user access to an application such as Google Suite, then this user account is automatically created in Google Suite. This allows you to quickly add new users to multiple applications and de-provision users from those applications instantly when they change roles or leave your organization.").
  * Synchronization is enabled. See [Enabling Synchronization for an App Catalog Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enable-synchronization-app-catalog-application.htm#enable-synchronization-app-catalog-application "User provisioning and synchronization is an important aspect of application management. After enabling provisioning, synchronization allows you to control how operations like creating and deleting accounts in Software as a Service \(SaaS\) applications are reflected in IAM.").


  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  3. Select the name of the app that you want to configure.
  4. Verify that the app is activated.
  5. Select **Import**.
The page lists the result of the last import if any and the actions you need to perform. See [Synchronizing User Accounts](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/synchronize-user-accounts.htm#synchronize-user-accounts "After synchronizing your SaaS app with an identity domain, you will see the result of the import including the number of users created, deleted, and updated. You can do a general search based on account name, user e-mail, or username. You can also filter and search the results based on Situation and Synchronization Status. Select values from the respective lists to view users matching the search criteria. These are helpful when you have to find a set of users based on their situation or status from a huge number of results.").
  6. If you want to invoke an on-demand synchronization, select the **Import** icon. If the icon is unavailable, select the **Provisioning** tab and verify that Provisioning and Synchronization are enabled, and the app is activated.
  7. A message confirms that the job for importing users is running successfully.

After the import finishes, the page lists the imported users.
Was this article helpful?
YesNo

