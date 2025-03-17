Updated 2024-10-15
# Volume Group Replication
You can use the Block Volume service's replication feature for volume groups.
Volume group replicas themselves don't contain the full source data from the volumes in the group. Instead, the volume group replica contains references to individual replicas for each of the volumes in the group. This approach provides a seamless replication experience for volumes whether they remain in the volume group, are removed from the volume group, or if replication is turned off for the volume group itself.
When you activate a volume group replica, a new volume group is created. The activation process is the same as creating a clone of the volume group. 
This topic covers information about the replication feature specific to volume groups. For general information about the replication feature and how it works, see [Replicating a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication "The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of block volumes, boot volumes, and volume groups to other regions and availability domains.").
**Note** Replication doesn't cause any downtime or impact on source volumes.
## Limitations and Considerations 🔗 
The details specified in [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#replicalimits) apply to volume group replication, in addition to the following:
  * While it is possible to activate individual volume replicas separately from the volume group replica, to ensure consistency, you should activate the volume group replica instead. Activating the volume group replica ensures that all replicas are activated from the same coordinated synchronization point.
  * When you remove a volume from a volume group, the volume is not available to add to another group until removal process is complete.
  * When you add one or more volumes not configured for replication to a volume group that is configured for replication, the Recovery Point Object (RPO) for the volume group replication might degrade while the initial synchronization process runs for the volumes added to the group.
To prevent this impact to the volume group's RPO, you can enable replication for the volume and wait until the initial synchronization process is complete before you add the volume to the group. To determine when the initial synchronization process is complete, monitor the status of the replica for the volume. After it has changed from **Provisioning** to **Available** the process is complete, and you can add the volume to the volume group without degrading the volume group replication's RPO.
  * When you configure replication for a volume group, if the group contains volumes that are already configured for replication, the volume's destination region and availability domain must match the volume group's destination region and availability domain for replication. If they don't match, a **Conflicting volumes** message occurs while creating the volume group. Remove these volumes from the group to successfully create the volume group. 
  * When you turn on replication for a volume group, all volumes in the group are included in the volume group replica in the destination region and availability domain. Volumes are no longer replicated individually, regardless of whether they were configured for replication before they were included in a volume group with replication turned on. You can no longer update the replication settings for an individual volume, the settings must be configured at the volume group level.
  * When you turn off replication for a volume group, by default all volumes continue to replicate, but as separate volume replicas, they are no longer part of a volume group replica. You can turn off individual volume replication for all volumes at this point. Choose this option if you want to stop replication of all volumes. If you want to continue replication of some volumes, but not others, do not select this option. Instead, after replication for the volume group has been turned off, you can turn off replication for individual volumes.
See the following topics for how to turn off replication for individual volumes:
**From the Console:**
    * [To disable cross region replication for a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#disablereplication)
    * [To disable cross region replication for a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#disablereplicationboot)
**Using the CLI:**
    * [To disable cross region replication for a block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#To_disable_block_replication)
    * [To disable cross region replication for a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#To_disable_boot_replication)


## Using the Console 🔗 
Use the Console procedures in this section for volume group replicas.
[To enable replication for a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
Use the steps described in this procedure to enable replication on an existing volume group. You can also enable replication when you create a volume, see [Creating a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm#top "Create a volume group in the Block Volume service.").
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
  2. Click the volume group that you want to enable replication for.
  3. Click **Edit**.
  4. In the **Cross Region Replication** section, select **ON**.
  5. For cross region replication, select the region you want to replicate the volume group to, the availability domain to place the volume group replica in, and then specify the name for the volume group replica.
For cross availability domain replication, select the same region the volume group is located in, the availability domain to place the volume group replica in, and then specify the name for the volume group replica.
  6. Optionally, encrypt the volume group replica in the destination region by using your own Vault encryption key. Select **Encrypt using customer-managed keys** for **Cross region replication encryption** , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume group to. For more information, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys).
  7. Check **CONFIRM** to acknowledge the cost warning.
  8. Click **Save Changes**.


[To update the destination region or availability domain replication settings for a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
To change the destination region or availability domain for cross region replication you need to first turn replication off for the volume group. Then specify the new region and availability domain selections when you turn replication on again.
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
  2. Click the volume group that you want to change the replication settings for.
  3. Click **Edit**.
  4. In the **Cross Region Replication** section, select **OFF**.
  5. Check **CONFIRM** to acknowledge the that volume group replica will be deleted.
  6. Click **Save Changes**.
  7. Click **Edit**.
  8. In the **Cross Region Replication** section, select **ON**.
  9. For cross region replication, select the region you want to replicate the volume group to, the availability domain to place the volume group replica in, and then specify the name for the volume group replica.
For cross availability domain replication, select the same region the volume group is located in, the availability domain to place the volume group replica in, and then specify the name for the volume group replica.
  10. Optionally, encrypt the volume group replica in the destination region by using your own Vault encryption key. Select **Encrypt using customer-managed keys** for **Cross region replication encryption** , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume group to. For more information, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys).
  11. Check **CONFIRM** to acknowledge the cost warning.
  12. Click **Save Changes**.


[To disable replication for a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
  2. Click the volume group that you want to disable replication for.
  3. Click **Edit**.
  4. In the **Cross Region Replication** section, select **OFF**.
  5. Check **CONFIRM** to acknowledge the that volume group replica will be deleted.
  6. Click **Save Changes**.


[To activate a volume group replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
**Note** For volumes in a volume group configured for replication, activate the volume group replica instead of individual volume replicas if you want to ensure that all volume replicas are activated from the same coordinated synchronization point. See [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations).
To create a new volume group from a volume group replica, you need to activate the replica. The activation process creates a new volume group by cloning the replica. 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Replicas**. Ensure that you're in correct destination region and availability domain that contains the volume group replica you want to activate.
  2. Click the replica that you want to activate.
  3. Click **Activate** to open the **Activate Volume Group Replica** form.
  4. On the **Activate Volume Group Replica** , specify the compartment and the name for the new volume group, and optionally select the cluster placement group.
**Note** The **Cluster Placement Group** control only appears in the Console if Cluster Placement Groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources, see [Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups "Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases."). 
  5. Click **Create**. The new volume group appears in the volume groups list, in the provisioning state.


[To monitor a volume group replica's status](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
The volume group replica's details page provides information about the replica's status.
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**. Ensure that you are in the destination region containing the volume group replica that you want to view.
  2. Click the replica that you're interested in.
  3. The replica details page displays the following relevant fields:
     * **Last Sync** : The time of the last data synchronization from the source volume group to the replica.
     * **Total Data Transfered** : The amount of data, in GBs, that has been transferred during the replication process for the volume group. This includes all data from the point that replication was enabled to now.


[To failback a volume group replica to the source region](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
To failback a volume group replica to the source region, you need activate the volume group replica in the destination region, with replication enabled, and select the original source region as the target region for replication. 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Replicas**. Ensure that you are in correct destination region that contains the volume replica you want to activate.
  2. Click the replica that you want to activate.
  3. Click **Activate** to open the **Activate volume group replica** form.
  4. On the **Activate Volume Group Replica** , specify the compartment and the name for the new volume group, and then click **Create**. The new volume group will appear in the volume groups list, in the provisioning state. 
Ensure that **Volume Replication** is enabled, and select the original source region.
  5. Once the volume group has been created, turn on replication for the volume group and specify the original source region as the destination region. See [To enable replication for a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegroupreplication_topic_To_enable_volume_group_replication). Once the initial synchronization finishes, the failback process is complete, and you can activate the volume group in the original source region.


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
Use the following operations for cross region replication of volumes groups.
[To enable cross region replication when creating a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group create --compartment-id <compartment_ID> --volume-group-replicas '[{"displayName":"<display_name>","availabilityDomain":"<availability-domain_ID>","xrrKmsKeyId" : "<kms_key_ID>"}]' 
```

For example:
Command
CopyTry It
```
oci bv volume-group create --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --volume-group-replicas '[{"displayName":"Sample_Replica","availabilityDomain":"pjBI:US-ASHBURN-AD-1","xrrKmsKeyId" : "ocid1.key.oc1.iad-ad-1.<unique_ID>"}]'
```

[To enable cross region replication when updating a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group update --volume-group-id <volume-group_ID> --volume-group-replicas '[{"displayName":"<display_name>","availabilityDomain":"<availability-domain_ID>","xrrKmsKeyId" : "<kms_key_ID>"}]' 
```

For example:
Command
CopyTry It
```
oci bv volume-group update --volume-group-id ocid1.volumegroup.oc1.phx.<unique_ID> --volume-group-replicas '[{"displayName":"Sample_Replica","availabilityDomain":"pjBI:US-ASHBURN-AD-1","xrrKmsKeyId" : "ocid1.key.oc1.iad-ad-1.<unique_ID>"}]'
```

[To disable cross region replication for a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group update --volume-group-id <volume-group_ID> --volume-group-replicas '[]' 
```

For example:
Command
CopyTry It
```
oci bv volume-group update --volume-group-id ocid1.volumegroup.oc1.phx.<unique_ID> --volume-group-replicas '[]'
```

[To activate a volume group replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
**Note** For volumes in a volume group configured for replication, activate the volume group replica instead of individual volume replicas if you want to ensure that all volume replicas are activated from the same coordinated synchronization point. See [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations).
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group create --source-details '{"type": "volumeGroupReplicaId", "volumeGroupReplicaId": "<VOLUME_GROUP_REPLICA_ID>"}' --compartment-id <compartment_ID> --availability-domain <availability_domain> 
```

For example:
Command
CopyTry It
```
oci bv volume-group create --source-details '{"type": "volumeGroupReplicaId", "volumeGroupReplicaId": "ocid1.volumegroupreplica.oc1.phx.<unique_ID>"}' --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --availability-domain ABbv:PHX-AD-1 
```

[To list volume group replicas](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group-replica list --availability-domain <availability_domain> --compartment-id <compartment_ID>
```

For example:
Command
CopyTry It
```
oci bv volume-group-replica list --availability-domain ABbv:PHX-AD-1 --compartment-id ocid1.compartment.oc1.phx.<unique_ID> 
```

[To retrieve a volume group replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group-replica get --volume-group-replica-id <volume-group-replica-ID>
```

For example:
Command
CopyTry It
```
oci bv volume-group-replica get --volume-group-replica-id ocid1.volumegroupreplica.oc1.phx.<unique_ID>
```

## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following operations to list and retrieve volume group replicas:
  * [ListVolumeGroupReplicas](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupReplica/ListVolumeGroupReplicas)
  * [GetVolumeGroupReplica](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupReplica/GetVolumeGroupReplica)


You can enable replication for volume group when you create or update the group. To disable replication, use the `Update` operation. To activate a volume group replica, use the `Create` operation and pass the source volume group's replica ID.
  * [CreateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup)
  * [UpdateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/UpdateVolumeGroup)


Was this article helpful?
YesNo

