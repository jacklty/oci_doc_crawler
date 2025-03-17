Updated 2024-04-02
# Managing Authorization Using the API
The identity domains REST API supports both token-based authorization and OCI request signatures. For security reasons, the identity domains REST API isn't accessible using only the username and password that you use to sign in to the identity domain. To access the identity domains REST API, you need an OAuth2 access token or an API key to use for authorization.
identity domains REST API use the OAuth 2.0 protocol for authentication and authorization and support these common authorization scenarios:
  * Web server
  * Mobile
  * JavaScript applications


The Authorization section discusses the OAuth 2.0 scenarios that identity domains support.
This section contains the following topics:
  * [Registering a Client Application](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/registering_a_client_application.htm "An application must be registered as an OAuth 2 Client using the identity domain. OAuth clients are HTTP clients that can get and then use an access token.")
  * [Security Recommendations](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SecurityChecklist.htm "To securely integrate your applications with identity domains using OAuth, you must implement security controls recommended by the standard.")
  * [Scopes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/Scopes.htm#Scopes "Using the scope parameter, the access token can grant different levels of access to multiple IAM identity domain APIs.")
  * [Access Grant Types](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedAccessGrantTypes.htm#SupportedAccessGrantTypes "The most important step for an application in the OAuth flow is how the application receives an access token \(and optionally a refresh token\). A grant type is the mechanism used to retrieve the token. OAuth defines several different access grant types that represent different authorization mechanisms.")
  * [Supported Tokens](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/SupportedTokens.htm "A token is used to make security decisions to authorize a user and to store tamper-proof information about a system entity in an identity domain.")
  * [Token Validation](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/TokenValidation.htm "Why do we validate tokens? When your web application checks credentials directly, it verifies that the username and password that are presented correspond to what you maintain. When using claims-based identity, you're outsourcing that job to an identity provider.")
  * [Working with AppRoles](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/working_with_app_roles.htm "Learn about AppRole permissions, which AppRoles can be granted to clients and users, and how to grant app roles to apps and groups.")
  * [Authentication and On-Demand MFA API HTTP Status Codes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/MFAAuthAPIStatusCodes.htm "The Authentication and On-Demand Multifactor Authentication \(MFA\) APIs for identity domains in IAM are REST compliant and use standard HTTP response status codes to indicate failure.")
  * [Authentication and On-Demand MFA API Error Codes](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/MFAAuthAPIErrorCodes.htm "The Authentication and On-Demand Multifactor Authentication \(MFA\) APIs for identity domains in IAM provide error codes and descriptive messages when errors occur.")


Was this article helpful?
YesNo

