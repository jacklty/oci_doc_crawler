Updated 2023-12-08
# Updating a Volume Group
Update a volume group in the Block Volume service. For example, add or remove block volumes or boot volumes.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/update-volume-group.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
    2. Under **List scope** , select the compartment that contains the volume group.
    3. In the **Volume Groups** list, click the volume group you want to update.
    4. Click **Edit**.
The **Edit volume group** page opens.
    5. To add a block volume or boot volume:
      1. Click **Add or remove volumes**.
      2. Click **+ Additional Volume**.
      3. Select the compartment that contains the volume that you want.
      4. Select the volume that you want.
**Note** For both block volumes and boot volumes:
       * You can't add a volume with an existing backup policy assignment to a volume group with a backup policy assignment. Remove the backup policy assignment from the volume before you add it to the volume group.
       * If any of the volumes you add to the group are configured for replication, the destination region configured for them must match the destination region you configure for the volume group. See [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations).
    6. To remove a volume:
      1. Click **Add or remove volumes**.
      2. Click **X** for the volume that want to remove.
**Note** When you remove the last volume in a volume group, the volume group is terminated. 
    7. To review changes, click **Summary**.
    8. Click **Save Changes**.
  * Use the [oci bv volume-group update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/update.html) command and required parameters to update a volume group:
Command
CopyTry It
```
oci bv volume-group update --volume-group-id <volume-group_ID> --volume-ids <volume_ID_JSON>
```

You can update the volume group display name along with adding or removing volumes from the volume group. The volume group is updated to include only the volumes specified in the update operation. This means that you need to specify the volume IDs for all of the volumes in the volume group each time you update the volume group.
The following example changes the volume group's display name for a volume group with two volumes:
Copy
```
oci bv volume-group update --volume-group-id ocid1.volumegroup.oc1.phx.<unique_ID> --volume-ids '["ocid1.volume.oc1.phx.<unique_ID_1>","ocid1.volume.oc1.phx.<unique_ID_2>"]' --display-name "new display name"
```

If you specify volumes in the command that are not part of the volume group they are added to the group. Any volumes not specified in the command are removed from the volume group.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/UpdateVolumeGroup) operation to update a volume group.


Was this article helpful?
YesNo

