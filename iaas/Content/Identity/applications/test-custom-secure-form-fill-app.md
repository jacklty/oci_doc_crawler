Updated 2025-01-14
# Testing a Custom Secure Form Fill App
After you create a custom secure form fill app in an identity domain in IAM, test the app before deploying it to your organization.
**Before you begin:**
**Before You Begin:**
  * A custom secure form fill app created in the identity domain.
  * The custom secure form fill app is set to display on the My Apps page.
  * The custom secure form fill app is assigned to you as a user or as a group.

To test a custom secure form fill app, complete the following steps: 
  1. Sign in to the Console to access the My Apps page.
  2. Install the secure form fill plug in, if you have not already installed it, and then refresh your browser.
  3. Open the app, enter the credentials for the application, and then select **Login**.


A successful result is IAM injecting the username and password, and then selecting the submit button.
If you are having issues, check the settings for your Web app in the Oracle Enterprise Single Sign-On (ESSO) Administrative Console, export the *.ini file if necessary, check the settings for your app in the identity domain, and try again.
Was this article helpful?
YesNo

