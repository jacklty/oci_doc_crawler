Updated 2025-01-15
# Updating the Name of a DRG
Rename a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-update.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment containing the DRG whose name you want to update.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
    4. Click **Edit**.
    5. Edit the display name. Avoid entering confidential information. 
    6. Click **Save Changes**.
  * Use the [network drg update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/update.html) command and required parameters to rename a DRG:
Command
CopyTry It
```
oci network drg update --drg-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateDrg](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/UpdateDrg) operation to rename a DRG.


Was this article helpful?
YesNo

