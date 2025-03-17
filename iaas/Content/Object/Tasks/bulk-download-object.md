Updated 2023-12-13
# Bulk Downloading Object Storage Objects
Download a group of objects from a bucket to a computer file system.
## Using the CLI 🔗 
Use the [oci os object bulk-download](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-download.html) command and required parameters to download a group of objects from a bucket:
Command
CopyTry It
```
oci os object bulk-download --bucket-name bucket_name --download-dir download_directory_location [OPTIONS]
```

where `download_directory_location` is the destination path for the objects being downloaded, such as `C:\workspace\Downloads\` or `/home/user/Documents/Downloads/`. If the directory doesn't exist, Object Storage creates the directory when you run the command.
For example:
```

oci os object bulk-download --bucket-name MyBucket --download-dir c:\workspace\Downloads
Downloaded MyFile.txt [####################################] 100%
Downloaded logFile.log [####################################] 100%
{
 "download-failures": {},
 "skipped-objects": []
}
```

By default, all objects in the bucket are downloaded. Use the **Optional Parameters** listed in the [oci os object bulk-download](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-download.html) page to specify what files in bulk to download.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
Was this article helpful?
YesNo

