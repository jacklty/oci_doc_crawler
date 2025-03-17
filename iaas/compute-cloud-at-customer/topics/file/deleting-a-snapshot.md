Updated 2024-01-18
# Deleting a Snapshot
On Compute Cloud@Customer, you can delete file system snapshots.
There are dependencies between file systems, snapshots, and clones. Compute Cloud@Customer doesn't allow you to delete any resources for which there is a dependency. For details, see [Deleting File System Resources Overview](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/file-storage.htm#deleting-file-system-resources-overview "On Compute Cloud@Customer, you can't delete a file system resource that has dependencies.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-a-snapshot.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-a-snapshot.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-a-snapshot.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. At the top of the page, select the compartment that contains the file system snapshot that you want to delete.
    3. Click the name of the file system where the snapshot resides.
    4. Under **Resources** , click **Snapshots**.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete**.
    6. Confirm the deletion.
  * Use the [oci fs snapshot delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/delete.html) command and required parameters to delete the specified snapshot.
Copy
```
oci fs snapshot delete --snapshot-id <snapshot_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/DeleteSnapshot) operation to delete the specified snapshot.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

