Updated 2024-05-13
# Cluster Placement Groups for Block Volume
Oracle Cloud Infrastructure Cluster Placement Groups lets you create resources in close proximity to one another to support low-latency networking use cases.
With Cluster Placement Groups, you can deploy block volumes and compute instances into the same logical grouping, known as a **cluster placement group** , to ensure that they're placed physically near one another in an availability domain. For more information, see [Overview of Cluster Placement Groups](https://docs.oracle.com/iaas/Content/cluster-placement-groups/overview.htm).
## Prerequisites 🔗 
Cluster Placement Groups can only be used if the following prerequisites are met:
  * Cluster Placement Groups must be enabled for the tenancy.
  * The region where you're creating the volume must have at least one cluster placement group [created](https://docs.oracle.com/iaas/Content/cluster-placement-groups/create-cluster-placement-group.htm) and [activated](https://docs.oracle.com/iaas/Content/cluster-placement-groups/activate-cluster-placement-group.htm), with the capabilities configured to support the volume resource for block-storage.


## Limitations and Considerations 🔗 
  * You need to configure the [capabilities](https://docs.oracle.com/iaas/Content/cluster-placement-groups/overview.htm#concepts) supported by the cluster placement group when you [create](https://docs.oracle.com/iaas/Content/cluster-placement-groups/create-cluster-placement-group.htm) it, you can't edit the capabilities after the cluster placement group has been created. You can see the capabilities supported by a cluster placement group in the Console, in the **Intended use** field on the details page, see [Getting a Cluster Placement Group's Details](https://docs.oracle.com/iaas/Content/cluster-placement-groups/get-cluster-placement-group.htm).
  * A cluster placement group can only be selected when a volume is created. This applies to all methods of creating a volume, including cloning, restoring a backup, and activating a replica, see [Cluster Placement Groups for Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/clusterplacementgroups.htm#clusterplacementgroups_volumes).
  * Volumes can't be moved from one cluster placement group to another. You can use volume clones or restore from backups as methods to migrate a volume to another cluster placement group.
  * When you create a volume, the volume is in the provisioning state. If the volume is created successfully in the cluster placement group, the volume transitions to the available state. When there's no capacity available in the cluster placement group, the created volume transitions from the provisioning state to the terminated state instead, meaning that the volume creation didn't succeed. If the volume creation fails, you might need to [contact support](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport_topic-Open_a_support_service_request.htm) to request capacity.
  * You can attach volumes in one cluster placement group to an instance in the same or different cluster placement group, or an instance that's not in any cluster placement group or vice versa. However, if latency performance is important, we recommend that you place volumes and instances in the same cluster placement group.
  * When attaching a volume to more than one instance, the instances don't need to be in the same cluster placement group.
  * When you deactivate and delete a cluster placement group, any volume resources in that cluster placement group are disassociated from the cluster placement group, however no volumes are deleted.


## Cluster Placement Groups for Volumes 🔗 
**Tip** In the Console, the Cluster Placement Group dropdown only appears if Cluster Placement Groups are enabled for the tenancy. You must have also created and activated one or more cluster placement groups, configured with the capability for volume resources. If you're using the CLI or API to create the volume you can specify a cluster placement group, but the request fails if the cluster placement group doesn't exist or Cluster Placement Groups aren't enabled for the tenancy.
You can only add a block volume to a cluster placement group when you create the volume, by selecting an option from the **Cluster Placement Group** control. The **Cluster Placement Group** control only appears in the Console if Cluster Placement Groups are enabled for the tenancy, and you have created and activated a cluster placement group configured with the capability for **volume** resources. This applies to all methods of creating a volume, including:
  * [Creating a block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#top "Create a block volume in the Block Volume service.")
  * [Restoring a volume from a backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringavolumefromabackup.htm#Restoring_a_Backup_to_a_New_Volume)
  * [Activating a volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#activateblockreplica)
  * [Cloning a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm#Cloning_a_Volume "Create a clone from a volume by using the Block Volume service. Cloning lets you to make a copy of an existing block volume without needing to go through the backup and restore process.")


## Cluster Placement Groups for Boot Volumes 🔗 
When you [create an instance](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm), you can specify a cluster placement group on the Advanced tab of the [instance details section](https://docs.oracle.com/iaas/Content/Compute/Tasks/launchinginstance.htm#console__define-instance-details) of the create workflow. The instance's boot volume is created in the same cluster placement group as the instance.
You can select a cluster placement group for a boot volume when you [clone](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningabootvolume.htm#Cloning_a_Boot_Volume) a boot volume, [restore a boot volume backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingbootvolume.htm#Restoring_a_Boot_Volume), or [activate](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#activatebootreplica) a boot volume replica.
## Cluster Placement Groups for Volume Groups 🔗 
When you add volumes to a volume group, you can select volumes that are in the same cluster placement group, different cluster placement groups, or no cluster placement groups.
If you select a cluster placement group when you [clone a volume group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/clone-volume-group.htm#top "Clone a volume group in the Block Volume service."), [activate a group volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#activate), or [restore a group volume backup](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroups.htm#To_restore_a_volume_group_from_a_volume_group_backup), all the volumes are created in the specified cluster placement group.
Was this article helpful?
YesNo

