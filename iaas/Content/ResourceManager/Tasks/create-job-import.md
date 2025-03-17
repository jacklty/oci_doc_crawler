Updated 2025-01-07
# Creating an Import Job
Create an import job in Resource Manager to import state files for existing resources already managed by Terraform. An import job sets the provided Terraform state file as the current state of the stack.
For example, use an import job to migrate a local Terraform environment to Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm)


  *     1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. Go to **More actions** and select **Import state**.
    3. (Optional) In the **Import** panel, edit the default name for the job. Avoid entering confidential information.
    4. For **Select a Terraform state file to upload** , add the Terraform state file that you want to import into the stack.
You can drag the file onto the control or select **Browse** and navigate to the file location.
    5. To retrieve the latest versions available from the configured source of Terraform providers, select **Show advanced options** and select **Upgrade provider versions**.
The stack must be Terraform 0.14 or later, and if the stack is older, it must be upgraded to [use Terraform Registry](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm#top "Update an older stack to fetch providers from Terraform Registry.").This step is required if provider versions in the Terraform configuration changed since the last time a job was run on the stack. [Dependency lock files](https://developer.hashicorp.com/terraform/language/files/dependency-lock) are automatically managed for new and updated stacks. Providers are updated within the version constraints of the Terraform configuration.
    6. (Optional) Add tags:
      1. To show tagging options, select **Show advanced options**.
      2. To add a defined tag, select the namespace and key, then enter a value.
      3. To add a free-form tag, enter a key and value.
    7. Select **Import**.
The import job is created. The new job is listed under **Jobs**.
  * Use the `oci resource-manager job create-import-tf-state-job[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-import-tf-state-job.html)` command and required parameters to run an import job.
Copy
```
oci resource-manager job create-import-tf-state-job --stack-id <stack_OCID> --tf-state-file <job_details>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob) operation to create an import job.
For an example of the `operation` part of the request, see [CreateImportTfStateJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateImportTfStateJobOperationDetails).


## What's Next 🔗 
After running an import job, get the job's details to check its status. You can optionally view the Terraform state file and view the logs.
Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm#lifecycle "Review possible lifecycle states for jobs.")) by [getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier."). **Succeeded** (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can [get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.").
To view the Terraform state file (shows the state of your resources after running the job), select the name of the job to display the **Job details** page, then select **View state** under **Resources**. Optionally select **Show changes in this version**.
To view the logs for the job, select the job to open its details page, then select **Logs** under **Resources**.
Was this article helpful?
YesNo

