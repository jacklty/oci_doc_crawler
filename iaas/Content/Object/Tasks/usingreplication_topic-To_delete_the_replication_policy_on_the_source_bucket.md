Updated 2025-01-22
# Deleting the Replication Policy from an Object Storage Source Bucket
Delete the replication policy for an Object Storage bucket.
For information about how replication works, see [Using Replication](https://docs.oracle.com/iaas/Content/Object/Tasks/usingreplication.htm).
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_delete_the_replication_policy_on_the_source_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_delete_the_replication_policy_on_the_source_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_delete_the_replication_policy_on_the_source_bucket.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Replication Policy**.
    3. From the **Actions** menu for the replication policy you want, select **Delete**.
    4. When prompted, confirm the deletion.
The **Replication Policy** list no longer has an entry. The **Create Policy** button reappears. The bucket reverts to being read/write.
  * Use the [oci os replication delete-replication-policy](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/delete-replication-policy.html) command and required parameters to delete the replication policy associated with an Object Storage source bucket.
Command
CopyTry It
```
oci os replication delete-replication-policy --bucket-name bucket_name --replication-id replication_policy_id [OPTIONS]
```

For example:
```
oci os replication delete-replication-policy --bucket-name MySourceBucket --replication-id bacb8334-b191-4026-aa65-5e4f5165ae3e
Are you sure you want to delete this resource? [y/N]: y
```

If the command is successful, you're returned to the prompt.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeleteReplicationPolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Replication/DeleteReplicationPolicy) operation to stop replication to delete the replication policy for an Object Storage bucket.


Was this article helpful?
YesNo

