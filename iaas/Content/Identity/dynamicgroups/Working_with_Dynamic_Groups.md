Updated 2023-09-07
# Working with Dynamic Groups
Work with dynamic groups.
When you create a dynamic group, you must provide a unique, unchangeable _name_ for the dynamic group. The name must be unique across all groups within your tenancy. You must also provide the dynamic group with a _description_ (although it can be an empty string), which is a non-unique, changeable description for the group. Oracle will also assign the dynamic group a unique ID called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Resource_Identifiers). 
**Note**
If you delete a dynamic group and then create a new dynamic group with the same name, they'll be considered different groups because they'll have different OCIDs. 
A dynamic group has no permissions until you write at least one **policy** that gives that dynamic group permission to access resources in either the tenancy or a compartment. In the policy, you can specify the dynamic group by using either the unique name or the dynamic group's OCID. Per the preceding note, even if you specify the dynamic group name in the policy, IAM internally uses the OCID to determine the dynamic group. For information about writing policies, see [Overview of Working with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/policymgmt/managingpolicies.htm#overview_policies). 
You can delete a dynamic group, but only if the group is empty.
Was this article helpful?
YesNo

