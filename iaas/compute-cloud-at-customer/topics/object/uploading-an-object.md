Updated 2024-01-18
# Uploading an Object
On Compute Cloud@Customer, you can upload an object using the CLI and API.
An object can be uploaded as a single part or as multiple parts. Use the `--no-multipart` option to upload as a single part. For detailed information on multipart uploads, see [Performing a Multipart Upload](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/performing-a-multi-part-upload.htm#performing-a-multi-part-upload "On Compute Cloud@Customer, you can upload objects in multiple parts.").
**Note** Objects stored in Compute Cloud@Customer Object Storage are compressed. You might notice that the size of an uploaded object is smaller that the size of the original object before it was uploaded.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/uploading-an-object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/uploading-an-object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/uploading-an-object.htm)


  * This task isn't available in the Console. 
  * Use the [oci os object put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/put.html) command and required parameters to upload an object to a bucket.
Copy
```
oci os object put --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --file <file_location> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [PutObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/PutObject) operation to upload an object to a bucket.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

