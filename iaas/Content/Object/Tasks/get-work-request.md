Updated 2025-01-22
# Getting an Object Storage Work Request's Details
View the details of an Object Storage work request.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Work Requests**.
The **Work Requests** list opens, displaying details on each work request. These details include the status, resource type, operation type, resource name, and time accepted for each work request.
  * Use the [oci os work-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/work-request/get.html) command and required parameters to get the details of a Object Storage work request:
Command
CopyTry It
```
oci os work-request get --work-request-id work_request_id [OPTIONS]
```

List the work requests in a compartment to get their IDs. See [Listing Work Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request.htm#top "View a list of the Object Storage work requests in a Oracle Cloud Infrastructure compartment.") for more information.
For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [GetWorkRequest](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/WorkRequest/GetWorkRequest) operation to get the details of a Object Storage work request.


Was this article helpful?
YesNo

