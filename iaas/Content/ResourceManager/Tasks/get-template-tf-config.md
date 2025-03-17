Updated 2024-10-08
# Getting a Private Template's Terraform Configuration
Get the Terraform configuration for a private template in Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-template-tf-config.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-template-tf-config.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-template-tf-config.htm)


  *     1. On the **Private templates** list page, select the private template that you want to work with. If you need help finding the list page or the private template, see [Listing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#top "List private templates in Resource Manager.").
    2. Next to **Terraform configuration** , select **Download**.
  * Use the [oci resource-manager template get-template-tf-config](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/template/get-template-tf-config.html) command and required parameters to get the Terraform configuration for a private template:
Command
CopyTry It
```
oci resource-manager template get-template-tf-config --template-id <template_OCID> --file <file_name>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [GetTemplateTfConfig](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template/GetTemplateTfConfig) operation to get the Terraform configuration for a private template.


Was this article helpful?
YesNo

