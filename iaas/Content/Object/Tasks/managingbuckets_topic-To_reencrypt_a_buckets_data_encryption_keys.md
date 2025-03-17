Updated 2025-01-30
# Re-encrypting an Object Storage Bucket's Data Encryption Keys
Re-encrypt the unique data encryption key that encrypts each object written to an Object Storagebucket by using the most recent version of the master encryption key.
See [Object Storage Data Encryption](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/encryption.htm#data-encryption "Learn about how Object Storage service encrypts and decrypts all objects using 256-bit Advanced Encryption Standard \(AES-256\) to encrypt object data on the server.") for more information,.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_reencrypt_a_buckets_data_encryption_keys.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_reencrypt_a_buckets_data_encryption_keys.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_reencrypt_a_buckets_data_encryption_keys.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Re-encrypt**.
**Note**
If the **Re-encrypt** button isn't enabled, either the bucket is using a master encryption key managed by Oracle rather than a Vault master encryption, or the bucket doesn't contain any objects.
    3. When prompted, confirm the re-encryption. Selecting **Re-encrypt** generates a work request to re-encrypt all data encryption keys associated with the bucket.
The **Work Requests Details** dialog box that displays information about the work request, including the percentage completed and the work request OCID. You can copy the work request OCID to monitor the request status later.
  * Use the [oci os bucket reencrypt](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/reencrypt.html) command and required parameters to re-encrypt the unique data encryption key that encrypts each object written to the bucket by using the most recent version of the master encryption key assigned to the bucket.
Command
CopyTry It
```
oci os bucket reencrypt --name bucket_name [OPTIONS]
```

For example:
```

oci os bucket reencrypt --name MyBucket
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ReencryptBucket](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/Bucket/ReencryptBucket) operation to re-encrypt the unique data encryption key that encrypts each object written to the bucket by using the most recent version of the master encryption key assigned to the bucket.
When accessing the Object Storage API, the bucket name is used with the Object Storage namespace name to form the request URL:
```
n/object_storage_namespace/b/bucket
```



Was this article helpful?
YesNo

