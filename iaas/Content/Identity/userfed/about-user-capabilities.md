Updated 2024-12-18
# About User Capabilities
About user capabilities.
To access Oracle Cloud Infrastructure, a user must have the required credentials. Users who need to use the Console must have a password. Users who need access through the API need API keys. Some service features require additional credentials, such as auth tokens, SMTP credentials, and customer secret keys (previously known as Amazon S3 Compatibility API keys). For a user to get these credentials, the user must be granted the capability to have the credential type.
User capabilities are managed by an Administrator in the user's details. Each user can see their capabilities, but only an Administrator can enable or disable them. The user capabilities available to federated users are:
  * API keys
  * auth tokens
  * SMTP credentials
  * customer secret keys
  * OAuth 2.0 client credentials


By default, these capabilities are enabled when you provision new users, allowing users to create these credentials for themselves. For information about these user credentials, see [Working with User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/usercred/usercredentials.htm#user_credentials). 
**Important** The capability "Console password" is not available for federated users. Federated users authenticate to the Console through their IdP, where their sign-in passwords are managed.
Was this article helpful?
YesNo

