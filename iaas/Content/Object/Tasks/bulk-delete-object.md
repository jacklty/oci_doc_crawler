Updated 2023-12-13
# Bulk Deleting Object Storage Objects
Delete a group of objects in a bucket or folder.
## Using the CLI 🔗 
Use the [oci os object bulk-delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-delete.html) command and required parameters to delete a group of objects from a bucket:
Command
CopyTry It
```
oci os object bulk-delete --bucket-name bucket_name
```

For example:
```
oci os object bulk-delete --bucket-name MyBucket
WARNING: This command will delete 2 objects. Are you sure you wish to continue? [y/N]:
Deleted MyRenamedFile.txt [####################################] 100%
Deleted logFile.log [####################################] 100%
{
 "delete-failures": {},
 "deleted-objects": [
  "MyRenamedFile.txt",
  "logFile.log"
 ]
}
```

By default, all objects in the bucket are deleted. Use the **Optional Parameters** listed in the [oci os object bulk-download](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-download.html) page to specify what files in bulk to delete.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
Was this article helpful?
YesNo

