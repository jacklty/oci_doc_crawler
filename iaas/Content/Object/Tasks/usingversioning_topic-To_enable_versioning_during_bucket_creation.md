Updated 2023-12-19
# Enabling Object Versioning when Creating an Object Storage Bucket
Enable object versioning when you create an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_versioning_during_bucket_creation.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_versioning_during_bucket_creation.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning_topic-To_enable_versioning_during_bucket_creation.htm)


  *     1. Create a bucket as described in [Creating an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#top "Create a Object Storage bucket to store objects."). 
    2. Select **Enable Object Versioning** to direct Object Storage to create an object version each time the content changes or the object is deleted.
  * Create a bucket as described in [Creating an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#top "Create a Object Storage bucket to store objects."). Include the `versioning` parameter with the value `enabled`:
Command
CopyTry It
```
oci os bucket create --name bucket_name --compartment-id compartment_ocid --versioning enabled
```

For example:
```
oci os bucket create --name MyStandardBucket --compartment-id ocid.compartment.oc1..exampleuniqueID --versioning enabled
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "compartment-id": "ocid1.compartment.oc1..aaaaaaaamnk2ilreg5fkgu7rarfbbhdv3a5ji4eixxgkl4uprbqk6aefv5sq",
  "created-by": "ocid1.user.oc1..aaaaaaaah46lg3ueuftovn3urjgstlg4laxnre3djelu5jxy5uaqhgy7acgq",
  "defined-tags": {
   "Financials": {
    "key1": "nondefault"
   }
  },
  "etag": "a91fd091-e112-483e-8e23-2b5d11e3dc2d",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1.phx.aaaaaaaaqagwnd5foe23xhpqk6ts754igpuw5t7qrnapbmrv5tjiugvjvicq",
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
  "time-created": "2020-04-14T14:14:08.421000+00:00",
  "versioning": "Enabled"
 },
 "etag": "a91fd091-e112-483e-8e23-2b5d11e3dc2d"
}				
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Create a bucket using the [CreateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/CreateBucket) operation as described in [Creating an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#top "Create a Object Storage bucket to store objects.") . Include the `versioning` attribute with the value `enabled`.


Was this article helpful?
YesNo

