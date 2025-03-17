Updated 2024-01-18
# Editing Path Route Sets
On Compute Cloud@Customer, you can edit a path route set to update the details. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-path-route-sets.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-path-route-sets.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-path-route-sets.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of load balancer for which to update the path route set details. 
    4. Under **Resources** , click **Path Route Sets**.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Edit**.
    6. Click **Save Changes**.
  * Use the [oci lb path-route-set update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/path-route-set/update.html) command and required parameters to update path route set details for a load balancer resource.
Copy
```
oci lb path-route-set update --load-balancer-id  _**load-balancer_OCID**_ 
--path-route-set-name _**name-of-path-route-set**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdatePathRouteSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/PathRouteSet/UpdatePathRouteSet) operation to change the specified path route set’s configuration information.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

