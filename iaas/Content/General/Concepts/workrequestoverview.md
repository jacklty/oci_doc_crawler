Updated 2025-02-13
# Work Requests
Work requests help you monitor long-running operations such as database backups or the provisioning of compute instances.
When you start a long-running operation, the service creates a _work request_. A work request is an activity log that lets you track each step in the operation's progress. Each work request has an **OCID** that lets you interact with it programmatically and use it for automation.
Work requests typically provide information about the status of the associated workflow, errors, log files, and a list of resources that are affected by the workflow.
**Note**
Some Oracle Cloud Infrastructure services, such as Compute and Database, support work requests using the [Work Requests API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/), which contains the `GetWorkRequest` operation.
Some services offer work requests supported by the service API rather than the Work Requests API discussed in this topic. These service APIs each include operations that work in a similar manner to the `GetWorkRequest` operation used by the Work Requests API.
See the reference documentation for each service's work request API for details. Links to each are provided in the [More Information and APIs for Supported Services](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#api) section.
## Getting Started with Work Requests 🔗 
Work requests are helpful in the following scenarios:
  * If an operation fails, a work request can help you determine which step of the process had an error. Work requests capture [asynchronous validation failures](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/workrequestoverview.htm#errors).
  * Some operations affect multiple resources. For example, creating an instance pool also affects instances and instance configurations. A work request provides a list of the resources that an operation affects.
  * For workflows that require sequential operations, you can monitor each operation's work request and confirm that the operation has completed before proceeding to the next operation. For example, say that you want to create an instance pool with autoscaling enabled. To do this, you must first create the instance pool, and then configure autoscaling. You can monitor the work request for creating the instance pool to determine when that workflow is complete, and then configure autoscaling after the instance pool workflow has finished.


Work requests are retained for 12 hours.
### Required IAM Policy 🔗 
To use Oracle Cloud Infrastructure, an administrator must be a member of a group granted security access in a **policy** by a tenancy administrator. This access is required whether you're using the Console or the REST API with an SDK, CLI, or other tool. If you get a message that you don't have permission or are unauthorized, verify with the tenancy administrator what type of access you have and which **compartment** your access works in.
For administrators: The permissions that allow users to view the work requests, logs, and error messages for an operation vary depending on the service. For some services, work requests inherit the permissions of the operation that spawns the work request. For other services, work requests require separate permissions. For more information, see [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
### Work Request Status 🔗 
Work requests provide visibility into the progress of long-running, asynchronous operations. The status of a work request indicates the progress of the operation.
Statuses typically include values such as `IN_PROGRESS`, `FAILED`, or `SUCCEEDED`. Because each service or operation that supports work requests provides its own API for obtaining status, the specific values that are returned in a work request can vary depending on the service and operation. For information about the status attributes that are supported by work requests for each service, see [Work Request Status](https://docs.oracle.com/iaas/Content/API/Concepts/workrequests.htm#status).
### Troubleshooting Validation Errors 🔗 
Work requests capture asynchronous validation failures. If an asynchronous operation fails, a work request can help you determine where in the process the error occurred.
Synchronous errors occur during the initial call to the service API and are returned by the service API. Asynchronous errors occur during the workflow that occurs after the initial API call and are returned by the work request. A successful call to the service API that returns an HTTP 200 response ("request was successful") might be followed by an asynchronous error that is captured by the work request.
For example, when you create a compute instance, an API call is made to the `LaunchInstance` operation. At this point, synchronous validation occurs. If a failure occurs, an [HTTP 4xx response](https://docs.oracle.com//iaas/Content/API/References/apierrors.htm) is returned. If the call succeeds, an HTTP 200 response is returned and the create instance workflow starts.
While the create instance workflow continues, additional validation and error checks occur, and an [asynchronous work request](https://docs.oracle.com/iaas/Content/API/Concepts/workrequests.htm) is created to track the progress of the workflow. The response to the `LaunchInstance` operation contains the OCID of the work request in the `opc-work-request-id` header. You can monitor the status of the work request at any time by calling the `GetWorkRequest` operation and passing in the work request ID. If an error occurs during the workflow, you can retrieve a list of errors by calling `ListWorkRequestErrors` and passing in the work request ID.
The work request itself remains in a queue until the operation has completed.
For detailed information about work requests, including how to filter the request response and a sample request and response, see [Asynchronous Work Requests](https://docs.oracle.com/iaas/Content/API/Concepts/workrequests.htm).
#### Example Work Request Validation Workflow 🔗 
The following diagram shows an example create instance workflow in which the synchronous validation succeeds and the asynchronous validation fails.
  1. You call the `LaunchInstance` endpoint in the Compute API.
  2. Synchronous validation occurs, and you receive an HTTP 2xx response from the Compute API. The response includes the OCID of the work request in the `opc-work-request-id` header.
  3. The create instance workflow starts, and asynchronous validation occurs throughout the workflow. An error occurs, and the validation fails.
  4. The Compute API populates the work request errors and marks the work request as failed.
  5. To monitor the work request, you call `GetWorkRequest` in the Work Requests API and pass in the work request ID found in the `opc-work-request-id` header.
  6. Seeing that the work request failed, you call `ListWorkRequestErrors` in the Work Requests API and pass in the work request ID to retrieve a list of errors.
  7. The Work Requests API returns a list of errors that you can use to determine the cause of the failure.


[![High level diagram of the create instance workflow showing synchronous and asynchronous validation.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/work-requests.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/work-requests.png)
## Using the Console to View Work Requests 🔗 
You can use the Console to see the log messages, error messages, and resources associated with a specific work request. The steps to view a work request might vary depending on the service and the resource whose work requests you want to see.
  1. Navigate to the resource whose work requests you want to see.
For example, to see the work requests for a compute instance: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. If the resource is displayed in a list view, click the resource name to view the resource details.
  3. Under **Resources** , click **Work Requests**. The status of all work requests appears on the page.
  4. To see the log messages, error messages, and resources that are associated with a specific work request, click the operation name. Then, select an option in the **More information** section.
For associated resources, you can click the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) next to a resource to copy the resource's OCID.


## More Information and APIs for Supported Services 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use the following API operations to monitor the state of work requests:
  * [Application Performance Monitoring work request API](https://docs.oracle.com/iaas/api/#/en/apm-control-plane/latest/WorkRequest/)
  * [Autonomous Recovery Service work request API](https://docs.oracle.com/iaas/api/#/en/recovery-service/latest/WorkRequest/)
  * [Bastion work request API](https://docs.oracle.com/iaas/api/#/en/bastion/latest/WorkRequest/)
  * [Blockchain Platform work requests](https://docs.oracle.com/en/cloud/paas/blockchain-cloud/administeroci/getting-started.html)
  * [Cloud Advisor work request API](https://docs.oracle.com/iaas/api/#/en/advisor/latest/WorkRequest/)
  * [Cluster Placement Groups work request API](https://docs.oracle.com/iaas/api/#/en/clusterplacementgroups/latest/WorkRequest/)
  * [Compute work request API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)
  * Connector Hub:
    * [Viewing the State of a Connector Hub Work Request](https://docs.oracle.com/iaas/Content/connector-hub/workrequests.htm)
    * [Connector Hub work request API](https://docs.oracle.com/iaas/api/#/en/serviceconnectors/latest/WorkRequest)
  * [Container Instances work request API](https://docs.oracle.com/iaas/api/#/en/container-instances/latest/WorkRequest/)
  * [Content Management work request API](https://docs.oracle.com/iaas/api/#/en/oce/latest/WorkRequest)
  * Data Catalog:
    * [Data Catalog Work Requests](https://docs.oracle.com/iaas/data-catalog/using/work-request.htm)
    * [Data Catalog work request API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)
  * [Data Integration work request API](https://docs.oracle.com/iaas/api/#/en/data-integration/latest/WorkRequest/)
  * Data Labeling:
    * [Data Labeling Work Requests](https://docs.oracle.com/iaas/Content/data-labeling/using/work-requests.htm)
    * [Data Labeling work request API](https://docs.oracle.com/iaas/api/#/en/datalabeling/latest/WorkRequest/)
  * Data Science:
    * [Creating Notebook Sessions](https://docs.oracle.com/iaas/data-science/using/create-notebook-sessions.htm) and [Deleting Projects](https://docs.oracle.com/iaas/data-science/using/manage-projects.htm#delete-projects)
    * [Data Science work request API](https://docs.oracle.com/iaas/api/#/en/data-science/latest/WorkRequest/)
  * [Database work request API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)
  * [Database Management work request API](https://docs.oracle.com/iaas/api/#/en/database-management/latest/WorkRequest/)
  * [Database Migration work request API](https://docs.oracle.com/iaas/api/#/en/database-migration/latest/WorkRequest/)
  * [Database Tools work request API](https://docs.oracle.com/iaas/api/#/en/database-tools/latest/WorkRequest/)
  * [OCI Database with PostgreSQL work request API](https://docs.oracle.com/iaas/api/#/en/postgresql/latest/WorkRequest/)
  * [DevOps work request API](https://docs.oracle.com/iaas/api/#/en/devops/latest/WorkRequest/)
  * [File Storage work request API](https://docs.oracle.com/iaas/api/#/en/workrequests/latest/)
  * [Fleet Application Management work request API](https://docs.oracle.com/iaas/api/#/en/fleet-management/latest/WorkRequest/)
  * [Full Stack Disaster Recovery work request API](https://docs.oracle.com/iaas/api/#/en/disaster-recovery/latest/WorkRequest/)
  * [Globally Distributed Autonomous Database work request API](https://docs.oracle.com/iaas/api/#/en/globally-distributed-autonomous-database/latest/WorkRequest/)
  * [GoldenGate work request API](https://docs.oracle.com/iaas/api/#/en/goldengate/latest/WorkRequest/)
  * IAM:
    * [IAM work request API](https://docs.oracle.com/iaas/api/#/en/identity/latest/WorkRequest/) ([To delete a different compartment](https://docs.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#To_delete_a_compartment))
    * [TaggingWorkRequest API](https://docs.oracle.com/iaas/api/#/en/identity/latest/TaggingWorkRequest/) ([Tags and Tag Namespace Concepts](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm))
  * [Integration work request API](https://docs.oracle.com/iaas/api/#/en/integration/latest/WorkRequest/)
  * [Java Management work request API](https://docs.oracle.com/iaas/api/#/en/jms/latest/WorkRequest/)
  * [Kubernetes Engine work request API](https://docs.oracle.com/iaas/api/#/en/containerengine/latest/WorkRequest/)
  * Load Balancer:
    * [Work Requests for Load Balancer](https://docs.oracle.com/iaas/Content/Balance/Tasks/viewingworkrequest.htm)
    * [Load Balancer work request API](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/WorkRequest/)
  * [Logging Analytics work request API](https://docs.oracle.com/iaas/api/#/en/logan-api-spec/latest/WorkRequest/)
  * [Management Agent work request API](https://docs.oracle.com/iaas/api/#/en/management-agent/latest/WorkRequest/)
  * [HeatWave work request API](https://docs.oracle.com/iaas/api/#/en/mysql/latest/WorkRequest/)
  * [Network Firewall work request API](https://docs.oracle.com/iaas/api/#/en/network-firewall/latest/WorkRequest/)
  * Object Storage:
    * [Copy Object Work Requests](https://docs.oracle.com/iaas/Content/Object/Tasks/copyingobjects.htm#workrequests)
    * [Object Storage work request API](https://docs.oracle.com/iaas/api/#/en/objectstorage/latest/WorkRequest/)
  * [Oracle Cloud Bridge work request API](https://docs.oracle.com/iaas/api/#/en/OCB/latest/WorkRequest/)
  * [Oracle Cloud Migrations work request API](https://docs.oracle.com/iaas/api/#/en/ocm/latest/WorkRequest/)
  * [OS Management Hub work request API](https://docs.oracle.com/iaas/api/#/en/osmh/latest/WorkRequest/)
  * [Process Automation work request API](https://docs.oracle.com/iaas/api/#/en/opa/latest/WorkRequest/)
  * [Queue work request API](https://docs.oracle.com/iaas/api/#/en/queue/latest/WorkRequest/)
  * [Resource Manager work request API](https://docs.oracle.com/iaas/api/#/en/resourcemanager/latest/WorkRequest/)
  * [Secure Desktops work request API](https://docs.oracle.com/iaas/api/#/en/secure-desktops/latest/WorkRequest/)
  * [Service Mesh work request API](https://docs.oracle.com/iaas/api/#/en/service-mesh/latest/WorkRequest/)
  * [Stack Monitoring work request API](https://docs.oracle.com/iaas/api/#/en/stack-monitoring/latest/WorkRequest/)
  * [Vision work request API](https://docs.oracle.com/iaas/api/#/en/vision/latest/WorkRequest/)
  * Visual Builder Studio: [WorkRequest API](https://docs.oracle.com/iaas/api/#/en/visual-builder-studio/latest/WorkRequest)
  * [Vulnerability Scanning work request API](https://docs.oracle.com/iaas/api/#/en/scanning/latest/WorkRequest/)


Was this article helpful?
YesNo

