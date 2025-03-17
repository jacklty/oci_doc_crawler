Updated 2024-01-18
# Copying an Object to a Different Bucket
On Compute Cloud@Customer, you can copy an object to a different bucket as long as the target bucket is located in the same Compute Cloud@Customer infrastructure.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/copying-an-object-to-a-different-bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/copying-an-object-to-a-different-bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/copying-an-object-to-a-different-bucket.htm)


  * This task isn't available in the Console. 
  * Use the [oci os object copy](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/object/copy.html) command and required parameters to copy an object to a different bucket.
Copy
```
oci os object copy --namespace-name <object_storage_namespace> --bucket-name <source_bucket_name> --source-object-name <source_object> --destination-bucket <destination_bucket_name> --destination-object-name <destination_object_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CopyObject](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Object/CopyObject) operation to copy an object to a different bucket.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

