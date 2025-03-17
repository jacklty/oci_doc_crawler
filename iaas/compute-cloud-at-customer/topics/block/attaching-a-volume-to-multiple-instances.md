Updated 2024-10-07
# Attaching a Volume to Multiple Instances
The Compute Cloud@Customer Block Volume service provides the capability to attach a block volume to multiple compute instances. With this feature, you can share block volumes across instances in read/write or read-only mode.
Attaching block volumes as read/write and shareable enables you to deploy and manage cluster-aware solutions.
**Important**
If you're attaching a volume that was detached, the volume might be associated with a different device name and the instance OS might not recognize the volume.
## Limits and Considerations 🔗 
  * The Block Volume service doesn't provide coordination for concurrent write operations to block volumes attached to multiple instances, so if you configure the block volume as read/write and shareable, you must deploy a cluster aware system or solution on top of the shared storage.
  * After you attach a block volume to an instance as read-only, it can only be attached to other instances as read-only. To attach the block volume to an instance as read/write, you need to detach the block volume from all instances and then you can reattach the block volume to instances as read/write.
  * If the block volume is already attached to an instance as read/write nonshareable you can't attach it to another instance until you detach it from the first instance. You can then reattach it to both the first and second instances as read/write shareable.
  * You can't delete a block volume until it has been detached from all instances it was attached to. 
  * You can attach a block volume as read/write shareable or read-only shareable up to a maximum of eight instances.
  * Block volumes attached as read-only are configured as shareable by default.
  * Performance characteristics are per volume, so when a block volume is attached to multiple instances the performance is shared across all the attached instances.


## Configuring Multiple Instance Volume Attachments with Read/Write Access 🔗 
The Block Volume service doesn't provide coordination for concurrent write operations to volumes attached to multiple instances. To prevent data corruption from uncontrolled read/write operations, you must install and configure a cluster aware system or solution such as Oracle Cluster File System version 2 (OCFS2) on top of the shared storage before you can use the volume.
**Summary of the required steps:**
  1. Attach the block volume to an instance as Read/Write and Shareable using the Compute Cloud@Customer Console, CLI, or API. 
See [Attaching a Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm#attaching-a-volume "You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance."). 
  2. Set up your OCFS2/O2CB cluster nodes.
  3. Create your OCFS2 file system and mount point.


## Configuring Multiple Instance Volume Attachments with Read-Only Mode  🔗 
Once you attach a block volume to an instance as read-only, it can only be attached to other instances as read-only. To attach the block volume to an instance as read/write, you need to detach the block volume from all instances and then you can reattach the block volume to instances as read/write.
  1. Attach the block volume to an instance as read-only using the Compute Cloud@Customer Console, CLI, or API.
See [Attaching a Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm#attaching-a-volume "You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance.").
  2. Attach the block volume to additional instances as read-only using the Compute Cloud@Customer Console, CLI, or API.
See [Attaching a Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm#attaching-a-volume "You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance.").


Was this article helpful?
YesNo

