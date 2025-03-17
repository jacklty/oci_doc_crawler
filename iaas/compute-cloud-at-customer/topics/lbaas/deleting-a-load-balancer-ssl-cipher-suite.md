Updated 2023-10-19
# Deleting a Load Balancer SSL Cipher Suite
On Compute Cloud@Customer, you can delete an SSL cipher suite associated with an existing load balancer.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-a-load-balancer-ssl-cipher-suite.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-a-load-balancer-ssl-cipher-suite.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-a-load-balancer-ssl-cipher-suite.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the Load Balancer that has the cipher suite you want to edit. 
    4. In **Resources** , click **Cipher Suites**.
The cipher suites are displayed.
    5. You can delete a cipher suite in one of two ways:
      1. Click the name of the cipher suite to display the details, then click **Delete**.
      2. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)) for the particular cipher suite, then click **Delete**.
  * Use the [oci lb ssl-cipher-suite delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/ssl-cipher-suite/delete.html) command and required parameters to delete a load balancer cipher suite:
Command
CopyTry It
```
oci lb ssl-cipher-suite delete --load-balancer-id  _**load-balancer_OCID**_ 
  --name _**cipher-suite-name**_
```

For a complete list of flags and variable options for CLI commands, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteSSLCipherSuire](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/SSLCipherSuite/DeleteSSLCipherSuite) operation to delete a load balancer cipher suite.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

