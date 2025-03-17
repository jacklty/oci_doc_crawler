Updated 2024-01-18
# Listing Snapshots
On Compute Cloud@Customer, you can list snapshots and view snapshot details.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-snapshots.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-snapshots.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-snapshots.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. At the top of the page, select the compartment that contains the file system with the snapshot.
    3. Click the file system name.
    4. Under **Resources** , click **Snapshots**.
The file system snapshots are listed.
    5. To get the details for a specific snapshot, click the snapshot name.
  * Use the [oci fs snapshot list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/list.html) command and required parameters to list snapshots of the specified file system.
Copy
```
oci fs snapshot list --file-system-id <file-system_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListSnapshots](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/SnapshotSummary/ListSnapshots) operation to list snapshots of the specified file system.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

