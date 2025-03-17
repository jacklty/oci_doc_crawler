Updated 2024-01-18
# Listing Exports
On Compute Cloud@Customer, you can list File System exports.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-exports.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-exports.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-exports.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **File Storage** , then click **Mount Targets**.
    2. At the top of the page, select the compartment that contains the mount targets.
    3. Click the mount target name.
The exports are displayed at the bottom of the page.
    4. To see the export details, click the export name.
  * Use the [oci fs export list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export/list.html) command and required parameters to list exports for the specified compartment.
Copy
```
oci fs export list --compartment-id <compartment_id> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListExports](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/ExportSummary/ListExports) operation to list exports for the specified compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

