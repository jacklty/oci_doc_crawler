Updated 2024-10-15
# Recovering a Corrupted Boot Volume for Windows Instances
If your instance fails to boot successfully or boots with the boot volume set to read-only access, the instance's boot volume may be corrupted. While it is rare, boot volume corruption can occur in the following scenarios:
  * When an instance experiences a forced shutdown using the API.
  * When an instance experiences a system hang due to an operating system or software error and a graceful reboot or shutdown of the instance times out, and then a forced shutdown occurs.
  * When an error or outage occurs in the underlying infrastructure and there were critical disk writes pending in the system.


**Important**
  * In most cases a simple reboot will resolve boot volume corruption issues, so this is the first action you should take when troubleshooting this.
  * When a boot volume is detached from a Windows instance, Windows alters that volume's boot configuration data (BCD). As a result, you might need to restore the BCD to be able to reattach the boot volume and boot the original instance. For more information, see the [Comprehensive Guide to Recovering and Restoring Windows Boot Volumes in OCI](https://support.oracle.com/knowledge/Oracle%20Cloud/3036441_1.html).

In most cases a simple reboot will resolve boot volume corruption issues, so this is the first action you should take when troubleshooting this.
This topic describes how to determine if your Windows instance's boot volume is corrupted and what steps to take to troubleshoot and recover the corrupted boot volume. For Linux-based instances, see [Recovering a Corrupted Boot Volume for Linux-Based Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/recoveringlinuxbootvolume.htm#Recovering_a_Corrupted_Boot_Volume_for_LinuxBased_Instances).
## Detecting Boot Volume Corruption 🔗 
When Windows operating systems detect boot volume corruption, the instance is usually able to recover from it by automatically repairing the file system. You can use a VNC console connection to verify that the instance isn't experiencing a system hang while repairing the file system, or to detect if there are other issues. VNC console connections enable you to see what's displayed through the VGA port, for more information about the VNC console, see [Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm).
**Important** VNC console connections only work for virtual machine (VM) instances launched on October 13, 2017 or later, and bare metal instances launched on February 21, 2019 or later. If your instance does not support VNC console connections, proceed to [Recovering the Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/recoveringwindowsbootvolume.htm#recover).
  1. [Create a VNC console connection for the instance](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm#Connecti2).
  2. [Connect to the instance through VNC console](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm#Connecti).
Check what is displayed in the VNC console to see if the instance is stuck in the boot process or if it is in the recovery partition. 
**Tip** For Windows Server 2012 and later versions, if the instance has booted into the recovery partition it may be possible to directly perform the steps to recover the boot volume in the recovery partition.


## Detaching the Boot Volume 🔗 
If you have detected that your instance's boot volume is corrupted, you need to detach the boot volume from the instance before you can begin troubleshooting and recovery steps.
  1. [Stop the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm). 
  2. [Detach the boot volume from the instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingabootvolume.htm#Detaching_a_Boot_Volume). 


## Recovering the Boot Volume 🔗 
To troubleshoot and recover the corrupted boot volume, you need to attach the boot volume to a second instance as a data volume. For the second instance we recommend that you use an instance running an operating system that most closely matches the operating system for the boot volume's instance, and you should only attach boot volumes for Windows instances to other Windows instances. The second instance must be in the same availability domain and region as the boot volume's instance. If no existing instance is available create a new Windows instance using the steps described in [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm).
Once you have the second instance, make sure you can log in to the instance and that it is functional before proceeding with the recovery steps. After you have confirmed that the instance is functional perform the following steps.
  1. Attach the boot volume to the second instance as a data volume. For more information, see [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.").
[To attach the boot volume as a data volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/recoveringwindowsbootvolume.htm)
    1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
    2. Click the instance that you want to attach a volume to.
    3. Under **Resources** , click **Attached Block Volumes**. 
    4. Click **Attach Block Volume**.
    5. Select **iSCSI** for the volume attachment type.
    6. In the **Block Volume Compartment** drop-down list, select the compartment. 
    7. Choose the **Select Volume** option and then select the volume from the **Boot Volume** section of the **Block Volume** drop-down list. 
    8. Select **Read/Write** as the access type.
    9. Click **Attach**.
When the volume's icon no longer lists it as **Attaching** , proceed with the next steps. 
  2. Connect to the second instance, see [Connecting to a Windows Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/connect-to-windows-instance.htm) for more information. 
  3. Connect to the volume, see [Connecting to a Volume on a Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume_topic-Connecting_to_iSCSIAttached_Volumes.htm#winconnect) for more information. Since you are attaching a boot volume as a data volume you must also run the `Connect-IscsiTarget` and set `IsMultiEnabled` to true. For example:
Copy
```
Set-Service -Name msiscsi -StartupType Automatic
Start-Service msiscsi
New-IscsiTargetPortal –TargetPortalAddress 169.254.2.4
Connect-IscsiTarget -NodeAddress iqn.2015-02.oracle.boot:uefi -TargetPortalAddress 169.254.2.4 -IsPersistent $True -IsMultipathEnabled $True
```

  4. Open **Computer Management** and navigate to **Storage** , and then **Disk Management**.
  5. Select the new disk and mark it **Online**. 
  6. Click **This PC** and then right-click on the new disk and select **Properties**.
  7. Navigate to **Tools** , **Error Checking** , and then **Check**. 
  8. Select **Scan Drive** and fix issues as they come up.
  9. Mark the new disk **Offline**.
  10. Open iscsi initiator with administrator privileges.
  11. In **Favorite Targets** , remove the iscsi target of the attached volume.


Was this article helpful?
YesNo

