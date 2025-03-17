Updated 2024-04-13
# Bulk Uploading Object Storage Objects to a Bucket
Upload a group of objects from a file system to an Object Storage bucket or folder.
To upload objects larger than 64 MiB, the Console uses multipart uploads. You need OBJECT_CREATE and OBJECT_OVERWRITE permissions to perform multipart uploads. For details, see [Object Storage Multipart Uploads](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads.htm#multipart-uploads "Learn how to use multipart uploads to move objects larger than 100 MB more efficiently and with greater resiliance.") and [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).
## Using the CLI 🔗 
Use the [oci os object bulk-upload](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-upload.html) command and required parameters to upload a group of files in a directory and its sub-directories to a bucket:
Command
CopyTry It
```
oci os object bulk-upload --bucket-name bucket_name --src-dir source_directory_location [OPTIONS]
```

where `source_directory_location` is the upload file system directory path, such as `C:\workspace\Upload\` or `/home/user/Documents/Upload`. 
If your source directory has subdirectories, the subdirectory names are prepended to the names of the files stored in those subdirectories, delimited with a forward slash (/) character. For example, if a file named `maple.jpg` is stored in the subdirectory `trees`, when the file is uploaded, Object Storage assigns the name `trees/maple.jpg` to the resulting object.
By default, all objects in the bucket are uploaded. Use the **Optional Parameters** listed in the [oci os object bulk-upload](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-upload.html) page to specify what files in bulk to upload.
### Specifying the Storage Tier of the Uploaded Bulk Objects 🔗 
Include the `storage-tier` parameter to assign a storage tier to the objects you're uploading in bulk.
Command
CopyTry It
```
oci os object bulk-upload --bucket-name bucket_name --src-dir source_directory_location --storage-tier [Archive | InfrequentAccess | Standard] [OPTIONS]
```

For example, if you're uploading to a Standard tier-configured bucket and you wan to upload objects to the Infrequent Access storage tier, include `--storage-tier InfrequentAccess` in the command:
```
oci os object bulk-upload --bucket-name MyBucket --src-dir C:\workspace\Files --storage-tier InfrequentAccess
Uploaded logFile.log [####################################] 100%
Uploaded MyFile.txt [####################################] 100%
{
 "skipped-objects": [],
 "upload-failures": {},
 "uploaded-objects": {
  "MyFile.txt": {   
  "etag": "e25f95e6-a2bd-435c-83d6-785f838134d5",
  "last-modified": "last-modified": "Sat, 12 Dec 2020 11:31:36 GMT",
  "opc-content-md5": "opc-content-md5": "vqglL/ToD0FxnqE83wBycw=="
 },
  "logFile.log": {
  "etag": "bbcf33dd-a177-4406-bed1-a4f7125da800",
  "last-modified": "Sat, 12 Dec 2020 11:31:36 GMT",
  "opc-content-md5": "K8vB8NVASIvtL2BE5ksUjw=="
  }
 }
}
```
See [Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#storage-tiers "Learn how Object Storage uses storage tiers to help you maximize access performance where appropriate and minimize storage costs where possible.") for more information on how storage tiers work.
If you don't specify `--storage-tier`, the object is automatically assigned and uploaded to the default storage tier of the bucket (Standard or Archive).
### Appending a Prefix String to the Uploaded Bulk Objects 🔗 
To append a [prefix string](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#nameprefix) to the object names created by your bulk upload, include the `object-prefix` parameter. For example:
Command
CopyTry It
```
oci os object bulk-upload --bucket-name MyBucket --src-dir C:\workspace\Files --object-prefix /bicycling/gloves/
				
Uploaded /bicycling/gloves/gloves_27_A.jpg [####################################] 100%
Uploaded /bicycling/gloves/gloves_31_A.jpg [####################################] 100%
{
 "skipped-objects": [],
 "upload-failures": {},
 "uploaded-objects": {
  "/bicycling/gloves/gloves_27_A.jpg": {
   "etag": "7ba793ce-a341-4c56-9baf-61ca2c56ad50",
   "last-modified": "Sat, 12 Dec 2020 18:35:09 GMT",
   "opc-content-md5": "1B2M2Y8AsgTpgAmY7PhCfg=="
 },
  "/bicycling/gloves/gloves_31_A.jpg": {
   "etag": "6efa58a6-a723-4696-a31f-3c5099adbec4",
   "last-modified": "Sat, 12 Dec 2020 18:35:09 GMT",
   "opc-content-md5": "6GxlLP9fa71HhVnpLNJ+DQ=="
  }
 }
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
Was this article helpful?
YesNo

