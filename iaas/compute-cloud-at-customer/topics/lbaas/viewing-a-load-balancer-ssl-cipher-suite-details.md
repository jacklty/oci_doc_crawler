Updated 2024-01-18
# Viewing a Load Balancer SSL Cipher Suite Details
On Compute Cloud@Customer, you can view a list of the SSL cipher suites associated with an existing load balancer and view their details.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-a-load-balancer-ssl-cipher-suite-details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-a-load-balancer-ssl-cipher-suite-details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-a-load-balancer-ssl-cipher-suite-details.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the Load Balancer for which you want to list existing load balancer cipher suites. 
    4. Under **Resources** , click **Cipher Suites**.
The list of cipher suites is displayed.
    5. If cipher suites exist, you can view the details in one of two ways:
      1. Click the name of the cipher suite.
      2. In the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), click **View Details**.
  * Use the [oci lb ssl-cipher-suite get](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/ssl-cipher-suite/get.html) command and required parameters to view a load balancer SSL cipher suite details.
Copy
```
oci lb ssl-cipher-suite get --load-balancer-id  _**load-balancer_OCID**_ --name _**cipher-suite-name**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [GetSSLCipherSuite](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/SSLCipherSuite/GetSSLCipherSuite) operation to get a load balancer SSL cipher suite details.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

