Updated 2024-01-18
# Deleting an Export
On Compute Cloud@Customer, deleting an export deletes the file system path that clients use to mount the file system. Deleting an export does not delete any file systems.
**Caution**
When you delete an export, you can no longer mount the file system using the file path specified in the deleted export. Any clients that use the export path to mount a file system will not be able to access the file system.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-an-export.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-an-export.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-an-export.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. At the top of the page, select the compartment that contains the file system with the export you plan to delete.
    3. Click the name of a file system that uses the export you plan to delete.
    4. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the export, then click **Delete**.
    5. Confirm the deletion.
  * Use the [oci fs export delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/delete.html) command and required parameters to delete the specified export.
Copy
```
oci fs export delete --export-id <export_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteExport](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Export/DeleteExport) operation to delete the specified export.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

