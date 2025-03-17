Updated 2025-01-23
# Moving a Private Template to a Different Compartment
Move a private template in Resource Manager to another compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/change-compartment-template.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/change-compartment-template.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/change-compartment-template.htm)


  *     1. On the **Private templates** list page, select the private template that you want to work with. If you need help finding the list page or the private template, see [Listing Private Templates](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-template.htm#top "List private templates in Resource Manager.").
    2. On the private template's details page, select **Move resource**.
    3. In the **Move resource** panel, select the destination compartment from the list.
    4. Select **Move resource**.
  * Use the [oci resource-manager template change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/template/change-compartment.html) command and required parameters to move a private template to another compartment:
Command
CopyTry It
```
oci resource-manager template change-compartment --template-id <template_OCID> --compartment-id <destination_compartment_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Run the [ChangeTemplateCompartment](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Template/ChangeTemplateCompartment) operation to move a private template.


Was this article helpful?
YesNo

