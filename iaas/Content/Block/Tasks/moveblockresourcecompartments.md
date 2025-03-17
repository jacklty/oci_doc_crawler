Updated 2024-06-04
# Move Block Volume Resources Between Compartments
You can move Block Volume resources such as block volumes, boot volumes, volume backups, volume groups, and volume group backups from one compartment to another. When you move a Block Volume resource to a new compartment, associated resources are not moved. After you move the resource to the new compartment, inherent policies apply immediately and affect access to the resource through the Console. For more information, see [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm).
**Important** When moving Block Volume resources between compartments you need to ensure that the resource users have sufficient access permissions on the compartment the resource is being moved to.
## Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, you must be granted security access in a **policy** by an administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with your administrator what type of access you have and which **compartment** to work in.
For administrators: The following policies allow users to move Block Volume resources to a different compartment:
Copy
```
Allow group BlockCompartmentMovers to manage volume-family in tenancy
```

If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/policygetstarted.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm).
## Security Zones 🔗 
[Security Zones](https://docs.oracle.com/iaas/security-zone/home.htm) ensure that your cloud resources comply with Oracle security principles. If any operation on a resource in a security zone compartment violates a [policy for that security zone](https://docs.oracle.com/iaas/security-zone/using/security-zone-policies.htm), then the operation is denied.
The following security zone policies affect your ability to move Block Volume resources from one compartment to another:
  * You can't move a block volume or boot volume from a security zone to a compartment that is not in the security zone.
  * You can't move a block volume or boot volume to a compartment that is in a security zone if the volume violates any security zone policies.


## Using the Console 🔗 
[To move a block volume to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. 
  2. In the **Scope** section, select a compartment. 
  3. Find the block volume in the list, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**.
  4. Choose the destination compartment from the list. 
  5. Click **Move Resource**.


[To move a block volume backup to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Backups**. 
  2. In the **Scope** section, select a compartment. 
  3. Find the block volume backup in the list, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**.
  4. Choose the destination compartment from the list. 
  5. Click **Move Resource**.


[To move a volume group to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Groups**.
  2. In the **Scope** section, select a compartment. 
  3. Find the volume group in the list, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**.
  4. Choose the destination compartment from the list. 
  5. Click **Move Resource**.


[To move a volume group backup to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Volume Group Backups**.
  2. In the **Scope** section, select a compartment. 
  3. Find the volume group backup in the list, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**.
  4. Choose the destination compartment from the list. 
  5. Click **Move Resource**.


[To move a boot volume to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volumes**. In the **Block Storage** menu on the sidebar, click **Boot Volumes**.
  2. In the **Scope** section, select a compartment. 
  3. Find the boot volume in the list, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**.
  4. Choose the destination compartment from the list. 
  5. Click **Move Resource**.


[To move a boot volume backup to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Backups**.
  2. In the **Scope** section, select a compartment. 
  3. Find the boot volume backup in the list, click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then click **Move Resource**.
  4. Choose the destination compartment from the list. 
  5. Click **Move Resource**.


## Using the CLI 🔗 
For information about using the CLI, see [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm).
[To move a block volume to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume change-volume-compartment --volume-id <volume_OCID> --compartment-id <destination_compartment_OCID>
```

[To move a block volume backup to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-backup change-volume-backup-compartment --volume-backup-id <volume_backup_OCID> --compartment-id <destination_compartment_OCID>
```

[To move a volume group to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group change-volume-group-compartment --volume-group-id <volume_group_OCID> --compartment-id <destination_compartment_OCID>
```

[To move a volume group backup to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv volume-group-backup change-volume-group-backup-compartment --volume-group-backup-id <volume_group_backup_OCID> --compartment-id <destination_compartment_OCID>
```

[To move a boot volume to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume change-boot-volume-compartment --boot-volume-id <boot_volume_OCID> --compartment-id <destination_compartment_OCID>
```

[To move a boot volume backup to a new compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/moveblockresourcecompartments.htm)
Open a command prompt and run:
Command
CopyTry It
```
oci bv boot-volume-backup change-boot-volume-backup-compartment --boot-volume-backup-id <boot_volume_backup_OCID> --compartment-id <destination_compartment_OCID>
```

## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following operations for moving Block Volume resources between compartments:
  * [ChangeVolumeCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/ChangeVolumeCompartment)
  * [ChangeVolumeBackupCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeBackup/ChangeVolumeBackupCompartment)
  * [ChangeVolumeGroupCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroup/ChangeVolumeGroupCompartment)
  * [ChangeVolumeGroupBackupCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeGroupBackup/ChangeVolumeGroupBackupCompartment)
  * [ChangeBootVolumeCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/ChangeBootVolumeCompartment)
  * [ChangeBootVolumeBackupCompartment](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolumeBackup/ChangeBootVolumeBackupCompartment)


Was this article helpful?
YesNo

