Updated 2025-01-07
# Creating an Apply Job
Create an apply job in Resource Manager.
When you create (run) an apply job for a stack, Terraform provisions the resources and executes the actions defined in your Terraform configuration, applying the execution plan to the associated stack to create (or modify) your Oracle Cloud Infrastructure resources. We recommend [running a plan job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager.") (generating an execution plan) before running an apply job.
For a walk-through using CLI for cloud provisioning in a CI/CD pipeline, see [IaC in the Cloud: Integrating Terraform and Resource Manager into your CI/CD Pipeline - Building With the OCI CLI](https://blogs.oracle.com/developers/iac-in-the-cloud%3a-integrating-terraform-and-resource-manager-into-your-cicd-pipeline-building-with-the-oci-cli).
For configurations stored in a source code control system, such as GitHub or GitLab, the job uses the most recent commit. The time required to complete an apply job depends on the number and type of cloud resources to be created.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)


  *     1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. On the stack's details page, select **Apply**.
    3. (Optional) In the **Apply** panel, edit the default name for the job. Avoid entering confidential information.
    4. (Optional) For **Apply job plan resolution** , select the name of the latest generated plan job. Only the latest generated plan job is available. If no plan job has been generated for this stack, then only the default value is available (**Automatically approve**). For more information about **Automatically approve** , see [Auto-Approve Option for Terraform Apply Command](https://developer.hashicorp.com/terraform/cli/commands/apply#auto-approve).
    5. To retrieve the latest versions available from the configured source of Terraform providers, select **Show advanced options** and select **Upgrade provider versions**.
The stack must be Terraform 0.14 or later, and if the stack is older, it must be upgraded to [use Terraform Registry](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack-tf-reg.htm#top "Update an older stack to fetch providers from Terraform Registry.").This step is required if provider versions in the Terraform configuration changed since the last time a job was run on the stack. [Dependency lock files](https://developer.hashicorp.com/terraform/language/files/dependency-lock) are automatically managed for new and updated stacks. Providers are updated within the version constraints of the Terraform configuration.
    6. To generate detailed log content for debugging, select **Show advanced options** and select the log level that you want from **Detailed log level**.
For more information, see [Debugging Terraform](https://developer.hashicorp.com/terraform/internals/debugging).
    7. To adjust the maximum number of concurrent operations as [Terraform walks the graph](https://developer.hashicorp.com/terraform/internals/graph#walking-the-graph), select **Show advanced options** and edit the value for **Maximum number of parallel operations**. (Default: `10`.) Use this option to speed up the job.
**Note** A high value might cause throttling of resources. For example, consider a Terraform configuration that defines hundreds of compute instances. An [**Apply**](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") job attempts to create as many instances as possible at the same time. In this example, a value of `100` might cause throttling by the Compute service.
    8. To fetch the latest state before running the job, select **Show advanced options** and select **Refresh resource states before checking for differences**.
Use this option to refresh the state first. For example, consider using this option with an [**Apply**](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") job that you intend to run on manually updated (existing) infrastructure.
**Note** Refreshing the state can affect performance. If the configuration includes several resources, consider not using this option.
    9. (Optional) Add tags:
      1. To show tagging options, select **Show advanced options**.
      2. To add a defined tag, select the namespace and key, then enter a value.
      3. To add a free-form tag, enter a key and value.
    10. Select **Apply**.
The apply job is created. The new job is listed under **Jobs**.
  * Use the `oci resource-manager job create-apply-job[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-apply-job.html)` command and required parameters to run an apply job.
Copy
```
oci resource-manager job create-apply-job [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
[Examples](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm)
Example 1: Reference a plan job.
Copy
```
oci resource-manager job create-apply-job --execution-plan-strategy <plan_job_ocid> --stack-id <stack_ocid>
```

Example 2: Automatically approve (don't reference a plan job).
Copy
```
oci resource-manager job create-apply-job --execution-plan-strategy AUTO_APPROVED --stack-id <stack_ocid>
```

  * Use the [CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob) operation to create an apply job.
For an example of the `operation` part of the request, see [CreateApplyJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/CreateApplyJobOperationDetails).


## What's Next 🔗 
Depending on the number and type of resources specified, a given apply job can take some time.
After running an apply job, get the job's details to check its status. You can optionally view the Terraform state file, view the logs, and confirm existence of provisioned resources.
Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm#lifecycle "Review possible lifecycle states for jobs.")) by [getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier."). **Succeeded** (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can [get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.").
To view the Terraform state file (shows the state of your resources after running the job), select the name of the job to display the **Job details** page, then select **View state** under **Resources**. Optionally select **Show changes in this version**.
To view the logs for the job, select the job to open its details page, then select **Logs** under **Resources**.
To confirm existence of newly provisioned resources, [inspect resources in the compartment](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/inspect-resources.htm#top "Inspecting resources in a compartment allows you to confirm existence of a resource that you provisioned \(by running an apply job\) or absence of a resource that you released \(by running a destroy job\)."). 
Was this article helpful?
YesNo

