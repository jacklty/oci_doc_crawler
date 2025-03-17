Updated 2023-08-16
# SSL Traffic Handling Configuration
On Compute Cloud@Customer, you can configure a load balancer to handle SSL traffic in different ways at different stages of the secured connection.
## Terminating SSL at the Load Balancer
This configuration is known as _frontend SSL_. Your load balancer can accept encrypted traffic from a client. No encryption of traffic exists between the load balancer and the backend servers.
To terminate SSL at the load balancer, you must create a listener at a port such as 443, and then associate an uploaded certificate bundle with the listener.
## Implementing Backend SSL
In a _backend SSL_ configuration, the load balancer does not accept encrypted traffic from client servers. Traffic between the load balancer and the backend servers is encrypted.
To implement SSL between the load balancer and your backend servers, you must associate an uploaded certificate bundle with the backend set.
If you want to have more than one backend server in the backend set, sign your backend servers with an intermediate CA certificate. The intermediate CA certificate must be included as part of the certificate bundle.
Your backend services must be able to accept and terminate SSL.
## Implementing Point-to-Point SSL
In a _point-to-point SSL_ configuration, the load balancer accepts SSL-encrypted traffic from clients and encrypts traffic to the backend servers.
To implement point-to-point SSL, you must associate uploaded certificate bundles with both the listener and the backend set.
Was this article helpful?
YesNo

