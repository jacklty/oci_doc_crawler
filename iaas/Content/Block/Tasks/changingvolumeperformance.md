Updated 2024-06-04
# Changing the Performance of a Volume
The Block Volume service enables you to dynamically configure the performance level for block volumes and boot volumes, for more information, see [Block Volume Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeperformance.htm#Block_Volume_Performance).
If you configure performance level for a block volume to the ultra high performance level the volume attachment should be multipath-enabled. You may need to take additional steps to optmize the volume's performance, for more information, see [Attaching Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#multipath). This does not apply to boot volumes configured for the ultra high performance level.
**Note** When you change a block volume's performance to ultra high performance from any other performance level you need to detach and then reattach the volume. See [Detaching a Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#Detaching_a_Volume "Detach a block volume from an instance.") and [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.").
## Required IAM Service Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes and backups, but not launch instances. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Limitations 🔗 
  * When you adjust the VPUs/GB setting for a volume, the volume's lifecycle state transitions to **Provisioning** while service updates the settings. During this process, you can't attach the volume to an instance or perform other volume operations. After this process is complete, the volume lifecycle state transitions back to **Available**. At this point, you can attach the volume to an instance.
  * You can only change the performance level on three volumes concurrently per tenancy.


## Using the Console 🔗 
The default volume performance setting for existing block volumes or when you create a new block volume is **Balanced**. You can change the default setting when you create a new block volume, see [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#top "Create a block volume in the Block Volume service."). You can also change the volume performance setting for an existing block volume using the steps in the following procedure.
[To change the volume performance for an existing block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changingvolumeperformance.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the block volume that you want to change the performance for.
  3. Click **Edit**.
  4. Using the **VPUs/GB** slider, specify the performance setting you want to change to. You can also specify the VPUs/GB value for the performance setting in **Default VPUs/GB**.
  5. Click **Save Changes**.


[To change the volume performance for an existing boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/changingvolumeperformance.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. Click the boot volume that you want to change the performance for.
  3. Click **Edit Size or Performance**.
  4. Click the volume performance option you want to change to.
  5. Click **Save Changes**.


If you are changing the boot volume's performance to the **Ultra High Performance** level, see [Boot Volumes and Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance__uhpboot) for additional details.
## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
Use the `volume update` operation or the `boot-volume update` operation with `vpus-per-gb` parameter to update a block volume's elastic performance setting. The `vpus-per-gb` parameter is where you specify the volume performance units (VPUs). VPUs represent the volume performance settings, with the following allowed values:
  * `0`: Represents the **Lower Cost** setting, applies to block volumes only. 
  * `10`: Represents the **Balanced** setting, applies to both block volumes and boot volumes. 
  * `20`: Represents the **Higher Performance** setting, applies to both block volumes and boot volumes. 
  * `30` to `120`: Represents the **Ultra High Performance** setting, applies to both block volumes and boot volumes. 


For example:
Command
CopyTry It
```
oci bv volume update --volume-id <volume_ID> --vpus-per-gb 20
```

If you are changing a boot volume's performance to the **Ultra High Performance** level, see [Boot Volumes and Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance__uhpboot) for additional details.
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
### Block Volumes
To update a block volume's performance setting, use the following operation: 
  * [UpdateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume)


The volume performance setting is specified in volume performance units (VPUs) in the `vpusPerGB` attribute of [UpdateVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails). 
Following are the allowed values for `vpusPerGB`:
  * `0`: Represents the **Lower Cost** setting, applies to block volumes only. 
  * `10`: Represents the **Balanced** setting, applies to both block volumes and boot volumes. 
  * `20`: Represents the **Higher Performance** setting, applies to both block volumes and boot volumes. 
  * `30` to `120`: Represents the **Ultra High Performance** setting, applies to both block volumes and boot volumes. 


### Boot Volumes
To update a boot volume's performance setting, use the following operation: 
  * [UpdateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume)


The volume performance setting is specified in the `vpusPerGB` attribute of [UpdateBootVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateBootVolumeDetails). 
Following are the allowed values for `vpusPerGB`:
  * `0`: Represents the **Lower Cost** setting, applies to block volumes only. 
  * `10`: Represents the **Balanced** setting, applies to both block volumes and boot volumes. 
  * `20`: Represents the **Higher Performance** setting, applies to both block volumes and boot volumes. 
  * `30` to `120`: Represents the **Ultra High Performance** setting, applies to both block volumes and boot volumes. 


If you are changing the boot volume's performance to the **Ultra High Performance** level, see [Boot Volumes and Ultra High Performance](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/blockvolumeultrahighperformance.htm#Higher_Performance__uhpboot) for additional details.
Was this article helpful?
YesNo

