Updated 2023-11-21
# Updating a Custom Secure Form Fill App
To update a custom secure form fill app, you first update the Web app using the Secure Form Fill App, export the configuration file in (*.ini), and then update the custom secure form fill app in the identity domain.
**Before you begin:**
  * Create a Web app in the Secure Form Fill Admin Client. See [Installing the Secure Form Fill Admin Client](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/install-secure-form-fill-admin-client.htm#install-secure-form-fill-admin-client "You use the Secure Form Fill Admin Client \(Oracle Enterprise Single Sign-On \(ESSO\) Administrative Console\) to create and update secure form fill configuration files for your custom secure form fill apps in IAM. Use these instructions to install the Secure Form Fill Admin Client.").
  * Create a custom secure form fill app created in the identity domain.

To update a custom secure form fill app, complete the following steps:
  1. If you need to update the Web app and configuration file created in Secure Form Fill Admin Client, update the Web app first, and then save and export the file. See [Create a Secure Form Fill Configuration File](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/create-secure-form-fill-configuration-file.htm#create-secure-form-fill-configuration-file "You use the Secure Form Fill Admin Client \(Oracle Enterprise Single Sign-On \(ESSO\) Administrative Console\) to create secure form fill configuration files for your custom secure form fill apps in IAM. Use these instructions to create secure form fill configuration files and then import those files into IAM.").
  2. To change the custom secure form fill app, access the application as an Identity domain administrator, make any necessary changes, import the new configuration file (if necessary), and then save the app. See [Create a Secure Form Fill App in IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/create-secure-form-fill-app-oci-iam.htm#create-secure-form-fill-app "After you create a configuration file in the Oracle Enterprise Single Sign-On \(ESSO\) Administrative Console, the next step is to create a secure form fill app.").

**What to do next:** Test your new configuration. See [Test a Custom Secure Form Fill App](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/test-custom-secure-form-fill-app.htm#test-custom-secure-form-fill-app "After you create a custom secure form fill app in an identity domain in IAM, test the app before deploying it to your organization.").
Was this article helpful?
YesNo

