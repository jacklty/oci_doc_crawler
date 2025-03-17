Updated 2024-10-08
# Updating a Job
Update a job's name or tags in Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job.htm)


  * These steps show how to update a job in a compartment. You can also update a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
    1. On the **Jobs** list page, select the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. To update the job name, follow these steps:
      1. Select **Edit job**.
      2. In the **Edit job** panel, update the job name.
      3. Select **Save changes**.
    3. To add a tag, select **Add tags** , and enter the tag namespace, key, and value.
    4. To view existing tags, select the **Tags** tab and then select **Defined tags** or **Free-form tags**.
    5. To edit an existing tag, select the edit icon, update the value in the **Edit tag** dialog box, and then select **Save**.
    6. To remove a tag, select the edit icon and then select **Remove tag**.
  * Use the `oci resource-manager job update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/update.html)` command and required parameters to update a job.
Command
CopyTry It
```
oci resource-manager job update --job-id <job_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/UpdateJob) operation to update a job.


Was this article helpful?
YesNo

