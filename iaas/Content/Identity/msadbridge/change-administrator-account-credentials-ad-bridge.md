Updated 2025-01-14
# Change Administrator Account Credentials for AD Bridge
Use the AD Bridge client to update administrator account details.
If the Active Directory credentials of the administrator changes, or if you want to use a diffferent administrator for AD Bridge, use the AD Bridge client to update them.
  1. Open `ADBridgeUI.exe`. It's in the AD Bridge installation folder. The default path is `C:\Program Files\Oracle\IDBridge`.
  2. Select **Update AD Credentials** and enter the changed username and password, or the username and password of another administrator.
  3. Check the credentials by selecting **Test**. When you select **Test** , the AD Bridge checks the following:
     * Whether sync is running or not. If it is running, wait for it to finish then try again. You can see the sync status in the Oracle Identity Cloud Service Admin console. See [Checking a Bridge Data Synchronization Status](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/check-bridge-data-synchronization-status.htm#check-bridge-data-synchronization-status "Checking the data synchronization status of an AD bridge in an IAM identity domain.").
     * That the credentials are valid. If they are not, check and re-enter them, then test again.
  4. Select **Update**.


Was this article helpful?
YesNo

