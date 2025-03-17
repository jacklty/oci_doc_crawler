Updated 2025-02-03
# The Default Identity Domain
Each tenancy includes a Default identity domain in the root compartment.
A Default identity domain: 
  * Can't be deactivated or deleted. (Lives with the life cycle of the tenancy.) 
  * Can't be hidden from the sign-in page.


The Default identity domain contains the initial tenant Administrator user and Administrators group and a default policy that allows administrators to manage any resource in the tenancy. The Administrators policy and the Administrators group can't be deleted and there must be at least one user in the Administrators group. You can also assign user accounts to predefined administrator roles to delegate administrative responsibilities it the Default domain.
**Note** Granting users or groups the identity domain administrator role for domains other than the default domain grants them full administrator permissions to only that domain (not to the tenancy). At least one administrator for the identity domain must be granted the identity domain administrator role directly. This is in addition to any identity domain administrator roles granted by group membership. For more information, see [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
You can upgrade a domain by changing the domain type. Each **identity domain type** is associated with a different set of features and object limits. For information to help you decide which domain type is appropriate for what you want to do, see [IAM Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#overview "Learn about identity domain types and the features and limits associated with each.").
Was this article helpful?
YesNo

