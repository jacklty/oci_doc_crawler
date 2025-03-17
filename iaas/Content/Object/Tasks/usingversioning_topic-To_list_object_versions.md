Updated 2025-01-22
# Listing Object Versions in an Object Storage Bucket
View a list the versions of an object in an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_list_object_versions.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. Select the down arrow (**Show Object Versions**) next to the object entry.
The list of versions of the object appears. The latest version appears at the top of the list. The version ID appears and you can copy it your clipboard by selecting **Copy**.
  * Use the [oci os object list-object-versions](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list-object-versions.html) command and required parameters to list all the objects and their versions in a bucket:
Command
CopyTry It
```

oci os object list-object-versions --bucket-name bucket_name
```

For example:
```

oci os object list-object-versions MyStandardBucket
{
 "data": {
  "items": [
   {
    "etag": null,
    "is-delete-marker": false,
    "md5": null,
    "name": "MyTextDocument.txt",
    "size": null,
    "time-created": null,
    "time-modified": "2020-04-14T22:18:08.777000+00:00",
    "version-id": "2d528a44-5b15-40dc-b303-20993d1ade66"
   },
   {
    "etag": null,
    "is-delete-marker": false,
    "md5": null,
    "name": "MyTextDocument.txt",
    "size": null,
    "time-created": null,
    "time-modified": "2020-04-14T22:17:10.371000+00:00",
    "version-id": "a175ddc0-cc86-425f-bc2e-9b9bcb9bff92"
   },
   {
    "etag": null,
    "is-delete-marker": false,
    "md5": null,
    "name": "MyTextDocument.txt",
    "size": null,
    "time-created": null,
    "time-modified": "2020-04-14T22:14:47.675000+00:00",
    "version-id": "8d8f06ef-e0c2-4435-bea6-f7c3ec80a444"
   }
  ],
  "prefixes": null
 }
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListObjectVersions](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjectVersions) operation to list all the objects and their versions in a bucket.


Was this article helpful?
YesNo

