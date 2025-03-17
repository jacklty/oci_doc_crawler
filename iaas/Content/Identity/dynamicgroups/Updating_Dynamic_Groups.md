Updated 2023-03-21
# Updating Dynamic Groups
Update dynamic groups.
You can update the matching rules that define the members of a dynamic group. For example, you might change a matching rule that includes all instances in a compartment to exclude a particular instance. Or, you might update a rule to include a new tag value.
**Important**
When you make a change to a matching rule you must allow about one hour for the updated policy to take effect. For example, if you update a rule to include instances with a specific tag in the dynamic group, you must wait about one hour before instances with that tag have the access granted in the policy.
Any policy that references a renamed dynamic group will continue to work. However, Oracle strongly recommends that you update policy statements to stay current with intended dynamic group names or to reference dynamic group OCIDs instead. Also delete any policies with outdated references you no longer need.
Was this article helpful?
YesNo

