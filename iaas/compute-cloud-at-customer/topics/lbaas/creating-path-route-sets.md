Updated 2024-01-18
# Creating Path Route Sets
On Compute Cloud@Customer, you can create a path route set for a LBaaS resource to distinguish by unique URL paths such as `/admin/`, `/data/`, `/video/`, or `/cgi/`.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-path-route-sets.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-path-route-sets.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-path-route-sets.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of load balancer for which to create the path route set. 
    4. Under **Resources** , click **Path Route Sets**.
    5. Click **Create Path Route Set**.
    6. Enter the following information:
       * **Name:** Enter a descriptive name for the Path Route Set.
       * **Path Route Rules:** Enter the following required information for Path Route Rule 1.
         * **Match Style:** Select Exact Match, Force Longest Prefix Match, Prefix Match, or Suffix Match. 
         * **URL String:** Enter the pattern that the style seeks to match. 
         * **Backend Set:** Select the name of the backend set from the drop-down list. If you haven't yet created a backend set, you can't create a path route set. 
       * **+New Rule:** Select this option if you want to create more than one rule for the path route set.
    7. Click **Create Path Route Set**. 
  * Use the [oci lb path-route-set create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/path-route-set/create.html) command and required parameters to create a path route set for a load balancer resource to distinguish by unique URL paths such as `/admin/`, `/data/`, `/video/`, or `/cgi/`.
Copy
```
oci lb path-route-set create --name  _**name-of-path-route-set**_ \
--path-routes _**[COMPLEX-TYPE]**_ --load-balancer-id _**load-balancer_OCID**_ 
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreatePathRouteSet](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/PathRouteSet/CreatePathRouteSet) operation to add a path route set to a load balancer.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

