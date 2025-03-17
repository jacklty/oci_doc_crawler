Updated 2024-02-12
# Listing Multipart Uploads in Object Storage
View a list of the in-progress multipart uploads for an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_list_the_parts_of_an_unfinished_or_failed_multipart_upload.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_list_the_parts_of_an_unfinished_or_failed_multipart_upload.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_list_the_parts_of_an_unfinished_or_failed_multipart_upload.htm)


  * This task can't be performed using the OCI Console.
  * Use the [oci os multipart list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/multipart/list.html) command and required parameters to list the in-progress multipart uploads in a bucket:
Command
CopyTry It
```
oci os multipart list --bucket-name bucket_name [OPTIONS]
```

For example:
Command
CopyTry It
```
oci os multipart list --namespace MyNamespace --bucket-name MyBucket{
 "data": [
  {
   "bucket": "MyBucket",
   "namespace": "MyNamespace",
   "object": "MyObject",
   "time-created": "2019-07-25T21:55:21.973000+00:00",
   "upload-id": "0b7abd48-9ff2-9d5f-2034-63a02fdd7afa"
  },
  {
   "bucket": "MyBucket",
   "namespace": "MyNamespace",
   "object": "MyObject",
   "time-created": "2019-07-25T21:53:09.246000+00:00",
   "upload-id": "1293ac9d-83f8-e055-a5a7-d1e13277b5c0"
  },
  {
   "bucket": "MyBucket",
   "namespace": "MyNamespace",
   "object": "MyObject",
   "time-created": "2019-07-25T21:46:34.981000+00:00",
   "upload-id": "33e7a875-9e94-c3bc-6577-2ee5d8226b53"
  }
...
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListMultipartUploads](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/ListMultipartUploads) operation to list the in-progress multipart uploads in a bucket.
See [Using the Multipart API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-Using_the_Multipart_Upload_API.htm#using_api "Learn how to run multipart uploads for a bucket using the API.") for more information.


Was this article helpful?
YesNo

