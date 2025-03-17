Updated 2024-10-08
# Listing a Stack's Resources
List stack resources in Resource Manager. Stack resources are infrastructure objects such as virtual networks and compute instances that were provisioned by the stack.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stack-resources.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stack-resources.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stack-resources.htm)


  *     1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. On the stack's details page, select **Stack resources**.
    3. To view a resource's attributes, select **Show**.
  * Use the `oci resource-manager associated-resource-summary list-stack-associated-resources[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/associated-resource-summary/list-stack-associated-resources.html)` command and required parameters to list stack resources.
Copy
```
oci resource-manager associated-resource-summary list-stack-associated-resources --stack-id <stack_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [ListStackAssociatedResources](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/AssociatedResourceSummary/ListStackAssociatedResources) operation to list stack resources.


Was this article helpful?
YesNo

