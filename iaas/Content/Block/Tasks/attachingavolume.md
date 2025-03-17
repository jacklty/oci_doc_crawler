Updated 2023-08-29
# Attaching a Block Volume to an Instance
Attach a block volume to a compute instance to expand the available storage on the instance.
If you specify [iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#iSCSI) as the volume attachment type, you must also connect and mount the volume from the instance for the volume to be usable. For more information, see [Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#attachtype) and [Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm#top "Connect to a block volume that's attached to a compute instance."). 
You can attach volumes to more than one instance at a time. For more information, see [Attaching a Volume to Multiple Instances](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm#Attaching_a_Volume_to_Multiple_Instances "The Oracle Cloud Infrastructure Block Volume service provides the capability to attach a block volume to multiple compute instances."). To prevent data corruption from uncontrolled read/write operations with multiple instance volume attachments you must install and configure a clustered file system before you can use the volume. For more information, see [Configuring Multiple Instance Volume Attachments with Read/Write Access](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingvolumetomultipleinstances.htm#configcluster).
**Note** When you change the performance for a volume, the volume's lifecycle state changes to **Provisioning** while the settings are being updated. During this process, you can't attach the volume to an instance. You must wait until the volume's lifecycle state transitions back to **Available** before you attach the volume to an instance.
## Attaching Ultra High Performance Volumes 🔗 
When you attach a volume configured for the **Ultra High Performance** level, the volume attachment must be enabled for multipath to optimize the volume's performance.
The Block Volume service attempts to configure the attachment as multipath-enabled during the attachment process. After you attach a volume, you can confirm if the volume attachment was successfully enabled for multipath. See [Checking if a Volume Attachment is Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/multipathcheck.htm#multipathcheck "When you attach a volume configured for the Ultra High Performance level, the volume attachment must be enabled for multipath to optimize the volume's performance. This topic describes how to verify if the volume attachment is multipath-enabled.").
Whether an attachment is enabled for multipath is determined based the attached instance's shape, along with whether all the applicable prerequisites are met and configured correctly. For more information about prerequisites and requirements for multipath-enabled attachments, see [Configuring Attachments to Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath "When you attach a volume configured for the Ultra High Performance level, to achieve the optimal performance, the volume attachment must be multipath-enabled.").
For more information about the **Ultra High Performance** level, see [Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#Block_Volume_Performance) and [Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance "The Ultra High Performance level is recommended for workloads with the highest I/O requirements, requiring the best possible performance, such as large databases.").
## Security Zones 🔗 
[Security Zones](https://docs.oracle.com/iaas/security-zone/home.htm) ensure that your cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a [policy for that security zone](https://docs.oracle.com/iaas/security-zone/using/security-zone-policies.htm), then the operation is denied.
The following security zone policies affect your ability to attach block volumes to compute instances.
  * All block volumes attached to a compute instance in a security zone must be in the same security zone.
  * Block volumes in a security zone can't be attached to a compute instance that is not in the same security zone.


  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm)


  *     1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
    2. Under **List scope** , select the compartment that contains the instance. 
    3. In the **Instances** list, click the name of the instance that you want to attach a volume to.
    4. In the **Resources** , click **Attached block volumes**. 
    5. Click **Attach block volume**.
    6. Specify the volume that you want to attach to the instance.
       * To use the volume name, select **Select volume** and then select the volume from the **Volume** list. If the volume is in a different compartment from the instance, click **Change compartment** and select the compartment that the volume is located in.
       * To specify the volume OCID, select **Enter volume OCID** and then enter the OCID into the **Volume OCID** field
    7. If the instance supports consistent device paths, and the volume that you're attaching is not a boot volume, select a path from the **Device path** list. This feature enables you to specify a device path for the volume attachment that remains consistent between instance reboots.
For more information about this feature and the instances that support it, see [Connecting to Volumes With Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/consistentdevicepaths.htm#Connecting_to_Volumes_With_Consistent_Device_Paths)
    8. Select the volume attachment type. See [Volume Attachment Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#attachtype).
    9. For iSCSI volume attachments, optionally require CHAP credentials by selecting the **Require CHAP credentials** check box.
For iSCSI attachments to Linux-based instances, you can also optionally configure the attachment to use the Block Volume Management plugin to run the iSCSI commands to automatically connect to the volume. To do this, select the **Use Oracle Cloud Agent to automatically connect to iSCSI-attached volumes** check box.
**Important** To automatically connect to the volume, the Block Volume Management plugin must be enabled on the instance. See [Enabling the Block Volume Management Plugin](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/enablingblockvolumemanagementplugin.htm#enablingblockvolumemanagementplugin "Enable the Block Volume Management plugin on a Compute instance.") for more information. When enabling the Block Volume Management plugin, ensure that the instance is running version 1.23.0 or newer of the Oracle Cloud Agent software.
    10. For paravirtualized attachments on virtual machine (VM) instances, optionally encrypt data that is transferred between the instance and the Block Volume service storage servers by selecting the **Use in-transit encryption** check box.
If you configured the volume to use an encryption key that you manage through the Vault service, this key is used for paravirtualized in-transit encryption. Otherwise, the Oracle-provided encryption key is used. When you attach the volume to a [bare metal instance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption__bm) that supports in-transit encryption, in-transit encryption is enabled by default and is not configurable. For more information about in-transit encryption, see [Block Volume Encryption](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#BlockVolumeEncryption).
    11. Select the access type. For more information, see [Volume Access Types](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#accesstype).
    12. Click **Attach**.
When the volume's state is **Attached** , if the attachment type is [Paravirtualized](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#Paravirtualized), the volume is connected automatically and you can use it. If the attachment type is [iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#iSCSI), you need to connect to the volume first. For more information, see [Connecting to a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume.htm#top "Connect to a block volume that's attached to a compute instance."). 
On Linux-based instances, if you want to automatically mount volumes when the instance starts, you need to set some specific options in the `/etc/fstab` file, or the instance might fail to start. This applies to both iSCSI and paravirtualized attachment types. For volumes that use consistent device paths, see [fstab Options for Block Volumes Using Consistent Device Paths](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptionsconsistentdevicepaths.htm#fstab_Options_for_Block_Volumes_Using_Consistent_Device_Paths). For all other volumes, see [Traditional fstab Options](https://docs.oracle.com/en-us/iaas/Content/Block/References/fstaboptions.htm#Traditional_fstab_Options). 
  * Use the [oci compute volume-attachment attach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/attach.html) command and required parameters to attach a block volume to an instance:
Command
CopyTry It
```
oci compute volume-attachment attach --instance-id instance_ocid --volume-id volume_ocid [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [AttachVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/AttachVolume) operation to attach a block volume to an instance.


Was this article helpful?
YesNo

