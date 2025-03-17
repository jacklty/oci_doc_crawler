Updated 2024-06-04
# Attaching a Volume to Multiple Instances
The Oracle Cloud Infrastructure Block Volume service provides the capability to attach a block volume to multiple compute instances.
With this feature, you can share block volumes across instances in read/write or read-only mode. Attaching block volumes as read/write and shareable enables you to deploy and manage your cluster-aware solutions. 
This topic describes how to attach block volumes as shareable, along with the limits and considerations for this feature.
See [Volume Access Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#accesstype) for more information about the available access type options. For attaching volumes to single instances, see [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance."). 
## Limits and Considerations 🔗 
  * The Block Volume service does not provide coordination for concurrent write operations to block volumes attached to multiple instances, so if you configure the block volume as read/write and shareable you must deploy a cluster aware system or solution on top of the shared storage, see [Configuring Multiple Instance Volume Attachments with Read/Write Access](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm#configcluster).
  * Once you attach a block volume to an instance as read-only, it can only be attached to other instances as read-only. If you want to attach the block volume to an instance as read/write, you need to detach the block volume from all instances and then you can reattach the block volume to instances as read/write.
  * If the block volume is already attached to an instance as read/write non-shareable you can't attach it to another instance until you detach it from the first instance. You can then reattach it to both the first and second instances as read/write shareable.
  * You can't delete a block volume until it has been detached from all instances it was attached to. When viewing the instances attached to the block volume from the **Resources** section of the **Volume Details** page, you should note that only instances in the selected compartment will be displayed. You may need to change the compartment to list additional instances that are attached to the volume.
  * You can attach up to 32 instances to a shared volume if the volume is not configured for the **Ultra High Performance** level
  * Volumes configured for the **Ultra High Performance** level require multipath-enabled attachments. You can attach up to 25 instances with multipath-enabled attachments to a shared volume configured for **Ultra High Performance**. If you try to attach additional multipath-enabled attachments beyond 25, the attachment process will fail. 
  * Block volumes attached as read-only are configured as shareable by default.
  * Performance characteristics described in [Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#Block_Volume_Performance) are per volume, so when a block volume is attached to multiple instances the performance is shared across all the attached instances.
  * Volumes configured for the **Ultra High Performance** level can also be attached to multiple instances, however the total IOPS and throughput of all attachments combined, including those configured for **Ultra High Performance** and non-**Ultra High Performance** are capped at the limits for a volume. For more information, see [Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance "The Ultra High Performance level is recommended for workloads with the highest I/O requirements, requiring the best possible performance, such as large databases.") and [Configuring Attachments to Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath "When you attach a volume configured for the Ultra High Performance level, to achieve the optimal performance, the volume attachment must be multipath-enabled.").


## Configuring Multiple Instance Volume Attachments with Read/Write Access 🔗 
The Block Volume service does not provide coordination for concurrent write operations to volumes attached to multiple instances. To prevent data corruption from uncontrolled read/write operations you must install and configure a cluster aware system or solution such as Oracle Cluster File System version 2 (OCFS2) on top of the shared storage before you can use the volume.
You can see an sample walkthrough of scenario using OCFS2 described in [Using the Multiple-Instance Attach Block Volume Feature to Create a Shared File System on Oracle Cloud Infrastructure](https://blogs.oracle.com/cloud-infrastructure/using-the-multi-attach-block-volume-feature-to-create-a-shared-file-system-on-oracle-cloud-infrastructure). The summary of the required steps for this scenario are:
  1. Attach the block volume to an instance as **Read/Write-Shareable** using the Console, CLI, or API. 
  2. Set up your OCFS2/O2CB cluster nodes.
  3. Create your OCFS2 file system and mount point.


## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let users launch compute instances](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#launch-instances) includes the ability to attach/detach existing block volumes. The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes and backups, but not launch instances. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Using the Console 🔗 
[To attach a volume to multiple instances from the Instance details page](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm)
  1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
  2. In the **Instances** list, click the instance that you want to attach a volume to.
  3. In the **Resources** section, click **Attached Block Volumes**. 
  4. Click **Attach Block Volume**.
  5. Select the volume attachment type, **iSCSI** or **Paravirtualized**.
For more information, see [Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#attachtype).
  6. Select the volume access type. Select **Read/Write-Shareable** if you want to enable read/write attachments to multiple instances or **Read-only-Shareable** for read-only attachments to multiple instances.
For more information, see [Volume Access Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#accesstype).
  7. In the **Block Volume Compartment** drop-down list, select the compartment. 
  8. Specify the volume you want to attach to. To use the volume name, choose **SELECT VOLUME** and then select the volume from the **Block Volume** drop-down list. To specify the volume OCID, choose **ENTER VOLUME OCID** and then enter the OCID into the **Block Volume OCID** field.
  9. If the instance supports consistent device paths select a path from the **Device Path** drop-down list when attaching. This is required and enables you to specify a device path for the volume attachment that remains consistent between instance reboots.
For more information about this feature and the instances that support it, see [Connecting to Volumes With Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#Connecting_to_Volumes_With_Consistent_Device_Paths)
**Tip** You must select a device path when you attach a volume from the Console, it is not optional. Specifying a device path is optional when you attach a volume using the CLI, REST APIs, or SDK.
  10. For paravirtualized volume attachments on virtual machine (VM) instances you can optionally encrypt data that is transferred between the instance and the Block Volume service storage servers. To do this, select the **Use in-transit encryption** check box. If you configured the volume to use an encryption key that you manage using the Vault service, this key is used for in-transit encryption. Otherwise, the Oracle-provided encryption key is used. 
For iSCSI attachments on [bare metal instances](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption__bm) that support in-transit encryption, in-transit encryption is enabled by default and is not configurable.
See [Block Volume Encryption](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption) for more information about in-transit encryption.
  11. Click **Attach**.
When the volume's icon no longer lists it as **Attaching** , if the attachment type is [Paravirtualized](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#Paravirtualized), you can use the volume. If the attachment type is [iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#iSCSI), you need to connect to the volume first. For more information, see [Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm#top "Connect to a block volume that's attached to a compute instance."). 
On Linux-based instances, if you want to automatically mount volumes on instance boot, you need to set some specific options in the `/etc/fstab` file, or the instance may fail to launch. This applies to both iSCSI and paravirtualized attachment types. For volumes using consistent device paths, see [fstab Options for Block Volumes Using Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptionsconsistentdevicepaths.htm#fstab_Options_for_Block_Volumes_Using_Consistent_Device_Paths). For all other volumes, see [Traditional fstab Options](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptions.htm#Traditional_fstab_Options). 


[To attach a volume to multiple instances from the Block Volume details page](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. In the **Block Volumes** list, click the block volume that you want to attach to an instance.
  3. In the **Resources** section, click **Attached Instances**. 
  4. Click **Attach to Instance**.
  5. Select the volume attachment type, **iSCSI** or **Paravirtualized**.
For more information, see [Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#attachtype).
  6. Select the volume access type. Select **Read/Write-Shareable** if you want to enable read/write attachments to multiple instances or **Read-only-Shareable** for read-only attachments to multiple instances.
For more information, see [Volume Access Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#accesstype).
  7. In the **Choose Instance** drop-down list, select the instance. Click **Change Compartment** if the instance is in a different compartment than the default one listed. If you want to specify the instance using the OCID, select the **ENTER INSTANCE OCID** option and then copy the OCID in the textbox.
  8. If the instance supports consistent device paths select a path from the **Device Path** drop-down list when attaching. This is required and enables you to specify a device path for the volume attachment that remains consistent between instance reboots.
For more information about this feature and the instances that support it, see [Connecting to Volumes With Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#Connecting_to_Volumes_With_Consistent_Device_Paths)
**Tip** You must select a device path when you attach a volume from the Console, it is not optional. Specifying a device path is optional when you attach a volume using the CLI, REST APIs, or SDK.
  9. For paravirtualized volume attachments on virtual machine (VM) instances you can optionally encrypt data that is transferred between the instance and the Block Volume service storage servers. To do this, select the **Use in-transit encryption** check box. If you configured the volume to use an encryption key that you manage using the Vault service, this key is used for in-transit encryption. Otherwise, the Oracle-provided encryption key is used.
For iSCSI attachments on [bare metal instances](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption__bm) that support in-transit encryption, in-transit encryption is enabled by default and is not configurable.
See [Block Volume Encryption](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption) for more information about in-transit encryption.
  10. Click **Attach**.
When the volume's icon no longer lists it as **Attaching** , if the attachment type is [Paravirtualized](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#Paravirtualized), you can use the volume. If the attachment type is [iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#iSCSI), you need to connect to the volume first. For more information, see [Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm#top "Connect to a block volume that's attached to a compute instance."). 
On Linux-based instances, if you want to automatically mount volumes on instance boot, you need to set some specific options in the `/etc/fstab` file, or the instance may fail to launch. This applies to both iSCSI and paravirtualized attachment types. For volumes using consistent device paths, see [fstab Options for Block Volumes Using Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptionsconsistentdevicepaths.htm#fstab_Options_for_Block_Volumes_Using_Consistent_Device_Paths). For all other volumes, see [Traditional fstab Options](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptions.htm#Traditional_fstab_Options). 


[To view the instances attached to a volume from the Volume details page](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. In the **Block Volumes** list, click the block volume that you want to view the attached instances for.
  3. In the **Resources** section, click **Attached Instances**. 


All the attached instances in the selected compartment will be displayed in the list. To view attached instances in other compartments, change the compartment in the **COMPARTMENT** drop down list.
[To view the volumes attached to an instance from the Instance details page](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm)
  1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
  2. In the **Instances** list, click the instance that you want to view the attached volumes for.
  3. In the **Resources** section, click **Attached Block Volumes**. 


All the block volumes attached to the instance will be displayed in the list, regardless of the compartment the block volumes are in. 
## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
[To attach a volume to an instance as shareable, read/write](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci compute volume-attachment attach --instance-id <instance_ID> --type <attachment_type> --volume-id <volume_ID> --read-only true/false --is-shareable true
```

For example:
```
oci compute volume-attachment attach --instance-id ocid1.instance.oc1..<unique_ID> --type iscsi --volume-id ocid1.volume.oc1..<unique_ID> --read-only false --is-shareable true
```

[To list all the instances attached to a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci compute volume-attachment list --compartment-id <compartment_ID> --volume-id <volume_ID>
```

For example:
```
oci compute volume-attachment attach --compartment-id ocid1.compartment.oc1..<unique_ID> --volume-id ocid1.volume.oc1..<unique_ID>
```

**Note** This operation will only return the attached instances that are in the specified compartment. You need to run this operation for every compartment that may contain instances that are attached to the specified volume.
## Using the API 🔗 
Use the following APIs to attach volumes and work with volume attachments to instances:
  * [AttachVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/AttachVolume)
Set the `isShareable` attribute of [AttachVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/AttachVolumeDetails) to `true`.
  * [GetVolumeAttachment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/GetVolumeAttachment)
  * [ListVolumeAttachments](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/ListVolumeAttachments)
The `ListVolumeAttachments` operation will only return the attached instances that are in compartment you specify. You need to run this operation for every compartment that may contain instances that are attached to the specified volume.


For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
## Additional Resources 🔗 
See the following links for example deployments of shared file systems on Oracle Cloud Infrastructure.
  * GitHub project for automated terraform deployment of [BeeGFS](https://www.beegfs.io/content/): [oci-beegfs](https://github.com/oracle-quickstart/oci-beegfs)
  * GitHub project for automated terraform deployment of [Lustre](http://lustre.org/): [oci-lustre](https://github.com/oracle-quickstart/oci-lustre)
  * GitHub project for automated terraform deployments of IBM Spectrum Scale (GPFS) distributed parallel file system on Oracle Cloud Infrastructure: [oci-ibm-spectrum-scale](https://github.com/oracle-quickstart/oci-ibm-spectrum-scale)


Was this article helpful?
YesNo

