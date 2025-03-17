Updated 2024-01-18
# Viewing a Load Balancer Backend Server
On Compute Cloud@Customer, you can view a list of the backend servers in an existing load balancer backend set and view their details.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-a-load-balancer-backend-server.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-a-load-balancer-backend-server.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-a-load-balancer-backend-server.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the load balancer for which you want to list backend servers. 
    4. Under **Resources** , click the name of the backend set to view its details, such as IP address, port, and weight. 
  * Use the [oci lb backend list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend/list.html) command and required parameters to view a list of the backend servers in an existing load balancer backend set and view their details.
```
oci lb backend list --backend-set-name _**backend-set-name**_ \
--load-balancer-id _**load-balancer_OCID**_ 
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListBackend](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Backend/ListBackends) operation to view a list of the backend servers in an existing load balancer backend set and view their details.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

