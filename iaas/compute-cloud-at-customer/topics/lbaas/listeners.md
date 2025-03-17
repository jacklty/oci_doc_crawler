Updated 2023-08-16
# Listeners
On Compute Cloud@Customer, 
The listener is a logical entity at the ingress side of the load balancer setup. It’s the key component that detects incoming traffic on the load balancer IP address. It listens for requests from clients using a particular protocol and port. Requests are subsequently routed to the appropriate backend servers based on the rules defined in the load balancer configuration. To handle TCP, HTTP, and HTTPS traffic, you must configure at least one listener per traffic type. 
When you create a listener, ensure that your VCN security rules allow the listener to accept traffic.
**Note**
To accommodate high-volume traffic, we recommend that you use _stateless_ security rules for your load balancer subnets. 
You can have one SSL certificate bundle per listener. You can configure two listeners, one each for ports 443 and 8443, and associate SSL certificate bundles with each listener. For more information about SSL certificates for load balancers, see [Load Balancer SSL Certificates](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/load-balancer-ssl-certificates.htm#load-balancer-ssl-certificates "On Compute Cloud@Customer, you can import and manage SSL certificates through the Load Balancing service, but the service doesn't generate any certificates.").
Was this article helpful?
YesNo

