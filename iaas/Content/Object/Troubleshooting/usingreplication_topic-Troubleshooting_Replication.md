Updated 2024-04-13
# Troubleshooting Object Storage Replication
Learn troubleshooting solutions for issues you might encounter using replication.
## Unable to create a replication policy on the source bucket 🔗 
Here are the common causes for replication policy creation failures:
  * The destination bucket cannot have versioning enabled.
  * The destination bucket cannot have retention rules.
  * Your IAM permissions are missing or incomplete. Policy creation requires:
    * User permissions that let you access both the source and destination buckets and let you manage the objects in those buckets.
    * Service permissions that authorize Object Storage itself to access both the source and destination bucket and their objects.
Review the existing policies that grant user and service permissions. For more information, see [Required IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication.htm#permissions).


## Policy is in error on the source bucket 🔗 
If the policy status changes from active to error, check these items:
  * You intentionally or unintentionally stopped replication on the destination bucket. To once again replicate to this target bucket, delete the existing policy on the source bucket and create a new policy.
  * Ensure that your user permissions are still in place.
  * Ensure that the policies that authorize Object Storage access to the source and destination buckets and their objects are still in place.
  * You might have exceeded your storage limits on the destination bucket. If you are a Free Trial or Always Free customer, your storage is limited. Upgrade to paid account or delete your replication policy.


## Unable to stop replication on the destination bucket and make the bucket writable 🔗 
If stopping a replication policy fails, the most likely cause is missing or incomplete IAM permissions. Policy creation requires the following:
  * User permissions that let you access both the source and destination buckets and let you manage the objects in those buckets. 
  * Service permissions that authorize Object Storage itself to access both the source and destination bucket and their objects.


Review the existing policies that grant user and service permissions. For more information, see [Required IAM Policies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication.htm#permissions).
Was this article helpful?
YesNo

