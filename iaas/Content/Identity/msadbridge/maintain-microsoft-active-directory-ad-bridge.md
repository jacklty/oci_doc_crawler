Updated 2025-01-14
# Transfer the AD Bridge
Transfer the bridge between IAM and Microsoft Active Directory to another machine and restart it.
## Transferring the AD Bridge 🔗 
**Note** If you can't remove the client for the AD bridge or the bridge still appears in the **Directory Integrations** page, then follow the procedure in [Removing an AD Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/remove-microsoft-active-directory-ad-bridge.htm#remove-microsoft-active-directory-ad-bridge "Remove an AD bridge from an IAM identity domain.").
  1. From the original machine, access the **Control Panel** , and uninstall the client for the AD bridge.
  2. On the other machine, install the client. See [Create a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/create-microsoft-active-directory-ad-bridge.htm#create-microsoft-active-directory-ad-bridge "Create a bridge between IAM and Microsoft Active Directory.").
  3. In the IAM Console, expand the **Navigation Drawer** , select **Settings** , and then select **Directory Integrations**.
  4. Verify that the AD bridge appears in the other machine with an **Active** status. This bridge can now be used to synchronize with your Microsoft Active Directory enterprise directory structure.


## Restarting the Microsoft Active Directory Bridge 🔗 
  1. Select **Start**.
  2. In the text box, enter **Services** , and then press **Enter**.
The **Services** window appears. This window contains a utility that's used to manage daemon processes within the Windows OS. These processes include the backend service that's used to establish communication between IAM and Microsoft Active Directory.
  3. Select**Services (Local)** , select the **Standard** tab, scroll down the list of services, right-click **Oracle Identity Cloud Service Microsoft Active Directory Bridge Service** , and then select **Start**.
  4. Verify that **Running** appears as the status for the service.


Was this article helpful?
YesNo

