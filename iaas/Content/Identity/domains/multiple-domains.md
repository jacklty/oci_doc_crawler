Updated 2025-02-03
# Using Multiple Identity Domains
Create and manage multiple identity domains (for example, one domain for development and one for production) each with different identity and security requirements to protect your applications and Oracle Cloud services.
Using multiple identity domains can help you maintain the isolation of administrative control over each identity domain. This is necessary if, for example, security standards prevent development user IDs from existing in the production environment, or require that different administrators have control over different environments.
Each tenancy contains a Default identity domain, the identity domain which comes with your tenancy. Administrators can create as many additional identity domains as their license allows. Administrators can:
  * Create additional identity domains and be the identity domain administrator for them or assign another user to be the administrator.
  * Create additional identity domains and, as part of the identity domain creation process, assign users to be identity domain administrators of the identity domains.
  * Delegate the creation of additional identity domains to other administrators.


An identity domain administrator is assigned to an identity domain during the creation of the identity domain. Although the identity domain administrator identity might have the same username as a user in the Default identity domain, they're different users who might have different privileges in each identity domain, and will have separate passwords.
The identity domain administrator can use the entire feature set of the identity domain. In an identity domain, the identity domain administrator can:
  * Manage users, groups, applications, system configuration, and security settings.
  * Perform delegated administration by assigning users to different administrative roles.
  * Enable and disable Multifactor Authentication (MFA), configure MFA settings, and configure authentication factors.
  * Create self-registration profiles to manage different sets of users, approval policies, and applications.


Was this article helpful?
YesNo

