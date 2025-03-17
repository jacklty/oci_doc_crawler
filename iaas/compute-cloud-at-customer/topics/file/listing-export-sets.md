Updated 2024-08-06
# Listing Export Sets
On Compute Cloud@Customer, you can list File System export sets using the CLI and API.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-export-sets.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-export-sets.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/listing-export-sets.htm)


  * This task isn't available in the Console.
  * Use the [oci fs export-set list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/export-set/list.html) command and required parameters to list the export set resources in the specified compartment.
Copy
```
oci fs export-set list --availability-domain <availability_domain_name> --compartment-id <compartment_id> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
**Procedure**
    1. Get the compartment where you want to list export sets (`oci iam compartment list`)
    2. Run the command.
Example:
```
oci fs export-set list --availability-domain AD-1 \
--compartment-id ocid1.compartment.uniqueID
{
 "data": [
  {
   "availability-domain": "AD-1",
   "compartment-id": "ocid1.compartment.uniqueID",
   "display-name": "MyMountTarget2 - export set",
   "id": "ocid1.exportset.uniqueID",
   "lifecycle-state": "ACTIVE",
   "time-created": "2021-06-17T19:01:37+00:00",
   "vcn-id": "ocid1.vcn.uniqueID"
  }
 ]
}
```

  * Use the [ListExportSets](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/ExportSetSummary/ListExportSets) operation to list the export set resources in the specified compartment.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

