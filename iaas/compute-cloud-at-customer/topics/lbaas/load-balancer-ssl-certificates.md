Updated 2025-02-21
# Load Balancer SSL Certificates
On Compute Cloud@Customer, you can import and manage SSL certificates through the Load Balancing service, but the service doesn't generate any certificates.
An SSL certificate can be one issued by a vendor such as VeriSign or GoDaddy, or a self-signed certificate that you generate with a tool like OpenSSL or Let's Encrypt.
**Attention**
You can use a custom, self-signed SSL certificate. However, for production environments, Oracle recommends that you use a CA-issued SSL certificate, which reduces the risk of a man-in-the-middle attack.
If you configure HTTPS or SSL for a listener, an SSL server certificate must be associated with the load balancer. A certificate enables the load balancer to terminate the connection and decrypt incoming requests before passing them to the backend servers. You can apply the following SSL configurations to your load balancer:
  * **SSL termination:** The load balancer handles incoming SSL traffic and passes the unencrypted request to a backend server.
  * **Point-to-point SSL:** The load balancer terminates the SSL connection with an incoming traffic client, and then initiates an SSL connection to a backend server.
  * **SSL tunneling:** If you configure the load balancer listener for TCP traffic, the load balancer tunnels incoming SSL connections to your application servers.


Load Balancing supports the TLS 1.2 protocol with a default setting of strong cipher strength.
To use standard SSL with a load balancer and its resources, you must supply a certificate. To use mutual TLS (mTLS) with your load balancer, you must add one or more certificate authority bundles (CA bundles) to your system. A certificate bundle includes the public certificate, the corresponding private key, and any associated Certificate Authority (CA) certificates. We recommend that you upload the certificate bundles before creating the listeners or backend sets you want to associate them with. Only X.509 certificates in PEM format are accepted. 
Load balancers commonly use single domain certificates. However, load balancers with listeners that include request routing configuration might require a subject alternative name (SAN) certificate (also called multidomain certificate) or a wildcard certificate. The Load Balancing service supports each of these certificate types.
Was this article helpful?
YesNo

