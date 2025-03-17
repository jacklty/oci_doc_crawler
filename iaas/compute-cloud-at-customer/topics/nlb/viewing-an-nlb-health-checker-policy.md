Updated 2024-01-18
# Viewing an NLB Health Checker Policy
On Compute Cloud@Customer, you can view the health checker policy parameters used by a network load balancer (NLB) to check backend set health.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-an-nlb-health-checker-policy.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-an-nlb-health-checker-policy.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/viewing-an-nlb-health-checker-policy.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Network Load Balancers**.
    2. At the top of the page, select the compartment that contains the NLB.
    3. Click the name of the NLB for which you want to view heath check policy. 
    4. Under **Resources** , click **Backend Sets**.
    5. Click the name of the backend set.
    6. Under the backend-set name for which to you want to view the health check policy, click **Backend Set Configuration**.
  * Use the [oci nlb health-checker get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/nlb/health-checker/get.html) command and required parameters to see the health check policy information for a particular network load balancer and backend set.
Copy
```
SYNTX [OPTIONS]
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [GetHealthChecker](https://docs.oracle.com/iaas/api/#/en/networkloadbalancer/20200501/HealthChecker/GetHealthChecker) operation to get the health check policy information for a particular network load balancer and backend set.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

