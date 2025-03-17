Updated 2025-01-22
# Updating the Object Storage Object's Storage Tier
Update the storage tier for an object in that reside in the Standard and Infrequent Access tiers in an Object Storage bucket.
You can update the storage tier for objects that reside in the Standard and Infrequent Access tiers, but not the Archive tier. If you update the storage tier of an object to Archive, you can't change it back to a different tier. To update the storage tier of an object, you need OBJECT_UPDATE_TIER permissions.
**Important**
Objects in the Archive and Infrequent Access tiers have a minimum storage retention period and data retrieval fees. For more information, see [Understanding Storage Tiers](https://docs.oracle.com/iaas/Content/Object/Concepts/understandingstoragetiers.htm#understanding_object_storage_tiers).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_update_the_storage_tier_of_an_object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_update_the_storage_tier_of_an_object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_update_the_storage_tier_of_an_object.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. From the **Actions** menu for the object you want, select **Update Storage Tier**.
    4. Select an option under **Storage Tier** :
       * **Standard Tier**
       * **Infrequent Access**
       * **Archive**
See [Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#storage-tiers "Learn how Object Storage uses storage tiers to help you maximize access performance where appropriate and minimize storage costs where possible.") for descriptions of the storage tier types.
    5. Select **Save Changes**.
  * Use the [oci os object update-storage-tier](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/update-storage-tier.html) command and required parameters to change the storage tier for an object in a bucket:
Command
CopyTry It
```
oci os object update-storage-tier --bucket-name bucket_name --name object_name --storage-tier [Archive | InfrequentAccess | Standard] [OPTIONS]
```

For example:
```
oci os object update-storage-tier --bucket-name MyStandardBucket --name MyFile.txt --storage-tier Archive

```

To view an object's storage tier, see [Getting an Object's Details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_get_object_details.htm#top "View the details for an object in an Object Storage bucket.").
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateObjectStorageTier](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/UpdateObjectStorageTier) operation to change the storage tier for an object in a bucket.
Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```
/n/object_storage_namespace/b/bucket/o/object_name
```

The object name is everything after the `/o/`, which could include hierarchy levels and prefix strings. 


Was this article helpful?
YesNo

