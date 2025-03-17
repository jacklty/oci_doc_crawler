Updated 2024-01-18
# Performing a Bulk Download
On Compute Cloud@Customer, you can download objects in bulk.
## Using the CLI 🔗 
Use the [oci os object copy](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/copy.html) command and required parameters to perform a bulk download.
Copy
```
oci os object bulk-download 
--namespace-name ** _<object_storage_namespace>_**
--bucket-name **_<bucket_name>_** 
--download-dir **_<download_directory_location>_** [OPTIONS]
```

The download directory (<download_directory_location>) is the destination path for the objects being downloaded, such as `C:\workspace\Downloads\` or `/home/user/Documents/Downloads/`. If the directory does not exist, Object Storage creates the directory when the command runs.
Example:
```
oci os object bulk-download  \
--namespace-name examplenamespace \
--bucket-name MyBucket  \
--download-dir c:\workspace\Downloads
Downloaded MyFile.txt [####################################] 100%
Downloaded logFile.log [####################################] 100%
{
 "download-failures": {},
 "skipped-objects": []
}

```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
Was this article helpful?
YesNo

