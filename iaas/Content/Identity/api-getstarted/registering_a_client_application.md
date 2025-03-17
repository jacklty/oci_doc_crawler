Updated 2024-04-02
# Registering a Client Application
An application must be registered as an OAuth 2 Client using the identity domain. OAuth clients are HTTP clients that can get and then use an access token. 
Complete the following steps to use an OAuth client to access identity domains REST API:
  1. Sign in to the identity domain using the username and password found in your Welcome email.
  2. Create an OAuth client application and make note of the client ID and client secret.
**Note** When you configure the OAuth client application, select the application roles that you want to assign to the application. This enables your application to access the REST APIs that each of those assigned application roles can access. Each application role has scopes assigned to it that define an even more fine-grain level of access to API operations. For example, select **Identity Domain Administrator** from the list. All REST API operations available to the identity domain administrator will be accessible to the application.
  3. Use the client ID and client secret to request an access token from the IAM OAuth Service.
  4. Include the access token in the appropriate HTTP header when you make REST API calls.


**More Information**
  * For more information on registering a client application, see [Registering a Client Application](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/register-client-app.htm#register-client-app "Before you configure multifactor authentication \(MFA\) in an identity domain in IAM, register a client application so that you have the credentials \(client ID and client secret\) that are used for authentication in REST API calls. Oracle Support can use your client ID and client secret to help you troubleshoot if you have issues, for example, if you lock yourself out of an identity domain when configuring MFA.").
  * For more information on grant types, see [Access Grant Types](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedAccessGrantTypes.htm#SupportedAccessGrantTypes "The most important step for an application in the OAuth flow is how the application receives an access token \(and optionally a refresh token\). A grant type is the mechanism used to retrieve the token. OAuth defines several different access grant types that represent different authorization mechanisms.").
  * To walk through the steps yourself, see [Using OAuth 2 to Access the REST API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/OATOAuthClientWebApp.htm "The identity domains REST API supports SCIM 2.0 compliant endpoints with standard SCIM 2.0 core schemas and Oracle schema extensions to programmatically manage users, groups, applications, and identity functions, such as password management and administrative tasks. To make REST API calls to your identity domain, you need an OAuth2 access token to use for authorization. The access token provides a session \(with scope and expiration\), that your client application can use to perform tasks in an identity domain.").
  * For a list of all available endpoint operations and the application roles required to access them, see [AppRole Permissions](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequiredRolePerEndpointExt.htm#RequiredRolePerEndpointExt "To grant an application access to the identity domains REST API, you must first know the allowed operations that you need the application to access. Then, assign the AppRoles with access to those operations to your application."). 
  * For a list of which AppRoles can be granted to both clients and users and which can only be granted to clients, see [AppRoles That Can Be Granted to Clients and Users](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/AppRoleClientsUsers.htm "Identity domains application roles define what a user or application client can do in an identity domain. These AppRoles directly translate into identity domain OAuth scopes that are used to secure access to protected identity domain resources. Some AppRoles are available only to clients. Some AppRoles are available to both clients and users.").


Was this article helpful?
YesNo

