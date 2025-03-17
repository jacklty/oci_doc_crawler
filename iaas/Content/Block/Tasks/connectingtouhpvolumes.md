Updated 2023-09-26
# Working with Multipath-Enabled iSCSI-Attached Volumes
When you attach a volume configured for the **Ultra High Performance** level, to optimize performance, the volume attachment must be enabled for multipath.
For more information, see [Attaching Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#multipath). For how to confirm that the iSCSI attachment is multipath-enabled, see [Checking if a Volume Attachment is Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/multipathcheck.htm#multipathcheck "When you attach a volume configured for the Ultra High Performance level, the volume attachment must be enabled for multipath to optimize the volume's performance. This topic describes how to verify if the volume attachment is multipath-enabled.").
This topic describes how to work with iSCSI-attached volumes that are multipath-enabled.
## Device Path 🔗 
A device path is required for multipath-enabled volume attachments. When attaching a volume configured for the **Ultra High Performance** level, using the iSCSI attachment type, the **Attach** button is not enabled until you select a device path. For more information about device paths, see [Connecting to Volumes With Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#Connecting_to_Volumes_With_Consistent_Device_Paths).
If you change the performance of an attached volume to the **Ultra High Performance** level and it was attached without a device path, it will not be multipath-enabled. This means that it will not be capable of the **Ultra High Performance** level numbers, until you specify a device path. You need to detach the volume, and then specify a device path when you reattach it to the instance. 
## Determining the Friendly Name 🔗 
To determine the friendly name for the multipath-enabled attached volume, connect to the instance and run the following command:
Copy
```
ls -l <Consistent_Device_Path>
```

If you have the friendly name for the device, run the following command to retrieve the device path name
Copy
```
sudo multipath -ll <Friendly_Name>
```

## Create the Partition with fdisk 🔗 
Use `fdisk` to partition the multipath-enabled volume, and use the `n` option to specify that it's a new partition.
Copy
```
fdisk <Friendly_Name
```

Use the `p` option to make it the primary partition.
Run the following command to list the partitions:
```
lsblk
```

## Create the File System 🔗 
Run the following command to create the file system:
Copy
```
mkfs.ext4 <Friendly_Name>
```

Run the following commands to create a directory and mount the partition on the mount point:
Copy
```
mkdir /data 
```

Copy
```
mount <Friendly_Name> /data
```

## fstab Options 🔗 
On Linux instances, if you want to automatically mount volumes on instance boot, you need to set some specific options in the `/etc/fstab` file, or the instance may fail to launch.
### Retrieving the Volume UUID
Run the following command to use the `blkid` utility to get the UUIDs for the volume
```
blkid
```

For more information about this, see [Volume UUIDs](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptions.htm#Volume_UUIDs).
### Use the _netdev Option
Add the following to the `/etc/fstab` file
Copy
```
<Volume_UUID> /data ext4 defaults,_netdev,noatime 0 2
```

After you've updated the `/etc/fstab` file, run the following command to mount the volume:
```
mount -a
```

Was this article helpful?
YesNo

