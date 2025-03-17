Updated 2025-01-07
# Deleting a Stack
Delete a stack in Resource Manager. You can't undo the deletion of a stack.
**Important** When you delete a stack, its associated resources persist but its associated state file is deleted. Cleaning up the resources associated with a deleted stack can be difficult without the state file, especially when those resources are spread across multiple compartments. To avoid difficult cleanup, we recommend that you release associated resources first by [running a destroy job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#top "Create a destroy job in Resource Manager to release \(tear down\) resources associated with a stack and clean up the tenancy. Released resources are eventually deleted by the related OCI service. For example, a released compute instance is eventually deleted by the OCI Compute service."). If the stack has no associated resources, then you can safely delete it without concern about missing state files.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-stack.htm)


  *     1. On the **Stacks** list page, find the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the stack, select **Delete**.
    3. When prompted, confirm the deletion.
  * Use the `oci resource-manager stack delete[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/delete.html)` command and required parameters to delete a stack.
Command
CopyTry It
```
oci resource-manager stack delete stack-id <stack_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [DeleteStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/DeleteStack) operation to delete a stack.


Was this article helpful?
YesNo

