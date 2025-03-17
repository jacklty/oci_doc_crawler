Updated 2023-08-15
# Managing Volume Groups
On Compute Cloud@Customer, the Block Volume service enables you to organize multiple volumes into a volume group. A volume group can include both block and boot volumes.
You can use volume groups to create volume group backups and clones that are point-in-time and crash-consistent. This simplifies the process to create time-consistent backups of running enterprise applications that span multiple storage volumes across multiple instances. You can then restore an entire group of volumes from a volume group backup.
Similarly, you can also clone an entire volume group in a time-consistent and crash-consistent manner. A deep disk-to-disk and fully isolated clone of a volume group, with all the volumes associated in it, becomes available for use within a matter of seconds. This speeds up the process of creating new environments for development, quality assurance, user acceptance testing, and troubleshooting.
When working with volume groups and volume group backups, keep the following in mind:
  * You can only add a volume to a volume group when the volume status is Available. 
  * A volume group can include up to 32 volumes, up to a maximum size of 128 TB. For example, if you wanted to add 32 volumes of equal size to a volume group, the maximum size for each volume would be 4 TB. You could add volumes that vary in size, however the overall combined size of all the block and boot volumes in the volume group cannot be more than 128 TB. Ensure you account for the size of any boot volumes in your volume group when considering volume group size limits.
  * A volume can only be in one volume group.
  * When you clone a volume group, a new group with new volumes is created. For example, if you clone a volume group containing three volumes, once this operation is complete, you will now have two separate volume groups and six different volumes with nothing shared between the volume groups. 
  * When you update a volume group using the CLI, SDKs, or REST APIs, specify all the volumes to include in the volume group. The list of volumes to include replaces the existing list. If you do not include a volume OCID in the updated list, that volume will be removed from the volume group. 
  * When you delete a volume group, the individual volumes in the group are not deleted.
  * When you delete a volume that is part of a volume group, you must first remove the volume from the volume group and then delete the volume. 
  * When you delete a volume group backup, all the volume backups in the volume group backup are deleted.


Was this article helpful?
YesNo

