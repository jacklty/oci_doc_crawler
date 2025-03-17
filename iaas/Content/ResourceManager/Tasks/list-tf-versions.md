Updated 2024-10-08
# Listing Terraform Versions
List versions of Terraform supported by Resource Manager.
For information about supported Terraform versions, see [Supported Terraform Versions](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Reference/terraformversions.htm#top "Review the Terraform versions supported by the Resource Manager service.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-tf-versions.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-tf-versions.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-tf-versions.htm)


  * Begin the stack creation process to view the list of Terraform versions.
    1. On the **Stacks** list page, select **Create stack**. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/list-stacks.htm).
    2. Under **Terraform version** , expand the list.
    3. (Optional) To finish creating a stack, provide values for other fields and select **Create**.
For information about the fields, see [Creating a Stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack.htm#top "Create a stack in Resource Manager. You can optionally postpone variables and other stack settings until after the stack is created.").
  * Use the `oci resource-manager stack list-terraform-versions[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/list-terraform-versions.html)` command and required parameters to list Terraform versions.
Copy
```
oci resource-manager stack list-terraform-versions [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [ListTerraformVersions](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/ListTerraformVersions) operation to list Terraform versions.


Was this article helpful?
YesNo

