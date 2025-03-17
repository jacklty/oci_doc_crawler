Updated 2024-01-18
# Creating am NLB Listener
On Compute Cloud@Customer, you can create a listener for an existing network load balancer (NLB). The listener waits for traffic to arrive for an IP address and distributes the traffic to the backend set servers. To handle traffic, you must configure at least one listener for each traffic type. When you create a listener, you must ensure that your VCN security rules allow the listener to accept traffic. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-am-nlb-listener.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-am-nlb-listener.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/creating-am-nlb-listener.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Network Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the Network Load Balancer for which you want to create the listener. 
Any existing listeners are listed under the NLB Resources information, otherwise the list displays **No data available**.
    4. Click **Create Listener**.
    5. Enter the following information: 
       * **Name:** Enter a descriptive name for the Listener. Avoid entering confidential information.
       * **Protocol:** Select TCP from the drop-down list.
       * **Port:** The default port value 22 for TCP is preselected. Use the up or down arrows to change the port value, or enter a value between 1 and 65,535. 
       * **Backend Set:** Select the backend set for the listener from the drop-down list. If the value is **None Available** , then you haven't yet created any NLB backend sets and must do so before this parameter can be configured. 
       * **IP Version:** The default IP Version 4 is preselected. 
    6. Click **Create Listener**. 
To display the details of the listener, you view the details for the network load balancer. See [Viewing NLB Details](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-nlb-details.htm#viewing-nlb-details "On Compute Cloud@Customer, you can view a list of existing network load balancers \(NLBs\) and view their details.").
  * Use the [oci nlb listener create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/listener/create.html) command and required parameters to add a listener to a network load balancer.
Copy
```
oci nlb listener create [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateListener](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Listener/CreateListener) operation to add a listener to a network load balancer.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

