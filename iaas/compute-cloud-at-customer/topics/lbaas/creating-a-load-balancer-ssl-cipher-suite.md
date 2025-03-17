Updated 2024-01-18
# Creating a Load Balancer SSL Cipher Suite
On Compute Cloud@Customer, a load balancer (LB) uses a cipher suite to secure Transport Layer Security (TLS) or Secure Socket Layer (SSL) network connections. The cipher suite defines a list of security algorithms that the load balancer uses to negotiate with peers exchanging information with the load balancer. The cipher suites used effect the security level, performance, and compatibility of data traffic.
A series of predefined cipher suites exist that you can use when you create an SSL configuration. If the predefined cipher suites don't meet requirements, you can create custom cipher suites.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-ssl-cipher-suite.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-ssl-cipher-suite.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-load-balancer-ssl-cipher-suite.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the Load Balancer for which you want to create the load balancer SSL cipher suite. 
    4. Under **Resources** , click **Cipher Suites**.
The list of available cipher suites appears. If none are listed, you must create one.
    5. To create a load balancer cipher suite, click **Create Cipher Suite**.
    6. In the **Load Balancer SSL Cipher Suite** dialog box, give the LB SSL cipher suite a name. For example, my_ssl_cipher_suite. 
**Note** The name of a user-defined cipher suite can't be the same as any of Oracle’s predefined or reserved SSL cipher suite names.
    7. Select the cipher suite components to be part of the SSL cipher suite. For example, **_AES256-SHA256_**.
    8. After you have selected all the components for the SSL cipher suite, click **Create Cipher Suite**. 
  * Use the [oci lb ssl-cipher-suite create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/ssl-cipher-suite/create.html) command and required parameters to create a load balancer SSL cipher suite.
Copy
```
oci lb ssl-cipher-suite create --ciphers  _**ssl_ciphers_complex_type**_ \ 
--load-balancer-id _**load-balancer_OCID**_ --name _**ssl_cipher_suite_name**_ 
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateSSLCipherSuite](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/SSLCipherSuite/CreateSSLCipherSuite) operation to create a load balancer SSL cipher suite.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

