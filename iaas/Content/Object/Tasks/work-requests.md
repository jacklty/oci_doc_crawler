Updated 2025-01-22
# Object Storage Work Requests
View the state of work requests associated with Object Storage.
The Object Storage service handles work requests asynchronously. The service creates a queue for work requests and then processes the requests when system resources become available. To provide visibility for in-progress operations, Object Storage creates a [work request](https://docs.oracle.com/iaas/Content/API/Concepts/workrequests.htm). You can track the progress of the operation by monitoring the status of the work request.
You can perform the following Object Storage work request management tasks:
  * [List the work requests for a bucket.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request.htm#top "View a list of the Object Storage work requests in a Oracle Cloud Infrastructure compartment.")
  * [Get the details of a work request.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm#top "View the details of an Object Storage work request.")
  * [List the errors for a work request.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request-error.htm#top "View a list of the errors for a Object Storage work request.")
  * [List the logs for a work request.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request-log-entry.htm#top "View a list of the logs for an Object Storage work request.")
  * [Cancel a work request.](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/cancel-work-request.htm#top "Cancel a work request.")


## Work Request Status Descriptions 🔗 
You can view the status of a work request in the following locations:
  * The **Work Request** list. See [Listing Work Requests](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request.htm#top "View a list of the Object Storage work requests in a Oracle Cloud Infrastructure compartment.") for more information.
  * The work request's **Details** page. See [Getting a Work Request's Details](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/get-work-request.htm#top "View the details of an Object Storage work request.") for more information.


Monitor these locations to get the updated status of a work request.
The following table lists and describes the work request status levels:
Work Request Status Indicators Status | Description  
---|---  
**Accepted** |  The request is in the work request queue to be processed.  
**In Progress** |  A work request record exists for the specified request, but no associated WORK_COMPLETED record exists.  
**Completed** |  A work request record exists for this request and an associated WORK_COMPLETED record has the state **Completed**.  
**Canceling** |  The work request is in the process of being canceled.  
**Canceled** |  The work request has been canceled.  
**Failed** |  A work request record exists for this request and an associated WORK_COMPLETED record has the state **Failed**. Check the **Error Details** column for more information on the reason for the fail. For example: `All five non-reserved IP addresses of the subnet_CIDR for ocid have already been allocated.` See [Lising a Work Request's Errors](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/list-work-request-error.htm#top "View a list of the errors for a Object Storage work request.") to learn more about why a work request failed.  
Was this article helpful?
YesNo

