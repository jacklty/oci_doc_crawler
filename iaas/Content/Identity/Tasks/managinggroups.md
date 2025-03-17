Updated 2025-01-14
# Managing Groups
This topic describes the basics of working with groups.
**Important** If your tenancy is federated with Oracle Identity Cloud Service, see [Managing Oracle Identity Cloud Service Users and Groups in the Oracle Cloud Infrastructure Console](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#Managing_Oracle_Identity_Cloud_Service_Users_and_Groups_in_the_Oracle_Cloud_Infrastructure_Console) to manage groups.
## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access for managing groups. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top). If you want to dig deeper into writing policies for groups or other IAM components, see [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top).
## Tagging Resources 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Working with Groups 🔗 
When creating a group, you must provide a unique, unchangeable _name_ for the group. The name must be unique across all groups within your tenancy. You must also provide the group with a _description_ (although it can be an empty string), which is a non-unique, changeable description for the group. Oracle will also assign the group a unique ID called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Resource_Identifiers). 
**Note**
If you delete a group and then create a new group with the same name, they'll be considered different groups because they'll have different OCIDs. 
A group has no permissions until you write at least one **policy** that gives that group permission to either the tenancy or a compartment. When writing the policy, you can specify the group by using either the unique name or the group's OCID. Per the preceding note, even if you specify the group name in the policy, IAM internally uses the OCID to determine the group. For information about writing policies, see [Managing Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpolicies.htm#Managing_Policies). 
You can delete a group, but only if the group is empty.
For information about the number of groups you can have, see [Service Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase.").
If you're federating with an identity provider, you'll create mappings between the identity provider's groups and your IAM groups. For more information, see [Federating with Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top).
## Using the Console 🔗 
[To create a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinggroups.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. A list of the groups in your tenancy is displayed.
  2. Click **Create Group**. 
  3. Enter the following: 
     * **Name:** A unique name for the group. The name must be unique across all groups in your tenancy. You cannot change this later. The name must be 1-100 characters long and can include the following characters: lowercase letters a-z, uppercase letters A-Z, 0-9, and the period (.), dash (-), and underscore (_). Spaces are not allowed. Avoid entering confidential information.
     * **Description:** A friendly description. You can change this later if you want to.
     * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  4. Click **Create Group**.


Next, you might want to add users to the group, or write a policy for the group. See [To create a policy](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy).
[To add a user to a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinggroups.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. A list of the groups in your tenancy is displayed.
  2. Locate the group in the list. 
  3. Select the group. Its details are displayed
  4. Select **Add User to Group**. 
  5. Select the user from the drop-down list, and then select **Add User**. 


[To remove a user from a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinggroups.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. A list of the groups in your tenancy is displayed.
  2. Locate the group in the list.
  3. Select the group to display its details. A list of users in the group is displayed.
  4. Locate the user in the list. 
  5. For the user you want to remove, select **Remove**. 
  6. Confirm when prompted. 


[To delete a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinggroups.htm)
Prerequisite: To delete a group, it must not have any users in it. 
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. A list of the groups in your tenancy is displayed.
  2. Locate the group in the list. 
  3. For the group you want to delete, select **Delete**.
  4. Confirm when prompted.


[To update a group's description](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinggroups.htm)
This is available only through the API. If you don't have access to the API and need to update a group's description, contact [Oracle Support.](http://support.oracle.com/)
[To apply tags to a group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managinggroups.htm)
For instructions, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags). 
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
**Note**
Updates Are Not Immediate Across All Regions
Your IAM resources reside in your home region. To enforce policy across all regions, the IAM service replicates your resources in each region. Whenever you create or change a policy, user, or group, the changes take effect first in the home region, and then are propagated out to your other regions. It can take several minutes for changes to take effect in all regions. For example, assume you have a group with permissions to launch instances in the tenancy. If you add UserA to this group, UserA will be able to launch instances in your home region within a minute. However, UserA will not be able to launch instances in other regions until the replication process is complete. This process can take up to several minutes. If UserA tries to launch an instance before replication is complete, they will get a not authorized error.
Use these API operations to manage groups:
  * [CreateGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/CreateGroup)
  * [ListGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/ListGroups)
  * [GetGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/GetGroup)
  * [UpdateGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/UpdateGroup): You can update only the group's description.
  * [DeleteGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/Group/DeleteGroup)
  * [ListUserGroupMemberships](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/ListUserGroupMemberships): Use to get a list of which users are in a group, or which groups a user is in.
  * [AddUserToGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/AddUserToGroup): This operation results in a `UserGroupMembership` object with its own OCID.
  * [GetUserGroupMembership](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/GetUserGroupMembership)
  * [RemoveUserFromGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/UserGroupMembership/RemoveUserFromGroup): This operation deletes a `UserGroupMembership` object.


For API operations related to group mappings for identity providers, see [Federating with Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top). 
Was this article helpful?
YesNo

