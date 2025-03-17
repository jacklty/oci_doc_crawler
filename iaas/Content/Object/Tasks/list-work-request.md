Updated 2025-01-22
# Listing Object Storage Work Requests
View a list of the Object Storage work requests in a Oracle Cloud Infrastructure compartment.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request.htm)


  *     1. On the **Buckets** list page, select the Object Storage bucket that you want to work with. If you need help finding the list page or the Object Storage bucket, see [Listing Buckets](https://docs.oracle.com/iaas/Content/Object/Tasks/managingbuckets_topic-To_get_a_list_of_buckets_concept.htm).
    2. On the details page, select **Work Requests**.
The **Work Requests** list opens. All work requests for the bucket are listed in a table.
  * Use the [oci os work-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/os/work-request/list.html) command and required parameters to list the Object Storage work requests in a compartment:
Command
CopyTry It
```
oci os work-request list --compartment-id compartment_ocid [OPTIONS]
```

For a complete list of parameters and values for CLI commands, see the [CLI Command Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest).
  * Run the [ListWorkRequests](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/WorkRequestSummary/ListWorkRequests) operation to list the Object Storage work requests in a compartment.


Was this article helpful?
YesNo

