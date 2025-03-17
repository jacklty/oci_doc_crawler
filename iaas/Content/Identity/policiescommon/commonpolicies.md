Updated 2024-12-18
# Policy Builder Policy Templates
This section includes some common policies you might want to use in your organization. 
**Note**
These policies use example group and compartment names. Make sure to replace them with your own names.
[Let the Help Desk manage users](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to create, update, and delete users and their credentials. It doesn't include the ability to put users in groups.
**Where to create the policy:** In the tenancy, because users reside in the tenancy. 
Copy
```
Allow group HelpDesk to manage users in tenancy
```

[Let auditors inspect your resources](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to list the resources in all compartments. Be aware that:
  * The operation to list IAM policies includes the contents of the policies themselves
  * The list operations for Networking resource-types return all the information (for example, the contents of security lists and route tables)
  * The operation to list instances requires the `read` verb instead of `inspect`, and the contents include the user-provided metadata. 
  * The operation to view Audit service events requires the `read` verb instead of `inspect`. 


**Where to create the policy:** In the tenancy. Because of the concept of _[Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM.")_ , auditors can then inspect both the tenancy and all compartments beneath it. Or you could choose to give auditors access to only specific compartments if they don't need access to the entire tenancy.
Copy
```
Allow group Auditors to inspect all-resources in tenancy
Allow group Auditors to read instances in tenancy
Allow group Auditors to read audit-events in tenancy
```

[Let network admins manage a cloud network](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to manage all components in Networking. This includes cloud networks, subnets, gateways, virtual circuits, security lists, route tables, and so on. If the network admins need to launch instances to test network connectivity, see [Let users launch compute instances](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm#launch-instances). 
**Where to create the policy:** In the tenancy. Because of the concept of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."), NetworkAdmins can then manage a cloud network in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group NetworkAdmins to manage virtual-network-family in tenancy

```

[Let network admins manage load balancers](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to manage all components in Load Balancer. If the group needs to launch instances, see [Let users launch compute instances](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm#launch-instances). 
**Where to create the policy:** In the tenancy. Because of the concept of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."), NetworkAdmins can then manage load balancers in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group NetworkAdmins to manage load-balancers in tenancy
```

If the group uses the Console to manage load balancers, an additional policy to use the associated networking resources is required:
Copy
```
Allow group NetworkAdmins to manage load-balancers in tenancy
Allow group NetworkAdmins to use virtual-network-family in tenancy

```

If a particular group needs to update existing load balancers (for example, modify the backend set) but not create or delete them, use this statement:
Copy
```
Allow group LBUsers to use load-balancers in tenancy
```

[Let users launch compute instances](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do everything with instances launched into the cloud network and subnets in **compartment** XYZ, and attach/detach any existing volumes that already exist in compartment ABC. The first statement also lets the group create and manage instance images in compartment ABC. If the group doesn't need to attach or detach volumes, you can delete the `volume-family` statement.
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartments (ABC and XYZ) to have control over the individual policy statements for their compartments, see [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM.").
Copy
```
Allow group InstanceLaunchers to manage instance-family in compartment ABC
Allow group InstanceLaunchers to read app-catalog-listing in tenancy
Allow group InstanceLaunchers to use volume-family in compartment ABC
Allow group InstanceLaunchers to use virtual-network-family in compartment XYZ

```

To allow users to create new cloud networks and subnets, see [Let network admins manage a cloud network](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm#network-admins-manage-cloud-network).
To allow users to determine whether capacity is available for a specific shape before creating an instance, add the following statement to the policy:
Copy
```
Allow group InstanceLaunchers to manage compute-capacity-reports in tenancy
```

[Let users launch compute instances from a specific custom image](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to launch instances into the cloud network and subnets in compartment XYZ using only the specified custom image. The policy also includes the ability to attach/detach any existing volumes that already exist in compartment ABC. If the group doesn't need to attach/detach volumes, you can delete the `volume-family` statement.
To specify multiple custom images, you can use [Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/conditions.htm#top "The optional conditions element of a policy statement limits access based on the provided attributes in IAM.").
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartments (ABC and XYZ) to have control over the individual policy statements for their compartments, see [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM.").
Copy
```
Allow group ImageUsers to inspect instance-images in compartment ABC
Allow group ImageUsers to {INSTANCE_IMAGE_READ} in compartment ABC where target.image.id='<image_OCID>'
Allow group ImageUsers to manage instances in compartment ABC
Allow group ImageUsers to read app-catalog-listing in tenancy
Allow group ImageUsers to use volume-family in compartment ABC
Allow group ImageUsers to use virtual-network-family in compartment XYZ
```

[Let image admins manage custom images](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do everything with custom images and compute instances. Also includes the ability to do everything with Object Storage buckets, objects, and namespaces in compartment Y (for creating images from objects and creating pre-authenticated requests to images); to attach/detach any existing volumes in compartment X; and to launch instances into the cloud network and subnets in compartment Z (for creating new instances to base an image on). If the group doesn't need to attach/detach volumes, you can delete the `volume-family` statement.
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartments (X, Y, and Z) to have control over the individual policy statements for their compartments, see [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM.").
Copy
```
Allow group ImageAdmins to manage instances in compartment X
Allow group ImageAdmins to manage instance-images in compartment X
Allow group ImageAdmins to read app-catalog-listing in tenancy
Allow group ImageAdmins to manage object-family in compartment Y
Allow group ImageAdmins to use volume-family in compartment X
Allow group ImageAdmins to use virtual-network-family in compartment Z
```

[Let users manage Compute instance configurations, instance pools, and cluster networks](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with instance configurations, instance pools, and cluster networks in all compartments.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the instance configurations, instance pools, and cluster networks in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group InstancePoolAdmins to manage compute-management-family in tenancy

```

If a group needs to create instance configurations using existing instances as a template, and uses the API, SDKs, or command line interface (CLI) to do this, add the following statements to the policy:
Copy
```
Allow group InstancePoolAdmins to read instance-family in tenancy
Allow group InstancePoolAdmins to inspect volumes in tenancy
```

If a particular group needs to start, stop, or reset the instances in existing instance pools, but not create or delete instance pools, use this statement:
Copy
```
Allow group InstancePoolUsers to use instance-pools in tenancy
```

If resources used by the instance pool contain default tags, add the following statement to the policy to give the group permission to the tag namespace `Oracle-Tags`:
```
Allow group InstancePoolUsers to use tag-namespaces in tenancy where target.tag-namespace.name = 'oracle-tags'
```

If the instance configuration used by the instance pool launches instances in a capacity reservation, add the following statement to the policy:
```
Allow service compute_management to use compute-capacity-reservations in tenancy
```

If the boot volume used in the instance configuration to create an instance pool is encrypted with a KMS key then, add the following statement to the policy:
```
allow service compute, blockstorage, compute_management to use key-family in compartment <compartment_id/<tenant_id>>
```

[Let users manage Compute autoscaling configurations](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to create, update, and delete autoscaling configurations.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the autoscaling configurations in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group AutoscalingAdmins to manage auto-scaling-configurations in tenancy
Allow group AutoscalingAdmins to manage instance-pools in tenancy

```

[Let users list and subscribe to images from the Partner Image catalog](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to list and create subscriptions to images in the Partner Image catalog. It does not include the ability to create instances using images from the Partner Image catalog (see [Let users launch compute instances](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm#launch-instances)).
**Where to create the policy:** In the tenancy. To reduce the scope of access to just creating subscriptions in a particular compartment, specify that compartment instead of the tenancy in the third statement.
Copy
```
Allow group CatalogSubscribers to inspect app-catalog-listing in tenancy
Allow group CatalogSubscribers to read app-catalog-listing in tenancy
Allow group CatalogSubscribers to manage app-catalog-listing in tenancy

```

[Let users create Compute instance console connections](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to create instance console connections.
**Where to create the policy:** In the tenancy.
Copy
```
Allow group <group_name> to manage instance-console-connection in tenancy
Allow group <group_name> to read instance in tenancy
```

[Let users manage Compute dedicated virtual machine hosts](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to create, update, and delete dedicated virtual machine hosts as well as launch instances on dedicated virtual machine hosts.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the dedicated virtual machine hosts and instances in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group DedicatedVMHostAdmins to manage dedicated-vm-hosts in tenancy
Allow group DedicatedVMHostAdmins to manage instances in tenancy

```

[Let users launch Compute instances on dedicated virtual machine hosts](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to launch instances on dedicated virtual machine hosts.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the dedicated virtual machine hosts and instances in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group DedicatedVMHostAdmins to use dedicated-vm-hosts in tenancy
Allow group DedicatedVMHostAdmins to manage instances in tenancy

```

[Let volume admins manage block volumes, backups, and volume groups](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with block storage volumes, volume backups, and volume groups in all compartments with the exception of copying volume backups across regions. This makes sense if you want to have a single set of volume admins manage all the volumes, volume backups, and volume groups in all the compartments. The second statement is required in order to attach/detach the volumes from instances.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the volumes/backups and instances in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group VolumeAdmins to manage volume-family in tenancy
Allow group VolumeAdmins to use instance-family in tenancy
```

If the group needs to also copy volume backups and boot volume backups across regions, add the following statements to the policy:
```
Allow group VolumeAdmins to use volume-backups in tenancy where request.permission='VOLUME_BACKUP_COPY'
Allow group VolumeAdmins to use boot-volume-backups in tenancy where request.permission='BOOT_VOLUME_BACKUP_COPY'
```

[Let volume backup admins manage only backups](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with volume backups, but not create and manage volumes themselves. This makes sense if you want to have a single set of volume backup admins manage all the volume backups in all the compartments. The first statement gives the required access to the volume that is being backed up; the second statement enables creation of the backup (and the ability to delete backups). The third statement enables the creation and management of user defined backup policies; the fourth statement enables assignment and removal of assignment of backup policies.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the volumes and backups in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group VolumeBackupAdmins to use volumes in tenancy
Allow group VolumeBackupAdmins to manage volume-backups in tenancy
Allow group VolumeBackupAdmins to manage backup-policies in tenancy
Allow group VolumeBackupAdmins to manage backup-policy-assignments in tenancy
```

If the group will be using the Console, the following policy gives a better user experience:
Copy
```
Allow group VolumeBackupAdmins to use volumes in tenancy
Allow group VolumeBackupAdmins to manage volume-backups in tenancy
Allow group VolumeBackupAdmins to inspect volume-attachments in tenancy
Allow group VolumeBackupAdmins to inspect instances in tenancy
Allow group VolumeBackupAdmins to manage backup-policies in tenancy
Allow group VolumeBackupAdmins to manage backup-policy-assignments in tenancy
```

The last two statements are not necessary in order to manage volume backups. However, they enable the Console to display all the information about a particular volume and the available backup policies.
[Let boot volume backup admins manage only backups](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with boot volume backups, but not create and manage boot volumes themselves. This makes sense if you want to have a single set of boot volume backup admins manage all the boot volume backups in all the compartments. The first statement gives the required access to the boot volume that is being backed up; the second statement enables creation of the backup (and the ability to delete backups). The third statement enables the creation and management of user defined backup policies; the fourth statement enables assignment and removal of assignment of backup policies.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the boot volumes and backups in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group BootVolumeBackupAdmins to use volumes in tenancy
Allow group BootVolumeBackupAdmins to manage boot-volume-backups in tenancy
Allow group BootVolumeBackupAdmins to manage backup-policies in tenancy
Allow group BootVolumeBackupAdmins to manage backup-policy-assignments in tenancy
```

If the group will be using the Console, the following policy gives a better user experience:
Copy
```
Allow group BootVolumeBackupAdmins to use volumes in tenancy
Allow group BootVolumeBackupAdmins to manage boot-volume-backups in tenancy
Allow group BootVolumeBackupAdmins to inspect instances in tenancy
Allow group BootVolumeBackupAdmins to manage backup-policies in tenancy
Allow group BootVolumeBackupAdmins to manage backup-policy-assignments in tenancy
```

The last two statements aren't necessary to manage volume backups. However, they enable the Console to display all the information about a particular boot volume and the available backup policies.
[Let users create a volume group](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to create a volume group from a set of volumes.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the volumes and volume groups in a particular compartment, specify that compartment instead of the tenancy.
Copy
```
Allow group VolumeGroupCreators to inspect volumes in tenancy
Allow group VolumeGroupCreators to manage volume-groups in tenancy
```

[Let users clone a volume group](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to clone a volume group from an existing volume group.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the volumes and volume groups in a particular compartment, specify that compartment instead of the tenancy.
Copy
```
Allow group VolumeGroupCloners to inspect volumes in tenancy
Allow group VolumeGroupCloners to manage volume-groups in tenancy
Allow group VolumeGroupCloners to manage volumes in tenancy
```

[Let users create a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to create a volume group backup.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the volumes/backups and volume groups/volume group backups in a particular compartment, specify that compartment instead of the tenancy.
Copy
```
Allow group VolumeGroupBackupAdmins to inspect volume-groups in tenancy
Allow group VolumeGroupBackupAdmins to manage volumes in tenancy
Allow group VolumeGroupBackupAdmins to manage volume-group-backups in tenancy
Allow group VolumeGroupBackupAdmins to manage volume-backups in tenancy
```

[Let users restore a volume group backup](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to create a volume group by restoring a volume group backup.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the volumes/backups and volume groups/volume group backups in a particular compartment, specify that compartment instead of the tenancy.
Copy
```
Allow group VolumeGroupBackupAdmins to inspect volume-group-backups in tenancy
Allow group VolumeGroupBackupAdmins to read volume-backups in tenancy
Allow group VolumeGroupBackupAdmins to manage volume-groups in tenancy
Allow group VolumeGroupBackupAdmins to manage volumes in tenancy
```

[Let users create, manage, and delete file systems](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to create, manage, or delete a file system or file system clone. Administrative functions for a file system include the ability to rename or delete it or disconnect from it.
**Where to create the policy** : In the tenancy, so that the ability to create, manage, or delete a file system is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of these administrative functions to file systems in a particular compartment, specify that compartment instead of the tenancy.
Copy
```
Allow group StorageAdmins to manage file-family in tenancy
```

[Let users create file systems](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to create a file system or file system clone.
**Where to create the policy** : In the tenancy, so that the ability to create a file system is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of these administrative functions to file systems in a particular compartment, specify that compartment instead of the tenancy.
Copy
```
Allow group Managers to manage file-systems in tenancy
Allow group Managers to read mount-targets in tenancy
```

The second statement is required when users create a file system using the Console. It enables the Console to display a list of mount targets that the new file system can be associated with.
[Let Object Storage admins manage buckets and objects](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with Object Storage buckets and objects in all compartments. 
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the buckets and objects in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group ObjectAdmins to manage buckets in tenancy
Allow group ObjectAdmins to manage objects in tenancy
```

[Let users write objects to Object Storage buckets](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to write objects to any Object Storage bucket in compartment ABC (imagine a situation where a client needs to regularly write log files to a bucket). This consists of the ability to list the buckets in the compartment, list the objects in a bucket, and create a new object in a bucket. Although the second statement gives broad access with the `manage` verb, that access is then scoped down to only the `OBJECT_INSPECT` and `OBJECT_CREATE `permissions with the condition at the end of the statement.
**Where to create the policy** : The easiest approach is to put this policy in the tenancy. If you want the admins of compartment ABC to have control over the policy, see [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Copy
```
Allow group ObjectWriters to read buckets in compartment ABC
Allow group ObjectWriters to manage objects in compartment ABC where any {request.permission='OBJECT_CREATE', request.permission='OBJECT_INSPECT'}
```

**Access limited to a specific bucket** : To limit access to a specific bucket in a particular compartment, add the condition `where           target.bucket.name='<bucket_name>'`. The following policy allows the user to list all the buckets in a particular compartment, but they can only list the objects in and upload objects to BucketA:
Copy
```
Allow group ObjectWriters to read buckets in compartment ABC
Allow group ObjectWriters to manage objects in compartment ABC where all {target.bucket.name='BucketA', any {request.permission='OBJECT_CREATE', request.permission='OBJECT_INSPECT'}}
```

**Access limited to buckets with a specific defined tag** : To limit access to the buckets with a specific tag in a given compartment, add the condition `where           target.bucket.tag.<TagNamespace>.<TagKeyDefinition>='<_TagValue>_'`. The following policy allows the user to list all buckets in compartment ABC, however, they can only list the objects in and upload objects to the bucket with the tag`MyTagNamespace.TagKey='MyTagValue'` :
Copy
```
Allow group ObjectWriters to read buckets in compartment ABC
Allow group ObjectWriters to manage objects in compartment ABC where all {target.bucket.tag.MyTagNamespace.TagKey='MyTagValue', any {request.permission='OBJECT_CREATE', request.permission='OBJECT_INSPECT'}}
```

For more information about using conditions, see [Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/conditions.htm#top "The optional conditions element of a policy statement limits access based on the provided attributes in IAM."). 
[Let users download objects from Object Storage buckets](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to download objects from any Object Storage bucket in compartment ABC. This consists of the ability to list the buckets in the compartment, list the objects in a bucket, and read existing objects in a bucket.
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. If you want the admins of compartment ABC to have control over the policy, see [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
Copy
```
Allow group ObjectReaders to read buckets in compartment ABC
Allow group ObjectReaders to read objects in compartment ABC

```

**Access limited to a specific bucket:** To limit access to a specific bucket in a particular compartment, add the condition `where target.bucket.name='<bucket_name>'`. The following policy allows the user to list all buckets in a particular compartment, but they can only read the objects in and download from BucketA:
Copy
```
Allow group ObjectReaders to read buckets in compartment ABC
Allow group ObjectReaders to read objects in compartment ABC where target.bucket.name='BucketA'

```

**Access limited to buckets with a specific defined tag**
To limit access to the buckets with a specific tag in a given compartment, add the condition `where           target.bucket.tag.<TagNamespace>.<TagKeyDefinition>='<_TagValue>_'`. The following policy allows the user to list all buckets in compartment ABC, however, they can only read the objects in and download the objects from the bucket with the tag`MyTagNamespace.TagKey='MyTagValue'` :
Copy
```
Allow group ObjectReaders to read buckets in compartment ABC
Allow group ObjectReaders to read objects in compartment ABC where target.bucket.tag.MyTagNamespace.TagKey='MyTagValue'
```

For more information about using conditions, see [Conditions](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/conditions.htm#top "The optional conditions element of a policy statement limits access based on the provided attributes in IAM.").
[Let users have full access to a folder in an Object Storage bucket](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability of a group of users to do all actions to an Object Storage bucket and its objects.
**Where to create the policy:** In the tenancy where the users reside.
```
ALLOW group test-group TO manage objects IN TENANCY where all {target.bucket.name = 'test-bucket', target.object.name = 'prod/*'} 
```

[Let users have read-only access to a folder in an Object Storage bucket](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability of a group of users to have read-only access to an Object Storage bucket and its objects.
**Where to create the policy:** In the tenancy where the users reside.
```
ALLOW group test-group TO manage objects IN TENANCY where all {target.bucket.name = 'test-bucket', target.object.name = 'prod/*', any{request.permission='OBJECT_INSPECT', request.permission='OBJECT_READ'}}
```

[Let users have write-once access to a folder in an Object Storage bucket (no read or delete)](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability of a group of users to have write-only access to a folder of objects within a bucket Users can't view a list of objects in the bucket, nor delete any objects it contains.
**Where to create the policy:** In the tenancy where the users reside.
```
ALLOW group test-group TO manage objects IN TENANCY where all {target.bucket.name = 'test-bucket', target.object.name = 'prod/*', any{request.permission='OBJECT_CREATE'}}
```

[Let users have read-write access to a folder in an Object Storage bucket (no listing or overwriting)](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability of a group of users to have read and write access to a folder of objects within an Object Storage bucket. Users can't generate a list of objects in the folder, nor overwrite any existing objects in the folder.
**Where to create the policy:** In the tenancy where the users reside.
```
ALLOW group test-group TO manage objects IN TENANCY where all {target.bucket.name = 'test-bucket', target.object.name = 'prod/*', any{request.permission='OBJECT_CREATE', request.permission='OBJECT_READ'}}
```

[Let a user have all access to an object pattern in an Object Storage bucket ](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability of a specified user to have full access to all objects that match a specified pattern within an Object Storage bucket.
**Where to create the policy:** In the tenancy where the user resides.
```
ALLOW any-group TO manage objects IN TENANCY where all {target.bucket.name = 'test-bucket', target.object.name = '*.pdf', request.user.id='ocid1.user.oc1..exampleuniqueID'}
```

[Let database admins manage Oracle Cloud database systems](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with the following system types and their associated resources in all compartments: 
  * Exadata Database Service on Dedicated Infrastructure instances
  * bare metal DB systems
  * virtual machine DB systems


This makes sense if you want to have a single set of database admins manage all the bare metal, virtual machine, and Exadata systems in all the compartments.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the database systems in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group DatabaseAdmins to manage database-family in tenancy
```

[Let database admins manage Exadata Database Service on Cloud@Customer instances](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with the Exadata Database Service on Cloud@Customer resources in all compartments. This makes sense if you want to have a single set of database admins manage all the Exadata Database Service on Cloud@Customer systems in all the compartments.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the Exadata Database Service on Cloud@Customer
systems in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group ExaCCAdmins to manage database-family in tenancy
```

[Let database admins manage MySQL Database resources](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:**
Ability to do all things with MySQL Database and MySQL HeatWave resources in all compartments. Creating and managing MySQL Database DB Systems also requires limited access to VCNs, Subnets, and Tag namespaces in the tenancy. 
**Where to create the policy:** In the tenancy, granting access to all compartments by [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM.").
Copy
```
Allow group <group_name> to {
 	COMPARTMENT_INSPECT, 
  VCN_READ, 
  SUBNET_READ, SUBNET_ATTACH, SUBNET_DETACH, 
  NETWORK_SECURITY_GROUP_UPDATE_MEMBERS,
  VNIC_CREATE, VNIC_UPDATE, VNIC_DELETE, VNIC_ASSOCIATE_NETWORK_SECURITY_GROUP
 } in tenancy | compartment <compartment_name> | compartment <compartment_ocid>
 Allow group <group_name> to manage mysql-family in tenancy | compartment <compartment_name> | compartment <compartment_ocid>
 Allow group <group_name> to use tag-namespaces in tenancy
```

[Let database admins manage Oracle Cloud external database resources](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with the following OCI [external database](https://docs.oracle.com/iaas/external-database/index.html) resources in all compartments: 
  * OCI external container database resources
  * OCI external pluggable database resources
  * OCI external non-container database resources
  * OCI external database connectors


This makes sense if you want to have a single set of database admins manage all the OCI external database resources in all the compartments.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the OCI external database resources in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group OnPremDatabaseAdmins to manage external-database-family in tenancy
```

[Let database and fleet admins manage Autonomous Databases](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
Type of access: Ability to manage Autonomous Database resources in all compartments. Applicable if you want to have a single set of database administrators manage all the Autonomous Database resources in all the compartments.
Where to create the policy: In the tenancy, so that the access is granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the Autonomous Databases in a particular compartment, specify that compartment instead of the tenancy. 
Example 1: For [User Roles Associated with Autonomous Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/iaas/autonomous-database/doc/user-roles.html). Enables Autonomous Database fleet administrator access to the any [workload types](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm#db-admins-manage-adb__workload_types "The following table documents the strings used for policies to represent Autonomous Database workload types"), and to manage the following dedicated Exadata infrastructure resources: Autonomous Container Databases and Autonomous VM Clusters.
Copy
```
Allow group DatabaseAdmins to manage autonomous-database-family in tenancy
```

**Tip** The `autonomous-database-family` aggregate resource-type does not cover the `cloud-exadata-infrastructures` resource-type needed to provision Autonomous Database on dedicated Exadata infrastructure. See [Policy Details for Exadata Database Service on Dedicated Infrastructure](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/ecs-policy-details.html#GUID-A967AE72-E18C-40ED-A928-D865618E9B9E) for information on the permissions required to manage cloud Exadata infrastructure resources. See [Let database admins manage Oracle Cloud database systems](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm#db-admins-manage-db-systems) for a sample policy covering cloud Exadata infrastructure resources.
If you must restrict access to the Autonomous VM Cluster and Autonomous Container Database resource types (applicable only to dedicated Exadata infrastructure), then you can do so by creating separate policy statements for database administrators that allow access to only Autonomous Databases and their backups. Because a policy statement can only specify one resource type, you must create separate statements for the database and backup resources. 
Example 2: For [Autonomous Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/iaas/autonomous-database/doc/adb.html#ADBOR-GUID-D1F52093-BF6F-4324-9673-634B31665B71). Enables Autonomous Database database administrators access to databases and backups of the various workload types, but denies access to Autonomous Container Databases, Autonomous VM Clusters, and Cloud Exadata Infrastructure resources.
Copy
```
Allow group ADB-Admins to manage autonomous-database in tenancy
```

Copy
```
Allow group ADB-Admins to manage autonomous-backup in tenancy
```

To reduce the scope of access for databases and backups to either the a specific workload type, use a `where` clause.
Example 3: For [Autonomous Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/iaas/autonomous-database/doc/adb.html#ADBOR-GUID-D1F52093-BF6F-4324-9673-634B31665B71). Limits Autonomous Database access to databases and backups for a specific workload type.
Copy
```
Allow group ADB-Admins to manage autonomous-databases in tenancy where target.workloadType = ' _workload_type_'
```

Copy
```
Allow group ADB-Admins to manage autonomous-backups in tenancy where target.workloadType = ' _workload_type_'
```

In the preceding code examples, `_workload_type_`is one of the strings listed in the following table.
Autonomous Database Workload Type Strings Database Workload Type | _workload_type_ String for Policies  
---|---  
Autonomous Database for Transaction Processing and Mixed Workloads | `OLTP`  
Autonomous Database for Analytics and Data Warehousing | `DW`  
Autonomous JSON Database | `AJD`  
Oracle APEX Application Development | `APEX`  
[Let security admins manage vaults, keys, and secrets](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with the Vault service in all compartments. This makes sense if you want to have a single set of security admins manage all the vaults, keys, and secret components (including secrets, secret versions, and secret bundles) in all compartments.
**Where to create the policy:** In the tenancy, so that access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the vaults, keys, and secret components in a particular compartment, specify that compartment instead of the tenancy. To reduce the scope of access to just vaults, keys, or secret components, include only the policy statement that pertains to the respective individual or aggregate resource-type, as appropriate.
Copy
```
Allow group SecurityAdmins to manage vaults in tenancy
Allow group SecurityAdmins to manage keys in tenancy
Allow group SecurityAdmins to manage secret-family in tenancy
```

[Let security admins manage all keys in a specific vault in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with keys in a specific vault in compartment ABC.
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Attachment.htm#top "When you create an IAM policy, you must attach it to a compartment in IAM.").
Copy
```
Allow group SecurityAdmins to manage keys in compartment ABC where target.vault.id='<vault_OCID>'

```

[Let security admins use a specific key in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to list, view, and perform cryptographic operations with a specific key in a compartment.
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Attachment.htm#top "When you create an IAM policy, you must attach it to a compartment in IAM.").
Copy
```
Allow group SecurityAdmins to use keys in compartment ABC where target.key.id='<key_OCID>'

```

[Let a user group delegate key usage in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to associate an Object Storage bucket, Block Volume volume, File Storage file system, Kubernetes cluster, or Streaming stream pool with a specific key authorized for use in a specific compartment. With this policy, a user in the specified group does not have permission to use the key itself. Rather, by association, the key can be used by Object Storage, Block Volume, File Storage, Kubernetes Engine, or Streaming on behalf of the user to:
  * Create or update an encrypted bucket, volume, or file system and to encrypt or decrypt data in the bucket, volume, or file system. 
  * Create Kubernetes clusters with encrypted Kubernetes secrets at rest in the etcd key-value store.
  * Create a stream pool to encrypt data in the streams in the stream pool.


This policy requires that you also have a companion policy that lets Object Storage, Block Volume, File Storage, Kubernetes Engine, or Streaming use the key to perform cryptographic operations.
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Attachment.htm#top "When you create an IAM policy, you must attach it to a compartment in IAM.").
Copy
```
Allow group ObjectWriters, VolumeWriters, FileWriters, ClusterWriters, StreamWriters to use key-delegate in compartment ABC where target.key.id = '<key_OCID>'

```

[Let Block Volume, Object Storage, Kubernetes Engine, and Streaming services encrypt and decrypt volumes, volume backups, buckets, Kubernetes secrets, and stream pools](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to list, view, and perform cryptographic operations with all keys in compartment ABC. Because Object Storage is a regional service, it has regional endpoints. As such, you must specify the regional service name for each region where you're using Object Storage with Vault encryption. This policy also requires that you have a companion policy that allows a user group to use the delegated key that Object Storage, Block Volume, Kubernetes Engine, or Streaming will use.
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Attachment.htm#top "When you create an IAM policy, you must attach it to a compartment in IAM.").
Copy
```
Allow service blockstorage, objectstorage-<region_name>, oke, streaming to use keys in compartment ABC where target.key.id = '<key_OCID>'

```

For Object Storage, replace <region_name> with the appropriate region identifier, for example:
  * objectstorage-us-phoenix-1
  * objectstorage-us-ashburn-1
  * objectstorage-eu-frankfurt-1
  * objectstorage-uk-london-1
  * objectstorage-ap-tokyo-1


To determine the region name value of an Oracle Cloud Infrastructure region, see [Regions and Availability Domains](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm#top).
For Kubernetes Engine, the service name used in the policy is `oke`.
For Streaming, the service name used in the policy is `streaming`.
[Let File Storage encrypt and decrypt file systems](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to list, view, and perform cryptographic operations with all keys in compartment ABC. This policy also requires that you have a companion policy that allows a user group to use the delegated key that File Storage will use.
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).
  1. Create a [dynamic group](https://docs.oracle.com/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm) for the file systems with a rule such as the following:
```
ALL { resource.type='filesystem', resource.compartment.id = '<file_system_compartment_OCID>' }
```

**Note** If you have more than one rule in the dynamic group, ensure that you use `Match any rules defined below` option.
  2. Create an IAM policy that gives the dynamic group of file systems access to Vault keys:
```
allow dynamic-group <dynamic_group_name> to use keys in compartment ABC
```



[Let security admins manage all secrets in a specific vault in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with secrets in a specific vault in compartment ABC.
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. If you want the admins of the individual compartment (ABC) to have control over the individual policy statements for their compartment, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Attachment.htm#top "When you create an IAM policy, you must attach it to a compartment in IAM.").
Copy
```
Allow group SecurityAdmins to manage secret-family in compartment ABC where target.vault.id='<vault_OCID>'

```

[Let users read, update, and rotate all secrets](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to read, update, and rotate all secrets in any vault in the tenancy.
**Where to create the policy:** In the tenancy, so that access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the vaults, keys, and secrets in a particular compartment, specify that compartment instead of the tenancy.
Copy
```
Allow group SecretsUsers to use secret-family in tenancy

```

[Let group admins manage group membership](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to manage the membership of a group. Does not include the ability to create or delete users, or manage their credentials (see [Let the Help Desk manage users](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm#helpdesk-manage-users)). 
The first two statements let GroupAdmins list all the users and groups in the tenancy, list which users are in a particular group, and list what groups a particular user is in. 
The last two statements together let GroupAdmins change a group's membership. The condition at the end of the last two statements lets GroupAdmins manage membership to all groups except the Administrators group (see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The)). You should protect membership to that group because it has power to do anything throughout the tenancy.
It might seem that the last two statements should also cover the basic listing functionality that the first two statements enable. To better understand how conditions work and why you also need the first two statements, see [Variables Not Applicable to a Request Result in a Declined Request](https://docs.oracle.com/en-us/iaas/Content/Identity/policysyntax/conditions.htm#variables_that_arent_applicable_to_request_result_in_declined_request). 
**Where to create the policy:** In the tenancy, because users and groups reside in the tenancy. 
Copy
```
Allow group GroupAdmins to inspect users in tenancy
Allow group GroupAdmins to inspect groups in tenancy
Allow group GroupAdmins to use users in tenancy where target.group.name != 'Administrators'
Allow group GroupAdmins to use groups in tenancy where target.group.name != 'Administrators'

```

[Let users manage their own passwords and credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
No policy is required to let users manage _their own_ credentials. All users can change and reset their own passwords, manage their own API keys, and manage their own auth tokens. For more information, see [Working with User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/usercred/usercredentials.htm#user_credentials). 
[Let a compartment admin manage the compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to manage all aspects of a particular compartment. For example, a group called A-Admins could manage all aspects of a compartment called Project-A, including writing additional policies that affect the compartment. For more information, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Attachment.htm#top "When you create an IAM policy, you must attach it to a compartment in IAM.").
**Where to create the policy:** In the tenancy. 
Copy
```
Allow group A-Admins to manage all-resources in compartment Project-A
```

[Restrict admin access to a specific region](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to manage resources in a specific region. Remember that IAM resources must be managed in the home region. If the specified region is not the home region, then the Admin will not be able to manage IAM resources. For more information about the home region, see [Managing Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm#Managing_Regions). 
**Where to create the policy:** In the tenancy. 
Copy
```
Allow group PHX-Admins to manage all-resources in tenancy where request.region='phx'
```

The preceding policy allows PHX-Admins to manage all aspects of all resources in US West (Phoenix). 
Members of the PHX-Admins group can only manage IAM resources if the tenancy's home region is US West (Phoenix).
[Restrict user access to view only summary announcements](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to view the summary versions of announcements about the operational status of Oracle Cloud Infrastructure services.
**Where to create the policy:** In the tenancy. 
Copy
```
Allow group AnnouncementListers to inspect announcements in tenancy
```

The preceding policy allows AnnouncementListers to view a list of summary announcements.
[Let users view details of announcements](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to view the details of announcements about the operational status of Oracle Cloud Infrastructure services.
**Where to create the policy:** In the tenancy. 
Copy
```
Allow group AnnouncementReaders to read announcements in tenancy
```

The preceding policy allows AnnouncementReaders to view a list of summary announcements and the details of specific announcements.
[Let admins manage announcement subscriptions](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to manage subscriptions that deliver announcements about the operational status of Oracle Cloud Infrastructure services.
**Where to create the policy:** The easiest approach is to put this policy in the tenancy. Because of the concept of policy inheritance, the group that you grant access can then manage announcement subscriptions in any compartment. To reduce the scope of access to announcements for a particular compartment, specify the compartment instead of the tenancy.
Copy
```
Allow group AnnouncementAdmins to manage announcement-subscriptions in tenancy
```

The preceding policy allows AnnouncementAdmins to view a list of summary announcements and the details of specific announcements.
[Let streaming admins manage streaming resources](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to do all things with the Streaming service in all compartments. 
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the streams in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group StreamAdmins to manage stream-family in tenancy
```

[Let streaming users publish messages to streams](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to produce messages to streams with the Streaming service in all compartments. 
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the streams in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group StreamUsers to use stream-push in tenancy
```

[Let streaming users publish messages to a specific stream](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to produce messages to a stream with the Streaming service. 
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the streams in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group StreamUsers to use stream-push in tenancy where target.stream.id = '<stream_OCID>'
```

[Let streaming users publish messages to a stream in a specific stream pool](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to produce messages to a stream with the Streaming service. 
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the streams in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group StreamUsers to use stream-push in tenancy where target.streampool.id = '<streampool_OCID>'
```

[Let streaming users consume messages from streams](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to consume messages from streams with the Streaming service in all compartments. 
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the streams in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group StreamUsers to use stream-pull in tenancy
```

[Let users view metric definitions in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to view **metric definitions** in a specific compartment. For more information about metrics, see [Metrics Feature Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics). 
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the metric definitions in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group MetricReaders to inspect metrics in compartment ABC
```

[Let users access monitoring metrics in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to view and retrieve monitoring **metrics** for supported resources in a specific compartment. For more information about metrics, see [Metrics Feature Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics). 
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the metrics in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group MetricReaders to read metrics in compartment ABC
```

[Restrict user access to a specific metric namespace](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to view and retrieve monitoring **metrics** for resources under a specific **metric namespace**. For more information about metrics, see [Metrics Feature Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics). 
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to the specified metric namespace to just within a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group MetricReaders to read metrics in compartment ABC where target.metrics.namespace='oci_computeagent'
```

The preceding policy allows `MetricReaders` to view and retrieve metric data points from all [monitoring-enabled](https://docs.oracle.com/iaas/Content/Compute/Tasks/enablingmonitoring.htm) Compute instances in the `ABC` compartment. 
[Let users publish custom metrics](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to publish custom **metrics** under a specific **metric namespace** to the Monitoring service. For instructions, see [Publishing Custom Metrics](https://docs.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm). 
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just metrics in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group MetricPublishers to use metrics in tenancy where target.metrics.namespace='mycustomnamespace'
```

The preceding policy allows `MetricPublishers` to publish data points for the custom metric namespace `mycustomnamespace` in the tenancy. 
[Let instances make API calls to access monitoring metrics in the tenancy](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to call the Monitoring API for access to monitoring **metrics**. The instances on which API requests originate must be members of the dynamic group indicated in the policy. For more information, see [Calling Services from an Instance](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/callingservicesfrominstances.htm#Calling_Services_from_an_Instance) and [Metrics Feature Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#metrics). 
**Where to create the policy:** In the tenancy. 
Copy
```
Allow dynamic-group MetricInstances to read metrics in tenancy
```

The preceding policy allows applications that are running on Compute instances in the dynamic group `MetricInstances` to send API requests to the Monitoring service in the tenancy. 
[Let users view alarms](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to view **alarms** for supported resources in tenancy. Does not include the ability to create alarms or to create or delete topics. For more information about alarms, see [Alarms Feature Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms). 
**Where to create the policy:** In the tenancy. Because of the concept of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."), AlarmUsers can then view alarms in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group AlarmUsers to read alarms in tenancy
Allow group AlarmUsers to read metrics in tenancy

```

[Let users manage alarms](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to view and create **alarms** with existing notification topics for supported resources in the tenancy. Does not include the ability to create or delete topics. For more information about alarms, see [Alarms Feature Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms). 
All statements are required to let AlarmUsers create alarms. 
**Where to create the policy:** In the tenancy. Because of the concept of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."), AlarmUsers can then view and create alarms in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group AlarmUsers to manage alarms in tenancy
Allow group AlarmUsers to read metrics in tenancy
Allow group AlarmUsers to use ons-topics in tenancy

```

[Let users manage alarms and create topics](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to view and create **alarms** (with new or existing **topics**) for supported resources in tenancy. Also includes the ability to create **subscriptions** in the tenancy, to publish **messages** (broadcast notification messages) to all subscriptions in the tenancy, and to move alarms to different compartments in the tenancy. For more information about alarms, see [Alarms Feature Overview](https://docs.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#alarms). 
**Where to create the policy:** In the tenancy. Because of the concept of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."), AlarmUsers can then view and create alarms in any compartment. To reduce the scope of access to a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group AlarmUsers to manage alarms in tenancy
Allow group AlarmUsers to read metrics in tenancy
Allow group AlarmUsers to manage ons-topics in tenancy
```

[Let users access usage reports](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to view usage reports for your tenancy. For more information about usage reports, see [Cost and Usage Reports Overview](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm). 
**Where to create the policy:** This is a special cross-tenancy policy and must be created in the tenancy. For more information, see [Accessing Cost and Usage Reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/usagereportsoverview.htm#Accessing_Cost_and_Usage_Reports). 
Copy
```
define tenancy usage-report as ocid1.tenancy.oc1..aaaaaaaaned4fkpkisbwjlr56u7cj63lf3wffbilvqknstgtvzub7vhqkggq
				endorse group Administrators to read objects in tenancy usage-report
```

[Let users analyze costs](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to see costs for the tenancy. See [Checking Your Expenses and Usage](https://docs.oracle.com/iaas/Content/Billing/Concepts/costs.htm).
**Where to create the policy:** In the tenancy so that users in the <Example_Group> can see costs for the entire account.
Copy
```
Allow group <Example_Group> to read usage-reports in tenancy
```

[Allow a group to manage topics](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to get, create, update, and delete **topics** in the tenancy, as well as move topics to different compartments in the tenancy. Also includes the ability to create **subscriptions** in the tenancy and to publish **messages** (broadcast notification messages) to all subscriptions in the tenancy. 
**Where to create the policy:** In the tenancy. 
Copy
```
Allow group A-Admins to manage ons-topics in tenancy
```

[Allow a group to manage topic subscriptions](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to list, create, update, and delete **subscriptions** for topics in the tenancy. Ability to move subscriptions to different compartments in the tenancy. 
**Where to create the policy:** In the tenancy. 
Copy
```
Allow group A-Admins to manage ons-subscriptions in tenancy
```

[Allow a group to publish messages to topics](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to broadcast notification **messages** to all **subscriptions** in the tenancy, as well as list, create, update, and delete subscriptions in the tenancy. 
**Where to create the policy:** In the tenancy. 
Copy
```
Allow group A-Admins to use ons-topics in tenancy
```

[Let users create, deploy, and manage functions and applications using Cloud Shell](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to create, deploy, and manage OCI Functions applications and functions using Cloud Shell. These policy statements give the group access to Cloud Shell, repositories in Oracle Cloud Infrastructure Registry, logs, metrics, functions, networks, and tracing.
**Where to create the policy:** In the tenancy, so that the access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the resources in a particular compartment, you can specify the compartment instead of the tenancy for most policy statements. However, `to use cloud-shell`, `to manage repos`, and `to read objectstorage-namespaces` must always be scoped to the tenancy.
Copy
```

Allow group functions-developers to use cloud-shell in tenancy
Allow group functions-developers to manage repos in tenancy
Allow group functions-developers to read objectstorage-namespaces in tenancy
Allow group functions-developers to manage logging-family in tenancy
Allow group functions-developers to read metrics in tenancy
Allow group functions-developers to manage functions-family in tenancy
Allow group functions-developers to use virtual-network-family in tenancy
Allow group functions-developers to use apm-domains in tenancy
Allow group functions-developers to read vaults in tenancy
Allow group functions-developers to use keys in tenancy
Allow service faas to use apm-domains in tenancy
Allow service faas to read repos in tenancy where request.operation='ListContainerImageSignatures'
Allow service faas to {KEY_READ} in tenancy where request.operation='GetKeyVersion'
Allow service faas to {KEY_VERIFY} in tenancy where request.operation='Verify'

```

[Let users list Events rules in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to list Events rules. 
**Where to create the policy:** In the tenancy. 
Copy
```
Allow group RuleReaders to read cloudevents-rules in tenancy
```

The preceding policy allows RuleReaders to list rules in the tenancy. 
[Let admins manage Events rules in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to manage Events rules, including creating, deleting and updating rules. 
**Where to create the policy:** In the tenancy. 
This line gives the user inspect access to resources in compartments to select actions. 
Copy
```
allow group <RuleAdmins> to inspect compartments in tenancy
```

This line gives the user access to defined tags to apply filter tags to rules.
Copy
```
allow group <RuleAdmins> to use tag-namespaces in tenancy
```

These lines give the user access to Streaming resources for actions
Copy
```
allow group <RuleAdmins> to inspect streams in tenancy
allow group <RuleAdmins> to use stream-push in tenancy
allow group <RuleAdmins> to use stream-pull in tenancy
```

These lines give the user access to Functions resources for actions. 
Copy
```
allow group <RuleAdmins> to use virtual-network-family in tenancy
allow group <RuleAdmins> to manage function-family in tenancy
```

This line give the user access to Notifications topics for actions. 
Copy
```
allow group <RuleAdmins> to use ons-topic in tenancy
```

This line gives the user manage access to rules for Events. 
Copy
```
allow group <RuleAdmins> to manage cloudevents-rules in tenancy
```

[Allow a group to access all of Cloud Guard](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Read-only access to all of Cloud Guard. In the example policy, the group is "CloudGuard_ReadOnly."
Copy
```
allow group CloudGuard_ReadOnly to read cloud-guard-family in tenancy
allow group CloudGuard_ReadOnly to read compartments in tenancy
allow group CloudGuard_ReadOnly to read announcements in tenancy
```

[Allow a group to access Cloud Guard problems](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Read-only access to Cloud Guard problems. In the example policy, the group is "CloudGuard_ReadOnlyProblems."
Copy
```
allow group CloudGuard_ReadOnlyProblems to read cloud-guard-family in tenancy
allow group CloudGuard_ReadOnlyProblems to inspect cloud-guard-detectors in tenancy
allow group CloudGuard_ReadOnlyProblems to inspect cloud-guard-targets in tenancy
allow group CloudGuard_ReadOnlyProblems to inspect cloud-guard-resource-types in tenancy
allow group CloudGuard_ReadOnlyProblems to read announcements in tenancy
allow group CloudGuard_ReadOnlyProblems to read compartments in tenancy
allow group CloudGuard_ReadOnlyProblems to read cloud-guard-config in tenancy
```

[Allow a group to access Cloud Guard detector recipes](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Read-only access to Cloud Guard detector recipes. In the example policy, the group is "CloudGuard_ReadOnlyDetectors."
Copy
```
allow group CloudGuard_ReadOnlyDetectors to read cloud-guard-detector-recipes in tenancy
allow group CloudGuard_ReadOnlyDetectors to read announcements in tenancy
allow group CloudGuard_ReadOnlyDetectors to read compartments in tenancy
allow group CloudGuard_ReadOnlyDetectors to read cloud-guard-config in tenancy
```

[Allow a group to access Cloud Guard in a single compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Read-only access to Cloud Guard in a single compartment. In the example policy, the group is "CloudGuard_ReadOnly_SingleCompartment" and the compartment name is "cgDemo_RestrictedAccess."
Copy
```
allow group CloudGuard_ReadOnly_SingleCompartment to read compartments in tenancy where target.compartment.name = 'cgDemo_RestrictedAccess'
allow group CloudGuard_ReadOnly_SingleCompartment to read cloud-guard-family in compartment cgDemo_RestrictedAccess
allow group CloudGuard_ReadOnly_SingleCompartment to read announcements in compartment cgDemo_RestrictedAccess
allow group CloudGuard_ReadOnly_SingleCompartment to read cloud-guard-config in tenancy
```

[Let security admins manage all bastions and sessions](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to manage all resources in the Bastion service in all compartments. This makes sense if you want to have a single set of security admins manage all **bastions** and **sessions** in all compartments.
**Where to create the policy:** In the tenancy, so that access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the bastions and bastion sessions in a particular compartment, specify that compartment instead of the tenancy.
Copy
```
Allow group SecurityAdmins to manage bastion in tenancy
Allow group SecurityAdmins to manage bastion-session in tenancy
Allow group SecurityAdmins to manage virtual-network-family in tenancy
Allow group SecurityAdmins to read instance-family in tenancy
Allow group SecurityAdmins to read instance-agent-plugins in tenancy
Allow group SecurityAdmins to inspect work-requests in tenancy
```

[Let security admins manage bastion sessions](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to manage all **sessions** on all **bastions** and in all compartments, including creating, connecting to, and terminating sessions.
**Where to create the policy:** In the tenancy, so that access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM."). To reduce the scope of access to just the bastion sessions in a particular compartment, specify that compartment instead of the tenancy. 
Copy
```
Allow group SecurityAdmins to use bastion in tenancy
Allow group SecurityAdmins to manage bastion-session in tenancy
Allow group SecurityAdmins to manage virtual-network-family in tenancy
Allow group SecurityAdmins to read instance-family in tenancy
Allow group SecurityAdmins to read instance-agent-plugins in tenancy
Allow group SecurityAdmins to inspect work-requests in tenancy
```

[Let security admins manage bastion sessions for a specific target host in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to manage **sessions** on a **bastion** in a specific compartment, and only for sessions that provide connectivity to a specific Compute instance.
**Where to create the policy:** In the tenancy, so that access is easily granted to all compartments by way of [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM.").
Copy
```
Allow group SecurityAdmins to use bastion in compartment ABC
Allow group SecurityAdmins to manage bastion-session in compartment ABC where ALL {target.resource.ocid='<instance_OCID>', target.bastion-session.username='<session_username>'}
Allow group SecurityAdmins to manage virtual-network-family in tenancy
Allow group SecurityAdmins to read instance-family in tenancy
Allow group SecurityAdmins to read instance-agent-plugins in tenancy
Allow group SecurityAdmins to inspect work-requests in tenancy
```

[Allow a group to manage connectors](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to list, create, update, and delete **connectors** in the tenancy. Ability to move connectors to different compartments in the tenancy.
**Where to create the policy:** In the tenancy.
Copy
```
Allow group A-Admins to manage serviceconnectors in tenancy
```

[Allow a group to call Ops Insights ingest operations at tenancy](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
**Type of access:** Ability to call [Ops Insights](https://docs.oracle.com/iaas/operations-insights/home.htm) ingest operations at the tenancy level only.
**Where to create the policy:** In the tenancy.
Copy
```
allow group opsi-users to use opsi-database-insights in tenancy 
where any 
{request.operation='IngestSqlBucket', 
request.operation='IngestSqlText',
request.operation='IngestSqlPlanLines'}
```

[Let users create and delete workspaces without networking (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
Ability to create, delete, and modify workspaces within a compartment.
Copy
```
allow group <group-name> to manage dis-workspaces in <compartment-name>
allow group <group-name> to manage dis-work-requests in <compartment-name>
allow group <group-name> to manage tag-namespaces in <compartment-name>
```

[Let users create and delete workspaces with networking (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
Ability to create, delete, and modify workspaces within a virtual network.
Copy
```
allow service dataintegration to use virtual-network-family in <compartment-name>
allow group <group-name> to manage dis-workspaces in <compartment-name>
allow group <group-name> to manage dis-work-requests in <compartment-name>
allow group <group-name> to use virtual-network-family in <compartment-name>
allow group <group-name> to manage tag-namespaces in <compartment-name>
```

[Let users and resource principal access and use Object Storage for a given workspace (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
Ability to create and use Object Storage data assets within all workspaces.
Copy
```
allow any-group to use buckets in <compartment-name> where ALL {request.principal.type='disworkspace'}
allow any-group to manage objects in <compartment-name> where ALL {request.principal.type='disworkspace'}
allow group <group-name> to use object-family in <compartment-name>
```

To give access to an individual workspace, specify the OCID for the workspace where you want to allow access. For example:
Copy
```
allow any-group to use buckets in <compartment-name> where ALL {request.principal.type='disworkspace', request.principal.id='<workspace-ocid>'}
allow any-group to manage objects in <compartment-name> where ALL {request.principal.type='disworkspace', request.principal.id='<workspace-ocid>'}
```

[Let users and resource principal access and use autonomous databases as a target for a specific workspace (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
Ability to create and use autonomous database data assets within all workspaces.
Copy
```
allow any-group to use buckets in <compartment-name> where ALL {request.principal.type='disworkspace'}
allow any-group to manage objects in <compartment-name> where ALL {request.principal.type='disworkspace'}
allow group <group-name> to use object-family in <compartment-name>
allow any-group to manage buckets in <compartment-name> where ALL {request.principal.type='disworkspace', request.permission='PAR_MANAGE'}
```

To give access to an individual workspace, specify the OCID for the workspace where you want to allow access. For example:
Copy
```
allow any-group to use buckets in <compartment-name> where ALL {request.principal.type='disworkspace', request.principal.id='<workspace-ocid>'}
allow any-group to manage objects in <compartment-name> where ALL {request.principal.type='disworkspace', request.principal.id='<workspace-ocid>'}
allow any-group to manage buckets in <compartment-name> where ALL {request.principal.type='disworkspace', request.principal.id='<workspace-ocid>', request.permission='PAR_MANAGE'}
```

[Let users search objects within a workspace (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
Ability to search the components of Data Integration in a given workspace.
This policy must be applied at the tenancy (root compartment) level. 
Copy
```
allow service dataintegration to {TENANCY_INSPECT} in tenancy
allow service dataintegration to {DIS_METADATA_INSPECT} in tenancy
```

[Let users move workspaces to a new compartment (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
Ability to move workspaces to a new compartment.
Copy
```
allow service dataintegration to inspect compartments in <compartment-name>
allow group <group-name> to manage dis-workspaces in <compartment-name>
```

[Let users publish tasks to the OCI Data Flow service (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
Ability to publish the different tasks within all workspaces to the OCI Data Flow service.
Copy
```
allow any-group to manage dataflow-application in <compartment-name> where ALL {request.principal.type='disworkspace'}
```

To give access to an individual workspace, specify the OCID for the workspace where you want to allow access. For example:
Copy
```
allow any-group to manage dataflow-application in <compartment-name> where ALL {request.principal.type='disworkspace', request.principal.id='<workspace-ocid>'}
```

[Let users access the OCI Vault service for a specific workspace (Data Integration)](https://docs.oracle.com/en-us/iaas/Content/Identity/policiescommon/commonpolicies.htm)
Ability to use OCI Vault secrets within all workspaces.
Copy
```
allow any-group to read secret-bundles in <compartment-name> where ALL {request.principal.type='disworkspace'}
allow group <group-name> to read secret-bundles in <compartment-name>
```

To give access to an individual workspace, specify the OCID for the workspace. For example:
Copy
```
allow any-group to read secret-bundles in <compartment-name> where ALL {request.principal.type='disworkspace', request.principal.id='<workspace-ocid>'}
```

Was this article helpful?
YesNo

