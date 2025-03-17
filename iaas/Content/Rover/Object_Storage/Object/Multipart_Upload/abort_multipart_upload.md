Updated 2024-09-16
# Aborting Multipart Uploads for Roving Edge Infrastructure
Describes how to abort multipart uploads to an Object Storage bucket on your Roving Edge Infrastructure devices.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/Multipart_Upload/abort_multipart_upload.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/Multipart_Upload/abort_multipart_upload.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Object_Storage/Object/Multipart_Upload/abort_multipart_upload.htm)


  * This task can't be performed using the Device Console.
  * Use the [oci os multipart abort](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/multipart/abort.html) command and required parameters to abort multipart uploads to an Object Storage bucket on your Roving Edge Infrastructure devices:
Copy
```
oci os multipart abort --bucket-name bucket_name --object-name object_name --upload-id upload_ocid [OPTIONS]
```

For example:
```
oci os multipart abort --bucket-name my_bucket --object-name 50MB.bin --upload-id 2~JiwKkKpDd1EMZVoaRz6ZihtQEDcULtH
{
 "data": [
  {
   "etag": "5f363e0e58a95f06cbe9bbc662c5dfb6",
   "md5": "5f363e0e58a95f06cbe9bbc662c5dfb6",
   "part-number": 3,
   "size": 5242880
  }
 ],
 "opc-next-page": "3"
}
WARNING: Are you sure you want to permanently remove this incomplete upload? [y/N]: y
```

Refer to your Roving Edge Infrastructure device's CLI help for a list of parameters available for this command. See [Accessing Command Line Interface Help](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLIAccessHelp).
For CLI setup information on your Roving Edge Infrastructure device, see [Using the Command Line Interface.](https://docs.oracle.com/en-us/iaas/Content/Rover/Access/cli_install.htm#CLI "Describes how to use the Command Line Interface to access a a Roving Edge Infrastructure device.")
  * Run the [AbortMultipartUpload](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/MultipartUpload/AbortMultipartUpload) operation to abort multipart uploads to an Object Storage bucket on your Roving Edge Infrastructure devices.


Was this article helpful?
YesNo

