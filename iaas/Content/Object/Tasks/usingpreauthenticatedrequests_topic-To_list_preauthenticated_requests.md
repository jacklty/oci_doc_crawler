Updated 2025-01-30
# Listing Pre-Authenticated Requests in Object Storage
View a list of the pre-authenticated requests in a bucket.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_list_preauthenticated_requests.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Pre-Authenticated Requests**.
The **Pre-Authenticated Request** list appears.All pre-authenticated requests are listed in a table.
When you create a pre-authenticated request, a unique identification number for the request is generated. You can access and copy this number from the pre-authenticated request list. From the **Actions** menu for the pre-authenticated request you want, select. The ID for the selected pre-authentication request is copied to the clipboard. See [Accessing the Pre-Authorized Request](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_copy_a_preauthenticated_request_ID.htm#top "Get access to your pre-authenticated request ID.") for more information.
  * Use the [oci os preauth-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/preauth-request/list.html) command and required parameters to list the pre-authenticated requests in a bucket:
Command
CopyTry It
```
oci os preauth-request list --bucket-name bucket_name [OPTIONS]
```

For example:
```
oci os preauth-request list --bucket-name MyParBucket
{
 "data": [
  {
   "access-type": "AnyObjectReadWrite",
   "bucket-listing-action": "ListObjects",
   "id": "1G9pfj8elWI0COPtQUmoQayRmYegDrTWjBskI5BixeGY7k5cPHr1BKdFzgEt3OEG",
   "name": "PrefixedObjectsReadWritePAR",
   "object-name": "service",
   "time-created": "2021-04-02T23:52:21.590000+00:00",
   "time-expires": "2022-11-21T23:00:00+00:00"
  },
  {
   "access-type": "AnyObjectReadWrite",
   "bucket-listing-action": "ListObjects",
   "id": "N5Fim23jXHBnAtWBo7FOCOTdXwAZgXRJD1FoDs1S8BD0qhYegO0eHF5prVkPkiVM",
   "name": "MyAllObjectsReadWritePAR",
   "object-name": null,
   "time-created": "2021-04-01T14:13:59.659000+00:00",
   "time-expires": "2022-11-21T23:00:00+00:00"
  },
  {
   "access-type": "ObjectReadWrite",
   "bucket-listing-action": null,
   "id": "I2Z3qm0rnYiJ5HSTvSCVu8+BqOmy1lXD1dNreBk3eM5VHLdWyIU3xkDTjBqAagoF:OCI_User_Guide.pdf",
   "name": "MyObjectReadWritePAR",
   "object-name": "OCI_User_Guide.pdf",
   "time-created": "2021-04-01T15:27:02.467000+00:00",
   "time-expires": "2022-11-21T23:00:00+00:00"
  },
  {
   "access-type": "AnyObjectReadWrite",
   "bucket-listing-action": "ListObjects",
   "id": "QgT6f1skUMbXDhpXKQ4BRX9u7ci8AAJ7f9OGzgdEkNJ3XQmHzeN/kDhLEbN2HvPn",
   "name": "MyAllObjectsReadWritePAR",
   "object-name": null,
   "time-created": "2021-04-02T22:25:27.322000+00:00",
   "time-expires": "2022-11-21T23:00:00+00:00"
  }
 ]
}
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListPreauthenticatedRequests](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/PreauthenticatedRequest/ListPreauthenticatedRequests) operation to list the pre-authenticated requests in a bucket.


Was this article helpful?
YesNo

