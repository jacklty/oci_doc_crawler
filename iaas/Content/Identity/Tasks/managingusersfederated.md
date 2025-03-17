Updated 2025-01-14
# Managing User Capabilities for Federated Users
This topic describes managing user capabilities for federated users when your tenancy is federated and configured for user provisioning with a [supported identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm#Prerequi).
## About User Capabilities 🔗 
To access Oracle Cloud Infrastructure, a user must have the required credentials. Users who need to use the Console, must have a password. Users who need access through the API need API keys. Some service features require additional credentials, such as auth tokens, SMTP credentials, and Amazon S3 Compatibility API keys. For a user to get these credentials, the user must be granted the capability to have the credential type.
User capabilities are managed by an Administrator in the user's details. Each user can see their capabilities, but only an Administrator can enable or disable them. The user capabilities available to federated users are:
  * API keys
  * auth tokens
  * SMTP credentials
  * customer secret keys
  * OAuth 2.0 client credentials


By default, these capabilities are enabled when you provision new users, allowing users to create these credentials for themselves. For information about these user credentials, see [Managing User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#top). 
**Important** The capability "Console password" is not available for federated users. Federated users authenticate to the Console through their IdP, where their sign-in passwords are managed.
## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access for managing user capabilities. A user can't enable or disable user capabilities for themselves (except for Administrators). However, a user can manage their own credentials that have been enabled for them.
## Prerequisites 🔗 
Management of user capabilities for federated users is supported for Oracle Identity Cloud Service and Okta federations only. 
  * Oracle Identity Cloud Service federations:
If your tenancy was created December 21, 2018 or later, your tenancy is automatically configured to manage user capabilities. There are no prerequisites.
If your tenancy was created before December 21, 2018, you must perform a one-time upgrade. See [Enabling User Provisioning](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingscim.htm#Enabling_User_Provisioning).
  * If your tenancy is federated with Okta, see [User Provisioning for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingscim.htm#User_Provisioning_for_Federated_Users).


## Viewing Provisioned Federated Users in the Console 🔗 
After the prerequisites are satisfied, you can view users that you create in your IdP that belong to groups mapped to Oracle Cloud Infrastructure groups. Whenever you add a user to a group mapped to an Oracle Cloud Infrastructure group, the user automatically displays in the Console.
**To list users in the Console** :
Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. 
Notice that you can filter the list by user type to include only users that belong to a specified identity provider. **Local Users** are users created in Oracle Cloud Infrastructure's IAM service. The filter list includes all identity providers you have set up. 
## Using the Console 🔗 
[ To edit user capabilities](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm)
If you're an Administrator, you can edit user capabilities.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed. 
  2. Click the user to see its details. 
  3. Click **Edit User Capabilities**.
  4. Select or clear the check box to add or remove a capability.
  5. Click **Save**. 


[To change a user's description](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed.
  2. Select the user you want to update. The user's details are displayed. The description is displayed under the user's login.
  3. Select the pencil next to the description.
  4. Edit the description and save it. This description is maintained in Oracle Cloud Infrastructure and is not synched back to your identity provider. 


[To apply tags to a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm)
For instructions, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags). 
[To delete a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed.
  2. Find the user you want to delete and select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)). 
  3. Select **Delete**.


**Important:** Deleting a user here does not delete the user in your IdP. If you later want the federated user to have a provisioned user in Oracle Cloud Infrastructure, you must remove the user from all OCI-mapped groups in Oracle Identity Cloud Service and re-add the user.
For information about managing user credentials in the Console, see [Managing User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#top).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage user capabilities:
  * [ListUsers](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/ListUsers)
  * [GetUser](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/GetUser)
  * [UpdateUser](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/UpdateUser): You can update the user capabilities and the user's description.
  * [UpdateUserCapabilities](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/UpdateUserCapabilities)
  * [DeleteUser](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/DeleteUser): This operation deletes the provisioned user in Oracle Cloud Infrastructure, but not the user in the identity provider.


For information about the API operations for managing user credentials, see [Managing User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#top).
The following operations are _not_ supported for federated users:
  * [ListUserGroupMemberships](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/ListUserGroupMemberships)
  * [AddUserToGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/AddUserToGroup)
  * [GetUserGroupMembership](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/GetUserGroupMembership)
  * [RemoveUserFromGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/RemoveUserFromGroup)


Was this article helpful?
YesNo

