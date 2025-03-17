Updated 2025-03-04
# Managing Emitting Events for Object State Changes in an Object Storage Bucket
Enable or disable whether events are emitted for object state changes in an Object Storage bucket.
You can create automation based on state changes for Oracle Cloud Infrastructure resources by using event types, rules, and actions. For more information, see [Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_emitting_events_for_object_state_changes.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_emitting_events_for_object_state_changes.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_enable_or_disable_emitting_events_for_object_state_changes.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, find **Emit Object Events** and select **Edit**.
    3. Select (to enable) or clear (to disable) **Emit Object Events**.
    4. Select **Save Changes**.
  * Use the [oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command and required parameters to enable or disable emitting events for a bucket.
Command
CopyTry It
```
oci os bucket update --name bucket_name --object-events-enabled [true | false] [OPTIONS]
```

Include the `object-events-enabled` parameter and indicate `true` for enabled, and `false` for disabled.
For example:
```

oci os bucket update --name MyBucket --object-events-enabled true
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid1.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1:user:oc1:phx:1458751937789:exampleuniqueID",
  "defined-tags": {
   "operations": {
    "costcenter": "42"
   }
  },
  "etag": "39d1db02-27d0-4263-b3ff-5e6450495457",
  "freeform-tags": {
   "Chicago_Team": "marketing_videos"
  },
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "kms-key-id": null,
  "metadata": {
   "department": "Finance"
  },
  "name": "MyBucket",
  "namespace": "MyNamespace",
  "object-events-enabled": true,
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess",
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-22T19:04:05.879000+00:00",
  "versioning": "Disabled"
 },
 "etag": "39d1db02-27d0-4263-b3ff-5e6450495457"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * This task can't be performed using the API.


Was this article helpful?
YesNo

