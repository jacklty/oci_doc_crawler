Updated 2025-01-15
# Moving a DRG to a Different Compartment
Move a Dynamic Routing Gateway (DRG) from one compartment to another.
You can move a DRG from one compartment to another. When you move a DRG to a new compartment, inherent policies apply immediately. 
For more information about using compartments and policies to control access to your cloud network, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control). For general information about compartments, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm). 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-change-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-change-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-change-compartment.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG that you want to move.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Find the DRG in the list, click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**.
    4. Choose the destination compartment from the list. 
    5. Click **Move Resource**.
  * Use the [network drg change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/change-compartment.html) command and required parameters to move a DRG from one compartment to another:
Command
CopyTry It
```
oci network drg change-compartment --drg-id ocid --compartment-id new-compartment-ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ChangeDrgCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/ChangeDrgCompartment) operation to move a DRG from one compartment to another.


Was this article helpful?
YesNo

