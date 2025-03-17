Updated 2024-01-18
# Editing Load Balancer Health Check Properties
On Compute Cloud@Customer, you can change load balancer (LB) and backend server set health check properties, such as the health check interval.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-load-balancer-health-check.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-load-balancer-health-check.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-load-balancer-health-check.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the load balancer for which you want to edit existing backend set health check parameters. 
    4. Under **Resources** , click **Backend Sets**.
    5. To edit the health check parameters of a backend set, do one of the following actions:
      1. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
      2. Click the backend set to view its details, then click **Edit**.
    6. Click **Save**.
  * Use the [oci lb health-checker update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/health-checker/update.html) command and required parameters to change load balancer (LB) and backend server set health check properties, such as the health check interval.
Copy
```
oci lb health-checker update --backend-set-name [ _**name-of-backend-set**_] \
 --interval-in-millis [_**integer-in-millis**_] \ 
 --load-balancer-id [_**loadbalancer_OCID**_] --port [_**port-integer**_] \
 --protocol [_**protocol-text**_] --response-body-regex [_**expression-text**_] \ 
 --retries [_**retries-integer**_] --return-code [_**rc-integer**_] \ 
 --timeout-in-millis [_**integer-in-millis**_] 
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * This task is not available in the API.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

