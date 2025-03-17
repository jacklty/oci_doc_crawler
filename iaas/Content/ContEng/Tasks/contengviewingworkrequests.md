Updated 2025-02-26
# Viewing Work Requests
_Find out how to view the operations of Kubernetes Engine (OKE) as work requests._
Many Kubernetes Engine service requests do not take effect immediately. For example, the creation of a node pool isn't completed until all required nodes are active. In these cases, the request is fulfilled asynchronously, and its progress tracked by an associated work request. A work request is an activity log that provides visibility into in-progress asynchronous operations, enabling you to track each step in the operation's progress. Each work request has an OCID that allows you to interact with it programmatically and use it for automation. 
Work requests include information about the time the request started and finished. If an operation fails, a work request can help you determine which step of the process had an error. Some operations affect multiple resources. For example, creating a node pool also affects nodes. A work request provides a list of the resources that an operation affects.
For more information, see [Work Requests](https://docs.oracle.com/iaas/Content/General/Concepts/workrequestoverview.htm) and the [Work Requests API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/).
## Node Pool Work Requests
Resources managed by Kubernetes Engine can only support one work request at a time. Work requests launched while another work request is in progress will fail and return a conflict. Because some operations depend on the completion of other operations, you must monitor each operation's work request and confirm it has succeeded before proceeding to the next operation. A create node pool work request has a status of **Succeeded** when the workflow successfully creates a node and the node is registered with an **Active** status. 
## Work Request Status 🔗 
The following table lists work request states:
Status |  Description  
---|---  
**Accepted** |  The request is in the work request queue to be processed.  
**In Progress** |  A work request record exists for the specified request, but no associated WORK_COMPLETED record exists.  
**Succeeded** |  A work request record exists for this request and an associated WORK_COMPLETED record has the state **Succeeded**.  
**Failed** |  A work request record exists for this request and an associated WORK_COMPLETED record has the state **Failed**.  
**Canceling** |  The work request is in the process of canceling.  
**Canceled** |  The work request has been canceled.  
## Required IAM Policy for Viewing Work Requests
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: Work requests inherit the permissions of the operation that spawns the work request. To enable users to view the work requests, logs, and error messages for an operation, write a policy that grants users permission to do the operation. For example, to let users see the work requests associated with launching instances, write a policy that enables users to launch instances.
To enable users to list all work requests in a tenancy, use the following policy:
Copy
```
Allow group SupportTeam to inspect work-requests in tenancy
```

If you're new to policies, see [Managing Identity Domains](https://docs.oracle.com/iaas/Content/Identity/domains/overview.htm) and [Common Policies](https://docs.oracle.com/iaas/Content/Identity/Concepts/commonpolicies.htm). 
## Getting Work Request Details 🔗 
Get the details of a work request for a cluster or node pool resource.
Use one of the following methods to get the details of a work request for a selected cluster or node pool resource.
[To get the details of a work request using the Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm)
Get the details of a work request for a cluster or node pool resource.
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Select the **Compartment** from the list.
  3. On the **Cluster List** page, click the name of the cluster for which you want to get work request details.
  4. If you want to get work request details for a particular node pool in the cluster, click **Node Pools** under **Resources** , and click the name of the node pool.
  5. To view work requests, click **Work Requests** under **Resources**.
  6. In the **Work Requests** list, find the work request for which you want to get details. For each recent work request, you can see the following:
     * **Operation Type:** The operation being performed by the work request.
     * **Status:** See [Work Request Status](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#contengviewingworkrequests__conteng-work-request-status) for a list of statuses and their descriptions.
     * **ID:** OCID of the work request.
     * **Resource:** The name of the resource.
     * **Time Started:** UTC-based date-time group when the work request was started.
     * **Time Finished:** UTC-based date-time group when the work request was finished.
  7. Click a particular work request to see:
     * **Log messages:** Information about the stage of the workflow and a timestamp for each stage.
     * **Error messages:** Information about errors and the timestamp of the error.
     * **Associated resources:** The name, type, and OCID of resources impacted by the work request. 


[To get the details of a work request using the CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm)
Use the command line interface (CLI) to get the details of a work request for a cluster or node pool resource.
Enter the following command:
Command
CopyTry It
```
oci ce work-request get --work-request-id work_request_id [OPTIONS]
```

See the CLI online help for a list of options:
Command
CopyTry It
```
oci ce work-request get --help
```

See [oci ce work-request get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/work-request/get.html) for a complete description of the command.
[To get the details of a work request using the API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm)
Use the API to get the details of a work request for a cluster or node pool resource.
Run the GetWorkRequest method to get the details of a work request for a cluster or node pool. See [GetWorkRequest](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/WorkRequest/GetWorkRequest) for a complete description.
## Listing Work Requests 🔗 
List the work requests for a cluster or node pool resource.
Use one of the following methods to display a list of work requests for a selected cluster or node pool resource.
[To list the work requests using the Console](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm)
Use the OCI Console to list the work requests for a cluster or node pool resource.
  1. Open the **navigation menu** and select **Developer Services**. Under **Containers & Artifacts**, select **Kubernetes Clusters (OKE)**.
  2. Select the **Compartment** from the list.
  3. On the **Cluster List** page, click the name of the cluster for which you want to list work requests.
  4. If you want to get work request details for a particular node pool in the cluster, click **Node Pools** under **Resources** , and click the name of the node pool.
  5. Click **Work Requests** under **Resources**.
The **Work Requests** list shows recent work requests.


[To list the work requests using the CLI](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm)
Use the command line interface (CLI) to list the work requests for a cluster or node pool resource.
Enter the following command:
Command
CopyTry It
```
oci ce work-request list --compartment-id compartment-OCID --resource-type CLUSTER|NODEPOOL --cluster-id cluster-OCID --resource-id resource-OCID [OPTIONS]
```

See the CLI online help for a list of options:
Command
CopyTry It
```
oci ce work-request list --help
```

See [oci ce work-request list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce/work-request/list.html) for a complete description of the command.
[To list the work requests using the API](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm)
Use the API to list the work requests for a cluster or node pool resource.
Run the ListWorkRequests method to list the work requests for a cluster or node pool resource. See [ListWorkRequests](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/WorkRequestSummary/ListWorkRequests) for a complete description.
Was this article helpful?
YesNo

