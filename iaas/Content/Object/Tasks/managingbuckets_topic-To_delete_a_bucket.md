Updated 2025-01-30
# Deleting an Object Storage Bucket
Delete an Object Storage bucket.
The Console collects and provides a count of each resource that would prevent bucket deletion. Upon confirmation, the resources are deleted and the bucket is deleted in a single action. If you're deleting a bucket that contains one or more of these resources, consider using the Console to accomplish this task rather than one of the other methods.
**Caution**
You can't recover a deleted bucket. You can cancel a deletion in progress. However, resources deleted before the cancellation can’t be recovered. You can't delete a bucket that contains any of the following resources:
  * Objects and object versions
  * Pre-authenticated requests
  * Replication policy
  * Uncommitted multi-part uploads


  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_delete_a_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_delete_a_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_delete_a_bucket.htm)


  *     1. On the **Buckets** list page, find the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. From the **Actions** menu for the bucket you want, select **Delete**.
    3. When prompted, confirm the deletion.
  * Use the [oci os bucket delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/delete.html) command and required parameters to delete a bucket:
Command
CopyTry It
```
oci os bucket delete --name bucket_name [OPTIONS]
```

For example:
```
oci os bucket delete --name MyDeletedBucket
Are you sure you want to delete this resource? [y/N]:
```

Select `y` and press `Enter`. The bucket is deleted with no further prompting.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/DeleteBucket) operation to delete bucket.
When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```
n/object_storage_namespace/b/bucket
```



Was this article helpful?
YesNo

