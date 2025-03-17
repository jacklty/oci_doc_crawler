Updated 2025-01-07
# Creating a Plan Job
Create a plan job in Resource Manager.
Creating (running) a plan job parses your Terraform configuration and converts it into an execution plan for the associated stack. The execution plan lists the sequence of specific actions planned to provision your Oracle Cloud Infrastructure resources, including actions that are expected after running an apply job. We recommend running a plan job (generating an execution plan) before [running an apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager."). The execution plan is handed off to the apply job, which then executes the instructions.
For configurations stored in a source code control system, such as GitHub or GitLab, the job uses the most recent commit. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm)


  *     1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. On the stack's details page, select **Plan**.
    3. (Optional) In the **Plan** panel, edit the default name for the job. Avoid entering confidential information.
    4. To retrieve the latest versions available from the configured source of Terraform providers, select **Show advanced options** and select **Upgrade provider versions**.
The stack must be Terraform 0.14 or later, and if the stack is older, it must be upgraded to [use Terraform Registry](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm#top "Update an older stack to fetch providers from Terraform Registry.").This step is required if provider versions in the Terraform configuration changed since the last time a job was run on the stack. [Dependency lock files](https://developer.hashicorp.com/terraform/language/files/dependency-lock) are automatically managed for new and updated stacks. Providers are updated within the version constraints of the Terraform configuration.
    5. To generate detailed log content for debugging, select **Show advanced options** and select the log level that you want from **Detailed log level**.
For more information, see [Debugging Terraform](https://developer.hashicorp.com/terraform/internals/debugging).
    6. To adjust the maximum number of concurrent operations as [Terraform walks the graph](https://developer.hashicorp.com/terraform/internals/graph#walking-the-graph), select **Show advanced options** and edit the value for **Maximum number of parallel operations**. (Default: `10`.) Use this option to speed up the job.
**Note** A high value might cause throttling of resources. For example, consider a Terraform configuration that defines hundreds of compute instances. An [**Apply**](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") job attempts to create as many instances as possible at the same time. In this example, a value of `100` might cause throttling by the Compute service.
    7. To fetch the latest state before running the job, select **Show advanced options** and select **Refresh resource states before checking for differences**.
Use this option to refresh the state first. For example, consider using this option with an [**Apply**](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") job that you intend to run on manually updated (existing) infrastructure.
**Note** Refreshing the state can affect performance. If the configuration includes several resources, consider not using this option.
    8. (Optional) Add tags:
      1. To show tagging options, select **Show advanced options**.
      2. To add a defined tag, select the namespace and key, then enter a value.
      3. To add a free-form tag, enter a key and value.
    9. Select **Plan**.
The plan job is created. The new job is listed under **Jobs**.
  * Use the `oci resource-manager job create-plan-job[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-plan-job.html)` command and required parameters to run a plan job.
Copy
```
oci resource-manager job create-plan-job [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob) operation to create a plan job.
For an example of the `operation` part of the request, see [CreatePlanJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreatePlanJobOperationDetails).


## What's Next 🔗 
Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm#lifecycle "Review possible lifecycle states for jobs.")) by [getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier."). **Succeeded** (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can [get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.").
Was this article helpful?
YesNo

