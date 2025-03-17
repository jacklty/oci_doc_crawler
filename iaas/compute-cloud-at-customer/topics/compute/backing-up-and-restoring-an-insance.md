Updated 2024-10-07
# Backing Up and Restoring an Instance
On Compute Cloud@Customer, supports backing up and restoring instances. The instance backup is created in an Object Storage bucket. From there, you can copy it to another server in your data center for safekeeping. When needed, you can import the backup into any Compute Cloud@Customer Object Storage bucket, and use it to create instances.
**Use Cases**
  * Back up instances and any attached block volumes.
  * Store the backups on another server for safekeeping.
  * Restore a faulty instance and any attached block volumes.
  * Use the backup to create matching instances.
  * Use the backup and restore feature to migrate instances to another tenancy, or to another Compute Cloud@Customer.


The restored instance has some of the same characteristics as the source instance. For example:
  * The type and version of the OS.
  * The OS configuration matches the OS configuration of the source instance. This includes things like OS user accounts, installed applications, and so on.
  * The type of storage, high-performance or balanced-performance, matches the source instance.
  * All the software on the block volumes is available after you attached the block volumes to the restored instance. 


Some aspects of the restored instance differ from the source instance, such as:
  * The restored instance and associated components, like boot and block volumes have unique OCIDs that don't match the source instance.
  * The source instance user account SSH keys aren't included in the restored instance. 
  * While creating the restored instance, you can configure the instance in a different compartment, with a different name, shape, subnet, and all the other attributes that you configure during the launch.


## Task Map - Backing Up an Instance 🔗 
No. | Task | Links  
---|---|---  
1. |  Ensure that you have an Object Storage bucket in the same tenancy where the instance is located. | 
  * [Listing Buckets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-buckets.htm#listing-buckets "On Oracle Compute Cloud@Customer, you can list buckets.")
  * [Creating a Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-bucket.htm#creating-a-bucket "On Compute Cloud@Customer, you can create Object Storage buckets.")

  
2. |  Create the instance backup. |  [Creating an Instance Backup](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/creating-an-instance-backup.htm#creating-an-instance-backup "On Compute Cloud@Customer, you can use the Compute Cloud@Customer Console and API to back up an instance.")  
3. |  Transfer the backup object from Object Storage to another system in your data center. |  [Transferring an Instance Backup to Another System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/transferring-an-intance-backup.htm#transferring-an-instance-backup-to-another-system)  
## Task Map – Restoring an Instance From a Backup 🔗 
The following tasks assume that you are restoring an instance from a backup that's on another system in your data center. If the backup is already on the Compute Cloud@Customer where you plan to restore the instance, start with task number 3.
No. | Task | Links  
---|---|---  
1. |  Ensure that you have an Object Storage bucket in the same tenancy where you plan to restore the instance. | 
  * [Listing Buckets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-buckets.htm#listing-buckets "On Oracle Compute Cloud@Customer, you can list buckets.")
  * [Creating a Bucket](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-bucket.htm#creating-a-bucket "On Compute Cloud@Customer, you can create Object Storage buckets.")

  
2. |  Upload the backup to the bucket. |  [Transferring an Instance Backup from Another System to Compute Cloud@Customer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/transferring-an-intance-backup.htm#transferring-an-instance-backup-from-another-system)  
3. | Identify the backup OCID. | [Listing Instance Backups](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/listing-instance-backups.htm#listing-instance-backups "On Compute Cloud@Customer, you can list instance backups using the Compute Cloud@Customer Console and API.")  
4. |  Import the backup from the bucket into the Compute Cloud@Customer. |  [Importing an Instance Backup](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/restoring-an-instance-from-an-instance-backup.htm#importing-an-instance-backup "On Compute Cloud@Customer, importing an instance backup copies the backup from an Object Storage backup to a location that's internal.")  
5. |  Finish restoring the instance by creating an instance using the imported instance backup. |  [Finishing the Instance Restore](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/compute/restoring-an-instance-from-an-instance-backup.htm#finishing-the-instance-restore "On Compute Cloud@Customer, you can create new instances from instance backups.")  
Was this article helpful?
YesNo

