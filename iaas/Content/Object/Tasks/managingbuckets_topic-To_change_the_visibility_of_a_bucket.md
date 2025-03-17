Updated 2025-01-22
# Changing an Object Storage Bucket's Visibility
Change the public or private visibility of an Object Storage bucket.
Buckets are private by default. For more information, see [Public Buckets](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets.htm#publicbuckets).
**Important** If a bucket is in a security zone, you can't change its visibility from private to public. We recommend using pre-authenticated requests instead of public buckets. Pre-authenticated requests support authorization, expiry, and scoping capabilities that aren't possible with public buckets.
See [Object Storage Pre-Authenticated Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm#pre-auth-req "Learn about how to use the pre-authenticated request feature to give users access a bucket or an object without providing their sign-on credentials.") for details.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_change_the_visibility_of_a_bucket.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Object Storage Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the bucket's details page, find **Visibility** and select **Edit**.
    3. Select **Public** or **Private**.
If you select **Public** to enable public access, decide whether you want to let users list the bucket contents. To set the visibility of bucket object lists, select **Allow users to list objects from this bucket**.
    4. Select **Save Changes**.
  * Use the [oci os bucket update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/bucket/update.html) command and required parameters to change the visibility of a bucket. Include the `public-access-type` parameter:
Command
CopyTry It
```
oci os bucket update --name bucket_name --public-access-type [NoPublicAccess | ObjectRead | ObjectReadWithoutList] [OPTIONS]
```

By default, the bucket is private. You can specify the bucket to be public by including the `public-access-type` parameter and one of its supported values:
    * `NoPublicAccess`: Allows only an authenticated caller to access the bucket and bucket contents. This is the default visibility of a bucket.
    * `ObjectReadWithoutList`: Allows public access for the `GetObject`, `HeadObject`, and `ListObjects` operations.
    * `ObjectRead`: Allows public access for the `GetObject` and `HeadObject` operations.
For example:```
oci os bucket update --name MyBucket --public-access-type ObjectRead
{
 "data": {
  "approximate-count": null,
  "approximate-size": null,
  "auto-tiering": null,
  "compartment-id": "ocid.compartment.oc1..exampleuniqueID",
  "created-by": "ocid1.user.oc1..exampleuniqueID",
  "defined-tags": {},
  "etag": "09ab3193-a441-43cc-a8e2-e468e94c7c60",
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
  **"public-access-type": "ObjectRead"**,
  "replication-enabled": false,
  "storage-tier": "Standard",
  "time-created": "2020-06-22T19:04:05.879000+00:00",
  "versioning": "Disabled"
 },
 "etag": "09ab3193-a441-43cc-a8e2-e468e94c7c60"
}
```
To configure a public bucket to be private, run the`oci os bucket update` command with the `--public-access-type NoPublicAccess` parameter and value.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * This task can't be performed using the API.


Was this article helpful?
YesNo

