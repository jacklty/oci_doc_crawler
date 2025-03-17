Updated 2025-01-30
# Editing an Object Storage Retention Rule
Update a retention rule for an Object Storage bucket.
You can get the retention rule's ID by running the list command. See [Listing Object Storage Retention Rules](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm#top "View a list of the retention rules for an Object Storage bucket.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_edit_a_retention_rule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_edit_a_retention_rule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_edit_a_retention_rule.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Retention Rules**.
    3. From the **Actions** menu for the retention rule you want, select **Edit**. 
    4. Update the settings as needed. Avoid entering confidential information. For descriptions of the settings, see [Creating a Retention Rule](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_create_a_retention_rule.htm#top "Create a retention rule for an Object Storage bucket.").
    5. Select **Save Changes**.
  * Use the [oci os retention-rule update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/update.html) command and required parameters to edit a retention rule for a bucket:
Command
CopyTry It
```
oci os retention-rule update --bucket-name bucket_name --retention-rule-id retention_rule_id [OPTIONS]
```

For example:
```
oci os retention-rule update --bucket-name MyBucket --retention-rule-id b1a6c84c-57c4-416c-b006-f864b0904c9e --time-amount 6 --time-unit years --time-rule-locked "2020-04-30 00:00"
{
 "data": {
  "display-name": "RegulatoryCompliance",
  "duration": {
   "time-amount": 6,
   "time-unit": "YEARS"
  },
  "etag": "700ada5c-6a2a-4c6c-acb6-4ebb173e0f8f",
  "id": "b1a6c84c-57c4-416c-b006-f864b0904c9e",
  "time-created": "2020-03-25T15:11:44.423000+00:00",
  "time-modified": "2020-03-25T15:46:28.724000+00:00",
  "time-rule-locked": "2020-04-30T00:00:00+00:00"
 },
 "etag": "700ada5c-6a2a-4c6c-acb6-4ebb173e0f8f"
}
```

In this example, the retention rule has been updated to include values for `time-amount`, `time-unit`, and `time-rule-locked`.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [UpdateRetentionRule](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/RetentionRule/UpdateRetentionRule) operation to edit a retention rule for a bucket.


Was this article helpful?
YesNo

