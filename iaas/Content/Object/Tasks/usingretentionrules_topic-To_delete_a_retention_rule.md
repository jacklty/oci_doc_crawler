Updated 2025-01-22
# Deleting an Object Storage Retention Rule
Delete a retention rule from an Object Storage bucket.
You can get the retention rule's ID by running the list command. See [Listing Object Storage Retention Rules](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_list_retention_rules.htm#top "View a list of the retention rules for an Object Storage bucket.").
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_delete_a_retention_rule.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_delete_a_retention_rule.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingretentionrules_topic-To_delete_a_retention_rule.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Retention Rules**.
    3. From the **Actions** menu for the retention rule you want, select **Delete**. 
    4. When prompted, confirm the deletion.
The retention rule you deleted to longer appears in the **Retention Rules** list.
  * Use the [oci os retention-rule delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/retention-rule/delete.html) command and required parameters to delete a retention rule from a bucket:
Command
CopyTry It
```
oci os retention-rule delete --bucket-name bucket_name --retention-rule-id retention_rule_id [OPTIONS]
```

For example:
```
oci os retention-rule delete --bucket-name MyBucket --retention-rule-id 4ed833b1-fb27-4a40-a8ab-14e09636a724
Are you sure you want to delete this resource? [y/N]: y
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteRetentionRule](https://docs.oracle.com/iaas/api/#23/en/objectstorage/latest/RetentionRule/DeleteRetentionRule) operation to delete a retention rule from a bucket.


Was this article helpful?
YesNo

