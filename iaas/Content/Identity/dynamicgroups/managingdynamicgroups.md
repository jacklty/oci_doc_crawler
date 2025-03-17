Updated 2024-09-26
# Managing Dynamic Groups
Dynamic groups allow you to group compute instances and other resources as "principal" actors (similar to user groups). You can then create policies to permit the resources to [make API calls against services](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/callingservicesfrominstances.htm#Calling_Services_from_an_Instance). When you create a dynamic group, rather than adding members explicitly to the group, you instead define a set of _matching rules_ to define the group members. Resources that match the rules are members of the group. For example, a rule could specify that all instances in a particular compartment are members of the dynamic group. The members can change dynamically as instances are launched and terminated in that compartment.
You can perform the following dynamic group management tasks:
  * [Working with Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Working_with_Dynamic_Groups.htm#Working "Work with dynamic groups.")
  * [Updating Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Updating_Dynamic_Groups.htm#Updating_Dynamic_Groups "Update dynamic groups.")
  * [Creating a Dynamic Group](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/To_create_a_dynamic_group.htm#create-dynamic-group "Create a dynamic group in IAM.")
  * [Updating a Dynamic Group's Description](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/To_update_a_dynamic_groups_description.htm#update-dynamic-group-description "Update a dynamic group's description.")
  * [Deleting a Dynamic Group](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/To_delete_a_dynamic_group.htm#delete-dynamic-group "Delete a dynamic group in IAM.")
  * [Assigning a Domain Role](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/assign-domain-role.htm#assign-domain-role "By default, every dynamic group is associated with the Identity Cloud Service \(IDCS\) application. You can assign a domain role to that application to allow members of the dynamic group to perform certain actions with IDCS in the identity domain.")
  * [Updating a Dynamic Group's Matching Rules](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/To_update_a_dynamic_groups_matching_rules.htm#update-dynamic-group-matching-rules "Update the matching rules for a dynamic group in IAM.")
  * [Writing Matching Rules to Define Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm#Writing "Matching rules define the resources that belong to a dynamic group.")
  * [Using the Rule Builder](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Using_the_Rule_Builder.htm#using-rule-builder "The rule builder is a tool available from the Console to help you write matching rules.")


## Required Policy or Role 🔗 
To manage identity domain settings, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role or the Security Administrator role
  * Be a member of a group granted `manage` domains


To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Was this article helpful?
YesNo

