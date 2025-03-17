Updated 2023-12-13
# Synchronizing Object Storage Objects
Synchronize a file system directory with objects in a bucket. 
Synchronization traverses the directories and sub-directories of the specified file system, and copying new and modified files or objects from the source to the destination and optionally deleting those that aren't present in the source.
## Using the CLI 🔗 
Use the [oci os object sync](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/sync.html) command and required parameters to synchronize the objects in a file system and a bucket:
Command
CopyTry It
```
oci os object sync --bucket-name bucket_name [OPTIONS]
```

Use the **Optional Parameters** listed in the [oci os object sync](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/sync.html) page to specify the criteria for when objects need to be synchronized.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
Was this article helpful?
YesNo

