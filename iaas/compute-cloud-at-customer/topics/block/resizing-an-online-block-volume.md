Updated 2024-12-16
# Online Block Volume Resizing
This topic describes how to resize a block volume while it is online.
**Caution**
Before you resize a boot or block volume, create a full backup of the volume. See [Backing Up Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/backing-up-block-volumes.htm#backing-up-block-volumes "On Oracle Compute Cloud@Customer, the backup feature for the Block Volume service enables you make a point-in-time snapshot of the data on a block or boot volume. These backups can then be restored to new volumes any time.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing-an-online-block-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing-an-online-block-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing-an-online-block-volume.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Block Volumes**.
    2. At the top of the page, select the compartment that contains the block volume that you want to resize.
    3. For the volume you plan to resize, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    4. Change the size:
       * **Size (in GBs):** You can increase the size in 1 GB increments up to 16384 (16 TB). You can't decrease the size.
    5. Click **Save Changes**.
    6. Perform disk administrative tasks. See [Completing the Online Resizing Operation](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/completing-the-online-resizing-operation.htm#completing-the-online-resizing-operation).
  * Use the [oci bv volume update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume/update.html) command and required parameters to resize the volume.
Command
CopyTry It
```
oci bv volume update --volume-id <volume_OCID> --size-in-gbs <size_in_GBS> [OPTIONS]
```

<size_in_GBS> is the size of the block volume. You can increment the size. You can't decrease the size. The value must be between 50 GB and 32 TB and specified in 1 GB increments.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
After resizing, perform disk administrative tasks. See [Completing the Online Resizing Operation](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/completing-the-online-resizing-operation.htm#completing-the-online-resizing-operation).
  * Use the [UpdateVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails) operation to resize a volume.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

