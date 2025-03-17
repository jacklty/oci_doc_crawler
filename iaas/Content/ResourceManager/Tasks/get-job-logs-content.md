Updated 2024-10-08
# Getting Logs Content for a Job
Download console logs (raw `.txt` job logs content) for a job in Resource Manager.
**Note** To prevent errors caused by unavailable files, wait a second after the job finishes to download the job information. An error appears if the job information doesn't exist yet. For example, a `409` error appears if you attempt to download the Terraform configuration immediately after running a job. In this case, the Terraform configuration is still being copied to a location using a background process. The Terraform configuration is available about a second after the job finishes.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm)


  * These steps show how to get logs content for a job in a compartment. You can also get logs content for a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
    1. On the **Jobs** list page, select the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. On the job's details page, select **Logs**.
    3. Select **Download logs**.
  * Use the `oci resource-manager job get-job-logs-content[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-logs-content.html)` command and required parameters to get logs content for a job.
Command
CopyTry It
```
oci resource-manager job get-job-logs-content [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [GetJobLogsContent](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/GetJobLogsContent) operation to get logs content for a job.


Was this article helpful?
YesNo

