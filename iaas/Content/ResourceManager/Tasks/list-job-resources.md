Updated 2024-10-08
# Listing Job Resources
List job resources in Resource Manager for a completed apply or apply rollback job. Job resources are infrastructure objects such as virtual networks and compute instances that were provisioned by the job.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-resources.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-resources.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-resources.htm)


  * These steps show how to list resources for a job in a compartment. You can also list resources for a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
    1. On the **Jobs** list page, select the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. On the job's details page, select **Job resources**.
Don't see **Job resources**? Check that the job has finished running, and that it's either an [apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") or an [apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm#top "Create an apply rollback job in Resource Manager."). No job resources are available for [canceled](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm#top "Cancel a running job in Resource Manager.") jobs.
  * Use the `oci resource-manager associated-resource-summary list-job-associated-resources[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/associated-resource-summary/list-job-associated-resources.html)` command and required parameters to list job resources.
Copy
```
oci resource-manager associated-resource-summary list-job-associated-resources --job-id <job_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [ListJobAssociatedResources](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/AssociatedResourceSummary/ListJobAssociatedResources) operation to list job resources.


Was this article helpful?
YesNo

