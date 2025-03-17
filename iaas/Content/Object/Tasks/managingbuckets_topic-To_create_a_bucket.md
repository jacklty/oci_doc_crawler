Updated 2025-01-22
# Creating an Object Storage Bucket
Create a Object Storage bucket to store objects.
For information on the required permissions to create a bucket in Object Storage, see [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm#permissions).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm)


  *     1. On the **Buckets** list page, select **Create bucket**. If you need help finding the list page, see [Listing Object Storage Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. Select **Create Bucket**.
    3. Enter the following information:
       * **Bucket Name** : The system generates a default bucket name that reflects the current year, month, day, and time, for example **bucket-2019030620230306****-1359**. If you change this default to any other bucket name, use letters, numbers, dashes, underscores, and periods. Avoid entering confidential information.
       * **Default Storage Tier** : Select the default tier in which you want to store your data. When you upload objects, the objects are automatically assigned to and uploaded to this tier.
         * **Standard** is the primary, default storage tier used for [Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm#overview "Learn how to use Object Storage to store and easily access an unlimited amount of data at low cost.") service data. Use this tier to store data that requires fast and immediate access. Standard buckets do, however, provide an option to assign and upload objects to different storage tiers (Infrequent Access and Archive) while remaining in the Standard bucket.
         * **Archive** is the default storage tier used for [Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) data. Use the **Archive** tier for storing data that requires long retention periods but not immediate access. Archived data must be restored before the data is accessible.
For more information, see [Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#storage-tiers "Learn how Object Storage uses storage tiers to help you maximize access performance where appropriate and minimize storage costs where possible.").
       * **Enable Auto-Tiering** : Select this option if you want Object Storage to monitor and automatically move infrequently accessed objects from the Standard tier to the less expensive Infrequent Access storage tier. For more information, see [Auto-Tiering](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#auto_tiering).
       * **Enable Object Versioning** : Select this option if you want Object Storage to create an object version each time the content changes or the object is deleted. For more information, see [Object Storage Versioning](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingversioning.htm#object-versioning "Learn how to use object versioning to apply data protection against the accidental or malicious object updating or deleting of Object Storage objects.").
       * **Emit Object Events** : Select this option if you want to enable the bucket to emit events for object state changes. For more information about events, see [Overview of Events](https://docs.oracle.com/iaas/Content/Events/Concepts/eventsoverview.htm).
       * **Uncommited Multipart Uploads Clean-up** : Select this option to create a lifecycle rule that automatically deletes all uncommitted multipart uploads after 7 days.
       * **Encryption** : Buckets are encrypted with keys managed by Oracle by default, but you can optionally encrypt the data in this bucket by using your own Vault encryption key. Select **Encrypt using customer-managed keys** , and then select the Vault compartment and Vault that contain the master encryption key you want to use. Also select the master encryption key compartment and master encryption key. For more information about encryption, see [Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm). For details on how to create a vault, see [Managing Vaults](https://docs.oracle.com/iaas/Content/KeyManagement/Tasks/managingvaults.htm).
       * **Tags** : If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm). If you're not sure whether to apply tags, skip this option (you can apply tags later) or ask your administrator.
    4. Select **Create**.
The bucket is created immediately and you can start uploading objects to it. Objects added to archive buckets are immediately archived and must be [restored](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) before they're available for download.
  * **Creating a Standard default storage tier bucket**
By default, a bucket is created in the Standard Object Storage tier. You don't need to explicitly set `--storage-tier`. Standard is the primary, default storage tier used for [Object Storage](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm#overview "Learn how to use Object Storage to store and easily access an unlimited amount of data at low cost.") service data. Use the Standard tier for storing data that requires fast and immediate access. Standard buckets do, however, provide an option to assign and upload objects to different storage tiers (Infrequent Access and Archive), while remaining in the Standard bucket.
Use the [oci os bucket create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/create.html) command and required parameters to create a bucket:
Command
CopyTry It
```
oci os bucket create --compartment-id compartment_ocid --name bucket_name [OPTIONS]
```

For example:
```
oci os bucket create --compartment-id ocid.compartment.oc1..exampleuniqueID --name MyStandardBucket
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
  "**name": "MyStandardBucket**",
  "namespace": "MyNamespace",
  "object-events-enabled": false,
  "object-level-audit-mode": "Disabled",
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess",
  "replication-enabled": false,
  "**storage-tier": "Standard**",
  "time-created": "2020-06-12T19:04:05.879000+00:00",
  "versioning": "Disabled"
 },
 "etag": "7b7c3dc1-713f-4996-b176-a938345cae8e"
}
```

You can also enable auto-tiering on a Standard bucket at creation time by specifying the optional `--auto-tiering InfrequentAccess` parameter. See [Auto-Tiering](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#auto_tiering) for details. For example:```
oci os bucket create --compartment-id ocid.compartment.oc1..exampleuniqueID --name MyStandardBucket --auto-tiering Infrequent Access
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

A Standard tier bucket is created immediately and you can start uploading objects.
**Creating an Archive default storage tier bucket**
To create an Archive tier bucket, you must explicitly set `--storage-tier Archive`. Archive is the default storage tier used for [Archive Storage](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) service data. Use the [Archive](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) tier for storing data that doesn't require immediate access, but requires long retention periods. Access to data in the Archive tier isn't immediate. Archived data must be [restored](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) before the data is accessible.
Command
CopyTry It
```
oci os bucket create --compartment-id compartment_ocid --name archive_bucket_name --storage-tier Archive [OPTIONS]
```

For example:
```
oci os bucket create --compartment-id ocid.compartment.oc1..exampleuniqueID --name MyArchiveBucket
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
  "**name": "MyArchiveBucket**",
  "namespace": "MyNamespace",
  "object-events-enabled": false,
  "object-level-audit-mode": "Disabled",
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess",
  "replication-enabled": false,
  "**storage-tier": "Archive**",
  "time-created": "2020-06-12T19:04:05.879000+00:00",
  "versioning": "Disabled"
 },
 "etag": "c8889cd1-8414-41fb-84b7-3738c39e62c5"
}
```

An Archive Storage bucket is created and you can start uploading objects. Objects uploaded to Archive Storage buckets are immediately archived and must be [restored](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) before they're available for download.
#### Creating Public Bucket (Listing and Downloading Bucket Objects) 🔗 
To create a public bucket that allows listing and downloading bucket objects, you must explicitly set `--public-access-type ObjectRead`.
Command
CopyTry It
```
oci os bucket create --compartment-id compartment_ocid --name bucket_name --public-access-type ObjectRead [OPTIONS]
```

For example:
```
oci os bucket create --compartment-id ocid.compartment.oc1..exampleuniqueID --name MyPublicObjectReadBucket --public-access-type ObjectRead
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  "defined-tags": {},
  "etag": "01096e0b-659a-4d9d-a806-d57568cf1b22",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "kms-key-id": null,
  "metadata": {},
  "**name": "MyPublicObjectReadBucket**",
  "namespace": "MyNamespace",
  "object-events-enabled": false,					
  "object-lifecycle-policy-etag": null,
  "**public-access-type": "ObjectRead**",
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-22T19:04:05.879000+00:00",
  "versioning": "Disabled"
 },
 "etag": "01096e0b-659a-4d9d-a806-d57568cf1b22"
}
```

#### Creating Public Bucket (Downloading Bucket Objects) 🔗 
To create a public bucket that allows just downloading bucket objects, you must explicitly set `--public-access-type ObjectReadWithoutList`.
Command
CopyTry It
```
oci os bucket create --compartment-id compartment_ocid --name bucket_name --public-access-type ObjectReadWithoutList [OPTIONS]
```

For example:
```
oci os bucket create --compartment-id ocid.compartment.oc1..exampleuniqueID --name MyPublicObjectReadBucket --public-access-type ObjectReadWithoutList
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  "defined-tags": {},
  "etag": "ec20c59a-f5ba-4a6d-8a7e-b69bb9bb76ad",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "kms-key-id": null,
  "metadata": {},
  "**name": "MyPublicObjectReadWithoutListBucket**",
  "namespace": "MyNamespace",
  "object-events-enabled": false,
  "object-lifecycle-policy-etag": null,
  "**public-access-type": "ObjectReadWithoutList**",
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-22T20:18:29.203000+00:00",
  "versioning": "Disabled"
 },
 "etag": "ec20c59a-f5ba-4a6d-8a7e-b69bb9bb76ad"
}
```

#### Creating a Bucket with Resource Tags 🔗 
You can create standard Object Storage tier or [Archive](https://docs.oracle.com/iaas/Content/Archive/Concepts/archivestorageoverview.htm) tier buckets with [resource tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).
To add resource tags when creating a bucket, set one or both of the `--defined-tags` and `--freeform-tags` options.
**Tip** The `--defined-tags` and `--freeform-tags` options require that the input to be a complex type formatted in valid JSON. See [Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output) and [Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON) for information about JSON formatting.
The following example syntax creates a standard Object Storage tier bucket with a defined tag:
Command
CopyTry It
```
oci os bucket create --compartment-id compartment_id --name bucket_name --defined-tags 'JSON_formatted_defined_tag' [OPTIONS]
```

Examples of defined tag formatting:
```
'{"Operations": {"CostCenter": "42"}'
```
```
'{"Logistics": {"Procurement": "Madrid Center"}},"Financials":{"Production": "Unit 5"}}'
```

**Note** If you're running the CLI on a Windows computer, you might need to use the backslash (\\) character to escape the strings containing the tag values. For example, a single defined tag is formatted `'{\"Logistics\": {\"Procurement\": \"Madrid Center\"}}'`
For example:
```
oci os bucket create --compartment-id ocid.compartment.oc1..exampleuniqueID --name MyBucketDefined --defined-tags {"Operations": {"CostCenter": "42"}}
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  **"defined-tags": {
   "operations": {
    "costcenter": "42"				}
  }**,
  "etag": "ea88f444-842c-462d-965e-d3540b3b54f6",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "kms-key-id": null,
  "metadata": {},
  "name": "MyBucketDefined",
  "namespace": "MyNamespace",
  "object-events-enabled": false,					
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess",
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-23T19:47:51.362000+00:00",
  "versioning": "Disabled"
 },
 "etag": "ea88f444-842c-462d-965e-d3540b3b54f6"
}
```

The following example syntax creates a Standard tier bucket with a free-form tag:
Command
CopyTry It
```
oci os bucket create --compartment-id compartment_ocid --name bucket_name --freeform-tags JSON_formatted_free-form_tag [OPTIONS]
```

Examples of free-form tag formatting:
```
'{"Chicago_Team": "marketing_videos"}'
```
```
'{"Project": "prototype 3","Manager": "Meadows"}'
```

**Note** If you're running the CLI on a Windows computer, you might need to use the backslash (\\) character to escape the strings containing the tag values. For example, a single free-form tag is formatted as `'{\"Chicago_Team\": {\"marketing_videos\"}}'`
For example:
```
oci os bucket create --compartment-id ocid.compartment.oc1..exampleuniqueID --name MyBucketFreeform --freeform-tags {"Chicago_Team": "marketing_videos"}
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  "defined-tags": {},
  "etag": "6f4bda10-fc8b-462e-8563-875639fd7294",
  **"freeform-tags": {
   "Chicago_Team": "marketing_videos"
  }**,
  "is-read-only": false,
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "kms-key-id": null,
  "metadata": {},
  "name": "MyBucketFreeform",
  "namespace": "MyNamespace",
  "object-events-enabled": false,					
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess",
  "storage-tier": "Standard",
  "time-created": "2020-06-23T20:51:16.260000+00:00"
 },
 "etag": "6f4bda10-fc8b-462e-8563-875639fd7294"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
#### Assigning a Key to the Bucket 🔗 
You can assign a Vault key to a bucket you're creating by including the kms_key_id parameter. 
Command
CopyTry It
```
oci os bucket create --compartment-id ocid.compartment.oc1..exampleuniqueID --name bucket_name --kms-key-id kms_key_id [OPTIONS]
```

where `kms_key_id` is the OCID of the key versions that contain the cryptographic material used to encrypt and decrypt data, protecting the data where the data is stored.
For example:
```

oci os bucket create --compartment-id ocid.compartment.oc1..exampleuniqueID --name MyKeyBucket --kms-key-id ocid1.key.region1.sea..exampleuniqueID
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  "defined-tags": {},
  "etag": "e7f29fdd-b5f5-42e5-a98b-80883f9f2f32",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "**kms-key-id": "ocid1.key.region1.sea..exampleuniqueID**",
  "metadata": {},
  "name": "MyKeyBucket",
  "namespace": "MyNamespace",
  "object-events-enabled": false,					
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess"
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-29T23:00:35.490000+00:00",
  "versioning": "Disabled"
 },
 "etag": "e7f29fdd-b5f5-42e5-a98b-80883f9f2f32"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/CreateBucket) operation to create a bucket.
When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```
n/object_storage_namespace/b/bucket
```

Two key properties in the payload are:
    * `publicAccessType` property controls whether the bucket is private or public and limits the capability to list public bucket contents.
    * `objectEventsEnabled` property controls if events are emitted for the objects in this bucket.


Was this article helpful?
YesNo

