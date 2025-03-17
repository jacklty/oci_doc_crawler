Updated 2024-01-18
# Listing the Parts of an Unfinished or Failed Multipart Upload
On Compute Cloud@Customer, you can list the parts of a multipart object upload using the CLI and API.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-the-parts-of-an-unfinished-or-failed-multi-part-upload.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-the-parts-of-an-unfinished-or-failed-multi-part-upload.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/listing-the-parts-of-an-unfinished-or-failed-multi-part-upload.htm)


  * This task isn't available in the Console. 
  * Use the [oci os multipart list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/multipart/list.html) command and required parameters to list the parts.
Syntax:
Copy
```
oci os multipart list --namespace-name <object_storage_namespace> --bucket-name <bucket_name> [OPTIONS]
```

Example
```
oci os multipart list
--namespace-name examplenamespace \ 
--bucket-name MyBucket \
{
 "data": [
  {
   "bucket": "MyBucket",
   "namespace": "examplenamespace",
   "object": "MyObject",
   "time-created": "2019-07-25T21:55:21.973000+00:00",
   "upload-id": "0b7abd48-9ff2-9d5f-2034-63a02fdd7afa"
  },
  {
   "bucket": "MyBucket",
   "namespace": "examplenamespace",
   "object": "MyObject",
   "time-created": "2019-07-25T21:53:09.246000+00:00",
   "upload-id": "1293ac9d-83f8-e055-a5a7-d1e13277b5c0"
  },
  {
   "bucket": "MyBucket",
   "namespace": "examplenamespace",
   "object": "MyObject",
   "time-created": "2019-07-25T21:46:34.981000+00:00",
   "upload-id": "33e7a875-9e94-c3bc-6577-2ee5d8226b53"
  }
...
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListMultipartUploadParts](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/ListMultipartUploadParts) operation to list the parts.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

