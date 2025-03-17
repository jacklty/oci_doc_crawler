Updated 2025-01-22
# Listing Object Storage Retention Rules
View a list of the retention rules for an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Retention Rules**.
The **Retention Rules** list opens. All retention rules in the selected bucket are displayed in a table.
  * Use the [oci os retention-rule list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/list.html) command and required parameters to list the retention rules for a bucket:
Command
CopyTry It
```
oci os retention-rule list --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os retention-rule list --bucket-name MyBucket
{
 "data": {
  "items": [
   {
    "display-name": "RegulatoryCompliance",
    "duration": {
     "time-amount": 5,
     "time-unit": "YEARS"
    },
    "etag": "c05f02d3-d2b5-4378-9fcb-3a92ba0e018f",
    "id": "b1a6c84c-57c4-416c-b006-f864b0904c9e",
    "time-created": "2020-03-25T15:11:44.423000+00:00",
    "time-modified": "2020-03-25T15:11:44.423000+00:00",
    "time-rule-locked": "2020-04-28T00:00:00+00:00"
   },
   {
    "display-name": "DataGovernance",
    "duration": {
     "time-amount": 5,
     "time-unit": "DAYS"
    },
    "etag": "efb9178f-4213-49f7-878d-7bbe57decc0b",
    "id": "89f4ca0c-4ad9-4fa5-8005-95e7741c531c",
    "time-created": "2020-03-25T15:08:01.601000+00:00",
    "time-modified": "2020-03-25T15:08:01.601000+00:00",
    "time-rule-locked": null
   },
   {
    "display-name": "LegalHold",
    "duration": null,
    "etag": "7f51ef6c-3fca-48f7-9060-c129911c1a50",
    "id": "5772c87f-6723-4ecc-b44c-bef86643be92",
    "time-created": "2020-03-25T14:53:20.792000+00:00",
    "time-modified": "2020-03-25T14:53:20.792000+00:00",
    "time-rule-locked": null
   }
  ]
 }
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListRetentionRules](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/ListRetentionRules) operation to list the retention rules for a bucket.


Was this article helpful?
YesNo

