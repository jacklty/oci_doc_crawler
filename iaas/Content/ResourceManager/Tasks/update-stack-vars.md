Updated 2024-10-08
# Updating Variables for a Stack
Update the variable values used by a stack in Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-vars.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-vars.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-vars.htm)


  *     1. On the **Stacks** list page, find the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the stack, select **Edit**.
    3. On the **Edit stack** panel, select **Configure variables**.
    4. Change the variable values that you want.
    5. Select **Next**.
    6. In the **Review** panel, verify the stack configuration.
    7. Select **Save changes**.
  * Use the `oci resource-manager stack update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update.html)` command and required parameters to update the variable values used by a stack.
Copy
```
oci resource-manager stack update --variables <json_input> [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack) operation to update the variable values used by a stack.
When defining details for [UpdateStackDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateStackDetails), provide the updated variable values using the `variables` attribute.


Was this article helpful?
YesNo

