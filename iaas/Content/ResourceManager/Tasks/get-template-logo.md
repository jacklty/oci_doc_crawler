Updated 2024-10-08
# Getting a Private Template's Logo
Get the logo (template icon) for a private template in Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-template-logo.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-template-logo.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-template-logo.htm)


  * On the **Private templates** list page, select the private template that you want to work with. If you need help finding the list page or the private template, see [Listing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#top "List private templates in Resource Manager.").
The private template's details page opens. The logo (template icon) is displayed under **Template icon**.
  * Use the [oci resource-manager template get-template-logo](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/template/get-template-logo.html) command and required parameters to get a private template's logo:
Command
CopyTry It
```
oci resource-manager template get-template-logo --template-id <template_OCID> --file <file_name>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [GetTemplateLogo](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template/GetTemplateLogo) operation to get a logo for a private template.


Was this article helpful?
YesNo

