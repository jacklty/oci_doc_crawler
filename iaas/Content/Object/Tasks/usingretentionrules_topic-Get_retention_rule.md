Updated 2025-01-22
# Getting an Object Storage Retention Rule's Details
View a retention rule's details for an Object Storage bucket.
You can get the retention rule's ID by running the list command. See [Listing Retention Rules](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm#top "View a list of the retention rules for an Object Storage bucket.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-Get_retention_rule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-Get_retention_rule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-Get_retention_rule.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Retention Rules**.
    3. From the **Actions** menu for the retention rule you want, select **View Details**. 
The **Retention Rules Details** dialog box opens.You can view the details for the retention rule, such as its retention duration lock state, scheduled lock time, and when it was last modified.
  * Use the [oci os retention-rule list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/list.html) command and required parameters to get the details of a retention rule for a bucket:
Command
CopyTry It
```
oci os retention-rule get --bucket-name bucket_name --retention-rule-id retention_rule_id [OPTIONS]
```

For example:
```
oci os retention-rule get --bucket-name MyBucket --retention-rule-id b1a6c84c-57c4-416c-b006-f864b0904c9e
{
 "data": {
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
 "etag": "c05f02d3-d2b5-4378-9fcb-3a92ba0e018f"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetRetentionRule](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/GetRetentionRule) operation get the details of a retention rule for a bucket.


Was this article helpful?
YesNo

