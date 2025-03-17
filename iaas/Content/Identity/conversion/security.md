Updated 2024-09-26
# Security
Find out about the Administrators group, administrator roles, administrator roles and policies, as well as password and sign-on policies.
## OCI Administrators Group 🔗 
Each OCI tenancy includes an Administrator account that is, by default, a member of the tenancy Administrators group. The Administrators group grants full access to the entire tenancy. For this reason, it's best practice not to use the Administrator account for day-to-day administration of the tenancy.
The best practice is to reserve the Administrators group for emergency scenarios. Individual administrators can be granted permissions to manage their respective areas without any single person having full access to the entire tenancy.
As Identity Cloud Service instances become a native part of OCI, members of the Administrators group have full access to manage IAM identity domains. This doesn't mean that current Identity Cloud Service administrators have administrative privileges on OCI accounts.
Confirm that use of the Administrators group is consistent with the security policies of your organization.
In some cases, a group called `OCI_Administrators` is added to the IDCS instance that was provided during tenancy creation (usually called the `IdentityCloudService`). This group is mapped to the Default identity domain's Administrators group, which doesn't have users assigned at creation time. If you want users to have full access to the entire tenancy, you can add them to the OCI_Administrators group in the IdentityCloudServicedomain.
## Identity Domain Admin Roles 🔗 
Any user with the identity domain administrator role has administrative privileges for that identity domain. Best practice is for the identity domain administrator to create other administrators administrators (or example, a user administrator) with the minimal set of administration responsibilities they need to perform their tasks. See [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
## Identity Domain Admin Roles Compared With Policies 🔗 
Administrator roles are scoped to a specific identity domain. So, for example, a user administrator for `DomainB` can only manage users in `DomainB` and can't manage users in `DomainA`.
In contrast to administrator roles, policies apply to compartments in the tenancy. So, for example, if a user in group `foo` in `DomainA` is given a policy such as:
```
allow group DomainA/foo to manage users in tenancy
```

This gives the user those privileges over the entire tenancy.
**Note**
When referencing groups, policies ought to include the specific domain as a prefix such as `DomainA` in the policy example preceding. See [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The) and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
## Authentication Settings Compared With Password Policies 🔗 
In identity domains, IAM authentication settings which are used to set password rules, are now part of Password Policies. You can define multiple password policies and assign them to different groups. See [Managing Sign-On Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/managingsignonpolicies.htm#Managing_signonpolicies).
## Network Sources Compared With Network Perimeters 🔗 
If you have been using network sources to specify an allowed set of IP addresses from which users can perform certain actions, such as sign in to the Console, with identity domains you can use network perimeters to do the same. See [Managing Network Perimeters](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/overview.htm#understand-network-perimeters "Network perimeters in an identity domain in IAM restrict the IP addresses that users can use to sign in.").
  1. Before your Identity Cloud Service is migrated, make a note of the network sources you use, for example, `my-allow-list 140.160.240.0/24`. 
  2. After your tenancy has migrated, create network perimeters using the same IP addresses. See [Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter.htm#add-network-perimeter "Create a network perimeter in an identity domain in IAM and configure it to restrict the IP addresses that users can use to sign in.").
  3. Create policies that reference the new network perimeters, such as a [sign-on policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/add-sign-policy.htm#add-sign-policy "Add a sign-on policy to an identity domain in IAM.") or an [identity provider policy](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/add-identity-provider-policy.htm#add-idp-policy "Create an identity provider policy for an identity domain.").


## Sign-On Policies 🔗 
If you have been using the default sign-on policy to protect the Identity Cloud Service Console, that policy continues to enforce rules after migration.
After migration, the OCI Console is enabled for your account and it's protected by a new sign-on policy called Security Policy for OCI Console.
For more information about the sign-on policies see [About Sign-On Policies and Sign-On Rules](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/managingsignonpolicies.htm#understand-sign-policies "A sign-on policy uses sign-on rules to define criteria that determine whether to allow a user to sign in to an identity domain or an application.").
Was this article helpful?
YesNo

