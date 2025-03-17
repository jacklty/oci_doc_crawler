Updated 2025-01-22
# Managing Auto-Tiering for an Object Storage Bucket
Enable or disable auto-tiering for any Standard storage-tier Object Storage bucket.
You can enable auto-tiering during the creation of a bucket. See [Creating an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#top "Create a Object Storage bucket to store objects.") for more information. 
You can enable or disable auto-tiering for an existing bucket using the instructions in this topic.
For more information on this feature, see [Auto-Tiering](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#auto_tiering).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_auto_tiering.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_auto_tiering.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_auto_tiering.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, find **Auto-Tiering** and select **Edit**.
    3. Select (to enable) or clear (to disable) the **Enable Auto-Tiering** check box.
    4. Select **Save Changes**.
  * Use the [oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command and required parameters to enable auto-tiering a bucket.
Command
CopyTry It
```
oci os bucket update --name bucket_name --auto-tiering InfrequentAccess [OPTIONS]
```

Include the `auto-tiering` parameter and the `InfrequentAccess` value to enable the feature.
For example:```
oci os bucket update --name MyStandardBucket --auto-tiering InfrequentAccess
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": "InfrequentAccess",
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  "defined-tags": {},
  "etag": "7b7c3dc1-713f-4996-b176-a938345cae8e",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "kms-key-id": null,
  "metadata": {},
  "name": "MyStandardBucket",
  "namespace": "MyNamespace",
  "object-events-enabled": false,
  "object-level-audit-mode": "Disabled",
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess",
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-12T19:04:05.879000+00:00",
  "versioning": "Disabled"
 },
 "etag": "7b7c3dc1-713f-4996-b176-a938345cae8e"
}
```

You can also disable auto-tiering at any time using the update action. Include the `auto-tiering` parameter and the `Disabled` value to disable the feature. For example:
Command
CopyTry It
```
oci os bucket update --name bucket_name --auto-tiering Disabled [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * This task can't be performed using the API.


Was this article helpful?
YesNo

