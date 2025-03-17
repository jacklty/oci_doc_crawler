Updated 2025-01-07
# Tagging a Job
Add tag metadata to a job in Resource Manager. Tags are key-value pairs that you attach to resources to help you organize and track the resources across compartments.
**Note** This page describes how to tag an existing job. You can also tag a job when you [create it](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-job.htm#top "Create a job in Resource Manager, such as plan, apply, or destroy.").
If you have permissions to create a resource, you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job-tags.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job-tags.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-job-tags.htm)


  * These steps show how to tag a job in a compartment. You can also tag a job [in a stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/get-stack.htm#top "Get the details of a stack in Resource Manager.").
    1. On the **Jobs** list page, find the job that you want to work with. If you need help finding the list page or the stack, see [Listing Jobs](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-jobs.htm#top "List jobs in Resource Manager.").
    2. To add a tag:
      1. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the job, select **Add tags**.
The **Add tags** dialog box opens.
      2. For a defined tag, select the namespace.
      3. Select or enter the key.
      4. Enter a value.
      5. Select **Add tags**.
    3. To edit a tag:
      1. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the job, select **View tags**.
The **View tags** dialog box opens.
      2. In the **View Tags** dialog box, select the tab for the type of tag that you want to edit (defined or free-form).
      3. Select the pencil icon for the tag that you want to edit.
      4. In the **Edit Tags** dialog box, update the value and then select **Save**.
  * Use the `oci resource-manager job update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/job/update.html)` command and required parameters to tag a job.
Command
CopyTry It
```
oci resource-manager job update [--defined-tags | --freeform-tags] <tags> [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [UpdateJob](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Job/UpdateJob) operation to tag a job.


Was this article helpful?
YesNo

