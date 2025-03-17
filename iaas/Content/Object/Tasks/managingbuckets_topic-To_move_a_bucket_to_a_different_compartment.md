Updated 2025-01-30
# Moving an Object Storage Bucket Between Compartments
Move an Object Storage bucket to a different compartment in your Oracle Cloud Infrastructure tenancy.
See [Managing Compartments](https://docs.oracle.com/iaas/Content/Identity/compartments/managingcompartments.htm) for information about compartments and access control.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_move_a_bucket_to_a_different_compartment.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_move_a_bucket_to_a_different_compartment.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_move_a_bucket_to_a_different_compartment.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. From the **Actions** menu for the bucket, select **Move resource**.
    3. In the **Move resource** panel, select the destination compartment from the list.
    4. Select **Move resource**.
The bucket now resides in the updated compartment.
  * Use the [oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command and required parameters to move the bucket to a different compartment:
Command
CopyTry It
```
oci os bucket update --name bucket_name --compartment-id destination_compartment_ocid [OPTIONS]
```

where `destination_compartment_ocid` is the compartment OCID associated with the destination compartment for the bucket you're moving.
For example:
```
oci os bucket update --name MyBucket --compartment-id ocid.compartment.oc1..exampleuniqueID
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "**new_ocid.compartment.oc1..exampleuniqueID**",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  "defined-tags": {},
  "etag": "fe4fb648-8ddd-42eb-9732-d431aafac354",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "kms-key-id": null,
  "metadata": {
   "department": "Finance"
  },
  "name": "MyBucket",
  "namespace": "MyNamespace",
  "object-events-enabled": false,					
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess",
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-22T19:04:05.879000+00:00",
  "versioning": "Disabled"
 },
 "etag": "fe4fb648-8ddd-42eb-9732-d431aafac354"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/GetBucket) operation with the `compartmentID` of the destination compartment to move a bucket to a different compartment.
When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```
n/object_storage_namespace/b/bucket
```



Was this article helpful?
YesNo

