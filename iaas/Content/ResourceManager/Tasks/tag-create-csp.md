Updated 2025-01-07
# Tagging a Configuration Source Provider at Creation
Add metadata to a configuration source provider when you first create it. This metadata enables you to define keys and values and to associate them with resources.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-create-csp.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-create-csp.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/tag-create-csp.htm)


  *     1. On the **Configuration source providers** list page, select **Create configuration source provider**. If you need help finding the list page or the configuration source provider, see [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-csp.htm#top "List configuration source providers in Resource Manager.").
    2. To show tagging options, select **Show advanced options**.
    3. To add a defined tag, select the namespace and key, then enter a value.
    4. To add a free-form tag, enter a key and value.
    5. Enter other values as needed.
For more information about the fields, see [Creating a Configuration Source Provider](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/create-csp.htm#top "Create a configuration source provider in Resource Manager.").
    6. Select **Create**.
  * Use the `oci resource-manager configuration-source-provider create[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/create.html)` command and required parameters to tag a configuration source provider when you create it.
Copy
```
oci resource-manager configuration-source-provider create [--defined-tags | --freeform-tags] <tags> [...]
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [CreateConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/CreateConfigurationSourceProvider) operation to tag a configuration source provider when you create it. Include the `definedTags` and `freeformTags` attributes and their values.


Was this article helpful?
YesNo

