Updated 2024-10-07
# Find Your Volume in the Instance
In Compute Cloud@Customer, when a block volume is initially attached to an instance, the instance sees the volume as a new disk, for example: as device `/dev/sdb`. This procedure describes how to list the disk devices in an instance so that you can find the volume and administer it in the OS.
For UNIX images, to mount these volumes when an instance boots, you need to add the volume to the `/etc/fstab` file. See [Configuring Volumes to Automatically Mount (Linux Instances)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/configuring-volumes-to-automatically-mount.htm#configuring-volumes-to-automatically-mount-linux "On Compute Cloud@Customer, for Linux instances, if you want to automatically mount volumes during an instance boot, you need add the volumes to the /etc/fstab file.").
Optionally, you can perform various administrative tasks to configure the storage to suit your storage requirements.
The utilities you use to perform the administrative tasks vary depending on the type of OS in the instance. For more administrative information, refer to the documentation for the version of the OS that's on the instance. These documentation libraries provide access to helpful information: 
  * Oracle Operating Systems Documentation: <https://docs.oracle.com/en/operating-systems/index.html>
  * Oracle Virtualization Documentation: <https://docs.oracle.com/en/virtualization/index.html>


## Identifying the Boot Volume and the Attached Block Volume Devices in the Instance Using Linux Commands 🔗 
  1. Log on to your instance. See [Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm). 
  2. List the disk devices.
**Important**
On UNIX OSs, the order in which volumes are attached is nondeterministic, so it can change with each reboot. If you refer to a volume using the device name, such as `/dev/sdb`, and you have more than one nonroot volume, there's no guarantee that the volume you intend to mount for a specific device name will be the volume mounted. When configuring the OS to recognize the block volume (for example, adding the volume to the `/etc/fstab` file), use the volume's SCSI ID as described in this procedure.
```
sudo ls /dev/sd*
/dev/sda /dev/sda1 /dev/sda2 /dev/sdb
```

In this example, two devices are listed, `/dev/sda` and `/dev/sdb`.
  3. Use the `fdisk` `-l` command to view configuration information about the devices.
In this example, `/dev/sda` is the boot volume and `/dev/sdb` is the attached block volume.
```
sudo fdisk -l
Disk **/dev/sda**: 53.7 GB, 53687091200 bytes, 104857600 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 8192 bytes / 8192 bytes
Disk label type: dos
Disk identifier: 0x000af694
  Device Boot Start End Blocks Id System
/dev/sda1 * 2048 2099199 1048576 83 Linux
/dev/sda2 2099200 61442047 29671424 8e Linux LVM
Disk /dev/mapper/ol-root: 27.2 GB, 27229421568 bytes, 53182464 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 8192 bytes / 8192 bytes

Disk /dev/mapper/ol-swap: 3145 MB, 3145728000 bytes, 6144000 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 8192 bytes / 8192 bytes

Disk **/dev/sdb**: 1099.5 GB, 1099511627776 bytes, 2147483648 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 8192 bytes / 8192 bytes
```

This example output provides this information about `/dev/sda` and `/dev/sdb`:
     * The size of `/dev/sda` is 53.7 GB (boot volume).
     * `/dev/sda` has two partitions: `/dev/sda1` and `/dev/sda2`.
     * The size of `/dev/sdb` is 1099.5 GB (the attached block volume), and doesn't have any partitions.
  4. Identify the devices that have file systems and are mounted in the OS. 
```
sudo df -T
Filesystem     Type   1K-blocks  Used Available Use% Mounted on
devtmpfs      devtmpfs 16318164    0 16318164  0% /dev
tmpfs        tmpfs   16332596    0 16332596  0% /dev/shm
tmpfs        tmpfs   16332596  8744 16323852  1% /run
tmpfs        tmpfs   16332596    0 16332596  0% /sys/fs/cgroup
/dev/mapper/ol-root xfs    26578248 2907292 23670956 11% /
/dev/sda1      xfs    1038336 292512  745824 29% /boot
tmpfs        tmpfs   3266520    0  3266520  0% /run/user/0
```

In this example:
     * `/dev/sda1` has an xfs file system and it's mounted on `/boot` (the boot volume). 
     * `/dev/sdb` isn't listed because this block volume was just attached and hasn't had a file system created and isn't mountable yet.
  5. Find the SCSI ID for the newly attached volume.
```
sudo ls -l /dev/disk/by-id
total 0
lrwxrwxrwx. 1 root root 10 Dec 6 18:26 dm-name-ol-root -> ../../dm-0
lrwxrwxrwx. 1 root root 10 Dec 6 18:26 dm-name-ol-swap -> ../../dm-1
lrwxrwxrwx. 1 root root 10 Dec 6 18:26 dm-uuid-LVM-83pr2aUrW2ZdCbWgsN4ZRFqvsXGGNZ8JO6il7j1YTWpywZeewYCiA6ywDmIeho1G -> ../../dm-0
lrwxrwxrwx. 1 root root 10 Dec 6 18:26 dm-uuid-LVM-83pr2aUrW2ZdCbWgsN4ZRFqvsXGGNZ8JsaUihE3RWozk5u4p5nOwG9sFcj34AU3F -> ../../dm-1
lrwxrwxrwx. 1 root root 10 Dec 6 18:26 lvm-pv-uuid-Dh9ydC-Rj90-chhj-tkwq-ZI0Z-mfop-Wtg5bh -> ../../sda2
lrwxrwxrwx. 1 root root 9 Dec 6 18:26 scsi-3600144f096933b92000061ae9bfc0025 -> ../../sda
lrwxrwxrwx. 1 root root 10 Dec 6 18:26 scsi-3600144f096933b92000061ae9bfc0025-part1 -> ../../sda1
lrwxrwxrwx. 1 root root 10 Dec 6 18:26 scsi-3600144f096933b92000061ae9bfc0025-part2 -> ../../sda2**
lrwxrwxrwx. 1 root root 9 Dec 8 15:17 scsi-3600144f096933b92000061b1129e0037 -> ../../sdb**
lrwxrwxrwx. 1 root root 9 Dec 6 18:26 wwn-0x600144f096933b92000061ae9bfc0025 -> ../../sda
lrwxrwxrwx. 1 root root 10 Dec 6 18:26 wwn-0x600144f096933b92000061ae9bfc0025-part1 -> ../../sda1
lrwxrwxrwx. 1 root root 10 Dec 6 18:26 wwn-0x600144f096933b92000061ae9bfc0025-part2 -> ../../sda2
lrwxrwxrwx. 1 root root 9 Dec 8 15:17 wwn-0x600144f096933b92000061b1129e0037 -> ../../sdb
```

In this example, the following line shows the SCSI ID assigned to `sdb`:
`lrwxrwxrwx. 1 root root 9 Dec 8 15:17 scsi-3600144f096933b92000061b1129e0037        -> ../../sdb`
where `scsi-3600144f096933b92000061b1129e0037` is the SCSI ID.
The SCSI ID is a persistent device name for `/dev/sdb` and is used when performing administrative operations on the device, such as partitioning, creating a file system, and mounting.
For more information about mounting a block volume file system to an instance, see [Configuring Volumes to Automatically Mount (Linux Instances)](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/configuring-volumes-to-automatically-mount.htm#configuring-volumes-to-automatically-mount-linux "On Compute Cloud@Customer, for Linux instances, if you want to automatically mount volumes during an instance boot, you need add the volumes to the /etc/fstab file.").
  6. Perform administrative tasks to configure the block volume to suit your storage requirements.
The specific tasks you perform depend on the type of OS that runs the instance and how you want the storage configured. Refer to your OS documentation for details.


Was this article helpful?
YesNo

