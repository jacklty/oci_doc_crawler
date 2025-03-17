Updated 2024-01-18
# Deleting a File System
On Compute Cloud@Customer, you can delete a file system that doesn't have any dependencies.
**Caution**
You can't undo this operation. Any data in a file system is permanently deleted with the file system. You can't recover a deleted file system or its snapshots. 
A file system that has an export can't be deleted. To delete the export, see [Deleting an Export](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-an-export.htm#deleting-an-export "On Compute Cloud@Customer, deleting an export deletes the file system path that clients use to mount the file system. Deleting an export does not delete any file systems.").
You can't delete file systems that have dependencies. For example, if you have created a snapshot of this file system and then created a new file system from the snapshot, you can't delete the source file system. 
For more information, see [Deleting File System Resources Overview](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/file-storage.htm#deleting-file-system-resources-overview "On Compute Cloud@Customer, you can't delete a file system resource that has dependencies.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-a-file-system.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-a-file-system.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-a-file-system.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. At the top of the page, select the compartment that contains the file system.
    3. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the file system and select **Delete**.
    4. Confirm the deletion.
  * Use the [oci fs file-system delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/delete.html) command and required parameters to delete the specified file system. Before you delete the file system, verify that no remaining export resources still reference it.
Copy
```
oci fs file-system delete --file-system-id<file-system_OCID>[OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/DeleteFileSystem) operation to delete the specified file system. Before you delete the file system, verify that no remaining export resources still reference it.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

