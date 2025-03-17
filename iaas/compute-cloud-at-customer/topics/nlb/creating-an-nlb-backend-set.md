Updated 2024-04-19
# Creating an NLB Backend Set
On Compute Cloud@Customer, you can create a backend set for an existing network load balancer (NLB). The backend set is a group of servers to which network traffic is load balanced. You can create backend servers _after_ you create the backend set, or at the same time. This topic creates only the backend set.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-an-nlb-backend-set.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-an-nlb-backend-set.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-an-nlb-backend-set.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Network Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the Network Load Balancer for which you want to create the network load balancer backend set. 
    4. Under **Resources** , click **Backend Sets**.
Any existing backend sets are listed, otherwise the list says **No data available**
    5. Click **Create Backend Set**.
    6. Enter the following information: 
       * **Name:** Specify a friendly name for the backend set. It must be unique within the network load balancer, and can't be changed. Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names can't contain spaces. Avoid entering confidential information.
       * **Load Balancing Policy:** The IP Hash policy uses an incoming request's source IP address as a hashing key to route "non-sticky" traffic to the same backend server. The load balancer routes requests from the same client to the same backend server as long as that server is available. This policy honors server weight settings when establishing the initial connection. Select one of the following load balancing policies: 
         * **5-Tuple hash:** This policy distributes incoming traffic based on 5-Tuple (source IP and port, destination IP and port, protocol) IP Hash. 
         * **3-Tuple hash:** This policy ensures that requests from a particular client are always directed to the same backend server based on 3-Tuple (source IP, destination IP, protocol) IP Hash. 
         * **2-Tuple hash:** This policy routes incoming traffic to the same backend server based on 2-Tuple (Source/Destination) IP Hash.
       * **Source Header Preservation:** The default value can't be changed.
       * **IP Protocol Version:** The network load balancer listener and backend set must use the same IP protocol version. Accepted values are: IPV4. 
       * **Health Check:** Specify the parameters to confirm the health of backend servers in the set:
         * **Protocol:** Enter the protocol: TCP or HTTP. HTTP is valid for NLB health checks. When using TCP as the protocol, you can optionally provide the request data and the response data. 
         * **Port:** Specify the backend server port against which to run the health check. You can enter the value '0' to have the health check use the backend server's traffic port. 
         * **Internal in MS:** Specify how often to run the health check in milliseconds. The default value is 10000 (10 seconds).
         * **Timeout in MS:** Specify the maximum time in milliseconds to wait for a reply to a health check. A health check is successful only if a reply returns within this timeout period. The default is 3000 (3 seconds).
         * **Number of Retries:** Specify the number of retries to try before a backend server is considered "unhealthy." This number also applies when recovering a server to the "healthy" state. The default is 3.
         * **Status Code:** Specify the status code a healthy backend server must return.
         * **URL Path (URI):** Specify a URL endpoint against which to run the health check. 
         * **Response Body Regex:** Provide a regular expression for parsing the response body from the backend server.
    7. Click **Create Backend Set**. 
To display the details of the new backend set, view the backend set.
  * Use the [oci nlb backend-set create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/backend-set/create.html) command and required parameters to add a backend set to a network load balancer.
Copy
```
oci nlb backend-set create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateBackendSet](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/BackendSet/CreateBackendSet) operation to add a backend set to a network load balancer.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

