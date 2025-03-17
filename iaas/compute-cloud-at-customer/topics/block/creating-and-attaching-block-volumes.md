Updated 2023-08-15
# Creating and Attaching Block Volumes
You can create and attach a block volume to an instance to expand the available storage on the instance. The topics in this section describe how to administer the Block Volume Storage service for Compute Cloud@Customer.
To create and attach block volumes to an instance, you perform a series of tasks.
**Task Flow**
No. | Task | Links  
---|---|---  
1. |  Create a block volume. |  [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/creating-a-block-volume.htm#creating-a-block-volume "On Compute Cloud@Customer, block volumes are detachable block storage devices that you can use to dynamically expand the storage capacity of an instance.")  
2. |  Attach the block volume to one or more instances. |  [Attaching a Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm#attaching-a-volume "You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance.") or [Attaching a Volume to Multiple Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume-to-multiple-instances.htm#attaching-a-volume-to-multiple-instances "The Compute Cloud@Customer Block Volume service provides the capability to attach a block volume to multiple compute instances. With this feature, you can share block volumes across instances in read/write or read-only mode.")  
3. | Identify the added block volume and perform administrative tasks. | [Find Your Volume in the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/find-your-volume-in-the-instance.htm#find-volume-in-the-instance "In Compute Cloud@Customer, when a block volume is initially attached to an instance, the instance sees the volume as a new disk, for example: as device /dev/sdb. This procedure describes how to list the disk devices in an instance so that you can find the volume and administer it in the OS.")  
4. |  Configure the volume to automatically mount when the instance is rebooted. |  [Find Your Volume in the Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/find-your-volume-in-the-instance.htm#find-volume-in-the-instance "In Compute Cloud@Customer, when a block volume is initially attached to an instance, the instance sees the volume as a new disk, for example: as device /dev/sdb. This procedure describes how to list the disk devices in an instance so that you can find the volume and administer it in the OS.")  
Was this article helpful?
YesNo

