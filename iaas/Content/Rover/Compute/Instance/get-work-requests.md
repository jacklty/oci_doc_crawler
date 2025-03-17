Updated 2023-07-17
# Getting an Instance Work Request's Details for Roving Edge Infrastructure
View the details and access additional information regarding an instance's work request for a Roving Edge Infrastructure device.
A work request is an activity log that tracks each step in an asynchronous operation. Use work requests to monitor the progress of long-running operations.
  * [Console](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-work-requests.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-work-requests.htm)
  * [API](https://docs.oracle.com/en-us/iaas/Content/Rover/Compute/Instance/get-work-requests.htm)


  *     1. Open the navigation menu and select **Compute > Instances**. The **Instances** page appears. All instances are listed in tabular form.
    2. (optional) Select a **State** from the list to limit the instances displayed to that state.
    3. Click the instance whose work request details you want to get. The **Details** page for that instance appears.
    4. Click **Work Requests** under **Resources**. The **Work Requests** page appears. All the work requests are listed in tabular form.
    5. Click the work request whose details you want to get. The **Details** page for that work request appears. The **Details** page contains information on the work request, including the time the job was accepted, started, and completed.
    6. Click any of the following commands under **Resources** to view additional information on the work request:
       * **Log Messages** : Displays general entries in the log and their timestamps.
       * **Error Messages** : Displays error entries in the log and their timestamps.
       * **Associated Resources** : Displays a link to the associated compute instance.
When the **Details** page indicates the work request has succeeded and displays a **Finished** time, the work request is complete.
  * Use the [oci work-requests work-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/work-requests/work-request/get.html) command and required parameters to view the details and access additional information regarding an instance's work request for a Roving Edge Infrastructure device:
```
oci work-requests work-request get --work-request-id work_request_ocid [OPTIONS]
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Run the [GetWorkRequest](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/WorkRequest/GetWorkRequest) operation to view the details and access additional information regarding an instance's work request for a Roving Edge Infrastructure device.


Was this article helpful?
YesNo

