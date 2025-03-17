Updated 2025-01-30
# Deleting a Pre-Authenticated Request in Object Storage
Delete a pre-authenticated request from a bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_delete_a_preauthenticated_request.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_delete_a_preauthenticated_request.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_delete_a_preauthenticated_request.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Pre-Authenticated Requests**.
    3. From the **Actions** menu for the pre-authenticated request you want, select **Delete**.
    4. When prompted, confirm the deletion.
The pre-authenticated request you deleted no longer appears in the list.
  * Use the [oci os preauth-request delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/preauth-request/delete.html) command and required parameters to delete a pre-authenticated request from a bucket:
Command
CopyTry It
```
oci os preauth-request delete --bucket-name bucket_name --par-id pre-authenticated_request_id [OPTIONS]
```

The `pre-authenticated_request_id` value is the identification number assigned to the pre-authorized request when it was created. See [Accessing the Pre-Authorized Request ID](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_copy_a_preauthenticated_request_ID.htm#top "Get access to your pre-authenticated request ID.") for more information.
For example:```
oci os preauth-request delete --bucket-name MyParBucket --par-id YOExDlFsNYBNEwF8Uo4aK8WHiz59enVQm1aID+4cxFobgcaofVbZkg371rxK+6Vb
Are you sure you want to delete this resource? [y/N]: y
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [DeletePreauthenticatedRequest](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PreauthenticatedRequest/DeletePreauthenticatedRequest) operation to delete a pre-authenticated request from a bucket.


Was this article helpful?
YesNo

