Updated 2025-01-22
# Getting an Object Storage Bucket's Details
View the details of an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_view_bucket_details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_view_bucket_details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_view_bucket_details.htm)


  * On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
The details page shows the following details about the bucket:
    * **Visibility** : Displays whether the bucket is a private or public bucket. See [Changing an Object Storage Bucket's Visibility](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm#top "Change the public or private visibility of an Object Storage bucket.").
    * **Namespace** : The namespace to which the bucket belongs.
    * **Default Storage Tier** : The type of storage tier such as Standard or Archive.
    * **Auto-Tiering** : Displays whether auto-tiering is enabled or disabled. See [Managing Auto-Tiering for an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_auto_tiering.htm#top "Enable or disable auto-tiering for any Standard storage-tier Object Storage bucket.").
    * **Approximate Count** : Approximate number of objects in the bucket.
    * **ETag** : The entity tag (ETag) for the bucket.
    * **OCID** : The Oracle Cloud ID for the bucket.
    * **Encryption Key** : The master encryption key name assigned to the bucket.
    * **Created** : The timestamp of bucket creation.
    * **Compartment** : The compartment to which the bucket belongs.
    * **Approximate Size** : Approximate total size of all the objects.
    * **Emit Object Events** : Displays whether the option to emit objects events is enabled or disabled. See [Managing Emitting Events for Object State Changes in an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_emitting_events_for_object_state_changes.htm#top "Enable or disable whether events are emitted for object state changes in an Object Storage bucket.").
    * **Object Versioning** : Displays whether object versioning is enabled or disabled. See [Managing Object Versioning in an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_suspend_object_versioning.htm#top "Enable or suspend object versioning on an Object Storage bucket.").
    * **Replication** : Displays whether replication policy is enabled. See [Replication Policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm#replication).
    * **Virtual Folders** : Allows you to view the objects in a folder structure. If you want a flat view of the objects, you can disable this option.
    * **Uncommitted Multipart Uploads Approximate Count** : The approximate number of objects with uncommitted or failed multipart uploads.
    * **Uncommitted Multipart Uploads Approximate Size** : The total approximate size of the uncommitted multipart uploads in the bucket. If this size exceeds the threshold, a warning icon is displayed.
  * Use the [oci os bucket get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/get.html) command and required parameters to get the details of a bucket:
Command
CopyTry It
```
oci os bucket get --name bucket_name [OPTIONS]
```

For example:```
oci os bucket get --name MyBucket
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  "defined-tags": {},
  "etag": "7b7c3dc1-713f-4996-b176-a938345cae8e",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "kms-key-id": null,
  "metadata": {},
  "name": "MyBucket",
  "namespace": "MyNamespace",
  "object-events-enabled": false,					
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess",
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-22T19:04:05.879000+00:00",
  "versioning": "Disabled"
 },
 "etag": "7b7c3dc1-713f-4996-b176-a938345cae8e"
}
```

#### Viewing Bucket Size and Number of Objects in the Bucket 🔗 
Use the `fields` parameter and its supported values to get information on the count and size of objects contained in a bucket.
    * `approximateCount` is the approximate number of objects in the bucket. Count statistics are reported periodically. You might see a lag between what is displayed and the actual object count.
    * `approximateSize` is the approximate total size of all objects in the bucket. Size statistics are reported periodically. You might see a lag between what is displayed and the actual size of the bucket.
For example:
Command
CopyTry It
```
oci os bucket get --name bucket_name --fields approximateCount --fields approximateSize [OPTIONS]
```

For example:```
oci os bucket get --name MyBucket --fields approximateCount --fields approximateSize
{
 "data": {
  **"approximate-count": 25**,
  **"approximate-size": 8075918**,
  "auto-tiering": null,
  "compartment-id": "ocid1.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1:user:oc1:phx:1458751937789:exampleuniqueID",
  "defined-tags": {},
  "etag": "218f201f-28a4-434d-9591-f05b6223c67a",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "kms-key-id": null,
  "metadata": {},
  "name": "MyBucket",
  "namespace": "MyNamespace",
  "object-events-enabled": false,
  "object-level-audit-mode": "Disabled",
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess",
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2017-10-19T04:11:32.040000+00:00",
  "versioning": "Disabled"
 },
 "etag": "218f201f-28a4-434d-9591-f05b6223c67a"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/GetBucket) operation to get the details of a bucket.
When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```
n/object_storage_namespace/b/bucket
```



Was this article helpful?
YesNo

