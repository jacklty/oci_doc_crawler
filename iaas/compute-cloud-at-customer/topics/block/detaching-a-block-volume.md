Updated 2024-01-18
# Detaching a Block Volume
On Compute Cloud@Customer, when an instance no longer needs access to a volume, you can detach the volume from the instance without affecting the volume's data.
**Caution**
If you later reattach the detached volume, the volume might be associated with a different device name and the instance operating system might not recognize the volume.
**Prerequisites**
  * Perform administrative tasks to remove any dependencies that any instances have for the block volume.
For example, ensure that no applications are accessing the volume. Unmount the volume and remove it from the `/etc/fstab` file, and so on. 


  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/detaching-a-block-volume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/detaching-a-block-volume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/detaching-a-block-volume.htm)


  *     1. Perform administrative tasks to remove any dependencies that any instances have for the block volume.
For example, ensure that no applications are accessing the volume. Unmount the volume and remove it from the `/etc/fstab` file, and so on. 
    2. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Compute** , then click **Instances**.
    3. At the top of the page, select the compartment that contains the instance with the volume that you want to detach.
    4. Click the name of the instance that has the volume attached.
    5. Under Resources, select **Attached Block Volumes**.
    6. Next to the volume you want to detach, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Detach**. 
    7. Confirm when prompted.
  * Use the [oci compute volume-attachment detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/detach.html) command and required parameters to detach a block volume from an instance.
Command
CopyTry It
```
oci compute volume-attachment detach --volume-attachment-id <volume-attachment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DetachVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/DetachVolume) operation to detach a block volume from an instance.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

