Updated 2025-01-23
# Moving a Configuration Source Provider to a Different Compartment
Move a configuration source provider in Resource Manager to another compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/change-compartment-csp.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/change-compartment-csp.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/change-compartment-csp.htm)


  *     1. On the **Configuration source providers** list page, select the configuration source provider that you want to work with. If you need help finding the list page or the configuration source provider, see [Listing Configuration Source Providers](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-csp.htm#top "List configuration source providers in Resource Manager.").
    2. On the configuration source provider's details page, select **Move resource**.
    3. In the **Move resource** panel, select the destination compartment from the list.
    4. Select **Move resource**.
  * Use the `oci resource-manager configuration-source-provider change-compartment[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/configuration-source-provider/change-compartment.html)` command and required parameters to move a configuration source provider to another compartment.
Copy
```
oci resource-manager configuration-source-provider change-compartment --configuration-source-provider-id <configuration_source_provider_OCID> --compartment-id <destination_compartment_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [ChangeConfigurationSourceProviderCompartment](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/ConfigurationSourceProvider/ChangeConfigurationSourceProviderCompartment) operation to move a configuration source provider to another compartment.


Was this article helpful?
YesNo

