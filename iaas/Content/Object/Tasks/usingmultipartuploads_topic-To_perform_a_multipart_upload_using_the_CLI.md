Updated 2024-02-12
# Running an Multipart Upload in Object Storage
Describes how to upload a large object using multipart upload in Object Storage.
For prerequisite information, see [Multipart Uploads](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads.htm#multipart-uploads "Learn how to use multipart uploads to move objects larger than 100 MB more efficiently and with greater resiliance.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_perform_a_multipart_upload_using_the_CLI.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_perform_a_multipart_upload_using_the_CLI.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-To_perform_a_multipart_upload_using_the_CLI.htm)


  * This task can't be performed using the OCI Console.
  * Use the [oci os object put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/put.html) command with the `part-size` parameter to upload an object to a bucket:
Command
CopyTry It
```
oci os object put --bucket-name bucket_name --file file_location --part-size part_size [OPTIONS]
```

where `part_size` value represents the size of each part in mebibytes (MiBs). Object Storage waives the minimum part size restriction for the last uploaded part. The `--part-size` value must be an integer.
Optionally, you can use the `--parallel-upload-count` parameter to set the maximum number of parallel uploads allowed:
Command
CopyTry It
```
oci os object put --bucket-name bucket_name --file file_location --part-size part_size --parallel-upload-count <maximum_number_parallel_uploads> [OPTIONS]
```

For example:
```
oci os object put --bucket-name MyBucket --file ~/path/to/file --part-size 500 --parallel-upload-count 10 
Upload ID: 277ffff5-e1b5-e81d-5f81-c374a8f33998
Split file into 12 parts for upload.
Uploading object ################################### 100%
{ "etag": "861c8341-74d8-4142-8da4-28e1ce7783ba", "last-modified": "Wed, 25 Sep 2019 19:59:15 GMT", "opc-multipart-md5": "9Qn1eyou2yMiyOO9Bc7o1A==-12" } 
```

For more information on the `oci os object put` command, see [Uploading an Object to a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm#top "Upload an object to a bucket or folder in Object Storage.").
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateMultipartUpload](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/CreateMultipartUpload) operation to create a multipart upload to a bucket.
See [Using the Multipart API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads_topic-Using_the_Multipart_Upload_API.htm#using_api "Learn how to run multipart uploads for a bucket using the API.") for more information.


Was this article helpful?
YesNo

