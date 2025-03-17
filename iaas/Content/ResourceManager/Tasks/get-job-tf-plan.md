Updated 2024-10-08
# Getting the Terraform Output for a Plan Job
Download the output of a plan job in Resource Manager.
**Note** To prevent errors caused by unavailable files, wait a second after the job finishes to download the job information. An error appears if the job information doesn't exist yet. For example, a `409` error appears if you attempt to download the Terraform configuration immediately after running a job. In this case, the Terraform configuration is still being copied to a location using a background process. The Terraform configuration is available about a second after the job finishes.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm)


  * These steps show how to get plan output for a job in a compartment. You can also get plan output for a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
    1. On the **Jobs** list page, select the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. Select **Download Terraform plan** and then select the file format option you want (binary or JSON file).
  * Use the `oci resource-manager job get-job-tf-plan[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get-job-tf-plan.html)` command and required parameters to get the output of a plan job.
Command
CopyTry It
```
oci resource-manager stack get-job-tf-plan --job-id <job_OCID> --file-id <file_name>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
[Example Request](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job-tf-plan.htm)
Example to get the output of a plan job in JSON format:
Command
CopyTry It
```
oci resource-manager job get-job-tf-plan --job-id ocid1.ormjob.oc1.phx.<uniqueid> --file tfplan.json --tf-plan-format JSON
```

  * Use the [GetJobTfPlan](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/GetJobTfPlan) operation to get the output of a plan job.


Was this article helpful?
YesNo

