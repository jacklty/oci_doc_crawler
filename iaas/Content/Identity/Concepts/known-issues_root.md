Updated 2024-12-18
# Known Issues for IAM without Identity Domains
Known issues have been identified in IAM without Identity Domains.
  * [Permissions granted through policies that specify groups or dynamic groups by name persist through name changes](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/known-issues_root.htm#knownissues_topic_Permissions_granted_by_policy_group_name_persist_through_name_changes)
  * [New permissions in resource-types are not propagated](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/known-issues_root.htm#new-permissions-in-family)
  * [Deleted compartments continue to count against service limits](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/known-issues_root.htm#iamdelComp)


## Permissions granted through policies that specify groups or dynamic groups by name persist through name changes 🔗  

Details
    Policy statements that reference a group or dynamic group by name remain valid even through changes to the group or dynamic group name. Any access granted to the group or dynamic group by its previous name persists. The policy continues to grant the members of the group or dynamic group access to resources without any changes to the policy statement itself. This happens because IAM applies the policy to the subject OCID rather than its name. 

Workaround
    Oracle strongly recommends that you update policy statements to stay current with intended group or dynamic group names or to reference subject OCIDs instead. Also delete any policy statements with outdated references that you no longer need.
## New permissions in resource-types are not propagated 🔗  

Details
    When a new permission is added to an existing resource-type, the permission is not propagated to any policies that include the resource-type. This happens because IAM does not recompile a policy unless there is a change to the policy statement. 

Workaround
    For any existing policies that use resource-types, when new permissions are added to the resource-type, edit the policy by adding a blank space. Then, save the policy.
## Deleted compartments continue to count against service limits 🔗  

Details
    Deleted compartments continue to count against the compartment service limit for your tenancy. A deleted compartment is removed from the count after 90 days. This is also the setting that specifies the time period for deleted compartments to remain displayed in the Console. 

Workaround
    Until this issue is resolved, you can request to have your service limit increased for compartments. See [Requesting a Service Limit Increase](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#Requesti).
Was this article helpful?
YesNo

