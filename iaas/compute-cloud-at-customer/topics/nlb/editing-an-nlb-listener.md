Updated 2024-01-18
# Editing an NLB Listener
On Compute Cloud@Customer, you can update a listener's configuration for a network load balancer (NLB).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/editing-an-nlb-listener.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/editing-an-nlb-listener.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/editing-an-nlb-listener.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Network Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the Network Load Balancer for which you want to edit listeners.
    4. Under **Resources** , click **Listeners**.
    5. Select the name of the NLB listener that you want to edit. 
    6. For the NLB listener you want to edit, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    7. Make allowable changes to the listener in the dialog box. 
    8. Click **Update Network Load Balancer Listener**.
  * Use the [oci nlb listener update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/listener/update.html) command and required parameters to update a listener for a particular network load balancer.
Copy
```
oci nlb listener update [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateListener](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/Listener/UpdateListener) operation to update a listener for a particular network load balancer.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

