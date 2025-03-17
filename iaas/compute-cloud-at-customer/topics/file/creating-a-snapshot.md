Updated 2024-01-18
# Creating a Snapshot
On Compute Cloud@Customer, You can create a snapshot of a file system. A snapshot is a point-in-time view of the file system. The snapshot is accessible at `.zfs/snapshot/` name.
Avoid entering confidential information.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-snapshot.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-snapshot.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-snapshot.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. At the top of the page, select the compartment that contains the file system for which you want to create a snapshot.
    3. Click the file system name.
    4. Under **Resources** , click **Snapshots**.
    5. Click **Create Snapshot**.
    6. Enter a name for the snapshot.
The name is limited to 64 characters and it must be unique among all other snapshots for this file system. The name can't be changed. Avoid entering confidential information.
    7. Click **Create Snapshot**.
The snapshot is accessible under the root directory of the file system at ``.zfs/snapshot/`name`.
  * Use the [oci fs snapshot create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/snapshot/create.html)oci_fs_snapshot_create command and required parameters to create a new snapshot of the specified file system.
Copy
```
oci fs snapshot create --file-system-id <file-system_OCID> --name <snapshot_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateSnapshot](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Snapshot/CreateSnapshot) operation to create a new snapshot of the specified file system.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

