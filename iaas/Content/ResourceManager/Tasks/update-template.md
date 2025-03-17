Updated 2024-10-08
# Updating a Private Template
Update a private template in Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-template.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-template.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-template.htm)


  *     1. On the **Private templates** list page, select the private template that you want to work with. If you need help finding the list page or the private template, see [Listing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#top "List private templates in Resource Manager.").
    2. On the private template's details page, select **Edit**.
    3. In the **Edit template** panel, update the values as needed.
For more information about the fields, see [Creating a Private Template](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-template.htm#top "Create a private template in Resource Manager.").
    4. Select **Save**.
  * Use the [oci resource-manager template update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/template/update.html) command and required parameters to update a private template:
Command
CopyTry It
```
oci resource-manager template update --template-id <template_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [UpdateTemplate](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template/UpdateTemplate) operation to update a private template.


Was this article helpful?
YesNo

