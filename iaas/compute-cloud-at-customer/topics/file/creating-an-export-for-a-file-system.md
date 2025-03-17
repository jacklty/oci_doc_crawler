Updated 2024-08-06
# Creating an Export for a File System
On Compute Cloud@Customer, exports control how NFS clients access file systems when they connect to a mount target. A file system must have at least one export in one mount target for instances to mount the file system. 
**Important**
When exporting file systems to overlapping CIDRs in a VCN, exports to the longest CIDR (smallest network) must be done first. For more information and an example, see My Oracle Support article [PCA File system as a Service Exports (Doc ID 2823994.1)](https://support.oracle.com/epmos/faces/DocContentDisplay?id=2823994.1).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/creating-an-export-for-a-file-system.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. In the left panel, select **File Systems**.
    3. At the top of the page, select the compartment that contains the file system for which you plan to create an export.
    4. Click the name of the file system.
    5. Click **Create Export**.
    6. Enter the required information:
       * **Mount Target** : Select a mount target from the list.
       * **Source CIDR** : Enter the longest CIDR (smallest network) in the CIDR range. Starting with the smallest CIDR range (largest network) will result in an error later in the process, because CIDR ranges larger than existing ones will not be accepted. For example, 10.0.0.0/29 is a longer CIDR than 10.0.0.0/28, so 10.0.0.0/29 must be added first.
    7. Click **Create Export**.
The file system export is created and the export details page is displayed.
    8. In the export details page, make note of the export path. The export path is used to mount the file system on an instance. Example:
![A screen shot showing where the file system export path is listed.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/fs-export2.png)
    9. In the lower panel, review the **NFS Export Options**.
The NFS export options for that file system are set to the default values, which allow full access for all NFS client source connections. These defaults must be changed to restrict access.
    10. Consider your next action:
       * Mount the file system from an NFS client. See [Mounting File Systems on UNIX-based Instances](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/mounting-file-systems-on-uxix-based-instances.htm#mounting-file-systems-on-uxix-based-instances "On Compute Cloud@Customer, instance users of UNIX based operating systems, such as Linux and Oracle Solaris, can use OS commands to mount and access file systems.").
       * Configure NFS options to secure the exported file system. See [Setting NFS Export Options](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/setting-nfs-export-options.htm#setting-nfs-export-options "On Compute Cloud@Customer, when you create a file system and export, the NFS export options for that file system are set to the defaults. The default values allow full access for all NFS client source connections. These defaults must be changed if you want to restrict access.").
  * Use the [oci fs export create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/create.html) command and required parameters to create a new export in the specified export set, path, and file system.
Copy
```
oci fs export create --export-set-id <export_set_OCID> --file-system-id <file_system_OCID> 
--path "</pathname>" [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateExport](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/Export/CreateExport) operation to create a new export in the specified export set, path, and file system.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

