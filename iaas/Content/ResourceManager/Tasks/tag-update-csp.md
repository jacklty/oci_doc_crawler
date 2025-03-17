Updated 2024-10-08
# Tagging a Configuration Source Provider When Updating
Add metadata to a configuration source provider when you update it. This metadata enables you to define keys and values and to associate them with resources.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-update-csp.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-update-csp.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-update-csp.htm)


  *     1. On the **Configuration source providers** list page, select the configuration source provider that you want to work with. If you need help finding the list page or the configuration source provider, see [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-csp.htm#top "List configuration source providers in Resource Manager.").
    2. To add a tag, select **Add tags** , and enter the tag namespace, key, and value.
    3. To view existing tags, select the **Tags** tab and then select **Defined tags** or **Free-form tags**.
    4. To edit an existing tag, select the edit icon, update the value in the **Edit tag** dialog box, and then select **Save**.
    5. To remove a tag, select the edit icon and then select **Remove tag**.
  * Use the `oci resource-manager configuration-source-provider update[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/update.html)` command and required parameters to tag a configuration source provider when you update it.
Copy
```
oci resource-manager configuration-source-provider update [--defined-tags | --freeform-tags] <tags> [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [UpdateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/UpdateConfigurationSourceProvider) operation to tag a configuration source provider when you update it. Include the `definedTags` and `freeformTags` attributes and their values.


Was this article helpful?
YesNo

