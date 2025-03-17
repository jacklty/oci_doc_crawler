Updated 2023-04-04
# Groups
Find out about the changes for dynamic groups and matching rules, as well as the default groups for identity domains.
## Dynamic Groups 🔗 
Any IAM dynamic groups that existed prior to identity domains, remain available in the Default identity domain. See [Managing Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm#Managing_Dynamic_Groups).
## Matching Rules for Dynamic Groups 🔗 
### `ANY` or `ALL` Prefixes Before Conditions
If you use dynamic groups, we recommend that you review all matching rules that define the members of these dynamic groups. Validation of matching rules has changed. If a matching rule evaluated multiple conditions, but didn't include a prefix of either `ANY` or `ALL` before each condition, IAM automatically processed the syntax as though a prefix was implied.
**Important** Rewrite matching rules so that they include the required prefix.
For example, previously you could previously write the following matching rule:
`instance.id = 'x', compartment.id = 'y'`
Now, you must write the matching rule as follows:
```
ANY {instance.id = 'x', compartment.id = 'y'}
```

The preceding syntax includes a resource if either the:
  * instance OCID was `x`.
  * compartment OCID was `y`.


### Sequential Statements in Matching Rules
Sequential statements in a matching rule, such as `ALL {instance.id = 'x', compartment.id = 'y'`}, `ALL {instance.id = 'x', compartment.id = 'y'}`, now need to be rewritten as: 
```
ANY {instance.id = 'x', compartment.id = 'y'}
```

See [Writing Matching Rules to Define Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm#Writing "Matching rules define the resources that belong to a dynamic group.").
## Default Group Names 🔗 
The default names for user groups and administrator groups differ depending on whether they're created in IAM or converted from Identity Cloud Service.
### New OCI Tenancy
When a new OCI tenancy is created, an IAM default domain is created with the following groups:
  * `Administrators`:
    * This group can't be deleted.
    * This group grants full administrative access to the entire tenancy and any child tenancies, along with any secondary IAM identity domains.
  * `All-Domain-Users`:
    * This group can't be deleted.
    * All users are a member of the respective IAM identity domain the group is in.


When a new secondary domain is created, the following groups are added:
  * `Domain_Administrators`:
    * This group can't be deleted.
    * When a user is added to this group, they're automatically added to the Identity Domain Administrator role.
    * Adding a user to the Identity Domain Administrator role doesn't add someone to the `Domain_Administrators` group.
  * `All-Domain-Users`:
    * This group can't be deleted.
    * All users are a member of the respective IAM identity domain the group is in.


### Identity Cloud Service Instance Converted to IAM with Identity Domains
When an Identity Cloud Service instance is converted to IAM with Identity Domains, the groups in the default domain are as follows (when secondary domains are created, the groups are as in the preceding section):
  * `IDCS_Administrators`:
    * This group can't be deleted.
    * This group grants administrative access to just the default domain.
  * `All-Tenant-Users`:
    * This group can't be deleted.
    * All users are a member of the Default identity domain.


### Relationship Between Groups and Roles
This table shows what the user and administrator groups names are for the three different scenarios.
Scenario | User Group Name | Administrator Group Name  
---|---|---  
Creating a tenancy which uses IAM. The default domain uses these names. | `All-Domain-Users` | `Administrators`  
Creating a secondary identity domain in the same tenancy. | `All-Domain-Users` | `Domain_Administrators`  
When an Identity Cloud Service instance has been converted to IAM. | `All-Tenant-Users` | `IDCS_Administrators`  
This diagram shows the relationship between the administrator and user group names and roles.
[![Diagram showing the relationship of groups after conversion](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_conversion_group.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_conversion_group.png)
Was this article helpful?
YesNo

