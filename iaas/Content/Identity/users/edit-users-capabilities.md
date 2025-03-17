Updated 2025-02-18
# Editing a User's Capabilities
Change the capabilities that decide which user credentials users can create for themselves, such as local password, API keys, Auth token, SMTP credentials, customer secret keys, OAuth 2.0 client credentials, database passwords, in an OCI IAM identity domain.
The user capabilities you can select or clear are:
  * Local password
  * API keys
  * Auth token
  * SMTP credentials
  * Customer secret keys
  * OAuth 2.0 client credentials
  * Database passwords


See [Working with User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/usercred/usercredentials.htm#user_credentials) for details of each option.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**.
  3. Select a user to see the user details.
  4. Select **Edit user capabilities**.
  5. Select or clear the checkbox to add or remove a capability.
**Note** The **Local password** option is disabled for federated users.
  6. Select **Save changes**.


Was this article helpful?
YesNo

