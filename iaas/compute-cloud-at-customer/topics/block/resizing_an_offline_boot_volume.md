Updated 2024-10-07
# Offline Boot Volume Resizing
On Oracle Compute Cloud@Customer, for offline boot volume resizing, you must stop the instance and detach the volume from an instance before you expand the volume size. When the volume is resized and reattached, you need to extend the partition, but you don't need to rescan the disk.
## Considerations When Resizing an Offline Volume 🔗 
Whenever you detach and reattach volumes, there are complexities and risks for both UNIX based and Microsoft Windows instances. Be aware of the following cautions.
**Caution**
Before you resize a boot or block volume, create a full backup of the volume. See [Backing Up Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/backing-up-block-volumes.htm#backing-up-block-volumes "On Oracle Compute Cloud@Customer, the backup feature for the Block Volume service enables you make a point-in-time snapshot of the data on a block or boot volume. These backups can then be restored to new volumes any time.").
**Caution**
When you reattach a volume to an instance after resizing, if you aren't using consistent device paths, or if the instance doesn't support consistent device paths, device order and path might change. If you're using a tool such as Logical Volume Manager (LVM), you might need to fix the device mappings.
**Prerequisites**
  * Stop the instance that has the boot volume. See [Stopping, Starting, and Resetting an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/stopping-starting-and-resetting-an-instance.htm#stopping-starting-and-resetting-an-instance "On Compute Cloud@Customer, you can control the state of an instance using the Compute Cloud@Customer Console, CLI, and API.")
  * Detach the boot volume. See [Detaching a Boot Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/detaching-a-boot-volume.htm#detaching-a-boot-volume "On Oracle Cloud Infrastructure, if you think a boot volume issue is causing a compute instance problem, you can stop the instance and detach the boot volume using the steps described in this topic. Then you can attach the boot volume to another instance as a data volume to troubleshoot it.").


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing_an_offline_boot_volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing_an_offline_boot_volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing_an_offline_boot_volume.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Boot Volumes**.
    2. At the top of the page, select the compartment that contains the boot volume you want to resize.
    3. For the volume you plan to resize, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    4. Change the size:
       * **Size (in GBs):** You can keep the size the same, or increment the size. You can't decrease the size. The value must be between 50 GB and 32 TB and specified in 1 GB increments.
    5. Click **Save Changes**.
    6. Complete the resizing operation. 
See [Completing the Offline Resizing Operation for Boot Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/completing_the_onffline_resizing_oeration_for_boot_volumes.htm#completing_the_onffline_resizing_oeration_for_boot_volumes "After resizing the online block volume or boot volume, you need to perform the following administrative tasks.")
  * Use the [oci bv boot-volume update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html) command and required parameters to resize a boot volume.
Command
CopyTry It
```
oci bv boot-volume update --boot-volume-id <volume_OCID> --size-in-gbs <size_in_GBs> [OPTIONS]
```

The `size_in_GBs` value is the size of the boot volume. You can increment the size. You can't decrease the size. The value must be between 50 GB and 32 TB and specified in 1 GB increments.
Next, complete the resizing operation. 
See [Completing the Offline Resizing Operation for Boot Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/completing_the_onffline_resizing_oeration_for_boot_volumes.htm#completing_the_onffline_resizing_oeration_for_boot_volumes "After resizing the online block volume or boot volume, you need to perform the following administrative tasks."). 
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume) operation to resize a boot volume.
Next, complete the resizing operation. 
See [Completing the Offline Resizing Operation for Boot Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/completing_the_onffline_resizing_oeration_for_boot_volumes.htm#completing_the_onffline_resizing_oeration_for_boot_volumes "After resizing the online block volume or boot volume, you need to perform the following administrative tasks.")
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

