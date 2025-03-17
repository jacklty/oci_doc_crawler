Updated 2025-01-14
# Adding a Social Identity Provider
Add a social identity provider (IdP) so that users can sign in to an identity domain in IAM with their social credentials.
Configure the IdP to Redirect to IAM.
  1. Create an application for the social IdP. 
For example, go to the Google developer site to create a Google application.
  2. Configure the value of `redirectUrl` in the application 
The value of `redirectUrl` must have the format:
```
https://<Identity domain base URL>/oauth2/v1/social/callback
```

**Note**
Ensure that the value of `redirectUrl` doesn't contain port number `:443`. If it does, update the existing URL to remove the port number or add a new URL without the port number to the IdP application by using the external provider developers' website.
Each social IdP calls these URLs by a different name:
     * Facebook: **Valid OAuth redirect URIs**
     * Google and LinkedIn: **Authorized redirect URL**
     * Microsoft: **Redirect URLs**
     * X (formerly Twitter): **Callback URL**
  3. Ensure that you retain the **Client ID** and the **Client Secret** values from the application that you created at the social IdP. You use this ID and secret when configuring the social IdP in the identity domain.

You can choose from the following predefined social login types: 
  * Facebook
  * Google
  * LinkedIn
  * Microsoft
  * OpenID Connect
  * X (formerly Twitter)


  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **Identity providers**.
  3. Select **Add IdP** , and then select **Add Social IdP**.
  4. In the **Add social identity provider** panel, select a social login.
  5. Enter a name and description for the social IdP.
  6. In the **Name** and **Description** fields, enter a name and description for the social identity provider.
**Note** The social identity provider name can contain spaces. However, it can't contain special characters. Avoid entering confidential information.
  7. Enter the client ID and the client secret for the social login type.
  8. To allow users to link their social accounts, select the **Enable account linking** checkbox. To prevent users from linking their social accounts, clear the checkbox.
**Note** You can prevent users from linking to their social accounts for security or organizational purposes. For example, if a hacker accesses the user's social account, the hacker can't sign in to the identity domain to access resources and applications.
  9. Select **IdP**.
  10. On the details page for the IdP you created, select **Activate IdP**.
  11. Log in with the social IdP.
**Note**
You might encounter this error message: "Not Logged In: You are not logged in. Please log in and try again."
The most likely cause is that the application you created on the social IdP side has the wrong client ID or redirect URL in the configuration. Check the client ID and the redirect URL configuration, and try to log in again.
  12. (Optional) Activate the IdP before adding it to any policies. For more information, see [Activating or Deactivating an Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/activate-identity-provider.htm#activate-identity-provider "Activate or deactivate an identity provider \(IdP\) for an identity domain in IAM.").


Was this article helpful?
YesNo

