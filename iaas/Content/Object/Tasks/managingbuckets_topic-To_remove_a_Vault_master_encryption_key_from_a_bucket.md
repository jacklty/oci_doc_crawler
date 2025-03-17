Updated 2025-01-22
# Removing a Vault Key from an Object Storage Bucket
Remove a Vault master encryption key from an Object Storage bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_remove_a_Vault_master_encryption_key_from_a_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_remove_a_Vault_master_encryption_key_from_a_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_remove_a_Vault_master_encryption_key_from_a_bucket.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, find **Encryption Key** and select **Unassign**.
    3. When prompted, confirm the unassignment.
  * Use the [oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command and required parameters to remove a Vault key to a bucket.
Command
CopyTry It
```
oci os bucket update --name bucket_name --kms-key-id "" [OPTIONS]
```

where the `kms-key-id` parameter has the value `""`.
For example:
```

oci os bucket update --name MyKeyBucket --kms-key-id ""
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  "defined-tags": {},
  "etag": "10a50818-e495-45a9-b1ce-cc815f7b39ad",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  **"kms-key-id": null**,
  "metadata": {},
  "name": "MyKeyBucket",
  "namespace": "MyNamespace",
  "object-events-enabled": false,					
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess",
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-29T23:00:35.490000+00:00",
  "versioning": "Disabled"
 },
 "etag": "10a50818-e495-45a9-b1ce-cc815f7b39ad"
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * This task can't be performed using the API.


Was this article helpful?
YesNo

