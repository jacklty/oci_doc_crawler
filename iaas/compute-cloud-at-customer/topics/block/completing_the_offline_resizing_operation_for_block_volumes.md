Updated 2023-08-15
# Completing the Offline Resizing Operation for Block Volumes
After resizing the offline block volume or boot volume, you need to perform the following administrative tasks.
  1. Reattach the volume.
See [Attaching a Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm#attaching-a-volume "You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance.").
  2. Rescan the disk.
For details, consult the OS documentation for the OS type and version running in the instance. Also see [Rescanning the Disk for a Block Volume or Boot Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/rescanningdisk.htm)
  3. Extend the partition.
For details, consult the OS documentation for the OS type and version running in the instance. Also see [Extending the Partition for a Block Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/extendingblockpartition.htm) and [Extending the Partition for a Boot Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/extendingbootpartition.htm).


Was this article helpful?
YesNo

