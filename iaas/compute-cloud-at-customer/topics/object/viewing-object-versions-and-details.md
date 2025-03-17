Updated 2024-01-18
# Viewing Object Versions and Details
On Compute Cloud@Customer, you can list object versions and details using the CLI and API.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-object-versions-and-details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-object-versions-and-details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-object-versions-and-details.htm)


  * This task isn't available in the Console.
  * Use the [oci os object list-object-versions](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/list-object-versions.html) command and required parameters to list the object versions in a bucket.
Copy
```
oci os object list-object-versions --namespace-name <object_storage_namespace> --bucket-name <bucket_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListObjectVersion](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/ListObjectVersions) operation to list the object versions in a bucket.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

