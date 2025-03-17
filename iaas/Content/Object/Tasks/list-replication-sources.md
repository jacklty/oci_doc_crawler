Updated 2023-12-14
# Listing Replication Sources for an Object Storage Bucket
View a list of replication sources for an Object Storage replication destination bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-replication-sources.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-replication-sources.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-replication-sources.htm)


  * This task can't be performed using the OCI Console.
  * Use the [oci os replication list-replication-sources](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/replication/list-replication-sources.html) command and required parameters to list the sources of a replication policy for an Object Storage replication destination bucket:
Command
CopyTry It
```
oci os replication list-replication-sources --bucket-name bucket_name [OPTIONS]
```

If you're replicating to a destination bucket in a different region, include the `region` parameter and the region identifier. For example:
For example:
```
oci os replication list-replication-sources --namespace MyNamespace --bucket-name MyDestinationBucket --region us-ashburn-1
{
 "data": [
  {
   "policy-name": "MyReplicationPolicy",
   "source-bucket": "MySourceBucket",
   "source-region": "us-phoenix-1"
  }
 ]
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListReplicationSources](https://docs.oracle.com/iaas/api/#23/en/objectstorage/latest/Replication/ListReplicationSources) operation to get the details of a replication policy for an Object Storage bucket.


Was this article helpful?
YesNo

