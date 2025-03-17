Updated 2024-10-08
# Listing Job Outputs
List outputs from a completed apply or apply rollback job in Resource Manager. Job outputs are generated from output variables in the job's associated Terraform configuration.
For information about output variables in Terraform configurations, see [Output Configuration](https://docs.oracle.com/iaas/Content/dev/terraform/authoring-configs.htm#output-config).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-outputs.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-outputs.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-job-outputs.htm)


  * These steps show how to list outputs for a job in a compartment. You can also list outputs for a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
    1. On the **Jobs** list page, select the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. On the job's details page, select **Outputs**.
Don't see **Outputs**? Check that the job has finished running, and that it's either an [apply job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply.htm#top "Create an apply job in Resource Manager.") or an [apply rollback job](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job-apply-rollback.htm#top "Create an apply rollback job in Resource Manager."). Outputs are generated at the same time as the job's [state file](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-state.htm#top "Download the Terraform state file \(.json\) from a completed apply, apply rollback, or import job in Resource Manager."). No outputs are available for [canceled](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/cancel-job.htm#top "Cancel a running job in Resource Manager.") jobs.
  * Use the `oci resource-manager job-output-summary list-job-outputs[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job-output-summary/list-job-outputs.html)` command and required parameters to list job outputs.
Copy
```
oci resource-manager job-output-summary list-job-outputs --job-id <job_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [ListJobOutputs](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/JobOutputSummary/ListJobOutputs) operation to list job outputs.


Was this article helpful?
YesNo

