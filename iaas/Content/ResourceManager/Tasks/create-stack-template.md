Updated 2025-01-07
# Creating a Stack from a Template
Create a stack in Resource Manager from a template. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.
For more information about templates, see [Oracle-Provided Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/templates.htm#top "Review the Oracle-provided templates available for Resource Manager. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.") and [Managing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingprivatetemplates.htm#top "Reuse Terraform configurations using private templates in Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-template.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-template.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-template.htm)


  *     1. On the **Stacks** list page, select **Create stack**. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
    2. On the **Create stack** page, under **Choose the origin of the Terraform configuration** , select **Template**.
    3. Under **Stack configuration** , select **Select template**.
    4. In the **Browse templates** panel, select the template you want and then select **Select template**.
[Private templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/managingprivatetemplates.htm#top "Reuse Terraform configurations using private templates in Resource Manager.") are under the **Private** tab.
The page is populated with information contained in the Terraform configuration.
    5. (Optional) To use [custom providers](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/update-stack-custom-providers.htm), select **Use custom providers** and then select the bucket that contains the custom provider.
    6. (Optional) Edit the default stack name and enter a stack description. Avoid entering confidential information.
    7. Select the compartment that you want to store the stack in.
    8. To add a defined tag, select the namespace and key, then enter a value.
    9. To add a free-form tag, enter a key and value.
    10. Select **Next**.
    11. In the **Configure variables** panel, review the variables listed from the Terraform configuration and change as needed.
**Important** Don't add your private key or other confidential information to configuration variables. 
    12. Select **Next**.
    13. In the **Review** panel, verify the stack configuration.
    14. (Optional) To automatically provision resources on creation of the stack, select **Run apply**.
    15. Select **Create**.
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

