Updated 2025-01-23
# Moving a Stack to a Different Compartment
Move a stack in Resource Manager to another compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/change-compartment-stack.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/change-compartment-stack.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/change-compartment-stack.htm)


  *     1. On the **Stacks** list page, select the stack that you want to work with. If you need help finding the list page or the stack, see [Listing Stacks](https://docs.oracle.com/en-us/iaas/Content/ResourceManager/Tasks/list-stacks.htm#top "List stacks in Resource Manager.").
    2. Go to **More actions** and then select **Move resource**.
    3. In the **Move resource** panel, select the destination compartment from the list.
    4. Select **Move resource**.
  * Use the `oci resource-manager stack change-compartment[](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager/stack/change-compartment.html)` command and required parameters to move a stack to another compartment.
Command
CopyTry It
```
oci resource-manager stack change-compartment --stack-id <stack_OCID> --compartment-id <destination_compartment_OCID>
```

For a complete list of parameters and values for CLI commands, see the [Command Line Reference for Resource Manager](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/resource-manager.html).
  * Use the [ChangeStackCompartment](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/Stack/ChangeStackCompartment) operation to move a stack to another compartment.


Was this article helpful?
YesNo

