Updated 2024-10-07
# Frontend Configuration
Compute Cloud@Customer supports different types of load balancers. 
In the context of load balancers, the term _frontend_ refers to the components that a client can see and send requests to. The entry point of client requests is the outward-facing floating IP address of the load balancer. Incoming traffic is checked by listeners, which are configured for specific protocols and ports. Different types of rules can be defined to categorize incoming requests and route them accordingly to different sets of backend servers.
## Load Balancer Types 🔗 
The Load Balancing service allows you to create a public or private load balancer within a VCN. Load balancers are deployed in pairs: one active and one standby instance sharing a floating IP address. A public load balancer has a public IP address that's accessible from outside the Compute Cloud@Customer network environment. A private load balancer has an IP address from the hosting subnet, which is visible only within the VCN.
You can configure multiple listeners for an IP address to load balance transport Layer 4 and Layer 7 (TCP and HTTP) traffic. Both public and private load balancers act as reverse proxies and can route data traffic to any backend server that's reachable from the VCN.
All load balancers have a backend set to route incoming traffic to compute instances. The backend set is a logical entity that includes:
  * a list of backend servers
  * a load balancing policy
  * a health check policy
  * (optional) SSL handling
  * (optional) session persistence configuration


The backend servers – compute instances – associated with a backend set can exist anywhere, as long as the associated network security groups (NSGs), security lists, and route tables allow the intended traffic flow.
## Private Load Balancer 🔗 
To isolate a load balancer from the external network and simplify its security posture, you can create a private load balancer. The Load Balancing service assigns it a private IP address that serves as the entry point for incoming traffic.
When you create a private load balancer, the service requires only one subnet to host both the primary and standby load balancers. The load balancer is accessible only from within the VCN that contains the host subnet, or as further restricted by security rules.
The assigned floating private IP address is local to the host subnet. The primary and standby load balancers each require an extra private IP address from the host subnet.
See [Creating a Private Load Balancer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-private-load-balancer.htm#creating-a-private-load-balancer "On Compute Cloud@Customer, when creating a load balancer \(LB\), you have two main options: you can provide minimal information when creating the LB and then add other resources later, or you can provide all of the information when creating the LB.").
## Public Load Balancer 🔗 
To accept traffic from a network location outside of Compute Cloud@Customer, you create a public load balancer. A public load balancer must be deployed in a public subnet of a VCN that has an internet gateway configured. The service assigns the load balancer a public IP address that serves as the entry point for incoming traffic. You can associate the public IP address with a friendly DNS name through any DNS provider.
A Compute Cloud@Customer is a single Availability Domain by definition, which implies that the primary and standby load balancers can't be deployed in separate Availability Domains. Therefore, both the primary and standby load balancer are deployed in the same subnet, and they each are assigned a private IP address from that host subnet. In addition, a load balancer uses one floating public IP address that can be reassigned between standby and primary as required.
See [Creating a Public Load Balancer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/creating-a-public-load-balancer.htm#creating-a-public-load-balancer "On Compute Cloud@Customer, when creating a load balancer \(LB\), you have two main options: you can provide minimal information when creating the LB and then add other resources later, or you can provide all of the information when creating the LB.").
Was this article helpful?
YesNo

