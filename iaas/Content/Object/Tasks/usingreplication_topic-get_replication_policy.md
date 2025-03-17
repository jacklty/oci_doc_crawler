Updated 2025-01-22
# Getting a Replication Policy's Details
View the details of the replication policy for an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-get_replication_policy.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Replication Policy**.
The **Replication Policy** list displays the details of the replication policy, including its destination region, destination bucket, and the time of the last replication.
  * Use the [oci os replication get-replication-policy](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/get-replication-policy.html) command and required parameters to get the details of a replication policy for an Object Storage bucket:
Command
CopyTry It
```
oci os replication get-replication-policy --bucket-name bucket_name --replication-id replication_policy_id [OPTIONS]
```

For example:
```
oci os replication get-replication-policy --bucket-name MySourceBucket --replication-id bacb8334-b191-4026-aa65-5e4f5165ae3e
{
 "data": {
  "destination-bucket": "MyDestinationBucket",
  "destination-region": "us-ashburn-1",
  "id": "bacb8334-b191-4026-aa65-5e4f5165ae3e",
  "name": "MyReplicationPolicy",
  "status": "ACTIVE",
  "status-message": "The policy is active.",
  "time-created": "2020-02-06T16:44:10+00:00",
  "time-last-sync": "2020-02-06T16:49:40+00:00"
 }
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetReplicationPolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Replication/GetReplicationPolicy) operation to get the details of a replication policy for an Object Storage bucket:


Was this article helpful?
YesNo

