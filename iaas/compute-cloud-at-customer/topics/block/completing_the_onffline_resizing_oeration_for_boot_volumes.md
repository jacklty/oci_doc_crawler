Updated 2023-08-15
# Completing the Offline Resizing Operation for Boot Volumes
After resizing the online block volume or boot volume, you need to perform the following administrative tasks.
  1. Attach the boot volume to a second instance as a data volume.
See [Attaching a Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm#attaching-a-volume "You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance.").
  2. Extend the partition and grow the file system.
For details, consult the OS documentation for the OS type and version running in the instance.
  3. Detach the data volume.
See [Detaching a Block Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/detaching-a-block-volume.htm#detaching-a-block-volume "On Compute Cloud@Customer, when an instance no longer needs access to a volume, you can detach the volume from the instance without affecting the volume's data.").
  4. Reattach the boot volume.
See [Reattaching a Boot Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/reattaching-a-boot-volume.htm#reattaching-a-boot-volume "On Oracle Cloud Infrastructure, you can reattach a boot volume to an instance.").
  5. Restart the instance.
See [Stopping, Starting, and Resetting an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-starting-and-resetting-an-instance.htm#stopping-starting-and-resetting-an-instance "On Compute Cloud@Customer, you can control the state of an instance using the Compute Cloud@Customer Console, CLI, and API.").


Was this article helpful?
YesNo

