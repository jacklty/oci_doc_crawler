Updated 2025-01-22
# Assigning a Key to an Object Storage Bucket
Assign a Vault master encryption key to an Object Storage bucket.
You can encrypt the data encryption keys that encrypt the objects in a bucket by using your own Vault master encryption key. By default, buckets are encrypted with keys managed by Oracle. For more information, see [Object Storage Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm#data-encryption "Learn about how Object Storage service encrypts and decrypts all objects using 256-bit Advanced Encryption Standard \(AES-256\) to encrypt object data on the server.") and [Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm)
**Important** Buckets in a security zone can't use the default encryption key managed by Oracle. You must use your own Vault master encryption key.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_assign_a_Vault_master_encryption_key_to_a_bucket.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, find **Encryption Key** and perform one of the following actions:
       * If the bucket is encrypted with a key managed by Oracle, select **Assign**. The **Assign Master Encryption Key** dialog box appears.
       * If the bucket already has a Vault master encryption key assigned, to assign a different key, select **Edit**. The **Edit Master Encryption Key** dialog box appears.
    3. Enter the following information:
       * The Vault compartment and vault that contain the master encryption key you want to use. The current compartment is displayed by default.
       * The master encryption key compartment and master encryption key. The current compartment is displayed by default.
    4. Select **Assign** or **Edit**.
  * Use the [oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command and required parameters to assign a Vault key to a bucket.
Command
CopyTry It
```
oci os bucket update --name bucket_name --kms-key-id kms_key_id [OPTIONS]
```

where `kms_key_id` is the OCID of the key versions that contain the cryptographic material used to encrypt and decrypt data, protecting the data where the data is stored.
For example:
```

oci os bucket update --name MyKeyBucket --kms-key-id ocid1.key.region1.sea..exampleuniqueID
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  "defined-tags": {},
  "etag": "e7f29fdd-b5f5-42e5-a98b-80883f9f2f32",
  "freeform-tags": {},
  "id": "ocid1.bucket.oc1..exampleuniqueID",
  "is-read-only": false,
  "**kms-key-id": "ocid1.key.region1.sea..exampleuniqueID**",
  "metadata": {},
  "name": "MyKeyBucket",
  "namespace": "MyNamespace",
  "object-events-enabled": false,					
  "object-lifecycle-policy-etag": null,
  "public-access-type": "NoPublicAccess"
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-29T23:00:35.490000+00:00",
  "versioning": "Disabled"
 },
 "etag": "e7f29fdd-b5f5-42e5-a98b-80883f9f2f32"
}
```
If you're updating the key, run the same[oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command with the updated kms_key_id value.
See [Overview of Vault](https://docs.oracle.com/iaas/Content/KeyManagement/Concepts/keyoverview.htm) for more details.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * This task can't be performed using the API.


Was this article helpful?
YesNo

