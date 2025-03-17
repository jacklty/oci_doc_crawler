Updated 2024-01-18
# Deleting a Load Balancer Backend Server
On Compute Cloud@Customer, you can delete a load balancer (LB) backend server from a backend set and remove it from service. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-a-load-balancer-backend-server.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-a-load-balancer-backend-server.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-a-load-balancer-backend-server.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the load balancer for which you want to delete the backend server.
    4. Under **Resources** , click **Backend Sets**.
    5. Click the name of the backend set that contains the backend server you want to delete.
    6. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Terminate**.
    7. Confirm the deletion.
  * Use the [oci lb backend delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend/delete.html) command and required parameters to remove a backend server from a given load balancer and backend set.
Copy
```
oci lb backend delete --backend-name  _**backend_server_name**_ --backend-set-name _**backendset_name**_ \
--load-balancer-id _**load-balancer_OCID**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteBackend](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Backend/DeleteBackend) operation to remove a backend server from a given load balancer and backend set.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

