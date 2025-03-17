Updated 2024-09-16
# Attaching a Block Volume to a Roving Edge Infrastructure Device
Describes how to attach a block volume to a compute instance on your Roving Edge Infrastructure device.
See [Attaching a Volume](https://docs.oracle.com/iaas/Content/Block/Tasks/attachingavolume.htm) in the Oracle Cloud Infrastructure documentation for more information on this feature.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/attach_volume-attachment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/attach_volume-attachment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Block_Volume/Attachment/attach_volume-attachment.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance to which you want to attach a block volume under **Instances**.
    4. Click **Attached Block Volumes** in the lower left corner. The **Attached Block Volumes** page appears. All attached block volumes are listed in tabular form.
    5. Click **Attach Block Volume**. The **Attach Block Volume** dialog box appears. By default, the attached block volume type is **Paravirtualized**.
    6. Choose the volume selection option:
       * **Select Volume** : Select the volume from the **Block Volume** list.
       * **Enter Volume OCID** : Enter the OCID into the **Block Volume OCID** box.
    7. **Select a Device Path** : Choose one from the list of device paths. For example:
`/dev/oracleoci/oraclevdb`
    8. Select the access type:
       * **Read/Write**
       * **Read/Write - Shareable**
       * **Read-only**
    9. Click **Attach**.
The block volume appears in the **Attached Block Volume** page.
  * Use the [oci compute volume-attachment attach](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/compute/volume-attachment/attach.html) command and required parameters to attach a block volume to a compute instance on your Roving Edge Infrastructure devices:
Copy
```
oci compute volume-attachment attach --instance-id instance_ocid --type paravirtualized --volume-id volume_ocid --device device [OPTIONS]
```

where `device` might be `/dev/oracleoci/oraclevdb`.
Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [AttachVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeAttachment/AttachVolume) operation to attach a block volume to a compute instance on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

