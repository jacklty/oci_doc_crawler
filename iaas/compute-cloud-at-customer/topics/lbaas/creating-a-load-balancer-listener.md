Updated 2024-01-18
# Creating a Load Balancer Listener
On Compute Cloud@Customer, you can create a listener for an existing load balancer (LB).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-listener.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-listener.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-listener.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the Load Balancer for which you want to create the listener. 
Any existing listeners are listed under the Load Balancer Information, otherwise the list says **No data available**.
    4. Click **Create Listener**.
    5. Enter the following information: 
       * **Name:** Enter a descriptive name for the Listener.
       * **Protocol:** Select the protocol (HTTP, TCP) to listen for from the drop-down list.
       * **Port:** The default port value 80 for the listener is preselected. Use the up or down arrows to change the port value, or enter a value between 1 and 65,535. 
       * **Hostnames:** Select the hostnames for the listener from the pull-down list. If the value is **None Available** , then you haven't yet created any LB hostnames and must do so before this parameter can be configured. 
       * **Backend Set:** Select the backend set for the listener from the pull-down list. If the value is **None Available** , then you haven't yet created any LB backend sets and must do so before this parameter can be configured. 
       * **Idle Timeout in Seconds:** The default value 60 seconds for the listener is preselected. Use the up or down arrows to change the idle timeout value, or enter a value greater than or equal to 1. 
    6. Click **Create Listener**. 
To display the details of the listener, you must view the details for the entire load balancer.
  * Use the [oci lb listener create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/listener/create.html) command and required parameters to create a listener for an existing load balancer. You must list the traffic protocols that the load balancer accepts before you create the listener.
Copy
```
oci lb listener create --default-backend-set-name  _**backend-set-name**_ \
--load-balancer-id _**load-balancer_OCID**_ \ 
--name _**listener-name**_ --port _**listener-port**_ \
--protocol _**listener-protocol**_ 
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateListener](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Listener/CreateListener) operation to create a listener for an existing load balancer. 
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

