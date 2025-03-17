Updated 2024-08-06
# Creating a Load Balancer Backend Set
On Compute Cloud@Customer, you can create a backend set for an existing load balancer. The backend set is a group of servers to which traffic is load balanced. You can create backend servers _after_ you create the backend set, or at the same time. This section creates only the backend set. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-backend-set.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-backend-set.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-backend-set.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the Load Balancer for which you want to create the load balancer backend set. 
    4. Under **Resources** , click **Backend Sets**.
Any existing backend sets are listed, otherwise the list says **No data available**.
    5. Click **Create Backend Set**.
    6. Enter the following information: 
       * **Name:** Enter a descriptive name for the LB backend set. This must be unique and can't be changed.
       * **Traffic Distribution Policy:** Select load balancer policy for the backend set. Possible values are: 
         * **Weighted Round Robin:** Traffic is balanced in a "next turn" fashion, with some servers having a preference.
         * **Least Connections:** Traffic is balanced based on the server with the fewest current connections.
         * **IP Hash:** Traffic is balanced based on a hash of several fields in the IP header.
       * **Session Persistence:** Select the box to enable session persistence.
       * **SSL:** Select the box to use SSL with the backend set. 
       * **Health Checking:** Enter the health checking parameters for the backend set. 
         * **Protocol:** Choose the protocol that the health checker monitors. Possible values are: HTTP or TCP.
         * **Port:** Enter the port that the protocol uses.
         * **Interval in Milliseconds:** Enter a number between 1 and 1,800,000 for the health check interval.
         * **Timeout in Milliseconds::** Enter a number between 1 and 600,000 for the health check timeout.
         * **Number of Retries:** Enter the number of health check retries.
         * **Status Code:** Enter the numeric value that the health check uses.
         * **URL Path:** Enter the URL path, such as `/.` that the health checker monitors.
         * **Response Body:** Enter the response body regex, such as` .*`, that the health checker uses.
    7. Click **Create Backend Set**. 
  * Use the [oci lb backend-set create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend-set/create.html) command and required parameters to create a backend set for an existing load balancer.
Copy
```
oci lb backend-set create --health-checker-protocol  _**health-checker-protocol-name**_ \
 --load-balancer-id _**load-balancer_OCID**_ \ 
 --name _**backend-set-name**_ --policy _**load-balancer-policy**_ --backends \ 
 _**backends-info-complex-type**_ --health-checker-port _**port-number**_ \ 
 --health-checker-response-body-regex _**regex**_ --health-checker-return-code _**code-number**_ 
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateBackendSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/BackendSet/CreateBackendSet) operation to create a backend set for an existing load balancer.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

