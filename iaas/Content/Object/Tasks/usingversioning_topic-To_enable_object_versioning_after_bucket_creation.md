Updated 2025-01-22
# Managing Object Versioning for an Object Storage Bucket
Enable or suspend object versioning on an Object Storage bucket.
By default, object versioning isn't enabled when you create a bucket. You can enable object versioning on an existing bucket. You can also suspend object versioning on a bucket where the feature is enabled. Versioning can't be disabled after it is enabled on a bucket. Versioning can only be suspended.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_object_versioning_after_bucket_creation.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_object_versioning_after_bucket_creation.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_object_versioning_after_bucket_creation.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, find **Object Versioning** under **Features**. 
If object versioning is listed as **Enabled** , no further action is required. If object versioning is listed as **Disabled** or **Suspended** , select **Edit**.
    3. Select **Enable Versioning**.
Object version is now enabled on the bucket. All later objects uploaded to the bucket are versioned.
  * Use the [oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command and required parameters to enable or suspend object versioning in a bucket. Include the `versioning` parameter and a value of either `Enabled` or `Suspended`:
Command
CopyTry It
```
oci os bucket update --name bucket_name --versioning [Enabled | Suspended] [OPTIONS]
```

For example:
```
oci os bucket update --name MyBucket --versioning Enabled
{ "data": {
  "approximate-count": null,
  "approximate-size": null,
  "compartment-id": "ocid1.compartment.oc1..aaaaaaaamnk2ilreg5fkgu7rarfbbhdv3a5ji4eixxgkl4uprbqk6aefv5sq",
  "created-by": "ocid1.user.oc1..aaaaaaaah46lg3ueuftovn3urjgstlg4laxnre3djelu5jxy5uaqhgy7acgq",
  "defined-tags": {
   "Financials": {
    "key1": "nondefault"
   }
  },
  "etag": "b8578b95-f37f-401f-ac4f-057b980ef680",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1.phx.aaaaaaaabez242beorntix2tb4qfure2x7n3vpfmarcfqscrtgh3hplacg5q",
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
  "time-created": "2020-03-25T05:27:12.373000+00:00",
  "versioning": "Enabled"
 },
 "etag": "b8578b95-f37f-401f-ac4f-057b980ef680"
}

```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/UpdateBucket) operation. Include the `versioning` attribute with either the `Enabled` or `Suspended` value depending on whether you want to enable or suspend object versioning on the bucket.


Was this article helpful?
YesNo

