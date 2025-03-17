Updated 2023-01-04
# Disconnecting From a Volume
For volumes attached with [iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#iSCSI) as the volume attachment type you need to disconnect the volume from an instance before you detach the volume. For more information about attachment type options, see [Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#attachtype).
## Required IAM Policy 🔗 
Disconnecting a volume from an instance does not require a specific IAM policy. Don't confuse this with detaching a volume (see [Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#Detaching_a_Volume "Detach a block volume from an instance.")). 
[Disconnecting from a Volume on a Linux Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/disconnectingfromavolume.htm)
**Caution** We recommend that you unmount and disconnect the volume from the instance using `iscsiadm` before you detach the volume. Failure to do so may lead to loss of data.
  1. Log on to your instance's guest OS and unmount the volume.
  2. Run the following command to disconnect the instance from the volume:
Copy
```
iscsiadm -m node -T <IQN> -p <iSCSI IP ADDRESS>:<iSCSI PORT> -u
```

A successful logout response resembles the following:
```
Logging out of session [sid: 2, target: iqn.2015-12.us.oracle.com:c6acda73-90b4-4bbb-9a75-faux09015418, portal: 169.254.0.2,3260]
Logout of [sid: 2, target: iqn.2015-12.us.oracle.com:c6acda73-90b4-4bbb-9a75-faux09015418, portal: 169.254.0.2,3260] successful.
```

  3. You can now detach the volume without the risk of losing data.


[Disconnecting from a Volume on a Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/disconnectingfromavolume.htm)
  1. Use a Remote Desktop client to log on to your Windows instance, and then open **Disk Management**.
  2. Right-click the volume you want to disconnect, and then click **Offline**.
  3. Open **iSCSI Initiator** , select the target, and then click **Disconnect**.
  4. Confirm the session termination. The status should show as **Inactive**.
  5. In **iSCSI Initiator** , click the **Favorite Targets** tab, select the target you are disconnecting, and then click **Remove**.
  6. Click the **Volumes and Devices** tab, select the volume from the **Volume List** , and then click **Remove**.
  7. You can now detach the volume without the risk of losing data.


Was this article helpful?
YesNo

