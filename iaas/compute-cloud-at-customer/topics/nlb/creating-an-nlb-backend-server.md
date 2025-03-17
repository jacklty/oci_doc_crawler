Updated 2024-01-18
# Creating an NLB Backend Server
On Compute Cloud@Customer, you can create backend servers _after_ you create the backend set, or at the same time. This topic creates only the backend server.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-an-nlb-backend-server.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-an-nlb-backend-server.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-an-nlb-backend-server.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Network Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the Network Load Balancer for which you want to create the network load balancer backend server. 
    4. Under **Resources** , click **Backend sets**.
Any existing backend servers are listed, otherwise the list displays **No data available**. 
    5. Click the hyperlink of the BackendSet to add the backend.
    6. Click Create **Backend**.
    7. Select the method for adding the backend server. Possible values are: 
       * **Computed Instances** Backend servers are added by instance. 
       * **IP Addresses** Backend servers are added by instance IP address.
    8. For **Computed Instances** , enter the following information: 
       * **Instance:** Enter the name of the backend server.
       * **Port:** Enter 22 (TCP). 
       * **Name:** Leave blank to take the default (ip_address:port#).
       * **Weight:** Enter a weight in the range 1 to 100. 
       * **Security Rules:** Select the security rules of the backend. Possible values are:
         * **Configure Manually** You manually configure security rules for the backend.
         * **Configure Automatically** The system automatically configures security rules for the backend.
    9. For **IP Addresses** , enter the following information: 
       * **IP Address:** Enter the IP address of the backend server.
       * **Port:** Enter the port number. 
       * **Name:** Enter the name of the backend.
       * **Weight:** Enter a weight in the range 1 to 100. 
    10. Click **Submit**. 
  * Use the [oci nlb backend create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend/create.html) command and required parameters to add a backend server to a backend set.
Copy
```
oci nlb backend create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateBackend](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Backend/CreateBackend) operation to add a backend server to a backend set.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

