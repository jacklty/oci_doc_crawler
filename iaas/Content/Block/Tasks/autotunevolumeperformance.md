Updated 2024-06-04
# Dynamic Performance Scaling
Block Volume provides dynamic performance scaling with autotuning. This feature enables you to configure your volumes so that the service adjusts the performance level automatically to optimize performance.
There are two types of dynamic performance scaling with autotuning you can enable for volumes:
  * **[Performance Based Auto-tuning](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm#perf):** When this option is enabled, Block Volume adjusts the volume's performance between the levels you specify, based on the monitored performance for the volume.
  * **[Detached Volume Auto-tuning](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm#detached):** When this option is enabled, Block Volume adjusts the volume's performance level based on whether the volume is attached or detached from an instance.


## Performance Based Dynamic Scaling  🔗 
The performance based autotuning feature enables Block Volume to adjust the volume's performance between levels you specify, based on the actual monitored performance of a volume. 
When you enable performance based dynamic scaling with autotuning, you specify the default performance setting (VPUs/GB), which is lowest performance level the volume will be adjusted to when attached to an instance. You also specify the maximum performance level (VPUs/GB), which is the maximum performance level the volume will be adjusted to. Block Volume monitors the volume's performance using the following metrics:
  * Volume throttled operations
  * Volume guaranteed VPUs/GB
  * Volume guaranteed IOPS
  * Volume guaranteed throughput


These metrics help the service determine the load on the volume and whether the performance level needs to be adjusted. For more information about these metrics, see [Performance Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm#perfmetrics) and [Block Volume Metrics](https://docs.oracle.com/en-us/iaas/Content/Block/References/volumemetrics.htm#Block_Volume_Metrics). 
When viewing the **Block Volume Details** or **Boot Volume Details** pages in the Console, the applicable fields are:
  * **Default Performance** : When **Performance Based Auto-tune** is enabled, this is the lowest performance level that Block Volume will adjust the performance to when the volume is attached. If **Performance Based Auto-tune** is disabled, this is the volume's performance level. If you have enabled **Detached Volume Auto-tune** , and the volume is detached, this is the performance level the volume will be adjusted to when the volume is reattached to an instance. 
  * **Auto-tuned Performance** : This is the volume's effective performance. If **Performance Based Auto-tune** is disabled for the volume, this is the same as the default performance for the volume.
  * **Performance Based Auto-tune** : This field indicates whether the performance based autotuning feature is enabled for the volume. When it is off, the volume's **Auto-tuned Performance** is always the same as what is specified for **Default Performance**. 


When **Performance Based Auto-tune** is enabled, Block Volume adjusts the performance to the default level as much as possible. As load on the volume increases, the service ramps up the performance level up as needed, on a best-effort basis.
The adjustments to ramp up the performance are fast acting, repeated actions, in tens of seconds, to provide steady performance increases as needed. The adjustments to ramp down the performance are slow-acting, with the initial adjustment taking effect in an hour, and then subsequent adjustments taking minutes. This avoids reducing volume performance abruptly while the performance is still needed. 
## Detached Volume Performance Autotuning 🔗 
The detached volume performance autotuning feature enables Block Volume to adjust the volume's performance level to the optimal level based on the attached state of the volume.
If this feature is enabled, when the volume is detached, the Block Volume service adjusts the performance level to **Lower Cost** (0 VPUs/GB) for both block volumes and boot volumes. When the volume is reattached, the performance is adjusted back to the performance level specified by the default VPUs/GB setting. If performance based dynamic scaling with autotuning is also enabled, it will take effect at this point to further dynamically scale performance as needed by workloads that use the volume. 
When viewing the **Block Volume Details** or **Boot Volume Details** pages in the Console, the applicable fields are:
  * **Default Performance** : When **Performance Based Auto-tune** is disabled, this is the volume's performance level that you specify when you create the volume or when you change the performance setting for an existing volume. When the volume is attached, regardless of whether **Detached Volume Auto-tune** is enabled or not, this is the volume's performance.
  * **Auto-tuned Performance** : This is the volume's effective performance. If **Detached Volume Auto-tune** is enabled for the volume, **Auto-tuned Performance** will be adjusted to **Lower Cost** when the volume is detached. Note that **Auto-tuned Performance** won't show the performance setting as **Lower Cost** until the performance adjustment is complete.
  * **Detached Volume Auto-tune** : This field indicates whether **Detached Volume Auto-tune** is enabled for the volume. When it is off, the volume's effective performance is always the same as what is specified for **Default Performance**. When it is on, the volume performance is adjusted to **Lower Cost** when the volume is detached.


See [Timing Limits and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm#autotunevolumeperformance_topic-limits_and_considerations) for details about when these settings take effect.
### Timing Limits and Considerations 🔗 
The following list identifies some timing considerations you should be aware of when using the detached volume autotuning feature.
  * When you enable **Detached Volume Auto-tune** for a detached volume, the Block Volume service starts the performance adjustment to **Lower Cost** after 14 days. 
  * When you enable **Detached Volume Auto-tune** for an attached volume, the Block Volume service starts the performance adjustment to **Lower Cost** 14 days after you detach the volume.
  * If you disable **Detached Volume Auto-tune** while a volume is detached, Block Volume service starts the performance adjustment to the **Default Performance** setting right away.
  * If you change the **Default Performance** for a detached volume with **Detached Volume Auto-tune** enabled, the **Auto-tuned Performance** for the volume will remain **Lower Cost** until you reattach the volume.
  * If you clone a detached volume with **Detached Volume Auto-tune** enabled, the Block Volume service starts the performance adjustment to **Lower Cost** after 14 days. 
  * To optimize performance for a volume configured for **Ultra High Performance** , the volume attachment needs to be enabled for multipath. When you reattach a volume that has had the detached volume autotuned to **Lower Cost** , but the volume is configured for **Ultra High Performance** , you need to confirm that the attachment is multipath-enabled after the volume is reattached. For more information, see:
    * [Attaching Ultra High Performance Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#multipath)
    * [Checking if a Volume Attachment is Multipath-Enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/multipathcheck.htm#multipathcheck "When you attach a volume configured for the Ultra High Performance level, the volume attachment must be enabled for multipath to optimize the volume's performance. This topic describes how to verify if the volume attachment is multipath-enabled.")
    * [Supported Compute Shapes for Multipath-Enabled Paravirtualized Attachments](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/configuringmultipathattachments.htm#multipath_shapes_pv)


## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The policy in [Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-admins-manage-volumes-and-backups) lets the specified group do everything with block volumes and backups, but not launch instances. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). For reference material about writing policies for instances, cloud networks, or other Core Services API resources, see [Details for the Core Services](https://docs.oracle.com/iaas/Content/Identity/policyreference/corepolicyreference.htm).
## Using the Console 🔗 
The following procedures describe how to enable the autotuning features in the Console.
[To enable performance based autotuning for a block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the block volume that you want to enable performance based autotuning for.
  3. Click **Edit**.
  4. In the **Volume Size and Performance** section, click the **Performanced Based Auto-tune** slider so that it changes from **Off** to **On**.
  5. Specify a value for **Default VPUs/GB**. This is the minimum performance setting the volume will be adjusted to. The value must be a multiple of 10. The minimum value is 10 and the maximum value is 110. You can also use the **VPUs/GB** slider to specify the value.
  6. Specify a value for **Maximum VPUs/GB**. This is the maximum performance setting the volume will be adjusted to. The value must be a multiple of 10, and must be at least 10 VPUs/GB higher than **Default VPUs/GB**. The maximum value is 120 VPUs/GB. You can also use the **VPUs/GB** slider to specify the value. 
  7. Click **Save Changes**.


[To enable performance based autotuning for a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. Click the block volume that you want to enable performance based autotuning for.
  3. Click **Edit**.
  4. In the **Volume Size and Performance** section, click the **Performanced Based Auto-tune** slider so that it changes from **Off** to **On**.
  5. Specify a value for **Default VPUs/GB**. This is the minimum performance setting the volume will be adjusted to. The value must be a multiple of 10. The minimum value is 10 and the maximum value is 110. You can also use the **VPUs/GB** slider to specify the value.
  6. Specify a value for **Maximum VPUs/GB**. This is the maximum performance setting the volume will be adjusted to. The value must be a multiple of 10, and must be at least 10 VPUs/GB higher than **Default VPUs/GB**. The maximum value is 120 VPUs/GB. You can also use the **VPUs/GB** slider to specify the value. 
  7. Click **Save Changes**.


[To enable detached volume autotuning for a block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. Click the block volume that you want to enable detached volume autotuning for.
  3. Click **Edit**.
  4. In the **Volume Size and Performance** section, click the **Detached Volume Auto-tune** slider so that it changes from **Off** to **On**.
  5. Click **Save Changes**.


[To enable detached volume autotuning for a boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**. 
  2. Click the boot volume that you want to enable detached volume autotuning for
  3. Click **Edit**.
  4. In the **Volume Size and Performance** section, click the **Detached Volume Auto-tune** slider so that it changes from **Off** to **On**.
  5. Click **Save Changes**.


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm). 
### Block Volume Operations 🔗 
Use the following operations for enabling autotuning for block volumes.
[To enable performance based autotuning when creating a block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume create --compartment-id <compartment_ID> --autotune-policies <auto-tune_policies_JSON>' 
```

For example:
Command
CopyTry It
```
oci bv volume create --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --autotune-policies '[{"autotune-type": "PERFORMANCE_BASED", "maxVpusPerGB": 50}]''
```

[To enable performance based autotuning for an existing block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume update --volume-id <volume_ID> --compartment-id <compartment_ID> --autotune-policies <auto-tune_policies_JSON>' 
```

For example:
Command
CopyTry It
```
oci bv volume update --volume-id ocid1.volume.oc1.phx.<unique_ID> --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --autotune-policies '[{"autotune-type": "PERFORMANCE_BASED", "maxVpusPerGB": 50}]''
```

[To enable detached volume autotuning when creating a block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume create --compartment-id <compartment_ID> --autotune-policies <auto-tune_policies_JSON>' 
```

For example:
Command
CopyTry It
```
oci bv volume create --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --autotune-policies '[{"autotune-type": "DETACHED_VOLUME"}]''
```

[To enable detached volume autotuning for an existing block volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume update --volume-id <volume_ID> --compartment-id <compartment_ID> --autotune-policies <auto-tune_policies_JSON>' 
```

For example:
Command
CopyTry It
```
oci bv volume update --volume-id ocid1.volume.oc1.phx.<unique_ID> --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --autotune-policies '[{"autotune-type": "DETACHED_VOLUME"}]''
```

### Boot Volume Operations 🔗 
Use the following operations for enabling autotuning for boot volumes.
[To enable performance based autotuning for an existing boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume update --volume-id <volume_ID> --compartment-id <compartment_ID> --autotune-policies <auto-tune_policies_JSON>' 
```

For example:
Command
CopyTry It
```
oci bv boot-volume update --volume-id ocid1.volume.oc1.phx.<unique_ID> --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --autotune-policies '[{"autotune-type": "PERFORMANCE_BASED", "maxVpusPerGB": 50}]''
```

[To enable detached volume autotuning for an existing boot volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/autotunevolumeperformance.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume update --volume-id <volume_ID> --compartment-id <compartment_ID> --autotune-policies <auto-tune_policies_JSON>' 
```

For example:
Command
CopyTry It
```
oci bv boot-volume update --volume-id ocid1.volume.oc1.phx.<unique_ID> --compartment-id ocid1.compartment.oc1.phx.<unique_ID> --autotune-policies '[{"autotune-type": "DETACHED_VOLUME"}]''
```

## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
You enable autotuning for a volume by specifying the `AutotunePolicy` values for the `autotunePolicies` attribute in the applicable volume details for the API operation.
For performance based autotuning, specify `PERFORMANCE_BASED` as the autotuneType. When specifying this type, you also need to specify the maximum VPUs to adjust the volume to in the `maxVpusPerGB` attribute. See [PerformanceBasedAutotunePolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/PerformanceBasedAutotunePolicy). 
For detached volume autotuning, specify `DETACHED_VOLUME` as the `autotuneType`. See [DetachedVolumeAutotunePolicy](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/DetachedVolumeAutotunePolicy).
### Block Volumes
To enable autotuning for new block volumes, use the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) and specify the autotuning features you want to enable in the `autotunePolicies` attribute of the [CreateVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateVolumeDetails). 
To enable autotuning for an existing block volume, use the [UpdateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/UpdateVolume) and specify the autotuning features you want to enable in the `autotunePolicies` attribute of the [UpdateVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateVolumeDetails). 
### Boot Volumes
To enable or disable the autotuning performance feature for a boot volume, use the [UpdateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/UpdateBootVolume) operation and specify the autotuning features you want to enable in the `autotunePolicies` attribute of the [UpdateBootVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/UpdateBootVolumeDetails). 
Was this article helpful?
YesNo

