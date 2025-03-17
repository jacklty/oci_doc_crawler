Updated 2025-01-07
# Tagging a Private Template at Creation
Add metadata to a private template when you first create it. This metadata enables you to define keys and values and to associate them with resources.
For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-create-template.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-create-template.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-create-template.htm)


  *     1. On the **Private templates** list page, select **Create private template**. If you need help finding the list page or the private template, see [Listing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#top "List private templates in Resource Manager.").
    2. To show tagging options, select **Show advanced options**.
    3. To add a defined tag, select the namespace and key, then enter a value.
    4. To add a free-form tag, enter a key and value.
    5. Enter other values as needed.
For more information about the fields, see [Creating a Private Template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-template.htm#top "Create a private template in Resource Manager.").
    6. Select **Create**.
  * Use the `oci resource-manager template create[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/template/create.html)` command and required parameters to tag a private template when you create it.
Copy
```
oci resource-manager template create [--defined-tags | --freeform-tags] <tags> [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [CreateTemplate](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template/CreateTemplate) operation to tag a private template when you create it. Include the `definedTags` and `freeformTags` attributes and their values.


Was this article helpful?
YesNo

