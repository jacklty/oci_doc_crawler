Updated 2024-01-18
# Editing a Load Balancer Backend Set
On Compute Cloud@Customer, you can change load balancer (LB) backend set properties, such as the health checker protocol used. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer-backend-set.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer-backend-set.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer-backend-set.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the load balancer for which you want to edit the backend set information.
    4. Under **Resources** , click **Backend Sets**.
    5. For the LB backend set that you want to edit, click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    6. Make allowable changes in the dialog box. 
    7. Click **Update Load Balancer Backend Set**.
  * Use the [oci lb backend-set update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/backend-set/update.html) command and required parameters to change load balancer (LB) backend set properties, such as the health checker protocol used.
Copy
```
oci lb backend-set update --load-balancer-id  _**loadbalancer_OCID**_ \
--backend-set-name _**[backendset_name]**_ \ 
--backends _**[complex-type]**_ --health-checker-protocol _**[protocol]**_ \
--policy _**[IP_HASH [OPTIONS]**_ 
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateBackendSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/BackendSet/UpdateBackendSet) operation to change load balancer backend set properties.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

