Updated 2024-10-07
# NLB Backend Configuration
On Compute Cloud@Customer, in the context of network load balancers (NLBs), the term _backend_ refers to the components that receive, process, and respond to forwarded client requests. Backend servers are grouped into backend sets; they receive client requests based on the configured load balancing policy. Health checks ensure that traffic only goes to healthy backend servers.
## NLB Backend Sets 🔗 
On Compute Cloud@Customer, the backend set in a network load balancer (NLB) configuration consists of a list of backend servers, an NLB policy, and a health check script. Backend sets help to group backend servers together and make them easier to configure and manage form an NLB perspective.
A backend set must be associated with one or more listeners.
See [Managing NLB Backend Sets](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/managing-nlb-backend-sets.htm#managing-nlb-backend-sets "On Compute Cloud@Customer, you can use backend sets to create logical entities consisting of a network load balancing \(NLB\) policy, health check policy, and a list of backend servers for a Network Load Balancer resource.").
## NLB Backend Servers 🔗 
On Compute Cloud@Customer, when creating a network load balancer (NLB), you must specify the backend servers to include in each backend set.
Backend servers can be set up as individual compute instances or as instance pools. You can add and remove backend servers without disrupting traffic.
TCP is the transport protocol of a backend server and is configured as part of the backend set. 
When you add backend servers to a backend set, you specify either the instance OCID or an IP address for the server to add. An instance with multiple VNICs attached can have multiple IP addresses pointing to it. If you identify a backend server by OCID, the NLB uses the primary VNIC primary private IP address. If you identify the backend servers to add to a backend set by their IP addresses, it is possible to point to the same instance more than once.
The NLB routes incoming traffic to the backend servers based on the configured load balancing policy. To route traffic to a backend server, the NLB requires the IP address of the compute instance and the relevant application port. If the backend server resides within the same VCN as the NLB, we recommend that you specify the compute instance's private IP address. The private IP address also works if a local peering gateway enables traffic between the NLB VCN and the backend server VCN. If the backend server and NLB reside in different VCNs without a peering connection, you must specify the public IP address of the compute instance. You must also ensure that the VCN security rules allow external traffic.
To enable backend traffic, your backend server subnets must have appropriate ingress and egress security rules. When you add backend servers to a backend set, you can specify the applicable network security groups (NSGs). If you prefer to use security lists for your VCN, you can configure them through the Networking service.
See [Managing NLB Backend Servers](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/nlb/managing-nlb-backend-servers.htm#managing-nlb-backend-servers "On Compute Cloud@Customer, manage the backend servers that receive incoming traffic based on the policies you specified for the backend set that contains it for the network load balancer \(NLB\).").
Was this article helpful?
YesNo

