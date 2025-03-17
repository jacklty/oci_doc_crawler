Updated 2024-01-18
# Deleting a Retention Rule
On Compute Cloud@Customer, you can delete Object Storage retention rules.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-a-retention-rule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-a-retention-rule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-a-retention-rule.htm)


  * This task isn't available in the Console. 
  * Use the [oci os retention-rule delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/delete.html) command and required parameters to delete a retention rule.
Copy
```
oci os retention-rule delete --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --retention-rule-id <retention_rule_identifier> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteRetentionRule](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/DeleteRetentionRule) operation to delete a retention rule.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

