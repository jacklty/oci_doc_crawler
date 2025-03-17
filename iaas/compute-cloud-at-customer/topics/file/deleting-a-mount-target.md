Updated 2024-01-18
# Deleting a Mount Target
On Compute Cloud@Customer, deleting a mount target deletes all the exports that are associated with the mount target.
**Caution**
Deleting the mount target also deletes all of its exports of associated file systems. File systems are no longer available through the deleted mount target. 
**Deleting a mount target has no effect on file system data or file system snapshots.**
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-a-mount-target.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-a-mount-target.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/deleting-a-mount-target.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **Mount Targets**.
    2. At the top of the page, select the compartment that contains the mount target that you want to delete.
    3. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the mount target you plan to delete, then click **Delete**.
    4. Confirm the deletion.
  * Use the [oci fs mount-target delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/mount-target/delete.html) command and required parameters to delete the specified mount target.
Copy
```
ci fs mount-target delete --mount-target-id <mount_target_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteMountTarget](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/MountTarget/DeleteMountTarget) command and required parameters to delete the specified mount target.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

