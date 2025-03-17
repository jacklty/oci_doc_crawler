Updated 2025-01-15
# Deleting a DRG
Delete a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure. 
**Prerequisites:**
  * The DRG can't be attached to a VCN.
  * The DRG can't be connected to another network by way of Site-to-Site VPN, FastConnect, or remote peering. 
  * The DRG can't be listed as a target in a [route rule](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingroutetables.htm#Route2).


  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-delete.htm)


  * Tor delete a DRG, follow these steps:
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG you want to delete.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
    4. Click **Terminate**.
    5. Confirm when prompted.
The DRG is in the Terminating state for a short period while it's being deleted. The DRG route tables and DRG route distributions contained in the DRG are also deleted.
  * Use the [network drg delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/delete.html) command and required parameters to delete a DRG:
Command
CopyTry It
```
oci network drg delete --drg-id ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/DeleteDrg) operation to delete a DRG.


Was this article helpful?
YesNo

