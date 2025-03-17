Updated 2024-08-06
# Updating a File System
On Compute Cloud@Customer, you can change some file system parameters. 
You can change the file system name and quota. You can't change the database record size or the backing store pool type assignment (default or high performance).
To reduce the quota for the file system, first check the current file system usage. The quota can't be set smaller than the current usage. Current usage includes the data in the file system and all snapshots created under the file system. To check the current usage, check the value of **Metered Bytes** on the file system details page using the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") or `metered-bytes` in the file system `get` output using the CLI.
**Note**
The **Metered Bytes** value can take up to 15 minutes to refresh on a system with active I/O.
Fifteen minutes after setting a lower quota, compare the quota and metered bytes values for the file system. Check the value of quota in the `OraclePCA` defined tag on the Tags tab on the file system details page in the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") or in `defined-tags` in the file system `get` output in the CLI. If the quota is less than metered bytes, then the quota isn't enforced and you should set a higher quota.
Avoid entering confidential information.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/updating-a-file-system.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/updating-a-file-system.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/updating-a-file-system.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. At the top of the page, select the compartment that contains the file system.
    3. For the file system you want to update, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    4. Enter a new name in the name field, or enter a new quota in the `OraclePCA`:quota defined tag as described in [Creating a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm#creating-a-file-system "On Compute Cloud@Customer, you can create a shared file system using the File Storage service."). 
    5. Click **Save Changes**.
  * Use the [oci fs file-system update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/update.html) command and required parameters to update the specified file system’s information. You can use this operation to rename a file system.
Copy
```
oci fs file-system update --file-system-id <file_system_OCID> --display-name <new_file-system_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Get the OCID of the file system that you want to update:`oci fs             file-system list`
    2. Specify a new name for the file system, or set a new quota in the `OraclePCA`:quota defined tag as described in [Creating a File System](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-a-file-system.htm#creating-a-file-system "On Compute Cloud@Customer, you can create a shared file system using the File Storage service."). 
    3. Run the update file system command.
Example:
Copy
```
oci fs file-system update --file-system-id ocid1.filesystem.unique_ID --defined-tags '{"OraclePCA":{"quota":500000}}'
```

  * Use the [UpdateFileSystem](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/UpdateFileSystem) operation to update the specified file system’s information. You can use this operation to rename a file system.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

