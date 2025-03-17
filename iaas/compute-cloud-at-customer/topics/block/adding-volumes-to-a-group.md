Updated 2024-01-18
# Adding Volumes to a Group
On Compute Cloud@Customer, you can add block and boot volumes to an existing volume group using the Compute Cloud@Customer Console, CLI, and API.
**Note**
You can't add a volume with an existing backup policy assignment to a volume group with a backup policy assignment. You must first remove the backup policy assignment from the volume before you can add it to the volume group.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/adding-volumes-to-a-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/adding-volumes-to-a-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/adding-volumes-to-a-group.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Volume Groups**.
    2. At the top of the page, select the compartment that contains the volume group.
    3. In the **Volume Groups** list, click the volume group you want to add the volume to.
    4. Under **Resources** , click **Volumes**.
    5. Click **Add Volumes**.
    6. Select a volume to add to the group from the volume drop-down list. You might need to select a different compartment above the volume drop-down list. Click **+ Add Volume** to add another volume.
    7. Click **Update Volume Group**.
  * Use the [oci bv volume-group update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/update.html) command and required parameters to update a volume group.
Command
CopyTry It
```
oci bv volume-group update --volume-group-id <volume_group_OCID> --volume-ids <volume_OCIDs_JSON> [OPTIONS]
```

For details about the JSON format, run this command:
```
oci bv volume-group update --generate-param-json-input volume-ids
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/UpdateVolumeGroup) operation to update a volume group.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

