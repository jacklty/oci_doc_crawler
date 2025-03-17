Updated 2025-01-07
# Deleting a Configuration Source Provider
Delete a configuration source provider in Resource Manager.
**Note** A configuration source provider can be deleted only if it's _not_ associated with a stack. To remove an association with a stack, [edit the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-stack.htm#top "Update a stack in Resource Manager.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-csp.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-csp.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/delete-csp.htm)


  *     1. On the **Configuration source providers** list page, find the configuration source provider that you want to work with. If you need help finding the list page or the configuration source provider, see [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-csp.htm#top "List configuration source providers in Resource Manager.").
    2. From the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the configuration source provider, select **Delete configuration source provider**.
    3. When prompted, confirm the deletion.
  * **Note** A configuration source provider cannot be deleted if it is associated with a stack. To remove the association from the stack, [update the stack](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/update-csp.htm#top "Update a configuration source provider in Resource Manager.").
Use the `oci resource-manager configuration-source-provider delete[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/delete.html)` command and required parameters to delete a configuration source provider.
Copy
```
oci resource-manager configuration-source-provider delete --configuration-source-provider-id <configuration_source_provider_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [DeleteConfigurationSourceProvider](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/DeleteConfigurationSourceProvider) operation to delete a configuration source provider.


Was this article helpful?
YesNo

