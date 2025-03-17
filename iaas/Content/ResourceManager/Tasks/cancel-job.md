Updated 2024-10-08
# Canceling a Job
Cancel a running job in Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm)


  * These steps show how to cancel a job in a compartment. You can also cancel a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
    1. On the **Jobs** list page, find the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the job, select **Cancel**.
The **Cancel job** dialog box opens.
    3. If the job is for [**Import state**](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-import.htm#top "Create an import job in Resource Manager to import state files for existing resources already managed by Terraform. An import job sets the provided Terraform state file as the current state of the stack."), [**Apply**](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager."), or [**Destroy**](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-destroy.htm#top "Create a destroy job in Resource Manager to release \(tear down\) resources associated with a stack and clean up the tenancy. Released resources are eventually deleted by the related OCI service. For example, a released compute instance is eventually deleted by the OCI Compute service."), then select the option that you want:
       * **Cancel job** : Resource Manager attempts to cancel the job gracefully. Internally, the running Terraform process signals the child processes to end. The job might run partially, depending on the responses of the child processes, even though the ultimate job status is **Canceled**.
       * **Force the job to cancel now** : Forces the job to cancel.
**Note** Forcing a job to cancel might cause a mismatch between the state file and the actual resource states.
    4. Select **Yes, cancel job**.
  * Use the `oci resource-manager job cancel[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/cancel.html)` command and required parameters to cancel a job.
Command
CopyTry It
```
oci resource-manager job cancel --job-id <job_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [CancelJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/CancelJob) operation to cancel a job.


Was this article helpful?
YesNo

