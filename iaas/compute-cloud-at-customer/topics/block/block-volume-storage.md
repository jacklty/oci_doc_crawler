Updated 2024-12-16
# Block Volume Storage
On Compute Cloud@Customer, Block Volumes provide high-performance network storage capacity that supports a broad range of I/O intensive workloads. 
## Block Volume Overview 🔗 
A block volume is a detachable block storage device that enables you to dynamically expand the storage capacity of your compute instances, provide durable and persistent data storage that can be migrated across compute instances, and host large databases. 
The Block Volume service enables you to group multiple volumes in a volume group. Volume groups simplify the process to create backups and clones. 
You can create, attach, connect, and move volumes, and change volume performance to meet your storage, performance, and application requirements. 
After you attach and connect a volume to a compute instance, you can use the volume like a regular hard drive. You can also disconnect a volume and attach it to another compute instance without the loss of data. 
The default size for block volumes is 1024 GB (1TB). Block volume size range is 50 GB to 32768 GB (32 TB). 

Types of Block Volumes
    
  * **Boot volume** : A detachable boot volume device that contains the image that's used to boot a Compute instance.
  * **Block volume** : A detachable block storage device that lets you to dynamically expand the storage capacity of an instance.


You can create, attach, connect, and move volumes, and change volume performance to meet your storage, performance, and application requirements. 
After you attach and connect a volume to a compute instance, you can use the volume like a regular hard drive. You can also disconnect a volume and attach it to another compute instance without the loss of data. 
When a volume is created, the volume is thin (sparse) provisioned: The volume consumes only the space that has been written to the volume. When the volume is attached to an instance, the volume is thick (non-sparse) provisioned: The volume reserves exactly enough space to completely fill the volume. This behavior avoids out-of-space errors. When the volume is detached, the volume is again thin provisioned if it is not still attached to another instance. 

Required Components
    
These components are required to create a volume and attach it to a compute instance:
  * **Compute Instance** : A virtual machine (VM) running in the Compute Cloud@Customer.
  * **Volume attachment** : A paravirtualized attachment that's available for compute instances.
  * **Volume** : A block volume or boot volume.



Volume Access Types
    
When you attach a block volume, you can specify one of the following access types: 
  * **Read/write:** This is the default option for volume attachments. With this option, an instance can read and write data to the volume. 
  * **Read/write, shareable:** With this option, you can attach a volume to more than one instance at a time and those instances can read and write data to the volume. To prevent data corruption from uncontrolled read/write operations with multiple instance volume attachments you must install and configure a cluster-aware solution before you can use the volume. 
  * **Read-only:** With this option, an instance can only read data on the volume. It can't update data on the volume. Specify this option to safeguard data against accidental or malicious modifications.


The access type for boot volumes is always read/write.
## Block Volume Performance Options 🔗  

Elastic Performance
    
When you create block storage, you can optionally enable High performance. By default, the volume is created with balanced performance. The volume performance setting can't be changed after the volume is created.
  * **High performance** : The High performance option is recommended for workloads with higher I/O requirements.
  * **Balanced performance** : The Balanced performance option is the default for new and existing block and boot volumes. This performance option provides a good balance between performance and cost savings for most workloads, including workloads that perform random I/O such as boot volumes.



Performance Limitations and Considerations
    
The following performance results are for unformatted data volumes.
  * Throughput performance on compute instances depends on the network bandwidth that's available to the compute instance, and further limited by that bandwidth for the volume.
  * If Microsoft Defender Advanced Threat Protection (Microsoft Defender ATP) is enabled in an instance, it has a significant negative impact on disk I/O performance. However, consider the security implications of disabling Microsoft Defender ATP.
  * Block volume performance is per volume, so when a block volume is attached to multiple compute instances, the performance is shared across all the attached compute instances.


## Block Volume Scenarios 🔗  

Adding Storage Capacity
    
A common use of a block volume is to add storage capacity to an instance. After you create an instance and set up a cloud network, you can create a block storage volume. Then, you attach the volume to a compute instance using a volume attachment. The volume can then be mounted and used by your compute instance. 

Moving a Volume to Another Compute Instance
    
A block volume can be detached from a compute instance and moved to a different compute instance without the loss of data. This data persistence lets you to migrate data between compute instances and ensures that data is safely stored, even when it's not connected to a compute instance. Any data remains intact until you delete the volume.
To move the volume to another compute instance, unmount the drive from the initial compute instance, detach the block volume, then attach the volume to another compute instance. From there, you connect and mount the drive from that instance's guest OS to have access to the data. 

Scaling a Compute Instance 
    
