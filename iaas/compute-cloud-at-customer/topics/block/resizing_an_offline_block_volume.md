Updated 2024-12-16
# Offline Block Volume Resizing
On Oracle Compute Cloud@Customer, for offline resizing, you detach the volume from an instance before you expand the volume size. When the volume is resized and reattached, you need to extend the partition, but you do not need to rescan the disk.
## Considerations When Resizing an Offline Volume 🔗 
Whenever you detach and reattach volumes, there are complexities and risks for both UNIX based and Microsoft Windows instances. Be aware of the following cautions.
**Caution**
Before you resize a boot or block volume, create a full backup of the volume. See [Backing Up Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/backing-up-block-volumes.htm#backing-up-block-volumes "On Oracle Compute Cloud@Customer, the backup feature for the Block Volume service enables you make a point-in-time snapshot of the data on a block or boot volume. These backups can then be restored to new volumes any time.").
**Caution**
When you reattach a volume to an instance after resizing, if you are not using consistent device paths, or if the instance does not support consistent device paths, device order and path might change. If you are using a tool such as Logical Volume Manager (LVM), you might need to fix the device mappings.
**Prerequisite**
  * Block Volumes: Detach the block volume. See [Detaching a Block Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/detaching-a-block-volume.htm#detaching-a-block-volume "On Compute Cloud@Customer, when an instance no longer needs access to a volume, you can detach the volume from the instance without affecting the volume's data.").


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing_an_offline_block_volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing_an_offline_block_volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing_an_offline_block_volume.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volumes**.
    2. At the top of the page, select the compartment that contains the block volume you want to resize.
    3. For the volume you plan to resize, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    4. Change the size:
       * **Size (in GBs):** You can increase the size in 1 GB increments up to 32768 (32 TB). You can't decrease the size.
    5. Click **Save Changes**.
    6. Complete the resizing operation. 
See [Completing the Offline Resizing Operation for Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/completing_the_offline_resizing_operation_for_block_volumes.htm#completing_the_offline_resizing_operation_for_block_volumes "After resizing the offline block volume or boot volume, you need to perform the following administrative tasks.")
  * Use the [oci bv boot-volume update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html) command and required parameters to resize the block volume.
Command
CopyTry It
```
oci bv volume update --volume-id <volume_OCID> --size-in-gbs <size_in_GBS> [OPTIONS]
```

<size_in_GBs> is the size of the block volume. You can increase the size in 1 GB increments up to 32768. You can't decrease the size.
Next, complete the resizing operation. 
See [Completing the Offline Resizing Operation for Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/completing_the_offline_resizing_operation_for_block_volumes.htm#completing_the_offline_resizing_operation_for_block_volumes "After resizing the offline block volume or boot volume, you need to perform the following administrative tasks.")
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume) operation to resize a block volume.
Next, complete the resizing operation. 
See [Completing the Offline Resizing Operation for Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/completing_the_offline_resizing_operation_for_block_volumes.htm#completing_the_offline_resizing_operation_for_block_volumes "After resizing the offline block volume or boot volume, you need to perform the following administrative tasks.")
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

