Updated 2023-10-19
# Troubleshooting Versioning
Identify and address common issues that can occur while working with object versioning on Compute Cloud@Customer.
## Unable to Enable Versioning 🔗 
If enabling versioning fails, the most likely cause is missing or incomplete IAM permissions. Enabling versioning requires:
  * User permissions that let you use the bucket and manage the objects in that bucket. 
  * BUCKET_UPDATE permissions.


## Unable to Delete a Bucket 🔗 
If deleting a bucket fails, the most likely cause is that the bucket is not empty. 
You can permanently delete an empty bucket. You can't delete a bucket that contains any of the following:
  * Any objects
  * Previous versions of an object
  * A multipart upload in progress
  * A preauthenticated request


**Tip**
When you delete an object in a version-enabled bucket, a previous version of that object is created. Select Show Deleted Objects to display the object versions that might prevent you from deleting the bucket.
## Unable to Delete a Previous Version 🔗 
If deleting a previous object version fails, the most likely cause is missing or incomplete IAM permissions. Object version deletion requires:
  * User permissions that let you use the bucket and manage the objects in that bucket. 
  * At minimum, OBJECT_VERSION_DELETE permissions.


Was this article helpful?
YesNo

