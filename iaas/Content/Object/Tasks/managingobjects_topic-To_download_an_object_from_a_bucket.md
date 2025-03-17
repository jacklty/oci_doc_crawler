Updated 2025-01-22
# Downloading an Object Storage Object
Download an object from an Object Storage bucket or folder to your computer.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_download_an_object_from_a_bucket.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Objects**.
    3. From the **Actions** menu for the object you want, select **Download**.
The **Download Object** dialog box appears while the object is downloading, and displays the download status.
  * Use the [oci os object get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/get.html) command and required parameters to download an object from a bucket:
Command
CopyTry It
```
oci os object get --bucket-name bucket_name --name object_name --file file_location [OPTIONS]
```

where `file_location` is the destination path for the file being downloaded, such as `C:\workspace\Downloads\MyFile.txt` or `/home/user/Documents/Downloads/MyFile.txt`. 
For example:
```
oci os object get --bucket-name MyBucket --name MyFile.txt --file c:\workspace\Downloads\MyFile.txt
```

No information is returned when you run the command. The file is downloaded to the specified destination.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/GetObject) operation to download an object from a bucket.
Object Storage prepends the Object Storage namespace string and bucket name to the object name when constructing a URL for use with the API: 
```
/n/object_storage_namespace/b/bucket/o/object_name
```

The object name is everything after the `/o/`, which could include hierarchy levels and prefix strings.


Was this article helpful?
YesNo

