Updated 2024-01-18
# Viewing Retention Rules and Details
On Compute Cloud@Customer, you can view Object Storage retention rules and details.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-retention-rules-and-details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-retention-rules-and-details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/viewing-retention-rules-and-details.htm)


  * This task isn't available in the Console. 
  * Use the [oci os retention-rule list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/list.html) command and required parameters to list retention rules.
Copy
```
oci os retention-rule list --namespace-name <object_storage_namespace> --bucket-name <bucket_name> [OPTIONS]
```

Use the [oci os retention-rule get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/get.html) command and required parameters to see the details for a retention rule.
Copy
```
oci os retention-rule get --namespace-name <object_storage_namespace> --bucket-name <bucket_name> 
--retention-rule-id <retention_rule_identifier> [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListRetentionRules](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/ListRetentionRules) operation to list retention rules.
Use the [GetRetentionRule](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/GetRetentionRule) operation to get the details for a retention rule.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

