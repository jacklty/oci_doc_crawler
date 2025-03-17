Updated 2024-01-18
# Removing Volumes from a Group
On Compute Cloud@Customer, you can remove block and boot volumes from an existing volume group using the Compute Cloud@Customer Console, CLI, and API.
When you remove the last volume in a volume group, the volume group is deleted.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/removing-volumes-from-a-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/removing-volumes-from-a-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/removing-volumes-from-a-group.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Block Storage** , then click **Volume Groups**.
    2. At the top of the page, select the compartment that contains the volume group that has the volume you want to remove.
    3. In the **Volume Groups** list, click the volume group that contains the volume you plan to remove.
    4. Under **Resources** , click **Volumes**. 
    5. For the volume that you want to remove, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Remove**.
    6. Confirm the removal.
  * Use the [oci bv volume-group update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/update.html) command and required parameters to update a volume group.
To remove a volume from a volume group, use the `oci bv volume-group           update` command, and remove the volume from the list of volumes in the argument for the `--volume-ids` option as described in [Adding Volumes to a Group](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/adding-volumes-to-a-group.htm#adding-volumes-to-a-group "On Compute Cloud@Customer, you can add block and boot volumes to an existing volume group using the Compute Cloud@Customer Console, CLI, and API.").
Command
CopyTry It
```
oci bv volume-group update --volume-group-id <volume_group_OCID> --volume-ids <volume_OCIDs_JSON> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/UpdateVolumeGroup) operation to update a volume group:
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

