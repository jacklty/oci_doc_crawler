Updated 2024-01-18
# Viewing NLB Work Request Errors
On Compute Cloud@Customer, you can view NLB work requests to see if and NLB work request encountered errors.
Many of the configuration steps used to create and configure network load balancer (NLB) operation don't take effect immediately. In these cases, the request initiates an asynchronous work flow known as a work request to carry out the operation. 
Because of the asynchronous nature of work request fulfillment, it's not always obvious that a configuration step has failed with an error. The failed step is often not revealed until the next step. 
You can view NLB work request status indicators to find out if a work request has failed with an error. You can check the progress of each operation, whether it resulted in a failed state, which step it failed on, and the reason for the failure.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-nlb-work-request-errors.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-nlb-work-request-errors.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-nlb-work-request-errors.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Network Load Balancers**.
    2. At the top of the page, select the compartment that contains the NLB.
    3. Click the name of the NLB for which you want to view work requests. 
    4. Under **Resources** , click **Work Requests**.
    5. For each work request, you can view the following information:
       * Type of work request
       * State of the work request (Succeeded, Failed, and so on)
       * Start and finish timestamp
    6. Click the name of a work request to see the following work request details:
       * General information about the work request, such as the type
       * OCID of the work request
       * Error detail of a failed work request (nothing is displayed for a nonfailure status)
       * Start and finish timestamp
  * Use the [oci nlb work-request-error list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/work-request-error/list.html) command and required parameters to see a paginated list of errors for a particular work request.
Copy
```
oci nlb work-request-error list [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListWorkRequestErrors](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/WorkRequestError/ListWorkRequestErrors) operation to list errors for a particular work request.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

