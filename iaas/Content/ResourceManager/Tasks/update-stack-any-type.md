Updated 2024-10-08
# Updating a Stack (Any Type)
Update a stack in Resource Manager. This page provides the basic steps for updating a stack.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-any-type.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-any-type.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-any-type.htm)


  *     1. On the **Stacks** list page, find the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the stack, select **Edit**.
    3. On the **Edit stack** page, update the values you want.
For example, upload a different [Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model."), or update the stack name or description. For information about the fields, see [Creating a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm#top "Create a stack in Resource Manager. You can optionally postpone variables and other stack settings until after the stack is created.").
    4. Select **Next**.
    5. In the **Configure variables** panel, update variable values as needed.
    6. Select **Next**.
    7. In the **Review** panel, verify the stack configuration.
    8. To automatically provision resources on creation of the stack, select **Run apply**.
    9. Select **Save changes**.
The **Stack details** page opens.
If **Run apply** was selected, then Resource Manager runs the apply action on the updated stack.
  * Use the `oci resource-manager stack update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update.html)` command and required parameters to update a stack.
Copy
```
oci resource-manager stack update --stack-id <stack_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack) operation to update a stack.


Was this article helpful?
YesNo

