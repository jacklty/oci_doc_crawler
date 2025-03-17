Updated 2023-11-21
# Configuring a File System to Automatically Mount (Linux Instances)
On Linux instances, if you want to automatically mount exported file systems during an instance boot, you need to add the mount information in the `/etc/fstab` file.
  1. Log into the instance where you want the file system mounted.
See [Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm).
  2. Create a mount point, if one hasn't been created.
Example:
```
mkdir /mnt/fs01
```

  3. Open the `/etc/fstab` file in an editor and add a line for the nfs file systems you want automatically mounted.
This is an example of an `/etc/fstab` file entry.
```
192.0.2.0:/export/3ywflz8hhqfde81miewqwjfd049zju69502t9ouo6shzidr4dndaz1hd6qfi /mnt/fs01 nfs nfsvers=4.1,nosuid,nofail 0 0
```

The `/etc/fstab` file space-separated fields are specified with these entries:
     * **Field 1:** Device to mount. For network file systems, specify: **_< mount target IP>_** `:` **_< export_path>_**
See [Obtaining the Mount Target IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/obtaining-the-mount-target-ip-address.htm#obtaining-the-muont-target-ip-address) and [Creating an Export for a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm#creating-an-export-for-a-file-system "On Compute Cloud@Customer, exports control how NFS clients access file systems when they connect to a mount target. A file system must have at least one export in one mount target for instances to mount the file system.").
     * **Field 2:** Full path of the mount point on the instance.
     * **Field 3:** File system type. In this case, specify `nfs`.
     * **Field 4:** NFS mount options separated with commas, such as: 
```
nfsvers=**_<version>_**,nosuid,nofail
```

       * `nfsvers=` where **_< version>_** is one of the following:
         * `3,noacl`
         * `4.0`
         * `4.1`
       * `nosuid `– prevents unprivileged users from escalating their permissions to root.
       * `nofail `– Ensures that an unavailable file system does not cause the instance reboot process to fail.
In this case, use the same options as described in [Mounting a File System on Linux, Red Hat, or CentOS](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/mounting-a-file-system-on-linux-redhat-or-centos.htm#mounting-a-file-system-on-linux-redhat-or-centos). Each option is separated by a comma (no spaces).
     * **Field 5:** Obsolete option for dump backups. Specify `0` (zero) for no dump backup.
     * **Field 6:** File system check (fsck) order. Specify `0` (zero) for no check.
  4. Use this command to mount the volumes that are in the `/etc/fstab` file:
```
sudo mount -a
```

If you get any error messages, fix the cause before proceeding. 
  5. Verify that the file systems are mounted: 
```
mount | grep nfs
```

  6. To verify that the file system will automatically mount, reboot the instance.
```
sudo reboot

```

  7. After the reboot, log into the instance and check to see if the nfs file system is mounted.
```
mount | grep nfs
```



Was this article helpful?
YesNo

