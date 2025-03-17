Updated 2025-01-14
# Modifying a Provisioning Bridge
Modify the name, description, or client secret of a provisioning bridge in an IAM identity domain.
To change the apps to which the bridge is assigned, see [Changing the Provisioning Bridge Assigned to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/change-provisioning-bridge-assigned-apps.htm#change-provisioning-bridge-assigned-apps "Only one provisioning bridge can be assigned to an app at any time. If you want to assign another bridge to the app, then you must replace the bridge that's already associated with the app with the designated bridge.").
To change the folder where all log files for the provisioning bridge are stored and the log level for these log files, see [Manage Log Files for a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/manage-log-files-provisioning-bridge.htm#manage-log-files-provisioning-bridge "After you install and start a provisioning bridge, you might want to access the log files for troubleshooting purposes. You can locate these files in the logs folder.").
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Settings** and then select **Provisioning bridges**.
  4. Select the name of the bridge that you want to modify.
  5. To edit the name or descriptive information about the bridge, select **Edit provisioning bridge** , change the values as needed, and then select **Save changes**.
  6. To regenerate the Client Secret for this bridge, select **Regenerate**.
     * If the bridge is in the Activated state, then you can't regenerate a client secret for it because the bridge is using this secret to access the identity domain as an administrator.
     * To regenerate a secret for this bridge, you must first deactivate the bridge, and then stop it. See [Deactivate Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/deactivate-provisioning-bridges.htm#deactivate-provisioning-bridges "You can deactivate a single provisioning bridge, or you can deactivate multiple provisioning bridges simultaneously.") and [Stop a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/stop-provisioning-bridge.htm#stop-provisioning-bridge "Stop a provisioning bridges in an OCI IAM identity domain.").
     * If you regenerate the secret for a provisioning bridge, then you must delete the `wallet` folder and recreate the Oracle Wallet that you made in [Create a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/create-provisioning-bridge.htm#create-provisioning-bridge "Create a provisioning bridge in an identity domain to link your on-premises apps with IAM.") so that the wallet contains the regenerated secret.
  7. In the **New client secret** window, select **Copy** to copy the client secret to the clipboard.
  8. Select **Close**.


Was this article helpful?
YesNo

