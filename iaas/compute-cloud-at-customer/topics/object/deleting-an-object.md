Updated 2024-01-18
# Deleting an Object
On Compute Cloud@Customer, you can permanently delete an object from a bucket or folder.
**Caution**
You can't recover a deleted object unless you have object versioning enabled. See [Managing Object Versioning](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/managing-object-versioning.htm#managing-object-versioning "On Compute Cloud@Customer, object versioning provides data protection against accidental or malicious object update, overwrite, or deletion.") for details.
You can't delete an object that has an active retention rule. See [Defining Retention Rules](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/defining-retention-rules.htm#defining-retention-rules "On Compute Cloud@Customer, retention rules provide immutable storage options for data written to Object Storage for data governance, regulatory compliance, and legal hold requirements. Retention rules can also protect your data from accidental or malicious writes or deletion. Retention rules can be locked to prevent rule modification and data deletion or modification even by administrators.") for details.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-an-object.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-an-object.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-an-object.htm)


  * This task isn't available in the Console. 
  * Use the [oci os object delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/delete.html) command and required parameters to delete an object or folder.
Copy
```
oci os object delete --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --object-name <object_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/DeleteObject) operation to delete an object or folder.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

