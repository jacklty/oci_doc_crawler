Updated 2024-10-08
# Tagging a Stack
Add tag metadata to a stack in Resource Manager. Tags are key-value pairs that you attach to resources to help you organize and track the resources across compartments.
**Note** This page describes how to tag an existing stack. You can also tag a stack when you [create it](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm#top "Create a stack in Resource Manager. You can optionally postpone variables and other stack settings until after the stack is created.").
If you have permissions to create a resource, you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tags.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tags.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tags.htm)


  *     1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. To add a tag, go to **More actions** , select **Add tags** , and enter the tag namespace, key, and value.
    3. To view existing tags, select the **Tags** tab and then select **Defined tags** or **Free-form tags**.
    4. To edit an existing tag, select the edit icon, update the value in the **Edit tag** dialog box, and then select **Save**.
    5. To remove a tag, select the edit icon and then select **Remove tag**.
  * Use the `oci resource-manager stack update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update.html)` command and required parameters to tag a stack.
Copy
```
oci resource-manager stack update [--defined-tags | --freeform-tags] <tags> [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack) operation to tag a stack.


Was this article helpful?
YesNo

