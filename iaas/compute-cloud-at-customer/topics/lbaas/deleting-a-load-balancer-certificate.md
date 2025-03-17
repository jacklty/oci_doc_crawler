Updated 2024-01-18
# Deleting a Load Balancer Certificate
On Compute Cloud@Customer, you can delete a public SSL certificate associated with an existing load balancer.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-a-load-balancer-certificate.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-a-load-balancer-certificate.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/deleting-a-load-balancer-certificate.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the LB for which you want to delete the certificate.
    4. Under **Resources** , click **Certificates**. 
The configured certificates are displayed.
    5. Click the Actions menu (![An image of the three dot icon.](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/images/three-dots.png)), then click **Delete**.
    6. Confirm the deletion.
  * Use the [oci lb certificate delete](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/certificate/delete.html) command and required parameters to delete a public SSL certificate associated with a load balancer
Copy
```
oci lb certificate delete --certificate-name  _**certificate_name**_ \ 
--load-balancer-id _**load-balancer_OCID**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [DeleteCertificate](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Certificate/DeleteCertificate) operation to delete the public SSL certificate used with a load balancer.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

