Updated 2024-10-15
# Managing Vault Encryption Keys for Block Volume
Customer-managed keys are keys that are managed and made available using the Oracle Cloud Infrastructure Vault.
By default block volumes are encrypted using Oracle-managed keys. You have the option to use your own keys, managed by Vault. You can specify a customer-managed key when you create a volume, see [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#top "Create a block volume in the Block Volume service."). The volume's backups automatically use the specified key. You can specify a different key when you create a new volume by cloning a volume or restoring a volume from a volume backup.
## Specifying a New Key When Restoring a Backup 🔗 
  * When using the CLI, run the following command:
Command
CopyTry It
```
oci bv create --display-name <volume_name> --compartment-id <compartment_ID> --availability-domain <AD> --kms-key-id <different_key_ID>
    --volume-backup-id=<source_backup_ID>
```

If you don't include the `--kms-key-id` attribute, the volume created from restoring a backup uses the Oracle managed key.
  * When you [restore the block volume from a backup](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringavolumefromabackup.htm#Restoring_a_Backup_to_a_New_Volume) in the Console, in the **Encryption** section on the **Restore block volume** form, select **Encrypt using customer-managed keys** , and then select the Vault encryption key you want to use. 
  * When using the API, specify the encryption key OCID in the `kmsKeyId` attribute of [CreateVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateVolumeDetails) when calling the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) operation.


## Specifying a New Key When Cloning a Volume 🔗 
  * When using the CLI, run the following command:
Command
CopyTry It
```
oci bv create --display-name <volume_name> --compartment-id <compartment_ID> --availability-domain <AD> --kms-key-id <different_key_ID>
--source-volume-id=<source_volume_ID>
```

  * When you [clone a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/cloningavolume.htm#Cloning_a_Volume "Create a clone from a volume by using the Block Volume service. Cloning lets you to make a copy of an existing block volume without needing to go through the backup and restore process.") in the Console, in the **Encryption** section on the **Create clone** form, select **Encrypt using customer-managed keys** , and then select the Vault encryption key you want to use. 
  * When using the API, specify the encryption key OCID in the `kmsKeyId` attribute of [CreateVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateVolumeDetails) when calling the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) operation.


## Specifying a New Key When Activating a Replica 🔗 
  * When using the CLI, run the following command:
Command
CopyTry It
```
oci bv create --display-name <volume_name> --compartment-id <compartment_ID> --availability-domain <AD> --kms-key-id <different_key_ID>
--source-volume-replica-id=<source_replica_ID>
```

  * When you [activate volume replica](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#activateblockreplica) in the Console, in the **Encryption** section on the **Activate a volume replica** form, select **Encrypt using customer-managed keys** , and then select the Vault encryption key you want to use. 
  * When using the API, specify the encryption key OCID in the `kmsKeyId` attribute of [CreateVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/requests/CreateVolumeDetails) when calling the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) operation.


## Specifying a Key When Enabling Replication 🔗 
You can optionally specify your own key to encrypt the volume replica in the destination region. The customer-managed key can either be:
  * a replicated key that exists in the destination region.
  * any key in target region that you own and is different than the one in the source region.


You can encrypt the volume replica with a customer-managed encryption key in the destination region when you enable replication for a volume or volume group. When you enable replication, select **Encrypt using customer-managed keys** for **Cross region replication encryption** , and then specify the OCID for a valid encryption key in the region you selected to replicate the volume or volume group to. If you don't specify a customer-managed key, an Oracle-managed encryption key is used instead.
See the following: 
  * [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys)
  * [Creating a Block Volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/creatingavolume.htm#top "Create a block volume in the Block Volume service.")
  * [Creating a Volume Group](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/create-volume-group.htm#top "Create a volume group in the Block Volume service.")
  * [Block Volume Replicas](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#Using_the_Console_Block_Replicas)
  * [Boot Volume Replicas](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumereplication.htm#Using_the_Console_Boot_Replicas)
  * [Volume Group Replication](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/volumegroupreplication.htm#volumegroupreplication "You can use the Block Volume service's replication feature for volume groups.")


## Rotating the Encryption Key 🔗 
Rotating the same key isn't supported today and the behavior isn't defined when you have multiple versions of a key. Block Volume only supports keys with a single version. To rotate an encryption key, change the volume's encryption key to a new key. You can also change the encryption key for a volume backup.
When you rotate the key for a volume by specifying a new encryption key, any child resources created before updating the key continue to use the old encryption key. This includes backups and clones. 
## Changing the Encryption Key for a Volume 🔗 
You can change the key assigned to a volume to another customer-managed key. Changing the encryption key doesn't re-encrypt the content of the volume, only the data key is re-encrypted.
  * To specify a different customer-managed key for a volume using the CLI, run the following command:
Command
CopyTry It
```
oci bv volume-kms-key update --volume-id=<volume_ID> --kms-key-id=<key_ID>
```

  * To specify a different customer-managed key for a volume using the Console, see [Update a Key to a Block Volume](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys_topic-To_assign_a_key_to_an_existing_Block_Volume.htm). 
  * To specify a different customer-managed key with the API, use the [UpdateVolumeKmsKey](https://docs.oracle.com/iaas/api/#/en/iaas/latest/VolumeKmsKey/UpdateVolumeKmsKey) operation.


## Changing the Encryption Key for a Volume Backup 🔗 
You can change the key assigned to a volume backup to another customer-managed key or to an Oracle managed key. Changing the encryption key doesn't re-encrypt the volume backup, only the data key is re-encrypted. For how to change the encryption key for a backup using the CLI, Console, or API, see [Volume Backup Encryption Keys](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#updatebackupkey).
## Cross Security Compartment Key Access
As a best practice, CIS Oracle Cloud Infrastructure Foundations Benchmark recommends that you create a vault for your customer-managed keys in a separate compartment and restrict access to this compartment. The following diagram shows how to organize this.
![Architecture diagram showing customer managed keys stored in a separate, restricted access compartment](https://docs.oracle.com/en-us/iaas/Content/Block/Images/block_single_tenant_best_practice.png)
The following policies are required to use the keys in a separate security compartment with restricted access to encrypt boot volumes, block volumes, and related resources.
```
Allow service blockstorage to use keys in compartment security-compartment where target.key.id = <key_ID>
Allow group projx-admin-group to use key-delegate in compartment security-compartment where target.key.id = <key_ID>
```

## Volume Backup Encryption Keys 🔗 
The Oracle Cloud Infrastructure Vault service enables you to bring and manage your own keys to use for encrypting volumes and their backups. When you create a volume backup, the encryption key used for the volume is also used for the volume backup.
You can change the key assigned to a volume backup to another customer-managed key or to an Oracle-managed key. Changing the encryption key doesn't re-encrypt the content of the volume, it just re-encrypts the data key. 
### Using the CLI 🔗 
To specify a different key for a volume backup using the CLI, run the following command:
Command
CopyTry It
```
oci bv backup update --backup-id=<backup_ID> --kms-key-id=<key_ID>
```

To specify that the volume backup use an Oracle-managed key, specify an empty string for the key ID, as shown in the following example: 
Command
CopyTry It
```
oci bv backup update --backup-id=<backup_ID> --kms-key-id=''
```

### Using the Console 🔗 
  1. Open the navigation menu and click **Storage**. Under **Block Storage** , click **Block Volume Backups**.
  2. Under **List Scope** , in the **Compartment** list, select the compartment that contains the volume backup that you want to update the key for.
  3. From the list of volume backups, click the backup you're interested in.
  4. Then, do one of the following:
     * If the volume backup already has a key assigned to it, next to **Encryption Key** , click **Edit** to assign a different key.
     * If the volume backup doesn't already have a key assigned to it, next to **Encryption Key** , click **Assign**.
  5. Select the vault compartment, vault, key compartment, and key.
  6. When you're finished, click **Assign** or **Update** , as appropriate.


### Using the API 🔗 
To specify a different customer-managed key with the API, use the `UpdateVolumeBackup` operation, and specify the encryption key OCID in the `kmsKeyId` attribute.
### Specifying a Key for Cross-Region Backup Copies 🔗 
When you [manually copy a volume backup between regions](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingvolumebackupcrossregion.htm#Copying_a_Volume_Backup_Between_Regions) you can use the Oracle-managed key or your own encryption key. When you assign a backup policy with [cross-region backup copies enabled](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#CrossRegionCopy) to a volume or volume group, or [perform a manual backup cross region copy](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/copyingvolumebackupcrossregion.htm#Copying_a_Volume_Backup_Between_Regions), you can optionally select **Encrypt using customer-managed keys** for **Cross region backup copy encryption** to encrypt the volume backup in the destination region. If you select this option, you must specify the OCID for a valid encryption key in the destination region. See also [Requirements for Customer-Managed Encryption Keys for Cross-Region Operations](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/managingblockencryptionkeys.htm#blockvolumeencryption_crossregionkeys).
### More Resources 🔗 
  * [Block Volume Encryption](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumeencryption.htm)
  * [Overview of Block Volume Backups](https://docs.oracle.com/iaas/Content/Block/Concepts/blockvolumebackups.htm)


## **Requirements for Customer-Managed Encryption Keys for Cross-Region Operations** 🔗 
When you specifying a customer-managed encryption key for cross-region operations, ensure the following:
  * The OCID is a valid OCID for the encryption key, in a format similar to the following:```
ocid1.key.oc1.iad-ad-1.<unique_ID>
```

  * The OCID is for an encryption key that exists in the destination region for the cross-region operation.
  * You have the required permissions configured in the destination region to use encryption keys with Block Volume. For more information, see the following:
    * [Assigning Master Encryption Keys - Required IAM Policy](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/assigningkeys.htm#permissions)
    * [Create a policy to enable encryption keys](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#services-use-key)
    * [Let a user group delegate key usage in a compartment](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm#os-bv-admins-use-key-id)


If you don't specify a customer-managed encryption key for cross-region operations, an Oracle-managed encryption is used by default. These requirements don't apply to Oracle-managed encryption keys.
Was this article helpful?
YesNo

