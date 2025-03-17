Updated 2025-01-07
# Creating a Plan Rollback Job
Create a plan rollback job in Resource Manager.
Creating (running) a plan rollback job parses the Terraform configuration in the target job and converts it into an execution plan for the associated stack. The execution plan lists the sequence of specific actions planned to rollback your Oracle Cloud Infrastructure resources, including actions that are expected after running an apply rollback job.
We recommend running a plan rollback job (generating an execution plan) before running an [apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm#top "Create an apply rollback job in Resource Manager."), using the following flow.
  1. Identify the successful apply job that you want to roll back to.
The job you want to roll back to is also known as the "target job."
  2. Create a plan rollback job for the target job.
Instructions are on this page.
  3. Confirm that the plan rollback job succeeded.
  4. Confirm that the generated execution plan meets expectations.
  5. [Create an apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm#top "Create an apply rollback job in Resource Manager.") using the generated execution plan (`executionPlanRollbackStrategy`).
The execution plan is handed off to the apply rollback job, which then executes the instructions.


  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm)


  *     1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. In the **Jobs** list, find the apply job that you want to roll back to.
    3. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the job, select **Rollback**.
The **Rollback** panel opens, showing the OCID and name of the selected [apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") (**OCID of target rollback job** and **Name of target rollback job**).
    4. For **Rollback job type** , select **Plan** to create a plan rollback job.
    5. (Optional) Edit the default name for the rollback job. Avoid entering confidential information.
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
    10. Select **Ok**.
The plan rollback job is created. The new job is listed under **Jobs**.
  * Use the `oci resource-manager job create-plan-rollback-job[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/create-plan-rollback-job.html)` command and required parameters to run a plan rollback job.
Copy
```
oci resource-manager job create-plan-rollback-job --stack-id <stack_OCID> --target-rollback-job-id <job_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CreateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CreateJob) operation to create a plan rollback job.
For examples of details for a plan rollback job, see [PlanRollbackJobOperationDetails](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/datatypes/PlanRollbackJobOperationDetails).


## What's Next 🔗 
Monitor the job status ([lifecycle state](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/jobs.htm#lifecycle "Review possible lifecycle states for jobs.")) by [getting the job's details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier."). **Succeeded** (`SUCCEEDED`) indicates that the job has completed. Depending on the complexity of the job, the operation can take some time. While the job runs, or after it finishes, you can [get the job logs content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.").
Was this article helpful?
YesNo

