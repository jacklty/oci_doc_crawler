Updated 2025-01-22
# Listing the Object Storage Replication Policy
View a list the replication policy for an Object Storage bucket.
**Note**
There's a maximum of one replication policy per bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_list_replication_policies.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_list_replication_policies.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_list_replication_policies.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Replication Policy**.
The **Replication Policies** list opens. All replication policies in the selected bucket are displayed in a table.
  * Use the [oci os replication list-replication-policies](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/list-replication-policies.html) command and required parameters to list the replication policies for a bucket:
Command
CopyTry It
```
oci os replication list-replication-policies --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os replication list-replication-policies --bucket-name MySourceBucket
{
 "data": [
  {
   "destination-bucket": "MyDestinationBucket",
   "destination-region": "us-ashburn-1",
   "id": "bacb8334-b191-4026-aa65-5e4f5165ae3e",
   "name": "MyReplicationPolicy",
   "status": "ACTIVE",
   "status-message": "The policy is active.",
   "time-created": "2020-02-06T16:44:10+00:00",
   "time-last-sync": "2020-02-06T16:53:42+00:00"
  }
 ]
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListReplicationPolicies](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Replication/ListReplicationPolicies) operation to list the replication policies for a bucket:


Was this article helpful?
YesNo

