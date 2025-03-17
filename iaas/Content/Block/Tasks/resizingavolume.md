Updated 2024-06-04
# Resizing a Volume
The Oracle Cloud Infrastructure Block Volume service lets you expand the size of block volumes and boot volumes. You have several options to increase the size of your volumes:
  * Expand an existing volume in place with online resizing. See [Online Resizing of Block Volumes Using the Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm#OnlineResize) for the steps to do this.
  * Restore from a volume backup to a larger volume. See [Restoring a Backup to a New Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringavolumefromabackup.htm#Restoring_a_Backup_to_a_New_Volume) and [Restoring a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingbootvolume.htm#Restoring_a_Boot_Volume).
  * Clone an existing volume to a new, larger volume. See [Cloning a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm#Cloning_a_Volume "Create a clone from a volume by using the Block Volume service. Cloning lets you to make a copy of an existing block volume without needing to go through the backup and restore process.") and [Cloning a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningabootvolume.htm#Cloning_a_Boot_Volume).
  * Expand an existing volume in place with offline resizing. See [Offline Resizing of Block Volumes Using the Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm#offlineResize) for the steps to do this.


For more information about the Block Volume service, see the[ Block Volume FAQ](https://cloud.oracle.com/infrastructure/storage/block-volume/faq).
You can only increase the size of the volume, you cannot decrease the size. 
**Note** If cross-region replication is enabled for the volume you want to resize, before you resize the volume, you must disable cross-region replication. Once the volume is resized, you can renable cross-region replication for the volume. For more information about this feature, see [Replicating a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication "The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of block volumes, boot volumes, and volume groups to other regions and availability domains.").
**Note**
Resizing IDE type boot volumes is not supported. This applies to both offline and online resizing. To workaround this limitation, you can do one of the following:
  * Terminate the VM instance, ensuring that you keep the boot volume when you terminate the instance. Resize the boot volume that you have kept, and then launch a new VM instance, using the resized boot volume as the image source.
  * Create a clone of the boot volume, resize the boot volume clone, and then launch a new VM instance using the resized boot volume clone as the image source.


**Caution** Before you resize a boot or block volume, you should create a backup of the volume.
**Note** After a volume has been resized, the first backup on the resized volume will be a full backup. See [Volume Backup Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumebackups.htm#backuptype) for more information about full versus incremental volume backups. 
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) includes the ability to attach/detach existing block volumes. The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes and backups, but not launch instances. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Online Resizing of Block Volumes Using the Console 🔗 
With online resizing, you can expand the volume size without detaching the volume from an instance. 
[To resize a block volume attached to a Linux-based instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. In the **Block Volumes** list, click the block volume you want to resize.
  3. Click **Edit Size or Performance**.
  4. Specify the new size in **VOLUME SIZE (IN GB)**. You must specify a larger value than the block volume's current size.
  5. Click **Save Changes**. This opens a dialog that lists the commands to rescan the disk that you need to run after the volume is provisioned. You need to run these commands so that the operating system identifies the expanded volume size. Click the **Copy** link to copy the commands, and then click **Close** to close the dialog. 
  6. Log on to your instance's OS and then paste and run the rescan commands you copied in the previous step into your instance session window. The rescan commands are also provided in [Rescanning the Disk for Volumes Attached to Linux-Based Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm#Rescanni).
  7. Extend the partition, see [Extending the Partition for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm#Extending_the_Partition_for_a_Block_Volume).


[To resize a block volume attached to a Windows instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm)
This procedure describes the process for online resizing for block volumes attached to Windows instances, or other instance types that are not Linux-based.
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. In the **Block Volumes** list, click the block volume you want to resize.
  3. Click **Edit Size or Performance**.
  4. Specify the new size in **VOLUME SIZE (IN GB)**. You must specify a larger value than the block volume's current size.
  5. Click **Save Changes**. 
  6. Rescan the disk, see [Rescanning the Disk for Volumes Attached to Windows Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm#Rescanni2). 
  7. Extend the partition, see [Extending the Partition for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm#Extending_the_Partition_for_a_Block_Volume).


[To resize a boot volume for a Linux-based Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. In the **Boot Volumes** list, click the boot volume you want to resize.
  3. Click **Edit Size or Performance**.
  4. Specify the new size in **VOLUME SIZE (IN GB)**. You must specify a larger value than the boot volume's current size.
  5. Click **Save Changes**. This opens a dialog that lists the commands to rescan the disk that you need to run after the volume is provisioned. You need to run these commands so that the operating system identifies the expanded volume size. Click the **Copy** link to copy the commands, and then click **Close** to close the dialog. 
  6. Log on to your instance's OS and then paste and run the rescan commands you copied in the previous step into your instance session window. The rescan commands are also provided in [Rescanning the Disk for Volumes Attached to Linux-Based Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm#Rescanni).
  7. Extend the partition and grow the file system using the `oci-growfs[](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm#oci-growfs)` operation from [OCI Utilities](https://docs.oracle.com/iaas/oracle-linux/oci-utils/index.htm). 


[Resizing a Boot Volume for a Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. In the **Boot Volumes** list, click the boot volume you want to resize.
  3. Click **Resize**.
  4. Click **Save Changes**. 
  5. Rescan the disk, see [Rescanning the Disk for Volumes Attached to Windows Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/rescanningdisk.htm#Rescanni2).
  6. Extend the partition, see [Extending the System Partition on a Windows-Based Image](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm#Extendin).


## Offline Resizing of Block Volumes Using the Console 🔗 
With offline resizing, you detach the volume from an instance before you expand the volume size. Once the volume is resized and reattached, you need to extend the partition, but you do not need to rescan the disk. 
### Considerations When Resizing an Offline Volume
Whenever you detach and reattach volumes, there are complexities and risks for both Linux-based and Windows-based instances. This applies to both paravirtualized and iSCSI attachment types. You should keep the following in mind when resizing volumes:
  * When you reattach a volume to an instance after resizing, if you are not using consistent device paths, or the instance does not support consistent device paths, device order and path may change. If you are using a tool such as Logical Volume Manager (LVM), you may need to fix the device mappings. For more information about consistent device paths, see [Connecting to Volumes With Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#Connecting_to_Volumes_With_Consistent_Device_Paths).
  * When you detach and then reattach an iSCSI-attached volume to an instance, the volume's IP address will increment.
  * Before you resize a volume, you should create a full backup of the volume.


[To resize a block volume attached to a Linux-based instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm)
  1. Detach the block volume, see [Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#Detaching_a_Volume "Detach a block volume from an instance.").
  2. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  3. In the **Block Volumes** list, click the block volume you want to resize.
  4. Click **Edit Size or Performance**.
  5. Specify the new size in **VOLUME SIZE (IN GB)**. You must specify a larger value than the block volume's current size.
  6. Click **Save Changes**. This opens a dialog that lists the required steps to complete the volume resize. For offline resizing, you need to extend the partition after you reattach the volume. Click **Close** to close the dialog. 
  7. Reattach the volume, see [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.").
  8. Extend the partition, see [Extending the Partition for a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingblockpartition.htm#Extending_the_Partition_for_a_Block_Volume).


[Resizing a Boot Volume for a Windows Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm)
  1. Stop the instance, see [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm).
  2. Detach the boot volume, see [Detaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingabootvolume.htm#Detaching_a_Boot_Volume).
  3. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  4. In the **Boot Volumes** list, click the boot volume you want to resize.
  5. Click **Edit Size or Performance**.
  6. Specify the new size in **VOLUME SIZE (IN GB)**. You must specify a larger value than the block volume's current size.
  7. Reattach the boot volume, see [Attaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingabootvolume.htm#Attaching_a_Boot_Volume).
  8. Restart the instance, see [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm).
  9. Extend the partition, see [Extending the System Partition on a Windows-Based Image](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm#Extendin).


[Resizing a Boot Volume for a Linux Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/resizingavolume.htm)
  1. Stop the instance, see [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm).
  2. Detach the boot volume, see [Detaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingabootvolume.htm#Detaching_a_Boot_Volume).
  3. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  4. In the **Boot Volumes** list, click the boot volume you want to resize.
  5. Click **Edit Size or Performance**.
  6. Specify the new size in **VOLUME SIZE (IN GB)**. You must specify a larger value than the block volume's current size.
  7. Attach the boot volume to a second instance as a data volume. See [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.") and [Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm#top "Connect to a block volume that's attached to a compute instance."). 
  8. Extend the partition and grow the file system, see [Extending the Root Partition on a Linux-Based Image](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/extendingbootpartition.htm#Extendin2).
  9. Reattach the boot volume, see [Attaching a Boot Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingabootvolume.htm#Attaching_a_Boot_Volume).
  10. Restart the instance, see [Stopping, Starting, or Restarting an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/restartinginstance.htm).


Was this article helpful?
YesNo

