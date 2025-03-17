Updated 2024-02-09
# Checking an Object Storage Object's Restoration Status
Check the status of an Archive Storage object restoration.
## Using the CLI 🔗 
Use the [oci os object restore-status](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/restore-status.html) command and required parameters to get that status of an object being restored from Archive Storage to Object Storage in a bucket:
Command
CopyTry It
```
oci os object restore-status --bucket-name archive_bucket_name --name archived_object_name [OPTIONS]
```

By default, you have 24 hours to download an object after restoration. However, you can include the optional `hours` parameter with an integer value of download time of from 1 to 240 hours. For example:
Command
CopyTry It
```
oci os object restore --bucket-name MyArchiveBucket --name MyArchivedObject --hours 12
```

You need `OBJECT_RESTORE` permissions to restore Archive Storage objects.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
Was this article helpful?
YesNo

