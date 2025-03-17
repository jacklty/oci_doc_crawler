Updated 2025-01-22
# Deleting an Object Storage Object 
Delete one or more objects from an Object Storage bucket
You can permanently delete an object from a bucket or folder. You can't, however, recover a deleted object unless you have object versioning enabled. See [Object Storage Versioning](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm#object-versioning "Learn how to use object versioning to apply data protection against the accidental or malicious object updating or deleting of Object Storage objects.") for details.
**Note** You can't delete an object that has an active [retention rule](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules.htm#data-retention-rules "Learn how to use retention rules to preserve Object Storage data.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. From the **Actions** menu for the object you want, select **Delete**. 
To delete several objects, select the check boxes next to the object names and select **Delete** from the **More Actions** menu.
    4. When prompted, confirm the deletion.
  * Use the [oci os object delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/delete.html) command and required parameters to delete an object from a bucket:
Command
CopyTry It
```
oci os object delete --bucket-name bucket_name --name object_name [OPTIONS]
```

For example:
```
oci os object delete --bucket-name MyBucket --name MyFile.txt
Are you sure you want to delete this resource? [y/N]: y
```

The object is deleted with no further information returned.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/DeleteObject) operation to delete an object from a bucket.
Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API: 
```
/n/object_storage_namespace/b/bucket/o/object_name
```

The object name is everything after the `/o/`, which could include hierarchy levels and prefix strings.


Was this article helpful?
YesNo

