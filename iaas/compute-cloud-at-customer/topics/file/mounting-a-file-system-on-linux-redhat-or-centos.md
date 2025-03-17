Updated 2023-11-21
# Mounting a File System on Linux, Red Hat, or CentOS
  1. Log into the instance where you want to mount the file system.
See [Connecting to an Instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/accessinginstance.htm).
Example:
```
ssh user@192.0.2.0
```

  2. Install the NFS client using this command:
```
sudo yum install nfs-utils
```

  3. Create a directory that will be used as the mount point. 
Replace <yourmountpoint> with a directory name of your choice. Example: `/mnt/mountpoint-A`
```
sudo mkdir -p <yourmountpoint>
```

  4. Mount the file system.
**Caution**
Omitting the `-o nosuid` option can allow unprivileged users to escalate their permissions to 'root'. The `nosuid` option disables set-user-identifier or set-group-identifier bits within the mounted system, which are rarely used. 
Example:
```
sudo mount -t nfs -o nfsvers=<version>,nosuid <10.x.x.x>:<fs-export-path> <yourmountpoint>
```

     * Replace <version> with one of the following, based on the NFS protocol version you want to use:
       * 3,noacl
       * 4.0
       * 4.1
     * Replace <10.x.x.x> with the mount target's private IP address. See [Obtaining the Mount Target IP Address](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/obtaining-the-mount-target-ip-address.htm#obtaining-the-muont-target-ip-address).
     * Replace <fs-export-path> with the export path that was generated when the export was created. See [Creating an Export for a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm#creating-an-export-for-a-file-system "On Compute Cloud@Customer, exports control how NFS clients access file systems when they connect to a mount target. A file system must have at least one export in one mount target for instances to mount the file system.").
     * Replace <yourmountpoint>with the full path to the local mount point.
  5. View the mounted file system.
```
df -h
```

  6. Write a file to the file system. 
Replace <yourmountpoint> with the path to the local mount point and <filename>with your file name. 
```
sudo touch /mnt/**_<yourmountpoint>_**/**_<filename>_**
```

  7. Verify that you can access the file system and view the file. 
Replace yourmountpoint with the path to the local mount point. 
```
cd <yourmountpoint>
ls
```

  8. Add the file system mount information to the appropriate mount file for your OS.
So far, the file system is manually mounted to the client. If the client is rebooted, the file system won't automatically mount unless you add it to the mount file (for example the `/etc/fstab` or `/etc/vfstab` file).


Was this article helpful?
YesNo

