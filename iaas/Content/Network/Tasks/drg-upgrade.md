Updated 2025-01-15
# Upgrading a DRG
Upgrade a Dynamic Routing Gateway (DRG) in Oracle Cloud Infrastructure.
A legacy DRG created before June 2021 (or possibly April 2021 depending on the region) must be upgraded before you can connect it to multiple VCNs, use it in cross-tenancy peering scenarios, or modify the internal routing policies. This upgrade process doesn't change the DRG's OCID. For details, see [Before you Upgrade a DRG](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingDRGs.htm#overview__before_upgrade). 
**Note** You can't roll back the change to the DRG. Upgrading the DRG resets existing BGP sessions for both Site-to-Site VPN and FastConnect. 
To monitor the upgrade process or determine if you might need to upgrade your DRG, follow the steps in [Finding the DRG Upgrade Status](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-get-upgrade-status.htm#drg-get_upgrade_status "Find the Dynamic Routing Gateway \(DRG\) upgrade status.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/drg-upgrade.htm)


  *     1. Open the **navigation menu** and select **Networking**. Under **Customer connectivity** , select **Dynamic routing gateway**.
    2. Under **List Scope** , select the compartment that contains the DRG that you want to upgrade.
The page updates to display only the resources in that compartment. If you're not sure which compartment to use, contact an administrator. For more information, see [Access Control](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/accesscontrol.htm#Access_Control).
    3. Click the name of the DRG.
    4. Click **Upgrade DRG**.
This option is available only for legacy DRGs that can be upgraded.
A message appears reminding you the action can't be reversed. 
    5. Click **Upgrade DRG**. 
    6. The upgrade occurs in the background. You can continue to make configuration settings while the upgrade is occurring. You're notified when the upgrade is complete. 
    7. When the upgrade finishes, click **Refresh page** to gain access to the new DRG capabilities. 
  * Use the [network drg upgrade](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/network/drg/upgrade.html) command and required parameters to upgrade a legacy DRG:
Command
CopyTry It
```
oci network drg upgrade --drg-id ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpgradeDrg ](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Drg/UpgradeDrg) operation to upgrade a legacy DRG.


Was this article helpful?
YesNo

