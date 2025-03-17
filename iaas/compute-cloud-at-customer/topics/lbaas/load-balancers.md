Updated 2023-08-16
# Managing Load Balancers
On Compute Cloud@Customer, load balancing is the method of sharing a workload equally among servers.
Load balancing prevents clients from overwhelming certain servers and helps the service to scale. When a flexible load balancer process on a system is configurable and available to all clients and servers then it's called Load Balancer as a Service (LBaaS). 
LBaaS on Compute Cloud@Customer provides automated traffic distribution from one entry point to multiple servers reachable from the virtual cloud network (VCN). The service offers a load balancer with a choice of using a public or private IP address, and various load balancing policies.
When you create an LB using the OCI CLI, you can either configure all the resources at the same time or create a minimal LB and supply other configuration details later. In other words, more than the basic LB is needed to assemble the complete LB after creation. These other components are added by editing the LB resources.
The two type of load balancers are:
  * Private: A private load balancer is isolated from the network outside the Oracle Compute Cloud@Customer and security is therefore easier. A private load balancer gets a private IP address assigned from the address block that serves as the entry point for incoming traffic.
  * Public: A public load balancer accepts traffic from a network location outside of Compute Cloud@Customer. Because of this outside traffic, a public load balancer is deployed in a public subnet of a VCN that has an internet gateway (IGW) configured. The service assigns the load balancer a public IP address that serves as the entry point for incoming traffic. You can associate the public IP address with a friendly DNS name through any DNS provider, but a public IP address must be available in order for public load balancer provisioning to succeed.


This chapter creates load balancers with minimal information, using the Console, API, or OCI CLI, and then supplies the details for the other resources. An implied order can be used in the way things are configured in the Console (which differs from the LB resource listing) because some items must be configured before use in other places (for example, virtual hostnames are needed to complete listener configuration). After initial load balancer configuration, the order used in this section is:
  * Cipher Suites and SSL Certificates
  * Backend Sets and Backend Servers
  * Virtual Hostnames
  * Path Route Sets
  * Listeners


This section also includes other parameters and commands that relate to these major configuration steps that aren't LB resources. They include:
  * Backend-set health check
  * Backend (server) health check
  * LB health policy


This isn't an exhaustive list. 
In addition, many configuration steps are processed as work requests. Work requests are tasks that can take some time to complete and therefore are tracked as they are processed and displayed as separate line items or OCI CLI output. For example, the act of creating an LB or cipher suite is a work request that records and displays start and finish times, state (succeeded, failed, and so on), and other relevant details. Work requests are part of the Console LB resource list. 
The status of a work request, such as "Succeeded," isn't the same as completion of the provisioning of the resource. In other words, load balancer creation can "succeed" while provisioning is still in progress.
Was this article helpful?
YesNo

