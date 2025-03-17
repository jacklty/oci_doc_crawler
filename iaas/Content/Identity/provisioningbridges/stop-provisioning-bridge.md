Updated 2025-01-14
# Stopping a Provisioning Bridge
Stop a provisioning bridges in an OCI IAM identity domain.
If you stop a provisioning bridge that's running on a Windows or generic machine, then you must wait three minutes to restart the bridge. Also, before you stop a provisioning bridge, you must deactivate it. See [Deactivate Provisioning Bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/deactivate-provisioning-bridges.htm#deactivate-provisioning-bridges "You can deactivate a single provisioning bridge, or you can deactivate multiple provisioning bridges simultaneously.").
Use the following table to guide you on how to stop a provisioning bridge.
Machine | Mode | Action  
---|---|---  
Generic |  `normal` | Close the Terminal window or press `Ctrl + C`.  
Generic |  `background` | At the prompt of the Terminal window, stop the process by entering `kill -9 [Process_ID]`.**Note:** Because you started the provisioning bridge in `background` mode, even if you close the Terminal window, the bridge continues to run. For this reason, you must stop the process to stop the provisioning bridge.**Tip:** If you don't know the process ID, then run the following command: ```
ps -ef | grep CrossPlatformBridgeRunner
```
  
Windows | N/A | Close the Command window.   
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Provisioning bridges**.
  3. Verify that the provisioning bridge that you stopped has a status of **Stopped**.
If you still see a status of **Started** for the provisioning bridge, then wait three minutes, and select **Refresh**.


Was this article helpful?
YesNo

