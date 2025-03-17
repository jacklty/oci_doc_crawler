Updated 2024-04-13
# Troubleshooting Object Storage Object Versioning
Learn troubleshooting solutions for issues you might encounter using object versioning.
## Unable to Enable Versioning 🔗 
If enabling versioning fails, the most likely cause is missing or incomplete IAM permissions. Enabling versioning requires the following:
  * User permissions that let you use the bucket and manage the objects in that bucket. 
  * Minimally, BUCKET_UPDATE permissions. 


Review the existing policies that grant user permissions. For more information, see [Required IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm#Permissions).
## Unable to Delete a Bucket 🔗 
If deleting a bucket fails, the most likely cause is that the bucket is not empty. 
**Caution**
You can't recover a deleted bucket. You can cancel a deletion in progress. However, resources deleted before the cancellation can’t be recovered. You can't delete a bucket that contains any of the following resources:
  * Objects and object versions
  * Pre-authenticated requests
  * Replication policy
  * Uncommitted multi-part uploads


**Tip** When you delete an object in a version-enabled bucket, a previous version of that object is created. Select **Show Deleted Objects** to display the object versions that might prevent you from deleting the bucket.
## Unable to Delete a Previous Object Version 🔗 
If deleting a previous object version fails, the most likely cause is missing or incomplete IAM permissions. Object version deletion requires the following:
  * User permissions that let you use the bucket and manage the objects in that bucket. 
  * Minimally, OBJECT_VERSION_DELETE permissions. 


Was this article helpful?
YesNo

