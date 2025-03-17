Updated 2025-01-14
# Editing Configuration Information for Custom Applications
You can edit configuration information for custom applications.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select the application that you want to modify.
  4. Select **Configuration**.
  5. Expand the **Client configuration** node.
  6. Modify a configuration value for the custom application by:
     * Entering the value in the attribute field (for example, in the **Redirect URL** field, entering the application URL where the user is redirected after authentication)
     * Selecting a button (for example, adding a resource to the custom application by selecting **Add** or removing a scope for a trusted application by selecting **Remove**)
     * Selecting or clearing the checkbox (for example, allowing the resource owner to be a grant type for the custom application by selecting **Resource owner**)
     * Selecting the value from the menu (for example, selecting **User administrator** from the **Grant the client access to Oracle Identity Cloud Service admin APIs.** list to enable the custom application to access user administrator-related APIs)
  7. If your custom application is a confidential or a mobile application, then you can switch **Bypass consent** on or off.
  8. If your custom application is a confidential application, then expand the **Resources** node.
If your custom application is a mobile application, then the **Resources** node doesn't appear in the **Configuration** tab. This is because confidential applications run on a protected server, and mobile applications run on an unauthenticated web browser or a mobile device.
  9. Modify a configuration value for the protected resources of your confidential application. See step 3 for more information about how to edit configuration values.
  10. Select **Save**.


See [Add a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-confidential-application.htm#add-confidential-application "Confidential applications run on a protected server."), [Add a Mobile Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-mobile-application.htm#add-mobile-application "Add mobile applications that use OAuth 2.0 and they can't maintain the confidentiality of their client secrets."), and [Add a SAML Application](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/add-saml-application.htm#add-saml-application "Create a Security Assertion Markup Language \(SAML\) application and grant it to users so that your users can single sign-on \(SSO\) into your SaaS applications that support SAML for SSO.") for more information about the configuration settings for client applications.
Was this article helpful?
YesNo

