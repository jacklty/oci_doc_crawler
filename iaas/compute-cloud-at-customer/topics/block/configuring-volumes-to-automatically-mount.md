Updated 2024-10-07
# Configuring Volumes to Automatically Mount (Linux Instances)
On Compute Cloud@Customer, for Linux instances, if you want to automatically mount volumes during an instance boot, you need add the volumes to the `/etc/fstab` file.
**Before You Begin**
Get the SCSI ID for the block volume you plan to mount. See [Find Your Volume in the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/find-your-volume-in-the-instance.htm#find-volume-in-the-instance "In Compute Cloud@Customer, when a block volume is initially attached to an instance, the instance sees the volume as a new disk, for example: as device /dev/sdb. This procedure describes how to list the disk devices in an instance so that you can find the volume and administer it in the OS.").
On Linux operating systems, specify the volume SCSI ID in the `/etc/fstab` file instead of the device name (for example, `/dev/sdb`). This is an example of a Volume SCSI ID:
```
/dev/disk/by-id/scsi-3600144f096933b92000061b1129e0037
```

## Adding Volumes to the `/etc/fstab` File 🔗 
  1. Prepare the newly attached block volume for mounting.
Use the disk administration utilities included with instance OS to perform tasks such as the following:
     * Partition the volume
     * Create file systems on the volume or partitions
Consult the documentation for your instance OS for details.
This is an example of creating an ext4 file system for a block volume attached to a Linux instance:
```
mkfs.ext4 /dev/disk/by-id/scsi-3600144f096933b92000061b1129e0037
mke2fs 1.42.9 (28-Dec-2013)
/dev/disk/by-id/scsi-3600144f096933b92000061b1129e0037 is entire device, not just one partition!
Proceed anyway? (y,n) y
Filesystem label=
OS type: Linux
Block size=4096 (log=2)
Fragment size=4096 (log=2)
Stride=2 blocks, Stripe width=2 blocks
67108864 inodes, 268435456 blocks
13421772 blocks (5.00%) reserved for the super user
First data block=0
Maximum filesystem blocks=2415919104
8192 block groups
32768 blocks per group, 32768 fragments per group
8192 inodes per group
Superblock backups stored on blocks:
    32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
    4096000, 7962624, 11239424, 20480000, 23887872, 71663616, 78675968,
    102400000, 214990848
Allocating group tables: done
Writing inode tables: done
Creating journal (32768 blocks): done
Writing superblocks and filesystem accounting information: done
```

  2. Create a mount point for each file system you plan to mount.
```
mkdir /mnt/volume1
```

  3. Add the volume to the `/etc/fstab` file.
For this example, the following new line is added to the `/etc/fstab` file:
```
/dev/disk/by-id/scsi-3600144f096933b92000061b1129e0037 /mnt/volume1 ext4 _netdev,nofail 0 0
```

Following are descriptions of these field values:
     * **Device:** Specified using the SCSI ID:
```
/dev/disk/by-id/scsi-3600144f096933b92000061b1129e003
```

     * **Mount point:** The mount point created in the previous step: `/mnt/volume1`
     * **Type:** The type of file system: `ext4` in this example.
     * **Options:**
       * `_netdev` – Configures the mount process to initiate before the volumes are mounted.
       * `nofail` – If the device does not exist, no errors are reported. This is a good option to use when an instance is used to create a custom image. Future instances created with that image will not include the block volume and might fail to boot without this option.
     * **Dump:** The value `0` means do not use the obsolete `dump` utility.
     * **fsck:** The value `0` means do not run `fsck`.
  4. Use the following command to mount the volumes that are in the `/etc/fstab` file:
```
sudo mount -a
```

  5. Verify that the file system is mounted:
```
mount | grep /mnt
/dev/sdb on /mnt/volume1 type ext4 (rw,relatime,seclabel,stripe=2,data=ordered,_netdev)
```



Was this article helpful?
YesNo

