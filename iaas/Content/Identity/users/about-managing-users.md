Updated 2024-11-23
# Managing Users
Describes how to create and manage user accounts, including creating, updating, and deleting them.
For information about the number of users you can have, see [IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits).
  * [Lifecycle for Managing Users](https://docs.oracle.com/en-us/iaas/Content/Identity/users/lifecycle-managing-users.htm#user-lifecycle "User life cycle is a term to describe the process flow of how a user account is created, managed, and deleted in an identity domain based on certain events or time factors.")
  * [Creating a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/create-user-accounts.htm#top "Create a user account for a user in an OCI IAM identity domain.")
  * [Viewing User Details](https://docs.oracle.com/en-us/iaas/Content/Identity/users/view-user-account.htm#top "View the details of a user account in an OCI IAM identity domain.")
  * [Editing a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/edit-user-account.htm#top "Modify the details of a user account in an OCI IAM identity domain.")
  * [Deleting a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/delete-user-accounts.htm#top "Delete one or more user accounts in an OCI IAM identity domain for users who no longer need access to the service.")
  * [Unlocking a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/unlock-user-accounts.htm#top "Unlock a user account in an OCI IAM identity domain.")
  * [Resetting a User Password](https://docs.oracle.com/en-us/iaas/Content/Identity/users/reset-passwords-user-accounts.htm#top "Reset the password for a single account, for multiple accounts, or for all accounts in an OCI IAM identity domain.")
  * [Resending an Invitation to a User to Activate their Account](https://docs.oracle.com/en-us/iaas/Content/Identity/users/resend-invitations.htm#top "Resend an invitation to a user so that they can activate their user account in an OCI IAM identity domain.")
  * [Editing a User's Capabilities](https://docs.oracle.com/en-us/iaas/Content/Identity/users/edit-users-capabilities.htm#top "Change the capabilities that decide which user credentials users can create for themselves, such as local password, API keys, Auth token, SMTP credentials, customer secret keys, OAuth 2.0 client credentials, database passwords, in an OCI IAM identity domain.")
  * [Listing Users](https://docs.oracle.com/en-us/iaas/Content/Identity/users/list-user-accounts.htm#top "List user accounts in an OCI IAM identity domain.")
  * [Searching for a User Account](https://docs.oracle.com/en-us/iaas/Content/Identity/users/search-user-accounts.htm#top "Search for a user in an OCI IAM identity domain.")
  * [Changing a User's Status](https://docs.oracle.com/en-us/iaas/Content/Identity/users/change-status-user-account.htm#top "Activate or deactivate a user account in an OCI IAM identity domain.")
  * [Clearing All Keep Me Signed-In Sessions for a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/clear-signed-in-sessions-for-users.htm#top "If Keep me signed-in has been set for an OCI IAM identity domain, you can delete the Keep me signed-in sessions for a user.")
  * [Linking a User to a My Oracle Cloud Support Account](https://docs.oracle.com/en-us/iaas/Content/Identity/users/link-to-mos.htm#top "Link a user in an OCI IAM identity domain with a My Oracle Cloud Support Account.")
  * [Assigning Applications to a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/assign-applications-users.htm#top "Assign applications to a user in an OCI IAM identity domain.")
  * [Removing Applications from a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/remove-applications-user-account.htm#top "Remove applications that have been assigned to a user in an OCI IAM identity domain.")
  * [Assigning Users to Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/users/assign-users-roles.htm#top "Assign users in an OCI IAM identity domain to a role.")
  * [Adding a User to a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/users/assign-groups-user-account.htm#top "Add a user in an OCI IAM identity domain to a group.")
  * [Removing Users from Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/users/remove-groups-user-account.htm#top "Remove a user in an OCI IAM identity domain from a group.")
  * [Resetting Authentication Factors for User Accounts](https://docs.oracle.com/en-us/iaas/Content/Identity/users/reset-authentication-factors-user-accounts.htm#top "Describes how to reset all verification factors for a user in an OCI IAM identity domain if the user's device can't be used to provide a second factor for authentication, for example, if the user's device is lost or the Oracle Mobile Authenticator app has been deleted from the device.")
  * [Generating a Bypass Code for a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/generate-bypass-codes-user-accounts.htm#top "Generate a bypass code for a user in an OCI IAM identity domain. The code can be used as a one-time 2-Step Verification method to sign in.")


## Required Policy or Role 🔗 
To manage identity domain settings, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role or the Security Administrator role
  * Be a member of a group granted `manage` domains


To give this permission to non administrators, you'll need to additionally write policies like the following:
Copy
```
allow group GroupA to {USAGE_BUDGET_READ} in tenancy
allow group GroupA to {USAGE_BUDGET_INSPECT} in tenancy
allow group GroupA to {USAGE_BUDGET_MANAGE} in tenancy
allow group GroupA to {TENANCY_INSPECT} in tenancy
```

where you replace GroupA with the name of the group you want to grant the permission to.
To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Was this article helpful?
YesNo

