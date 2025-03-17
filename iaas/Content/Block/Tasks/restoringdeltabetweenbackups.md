Updated 2024-10-15
# Direct APIs for Changed Block Tracking Between Two Backups
Block Volume direct APIs enable changed block tracking between two backups.
Data protection services vendors and developers of backup/restore solutions can use this interface to identify the blocks that changed between two backups and get the delta data between backups directly to analyze and optimize their backup workflows. By leveraging changed block tracking, they don't need to restore two full volumes from two backups to compare and process them, enabling more efficient backup processes.
The process is similar to creating a new volume by restoring a backup, however in this case, the newly created volume contains only the differences between the two backups. 
For a complete list of restrictions and caveats, see [Limitations and Considerations](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringdeltabetweenbackups.htm#limitations). 
**Important** We recommend that you delete the volumes that contain the changed blocks as soon as you have completed using the changed blocks. You shouldn't use these volumes for any purposes other than retrieving the changed blocks. These volumes aren't usable as file systems.
## Limitations and Considerations 🔗 
  * This feature is supported for block volume backups and boot volume backups.
  * For volume group backups, you can retrieve the changed blocks for individual volume backups from the volume group backup.
  * We recommend that you delete the volumes that contain the changed blocks as soon as you're done processing the changed blocks.
  * You can't use the restored volume in the same way as a regular volume, for example, it doesn't have any kind of usable file system, nor can you create and mount a file system to it. 
  * Both backups must be of the same volume.
  * The first backup can be a full backup or an incremental backup. The second backup must be an incremental backup. If both backups are incremental, there must not have been a full backup taken between the two incremental backups.
  * The volume must not have been resized between the backups.
  * Recommended scan length is up to 1 GB worth of logical blocks. Scan length greater than 1 GB isn't supported and the output is undefined. If the scan length is specified as 0, or not specified at all, then scan length is considered as the entire volume which is subject to the same limitation of 1 GB.
  * The volume created to retrieve the changed blocks doesn't support the **Lower Cost** performance level.
  * With regards to cost, the volume created to retrieve the changed blocks will be the same size as the original source volume for the backups, so it's charged as such.
  * By default, the block size for block volumes is 4 KB. If you're exporting the volume to a backup format with a larger block size, you can use the `changeBlockSizeInBytes` parameter when restoring the volume to specify a larger block size for the external backup format.


## Using Changed Block Tracking 🔗 
Working with Direct APIs to retrieve the changed blocks between two backups has the following steps:
  1. [Create a volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringdeltabetweenbackups.htm#restoringdeltabetweenbackups_creatingchangedblockvolume) that contains the changed blocks by providing the first and second backup OCIDs as the source.
  2. [Attach and connect](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringdeltabetweenbackups.htm#restoringdeltabetweenbackups_attachingchangedblocksvolume) the volume to a Linux-based instance using an iSCSI attachment. Paravirtualized attachments aren't supported. Attachments to Windows-based instances aren't supported.
  3. [Scan the attached volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringdeltabetweenbackups.htm#scsi-get-lba-status) for changed blocks using `SCSI GET LBA STATUS` commands and retrieve the changed blocks reported by `SCSI GET LBA STATUS`.
  4. [Delete the volume](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringdeltabetweenbackups.htm#restoringdeltabetweenbackups_deletingchangedblocksvolume) after you finish processing the volume. You need to disconnect and detach the volume from the instance first. 


### Step 1: Create the Volume Containing the Changed Blocks 🔗 
You can use the [CLI](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringdeltabetweenbackups.htm#cli) or [API](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/restoringdeltabetweenbackups.htm#usingapi) to create the volume containing the changed blocks between two backups. You provide the OCIDs for the first backup and second backup as the source for the volume.
You can identity a volume that has been created this way from two backups by checking the **Volume type** field in the **Source details** section in the Console, see [Getting a Block Volume's Details](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/get-bv-volume.htm#top "View a block volume's details."). The value specified in this field for these volumes is **volumeBackupDelta**. 
#### Using the CLI 🔗 
For block volumes, use the `create-volume-volume-source-from-volume-backup-delta-details` command and required parameters to create a block volume:
Command
CopyTry It
```
oci bv volume create-volume-volume-source-from-volume-backup-delta-details --availability-domain <AD> --source-details-first-backup-id <first_backup_ID> --source-details-second-backup-id <second_backup_ID> --source-details-change-block-size-in-bytes <change_block_size> [OPTIONS] 
```

For boot volumes, use the `create-boot-volume-boot-volume-source-from-boot-volume-backup-delta-details` command and required parameters to create a block volume:
Command
CopyTry It
```
oci bv boot-volume create-boot-volume-boot-volume-source-from-boot-volume-backup-delta-details --availability-domain <AD> --source-details-first-backup-id <first_backup_ID> --source-details-second-backup-id <second_backup_ID> --source-details-change-block-size-in-bytes <change_block_size> [OPTIONS] 
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
#### Using the API 🔗 
##### CreateVolume API 🔗 
Use the [CreateVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Volume/CreateVolume) operation and specify `VolumeSourceFromVolumeBackupDeltaDetails` for [CreateVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateVolumeDetails).
This operation has the following parameters:
  * **firstBackupId** : The OCID for the first backup to compare. This backup must be older than the second backup.
  * **secondBackupId** : The OCID for the backup to compare to the first backup. This backup must be newer than the first backup.
  * **changeBlockSizeInBytes** : (Optional) By default, the block size for volumes is 4 KB. If you're exporting the restored volume to a backup format with a larger block size, use this parameter to specify a larger block size to match the larger block size of the external backup format. From 4096 to 1048576, in powers of two. Default is 4096.
  * **type** : `volumeBackupDelta`.


##### CreateBootVolume API 🔗 
Use the [CreateBootVolume](https://docs.oracle.com/iaas/api/#/en/iaas/latest/BootVolume/CreateBootVolume) operation and specify `BootVolumeSourceFromBootVolumeBackupDeltaDetails` for [CreateBootVolumeDetails](https://docs.oracle.com/iaas/api/#/en/iaas/latest/datatypes/CreateBootVolumeDetails).
This operation has the following parameters:
  * **firstBackupId** : The OCID for the first backup to compare. This backup must be older than the second backup.
  * **secondBackupId** : The OCID for the backup to compare to the first backup. This backup must be newer than the first backup.
  * **changeBlockSizeInBytes** : (Optional) By default, the block size for volumes is 4 KB. If you're exporting the restored volume to a backup format with a larger block size, use this parameter to specify a larger block size to match the larger block size of the external backup format. From 4096 to 1048576, in powers of two. Default is 4096.
  * **type** : `bootVolumeBackupDelta`.


#### Response Codes 🔗 
Response Code |  Description  
---|---  
`200 OK` | The request was successfully completed.   
`400 Bad Request` | Depending on the message returned, this code is returned in the following scenarios:
  * The OCID specified for `firstBackupId` or `secondBackupId` is invalid or the format is incorrect.
  * The same OCID is specified for both `firstBackupId` and `secondBackupId`.
  * The backup specified in `firstBackupId` was taken later than the backup specified in `secondBackupId`.
  * The value specified for `volumeBackupDelta` is invalid or not in the correct format.

  
`403 Forbidden` | This code is returned if:
  * The backups specified in `firstBackupId` and `secondBackupId` aren't from the same volume.
  * The volume was resized between the backups specified in `firstBackupId` and `secondBackupId`.

  
`404 Not Found` | Depending on the message returned, this code is returned in the following scenarios:
  * The backup restore delta feature isn't enabled for the tenancy.
  * The specified backup doesn't exist.
  * The **Lower Cost** performance level was specified, this level isn't supported when creating a volume using the backup restore delta feature. 

  
`409 Conflict` | This code is returned if the lifecycle state for either of the backups isn't **Available**.  
`500 Internal Server Error` | The server encountered an unexpected condition that prevented it from fulfilling the request.  
#### Audit Logs 🔗 
Audit logs are generated for all create volume operations. You can find details about the first and second backups used as the source for a volume containing the changed blocks between two backups. The details are in the `sourceDetails` element in the log data, as shown in the following example: 
```
 "sourceDetails": {
      "changeBlockSizeInBytes": 1048576,
      "firstBackupId": "ocid1.volumebackup.oc1.eu-paris-1.<first_backup_unique_ID>",
      "secondBackupId": "ocid1.volumebackup.oc1.eu-paris-1.<second_backup_unique_ID>",
      "type": "volumeBackupDelta"
     },

```

The `type` attribute for these volumes is `volumeBackupDelta`.
For more information, see [Overview of Audit](https://docs.oracle.com/iaas/Content/Audit/Concepts/auditoverview.htm) and [Viewing Audit Log Events](https://docs.oracle.com/iaas/Content/Audit/Tasks/viewinglogevents.htm).
### Step 2: Attach and Connect the Volume Containing the Changed Blocks 🔗 
After the volume is created, before you can start scanning the volume, you need to attach it to Linux-based instance using an iSCSI attachment. Paravirtualized attachments and attachments to Windows-based instances aren't supported.
See the following topics for more information about these tasks:
  * [Attaching a Block Volume to an Instance](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/attachingavolume.htm#top "Attach a block volume to a compute instance to expand the available storage on the instance.")
  * [iSCSI Commands and Information](https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/iscsiinformation.htm#iSCSI_Commands_and_Information)
  * [Connecting to iSCSI-Attached Block Volumes](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/connectingtoavolume_topic-Connecting_to_iSCSIAttached_Volumes.htm#top "Connect to an iSCSI-attached block volume.")


### Step 3: Scan the Volume for Changed Blocks with SCSI Get LBA Status 🔗 
After you have attached and connected the volume to a Linux-based instance, you can scan the attached volume for changed blocks using `SCSI GET LBA STATUS` commands, and then retrieve the changed blocks reported by the commands.
#### Using SCSI GET LBA STATUS
You can send `SCSI GET LBA STATUS` commands to both boot volumes and block volumes to find and get the changed blocks on the volume for the specified starting logical block address (LBA) and the length to scan to identify the changed blocks (scan length). The time it takes to return provisioning status of the blocks on a device depends on the scan length provided in the command, and the performance level configured for the volume. 
You can build and install `sg3_utils` from [sg3_utils-1.48](https://www.linuxfromscratch.org/blfs/view/svn/general/sg3_utils.html). See also [Manpage](https://manpages.ubuntu.com/manpages/focal/en/man8/sg_get_lba_status.8.html).
#### Limitations and Considerations for Using LBA Status
  * The 32-byte command for Linux is the only supported version. The 16-byte command for Linux isn't supported.
  * No commands are supported for Windows.
  * Only iSCSI-attached volumes are supported.
  * Recommended scan length is up to 1 GB worth of logical blocks. See the example in the next section for scan length (`-s`) usage. Scan length greater than 1 GB isn't supported and the output is undefined. If the scan length is specified as 0 or omitted, the behavior is undefined. 
  * The default allocation length is 24 bytes, for 1 descriptor only.
  * If report type is 0 (all), provisioning statuses for uninitialized blocks are also included in the result as deallocated blocks leading to is no distinction between uninitialized and explicitly deallocated blocks.


#### Example
The details in this section provide an example of running the commands on a Linux instance to get the changed blocks.
To only get provisioning status about mapped and deallocated blocks, and not uninitialized blocks, use report type `1` to specify a non-zero provisioning status.
For example:```
sudo sg_get_lba_status -b -T -l 96 -m 32768 -s 2097152 -t 1 /dev/sdc
```

In the preceding example, the logical block size is 512 bytes and the block device is `/dev/sdc`. This example uses the 32-byte command (`-T`) and scans 1 GB (or 2097152 contiguous logical blocks), starting from `lba 96` with an allocation length of 32768 bytes. The specified report type is `1`. Specifying the `-b` option prints the output in brief. 
#### Understanding Output
The following is example output from the running the previous command example:
```
Completion condition=3
RTP=1
0x0000000000000060 0x10 3 0
0x0000000000000070 0x8 1 0
0x0000000000000078 0x10 3 0
0x0000000000000088 0x8 1 0
0x0000000000000090 0x10 3 0
0x00000000000000a0 0xfff60 1 0
```

The preceding output contains six descriptors, each with a starting lba, count, and provisioning status of that many contiguous blocks. 
For example, the first descriptor's starting lba is 96, count is 16, and provisioning status is 3, which means blocks from 96 to 112 are mapped. 
`RTP=1` means the report type sent in the command was considered in processing of the Get Lba Status command.
The four completion condition types in the example output are:
  * Completion condition = 0: the device server didn't return any output.
  * Completion condition = 1: the device server stopped processing as the allocation length was met, and the next command should use starting lba after the last lba in the output. 
  * Completion condition = 2: the device server scanned the entire scan length and returned the output. Therefore, the next command can use starting lba after the scan length sent before.
  * Completion condition = 3: the device server reached the end of the volume, and no more commands should be sent after the last lba in the output.


### Step 4: Delete the Volume Containing the Changed Blocks 🔗 
You shouldn't use volumes containing the changed blocks between two backups for any purposes other than retrieving the changed blocks, so we recommend that you delete these volumes as soon as you have completed using the changed blocks.
You first need to [disconnect](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/disconnectingfromavolume.htm#Disconnecting_From_a_Volume) the volume from the instance, and then [detach](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/detachingavolume.htm#Detaching_a_Volume "Detach a block volume from an instance.") it from the instance. After the volume is detached, you can then [delete](https://docs.oracle.com/en-us/iaas/Content/Block/Tasks/deletingavolume.htm#Deleting_a_Volume "Delete a block volume from the Block Volume service when it's no longer needed.") the volume.
Was this article helpful?
YesNo

