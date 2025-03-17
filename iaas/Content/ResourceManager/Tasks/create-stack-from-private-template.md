Updated 2025-01-07
# Creating a Stack from a Private Template
Create a stack in Resource Manager from a template. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.
For more information about templates, see [Oracle-Provided Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/templates.htm#top "Review the Oracle-provided templates available for Resource Manager. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.") and [Managing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingprivatetemplates.htm#top "Reuse Terraform configurations using private templates in Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-private-template.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-private-template.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-from-private-template.htm)


  *     1. On the **Private templates** list page, find the private template that you want to work with. If you need help finding the list page or the private template, see [Listing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#top "List private templates in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the private template, select **Create stack from private template**.
The **Create stack** page opens with the private template already selected.
    3. (Optional) To use [custom providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm#top "Update a stack to fetch custom providers from Object Storage buckets."), select **Use custom providers** and then select the bucket that contains the custom provider.
    4. (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
    5. Select the compartment that you want to store the stack in.
    6. For **Terraform version** , select the version used by the Terraform configuration.
    7. (Optional) Add tags:
      1. To show tagging options, select **Show advanced options**.
      2. To add a defined tag, select the namespace and key, then enter a value.
      3. To add a free-form tag, enter a key and value.
    8. Select **Next**.
    9. In the **Configure variables** panel, review the variables listed from the Terraform configuration and change as needed.
**Important** Don't add your private key or other confidential information to configuration variables. 
    10. Select **Next**.
    11. In the **Review** panel, verify the stack configuration.
    12. (Optional) To automatically provision resources on creation of the stack, select **Run apply**.
**Run apply** is selected by default for stacks created from [the Deploy to Oracle Cloud button](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/deploybutton.htm#tocreatestack) or from [Marketplace](https://docs.oracle.com/iaas/Content/Marketplace/Tasks/launch_a_stack.htm).
    13. Select **Create**.
The stack is created and its details page opens.
If you selected **Run apply** , then Resource Manager runs the apply action on the new stack.
  * Use the `oci resource-manager stack create-from-template[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/create-from-template.html)` command and required parameters to create a stack from a template.
Copy
```
oci resource-manager stack create-from-template --compartment-id <compartment_OCID> --template-id <template_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/CreateStack) operation to create a stack from a template.
For an example of the `configSource` part of the request, see [CreateStackTemplateConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateStackTemplateConfigSourceDetails).


Was this article helpful?
YesNo

