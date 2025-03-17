Updated 2024-01-18
# Setting NFS Export Options
On Compute Cloud@Customer, when you create a file system and export, the NFS export options for that file system are set to the defaults. The default values allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access.
**Caution**
If a file system is mounted by any clients, creating, deleting, or editing the Source value can disrupt file system I/O operations.
Export Option in the Compute Cloud@Customer Console | Export Option in the CLI | Default Value | Description  
---|---|---|---  
**Source:** |  `source` |  0.0.0.0/0 |  The IP address or CIDR block of a connecting NFS client.   
**Ports:** |  `require-privileged-source-port` |  Any |  Always set to:
  * UI: Any
  * CLI: `false`

  
**Access:** |  `access` |  Read/Write |  Specifies the source NFS client access. Can be set to one of these values:
  * `READ_WRITE`
  * `READ_ONLY`

  
**Squash:** |  `identity-squash` |  None |  Determines whether the clients accessing the file system as root have their User ID (UID) and Group ID (GID) remapped to the squash UID/GID. Possible values:
  * Root – Only the root user is remapped.
  * None – No users are remapped.

  
**Squash UID/GID:** |  `anonymous-uid` and `anonymous-gid` |  65534 |  This setting is used along with the Squash option. When remapping a root user, you can use this setting to change the default anonymousUid and anonymousGid to any user ID of your choice.  
**Note** – If you change the RW/RO permissions of an export option for an SMB share, the changes are only enforced for newly network-mapped drives of that share. Any previously mapped drives of the same share retain the original permissions. To have the changed permissions enforced on previously mapped drives on SMB clients, disconnect the shares and map them again. 
For more information about configuring the options to suit various access scenarios, see [Export Options for File Storage](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/export-options-for-file-storage.htm#export-options-for-file-storage "On Compute Cloud@Customer, NFS export options enable you to create more granular access control than is possible using security list rules to limit VCN access. You can use NFS export options to specify access levels for IP addresses or CIDR blocks connecting to file systems through exports in a mount target. Access can be restricted so that each client’s file system is inaccessible and invisible to the other, providing better security controls in multitenant environments.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. At the top of the page, select the compartment that contains the file system.
    3. Click the file system name.
    4. Under **Resources** , select **Exports**.
    5. Click the export's export path.
The NFS Export Options are displayed.
    6. Click **Edit Options**.
    7. In the **NFS Export Options** dialog box, configure the NFS options.
    8. Click **Update Options**.
  * Use the [oci fs export update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/update.html) command and required parameters to update the export information.
Copy
```
oci fs export update --export-id <export_id> --export-options <file://json_file or json_string> [OPTIONS]
```

**Note** – The `require-privileged-source-port` option can only be set to `false`.
For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateExport](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Export/UpdateExport) operation to update the export information.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

