Updated 2024-08-06
# Creating a File System Clone
On Compute Cloud@Customer, you can create a file system clone by cloning the file system snapshot.
**Prerequisite**
A snapshot of the file system must exist. See [Creating a Snapshot](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-snapshot.htm#creating-a-snapshot "On Compute Cloud@Customer, You can create a snapshot of a file system. A snapshot is a point-in-time view of the file system. The snapshot is accessible at .zfs/snapshot/ name.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system-clone.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system-clone.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system-clone.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. At the top of the page, select the compartment that contains the file system you want to clone.
    3. Click the name of the file system that you want to clone.
    4. Under **Resources** , click **Snapshots**.
    5. For the snapshot that you want to clone, Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), and click **Clone**.
    6. In the **Clone Snapshot from File System** dialog box, provide the following information:
       * **Name** : Enter a name for the clone. Avoid entering confidential information.
       * **Create in Compartment** : Select the compartment where you want to create the clone.
       * **Tagging:** (Optional) Add one or more tags to this resource. Tags can also be applied later. For more information about tagging resources, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
    7. Click **Create File System**.
The clone is created and the details page of the new file system clone is displayed.
In the **Clones** section of the file system clone details page, **Clone Parent** is false and **Clone Root** is false. The name of the **Parent File System** is shown and is clickable, and the name of the **Source Snapshot** is shown and is clickable.
If you click the name of the parent file system, the **Clones** section of the details page of that parent file system shows **Clone Parent** is true, and **Parent File System** and **Source Snapshot** have no values.
  * Use the [oci fs file-system create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/create.html) command and required parameters to create a file system clone of a file system snapshot.
Copy
```
oci fs file-system create --availability-domain <availability_domain_name> --compartment-id <compartment_id> --display-name <fs_clone_display_name> --source-snapshot-id <fs_snapshot_id> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/CreateFileSystem) operation to create a file system clone of a file system snapshot.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

