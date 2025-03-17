Updated 2024-01-18
# Moving a Bucket to a Different Compartment
On Compute Cloud@Customer, you can move a bucket from one compartment to another as long as both the source and target compartments are in the same tenancy. This capability includes moving a bucket from one compartment level down to a lower level within the source compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/moving-a-bucket-to-a-different-compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/moving-a-bucket-to-a-different-compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/moving-a-bucket-to-a-different-compartment.htm)


  * This task isn't available in the Console.
  * Use the [oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command and required parameters to move a bucket from one compartment to another within the same tenancy. Supply the compartment Id of the compartment that you want to move the bucket to.
Copy
```
oci os bucket update --namespace-name <object_storage_namespace> --compartment-id <target_compartment_id> --bucket-name <bucket_name> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/UpdateBucket) operation to move a bucket from one compartment to another within the same tenancy. Supply the compartment Id of the compartment that you want to move the bucket to. 
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

