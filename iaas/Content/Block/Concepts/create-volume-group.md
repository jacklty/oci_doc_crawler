Updated 2024-10-15
# Creating a Volume Group
Create a volume group in the Block Volume service.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm)


  *     1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
    2. Click **Create volume group**.
    3. On the **Basic information** page, enter a user-friendly name or description. Avoid entering confidential information.
    4. Select the compartment that you want to store the volume group in.
    5. Select the availability domain for the volume group.
    6. (Optional) Click **Show Tagging Options** to add tags to the volume group.
       * **Tag namespace** : To add a defined tag, select an existing namespace. To add a free-from tag, leave the value blank.
       * **Tag key** : To add a defined tag, select an existing tag key. To add a free-form tag, type the key name that you want.
       * **Tag value** : Type the tag value that you want.
       * **Add tag** : Click to add another tag.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
    7. Click **Next**.
    8. On the **Add volumes** page, add each volume that you want. After adding volumes, click **Next**.
      1. Click **+ Additional Volume**.
      2. Select the compartment that contains the volume that you want.
      3. Select the volume that you want.
**Note** For both block volumes and boot volumes:
       * You can't add a volume with an existing backup policy assignment to a volume group with a backup policy assignment. Remove the backup policy assignment from the volume before you add it to the volume group.
       * If any of the volumes you add to the group are configured for replication, the destination region configured for them must match the destination region you configure for the volume group. See [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations).
    9. (Optional) On the **Cross region replication** page, enable asynchronous [cross region replication](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegroupreplication "You can use the Block Volume service's replication feature for volume groups.") for the volume group, and then click **Next**.
If you enable cross-region replication, you can encrypt the volume group replica in the destination region with your own Vault encryption key by selecting **Encrypt using customer-managed keys** for **Cross region replication encryption**. If you select this option, you must specify the OCID for a valid encryption key in the destination region, for more information, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys).
If any of the volumes you add to the group are configured for replication, the destination region configured for them must match the destination region you configure for the volume group, see [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations).
    10. (Optional) On the **Backup policies** page, select a backup policy to configure schedule backups for the volume group, and then click **Next**.
If you select a backup policy enabled for cross region backup copies you can encrypt the volume group backup copy in the destination region with your own Vault encryption key by selecting **Encrypt using customer-managed keys** for **Cross region backup copy encryption**. If you select this option, you must specify the OCID for a valid encryption key in the destination region, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys) for more information.
For more information, see [Policy-Based Volume Group Backups](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm#scheduledbackups).
    11. On the **Summary** page, review the information to confirm that it's correct.
    12. Click **Create**.
  * Use the [oci bv volume-group create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/bv/volume-group/create.html) command and required parameters to create a volume group from existing volumes:
Command
CopyTry It
```
oci bv volume-group create --compartment-id <compartment_ID> --availability-domain <external_AD> --source-details <Source_details_JSON>
```

Volume lifecycle status must be `AVAILABLE` to add it to a volume group.
For example:
Command
CopyTry It
```
oci bv volume-group create --compartment-id ocid1.compartment.oc1..<unique_ID> --availability-domain ABbv:PHX-AD-1 --source-details '{"type": "volumeIds", "volumeIds":["ocid1.volume.oc1.phx.<unique_ID_1>", "ocid1.volume.oc1.phx.<unique_ID_2>"]}'
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup) operation to create a volume group.


Was this article helpful?
YesNo

