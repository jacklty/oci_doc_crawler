Updated 2025-01-22
# Getting the Object Lifecycle Policy Details in Object Storage
View the details of the object lifecycle policy for an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_get_a_buckets_lifecycle_policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_get_a_buckets_lifecycle_policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usinglifecyclepolicies_topic-To_get_a_buckets_lifecycle_policy.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Lifecycle Policy Rules**.
    3. From the **Actions** menu for the lifecycle policy rule you want, select **View Lifecycle Rule Details**.
The **Lifecycle Rule Details** dialog box opens. Here you can view the lifecycle rule's details, such as the target type and lifecycle action.
  * Use the [oci os object-lifecycle-policy get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object-lifecycle-policy/get.html) command and required parameters to get the object lifecycle policy configuration for a bucket.
Command
CopyTry It
```
oci os object-lifecycle-policy get --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os object-lifecycle-policy get --bucket-name MyStandardTierBucket
{
 "data": {
  "items": [
   {
    "action": "ABORT",
    "is-enabled": true,
    "name": "Delete-Failed-Multipart-Uploads-Rule",
    "object-name-filter": null,
    "target": "multipart-uploads",
    "time-amount": 5,
    "time-unit": "DAYS"
   },
   {
    "action": "DELETE",
    "is-enabled": true,
    "name": "Delete-from-Archive-Rule",
    "object-name-filter": {
     "exclusion-patterns": null,
     "inclusion-patterns": null,
     "inclusion-prefixes": null
    },
    "target": "objects",
    "time-amount": 240,
    "time-unit": "DAYS"
   },
   {
    "action": "INFREQUENT_ACCESS",
    "is-enabled": true,
    "name": "Move-to-Infrequent-Access-Rule",
    "object-name-filter": {
     "exclusion-patterns": null,
     "inclusion-patterns": null,
     "inclusion-prefixes": null
    },
    "target": "objects",
    "time-amount": 45,
    "time-unit": "DAYS"
   },
   {
    "action": "ARCHIVE",
    "is-enabled": true,
    "name": "Move-to-Archive-Rule",
    "object-name-filter": {
     "exclusion-patterns": null,
     "inclusion-patterns": null,
     "inclusion-prefixes": null
    },
    "target": "previous-object-versions",
    "time-amount": 90,
    "time-unit": "DAYS"
   }
  ],
  "time-created": "2021-02-01T15:34:59.007000+00:00"
 },
 "etag": "009743fb-9503-4442-913f-fddd2ebd9542"
}
```

For example, to get the lifecycle policy that archives objects after 30 days:
```
oci os object-lifecycle-policy get --bucket-name MyBucketWithoutVersioning
{
 "data": {
  "items": [
   {
    "action": "ARCHIVE",
    "is-enabled": true,
    "name": "Archive-After-30-Days-Rule",
    "object-name-filter": {
     "exclusion-patterns": null,
     "inclusion-patterns": null,
     "inclusion-prefixes": null
    },
    "target": "objects",
    "time-amount": 30,
    "time-unit": "DAYS"
   }
  ],
  "time-created": "2020-10-27T17:56:27.085000+00:00"
 },
 "etag": "lifecycle-policy-a3f5d4a6-ca25-4a28-9eea-7d073f51e754"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetObjectLifecyclePolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/ObjectLifecyclePolicy/GetObjectLifecyclePolicy) operation to get the object lifecycle policy configuration for a bucket.


Was this article helpful?
YesNo

