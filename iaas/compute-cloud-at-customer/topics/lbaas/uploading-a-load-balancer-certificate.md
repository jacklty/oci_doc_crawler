Updated 2025-02-21
# Adding a Load Balancer Certificate
On Compute Cloud@Customer, you can add a public SSL certificate to use with a load balancer. 
Certificates are one of the resources listed for a load balancer. You can either upload the certificate as a **`.pem`**file, or paste the content from the**`.pem`**file directly into the creation dialog box using drag and drop. The certificates are stored in the Vault and you must have access to the vault to configure and use load balancer certificates.
Optionally, you can also provide a certificate for a Certificate Authority (CA) or configure a private key.
**Attention**
You can use a custom, self-signed SSL certificate. However, for production environments, Oracle recommends that you use a CA-issued SSL certificate, which reduces the risk of a man-in-the-middle attack.
  * [Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/uploading-a-load-balancer-certificate.htm)
  * [CLI](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/uploading-a-load-balancer-certificate.htm)
  * [API](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/uploading-a-load-balancer-certificate.htm)


  *     1. In the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure.") navigation menu, click **Networking** , then click **Load Balancers**.
    2. At the top of the page, select the compartment that contains the load balancer.
    3. Click the name of the LB for which you want to create the certificate.
    4. Under **Resources** , click **Certificates**. 
    5. Click **Create Certificate**.
    6. In the **Load Balancer Create Certificate** dialog box, enter the following information:
       * **Certificate Name:** Enter a name for the LB certificate. For example, my_new_certificate. 
Avoid entering confidential information
       * **Public certificate:** You can either upload, or paste the content from the SSL Certificate (`.pem` file).
       * **Certificate Authority:** Select the Enable certificate authority box if you're also using a certificate authority certificate. You can either upload, or Paste the content from the Certificate Authority certificate (`.pem` file).
       * **Private Key:** Select the Enable private key box if you're also using a private key certificate. You can either upload, or Paste the content from the private key (`.pem`) file.
    7. Click **Create Certificate**. 
  * Use the [oci lb certificate create](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/lb/certificate/create.html) command and required parameters to create a public SSL certificate to use with a load balancer.
Copy
```
oci lb certificate create --certicate-name  _**certificate-name**_ \ 
--load-balancer-id _**load-balancer_OCID**_ --certificate-file _**[path/to/file]**_
```

For a complete list of CLI commands, flags, and options, see the [Command Line Reference](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/index.html).
  * Use the [CreateCertificate](https://docs.oracle.com/iaas/api/#/en/loadbalancer/latest/Certificate/CreateCertificate) operation to create a load balancer certificate.
For information about using the API and signing requests, see [REST APIs](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm#REST_APIs) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm#Software_Development_Kits_and_Command_Line_Interface).


Was this article helpful?
YesNo

