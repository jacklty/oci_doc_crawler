Updated 2024-01-18
# Viewing the Health of an NLB Backend Set
On Compute Cloud@Customer, you can view the network load balancer (NLB) backend set health status.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-the-health-of-an-nlb-backend-set.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-the-health-of-an-nlb-backend-set.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-the-health-of-an-nlb-backend-set.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Network Load Balancers**.
    2. At the top of the page, select the compartment that contains the NLB.
    3. Click the name of the NLB for which you want to view backend set health status. 
    4. Under **Resources** , click **Backend Sets**.
    5. Click the Backend Set to view the backend set health status. 
  * Use the [oci nlb backend-set-health get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend-set-health/get.html) command and required parameters to see the health status for the specified backend set.
Copy
```
oci nlb backend-set-health get [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [GetBackendSetHealth](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/BackendSetHealth/GetBackendSetHealth) operation to get the health status for the specified backend set.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

