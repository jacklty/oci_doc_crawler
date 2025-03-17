Updated 2024-01-18
# Bulk Deleting All Objects in a Bucket
On Compute Cloud@Customer, you can delete all objects in a bucket using the CLI.
**Caution**
You can't recover a deleted object unless you have object versioning enabled. See [Managing Object Versioning](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/managing-object-versioning.htm#managing-object-versioning "On Compute Cloud@Customer, object versioning provides data protection against accidental or malicious object update, overwrite, or deletion.") for details.
You can't delete an object that has an active retention rule. See [Defining Retention Rules](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/defining-retention-rules.htm#defining-retention-rules "On Compute Cloud@Customer, retention rules provide immutable storage options for data written to Object Storage for data governance, regulatory compliance, and legal hold requirements. Retention rules can also protect your data from accidental or malicious writes or deletion. Retention rules can be locked to prevent rule modification and data deletion or modification even by administrators.") for details.
## Using the CLI 🔗 
Use the [oci os object bulk-delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/bulk-delete.html) command and required parameters to delete an object or folder.
To see a list of the files impacted by a bulk delete command without actually deleting the files, use the `--dry-run` option. Perform the command without the `--dry-run` option to bulk delete all objects in the bucket.
```
oci os object bulk-delete --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --dry-run
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
Was this article helpful?
YesNo

