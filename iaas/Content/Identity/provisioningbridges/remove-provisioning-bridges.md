Updated 2025-01-14
# Removing Provisioning Bridges
You can remove unused provisioning bridges from OCI IAM identity domain. You can remove either a single provisioning bridge or multiple bridges.
**Important** Before you remove any provisioning bridges, ensure that you:
  * Deactivate the provisioning bridges. See [Deactivate Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/deactivate-provisioning-bridges.htm#deactivate-provisioning-bridges "You can deactivate a single provisioning bridge, or you can deactivate multiple provisioning bridges simultaneously.").
  * Assign different provisioning bridges to apps. See [Change the Provisioning Bridge Assigned to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/change-provisioning-bridge-assigned-apps.htm#change-provisioning-bridge-assigned-apps "Only one provisioning bridge can be assigned to an app at any time. If you want to assign another bridge to the app, then you must replace the bridge that's already associated with the app with the designated bridge.").
  * Stop the provisioning bridges. See [Stop a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/stop-provisioning-bridge.htm#stop-provisioning-bridge "Stop a provisioning bridges in an OCI IAM identity domain.").


  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Provisioning bridges**.
  3. Select the checkbox for each provisioning bridge that you want to remove.
  4. Select **Delete**.
  5. In the Delete provisioning bridge window, select **Delete provisioning bridge**.


Was this article helpful?
YesNo

