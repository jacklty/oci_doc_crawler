Updated 2025-02-28
# Managing Identity Domains
An identity domain is a container for managing users and roles, federating and provisioning of users, secure application integration through Oracle Single Sign-On (SSO) configuration, and SAML/OAuth based Identity Provider administration. It represents a user population in Oracle Cloud Infrastructure and its associated configurations and security settings (such as MFA). 
## Overview
Identity domains are similar to other OCI resources. As an administrator, you can create, move, tag, and delete an identity domain. OCI access policies can be written to allow users in a specific domain to access resources in other domains. You can also assign user accounts to predefined administrator roles to delegate administrative responsibilities within a domain. For more information about administrator roles and the privileges associated with each role, see [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
You manage identity domains (for example, creating or deleting a domain) using the user interface or the IAM API. You manage resources (for example, users and groups) within an identity domain using the user interface or with the SCIM-based IAM Identity Domains API.
Each tenancy includes a Default identity domain created in the root compartment that contains the initial tenant administrator user and group and a default Policy that allows administrators to manage any resource in the tenancy. The Default identity domain lives with the life cycle of the tenancy and can't be deleted.
You can create additional identity domains within a tenancy. Multiple identity domains are useful when you need separate environments for a single cloud service or application (for example, one environment for development and one for production). For added security, you can configure each identity domain to have its own credentials (for example, Password and Sign-On policies). You can also configure an identity domain for consumer-facing applications and allow consumer users to perform self-registration and social login.
You can upgrade a domain by changing the domain type. Each **identity domain type** is associated with a different set of features and object limits. For information to help you decide which domain type is appropriate for what you want to do, see [IAM Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#overview "Learn about identity domain types and the features and limits associated with each.").
Users in identity domains can request access to groups and applications. Users can also perform self-service tasks such as updating profile information, changing passwords, and configuring settings for 2-Step Verification.
## Information for Existing IAM and IDCS Administrators 🔗 
If you're an existing IAM or IDCS administrator and you don't see identity domains in your regions, read the following information to learn what to expect when the update happens.
  * [OCI IAM Identity Domains: What OCI IAM customers need to know](https://www.oracle.com/a/ocom/docs/security/what-oci-iam-customers-should-expect.pdf)
  * [OCI IAM Identity Domains: What Oracle IDCS customers need to know](https://www.oracle.com/a/ocom/docs/security/what-idcs-customers-should-expect.pdf)


If you're an existing IAM or IDCS administrator and your region has been updated recently, read the following information to learn about what to expect post update.
  * [OCI IAM Identity Domains: What OCI IAM customers need to know](https://www.oracle.com/a/ocom/docs/security/what-oci-iam-customers-should-expect-post-migration.pdf)
  * [OCI IAM Identity Domains: What Oracle IDCS customers need to know](https://www.oracle.com/a/ocom/docs/security/what-idcs-customers-should-expect-post-migration.pdf)


This section includes the following overview topics:
  * [Introduction](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/introduction-identity-domains.htm#introduction-identity-domains "Learn about the Default identity domain, how to use several domains, disaster recovery and domains, and more.")
  * [Using Implicit Access for Default Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/implicitManagedAccess-defaultdomain.htm#implicitManagedAccess_defaultdomain "OCI creates an automatic break glass workflow for default domains. This prevents users from being locked out of the system when a sign-on policy or an identity provider \(IdP\) policy isn't correctly configured.")


You can perform the following tasks related to identity domains:
  * [Listing Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-identity-domains.htm#view-identity-domains "Retrieve a list of the identity domains in a specific compartment in a tenancy in IAM.")
  * [Listing License Types](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-list-license-types.htm#untitled1 "Retrieve a list of the license types for identity domains in IAM supported by Oracle Cloud Infrastructure.")
  * [Creating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm#create-identity-domain "To create an identity domain in IAM, administrators need to know which identity domain type they want to create, in which compartment to create it, and the new identity domain administrator's sign-in credentials, if needed. The domain types that you're allowed to create are based on your subscription.")
  * [Getting an Identity Domain's Details](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-view-details-of-an-identity-domain.htm#view-details-identity-domains "View the details of an identity domain in IAM.")
  * [Editing an Identity Domain's Details](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-edit-domain-details.htm#edit-identity-domain "You can edit details for an identity domain in IAM. For example, you can select whether to show the identity domain on the sign-in page or upgrade a domain by changing the domain type.")
  * [Moving an Identity Domain Between Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-move-resources-to-a-different-compartment.htm#move-domain "Move identity domains between compartments in IAM.")
  * [Activating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-activate-a-domain.htm#deactivate-domain "You might create an identity domain in IAM that you need only temporarily, for example, for testing purposes. You can deactivate the identity domain when it's not in use and then reactivate it when it's needed.")
  * [Deactivating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm#deactivate-domain "You might create an identity domain in IAM that you need only temporarily, for example, for testing purposes. You can deactivate the identity domain when it's not in use and then reactivate it when it's needed. An identity domain must be deactivated before it can be deleted.")
  * [Changing an Identity Domain's Type](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-change-identity-domain-type.htm#changing_domain_type "Upgrade an identity domain in IAM.")
  * [Copying an Identity Domain's OCID](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-copy-an-identity-domain-ocid.htm#copy-identity-domain-ocid "Copy an identity domain's OCID so that you can, for example, paste it in the search field when searching for resources related to an OCID in a tenancy in IAM.")
  * [Replicating an Identity Domain to Multiple Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-manage-regions-for-domains.htm#manage-domain-regions "You can replicate an identity domain in IAM to additional regions to enable users in that domain to interact with OCI resources in those regions.")
  * [Resetting All Passwords for an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-reset-all-passwords-for-domain.htm#reset-all-domain-passwords "Force all users and administrators in an identity domain in IAM, including the identity domain administrators, to reset their password for the identity domain. After you select to reset the passwords, users and administrators receive an email notification requesting them to reset their passwords.")
  * [Deleting an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-delete-a-domain.htm#delete-domain "Delete an identity domain in a tenancy in IAM.")


## Required Policy or Role 🔗 
To manage identity domain settings, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role
  * Be a member of a group granted `manage` domains


To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Was this article helpful?
YesNo

