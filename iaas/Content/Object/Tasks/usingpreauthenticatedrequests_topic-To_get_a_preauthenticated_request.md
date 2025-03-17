Updated 2025-01-30
# Getting a Pre-Authenticated Request's Details in Object Storage
View the details of a pre-authenticated request in a bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_get_a_preauthenticated_request.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_get_a_preauthenticated_request.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_get_a_preauthenticated_request.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Pre-Authenticated Requests**.
    3. From the **Actions** menu for the pre-authenticated request you want, select **View Details**.
The **Pre-Authenticated Request Details** dialog box opens, containing details of the pre-authenticated request such as the status, the access type, and the expiration date.
  * Use the [oci os preauth-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/preauth-request/get.html) command and required parameters to get the details of a pre-authenticated request in a bucket:
Command
CopyTry It
```
oci os preauth-request get --bucket-name bucket_name --par-id pre-authenticated_request_id [OPTIONS]
```

The `pre-authenticated_request_id` value is the identification number assigned to the pre-authorized request when it was created. See [Accessing the Pre-Authorized Request ID](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_copy_a_preauthenticated_request_ID.htm#top "Get access to your pre-authenticated request ID.") for more information.
For example:
```
oci os preauth-request get --bucket-name MyParBucket --par-id YOExDlFsNYBNEwF8Uo4aK8WHiz59enVQm1aID+4cxFobgcaofVbZkg371rxK+6Vb
{
 "data": {
  "access-type": "AnyObjectReadWrite",
  "bucket-listing-action": "ListObjects",
  "id": "YOExDlFsNYBNEwF8Uo4aK8WHiz59enVQm1aID+4cxFobgcaofVbZkg371rxK+6Vb",
  "name": "PrefixedObjectsReadWritePAR",
  "object-name": "service",
  "time-created": "2021-04-01T15:35:40.609000+00:00",
  "time-expires": "2022-11-21T23:00:00+00:00"
 }
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetPreauthenticatedRequest](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PreauthenticatedRequest/GetPreauthenticatedRequest) operation to get the details of a pre-authenticated request in a bucket.


Was this article helpful?
YesNo

