Updated 2023-07-17
# Listing an Instance's Work Requests for Roving Edge Infrastructure
View a list of an instance's work requests for Roving Edge Infrastructure.
A work request is an activity log that tracks each step in an asynchronous operation. Use work requests to monitor the progress of long-running operations.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/list-work-requests.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance whose work request details you want to get. The **Details** page for that instance appears.
    4. Click **Work Requests** under **Resources**.
The **Work Requests** page appears. All the work requests are listed in tabular form.
  * Use the [oci work-requests work-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/work-requests/work-request/list.html) command and required parameters to view a list of an instance's work requests for a Roving Edge Infrastructure device:
```
oci work-requests work-request list --compartment-id compartment_ocid --resource-id instance_ocid [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [ListWorkRequests](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/WorkRequestSummary/ListWorkRequests) operation to view a list of an instance's work requests for a Roving Edge Infrastructure device.


Was this article helpful?
YesNo

