Updated 2024-10-15
# Replicating a Volume
The Block Volume service provides you with the capability to perform ongoing automatic asynchronous replication of block volumes, boot volumes, and volume groups to other regions and availability domains.
Block Volume supports two types of replication:
  * [Cross region](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication_topic-Cross_Region_Replication), for replication between regions.
  * [Cross availability domain](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication_topic-Cross_AD_Replication), for replication between availability domains within the same region.


This feature supports the following scenarios without requiring volume backups and volume group backups:
  * Disaster recovery
  * Migration
  * Business expansion


The replication feature is complementary to the backup feature, not a replacement. Backups give you a point-in-time snapshot of volumes that enables you to return to a previous version of a volume or volume group. Replicas give you the current version of the data.
When you enable replication for a volume or volume group, the process includes an initial sync of the data from the source to the replica. Depending on volume size and amount of data written to volumes, this sync can take hours. After the initial synchronization process is complete, the replication process is continuous, with the typical Recovery Point Object (RPO) target rate being less than thirty minutes for replication across regions, however the RPO can vary. See [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#replicalimits).
**Note** Replication doesn't cause any downtime or impact on source volumes.
## Limitations and Considerations 🔗 
The following applies to both replication to another region and replication to another availability domain within the same region.
  * Replication isn't supported for volumes encrypted using customer-managed Vault encryption keys.
  * You can't resize a volume with replication enabled. When resizing a volume, you need to disable replication, which deletes the volume replica. After the volume is resized, you can reenable replication for the volume, which starts the replication process from scratch.
  * While the typical RPO target rate is significantly less than thirty minutes for replication, the RPO can vary depending on the change rate of data on the source volume. For example, the RPO can be greater than an hour for volumes with a large amount of write I/O operations to the volume.


### Cost Considerations for Replication 🔗 
After you enable replication for a volume or volume group, it will be replicated in the specified availability domain or the specified region and availability domain. Your bill will include storage costs for the volume or volume group replica in the destination. The replica in the destination is billed using the Block Storage Lower Cost option price, regardless of volume type in the source region. 
See [Oracle Storage Cloud Pricing](https://www.oracle.com/cloud/storage/pricing.html) for information about storage pricing.
For cross region replication, your bill will also include applicable network costs, see [Network Costs for Cross Region Replication](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#volumereplication_topic-Cross_Region_Network_Costs).
## Cross Region Replication 🔗 
Block Volume replication supports replicating a volume or volume group to another region. For this type of replication, when you enable replication for a volume or volume group, you select a different region than the current source region as the destination region to replicate to. If the destination region supports multiple availaiblity domains, you can also select the availability domain you want to replicate to.
The source region for the volume or volume group determines the target regions available to select as a destination region for replication. Each region has one or more regions available as possible destination regions. The destination regions are selected based on geographical locations. Your tenancy must be subscribed to the destination region for replication. See [Source and Destination Region Mappings](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#regionmapping) for more information.
### Network Costs for Cross Region Replication 🔗 
Your bill will also include any applicable network costs for the replication process between regions. Network costs for replication between availability domains within the same region are not billed. As part of the replication process, all data being updated on the source volume or source volume group is transferred to the replica, so volumes with continual updates incur higher network costs.
You can see the amount of data transferred for an individual volume during replication in the Console.
To see the amount of data transferred from the replication process for a volume
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**.
  2. Click the replica that you want to see the amount of data transferred for. On the **Replica Details** page, the **Total Data Transferred** field displays the amount of data, in GBs, that has been transferred during the replication process for the volume. This number includes all data from the point that volume replication was enabled to now.


See [Oracle Networking Cloud Pricing](https://www.oracle.com/cloud/networking/networking-pricing.html) for information about network pricing.
### Source and Destination Region Mappings 🔗 
If your tenancy is not subscribed to any of the destination regions for the source region, and the source region only supports one availability domain, no regions are displayed in the region list and an error message is shown. For source regions containg multiple availability domains, the source region is displayed in the region list, and cross availability domain replication is the only replication available. To use cross region replication, you must subscribe to one of the destination regions for the source region. To subscribe to a region, see [Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm). 
**Note** If you do not see a region that you are subscribed to in the destination region list, [open a support ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport_topic-Open_a_support_service_request.htm) to request that the region be added as a destination target for the source region for your volume or volume group.
The following table lists the region mappings for cross region replication.
Source Region  | Destination Region  
---|---  
Australia East (Sydney)  | 
  * Australia Southeast (Melbourne)
  * Japan East (Tokyo) 
  * US East (Ashburn)
  * US Midwest (Chicago)
  * US West (Phoenix)
  * US West (San Jose)

  
Australia Southeast (Melbourne)  | 
  * Australia East (Sydney)
  * Singapore (Singapore) 
  * Singapore West (Singapore)
  * US East (Ashburn)
  * US Midwest (Chicago)
  * US West (Phoenix)
  * US West (San Jose)

  
Brazil East (Sao Paulo)  | 
  * Brazil Southeast (Vinhedo)
  * Chile Central (Santiago)
  * Colombia Central (Bogota)
  * US East (Ashburn)
  * US West (Phoenix)
  * US West (San Jose)

  
Brazil Southeast (Vinhedo)  | 
  * Brazil East (Sao Paulo)
  * US East (Ashburn)
  * US West (Phoenix)
  * US West (San Jose)

  
Canada Southeast (Montreal)  | 
  * Canada Southeast (Toronto)

  
Canada Southeast (Toronto)  | 
  * Canada Southeast (Montreal)
  * US Midwest (Chicago)
  * US East (Ashburn)

  
Chile Central (Santiago)  | 
  * Brazil East (Sao Paulo)
  * Chile West (Valparaiso)

  
Chile West (Valparaiso)  | 
  * Chile Central (Santiago)
  * Colombia Central (Bogota)

  
Colombia Central (Bogota)  | 
  * Brazil East (Sao Paulo)
  * Chile West (Valparaiso)
  * Mexico Central (Queretaro)
  * US East (Ashburn)

  
France Central (Paris) | 
  * France South (Marseille)
  * Germany Central (Frankfurt)
  * Italy Northwest (Milan)
  * Netherlands Northwest (Amsterdam)
  * Spain Central (Madrid)
  * Sweden Central (Stockholm)
  * Switzerland North (Zurich) 
  * UK South (London) 
  * UK West (Newport)
  * US East (Ashburn)

  
France South (Marseille) | 
  * France Central (Paris)
  * Germany Central (Frankfurt)
  * Italy Northwest (Milan)
  * Netherlands Northwest (Amsterdam)
  * Spain Central (Madrid)
  * Sweden Central (Stockholm)
  * Switzerland North (Zurich)
  * UK South (London) 
  * UK West (Newport)

  
Germany Central (Frankfurt)  | 
  * France Central (Paris)
  * France South (Marseille)
  * Netherlands Northwest (Amsterdam)
  * Israel Central (Jerusalem)
  * Italy Northwest (Milan)
  * Spain Central (Madrid)
  * Sweden Central (Stockholm)
  * Switzerland North (Zurich)
  * UK South (London)
  * UK West (Newport)

  
India South (Hyderabad)  | 
  * India West (Mumbai)
  * Singapore (Singapore) 
  * Singapore West (Singapore)

  
India West (Mumbai)  | 
  * India South (Hyderabad)
  * Singapore West (Singapore)
  * UK South (London) 

  
Israel Central (Jerusalem) | 
  * Germany Central (Frankfurt)
  * UK South (London)

  
Italy Northwest (Milan) | 
  * France Central (Paris)
  * France South (Marseille)
  * Germany Central (Frankfurt)
  * Netherlands Northwest (Amsterdam)
  * Spain Central (Madrid)
  * Sweden Central (Stockholm)
  * Switzerland North (Zurich) 
  * UK South (London)
  * UK West (Newport)

  
Japan Central (Osaka)  | 
  * Japan East (Tokyo)
  * South Korea Central (Seoul)
  * South Korea North (Chuncheon)
  * US East (Ashburn)
  * US West (Phoenix)
  * US West (San Jose)

  
Japan East (Tokyo)  | 
  * Australia East (Sydney)
  * Japan Central (Osaka)
  * Singapore (Singapore) 
  * Singapore West (Singapore)
  * South Korea Central (Seoul)
  * South Korea North (Chuncheon)
  * US East (Ashburn)
  * US West (Phoenix)
  * US West (San Jose)

  
Mexico Central (Queretaro)  | 
  * Colombia Central (Bogota)
  * Mexico Northeast (Monterrey)
  * US East (Ashburn)
  * US West (Phoenix)
  * US West (San Jose)

  
Mexico Northeast (Monterrey)  | 
  * Mexico Central (Queretaro)
  * US East (Ashburn)
  * US West (Phoenix)
  * US West (San Jose)

  
Netherlands Northwest (Amsterdam)  | 
  * France Central (Paris)
  * Germany Central (Frankfurt)
  * Italy Northwest (Milan)
  * Spain Central (Madrid)
  * Sweden Central (Stockholm)
  * Switzerland North (Zurich) 
  * UK South (London)
  * UK West (Newport)
  * US East (Ashburn)

  
Saudi Arabia West (Jeddah)  | 
  * UAE East (Dubai)

  
Singapore (Singapore)  | 
  * Australia Southeast (Melbourne) 
  * India South (Hyderabad)
  * Japan East (Tokyo)
  * Singapore West (Singapore)

  
Singapore West (Singapore)  | 
  * Australia Southeast (Melbourne) 
  * India South (Hyderabad)
  * India West (Mumbai)
  * Japan East (Tokyo)
  * Singapore (Singapore) 

  
South Africa Central (Johannesburg) | 
  * UK South (London)

  
South Korea Central (Seoul)  | 
  * Japan Central (Osaka) 
  * Japan East (Tokyo)
  * South Korea North (Chuncheon)

  
South Korea North (Chuncheon)  | 
  * Japan Central (Osaka)
  * Japan East (Tokyo) 
  * South Korea Central (Seoul)

  
Spain Central (Madrid)  | 
  * France Central (Paris)
  * France South (Marseille)
  * Germany Central (Frankfurt)
  * Italy Northwest (Milan)
  * Netherlands Northwest (Amsterdam)
  * Sweden Central (Stockholm)
  * Switzerland North (Zurich) 
  * UK South (London)
  * UK West (Newport)

  
Sweden Central (Stockholm) | 
  * France Central (Paris)
  * France South (Marseille)
  * Germany Central (Frankfurt)
  * Italy Northwest (Milan)
  * Netherlands Northwest (Amsterdam)
  * Spain Central (Madrid)
  * Switzerland North (Zurich)
  * UK South (London)
  * UK West (Newport)

  
Switzerland North (Zurich)  | 
  * France Central (Paris)
  * France South (Marseille)
  * Germany Central (Frankfurt)
  * Italy Northwest (Milan)
  * Netherlands Northwest (Amsterdam)
  * Spain Central (Madrid)
  * Sweden Central (Stockholm)
  * UK South (London)
  * UK West (Newport)

  
UAE Central (Abu Dhabi) | 
  * UAE East (Dubai)

  
UAE East (Dubai)  | 
  * Saudi Arabia West (Jeddah)
  * UAE Central (Abu Dhabi)

  
UK South (London)  | 
  * France Central (Paris)
  * France South (Marseille)
  * Germany Central (Frankfurt)
  * India West (Mumbai) 
  * Israel Central (Jerusalem)
  * Italy Northwest (Milan)
  * Netherlands Northwest (Amsterdam)
  * Spain Central (Madrid)
  * Sweden Central (Stockholm)
  * Switzerland North (Zurich)
  * UK West (Newport)
  * US East (Ashburn)

  
UK West (Newport)  | 
  * France Central (Paris)
  * France South (Marseille)
  * Germany Central (Frankfurt)
  * Italy Northwest (Milan)
  * Netherlands Northwest (Amsterdam)
  * Spain Central (Madrid)
  * Sweden Central (Stockholm)
  * Switzerland North (Zurich)
  * UK South (London)

  
US East (Ashburn)  | 
  * Australia East (Sydney)
  * Australia Southeast (Melbourne)
  * Brazil East (Sao Paulo)
  * Brazil Southeast (Vinhedo)
  * Colombia Central (Bogota)
  * Canada Southeast (Toronto) 
  * France Central (Paris)
  * Japan Central (Osaka)
  * Japan East (Tokyo)
  * Mexico Central (Queretaro)
  * Mexico Northeast (Monterrey)
  * Netherlands Northwest (Amsterdam)
  * UK South (London)
  * US Midwest (Chicago)
  * US West (Phoenix)
  * US West (San Jose)

  
US Midwest (Chicago)  | 
  * Australia East (Sydney)
  * Australia Southeast (Melbourne)
  * Canada Southeast (Toronto)
  * US East (Ashburn)
  * US West (Phoenix)
  * US West (San Jose)

  
US West (Phoenix)  | 
  * Australia East (Sydney)
  * Australia Southeast (Melbourne)
  * Brazil East (Sao Paulo)
  * Brazil Southeast (Vinhedo)
  * Japan Central (Osaka)
  * Japan East (Tokyo)
  * Mexico Central (Queretaro)
  * Mexico Northeast (Monterrey)
  * US East (Ashburn)
  * US Midwest (Chicago)
  * US West (San Jose)

  
US West (San Jose)  | 
  * Australia East (Sydney)
  * Australia Southeast (Melbourne)
  * Brazil East (Sao Paulo)
  * Brazil Southeast (Vinhedo)
  * Japan Central (Osaka) 
  * Japan East (Tokyo)
  * Mexico Central (Queretaro)
  * Mexico Northeast (Monterrey)
  * US East (Ashburn)
  * US Midwest (Chicago)
  * US West (Phoenix)

  
## Cross Availability Domain Replication 🔗 
Block Volume replication supports replicating a volume or volume group to another availability domain within the same region. For this type of replication, when you enable replication for a volume or volume group, if the current region contains more than one availability domain, the regions list will include the current region. Select this region as the source region, and then select the availaiblity domain that you want to replicate to.
**Note**
Replication across availability domains is only supported in commercial regions with multiple availability domains. To determine which regions contain more than one availability domain, see the _Availability Domains_ field in the table listing the commercial regions in [About Regions and Availaibility Domains](https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm#About).
## Replication Metrics 🔗 
The Block Volume service emits metrics to help you track volume replication operations. For more information, see [Replication Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm#replicatmetrics) and [Block Volume Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm#Block_Volume_Metrics). 
## Tagging Resources 🔗 
You can apply tags to your resources to help you organize them according to your business needs. You can update the resource later with the desired tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). Any tags applied to the source volume are replicated to the volume replica in the destination region.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes, backups, and volume groups.
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Using the Console 🔗 
### Block Volume Replicas 🔗 
Use the Console procedures in this section for block volume replicas.
[To enable replication for a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Use the steps described in this procedure to enable replication on an existing volume. You can also enable replication when you create a volume, see [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#top "Create a block volume in the Block Volume service.").
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the block volume that you want to enable replication for.
  3. Click **Edit**.
  4. In the **Cross Region Replication** section, select **ON**.
  5. For cross region replication, select the region you want to replicate the volume to, the availability domain to place the volume replica in, and then specify the name for the volume replica.
To replicate to another availability domain in the same region, select the region the volume is located in, the availability domain to place the volume replica in, and then specify the name for the volume replica. 
  6. Optionally, encrypt the volume replica in the destination region by using your own Vault encryption key. Select **Encrypt using customer-managed keys** for **Cross region replication encryption** , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume to. For more information, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys).
  7. Check **CONFIRM** to acknowledge the cost warning.
  8. Click **Save Changes**.


[To update the destination region or availability domain replication settings for a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
To change the destination region or availability domain for cross region replication you need to first turn cross region replication off for a volume. Then specify the new region and availability domain selections when you turn replication on again.
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the block volume that you want to change the replication settings for.
  3. Click **Edit**.
  4. In the **Cross Region Replication** section, select **OFF**.
  5. Check **CONFIRM** to acknowledge the that volume replica will be deleted.
  6. Click **Save Changes**.
  7. Click **Edit**.
  8. In the **Cross Region Replication** section, select **ON**.
  9. For cross region replication, select the region you want to replicate the volume to, the availability domain to place the volume replica in, and then specify the name for the volume replica.
To replicate to another availability domain in the same region, select the region the volume is located in, the availability domain to place the volume replica in, and then specify the name for the volume replica. 
  10. To encrypt the volume replica by using your own Vault encryption key, select **Encrypt using customer-managed keys** for **Cross region replication encryption** , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume to. For more information, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys)
  11. Check **CONFIRM** to acknowledge the cost warning.
  12. Click **Save Changes**.


[To disable cross region replication for a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the block volume that you want to disable replication for.
  3. Click **Edit**.
  4. In the **Cross Region Replication** section, select **OFF**.
  5. Check **CONFIRM** to acknowledge the that volume replica will be deleted.
  6. Click **Save Changes**.


[To activate a volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
**Note**
For volumes in a volume group configured for replication, activate the volume group replica instead of individual volume replicas if you want to ensure that all replicas are activated from the same coordinated synchronization point.
See [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations) and [To activate a volume group replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#activate).
To create a new volume from a volume replica, you need to activate the replica. The activation process creates a new volume by cloning the replica. 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Replicas**. Ensure that you are in correct destination region or availability domain that contains the volume replica you want to activate.
  2. Click the replica that you want to activate.
  3. Click **Activate** to open the **Activate Volume Replica** form.
  4. On the **Activate Volume Replica** form, specify the settings for the new volume, including:
     * Name
     * Compartment
     * (Optional) Cluster Placement Group 
**Note** The **Cluster Placement Group** control only appears in the Console if Cluster Placement Groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources, see [Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups "Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases."). 
     * Size and performance settings
     * Backup policy
     * Volume replication
     * Encryption
     * Tags
  5. Click **Create**. The new volume appears in the block volumes list, in the provisioning state.


[To monitor a replica's status](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
The volume replica's details page provides information about the replica's status.
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Replicas**. Ensure that you are in the destination region and availability domain containing the volume replica that you want to view.
  2. Click the replica that you're interested in.
  3. The replica details page displays the following relevant fields:
     * **Last Sync** : The time of the last data synchronization from the source volume to the replica.
     * **Total Data Transfered** : The amount of data, in GBs, that has been transferred during the replication process for the volume. This includes all data from the point that volume replication was enabled to now.


[To failback a volume replica to the source region](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
To failback a volume replica to the source region, you need activate the volume replica in the destination region, with volume replication enabled, and select the original source region as the target region for replication. 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Replicas**. Ensure that you're in correct destination region that contains the volume replica you want to activate.
  2. Click the replica that you want to activate.
  3. Click **Activate** to open the **Activate Volume Replica** form.
  4. On the **Activate Volume Replica** , specify the settings for the new volume, including:
     * Name
     * Compartment
     * Size and performance settings
     * Backup policy
     * Volume replication
     * Encryption
     * Tags
Ensure that **Volume Replication** is enabled, and select the original source region.
  5. Click **Create**. The new volume appears in the block volumes list, in the provisioning state. After the initial synchronization finishes, the failback process is complete, and you can use the volume in the original source region.


### Boot Volume Replicas 🔗 
Use the Console procedures in this section for boot volume replicas.
[To enable replication for a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Use the steps described in this procedure to enable replication on an existing boot volume. 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. Click the boot volume that you want to enable replication for.
  3. Click **Edit**.
  4. In the **Cross Region Replication** section, select **ON**.
  5. For cross region replication, select the region you want to replicate the boot volume to, the availability domain to place the boot volume replica in, and then specify the name for the boot volume replica.
To replicate to another availability domain in the same region, select the region the boot volume is located in, the availability domain to place the boot volume replica in, and then specify the name for the boot volume replica. 
  6. Optionally, encrypt the boot volume replica in the destination region by using your own Vault encryption key. Select **Encrypt using customer-managed keys** for **Cross region replication encryption** , and then specify the OCID for a valid encryption key in the region you selected to replicate the boot volume to. For more information, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys).
  7. Check **CONFIRM** to acknowledge the cost warning.
  8. Click **Save Changes**.


[To update the destination region or availability domain replication settings for a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
To change the destination region or availability domain for cross-region replication you need to first turn cross-region replication off for a boot volume. Then specify the new region and availability domain selections when you turn cross-region replication on again.
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. Click the boot volume that you want to change the replication settings for.
  3. Click **Edit**.
  4. In the **Cross Region Replication** section, select **OFF**.
  5. Check **CONFIRM** to acknowledge the that boot volume replica will be deleted.
  6. Click **Save Changes**.
  7. Click **Edit**.
  8. In the **Cross Region Replication** section, select **ON**.
  9. For cross region replication, select the region you want to replicate the boot volume to, the availability domain to place the boot volume replica in, and then specify the name for the boot volume replica.
To replicate to another availability domain in the same region, select the region the boot volume is located in, the availability domain to place the boot volume replica in, and then specify the name for the boot volume replica. 
  10. To encrypt the volume replica by using your own Vault encryption key, select **Encrypt using customer-managed keys** for **Cross region replication encryption** , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume to. For more information, see [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys).
  11. Check **CONFIRM** to acknowledge the cost warning.
  12. Click **Save Changes**.


[To disable cross region replication for a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. Click the boot volume that you want to disable replication for.
  3. Click **Edit**.
  4. In the **Cross Region Replication** section, select **OFF**.
  5. Check **CONFIRM** to acknowledge the that boot volume replica will be deleted.
  6. Click **Save Changes**.


[To activate a boot volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
**Note**
For volumes in a volume group configured for replication, activate the volume group replica instead of individual volume replicas to ensure that all replicas are activated from the same coordinated synchronization point.
See [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations) and [To activate a volume group replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#activate).
To create a new volume from a volume replica, you need to activate the replica. The activation process creates a new volume by cloning the replica. 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volume Replicas**. Ensure that you're in correct destination region that contains the boot volume replica you want to activate.
  2. Click the boot volume replica that you want to activate.
  3. Click **Activate** to open the **Activate Volume Replica** form.
  4. On the **Activate Volume Replica** , specify the settings for the new volume, including:
     * Name
     * Compartment
     * (Optional) Cluster Placement Group 
**Note** The **Cluster Placement Group** control only appears in the Console if Cluster Placement Groups are enabled for the tenancy, and you've created and activated a cluster placement group with the capability added for volume resources, see [Cluster Placement Groups for Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups "Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases.").
     * Size and performance settings
     * Backup policy
     * Volume replication
     * Encryption
     * Tags
  5. Click **Create**. The new volume will appear in the boot volumes list, in the provisioning state.


[To monitor a boot volume replica's status](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
The boot volume replica's details page provides information about the replica's status.
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volume Replicas**. Ensure that you are in the destination region and availability domain containing the boot volume replica that you want to view.
  2. Click the replica that you're interested in.
  3. The replica details page displays the following relevant fields:
     * **Last Sync** : The time of the last data synchronization from the source boot volume to the replica.
     * **Total Data Transfered** : The amount of data, in GBs, that has been transferred during the replication process for the boot volume. This includes all data from the point that cross-region replication was enabled to now.


[To failback a boot volume replica to the source region](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
To failback a boot volume replica to the source region, you need activate the boot volume replica in the destination region, with volume replication enabled, and select the original source region as the target region for replication.
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volume Replicas**. Ensure that you are in correct destination region that contains the boot volume replica you want to activate.
  2. Click the replica that you want to activate.
  3. Click **Activate** to open the **Activate Volume Replica** form.
  4. On the **Activate Volume Replica** , specify the settings for the new boot volume, including:
     * Name
     * Compartment
     * Size and performance settings
     * Backup policy
     * Volume replication
     * Encryption
     * Tags
Ensure that **Volume Replication** is enabled, and select the original source region.
  5. Click **Create**. The new boot volume will appear in the boot volumes list, in the provisioning state. Once the initial synchronization finishes, the failback process is complete, and you can use the boot volume in the original source region.


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
### Block Volume Operations 🔗 
Use the following operations for cross region replication of block volumes.
[To enable cross region replication when creating a block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume create --compartment-id <compartment_ID> --block-volume-replicas '[{"displayName":"<display_name>","availabilityDomain":"<availability-domain_ID>","xrrKmsKeyId" : "<kms_key_ID>"}]' 
```

For example:
Command
CopyTry It
```
oci bv volume create --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --block-volume-replicas '[{"displayName":"Sample_Replica","availabilityDomain":"pjBI:US-ASHBURN-AD-1","xrrKmsKeyId" : "ocid1.key.oc1.iad-ad-1.<unique_ID>"}]'
```

[To enable cross region replication when updating a block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume update --volume-id <volume_ID> --block-volume-replicas '[{"displayName":"<display_name>","availabilityDomain":"<availability-domain_ID>","xrrKmsKeyId" : "<kms_key_ID>"}]' 
```

For example:
Command
CopyTry It
```
oci bv volume update --volume-id ocid1.volume.oc1.phx.<unique_ID> --block-volume-replicas '[{"displayName":"Sample_Replica","availabilityDomain":"pjBI:US-ASHBURN-AD-1","xrrKmsKeyId" : "ocid1.key.oc1.iad-ad-1.<unique_ID>"}]'
```

[To disable cross region replication for a block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume update --volume-id <volume_ID> --block-volume-replicas '[]' 
```

For example:
Command
CopyTry It
```
oci bv volume update --volume-id ocid1.volume.oc1.phx.<unique_ID> --block-volume-replicas '[]'
```

[To activate a block volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
**Note**
For volumes in a volume group configured for replication, activate the volume group replica instead of individual volume replicas if you want to ensure that all replicas are activated from the same coordinated synchronization point.
See [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations) and [To activate a volume group replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegroupreplication_topic_CLI_To_activate_volume_group_replica).
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume create --source-volume-replica-id <volume_ID> --compartment-id <compartment_ID> --availability-domain <availability_domain> 
```

For example:
Command
CopyTry It
```
oci bv volume create --source-volume-replica-id ocid1.blockvolumereplica.oc1.phx.<unique_ID> --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --availability-domain ABbv:PHX-AD-1 
```

[To list block volume replicas](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv block-volume-replica list --availability-domain <availability_domain> --compartment-id <compartment_ID>
```

For example:
Command
CopyTry It
```
oci bv block-volume-replica list --availability-domain ABbv:PHX-AD-1 --compartment-id ocid1.compartment.oc1.phx.<unique_ID> 
```

[To retrieve a block volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv block-volume-replica get --block-volume-replica-id <block-volume-replica-ID>
```

For example:
Command
CopyTry It
```
oci bv block-volume-replica get --block-volume-replica-id ocid1.blockvolumereplica.oc1.phx.<unique_ID>
```

### Boot Volume Operations 🔗 
Use the following operations for cross region replication of boot volumes.
[To enable cross region replication when creating a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume create --source-boot-volume-id <volume_ID> --compartment-id <compartment_ID> --boot-volume-replicas '[{"displayName":"<display_name>","availabilityDomain":"<availability-domain_ID>","xrrKmsKeyId" : "<kms_key_ID>"}]' 
```

For example:
Command
CopyTry It
```
oci bv boot-volume create --source-boot-volume-id ocid1.bootvolume.oc1.phx.<unique_ID> --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --boot-volume-replicas '[{"displayName":"Sample_Replica","availabilityDomain":"pjBI:US-ASHBURN-AD-1","xrrKmsKeyId" : "ocid1.key.oc1.iad-ad-1.<unique_ID>"}]'
```

[To enable cross region replication when updating a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume update --boot-volume-id <volume_ID> --boot-volume-replicas '[{"displayName":"<display_name>","availabilityDomain":"<availability-domain_ID>","xrrKmsKeyId" : "<kms_key_ID>"}]' 
```

For example:
Command
CopyTry It
```
oci bv boot-volume update --boot-volume-id ocid1.bootvolume.oc1.phx.<unique_ID> --boot-volume-replicas '[{"displayName":"Sample_Replica","availabilityDomain":"pjBI:US-ASHBURN-AD-1","xrrKmsKeyId" : "ocid1.key.oc1.iad-ad-1.<unique_ID>"}]'
```

[To disable cross region replication for a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume update --boot-volume-id <volume_ID> --boot-volume-replicas '[]' 
```

For example:
Command
CopyTry It
```
oci bv boot-volume update --boot-volume-id ocid1.bootvolume.oc1.phx.<unique_ID> --boot-volume-replicas '[]'
```

[To activate a boot volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
**Note**
For volumes in a volume group configured for replication, activate the volume group replica instead of individual volume replicas if you want to ensure that all replicas are activated from the same coordinated synchronization point.
See [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations) and [To activate a volume group replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegroupreplication_topic_CLI_To_activate_volume_group_replica).
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume create --source-volume-replica-id <volume_ID> --compartment-id <compartment_ID> --availability-domain <availability_domain> 
```

For example:
Command
CopyTry It
```
oci bv boot-volume create --source-volume-replica-id ocid1.bootvolumereplica.oc1.phx.<unique_ID> --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --availability-domain ABbv:PHX-AD-1 
```

[To list boot volume replicas](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume-replica list --availability-domain <availability_domain> --compartment-id <compartment_ID>
```

For example:
Command
CopyTry It
```
oci bv boot-volume-replica list --availability-domain ABbv:PHX-AD-1 --compartment-id ocid1.compartment.oc1.phx.<unique_ID> 
```

[To retrieve a boot volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume-replica get --boot-volume-replica-id <boot-volume-replica-ID>
```

For example:
Command
CopyTry It
```
oci bv boot-volume-replica get --boot-volume-replica-id ocid1.bootvolumereplica.oc1.phx.<unique_ID>
```

## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following operations to list and retrieve volume replicas:
  * [ListBlockVolumeReplicas](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BlockVolumeReplica/ListBlockVolumeReplicas)
  * [GetBlockVolumeReplica](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BlockVolumeReplica/GetBlockVolumeReplica)
  * [ListBootVolumeReplicas](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeReplica/ListBootVolumeReplicas)
  * [GetBootVolumeReplica](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeReplica/GetBootVolumeReplica)
  * [ListVolumeGroupReplicas](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupReplica/ListVolumeGroupReplicas)
  * [GetVolumeGroupReplica](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupReplica/GetVolumeGroupReplica)


You can enable replication for a boot volume or block volume when you create or update a volume. To disable replication, use the Update operation. To activate a volume replica, use the Create operation and pass the source volume's replica ID.
  * [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume)
  * [CreateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/CreateBootVolume)
  * [CreateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup)
  * [UpdateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)
  * [UpdateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume)
  * [UpdateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/UpdateVolumeGroup)


**Note** For volumes in a volume group configured for replication, use [CreateVolumeGroup](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/CreateVolumeGroup) to activate replicas instead of [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) or [CreateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/CreateBootVolume) if you want to ensure that all replicas are activated from the same coordinated synchronization point. See [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegropureplication_topic_Limits_and_Considerations).
Was this article helpful?
YesNo

