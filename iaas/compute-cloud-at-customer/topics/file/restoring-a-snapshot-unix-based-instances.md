Updated 2024-10-07
# Restoring a Snapshot (UNIX-Based Instances)
On Compute Cloud@Customer, you can restore individual snapshot files or an entire snapshot using the `cp` command.
**Note**
Optionally, you can use `rsync`, `tar`, or another tool that supports NFS to copy your data to another remote location.
## Using the Instance OS 🔗 
  1. Log into the instance OS that has the mounted the file system from which the snapshot was made.
  2. List the snapshots.
Syntax:
```
ls -la **_<mount-point>_**/.zfs/snapshot/
```

Example:
```
ls -la /mnt/MyMountPoint/.zfs/snapshot
total 17
dr-xr-xr-x. 4 root root 4 Sep 8 15:54 .
dr-xr-xr-x. 4 root root 4 Sep 1 17:27 ..
drwxr-xr-x. 4 root root 7 Sep 8 15:53 file-system-FS-snapshot-02
drwxr-xr-x. 4 root root 6 Sep 1 18:12 file-system-FS-snapshot-01
```

  3. Use the `cp` command to copy individual snapshot files, or the entire snapshot to a location of your choice.
Use the `-r` option when restoring a snapshot that contains subdirectories.
Example:
```
cp -r /mnt/MyMountPoint/.zfs/snapshot/**_<snapshot_name>_**/* **_<destination_directory>_**
```



Was this article helpful?
YesNo

