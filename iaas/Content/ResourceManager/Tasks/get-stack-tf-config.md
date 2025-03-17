Updated 2024-10-08
# Getting a Stack's Terraform Configuration
Download the Terraform configuration used by a stack in Resource Manager. The Terraform configuration file for a stack is the one associated with the most recent successful job.
**Note** For stacks created from [Terraform configurations in Git](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-stack-git.htm#top "Create a stack in Resource Manager from a Terraform configuration stored in Git. Select a configuration source provider that specifies the Git information needed to access the configurations."), configuration files aren't available for download until a [job is successfully run](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job.htm#top "Create a job in Resource Manager, such as plan, apply, or destroy.") on the stack.
Alternatively, you can view the generated Terraform configuration file in Code Editor. For more information, see [Editing a Configuration Using Code Editor](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/code-editor.htm#top "Use Code Editor to edit the Terraform configuration associated with a stack in Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack-tf-config.htm)


  *     1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. Next to **Terraform configuration** , select **Download**.
  * Use the `oci resource-manager stack get-stack-tf-config[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/get-stack-tf-config.html)` command and required parameters to get a stack's Terraform configuration file.
Command
CopyTry It
```
oci resource-manager stack get-stack-tf-config --stack-id <stack_OCID> --file-id <file_name>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [GetStackTfConfig](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/GetStackTfConfig) operation to get a stack's Terraform configuration file.


Was this article helpful?
YesNo

