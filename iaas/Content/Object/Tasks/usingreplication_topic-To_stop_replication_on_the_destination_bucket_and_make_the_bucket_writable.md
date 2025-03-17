Updated 2025-01-22
# Stopping Replication to the Object Storage Destination Bucket
Stop replication to the Object Storage destination bucket and make the bucket writable.
**Note**
If you stop replication, the policy is removed from the destination bucket and can't be recovered. The bucket reverts to a standard read/write bucket and is no longer a replication target.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_stop_replication_on_the_destination_bucket_and_make_the_bucket_writable.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_stop_replication_on_the_destination_bucket_and_make_the_bucket_writable.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_stop_replication_on_the_destination_bucket_and_make_the_bucket_writable.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Replication Policy**.
    3. From the **Actions** menu for the replication policy you want, select **Stop Replication**.
    4. When prompted, confirm stopping the replication.
The **Replication Policy** list no longer has an entry. The **Create Policy** button reappears. The bucket reverts to being read/write.
  * Use the [oci os replication make-bucket-writable](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/make-bucket-writable.html) command and required parameters to stop replication to the Object Storage destination bucket and make the bucket writable.
Command
CopyTry It
```
oci os replication make-bucket-writable --bucket-name bucket_name [OPTIONS]
```

If you're replicating to a destination bucket in a different region, include the `region` parameter and the region identifier. For example:
```
oci os replication make-bucket-writable --bucket-name MyDestinationBucket --region us-ashburn-1
```

If the command is successful, you're returned to the prompt.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [MakeBucketWritable](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Replication/MakeBucketWritable) operation to stop replication to the Object Storage destination bucket and make the bucket writable.


Was this article helpful?
YesNo

