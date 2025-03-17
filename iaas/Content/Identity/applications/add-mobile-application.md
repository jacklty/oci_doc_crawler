Updated 2025-01-14
# Adding a Mobile Application
Add mobile applications that use OAuth 2.0 and they can't maintain the confidentiality of their client secrets.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select **Add application**.
  4. In the **Add application** window, select **Mobile Application**.
  5. Select **Launch workflow**.
  6. In the Add applications details page, use the following table to configure the application details.
Option | Description  
---|---  
**Name** |  Enter a name for the mobile application. You can enter up to 125 characters. For applications with lengthy names, the application name appears truncated in the **My Apps** page. Consider keeping application names as short as possible.  
**Description** |  Enter a description of the mobile application. You can enter up to 250 characters.  
**Application icon** |  Select the close (X) in the Application icon window to delete the default **Application icon** and then add your own icon for the application. This icon appears next to the name of the application on the My Apps page and the Applications page.  
**Custom sign-in URL** |  In the **Custom sign-in URL** field, specify a custom sign-in URL. However, if you're using a default login page provided by IAM, then leave this field blank.  
**Custom sign-out URL** |  In the **Custom sign-out URL** field, specify a custom sign-out URL. However, if you're using a default login page provided by IAM, then leave this field blank.  
**Custom error URL** |  This is an optional field. Enter the error page URL to which a user has to be redirected, if there is a failure. If not specified, the domain-specific Error page URL is used. If both the error URLs are not configured, then the error is redirected to the IAM Error Page (/ui/v1/error). When a user tries to use social authentication (ex: Google, Facebook, and so on) for logging into IAM, the callback URL must be configured in the **Custom error URL** field. Social providers need this callback URL to call IAM and send the response back after social authentication. The provided callback URL is used to verify whether the user exists or not (if this is a first-time social login), and display an error if the social authentication has failed.  
**Custom social linking callback URL** |  This is an optional field. Enter the URL that IAM can redirect to after linking of a user between social providers and IAM is complete. When you create a custom app using IAM custom SDK and integrate with IAM Social Login, the custom app needs to have the Custom social linking callback URL which can be redirected after linking of the user between social provider and IAM is complete.  
**Display in My Apps** |  Select the checkbox if you want the mobile application to be listed for users on their My Apps pages. In this case, you need to configure the application as a resource server. When you select the **Display in My Apps** checkbox in applications, the app is then visible in the **My Apps** page, but selecting this checkbox doesn't enable or disable SSO to the app. The flag to enable or disable SSO comes from the app template. Use the IAM REST APIs to update this flag. You can't set the SSO flag from the UI.   
**User can request access** |  Select the **User can request access** checkbox if you want the app to be listed in the Catalog. This option allows end users to request access to the app from their My Apps page by selecting **Add** and then selecting the app from the Catalog.  
**Enforce grants as authorization** |  Select the checkbox if you want end users to be able to request access to the app from their **My Apps** page by selecting **Add access.** If self-service isn't enabled, users won't see the **Add access** button.  
  7. Select **Next**. 
  8. In the **Authorization** section of the Add Mobile Application page, use the following table to configure application details.
Option | Description  
---|---  
**Allowed grant types** |  Select the checkbox for the grant types that this application is allowed to use when requesting validation.
     * Select the **Refresh token** grant type when you want a refresh token supplied by the authorization server, and then use it to obtain a new access token. Refresh tokens are used when the current access token becomes invalid or expires and don't require the resource owner to reauthenticate.
     * Select the **Authorization code** checkbox when you want to obtain an authorization code by using an authorization server as an intermediary between the client application and resource owner. An **authorization code** is returned to the client through a browser redirect after the resource owner gives consent to the authorization server. The client then exchanges the authorization code for an access (and often a refresh) token. Resource owner credentials are never exposed to the client.
     * Select the **Implicit** checkbox if the application can't keep client credentials confidential for use in authenticating with the authorization server. An access token is returned to the client through a browser redirect in response to the resource owner authorization request (rather than an intermediate authorization code).
     * Select the **Device code** grant type if the client can't receive requests from the OAuth Authorization Server, for example, it can't act as an HTTP server such as game consoles, streaming media players, digital picture frames, and others.  In this flow, the client obtains the user code, device code, and verification URL. The user then accesses the verification URL in a separate browser to approve the access request. Only then can the client obtain the access token using the device code.  
**Allow non-HTTPS URLs** |  Select this checkbox if you want to use HTTP URLs for the **Redirect URL** , **Logout URL** , or **Post logout redirect URL** fields. For example, if you're sending requests internally, want a non-encrypted communication, or want to be backward-compatible with OAuth 1.0, then you can use an HTTP URL. Also, select this checkbox when you're developing or testing your application and you might not have configured SSL. This option is provided as a convenience and isn't recommended for production deployments.  
**Redirect URL** |  Enter the application URL where the user is redirected after authentication. Add additional redirect URLs as needed.  
**Post-logout redirect URL** |  Enter the URL where you want to redirect the user after logging out of the application. Add additional post-logout redirect URLs as needed.  
**Logout URL** |  Enter the URL where the user is redirected after logging out of the application.  
**Allowed operations** |  Select the **On behalf of** checkbox, if you want to ensure that access privileges can be generated from the user's privileges alone, so that a client application can access endpoints to which the user has access, even if the client application by itself would not normally have access.  
**Bypass consent** |  If enabled, this attribute overwrites the **Require consent** attribute for all the scopes configured for the application, and then no scope will require consent.  
**Client IP address** | 
     * **Anywhere** : The token request is allowed from anywhere. There's no perimeter.
     * **Restrict by network perimeter** : Select the network perimeters so that a token request is only allowed from them.  
**Add resources** |  If you want your application to access APIs from other applications, then select **Add scope** in the **Token issuance policy** section. Then, in the **Add scope** window, select the applications that your application will reference.  
**Add app roles** |  Select **Add** to enable your mobile application to access IAM APIs. In the **Add app roles** window, select the application roles that you want to assign to this application. This enables your application to access the REST APIs that each of the assigned application roles can access. For example, select **Identity Domain Administrator** from the list. All REST API tasks available to the identity domain administrator will be accessible to your application. You can delete the application roles by selecting the **x** icon for the row of the required application role. **Note:** You can't delete protected application roles.  
  9. Select **Finish**. A message confirms that the application has been added in deactivated state. To activate your application see [Activating Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/activate-applications.htm#activate-applications "Activate an application in an identity domain in IAM to reinstate the access rights to the application for users and groups.").
  10. Note that the Client ID appears General information section for the application. To integrate with your application, use this ID as part of your connection settings. Because a mobile application runs on a mobile device, a Client Secret isn't generated for this type of application.


Was this article helpful?
YesNo

