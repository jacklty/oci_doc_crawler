Updated 2024-01-18
# Enabling or Suspending Versioning
On Compute Cloud@Customer, object versioning provides data protection against accidental or malicious object updates and deletions.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/enabling-or-suspending-versioning.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/enabling-or-suspending-versioning.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/enabling-or-suspending-versioning.htm)


  * This task isn't available in the Console.
  * Use the [oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command and required parameters to enable or suspend versioning.
For the `--versioning` option, choose one of these values: `Enabled` or `Suspended`.
Copy
```
oci os bucket update --namespace-name <object_storage_namespace> --compartment-id <target_compartment_id> --bucket-name <bucket_name> --versioning <enabled | suspended> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/UpdateBucket) operation to enable or suspend versioning.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

