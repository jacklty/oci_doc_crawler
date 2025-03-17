Updated 2024-01-18
# Deleting a Bucket
On Compute Cloud@Customer, you can permanently delete an empty bucket.
**Caution**
You can't recover a deleted bucket.
You can't delete a bucket that contains any of the following:
  * Any objects
  * Previous versions of an object
  * A multipart upload in progress
  * A preauthenticated request


**Tip**
When you delete an object in a version-enabled bucket, a previous version of that object is created. Select Show Deleted Objects to display the object versions that might prevent you from deleting the bucket. For more information, see [Managing Object Versioning](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/managing-object-versioning.htm#managing-object-versioning "On Compute Cloud@Customer, object versioning provides data protection against accidental or malicious object update, overwrite, or deletion.").
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-a-bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-a-bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/object/deleting-a-bucket.htm)


  * This task isn't available in the Console.
  * Use the [oci os bucket delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/delete.html) command and required parameters to delete a bucket if the bucket is empty. 
Copy
```
oci os bucket delete --namespace-name <object_storage_namespace> --bucket-name <bucket_name>[OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteBucket](https://docs.oracle.com/iaas/api/#/en/s3objectstorage/latest/Bucket/DeleteBucket) operation to delete a bucket if the bucket is empty.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

