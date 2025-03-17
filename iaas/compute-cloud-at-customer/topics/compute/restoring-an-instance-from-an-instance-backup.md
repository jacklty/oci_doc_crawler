Updated 2024-10-07
# Restoring an Instance from an Instance Backup
On Compute Cloud@Customer, you restore an instance by importing the instance backup from an Object Storage bucket. Next, create the instance using the boot volume from the backup as the image source. Then attach any block volumes that were included in the backup.
## Importing an Instance Backup 🔗 
On Compute Cloud@Customer, importing an instance backup copies the backup from an Object Storage backup to a location that's internal.
For a particular instance backup, you can only have one imported copy. If you need to import the same instance backup again, you must first delete the original instance backup. See [Deleting an Instance Backup](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/deleting-an-instance-backup.htm#deleting-an-instance-backup "On Compute Cloud@Customer, you can use the DELETE API to delete exported and imported instance backups.").
**Prerequisites**
  * You must have an instance backup in an Object Storage bucket. 
If needed, transfer the backup to Compute Cloud@Customer. See [Transferring an Instance Backup from Another System to Compute Cloud@Customer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/transferring-an-intance-backup.htm#transferring-an-instance-backup-from-another-system).


## Finishing the Instance Restore 🔗 
On Compute Cloud@Customer, you can create new instances from instance backups.
Perform the following steps to create as many instances as you like from the instance backup.
  1. Create an instance by following the instructions in [Creating an Instance](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance.htm#creating-an-instance "On Compute Cloud@Customer, you can create an instance using the Compute Cloud@Customer Console, CLI, and API.")). While doing so, perform these actions:
     * For the source image, specify a backup boot volume instead of an image. Then select an imported instance.
     * If the instance requires access using SSH, ensure that you include an SSH public key.
  2. (Optional) Attach any block volumes that were included in the instance backup.
See [Attaching a Volume](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/block/attaching-a-volume.htm#attaching-a-volume "You attach a volume to a Compute Cloud@Customer instance to expand the available storage on the instance.").


Was this article helpful?
YesNo

