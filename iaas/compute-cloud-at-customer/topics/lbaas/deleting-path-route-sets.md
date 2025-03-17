Updated 2024-01-18
# Deleting Path Route Sets
On Compute Cloud@Customer, you can delete a path route set for a load balancer resource. 
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-path-route-sets.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-path-route-sets.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-path-route-sets.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Select the name of load balancer for which to delete the path route set. 
    4. Under **Resources** , click **Path Route Sets**.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete**.
    6. Click **Confirm**.
  * Use the [oci lb path-route-set delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/path-route-set/delete.html) command and required parameters to delete a path route set resource.
Copy
```
oci lb path-route-set delete --load-balancer-id  _**load-balancer_OCID**_ 
--path-route-set-name _**name-of-path-route-set**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeletePathRouteSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/PathRouteSet/DeletePathRouteSet) operation to delete a path route set resource.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

