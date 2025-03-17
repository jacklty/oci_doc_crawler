Updated 2023-01-04
# Traditional fstab Options
On Linux instances, if you want to automatically mount volumes on instance boot, you need to set some specific options in the `/etc/fstab` file, or the instance may fail to launch.
**Note** These steps are for block volumes that do not have [consistent device paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#Connecting_to_Volumes_With_Consistent_Device_Paths) enabled. If consistent device paths are enabled for the block volume, use the [/etc/fstab options for block volumes using consistent device paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptionsconsistentdevicepaths.htm#fstab_Options_for_Block_Volumes_Using_Consistent_Device_Paths) instead.
## Volume UUIDs 🔗 
On Linux operating systems, the order in which volumes are attached is non-deterministic, so it can change with each reboot. If you refer to a volume using the device name, such as `/dev/sdb`, and you have more than one non-root volume, you can't guarantee that the volume you intend to mount for a specific device name will be the volume mounted.
To prevent this issue, specify the volume UUID in the `/etc/fstab` file instead of the device name. When you use the UUID, the mount process matches the UUID in the superblock with the mount point specified in the `/etc/fstab` file. This process guarantees that the same volume is always mounted to the same mount point.
### Determining the UUID for a Volume
  1. Follow the steps to [attach a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.") and [connect to the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm#top "Connect to a block volume that's attached to a compute instance.").
  2. After the volumes are connected, create the file system of your choice on each volume using standard Linux tools.
The remaining steps assume that three volumes were connected, and that an XFS file system was created on each volume. 
  3. Run the following command to use the **blkid** utility to get the UUIDs for the volumes:
Copy
```
sudo blkid
```

The output will look similar to the following:
```
{{ /dev/sda3: UUID="1701c7e0-7527-4338-ae9f-672fd8d24ec7" TYPE="xfs" PARTUUID="82d2ba4e-4d6e-4a33-9c4d-ba52db57ea61"}}
{{ /dev/sda1: UUID="5750-10A1" TYPE="vfat" PARTLABEL="EFI System Partition" PARTUUID="082c26fd-85f5-4db2-9f4e-9288a3f3e784"}}
{{ /dev/sda2: UUID="1aad7aca-689d-4f4f-aff0-e0d46fc1b89f" TYPE="swap" PARTUUID="94ee5675-a805-49b2-aaf5-2fa15aade8d5"}}
{{ /dev/sdb: UUID="699a776a-3d8d-4c88-8f46-209101f318b6" TYPE="xfs"}}
{{ /dev/sdd: UUID="85566369-7148-4ffc-bf97-50954cae7854" TYPE="xfs"}}
{{ /dev/sdc: UUID="ba0ac1d3-58cf-4ff0-bd28-f2df532f7de9" TYPE="xfs"}}
```

The root volume in this output is `/dev/sda*`. The additional remote volumes are:
     * `/dev/sdb`
     * `/dev/sdc`
     * `/dev/sdd`
  4. To automatically attach the volumes at `/mnt/vol1`, `/mnt/vol2`, and `/mnt/vol3` respectively, create the three directories using the following commands:
Copy
```
bash-4.2$ sudo mkdir /mnt/vol1
{{ bash-4.2$ sudo mkdir /mnt/vol2}}
{{ bash-4.2$ sudo mkdir /mnt/vol3}}
```



## Use the _netdev and nofail Options 🔗 
By default, the `/etc/fstab` file is processed before the initiator starts. Configure the mount process to initiate before the volumes are mounted by specifying the `_netdev` option on each line of the `/etc/fstab` file. 
When you create a custom image of an instance where the volumes, excluding the root volume, are listed in the `/etc/fstab` file, instances will fail to launch from the custom image. To prevent this issue, specify the `nofail` option in the `/etc/fstab` file.
In the example scenario with three volumes, the `/etc/fstab` file entries for the volumes with the `_netdev` and `nofail` options are as follows:
Copy
```

UUID=699a776a-3d8d-4c88-8f46-209101f318b6 /mnt/vol1 xfs defaults,_netdev,nofail 0 2
UUID=ba0ac1d3-58cf-4ff0-bd28-f2df532f7de9 /mnt/vol2 xfs defaults,_netdev,nofail 0 2
UUID=85566369-7148-4ffc-bf97-50954cae7854 /mnt/vol3 xfs defaults,_netdev,nofail 0 2
```

After you have updated the `/etc/fstab` file, use the following command to mount the volumes:
Copy
```
bash-4.2$ sudo mount -a

```

Reboot the instance to confirm that the volumes are mounted properly on reboot with the following command:
Copy
```
bash-4.2$ sudo reboot

```

## Troubleshooting Issues with the /etc/fstab File 🔗 
If the instance fails to reboot after you update the `/etc/fstab` file, you may need to undo the changes to the `/etc/fstab` file. To update the file, first [connect to the serial console for the instance](https://docs.oracle.com/iaas/Content/Compute/References/serialconsole.htm). When you have access to the instance using the serial console connection, you can remove, comment out, or fix the changes that you made to the `/etc/fstab` file.
Was this article helpful?
YesNo

