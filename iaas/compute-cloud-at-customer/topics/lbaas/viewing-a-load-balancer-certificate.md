Updated 2024-08-06
# Viewing a Load Balancer Certificate
On Compute Cloud@Customer, you can view a public SSL certificate used with a load balancer. Certificates are one of the resources listed for a load balancer. You can't edit any of the details. To change a certificate, you delete the old one and create another one.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-a-load-balancer-certificate.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-a-load-balancer-certificate.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/viewing-a-load-balancer-certificate.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the LB for which you want to view the certificate.
    4. Under **Resources** , click **Certificates**.
All the details of the configured certificates are displayed.
  * Use the [oci lb certificate list](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/certificate/list.html) command and required parameters to a view the public SSL certificate used with a load balancer.
Copy
```
oci lb certificate list --load-balancer-id <load-balancer_OCID>
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [ListCertificate](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Certificate/ListCertificates) operation to a view the public SSL certificate used with a load balancer.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

