Updated 2024-01-18
# Moving a File System to a Different Compartment
On Compute Cloud@Customer, you can move a file system to another compartment using the CLI or API.
The file system is moved immediately. Moving a file system doesn't affect mounted instances. 
For information about moving resources between compartments, see [Moving Resources to a Different Compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/moving-a-file-system-to-a-different-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/moving-a-file-system-to-a-different-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/file/moving-a-file-system-to-a-different-compartment.htm)


  * This task isn't available in the Console.
  * Use the [oci fs file-system change-compartment](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/fs/file-system/change-compartment.html) command and required parameters to move a file system and its associated snapshots into a different compartment within the same tenancy. 
Copy
```
oci fs file-system change-compartment --file-system-id <file-system_OCID> --compartment-id <destination_compartment_OCID> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ChangeFileSystemCompartment](https://docs.oracle.com/iaas/api/#/en/filestorage/latest/FileSystem/ChangeFileSystemCompartment) operation to move a file system and its associated snapshots into a different compartment within the same tenancy.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

