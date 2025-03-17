Updated 2025-01-23
# Getting a Job's Details
Get the details of a job in Resource Manager. You can view name, type, status, and other key information about jobs for a specific compartment or stack. For configurations stored in Git, job details include the relevant commit identifier.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm)


  * These steps show how to get a job in a compartment. You can also get a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
On the **Jobs** list page, select the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
The details page opens and displays information about the job. Access the various resources associated with the job by selecting their links or tabs.
  * Use the `oci resource-manager job get[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/get.html)` command and required parameters to get a job.
Command
CopyTry It
```
oci resource-manager job get --job-id <job_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [GetJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/GetJob) operation to get a job.
[Example Response](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-job.htm)
This example shows `ACCEPTED` for `lifecycle-state`. 
```
{
 "data": 
 {
  "compartment-id": " ocid1.compartment.oc1..uniqueid",
  "defined-tags": null,
  "display-name": "Example Plan Job",
  "freeform-tags": {},
  "id": "ocid1.ormjob.oc1..uniqueid",
  "lifecycle-state": "ACCEPTED",
  "operation": "PLAN",
  "jobOperationDetails": 
  {
   "operation": "PLAN"
  },
  "stack-id": " ocid1.ormstack.oc1..uniqueid",
  "time-created": "2019-03-09T20:52:13.922000+00:00",
  "time-finished": null,
  "variables": 
  {
   "compartment_ocid": "ocid1.compartment.oc1..uniqueid",
   "region": "us-phoenix-1"
  }
 }
}
```



Was this article helpful?
YesNo

