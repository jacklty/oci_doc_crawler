Updated 2024-01-18
# Enabling Versioning During Bucket Creation
On Compute Cloud@Customer, you can enable object versioning during bucket creation using the CLI and API.
Object versioning provides data protection against accidental or malicious object updates and deletions.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/enabling-versoining-during-bucket-creation.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/enabling-versoining-during-bucket-creation.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/enabling-versoining-during-bucket-creation.htm)


  * This task isn't available in the Console.
  * Use the [oci os bucket create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/create.html) command and required parameters to enable object versioning during bucket creation.
Copy
```
oci os bucket create --namespace-name <object_storage_namespace> --compartment-id <target_compartment_id> --name <bucket_name> --versioning enabled [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/CreateBucket) operation to enable object versioning during bucket creation.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

