Updated 2024-08-06
# Editing a Load Balancer
On Compute Cloud@Customer, You can change load balancer (LB) properties, such as the name of the LB. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. For the load balancer you want to edit, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**. 
    4. In the dialog box, make allowable changes to the LB. The following property can be edited:
       * **Name:** Change the name of the LB.
    5. Click **Update Load Balancer**.
  * Use the [oci lb load-balancer update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/load-balancer/update.html) command and required parameters to edit load balancer properties.
Copy
```
oci lb load-balancer update --load-balancer-id  _**loadbalancer_OCID**_ \
 --display-name **_name-of-load-balancer_** 
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateLoadBalancer](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/LoadBalancer/UpdateLoadBalancer) operation to update a load balancer configuration.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

