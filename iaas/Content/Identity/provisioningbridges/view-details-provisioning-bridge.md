Updated 2025-01-14
# Viewing Details about a Provisioning Bridge
View the details of a provisioning bridge in an IAM identity domain.
On the provisioning bridges list page, you can see the name, description, and connection status for each bridge.
On a bridge's details page, Yyou can also see other information about a provisioning bridge, such as its identity domain URL, version number, client ID, and client secret, any apps assigned to the bridge, and any connectors that are used by the bridge to communicate between the apps and the identity domain.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Settings** and then select **Provisioning bridges**.
  4. Select the name of the bridge about which you want to see information.
On the details page, the **Provisioning bridge Information** tab displays information about the provisioning bridge, including its name, description, identity domain URL, version number, and client ID. By selecting **Show secret** , you can see the client secret for the provisioning bridge in clear text. By selecting **Regenerate** , you can regenerate the secret for this bridge.
  5. Select **Details**.
In this tab, you see information about the provisioning bridge, including its name, description, identity domain URL, version number, and Client ID. By selecting **Show Secret** , you can see the Client Secret for the provisioning bridge in clear text. By selecting **Regenerate** , you can regenerate the Secret for this bridge.
  6. Under **Resources** , select **Apps**.
The **Apps** section displays a list of apps assigned to the provisioning bridge. You can assign more apps to this bridge or change the bridge associated with the apps. See [Assign a Provisioning Bridge to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/assign-provisioning-bridge-apps.htm#assign-provisioning-bridge-apps "After creating a provisioning bridge for an identity domain in IAM, you can assign it to on-premises apps in the App Catalog. Because this bridge serves as a provisioning and synchronizing agent between the identity domain and your apps, the bridge can poll for changes to users or groups in the apps and synchronize those changes into the identity domain.") and [Change the Provisioning Bridge Assigned to Apps](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/change-provisioning-bridge-assigned-apps.htm#change-provisioning-bridge-assigned-apps "Only one provisioning bridge can be assigned to an app at any time. If you want to assign another bridge to the app, then you must replace the bridge that's already associated with the app with the designated bridge."). 
**Note** For load-balancing purposes, Oracle suggests that you don't assign more than 10 apps to a provisioning bridge. To maintain more apps, create another provisioning bridge.
  7. Under **Resources** , select **Connectors**.
The **Connectors** sections displays any connectors that the provisioning bridge uses to communicate with the apps.


Was this article helpful?
YesNo

