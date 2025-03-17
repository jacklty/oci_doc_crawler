Updated 2025-01-14
# Starting a Provisioning Bridge on a Windows Machine
Start a provisioning bridges in an IAM identity domain on a Windows machine.
**Important** You can't start multiple provisioning bridges with the same configuration information. If you want to start another provisioning bridge, then use the provisioning bridges list page to create a new bridge, and use the newly generated client ID and secret for the identity domain to start the bridge.
  1. Start the Windows machine where you installed the client for the provisioning bridge.
**Important** Ensure that you have administrative rights for this machine. Also, check that this machine communicates with the client network that the provisioning bridge uses to access the apps that you want to monitor.
  2. Open Windows Explorer, and then navigate to the folder you created that contains the files for the provisioning bridge. You created this folder in [Create a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/create-provisioning-bridge.htm#create-provisioning-bridge "Create a provisioning bridge in an identity domain to link your on-premises apps with IAM.").
  3. Double-click the `startup.bat` file.
  4. At the command window prompt, enter the password for Oracle Wallet that you created when you created the bridge.
The provisioning bridge attempts to connect to the identity domain server.
  5. Verify that you see the status message `The Provisioning Bridge is started.` which indicates that a connection is established between the provisioning bridge and the identity domain server.
**Important** Ensure that you keep this command window open. If you close it, then you stop the Provisioning Bridge.
  6. In the Oracle Cloud Console, open the navigation menu and select **Identity & Security**. Under **Identity** , select **Domains**.
  7. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  8. Select **Settings** and then select **Provisioning bridges**.
  9. Verify that the bridge has a status of **Started**.
  10. Select the name of the bridge, and then select **Connectors**.
  11. Verify that you see the names and versions of the connectors that are used by the bridge to communicate with the associated apps.


Was this article helpful?
YesNo

