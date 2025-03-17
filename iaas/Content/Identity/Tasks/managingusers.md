Updated 2025-01-14
# Managing Users
This topic describes the basics of working with users.
**Important** If your tenancy is federated with Oracle Identity Cloud Service, see [Managing Oracle Identity Cloud Service Users and Groups in the Oracle Cloud Infrastructure Console](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#Managing_Oracle_Identity_Cloud_Service_Users_and_Groups_in_the_Oracle_Cloud_Infrastructure_Console) to manage users.
## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access for managing users. 
  * You can create a policy that gives someone the power to create new users and credentials but not control which groups those users are in. See [Let the Help Desk manage users](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#helpdesk-manage-users).


If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top). If you want to dig deeper into writing policies for users or other IAM components, see [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top).
## Tagging Resources 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Working with Users 🔗 
When creating a user, you must provide a unique, unchangeable _name_ for the user. The name must be unique across all users within your tenancy. This name is the user's login to the Console. You might want to use a name that's already in use by your company's own identity system (for example, Active Directory, LDAP, etc.). You must also provide the user with a _description_ (although it can be an empty string), which is a non-unique, changeable description for the user. This value could be the user's full name, a nickname, or other descriptive information. Oracle also assigns the user a unique ID called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Resource_Identifiers). 
**Note**
If you delete a user and then create a new user with the same name, the two users are considered different users, because they have different OCIDs. 
Oracle recommends that you supply a password recovery email address for the user. If the user forgets their password, they can request to have a temporary password sent to them using the **Forgot Password** link on the sign-on page. If no email address is present for the user, an administrator must intervene to reset their password.
A new user has no permissions until you place the user in one or more groups and at least one **policy** gives that group permission to either the tenancy or to a compartment. Exception: each user can manage _their own_ credentials they have been enabled to have. An administrator does not need to create a policy to give a user that ability. For more information, see [User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#User_Credentials).
**Important** After creating a user and putting them in a group, let them know which compartment(s) they have access to. 
You also need to give the new user some credentials so they can access Oracle Cloud Infrastructure. A user can have one or both of the following credentials, depending on the type of access they need: A password for using the Console and an API signing key for using the API. 
## About User Capabilities 🔗 
To access Oracle Cloud Infrastructure, a user must have the required credentials. Users who need to use the Console must have a password. Users who need access through the API need API keys. Some service features require additional credentials, such as auth tokens, SMTP credentials, and Amazon S3 Compatibility API keys. For a user to get these credentials, the user must be granted the capability to have the credential type.
Administrators manage user capabilities in the User details. Each user can see their capabilities, but only an Administrator can enable or disable those capabilities. The user capabilities are:
  * Can use Console password (native users only)
  * Can use API keys
  * Can use auth tokens
  * Can use SMTP credentials
  * Can use customer secret keys


By default, all these capabilities are enabled when you create users, allowing users to create these credentials for themselves. For information about working with user credentials, see [Managing User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#top).
## Enabling Multifactor Authentication for a User 🔗 
See [Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingmfa.htm#Managing_MultiFactor_Authentication) for details.
## Signing In to the Console 🔗 
Users created through this procedure are created in IAM and are sometimes called "local users." If your tenancy is federated with another identity provider (such as Oracle Identity Cloud Service, Azure AD, or Okta), your sign-in page to the Console displays two options for signing in. The local users you create in IAM use the Oracle Cloud Infrastructure option to sign in, as shown in the following image:
[![Sign in option for local users](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_local_signin.PNG)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_local_signin.PNG)
If your tenancy is not federated, you only have one sign in option.
## Tracking Recent Sign-in Activity 🔗 
The Users list page displays information to assist administrators in determining whether user accounts are active. The **Last recorded sign in** field displays the date and time the user last signed in to Oracle Cloud Infrastructure by using the Console or by using Oracle DB integrated with IAM. For Console sign-ins, the timestamp is the last Console sign-in. For sign-ins using Oracle DB integrated with IAM, timestamps can have up to a 15-minute buffer from the **Last recorded sign in**. This field is displayed only on the list view of all users, it's not displayed on the individual user details page. 
This field only tracks sign-ins from the Console or from Oracle DB integrated with IAM. If a user accesses Oracle Cloud Infrastructure through other access methods (for example, through the SDK), those sign-ins are not tracked.
## Linking a User to a My Oracle Support Account 🔗 
To file support requests directly from the Console, each user must link their IAM user account with their My Oracle Support (MOS) account. You only need to complete this step once. For instructions, see [To link a user to their My Oracle Support account](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm#To2).
### Prerequisites 🔗 
  * Before a user can create this link, they must set up an account in My Oracle Cloud Support. For information on setting up a My Oracle Cloud Support account, see [Creating an Oracle Single Sign On (SSO) Account](https://docs.oracle.com/iaas/Content/GSG/Tasks/usingsupport.htm#ToGetSSOforMOS).


## Unblocking a User After Unsuccessful Sign-in Attempts 🔗 
If a user unsuccessfully tries to sign in to the Console 10 times in a row, they are blocked from further sign-in attempts. An administrator can unblock the user in the Console (see [To unblock a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm#unblock_user)) or with the [UpdateUserState](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/UpdateUserState) API operation.
## Deleting a User 🔗 
You can delete a user, but only if the user is not a member of any groups. 
## Limits on Users 🔗 
For information about the number of users you can have, see [Service Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase.").
## Using the Console 🔗 
[To create a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed.
  2. Select **Create User**. 
  3. Enter the following: 
     * **Name:** A unique name or email address for the user. For tips about what value to use, see [Working with Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm#Working). The name must be unique across all users in your tenancy. You cannot change this value later. The name must meet the following requirements: No spaces. Only Basic Latin letters (ASCII), numerals, hyphens, periods, underscores, +, and @.
     * **Description:** This value could be the user's full name, a nickname, or other descriptive information. You can change this value later.
     * **Email:** Enter an email address for the user. This email address is used for password recovery. The email address must be unique in the tenancy. 
If the user forgets their password, they can select **Forgot Password** on the sign on page, and a temporary password is generated and sent to the email address provided here. The user or an administrator can also update the email address can also later.
     * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  4. Select **Create**. 


Next, you need to give the user permissions by adding them to at least one group. You also need to give the user the credentials they need (see [Managing User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#top)).
[To add a user to a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed.
  2. Locate the user in the list. 
  3. Click the user. The user's details are displayed.
  4. Click **Groups**.
  5. Click **Add User to Group**. 
  6. Select the group from the drop-down list, and then click **Add**.


Let the user know which compartment(s) they have access to. 
[To remove a user from a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed.
  2. Locate the user in the list.
  3. Select the user. The user's details are displayed.
  4. Select **Groups**.
  5. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Remove**.
  6. Confirm when prompted. 


[To delete a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
Prerequisite: To delete a user, the user must not be in any groups. 
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed.
  2. For the user you want to delete, select **Delete**.
  3. Confirm when prompted. 


[To unblock a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
If you are an administrator, you can use the following procedure to unblock a user who has unsuccessfully tried to sign in to the Console 10 times in a row.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed. 
  2. Select the user. The user's details are displayed, including the current status.
  3. Select **Unblock**.
  4. Confirm when prompted. 


[To change a user's description](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed.
  2. Select the user you want to update. The user's details are displayed. The description is displayed under the user's login.
  3. Select the pencil next to the description.
  4. Edit the description and save it. 


[To edit a user's email](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed.
  2. Select the user you want to update. The user's details are displayed.
  3. Under **User Information** , select the pencil next to **Email**.
  4. Enter the email address and select the save icon. The email address must be unique in the tenancy. 


[ To edit user capabilities](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
If you're an Administrator, you can edit user capabilities.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed. 
  2. Click the user to see its details. 
  3. Click **Edit User Capabilities**.
  4. Select or clear the check box to add or remove a capability.
  5. Click **Save**. 


[To apply tags to a user](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
For instructions, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags). 
[To link a user to their My Oracle Support account](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
**Important:** Ensure that you meet the prerequisites before linking your account. See [Linking a User to a My Oracle Support Account](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm#Linking).
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed.
  2. Select the user you want to update. The user's details are displayed.
  3. Select **Link Support Account**. The Oracle account sign in page prompts you to enter your Oracle credentials.
  4. Enter the **User name** and **Password** of the Oracle support account that you want to link to this user and select **Sign in**. The IAM user account is linked to the Oracle support account. The e-mail address associated with the support account is displayed in the user details in the field **My Oracle Support account**. 


[To unlink a user a user from a My Oracle Support account](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusers.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Users**. A list of the users in your tenancy is displayed.
  2. Select the user you want to update. The user's details are displayed.
  3. Select **Unlink Support Account**. 
  4. In the confirmation prompt, select **Unlink**. 


For information about managing user credentials in the Console, see [Managing User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#top).
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
**Note**
Updates Are Not Immediate Across All Regions
Your IAM resources reside in your home region. To enforce policy across all regions, the IAM service replicates your resources in each region. Whenever you create or change a policy, user, or group, the changes take effect first in the home region, and then are propagated out to your other regions. It can take several minutes for changes to take effect in all regions. For example, assume you have a group with permissions to launch instances in the tenancy. If you add UserA to this group, UserA is able to launch instances in your home region within a minute. However, UserA is not able to launch instances in other regions until the replication process is complete. This process can take up to several minutes. If UserA tries to launch an instance before replication is complete, they will get a not authorized error.
Use these API operations to manage users:
  * [CreateUser](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/CreateUser)
  * [ListUsers](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/ListUsers)
  * [GetUser](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/GetUser)
  * [UpdateUserState](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/UpdateUserState): Unblocks a user who has tried to sign in 10 times in a row unsuccessfully.
  * [UpdateUser](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/UpdateUser): You can update the user's description, email, and tags.
  * [UpdateUserCapabilities](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/UpdateUserCapabilities)
  * [DeleteUser](https://docs.oracle.com/iaas/api/#/en/identity/latest/User/DeleteUser)
  * [ListUserGroupMemberships](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/ListUserGroupMemberships): Use this operation to get a list of which users are in a group, or which groups a user is in.
  * [AddUserToGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/AddUserToGroup): This operation results in a `UserGroupMembership` object with its own OCID.
  * [GetUserGroupMembership](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/GetUserGroupMembership)
  * [RemoveUserFromGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/RemoveUserFromGroup): This operation deletes a `UserGroupMembership` object.


For information about the API operations for managing user credentials, see [Managing User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm#top).
Was this article helpful?
YesNo

