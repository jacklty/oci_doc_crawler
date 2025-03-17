Updated 2024-01-18
# Performing a Multipart Upload
On Compute Cloud@Customer, you can upload objects in multiple parts.
With multipart uploads, individual parts of an object can be uploaded in parallel to reduce the amount of time you spend uploading.
Multipart uploads accommodate objects that are too large for a single upload operation. Object parts must be no larger than 50 GiB.
You can pause between the uploads of individual parts, and resume the upload when your schedule and resources allow.
## Object Parts 🔗 
With multipart upload, you split the object you want to upload into individual parts. Individual parts can be as large as 50 GiB. The maximum size for an uploaded object is 10 TiB.
Decide what part number you want to use for each part. Part numbers can range from 1 to 10,000. You do not need to assign contiguous numbers, but Object Storage constructs the object by ordering part numbers in ascending order.
## Multipart Upload API 🔗 
Before you use the multipart upload API, you are responsible for creating the parts to upload. Object Storage provides API operations for the remaining steps.
A multipart upload performed using the API consists of the following steps:
  1. Start an upload.
  2. Upload object parts.
  3. Commit the upload.


The service also provides API operations for listing in-progress multipart uploads, listing the object parts in an in-progress multipart upload, and aborting in-progress multipart uploads initiated through the API.
## Multipart Upload CLI 🔗 
When you perform a multipart upload using the CLI, you don't need to split the object into parts as you are required to do by the API. Instead, you specify the part size of your choice, and Object Storage splits the object into parts and performs the upload of all parts automatically. You can choose to set the maximum number of parts that can be uploaded in parallel. By default, the CLI limits the number of parts that can be uploaded in parallel to three. When using the CLI, you don't have to perform a commit when the upload is complete.
You can also use the CLI to list in-progress multipart uploads, and to cancel multipart uploads initiated through the API.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/performing-a-multi-part-upload.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/performing-a-multi-part-upload.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/performing-a-multi-part-upload.htm)


  * This task isn't available in the Console. 
  * Use the [oci os object put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/put.html) command and required parameters to upload an object in multiple parts.
Syntax:
Copy
```
oci os object put --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --file <file_location> --parallel-upload-count <maximum_number_parallel_uploads> --part-size <upload_part_size_in_MB> --force [OPTIONS]
```

Example:
```
oci os object put  \
--namespace-name examplenamespace \
--file /boot/initramfs-0-rescue-e542c19f0fbf4e41a41428d933a7357f.img  \
--parallel-upload-count 5  \
--part-size 15  \
--force
Upload ID: a21bba2c-8922-4b9c-a98a-9ef3569c0138
Split file into 6 parts for upload.
Uploading object [####################################] 100%
{
 "etag": "0964effc8dc4394fd317f03a025ae5d0",
 "last-modified": "2021-05-11T21:35:19",
 "opc-multipart-md5": "UIVRhiwSHY6o0E4pi/yfGg==-6"
}
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * A multipart upload performed using the API consists of the following steps:
    1. Starting an upload.
    2. Uploading object parts.
    3. Committing the upload.
Before you use the multipart upload API, you're responsible for creating the parts to upload. Object Storage provides API operations for the remaining steps. The service also provides API operations for listing in-progress multipart uploads, listing the object parts in an in-progress multipart upload, and aborting in-progress multipart uploads initiated through the API. 
**Note** These multipart upload API requirements do not apply to the CLI.
For more information about using the multipart Upload API, see [Using the Multipart Upload API](https://docs.oracle.com/iaas/Content/Object/Tasks/usingmultipartuploads.htm#using_api).
Use the [PutObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/PutObject) operation to upload an object in multiple parts.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

