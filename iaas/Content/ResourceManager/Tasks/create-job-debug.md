Updated 2024-10-08
# Debugging a Job by Generating Detailed Log Content
Debug a job by generating detailed log content. Detailed log content is generated for a job when you specify the verbosity to use, such as `ERROR`. By default, no detailed log content is generated (null or **None**).
For more information, see [Debugging Terraform](https://developer.hashicorp.com/terraform/internals/debugging).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-debug.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-debug.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-debug.htm)


  * These steps show how to debug a job in a stack. You can also retrieve the latest providers for a job [in a compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. Select the option for running the [type of job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job.htm#top "Create a job in Resource Manager, such as plan, apply, or destroy.") that you want.
    3. In the panel for the job type that you selected, select **Show advanced options** and select a value for **Detailed log level**.
    4. Run the [job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job.htm#top "Create a job in Resource Manager, such as plan, apply, or destroy.").
  * Use the command and required parameters for the type of job you want to run, and specify verbosity in JSON input for `--terraform-advanced-options` to generate Terraform detailed log content for the job.
Copy
```
oci resource-manager job <command> --stack-id <stack_ocid> --terraform-advanced-options <json_input>
```

For example, to generate Terraform detailed log content at the debug verbosity level when running a plan job, use the `oci resource-manager job create-plan-job[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-plan-job.html)` command, with the following JSON input for `--terraform-advanced-options`.
Copy
```
oci resource-manager job create-plan-job --stack-id <stack_ocid> --terraform-advanced-options '{"detailedLogLevel": "DEBUG", "parallelism": 20, "isRefreshRequired": true}'
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob) operation to generate Terraform detailed log content when running a job.
When defining `jobOperationDetails` ([CreateJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateJobOperationDetails) in [CreateJobDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateJobDetails), specify the `detailedLogLevel` attribute (severity) in [TerraformAdvancedOptions](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/TerraformAdvancedOptions).


Was this article helpful?
YesNo

