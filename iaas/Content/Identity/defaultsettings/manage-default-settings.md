Updated 2024-09-26
# Managing Domain Settings
Domain settings are applied to this identity domain in the Cloud. You can specify settings such as the time zone, password recovery email, and language.
  * [Changing Locale Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/change-locale-settings.htm#change-default-settings "Change the identity domain–level default settings for time zone and language in IAM. Users can override the default settings in the My Profile Details tab in the My Profile console.")
  * [Viewing SAML Certificate Metadata](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/set-access-signing-certificate.htm#change-default-settings "Allow clients to access the signing certificate for the identity domain in IAM without logging in to an identity domain.")
  * [Getting the Root CA Certificate](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/obtain-root-ca-certificate.htm#obtain-root-ca-certificate "When you set up service providers and identity providers for federated SSO in an identity domain in IAM, you need to download the metadata file and the signing and encryption certificates. However, these certificates are not self-signed and are issued by a root certificate. So, for a proper setup and function, you need to get the root certificate and install it at the federation partner.")
  * [Setting Contact Email Addresses](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/set-contact-email.htm#change-default-settings "Set the email addresses to appear in email notifications from an identity domain in IAM.")
  * [Setting the Audit Retention Period](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/config-audit-retention.htm#change-default-settings "Set the retention period for audit logs for an identity domain in IAM.")
  * [Purging Audit Data for a Deleted User](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/purge-audit-data-deleted-user.htm#purge-audit-data-deleted-user "When you delete a user from an identity domain in IAM, the audit data of the user remains in the system. You can manually and immediately purge the audit data of that deleted user.")
  * [Requiring User's Email Address for Account Creation](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/set-primary-email-user.htm#change-default-settings "Set whether a primary email address is required to create user accounts in an identity domain in IAM.")


## Required Policy or Role
To change domain settings, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role or the Security Administrator role
  * Be a member of a group granted `manage` domains


To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Was this article helpful?
YesNo

