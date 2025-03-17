Updated 2024-09-26
# Policies and Service Updates
The definition of a verb or resource-type might change after a service update.
If a verb or resource type changes after a service update, then existing policy statements are supported. For example, let's say that the family resource-type `virtual-network-family` changes to include a new kind of resource that adds to Networking. By default, policies automatically stay current with any changes in service definition, so any policy you have that gives access to `virtual-network-family` automatically includes access to the newly added resource.
**Important** If a service introduces new permissions for an existing resource type, you must update the policy statement for the existing resource type to make the new permissions take effect. For more information, see [New permissions in resource-types are not propagated](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/known-issues_root.htm#new-permissions-in-family) for more information.
Was this article helpful?
YesNo

