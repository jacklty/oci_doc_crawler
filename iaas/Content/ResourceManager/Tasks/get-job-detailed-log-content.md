Updated 2024-10-08
# Getting Detailed Log Content for a Job
Download detailed log content (a `.log` file) for a job in Resource Manager.
**Note** To prevent errors caused by unavailable files, wait a second after the job finishes to download the job information. An error appears if the job information doesn't exist yet. For example, a `409` error appears if you attempt to download the Terraform configuration immediately after running a job. In this case, the Terraform configuration is still being copied to a location using a background process. The Terraform configuration is available about a second after the job finishes.
For more information about detailed log levels and generating detailed log content, see [Debugging Terraform](https://developer.hashicorp.com/terraform/internals/debugging).
## Before You Begin 🔗 
Before you can get detailed log content for a job, detailed log content must exist. For instructions on generating detailed log content for a job, see [Debugging a Job by Generating Detailed Log Content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-debug.htm#top "Debug a job by generating detailed log content. Detailed log content is generated for a job when you specify the verbosity to use, such as ERROR. By default, no detailed log content is generated \(null or None\)."). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-detailed-log-content.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-detailed-log-content.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-detailed-log-content.htm)


  * These steps show how to get detailed log content for a job in a compartment. You can also get detailed log content for a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
    1. On the **Jobs** list page, select the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. Next to **Detailed log level** , select **Download detailed log file**.
  * Use the `oci resource-manager job get-detailed-log-content[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-detailed-log-content.html)` command and required parameters to get detailed log content for a job.
Command
CopyTry It
```
oci resource-manager job get-detailed-log-content --job-id <job_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [GetJobDetailedLogContent](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/GetJobDetailedLogContent) operation to get detailed log content for a job.


Was this article helpful?
YesNo

