Updated 2024-10-07
# Accessing a Snapshot on the Mounted File System
On Compute Cloud@Customer, when a file system snapshot is created, the snapshot is placed in the file system. If the file system is mounted in a client system, you can access the snapshot on the client system.
The snapshot is accessible in this directory path: `<mount-point>`/.zfs/snapshot/`<snapshot-name>`.
## From a UNIX OS Client 🔗 
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

  3. Change to the directory of a snapshot.
Example:
```
cd /mnt/MyMountPoint/.zfs/snapshot/file-system-FS-snapshot-02
```

  4. List the contents of the snapshot.
```
ls -la
total 3027
drwxr-xr-x. 4 root root    7 Sep 8 15:53 .
dr-xr-xr-x. 4 root root    4 Sep 8 15:54 ..
-rwxr-xr-x. 1 root root   429 Sep 8 15:53 example1
drwxr-x---. 2 root sys    3 Sep 1 17:28 .$EXTEND
drwxr-xr-x. 2 root root    2 Sep 1 18:10 ABC-directory
-rw-r--r--. 1 root root    0 Sep 1 18:10 xyz-file
-rw-r--r--. 1 root root 3073219 Sep 1 18:12 zap.zip
```



Was this article helpful?
YesNo

