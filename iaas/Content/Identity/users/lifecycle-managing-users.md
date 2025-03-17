Updated 2023-04-27
# Lifecycle for Managing Users
User life cycle is a term to describe the process flow of how a user account is created, managed, and deleted in an identity domain based on certain events or time factors.
A user account goes through various stages in the life cycle. The stages are non existent, deactivated, activated, and deleted.
You can define business requirements for each transition of the user life cycle. Use the sample scenarios listed in the following table to establish the link between user lifecycle transitions and business objectives.
Current State | Operation | Sample Scenario | Process Description  
---|---|---|---  
Non-existent | Create | Human resources (HR) enters user profile information for a new hire. |  If the new hire's start date isn't a future date, then the user account is introduced with an **Activated** status.  If the new hire's start date is a future date, then the user account is created, and is then deactivated.  
Deactivated | Activate | The user's start date is in effect. |  The user account is activated, and the user can now sign in and use this Oracle Cloud service. The user can access all groups, applications, and administration role privileges assigned to the user account.  
Activated | Modify | The user is promoted to a new position. HR changes the job title of the user. |  New groups, applications, and administration roles are assigned to the user account. Old irrelevant groups, applications, and administration roles are removed from the user account.  
Activated | Deactivate | The user takes a one-year sabbatical from the company. HR manually deactivates the user account on the last working day of the user. The user rejoins the company after some period. HR activates the user account. | The user account is deactivated, and the user can no longer sign in and use this Oracle Cloud service. The user account can be activated again.  
Activated | Delete | The user retires from the company. HR manually deletes the user account on the last working day of the user. |  The user account is removed. All groups, applications, and administration role privileges assigned to the user account are revoked as part of the workflow. If you remove (delete) the user, the audit data of the user remains in the system. To manually (and immediately) purge the audit data of the deleted user, see [Purging Audit Data for a Deleted User](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/purge-audit-data-deleted-user.htm#purge-audit-data-deleted-user "When you delete a user from an identity domain in IAM, the audit data of the user remains in the system. You can manually and immediately purge the audit data of that deleted user.").  
The following concepts are integral to user lifecycle management:
  * User Account: A user account represents a user in an identity domain, and enables the user to access the Oracle Cloud service to which they belong. In an identity domain, there is a one-to-one relationship between a user and a user account. By default, all users can use their accounts to perform self-service capabilities. Users can update their profiles, reset their passwords, unlock their accounts, and change their email preferences.
  * Administrator Role: You might want to provide a user account with administrative capabilities in IAM. To do this, you assign administrator roles to user accounts. See [Assigning Users to Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/users/assign-users-roles.htm#top "Assign users in an OCI IAM identity domain to a role.").
  * Group: Identity domains provide easy and controlled privilege management through groups. Groups are the links between user accounts and applications in the identity domain. Groups are designed to ease the administration of privileges that you grant to user accounts or other groups. See [Managing Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/managinggroups.htm#Managing_Groups).
  * Application: Oracle applications are a complete and modular set of enterprise applications, engineered from the ground up to be cloud-ready and to coexist seamlessly in mixed environments.
You can use identity domains in IAM to grant access to Oracle applications in two ways:
    * Directly: Assigning users to the applications
    * Indirectly: Assigning groups to the applications. Any users who are members of the groups are granted access to the applications.
In addition to granting users and groups access to Oracle applications, you can grant users and groups access to entitlements within applications. For example, you use IAM to grant John Doe and Jane Doe access to Oracle Java Cloud Service. You want John Doe to have administrator privileges for Oracle Java Cloud Service, but Jane Doe to have user privileges only.
Each entitlement in an Oracle application is represented by an **application role**. So by assigning John Doe to the application administrator role of Oracle Java Cloud Service, he can not only access this Oracle Cloud service, but he can also function as an administrator within it.
See [Managing Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/overview.htm#overview "Identity domains provide a secure and centralized cloud service to manage your cloud, Oracle, custom, and enterprise applications.") for more information about how you can use IAM to grant and revoke access rights for users and groups to applications and application roles.


Was this article helpful?
YesNo

