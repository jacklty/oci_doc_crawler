Updated 2025-01-30
# Tagging an Object Storage Bucket when Updating
Add metadata to an Object Storage bucket when you update an existing one. This metadata enables you to define keys and values and associate them with resources.
For more information, see [Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-bucket-update.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-bucket-update.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-bucket-update.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. Enter the following information:
       * **Tag namespace**
       * **Tag key**
       * **Tag value**
See [Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm) for descriptions of these options.
    3. Select **Add tags**.
  * Use the `--defined-tags` or `--freeform-tags` options when running the [oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command to tag a private endpoint you're updating:
Command
CopyTry It
```
oci os bucket update --name bucket_name --defined-tags JSON_formatted_defined_tag --freeform-tags JSON_formatted_free-form_tag [OPTIONS]
```

Provide key-value pair input for `--defined-tags` and `--freeform-tags` as valid formatted JSON. See [Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output) and [Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON) for information about JSON formatting.
For example:
```
oci os bucket update --name MyBucket --defined-tags '{"Operations": {"CostCenter": "42"}}' --freeform-tags '{"Chicago_Team": "marketing_videos"}'
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
   **"defined-tags": {
   "operations": {
    "costcenter": "42"**
   }
  },
  "etag": "0a26b47d-c43f-4ef8-9c26-02bb8d69fa34",
  **"freeform-tags": {
   "Chicago_Team": "marketing_videos"**,
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "kms-key-id": null,
  "metadata": {
   "department": "Finance"
  },
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
 "etag": "0a26b47d-c43f-4ef8-9c26-02bb8d69fa34"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/UpdateBucket) operation. Include the `definedTags` and `freeformTags` attributes and their values.
When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```
n/object_storage_namespace/b/bucket
```



Was this article helpful?
YesNo

