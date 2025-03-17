Updated 2024-10-07
# LBaaS Security
On Compute Cloud@Customer, you can configure and secure the Load Balancer as a Service (LBaaS).
A load balancer (LB) connects a client’s applications and a customer’s VCN. LBs use TLS1.2 by default. You can configure LBs to use Compute Cloud@Customer public or private IP addresses.
Compute Cloud@Customer LBs use TLS and SSL for security. You can create LBs with one of three different types of connections:
  * **SSL Termination:** The load balancer handles incoming SSL traffic and passes the unencrypted request to a backend server.
  * **End-to-End (Point-to-Point) SSL:** The load balancer ends the SSL connection from an incoming traffic client, and then initiates another SSL connection to a backend server.
  * **SSL Tunneling:** If the load balancer listener is configured for TCP traffic, the load balancer tunnels incoming SSL connections to the application servers.


You can configure LBs with two types of protocols:
  * **HTTP:** LBs using HTTP or HTTPS end the TLS connection at the LB itself.
  * **TCP:** LBs using TCP end the TLS connection at a backend server.


LBs listen to an IP address for these types of protocols. 
For information about managing the LBaaS service, see [Load Balancer as a Service](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/load-balancer-as-a-service.htm#load-balancer-as-a-service "On Compute Cloud@Customer, you can configure the Load Balancing service \(LBaaS\) to automatically distribute network traffic.").
## SSL Certificates 🔗 
On Compute Cloud@Customer, LBaaS requires the use of secure certificates. You must supply a certificate to use standard SSL for the LBs and their resources. You can upload SSL certificates if none are available. 
**Note** We recommend that you upload the certificates you want to use before you create the listeners or backend sets you want to associate them with.
Compute Cloud@Customer LBaaS doesn't generate SSL certificates. It can only import an existing certificate that you already own. The certificate can be one issued by a vendor, such as Verisign or GoDaddy. You can also use a self-signed certificate that you generate with an open source tool, such as OpenSSL or Let's Encrypt. Refer to the corresponding tool's documentation for instructions on how to generate a self-signed certificate.
If you submit a self-signed certificate for backend SSL, you must submit the same certificate in the corresponding CA Certificate field.
Compute Cloud@Customer accepts x.509 type certificates in PEM format only. The following is an example PEM encoded certificate:
```
-----BEGIN CERTIFICATE-----
<Base64_encoded_certificate>
-----END CERTIFICATE-----
```

For more information about certificates, see [Managing SSL Certificates](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/ssl-certificates.htm#ssl-certificates "On Compute Cloud@Customer, you can use secure socket layer \(SSL\) certificates with your load balancer.").
## Security Lists 🔗 
On Compute Cloud@Customer, you use VCN network security groups (NSGs) or security lists to control network access to load balancers. This method provides the Compute Cloud@Customer with functionality similar to traditional LB firewalls. You configure the load balancer rules by configuring the NSGs or the subnet security lists for the LBs. 
When you create a listener, you must also update the VCN security list to permit traffic to that LB listener. 
The ingress rule for the security list must be edited to permit the following:
  * Source CIDR (Enter a block that covers the networks using the LB. Can be 0.0.0.0/0.)
  * Protocol TCP
  * Destination port range 80 (the listener port)


If you created other listeners, then you must add an ingress rule for each listener port to permit traffic to reach the listener. For example, if you created a listener on port 443, you must permit traffic for port 443.
For more information about NSGs and security lists, see [Controlling Traffic with Security Lists](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-security-lists.htm#controlling-traffic-with-security-lists "On Compute Cloud@Customer, both security lists and network security groups \(NSGs\) are types of virtual firewalls for your compute instances. Both security lists and NSGs define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).") and [Controlling Traffic with Network Security Groups](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/controlling-traffic-with-network-security-groups.htm#controlling-traffic-with-network-security-groups "On Compute Cloud@Customer, both network security groups \(NSGs\) and security lists are types of virtual firewalls for your compute instances. Both NSGs and security lists define network security rules that decide which types of traffic are allowed in and out of instances \(VNICs\).").
## Backend Server Security 🔗 
For public LBs on Compute Cloud@Customer, you must configure the VCN NSGs or security lists for the backend servers to accept traffic only for the public LBs. You can update the security lists used by the backend server subnets to permit ingress traffic from the LB subnet. 
For example, if the LB is in subnet 10.0.4.0/24 and you're balancing traffic for web servers, then you must add a stateful ingress rule to permit traffic from source IP address 10.0.4.0/24, using the TCP protocol, from all source ports, and to destination port 80. This new rule permits ingress traffic from the LB subnet.
VCN subnet Security Lists (or NSGs, if used) can be associated with an NSG and need to be updated after an LB, Listener and backends have been created. Typically a Load balancer would be created in a different subnet than the backend servers. For example, a public LB created in a public subnet forwards traffic to backend servers in a private subnet. 
However (though not recommended), the LB could be created in the same subnet as a backend server. In either case, the security lists for all subnets that involve the LB and backend servers need to be updated. 
For the LB subnet, the Security List (or NSG) must be updated to permit egress traffic from the load balancer to each backend server's subnet. For example if the backend servers are in Subnet1 (10.0.1.0/24) and Subnet2 (10.0.0.0/24), then updates to the security list for the LB subnet would be:
  * Allow egress traffic to the backend server on Subnet1
  * Allow egress traffic to the backend server on Subnet2


In addition to the updates to permit egress traffic to the backend subnets, updates must be made to permit the listener to accept traffic. For example, if a public LB permits traffic from anywhere to reach the LB on port 80, you must add the following ingress rule to the subnet that hosts the LB:
  * Source Type: CIDR
  * Source CIDR: 0.0.0.0/0
  * IP Protocol: TCP
  * Destination Port Range: 80 (listener port)


If the LB is in subnet 10.0.4.0/24, then stateful rule updates to the security lists used by the backend server subnets are needed to permit ingress traffic from the load balancer subnet: 
  * Source Type: CIDR
  * Source CIDR: 10.0.4.0/24
  * IP Protocol: TCP
  * Destination Port Range: 80 (listener port)


This new stateful ingress rule permits TCP traffic to reach the backend servers. The stateful nature permits responses.
Finally, delete all egress rules. There can be no egress rules for the backend servers.
## Route Table Considerations 🔗 
On Compute Cloud@Customer, the VCN route table must route requests to the various backend sets of the LB. You can assign a virtual hostname to a listener or create route rules for this purpose. 
For more information on these LB topics, see:
  * [Managing Virtual Hostnames](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/virtual-hostnames.htm#virtual-hostnames "On Compute Cloud@Customer, you can use virtual hostnames with a load balancer for one or more listeners.")
  * [Managing Listeners](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/managing-listeners.htm#managing-listeners "On Compute Cloud@Customer, you can use listeners to check for incoming traffic on the load balancer IP address.")
  * [Managing Backend Sets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/backend-sets.htm#backend-sets "On Compute Cloud@Customer, you an use backend sets to create logical entities consisting of a load balancing policy, health check policy, and a list of backend servers for a load balancer resource.")


For more information on route table configuration in general, see [Working with Route Tables](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/network/working-with-route-tables.htm#working-with-route-tables "On Compute Cloud@Customer,"). 
Was this article helpful?
YesNo

