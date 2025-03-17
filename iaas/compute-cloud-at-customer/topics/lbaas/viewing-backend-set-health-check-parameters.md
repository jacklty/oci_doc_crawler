Updated 2024-01-18
# Viewing Backend Set Health Check Parameters
On Compute Cloud@Customer, you can view the parameters used by the backend set of an existing load balancer to check the health of the backend servers in the set.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-backend-set-health-check-parameters.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-backend-set-health-check-parameters.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-backend-set-health-check-parameters.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the load balancer for which you want to view the backend set health status. 
    4. Under **Resources** , click **Backend Sets**.
    5. Click the name of the backend set to view its health check details, such as OK or Critical, among others.
  * Use the [oci lb backend-set-health get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend-set-health/get.html) command and required parameters to view the parameters used by the backend set of an existing load balancer to check the health of the backend servers in the set.
Copy
```
oci lb backend-set-health get --backend-set-name  _**backend-set-name-text**_ \
 --load-balancer-id _**load-balancer_OCID**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [GetBackendSetHealth](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/BackendSetHealth/GetBackendSetHealth) operation to view the parameters used by the backend set of an existing load balancer to check the health of the backend servers in the set.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

