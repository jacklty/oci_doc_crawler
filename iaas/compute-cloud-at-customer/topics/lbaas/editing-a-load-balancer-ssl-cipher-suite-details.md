Updated 2024-01-18
# Editing a Load Balancer SSL Cipher Suite Details
On Compute Cloud@Customer, you can edit the SSL cipher suites associated with an existing load balancer to alter their details by adding or removing values.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer-ssl-cipher-suite-details.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer-ssl-cipher-suite-details.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/editing-a-load-balancer-ssl-cipher-suite-details.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the Load Balancer that has the cipher suite you want to edit. 
    4. Under **Resources** , click **Cipher Suites**.
The cipher suites are displayed.
    5. Click the name of the cipher suite to display the details, then click **Edit**.
    6. Edit the cipher.
    7. Click **Update ciphers**.
  * Use the [oci lb ssl-cipher-suite update](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/ssl-cipher-suite/update.html) command and required parameters to update the details of a load balancer SSL cipher suite.
Copy
```
oci lb ssl-cipher-suite update --load-balancer-id  _**load-balancer_OCID**_ 
  --name _**cipher-suite-name**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [UpdateSSLCipherSuire](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/SSLCipherSuite/UpdateSSLCipherSuite) operation to update the details of a load balancer SSL cipher suite.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

