Updated 2024-08-06
# Creating a Load Balancer Backend Server
On Compute Cloud@Customer, you can create a backend server to add to an existing load balancer backend set. A backend set is a group of backend servers to which traffic is load balanced. 
If the backend server resides in a different VCN as the load balancer, then you must set up a local peering gateway so the LB and backend servers can communicate.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-backend-server.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-backend-server.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-backend-server.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the load balancer for which you want to create a backend server.
    4. Under **Resources** , click **Backend Sets**.
    5. Click the name of the backend set. 
    6. On the Details page of the backend set, click **Create Backend**. 
    7. Enter the following information: 
       * **Computed Instances:** The system provides a list of instances for the backend server.
       * **IP Addresses:** You can add backend servers by IP address. You must also provide: 
         * **Port:** The server port to load balance.
         * **Weight:** The precedence assigned to this backend server within the group.
You can add more than one IP address by clicking +Add IP Address.
       * **Security Rules:** To enable load balancer traffic, you must add ingress and egress security list rules to the corresponding subnets. You can choose to configure the security rules manually or automatically. The default is to manually configure the security rules.
    8. Click **Submit**.
  * Use the [oci lb backend create](https://docs.oracle.com/iaas/tools/oci-cli/3.29.4/oci_cli_docs/cmdref/lb/backend/create.html) command and required parameters to create a backend server to add to an existing load balancer backend set.
Copy
```
oci lb backend create --backend-set-name  _**backend-server-set-name**_ \ 
--ip-address _**ip-addr-of-compute-instance**_ \ 
--load-balancer-id _**load-balancer_OCID**_ --port _**port-integer**_ 
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateBackend](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Backend/CreateBackend) operation to add a backend server to a backend set.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

