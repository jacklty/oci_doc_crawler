Updated 2023-12-13
# Bulk Deleting an Object Storage Object's Versions
Delete a group of object versions in a Object Storage bucket or folder.
## Using the CLI 🔗 
Use the [oci os object bulk-delete-versions](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-delete-versions.html) command and required parameters to delete all object versions that match the specified criteria in a bucket:
Command
CopyTry It
```
oci os object bulk-delete-versions --bucket-name bucket_name [OPTIONS]
```

By default, all object versions in the bucket are deleted. Use the **Optional Parameters** listed in the [oci os object bulk-delete-versions](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-delete-versions.html) page to specify what object versions in bulk to delete.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
Was this article helpful?
YesNo

