Updated 2024-01-18
# Downloading an Object
On Compute Cloud@Customer, you can download an object using the CLI and API.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/downloading-an-object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/downloading-an-object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/downloading-an-object.htm)


  * This task isn't available in the Console.
  * Use the [oci os object get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/get.html) command and required parameters to download an object.
Syntax:
Copy
```
oci os object get --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --name<object_name> --file<file_location> [OPTIONS]
```

<file_location> is the destination path for the file being downloaded, such as `C:\workspace\Downloads\MyFile.txt` or `/home/user/Documents/Downloads/MyFile.txt`. 
Example:
```
oci os object get \
--namespace-name examplenamespace \
--bucket-name MyBucket \
--name photos \
--file /home/photos_backup
Downloading object [#-----------------------------------] 100%
# ls -l
total 8
-rw-r--r-- 1 root root 1363 Jun 1 17:56 photo1
-rw-r--r-- 1 root root 1363 Jun 1 21:40 photo1_backup
-rw-r--r-- 1 root root 0 Jun 1 20:42 photo2
-rw-r--r-- 1 root root 0 Jun 1 20:42 photo3
-rw-r--r-- 1 root root 0 Jun 1 20:42 photo4
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [GetObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/GetObject) operation to download an object.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

