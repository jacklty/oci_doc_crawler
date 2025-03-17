Updated 2025-01-14
# Starting a Provisioning Bridge on a Generic Machine
Start a provisioning bridges in an IAM identity domain on a generic machine.
A generic machine has Java 8 installed on it and supports bash shell. For this type of machine, you can start the Provisioning Bridge in two modes:
  * `normal:` The bridge starts in a Terminal window. 
  * `background:` The bridge starts as a process in the background in a Terminal window.


**Important** You can't start multiple provisioning bridges with the same configuration information. If you want to start another provisioning bridge, then use the provisioning bridges list page to create a new bridge, and use the newly generated client ID and secret for the identity domain to start the bridge.
  1. Start the generic machine where you installed the client for the bridge.
**Important** Ensure that you have administrative rights for this machine. Also, check that this machine communicates with the client network that the bridge uses to access the apps that you want to monitor.
  2. In a Terminal window, navigate to the folder you created that contains the files for the bridge. You created this folder in [Create a Provisioning Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/create-provisioning-bridge.htm#create-provisioning-bridge "Create a provisioning bridge in an identity domain to link your on-premises apps with IAM.").
  3. 3. At the prompt, enter one of the following commands, depending on the mode you want to use: `./startup.sh normal`.
     * `./startup.sh normal`
     * `./startup.sh background`
  4. At the prompt, enter the password for Oracle Wallet that you created when you created the bridge.
The Provisioning Bridge attempts to connect to the identity domain server.
  5. If you're using `normal` mode, verify that you see the status message `The Provisioning Bridge is started`, which indicates that a connection is established between the bridge and the identity domain server.
**Important** Ensure that you keep this Terminal window open. If you close it, then you stop the Provisioning Bridge.
  6. If you're using background mode, verify that you see the status message `The Provisioning Bridge is started. [Process_ID] is the process ID that's used to start this bridge`. A connection is established between the bridge and the identity domain server
**Note** If you want to stop the bridge, then use the process ID to stop the process. You can also use this ID to check if the process is running properly, or if there are any errors associated with the process.
  7. In the Oracle Cloud Console, open the navigation menu and select **Identity & Security**. Under **Identity** , select **Domains**.
  8. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  9. Select **Settings** and then select **Provisioning bridges**.
  10. Verify that the bridge has a status of **Started**.
  11. Select the name of the bridge, and then select **Connectors**.
  12. Verify that you see the names and versions of the connectors that are used by the bridge to communicate with the associated apps.


Was this article helpful?
YesNo

