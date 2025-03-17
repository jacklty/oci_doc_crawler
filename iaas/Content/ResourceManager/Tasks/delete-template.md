Updated 2025-01-07
# Deleting a Private Template
Delete a private template in Resource Manager.
**Note** You can't undo the deletion of a private template.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-template.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-template.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-template.htm)


  *     1. On the **Private templates** list page, find the private template that you want to work with. If you need help finding the list page or the private template, see [Listing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#top "List private templates in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the private template, select **Delete private template**.
    3. When prompted, confirm the deletion.
  * Use the [oci resource-manager template delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/template/delete.html) command and required parameters to delete a private template:
Command
CopyTry It
```
oci resource-manager template delete --template-id <template_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [DeleteTemplate](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template/DeleteTemplate) operation to delete a private template.


Was this article helpful?
YesNo

