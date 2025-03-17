Updated 2025-01-30
# Uploading an Object Storage Object to a Bucket
Upload an object to a bucket or folder in Object Storage.
To upload objects larger than 64 MiB, the Console uses multipart uploads. You need OBJECT_CREATE and OBJECT_OVERWRITE permissions to perform multipart uploads. For details, see [Object Storage Multipart Uploads](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads.htm#multipart-uploads "Learn how to use multipart uploads to move objects larger than 100 MB more efficiently and with greater resiliance.") and [Details for Object Storage, Archive Storage, and Data Transfer](https://docs.oracle.com/iaas/Content/Identity/policyreference/objectstoragepolicyreference.htm).
Use the prefix option to prepend a prefix value to any object's name that you upload to the bucket. You can use the prefix to search the bucket for only those objects whose names match the prefix. For example, if you included the prefix "test" during an object upload, all the included objects names are prepended with that prefix value. An object named "my-object.txt" is uploaded to the bucket as "testmy-object.txt." 
See [Object Naming Using Prefixes and Hierarchies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#nameprefix) for more information about creating prefixes for objects. 
See [Searching for Objects in a Bucket](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/search-objects.htm#top "Search for objects in an Object Storage bucket.") for more information on how to search for objects in a bucket using the prefix option.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. Select **Upload**. To upload objects to a folder or subfolder in the **Objects** list, open that folder and select **Upload**.
    4. Enter the following information:
       * **Object Name Prefix** : (optional) If provided, this prefix is prepended to each one of the files you upload.
         * Prefix strings with a slash ("/") delimiter to simulate hierarchy and create folders or subfolders.
         * Prefix strings without a delimiter for matching purposes to perform allowed bulk operations.
For details, see [Object Naming Using Prefixes and Hierarchies](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#nameprefix).
       * **Storage Tier** : Specify the type of storage tier the object being uploaded belongs to:
         * **Standard Tier**
         * **Infrequent Access**
         * **Archive**
See [Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#storage-tiers "Learn how Object Storage uses storage tiers to help you maximize access performance where appropriate and minimize storage costs where possible.") for descriptions of the storage tier types.
**Note**
Standard storage tier buckets can contain a mix of objects with different storage tier assignments. An object remains in the Standard bucket, even if the object is archived, restored, or if tier assignment is changed.
    5. Select the objects that you want to upload into the **Choose Files from your Computer** box using one of the following methods:
       * Drag one or more files from your computer into the box.
       * Select the **select files** link to display a file selection dialog box where you can navigate to the files you want to upload.
The files you select to upload are displayed in a list. To remove a selected file from being uploaded, select the **X** next to the file name.
If the files you select to upload are already stored in the bucket or folder with the same name, the Console displays messages warning you of an overwrite.
    6. (Optional) Select **Show Optional Response Headers and Metadata** to specify values for optional response headers and metadata to be displayed in the **Object Details** dialog box.
      1. Select the type of attribute that you're adding:
         * To add a response header, select a value in the **Name** list and then enter a value in the **Value** box.
         * To add metadata, enter a value in the **Name** box and then enter a value in the **Value** box.
      2. To add another attribute, select **+ Add More Headers or Metadata**. To delete an attribute, select the **X** next to the attribute.
    7. Select **Upload**. The selected objects are uploaded and displayed in the list of objects in the bucket or folder.
  * Use the [oci os object put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/put.html) command and required parameters to upload an object to a bucket:
Command
CopyTry It
```
oci os object put --bucket-name bucket_name --file file_location [OPTIONS]
```

where `file_location` is the source directory path of the object being uploaded, such as `C:\workspace\Uploads\MyFile.txt` or `/home/user/Documents/Uploads/MyFile.txt`. The uploaded object's name doesn't include the path information (for example, `C:\workspace\Uploads\`), just the actual file name by itself (`MyFile.txt`).
An object can be uploaded as a single part or as multiple parts. Use the `--no-multipart` option to upload as a single part. For detailed information on multipart uploads, see [Object Storage Multipart Uploads](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingmultipartuploads.htm#multipart-uploads "Learn how to use multipart uploads to move objects larger than 100 MB more efficiently and with greater resiliance.").
For more information about attributes that you can add when you upload an object, see [Optional Response Headers and Metadata](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects.htm#HeadersAndMetadata).
To add custom metadata key-value pairs, use the `--metadata` option:
Command
CopyTry It
```
oci os object put --bucket-name bucket_name --file file_location --name object_name --metadata json_formatted_key-value_pairs
```

where `JSON-formatted_key-value_pair` is a key-value pair input as valid formatted JSON. See [Passing Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#Managing_CLI_Input_and_Output__Passing) and [Using a JSON File for Complex Input](https://docs.oracle.com/iaas/Content/API/SDKDocs/cliusing.htm#AdvancedJSON) for more information about JSON formatting.
For example:
Command
CopyTry It
```
oci os object put --bucket-name MyBucket --file C:\workspace\MyFile.txt --metadata '{"Department": "Finance"}'
{
 "etag": "3504606b-8412-4b5d-924a-aeaeacf1df1e",
 "last-modified": "Wed, 20 Nov 2019 04:37:29 GMT",
 "opc-content-md5": "1B2M2Y8AsgTpgAmY7PhCfg=="
}
```

#### Specifying the Storage Tier of the Uploaded Object 🔗 
Include the `storage-tier` parameter to assign a storage tier to the object you're uploading.
Command
CopyTry It
```
oci os object put --bucket-name bucket_name --file file_location --storage-tier [Archive | InfrequentAccess | Standard] [OPTIONS]
```

For example, if you're uploading to a Standard tier-configured bucket and you want to assign the object to the InfrequentAccess storage tier, include `--storage-tier InfrequentAccess` in the command:
```
oci os object put --bucket-name MyStandardBucket --file C:\workspace\Uploads\MyDocument.txt --storage-tier InfrequentAccess
{
	"etag": "6b292c1a-b01b-4f36-97c8-4567fb43d071",
	"last-modified": "Sat, 12 Dec 2020 12:58:01 GMT",
	"opc-content-md5": "9P61OSaYe4fXxaeK8siuDw=="
}
```
See [Object Storage Storage Tiers](https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/understandingstoragetiers.htm#storage-tiers "Learn how Object Storage uses storage tiers to help you maximize access performance where appropriate and minimize storage costs where possible.") for more information on how storage tiers work.
If you don't specify a storage tier in the command, the object is automatically assigned and uploaded to the default storage tier of the bucket (Standard or Archive).
#### Naming the Uploaded Object 🔗 
Include the `name` parameter to name the uploaded object excluding its path. This parameter is required if the object is being read from STDIN. For example:
```
oci os object put --bucket-name MyBucket --file C:\workspace\Uploads\MyFile.txt --name AboutMyCompany
{
	"etag": "cadb9f8a-3292-45e6-a1e8-f075699fb619",
	"last-modified": "Fri, 11 Dec 2020 14:04:19 GMT",
	"opc-content-md5": "9P61OSaYe4fXxaeK8siuDw=="
}
```

If you don't include the `name` parameter, the file name is used as the uploaded object's name (if not being read from STDIN)
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [PutObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/PutObject) operation to upload an object to a bucket.
Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API:
```
/n/object_storage_namespace/b/bucket/o/object_name
```

The object name is everything after the `/o/`, which could include hierarchy levels and prefix strings. 


Was this article helpful?
YesNo

