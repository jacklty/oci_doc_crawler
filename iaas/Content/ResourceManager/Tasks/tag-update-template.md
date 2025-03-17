Updated 2024-10-08
# Tagging a Private Template When Updating
Add metadata to a private template when you update it. This metadata enables you to define keys and values and to associate them with resources.
For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-update-template.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-update-template.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-update-template.htm)


  *     1. On the **Private templates** list page, select the private template that you want to work with. If you need help finding the list page or the private template, see [Listing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#top "List private templates in Resource Manager.").
    2. To add a tag, select **Add tags** , and enter the tag namespace, key, and value.
    3. To view existing tags, select the **Tags** tab and then select **Defined tags** or **Free-form tags**.
    4. To edit an existing tag, select the edit icon, update the value in the **Edit tag** dialog box, and then select **Save**.
    5. To remove a tag, select the edit icon and then select **Remove tag**.
  * Use the `oci resource-manager template update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/template/update.html)` command and required parameters to tag a private template when you update it.
Copy
```
oci resource-manager template update [--defined-tags | --freeform-tags] <tags> [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [UpdateTemplate](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template/UpdateTemplate) operation to tag a private template when you update it. Include the `definedTags` and `freeformTags` attributes and their values.


Was this article helpful?
YesNo

