Updated 2025-01-22
# Deleting an Object Storage Object Version
Delete an object's version from an Object Storage bucket.
Deleting an object's version is permanent. You can't recover a deleted version. See [Object Version Deletion](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm#Understa) for more information.
See [Listing Object Versions in a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm#top "View a list the versions of an object in an Object Storage bucket.") for information on getting an object version's ID.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_delete_an_object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_delete_an_object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_delete_an_object.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. Select the down arrow (**Show Object Versions**) next to the object entry you want.
The list of versions of the object appears. The latest version appears at the top of the list.
    4. From the **Actions** menu for the object you want, select **Delete**.
    5. When prompted, confirm the deletion.
The version you deleted no longer appears in the object's list of versions.
  * Use the [oci os object delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/delete.html) command and required parameters as described in [Deleting an Object](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_delete_objects_from_a_bucket.htm#top "Delete one or more objects from an Object Storage bucket"). Include the `version-id` parameter and version ID:
Command
CopyTry It
```
oci os object delete --bucket-name bucket_name --name object_name --version-id version_id [OPTIONS]
```

For example:
```
oci os object delete --bucket-name MyStandardBucket --name MyTextDocument.txt delete --version-id 8d8f06ef-e0c2-4435-bea6-f7c3ec80a444 
Are you sure you want to delete this resource? [y/N]: y
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/DeleteObject) operation to delete an object from a bucket. Include the `versionId` attribute and the version ID.
Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API: 
```
/n/object_storage_namespace/b/bucket/o/object_name
```

The object name is everything after the `/o/`, which could include hierarchy levels and prefix strings.


Was this article helpful?
YesNo

