Updated 2024-10-08
# Getting a Job's Terraform Configuration
Download the Terraform configuration (`.zip` file) for a job in Resource Manager.
**Note** To prevent errors caused by unavailable files, wait a second after the job finishes to download the job information. An error appears if the job information doesn't exist yet. For example, a `409` error appears if you attempt to download the Terraform configuration immediately after running a job. In this case, the Terraform configuration is still being copied to a location using a background process. The Terraform configuration is available about a second after the job finishes.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-config.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-config.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-config.htm)


  * These steps show how to get the Terraform configuration for a job in a compartment. You can also get the Terraform configuration for a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
**Tip** As an alternative to these steps, edit the generated Terraform configuration file in Code Editor. For more information, see [Editing a Configuration Using Code Editor](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/code-editor.htm#top "Use Code Editor to edit the Terraform configuration associated with a stack in Resource Manager.").
    1. On the **Jobs** list page, find the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the job, select **Download Terraform configuration**.
  * Use the `oci resource-manager job get-job-tf-config[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-tf-config.html)` command and required parameters to get a job's Terraform configuration file.
Command
CopyTry It
```
oci resource-manager stack get-job-tf-config [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [GetJobTfConfig](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/GetJobTfConfig) operation to get a job's Terraform configuration file.


Was this article helpful?
YesNo

