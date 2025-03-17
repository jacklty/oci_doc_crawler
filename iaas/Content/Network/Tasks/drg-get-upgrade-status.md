Updated 2025-01-15
# Finding the DRG Upgrade Status
Find the Dynamic Routing Gateway (DRG) upgrade status.
DRGs created before June 2021 (or possibly April 2021 depending on the region) use legacy software, and can be [upgraded to the most recent version](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__Versions). The status can be _not updated_ , _in progress_ , or _updated_. 
DRGs created after that date always use the upgraded software. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm)


  * This information is only seen for DRGs created before May 17, 2021. DRGs created after that date are upgraded by default.
    1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment containing the DRG you want to find upgrade status for.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
If this DRG is a legacy DRG, the upgrade status displays in the **Dynamic routing gateway information** tab. Upgraded DRGs don't have a field indicating the upgrade status.
  * Use the [network drg get-upgrade-status](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/get-upgrade-status.html) command and required parameters to find the DRG upgrade status:
Command
CopyTry It
```
oci oci network drg get-upgrade-status --drg-id ocid ... [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetUpgradeStatus](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/GetUpgradeStatus) operation to find the DRG upgrade status.


Was this article helpful?
YesNo

