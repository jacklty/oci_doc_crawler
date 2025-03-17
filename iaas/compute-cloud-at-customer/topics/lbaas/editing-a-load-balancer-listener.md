Updated 2024-01-18
# Editing a Load Balancer Listener
On Compute Cloud@Customer, you can change load balancer (LB) listener properties, such as the listener communication port used.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer-listener.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer-listener.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer-listener.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Under **Resources** , click **Listeners**.
    4. Click the name of the load balancer listener that you want to edit. 
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    6. Make allowable changes to the listener in the dialog box. 
    7. Click **Update Load Balancer Listener**.
  * Use the [oci lb listener update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/listener/update.html) command and required parameters to change load balancer listener properties, such as the listener communication port used load.
Copy
```
oci lb listener update --default-backend-set-name  _**[default-backendset-name]**_ \ 
--listener-name _**[listener-name]**_ --load-balancer-id _**[loadbalancer_OCID]**_\
--port _**[port-integer]**_ --protocol _**[protocol-text]**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateListener](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Listener/UpdateListener) operation to change load balancer listener properties.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

