Updated 2024-10-08
# Updating a Stack's Terraform Configuration (Zip File or Folder)
Update the zip file or folder Terraform configuration used by a stack in Resource Manager. The updated configuration is used when you run jobs on the stack. A folder-based update is available using the Console only.
## Before You Begin 🔗 
Review prerequisites for updating the Terraform configuration used by a stack in Resource Manager.
**Important** If you're uploading a different Terraform configuration, ensure that the configuration file is valid. See [Authoring Configurations](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/authoring-configurations.htm#top "Write a Terraform configuration to describe infrastructure using the HashiCorp Configuration Language format \(HCL\).") and [Terraform Configurations for Resource Manager](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.").
Ensure that you have your revised [Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.") (`.zip` file or folder) ready for upload. No configuration file is available for download until a job is successfully run on the stack. To edit a Terraform configuration that was generated from a [template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/templates.htm#top "Review the Oracle-provided templates available for Resource Manager. A template is a prebuilt Terraform configuration for deploying cloud resources in a common scenario.") or existing compartment using [resource discovery](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resource-discovery.htm#top "Discover already deployed Oracle Cloud Infrastructure resources using Resource Manager."), first [download the configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm#top "Download the Terraform configuration used by a stack in Resource Manager. The Terraform configuration file for a stack is the one associated with the most recent successful job."). Then use the edited configuration `.zip` file for the update.
If the stack's configuration is stored in Git or a bucket, then upload the configuration there.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-config.htm)


  * **Tip** As an alternative to these steps, edit the generated Terraform configuration file in Code Editor. For more information, see [Editing a Configuration Using Code Editor](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/code-editor.htm#top "Use Code Editor to edit the Terraform configuration associated with a stack in Resource Manager.").
After completing all the prerequisites, follow these steps in the Console to update a stack's Terraform configuration from a zip file or folder.
    1. On the **Stacks** list page, find the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the stack, select **Edit**.
    3. On the **Edit stack** page, select **Folder** or **.Zip file** and add the revised [Terraform configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/terraformconfigresourcemanager.htm#top "Review requirements and recommendations for Terraform configurations used with Resource Manager. Use Terraform and Resource Manager to install, configure, and manage resources using the infrastructure-as-code model.").
You can either drag the file onto the dialog's control or select **Browse** and navigate to the location of the file or folder.
    4. (Optional) Update other values as needed.
For example, update the stack name or description. For information about the fields, see [Creating a Stack from a Zip File](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-local.htm#top "Create a stack in Resource Manager from a local Terraform configuration stored in a zip file.").
    5. Select **Next**.
    6. In the **Configure variables** panel, update variable values as needed.
    7. Select **Next**.
    8. In the **Review** panel, verify the stack configuration.
    9. To automatically provision resources on creation of the stack, select **Run apply**.
    10. Select **Save changes**.
The **Stack details** page opens.
If **Run apply** was selected, then Resource Manager runs the apply action on the updated stack.
  * Use the `oci resource-manager stack update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/update.html)` command and required parameters to update the Terraform configuration zip file used by a stack.
Copy
```
oci resource-manager stack update --config-source <file-path> [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateStack](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/UpdateStack) operation to update the Terraform configuration zip file used by a stack.
For an example of the `configSource` part of the request, see [UpdateZipUploadConfigSourceDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/UpdateZipUploadConfigSourceDetails).


Was this article helpful?
YesNo

