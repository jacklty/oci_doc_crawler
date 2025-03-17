Updated 2025-01-30
# Creating an Object Storage Replication Policy
Create a replication policy for an Object Storage source bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_create_a_replication_policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_create_a_replication_policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingreplication_topic-To_create_a_replication_policy.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Replication Policy**.
    3. Select **Create Policy**.
    4. Enter the following information:
       * **Name** : Accept the default name or enter your own. Object Storage generates a policy name that reflects the current year, month, day, and time, for example, **replication-policy-20200129-2230**. If you change this name, use letters, numbers, dashes, underscores, and periods.
       * **Destination Region** : Select the OCI region that contain the destination bucket that you want to replicate to from the list. Your tenancy must be subscribed to a region for you to replicate to that region. See [Managing Regions](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingregions.htm) for more information.
       * **Destination Bucket** : Select the name destination bucket for replication. Select **Change compartment** to select a bucket in a different compartment. Ensure you have the required policy access for the destination bucket.
    5. Select **Create**.
The Console checks the IAM policies that are in place to perform this task successfully. If you see a policy missing warning, you can let the Console try to create any missing policies or copy the missing policy details to the clipboard to email your administrator. If you have the required policies in place, create the replication policy.
After the policy is created, **Replication: Enabled (Source)** is added to the bucket information. Objects uploaded to the source bucket after the policy is created are asynchronously replicated to the destination bucket.
  * Use the [oci os replication create-replication-policy](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/create-replication-policy.html) command and required parameters to create a replication policy for a bucket:
Command
CopyTry It
```
oci os replication create-replication-policy --bucket-name bucket_name --destination-region destination_region_id --destination-bucket destination_bucket_name [OPTIONS]
```

For example:
```
oci os replication create-replication-policy --bucket-name MySourceBucket --destination-region us-ashburn-1 --destination-bucket MyDestinationBucket --name MyReplicationPolicy
{
 "data": {
  "destination-bucket": "MyDestinationBucket",
  "destination-region": "us-ashburn-1",
  "id": "bacb8334-b191-4026-aa65-5e4f5165ae3e",
  "name": "MyReplicationPolicy",
  "status": "ACTIVE",
  "status-message": "The policy is active.",
  "time-created": "2020-02-06T16:44:10+00:00",
  "time-last-sync": "2020-02-06T16:44:20+00:00"
 }
}
```

Objects uploaded to the source bucket after policy creation are asynchronously replicated to the destination bucket.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [CreateReplicationPolicy](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Replication/CreateReplicationPolicy) operation to create a replication policy for a bucket.


Was this article helpful?
YesNo

