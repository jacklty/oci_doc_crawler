Updated 2025-01-23
# Listing Private Templates
List private templates in Resource Manager.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm)


  *     1. Open the **navigation menu** and select **Developer Services**. Under **Resource Manager** , select **Private Templates**.
    2. To view the resources in a different compartment, use the **Compartment** filter to switch compartments.
You must have permission to work in a compartment to see the resources in it. If you're not sure which compartment to use, contact an administrator. For more information, see [Understanding Compartments](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm#Understa).
    3. To filter the list by tag:
      1. Next to **Tag filters** , select **add**.
      2. In the **Add a tag filter** dialog, enter the following:
         * **Tag namespace:** Select the tag namespace.
         * **Tag key:** Select the key.
         * **Tag value:** Select from the following:
           * **Match any value** - returns all resources tagged with the selected namespace and key, regardless of the tag value.
           * **Specify matching values** - returns resources with the tag value you enter in the text box. Enter a single value in the text box. To specify multiple values for the same namespace and key, select **+** to display another text box. Enter one value per text box.
      3. Select **Apply filter**.
  * Use the [oci resource-manager template list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/template/list.html) command and required parameters to list templates, setting `--template-category-id` to `3`:
Command
CopyTry It
```
oci resource-manager template list --template-category-id 3 [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [ListTemplates](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template/ListTemplates) operation to list templates. To filter the list to private templates, set `templateCategoryId` to `3`.


Was this article helpful?
YesNo

