Updated 2024-12-16
# Online Boot Volume Resizing
This topic describes how to resize a boot volume while it's online.
**Important**
Before you resize a boot or block volume, create a full backup of the volume. See [Backing Up Block Volumes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/backing-up-block-volumes.htm#backing-up-block-volumes "On Oracle Compute Cloud@Customer, the backup feature for the Block Volume service enables you make a point-in-time snapshot of the data on a block or boot volume. These backups can then be restored to new volumes any time.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing_an_online_boot_volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing_an_online_boot_volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/resizing_an_online_boot_volume.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Boot Volumes**.
    2. At the top of the page, select the compartment that contains the boot volume.
    3. For the volume you plan to resize, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    4. Change the size:
       * **Size (in GBs):** You can keep the size the same, or increase the size in 1 GB increments up to 16384 (16 TB). You can't decrease the size.
    5. Click **Save Changes**.
    6. Rescan the disk.
For details, consult the OS documentation for the OS type and version running in the instance.
    7. Extend the partition.
For details, consult the OS documentation for the OS type and version running in the instance.
  * Use the [oci bv boot-volume update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/boot-volume/update.html) command and required parameters to resize a boot volume.
Command
CopyTry It
```
oci bv boot-volume update --boot-volume-id <volume_OCID> --size-in-gbs <size_in_GBSs [OPTIONS]
```

For `_size _in_GBs_`specify the size of the boot volume. You can increase the size in 1 GB increments up to 16384 (16 TB). You can't decrease the size.
**Important**
The `path` option is required and its value must be `AUTOSELECT`. The value must be given in all uppercase letters. Providing any other value will cause the `export create` command to fail.
The export path is always automatically generated. See the `path` property in the command output for the export path.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
After resizing, perform disk administrative tasks. See [Completing the Online Resizing Operation](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/completing-the-online-resizing-operation.htm#completing-the-online-resizing-operation).
  * Use the [UpdateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume) operation to resize a boot volume.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

