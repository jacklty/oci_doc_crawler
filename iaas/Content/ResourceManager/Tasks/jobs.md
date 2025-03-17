Updated 2023-06-27
# Managing Jobs
Manage jobs in Resource Manager.
**Note** For descriptions of job types, lifecycle states, and the default retry policy, see [job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#concepts__jobdefinition) in the overview page.
## Required IAM Policy 🔗 
Use policies to grant access to jobs in Resource Manager.
To manage jobs, you must be given the required type of access in a **policy** written by an administrator, whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/policiesgs/get-started-with-policies.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/policiescommon/commonpolicies.htm).
Administrators: For common policies that give groups access to jobs in Resource Manager, see [Manage Stacks and Jobs (Securing Resource Manager)](https://docs.oracle.com/iaas/Content/Security/Reference/resourcemanager_security.htm#iam-policies__stacks-jobs).
## Tasks 🔗 
You can perform the following job management tasks:
  * [Creating a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job.htm#top "Create a job in Resource Manager, such as plan, apply, or destroy.")
    * [Creating a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan.htm#top "Create a plan job in Resource Manager.")
    * [Creating a Plan Rollback Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-plan-rollback.htm#top "Create a plan rollback job in Resource Manager.")
    * [Creating an Apply Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.")
    * [Creating an Apply Rollback Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm#top "Create an apply rollback job in Resource Manager.")
    * [Creating an Import Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm#top "Create an import job in Resource Manager to import state files for existing resources already managed by Terraform. An import job sets the provided Terraform state file as the current state of the stack.")
    * [Creating a Destroy Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#top "Create a destroy job in Resource Manager to release \(tear down\) resources associated with a stack and clean up the tenancy. Released resources are eventually deleted by the related OCI service. For example, a released compute instance is eventually deleted by the OCI Compute service.")
    * [Bulk Destroying Resources and Deleting Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/bulk-destroy-delete2.htm#bulk-destroy-delete2 "For the specified compartment, use the following script to delete all the stacks in Resource Manager and destroy all the resources associated with the corresponding stacks.")
  * [Retrieving the Latest Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-lock-file.htm#top "Within the version constraints of the Terraform configuration, retrieve the latest versions available from the configured source of Terraform providers when running a job. You can retrieve the latest providers when running the following types of jobs: plan, apply, destroy, import state, and run drift detection.")
  * [Debugging a Job by Generating Detailed Log Content](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-debug.htm#top "Debug a job by generating detailed log content. Detailed log content is generated for a job when you specify the verbosity to use, such as ERROR. By default, no detailed log content is generated \(null or None\).")
  * [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.")
  * [Getting a Job's Details](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm#top "Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier.")
  * [Listing Job Resources](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-resources.htm#top "List job resources in Resource Manager for a completed apply or apply rollback job. Job resources are infrastructure objects such as virtual networks and compute instances that were provisioned by the job.")
  * [Listing Job Outputs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-outputs.htm#top "List outputs from a completed apply or apply rollback job in Resource Manager. Job outputs are generated from output variables in the job's associated Terraform configuration.")
  * [Getting Detailed Log Content for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-detailed-log-content.htm#top "Download detailed log content \(a .log file\) for a job in Resource Manager.")
  * [Getting Logs for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs.htm#top "View console logs for a job in Resource Manager.")
  * [Getting Logs Content for a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-logs-content.htm#top "Download console logs \(raw .txt job logs content\) for a job in Resource Manager.")
  * [Getting a Job's Terraform Configuration](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-config.htm#top "Download the Terraform configuration \(.zip file\) for a job in Resource Manager.")
  * [Getting the Terraform Output for a Plan Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm#top "Download the output of a plan job in Resource Manager.")
  * [Getting a Job's State File](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm#top "Download the Terraform state file \(.json\) from a completed apply, apply rollback, or import job in Resource Manager.")
  * [Updating a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job.htm#top "Update a job's name or tags in Resource Manager.")
  * [Tagging a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job-tags.htm#top "Add tag metadata to a job in Resource Manager. Tags are key-value pairs that you attach to resources to help you organize and track the resources across compartments.")
  * [Canceling a Job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm#top "Cancel a running job in Resource Manager.")


## Lifecycle States 🔗 
Review possible lifecycle states for jobs.
  * **Accepted** (`ACCEPTED`): The job was accepted for processing.
  * **In progress** (`IN_PROGRESS`): The job is running (executing).
  * **Failed** (`FAILED`): The job did not complete execution.
  * **Succeeded** (`SUCCEEDED`): The job has completed successfully.
  * **Canceling** (`CANCELING`): The job is being canceled; a notification has been sent, but the job has not yet stopped running.
  * **Canceled** (`CANCELED`): The job was canceled and has stopped running.


Was this article helpful?
YesNo

