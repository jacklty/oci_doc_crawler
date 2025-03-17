Updated 2024-01-18
# Modifying a Retention Rule
On Compute Cloud@Customer, you can modify Object Storage retention rules.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/modifying-a-retention-rule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/modifying-a-retention-rule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/modifying-a-retention-rule.htm)


  * This task isn't available in the Console.
  * Use the [oci os retention-rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/update.html) command and required parameters to update a retention rule.
Syntax:
Copy
```
oci os retention-rule update --namespace-name <object_storage_namespace> --bucket-name <bucket_name> --retention-rule-id <retention_rule_id>
     
```

Followed by the retention rule item that you plan to change:
```
--time-amount <time_integer> --time-unit <days|years>
```

Example:
```
oci os retention-rule update \
--namespace-name examplenamespace \
--bucket-name MyBucket \
--retention-rule-id 344a9c205187408699b51c7769dc1bb4 \
--time-amount 60 \
--time-unit days 
{
 "data": {
  "display-name": "TempHold",
  "duration": {
   "time-amount": 60,
   "time-unit": "DAYS"
  },
  "etag": "344a9c205187408699b51c7769dc1bb4",
  "id": "344a9c205187408699b51c7769dc1bb4",
  "time-created": "2021-06-10T22:17:50+00:00",
  "time-modified": "2021-06-10T22:45:16+00:00",
  "time-rule-locked": null
 }
}
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateRetentionRule](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/UpdateRetentionRule) operation to update a retention rule.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

