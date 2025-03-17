Updated 2023-05-25
# Understanding Administrator Roles
Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.
In your organization, you might want administrators to have different levels of access to various tasks and resources. For example, the identity domain administrator has superuser privileges for an identity domain. This administrator may want to delegate some of their responsibilities to other users to carry out the tasks associated with these responsibilities, such as managing system configuration and security settings, applications, users, groups, group memberships, and so on. To do this, the administrator assigns these users to other administrator roles. Users who are assigned to these roles will be able to perform specific tasks that are associated with the roles.
The following table lists the administrator roles and summarizes the privileges for each role.
Administrator role | Privileges  
---|---  
Identity domain administrator |  Has superuser privileges for an identity domain in IAM Identity domain administrators can:
  * Manage users, groups, applications, system configuration, and security settings
  * Perform delegated administration by assigning users to different administrative roles
  * Enable and disable Multi Factor Authentication (MFA), configure MFA settings, and configure authentication factors
  * Create self-registration profiles to manage different sets of users, approval policies, and applications

  
Security administrator |  Manage IAM system configuration and security settings for an identity domain. Security administrators can customize the interface, default settings, notifications, and the password policies, configure Multi Factor Authentication (MFA), and manage the Microsoft Active Directory (AD) Bridge, Provisioning Bridge, identity providers, and trusted partner certificates.  
Application administrator | Manage applications. Application administrators can create, update, activate, deactivate, and delete applications. Application administrators can also grant and revoke access to applications for groups and users.  
User administrator | Manage users, groups, and group memberships for an identity domain.  
User manager | Manage all users or users of selected groups in an identity domain. User managers can update, activate, deactivate, remove, and unlock user accounts. User managers can also reset passwords, reset authentication factors, and generate bypass codes for user accounts.  
Help desk administrator | Manage all users or users of selected groups in an identity domain. Help desk administrators can view the details of a user and unlock a user account. Help desk administrators can also reset passwords, reset authentication factors, and generate bypass codes for user accounts.  
Audit administrator | Run reports for an identity domain.  
[Assigning Users to Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/users/assign-users-roles.htm#top "Assign users in an OCI IAM identity domain to a role.").
Was this article helpful?
YesNo

