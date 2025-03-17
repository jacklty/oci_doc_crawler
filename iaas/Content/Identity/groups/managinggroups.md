Updated 2024-09-26
# Managing Groups
A group has no permissions until you do one of the following:
  * Write at least one **policy** that gives that group permission to either the tenancy or a compartment. When writing the policy, you can specify the group by using either the unique name or the group's OCID. For information about writing policies, see [Managing Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies.htm#overview_policies).
  * Assign the group to an application.


**Note**
The **All-Domain-Users** group is a group that's created by IAM. All identity domain users are assigned to this group by default. If you assign this group to any of your applications, then all users are assigned to these applications indirectly. 
For a user, the **All-Domain-Users** group doesn't appear in the **Groups** tab because this group is assigned automatically when a new user is created. Also, because this group is created by IAM, and not by an administrator, you can't delete this group.
For information about the number of groups you can have, see [IAM Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits).
  * [Creating a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/create-groups.htm#create-groups "Create an identity domain group in IAM.")
  * [Adding Users to a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/add-users-to-groups.htm#add-users-to-groups "Add users to an identity domain group in IAM.")
  * [Removing Users from a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/remove-users-from-groups.htm#remove-users-from-groups "Remove users from an identity domain group.")
  * [Assigning Applications to a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/assign-applications-group.htm#assign-applications-group "Assign applications to an identity domain group in IAM.")
  * [Removing Applications from a Group](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/remove-applications-group.htm#remove-applications-group "Remove applications from an identity domain group.")
  * [Deleting Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/delete-groups.htm#remove-groups "Delete groups from an identity domains in IAM.")


## Required Policy or Role 🔗 
To manage identity domain settings, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role or the Security Administrator role
  * Be a member of a group granted `manage` domains


To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Was this article helpful?
YesNo

