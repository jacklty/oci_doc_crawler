Updated 2025-01-22
# Listing Object Storage Objects in a Bucket
View a list of the objects in an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_list_objects_in_a_bucket.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
The **Objects** list opens. All objects in the selected bucket are displayed in a table.
  * Use the [oci os object list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list.html) command and required parameters to list the objects in a bucket:
Command
CopyTry It
```
oci os object list --bucket-name bucket_name [OPTIONS]
```

By default, a minimal number of fields are returned for each object. For example:
```
oci os object list --bucket-name MyBucket
{
 "data": [
  {
   "etag": "7588e71f-433f-4518-ba2d-90082208bd5d",
   "md5": "As+3syaEbvMhPm8fM+DSAw==",
   "name": "eventslogreference.htm",
   "size": 13515,
   "storage-tier": "InfrequentAccess",
   "time-created": "2021-01-11T15:47:44.427000+00:00",
   "time-modified": "2021-01-11T15:47:44.441000+00:00"
  },
  {
   "etag": "833c7099-f74e-4ce5-a7c8-ffa29a112d88",
   "md5": "JI9YzxOg5HsbPSANkTVy8g==",
   "name": "flowlogreference.htm",
   "size": 16601,
   "storage-tier": "Archive",
   "time-created": "2021-01-11T15:47:44.617000+00:00",
   "time-modified": "2021-01-11T15:47:44.638000+00:00"
  },
  {
   "etag": "3b833478-87c5-49f1-8bb4-f33b66c2758a",
   "md5": "skstBGw3YcHBomI6X/YwEA==",
   "name": "objectstoragelogreference.htm",
   "size": 18631,
   "storage-tier": "Standard",
   "time-created": "2021-01-11T20:50:48.996000+00:00",
   "time-modified": "2021-01-11T20:50:49.019000+00:00"
  }
 ],
 "prefixes": []
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListObjects](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjects) operation to list the objects in a bucket.
Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```
/n/object_storage_namespace/b/bucket/o/object_name
```

The object name is everything after the `/o/`, which could include hierarchy levels and prefix strings. 


Was this article helpful?
YesNo

