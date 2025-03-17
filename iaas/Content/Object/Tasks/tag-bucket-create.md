Updated 2025-01-30
# Tagging an Object Storage Bucket at Creation
Add metadata to an Object Storage bucket when you first create it. This metadata enables you to define keys and values and associate them with resources.
For more information, see [Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-bucket-create.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-bucket-create.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/tag-bucket-create.htm)


  *     1. Begin the steps for creating a bucket using the Oracle Cloud Infrastructure Console as described in [Creating an Object Storage Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#top "Create a Object Storage bucket to store objects."). 
    2. Find the **Tags** section of the **Create Bucket** dialog box.
    3. Complete the following. See [Overview of Tagging](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm) for descriptions of these fields.
       * **Tag namespace**
       * **Tag key**
       * **Value**
    4. Select **Create**.
  * Use the `--defined-tags` or `--freeform-tags` options when running the [oci os bucket create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/create.html) command to tag a bucket at the time of its creation:
Command
CopyTry It
```
oci os bucket create --compartment-id compartment_ocid --defined-tags JSON_formatted_defined_tag --freeform-tags JSON_formatted_free-form_tag [OPTIONS]
```

Provide key-value pair input for `--defined-tags` and `--freeform-tags` as valid formatted JSON. See [Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output) and [Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON) for information about JSON formatting.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/CreateBucket) operation to create a bucket. Include the `definedTags` and `freeformTags` attributes and their values.
When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```
n/object_storage_namespace/b/bucket
```



Was this article helpful?
YesNo

