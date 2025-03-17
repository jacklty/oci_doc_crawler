Updated 2023-08-21
# Detaching a Volume
Detach a block volume from an instance.
When an instance no longer needs access to a volume, you can detach the volume from the instance without affecting the volume's data. 
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm)


  * **Caution** For volumes attached using [iSCSI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm#iSCSI), we recommend that you unmount and disconnect the volume from the instance using `iscsiadm `before you detach the volume. Failure to do so may lead to loss of data. See [Disconnecting From a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/disconnectingfromavolume.htm#Disconnecting_From_a_Volume) for more information. 
    1. Open the navigation menu and click **Compute**. Under **Compute** , click **Instances**.
    2. In the **Instance** list locate the instance. Click its name to display the instance details.
    3. In the **Resources** section on the **Instance Details** page, click **Attached Block Volumes**
    4. Click the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) next to the volume you want to detach, and then click **Detach**. Confirm when prompted. 
  * Use the [oci compute volume-attachment detach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/detach.html) command and required parameters to detach a block volume from an instance:
Command
CopyTry It
```
oci compute volume-attachment detach --volume-attachment-id volume_attachment_ocid [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [DetachVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/DetachVolume) operation to detach a block volume from an instance.


Was this article helpful?
YesNo

