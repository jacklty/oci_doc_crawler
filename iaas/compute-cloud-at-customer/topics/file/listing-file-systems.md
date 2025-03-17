Updated 2024-08-06
# Listing File Systems
On Compute Cloud@Customer, file systems are associated with a single compartment. When you select a compartment, the Compute Cloud@Customer Console displays all file systems in the compartment. You can also see exports and snapshots associated with each file system. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-file-systems.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-file-systems.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-file-systems.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **File Systems**.
    2. At the top of the page, select the compartment that contains the file system.
The file systems for the compartment are listed.
    3. To see file system details, click the name of the file system.
  * Use the [oci fs file-system list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/list.html) command and required parameters to list file systems.
Copy
```
oci fs file-system list --availability-domain <availability_domain_name> --compartment-id <compartment_OCID> [OPTIONS]
```

Use the [oci fs file-system get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/get.html) command and required parameters to view file system details.
Copy
```
oci fs file-system get --file-system-id <file-system_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListFileSystems](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystemSummary/ListFileSystems) operation to delete the specified mount target. This operation also deletes the mount target’s VNICs.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

