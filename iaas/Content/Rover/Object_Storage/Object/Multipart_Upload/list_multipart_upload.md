Updated 2024-09-16
# Listing Multipart Uploads for Roving Edge Infrastructure 
Describes how to list the multipart uploads that move large objects to an Object Storage bucket on your Roving Edge Infrastructure devices.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/Multipart_Upload/list_multipart_upload.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/Multipart_Upload/list_multipart_upload.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/Multipart_Upload/list_multipart_upload.htm)


  * This task cannot be performed using the Device Console.
  * Use the [oci os multipart list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/multipart/list.html) command and required parameters to list the multipart uploads that move large objects to an Object Storage bucket on your Roving Edge Infrastructure devices:
Copy
```
oci os multipart list --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os multipart list --bucket-name my_bucket
{
 "data": [
  {
   "bucket": "my_bucket",
   "namespace": "rover-namespace",
   "object": "50MB.bin",
   "storage-tier": null,
   "time-created": "2023-06-02T12:56:30.270000+00:00",
   "upload-id": "2~JiwKkKpDd1EMZVoaRz6ZihtQEDcULtH"
  }
 ]
} 
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [ListMultipartUploads](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/ListMultipartUploads) operation to list the multipart uploads that move large objects to an Object Storage bucket on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

