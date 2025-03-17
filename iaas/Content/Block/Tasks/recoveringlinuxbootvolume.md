Updated 2024-03-22
# Recovering a Corrupted Boot Volume for Linux-Based Instances
If your instance fails to boot successfully or boots with the boot volume set to read-only access, the instance's boot volume may be corrupted. While it is rare, boot volume corruption can occur in the following scenarios:
  * When an instance experiences a forced shutdown using the API.
  * When an instance experiences a system hang due to an operating system or software error and a graceful reboot or shutdown of the instance times out, and then a forced shutdown occurs.
  * When an error or outage occurs in the underlying infrastructure and there were critical disk writes pending in the system.


**Important** In most cases a simple reboot will resolve boot volume corruption issues, so this is the first action you should take when troubleshooting this.
This topic describes how to determine if your Linux-based instance's boot volume is corrupted and what steps to take to troubleshoot and recover the corrupted boot volume. For Windows instances, see [Recovering a Corrupted Boot Volume for Windows Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/recoveringwindowsbootvolume.htm#Recovering_a_Corrupted_Boot_Volume_for_Windows_Instances).
## Detecting Boot Volume Corruption 🔗 
Boot volume corruption can prevent an instance from booting successfully, so you might not be able to connect to the instance using SSH. Instead, you can use the instance console connection feature to connect to the malfunctioning instance. For more information about using this feature, see [Troubleshooting Instances Using Instance Console Connections](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm).
This section describes how to use a serial console connection to detect if boot volume corruption has occurred. 
**Tip** If you have already confirmed your instance's boot volume is corrupted or if you are using an imported custom image, proceed to the [Recovering the Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/recoveringlinuxbootvolume.htm#recover) section, which describes how to use a second instance along with standard file system tools to both detect and repair boot volume corruption.
  1. [Create a serial console connection for the instance](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm#Creating). 
  2. [Connect to the instance through serial console](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm#Connecti2).
At this point, it's normal for the serial console to appear to hang, as the system may have already crashed.
  3. [Reboot the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm) from the Console. 
  4. Once the reboot process starts, switch back to the terminal window, and you should see system messages from the instance start to appear in the window.
  5. Monitor the messages that appear as the system is starting up. Most operating systems will set the boot volume to read-only as soon as disk corruption is detected to prevent writes from further corrupting the volume, so look for messages that indicate the boot volume is in read-only mode. Following are some examples:
     * On an instance with iSCSI-attached boot volumes, the `iscsiadm` service will fail to attach a volume because the volume is in read-only mode. This will typically prevent instances from continuing to boot. The serial console may display a message similar to the following:
```
iscsiadm: Maybe you are not root?
iscsiadm: Could not lock discovery DB: /var/lock/iscsi/lock.write: Read-only file system
touch: cannot touch `/var/lock/subsys/iscsid': Read-only file system
touch: cannot touch `/var/lock/subsys/iscsi': Read-only file system
```

     * On an instance with paravirtualized-attached boot volumes, the system may continue the boot process, but will be in a degraded state because nothing can be written to the boot drive.The serial console may display error messages similar to the following:
```
[FAILED] Failed to start Create Volatile Files and Directories.
See 'systemctl status systemd-tmpfiles-setup.service' for details.
...
[  27.160070] cloud-init[819]:   os.chmod(path, real_mode)
[  27.166027] cloud-init[819]: OSError: [Errno 30] Read-only file system: '/var/lib/cloud/data'
```

The error messages and system behavior described here are the most commonly seen for boot volume corruption, however depending on the operating system, you may see different error messages and system behavior. If you don't see the ones described here, consult the documentation for your operating system for additional troubleshooting information.


## Recovering the Boot Volume 🔗 
To troubleshoot and recover the corrupted boot volume, you need to detach the boot volume from the instance and then attach the boot volume to a second instance as a data volume. 
### Detaching the Boot Volume
If you have detected that your instance's boot volume is corrupted, you need to detach the boot volume from the instance before you can begin troubleshooting and recovery steps.
  1. [Stop the instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm). 
  2. [Detach the boot volume from the instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingabootvolume.htm#Detaching_a_Boot_Volume). 


### Attaching the Boot Volume as a Data Volume to a Second Instance
For the second instance, we recommend that you use an instance running an operating system that most closely matches the operating system for the boot volume's instance. You should only attach boot volumes for Linux-based instances to other Linux-based instances. The second instance must be in the same availability domain and region as the boot volume's instance. If no existing instance is available, create a new Linux instance using the steps described in [Creating an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm). Once you have the second instance, make sure you can log into the instance and that it is functional before proceeding with the recovery steps. For steps to access the instance, see [Connecting to a Linux Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/connect-to-linux-instance.htm). After you have confirmed that the instance is functional, perform the following steps.
  1. Run the `lsblk` command and make note of the drives that are currently on the instance, for example:
```
lsblk
NAME  MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
sda   8:0  0 46.6G 0 disk
├─sda2  8:2  0  8G 0 part [SWAP]
├─sda3  8:3  0 38.4G 0 part /
└─sda1  8:1  0 200M 0 part /boot/efi
```

  2. Attach the boot volume to the second instance as a data volume. For more information, see [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.").
[To attach the boot volume as a data volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/recoveringlinuxbootvolume.htm)
    1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
    2. Click the instance that you want to attach a volume to.
    3. Under **Resources** , click **Attached Block Volumes**. 
    4. Click **Attach Block Volume**.
    5. Select the volume attachment type. If **Paravirtualized** attachments are available for this instance, we recommend that you select this attachment type for this procedure.
If you select **iSCSI** as the volume attachment type, you need to connect to the volume, see [Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm#top "Connect to a block volume that's attached to a compute instance.") for more information.
    6. In the **Block Volume Compartment** drop-down list, select the compartment. 
    7. Choose the **Select Volume** option and then select the volume from the **Boot Volume** section of the **Block Volume** drop-down list. 
    8. Select **Read/Write** as the access type.
    9. Click **Attach**.
When the volume's icon no longer lists it as **Attaching** , proceed with the next steps. 
  3. Run the `lsblk` command again to confirm that the boot volume now shows up as a volume attached to the instance. In this sample output for the `lsblk`, the boot volume attached as a data volume shows up as `sdb`:```
lsblk
NAME  MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
sdb   8:16  0 46.6G 0 disk
├─sdb2  8:18  0  8G 0 part
├─sdb3  8:19  0 38.4G 0 part
└─sdb1  8:17  0 200M 0 part
sda   8:0  0 46.6G 0 disk
├─sda2  8:2  0  8G 0 part [SWAP]
├─sda3  8:3  0 38.4G 0 part /
└─sda1  8:1  0 200M 0 part /boot/efi
```

  4. Run the `fsck` command on the volume's root partition. The root partition is usually the largest partition on the volume.
The following sample for the `fsck` command shows the output when there are no errors or corruption present on the partitions for an Oracle 7.6 instance:
```
sudo fsck -V /dev/sdb1
fsck from util-linux 2.23.2
[/sbin/fsck.vfat (1) -- /boot/efi] fsck.vfat /dev/sdb1
fsck.fat 3.0.20 (12 Jun 2013)
/dev/sdb1: 17 files, 2466/51145 clusters
sudo fsck -V /dev/sdb2
fsck from util-linux 2.23.2
sudo fsck -V /dev/sdb3
fsck from util-linux 2.23.2
[/sbin/fsck.xfs (1) -- /] fsck.xfs /dev/sdb3
If you wish to check the consistency of an XFS filesystem or
repair a damaged filesystem, see xfs_repair(8).
```

If errors are present on a partition, you will usually be prompted to repair the errors. Following is an example of an interactive repair session of a corrupt ext4 boot volume for an Ubuntu instance:
```
sudo fsck -V /dev/sdb1
fsck from util-linux 2.31.1
[/sbin/fsck.ext4 (1) -- /] fsck.ext4 /dev/sdb1
e2fsck 1.44.1 (24-Mar-2018)
One or more block group descriptor checksums are invalid. Fix<y> yes
Group descriptor 92 checksum is 0xe9a1, should be 0x1f53. FIXED.
Pass 1: Checking inodes, blocks, and sizes
Pass 2: Checking directory structure
Pass 3: Checking directory connectivity
Pass 4: Checking reference counts
Pass 5: Checking group summary information
Block bitmap differences: Group 92 block bitmap does not match checksum.
FIXED.
cloudimg-rootfs: ***** FILE SYSTEM WAS MODIFIED *****
cloudimg-rootfs: 75336/5999616 files (0.1% non-contiguous), 798678/12181243 blocks
```

**Note**
XFS file systems will usually auto-repair their contents when the system boots up, fixing any corruption during the boot process. You can use the `xfs_repair` command to force a repair for scenarios where boot volume corruption is preventing the auto-repair functionality from working, as shown in the following example:
```
sudo xfs_repair /dev/sdb3
Phase 1 - find and verify superblock...
Phase 2 - using internal log
- zero log...
- scan filesystem freespace and inode maps...
...
Phase 7 - verify and correct link counts...
done
```



Was this article helpful?
YesNo

