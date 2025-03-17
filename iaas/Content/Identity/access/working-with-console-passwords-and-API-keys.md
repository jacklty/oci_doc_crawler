Updated 2024-09-30
# Working with Console Passwords and API Keys
Each user automatically can change or reset _their own_ identity domain password, as well as manage _their own_ API keys. An administrator doesn't need to create a policy to give a user those abilities.
**Note** Federated users might need to create a policy to modify API keys. For example, users who were provisioned through SCIM.
To manage credentials for users other than yourself, you must be in the Administrators group or some other group that has permission to work with the tenancy. Having permission to work with a compartment within the tenancy isn't enough. For more information, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The).
IAM administrators (or anyone with permission to the tenancy) can use either the Console or the API to manage all aspects of both types of credentials, for themselves and all other users. This includes creating an initial one-time password for a new user, resetting a password, uploading API keys, and deleting API keys. 
Users who aren't administrators can manage _their own_ credentials. They can:
  * Change or reset their own password.
  * Upload an API key in the Console for their own use (and also delete their own API keys).


And with the API, users can:
  * Reset their own password with [CreateOrResetUIPassword](https://docs.oracle.com/iaas/api/#/en/identity/latest/UIPassword/CreateOrResetUIPassword).
  * Upload an additional API key to the IAM service for their own use with [UploadApiKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/ApiKey/UploadApiKey) (and also delete their own API keys with [DeleteApiKey](https://docs.oracle.com/iaas/api/#/en/identity/latest/ApiKey/DeleteApiKey)). Remember that a user can't use the API to change or delete their own credentials until they themselves upload a key to the identity domain or an administrator uploads a key for that user by using the Console or the API.


A user can have a maximum of three API keys at a time.
Was this article helpful?
YesNo

