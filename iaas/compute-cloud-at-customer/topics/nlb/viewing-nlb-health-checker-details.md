Updated 2024-01-18
# Viewing NLB Health Checker Status Details
On Compute Cloud@Customer, you can view the health status details of a network load balancer (NLB).
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-nlb-health-checker-details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-nlb-health-checker-details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-nlb-health-checker-details.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Network Load Balancers**.
    2. At the top of the page, select the compartment that contains the NLB.
    3. Click the name of the NLB for which you want to view existing load balancer backend set health parameters. 
    4. Under **Resources** , click **Backend Sets**.
    5. Click the name of the Backend Set to view its health check details.
  * Use the [oci nlb health-checker get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/health-checker/get.html) command and required parameters to see the health status details for the specified network load balancer.
Copy
```
oci nlb network-load-balancer-health get [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [GetNetworkLoadBalancerHealth](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/NetworkLoadBalancerHealth/GetNetworkLoadBalancerHealth) operation to get the health status details for the specified network load balancer.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