When you delete a compute instance, you can keep the associated boot volume and use it to create a new compute instance with a different compute instance type or shape. This capability lets you to easily scale up or scale down the number of cores for a compute instance.
## Volume Backups and Clones 🔗 
**Backup and Restore**
Backup and restore operations are supported on boot volumes, data volumes, and volume groups. All backups are full backups, not incremental.
To back up a boot volume, block volume, or volume group, use one of the following methods:
  * **Clone** : Cloning volumes enables you to create a copy without performing the backup and restore operations. For more information about clones, see the "Clones" section and "Differences Between Volume Clones and Backups" table below. For general information about cloning boot volumes, see [Cloning a Boot Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/cloning-a-boot-volume.htm#cloning-a-boot-volume "On Oracle Cloud Infrastructure, you can create a clone from a boot volume using the Block Volume service. Cloning enables you to make a copy of an existing boot volume without needing to go through the backup and restore process.").
  * **Manual backup** : These backups are performed one time as soon as you create the backup. These backups are retained indefinitely, or until a policy-based (scheduled) backup is created for this volume.
  * **Scheduled backups** : These backups are performed periodically according to a schedule defined in a backup policy. The policy schedule specifies the frequency (period) and time of the backups, and how long to retain the backups. You can create your own backup policies, or you can use Oracle provided backup policies.


**Oracle Provided Backup Policies**
Oracle defined backup policies cannot be used to back up a volume group. These policies can be used to back up individual block volumes and boot volumes.
Oracle defined policies cannot be changed. If you need a different backup time or retention time, for example, create a user defined backup policy as described in [Managing Backup Policies](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/managing-backup-policies.htm#managing-backup-policies "On Compute Cloud@Customer, you can perform volume backups and volume group backups automatically using a schedule, and retain them based on the retention setting in the backup policy.").
The following backup policies are provided by Oracle and available in every compartment. A resource can have only one backup policy assigned, but a backup policy can have multiple schedules. The Oracle Bronze policy has one schedule, the Silver policy has two schedules, and the Gold policy has three schedules. All schedule times are your regional data center time. All backup types are full backups. 

**Bronze** 
    
  1. Monthly backups that run at 00:00 on the first day of the month and are retained for twelve months.



**Silver** 
    
  1. Weekly backups that run at 00:00 every Monday and are retained for four weeks.
  2. Monthly backups that run at 00:00 on the first day of the month and are retained for twelve months.



**Gold** 
    
  1. Daily backups that run at 00:00 and are retained for seven days.
  2. Weekly backups that run at 00:00 every Monday and are retained for four weeks.
  3. Monthly backups that run at 00:00 on the first day of the month and are retained for twelve months.


The Block Volume service will not run more than one scheduled backup of a particular resource in one day. When schedules conflict, for example, daily, weekly, and monthly backups are scheduled to run at the same time, the backup with the longest period runs.
**Volume Group Back Up and Restore**
You can perform most of the same backup operations and tasks with volume groups that you can perform with individual block volumes.
Volume group backups enable you to manage the backup settings for several volumes in one place. This feature simplifies the process to create time-consistent backups of running enterprise applications that span multiple storage volumes across multiple compute instances.
You can restore a volume group backup to a volume group, or you can restore individual volumes in the volume group from volume backups.
**Clones**
You can create a clone from a volume using the Block Volume service. Cloning enables you to make a copy of an existing block volume without needing to go through the backup and restore process.
The clone operation occurs immediately, and you can attach and use the cloned volume as a regular volume when the state changes to Available. At this point, the volume data is being copied in the background, and can take up to thirty minutes depending on the size of the volume.
There's a single point-in-time reference for a source volume while it's being cloned. If the source volume is attached when a clone is created, you need to wait for the first clone operation to complete from the source volume before creating additional clones. If the source volume is detached, you can create up to 10 clones from the same source volume simultaneously.
You can only create a clone for a volume within the same tenant. You can create a clone of a volume in a different compartment from the source volume compartment if you have the required access permissions.
**Differences Between Volume Clones and Backups**
Consider the following criteria when you decide whether to create a backup or a clone of a volume.
Comparison | Volume Backup | Volume Clone  
---|---|---  
**Description** |  Creates a point-in-time backup of data on a volume. You can restore multiple new volumes from the backup later in the future. | Creates an immediately usable copy of a block volume without having to go through the backup and restore process.  
**Use Case** |  Retain a backup of the data in a volume, so that you can duplicate an environment later or preserve the data for future use. Meet compliance and regulatory requirements, because the data in a backup remains unchanged over time. Support business continuity requirements. Reduce the risk of outages or data mutation over time. | Creates an immediately usable copy of a block volume without having to go through the backup and restore process.  
**Storage Location** | Block Volume | Block Volume  
**Retention Policy** | Policy-based backups expire, manual backups don't expire. | No expiration  
**Volume Groups** | Supported. You can back up a volume group. | Supported. You can clone a volume group.  
Was this article helpful?
YesNo

