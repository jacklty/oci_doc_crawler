Updated 2024-08-06
# Creating a Folder or Subfolder
On Compute Cloud@Customer, you can create a folder in a bucket or you can create a subfolder in an existing folder or subfolder using the CLI and API.
Avoid entering confidential information in names and tags.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-folder-or-subfolder.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-folder-or-subfolder.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/creating-a-folder-or-subfolder.htm)


  * This task isn't available in the Console. 
  * Use the [oci os object put](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/put.html) command and required parameters to create a folder in a bucket or a subfolder in an existing folder or subfolder.
Syntax:
Copy
```
oci os object put --namespace-name<object_storage_namespace>--bucket-name<bucket_name>--file<file_location>--name<object_name>[OPTIONS]
```

Example:
```
oci os object put --namespace-name examplenamespace --bucket-name Bucket1_objv-enabl --file /home/log_files/install.log --name /home/log_files/install.log
```
```
oci os object put --namespace-name examplenamespace --bucket-name Bucket1_objv-enabl --file myfile --name /home/log_files/install.log
```
```
oci os object put --namespace-name examplenamespace --bucket-name Bucket1_objv-enabl --file /home/log_files/install.log --name /home/log_files/install.log Uploading object [####################################] 100% { "etag": "bae04836d4ea5d521c23cbee70566cf2", "last-modified": "2021-05-13T15:37:18.000Z", "opc-content-md5": "GWZbZ8CXPCjLcPxBs6cPCQ==" }
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [PutObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/PutObject) operation to create a folder in a bucket or a subfolder in an existing folder or subfolder.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

