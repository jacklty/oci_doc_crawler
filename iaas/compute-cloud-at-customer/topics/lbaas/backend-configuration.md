Updated 2024-08-06
# Backend Configuration
On Compute Cloud@Customer, in the context of load balancers, the term backend refers to the components that receive, process, and respond to forwarded client requests.
Backend servers are grouped into backend sets; they receive client requests based on the configured load balancing policy. Health checks ensure that traffic only goes to healthy backend servers. 

Backend Sets
    
The backend set in a load balancer configuration consists of a list of backend servers, a load balancing policy, and a health check script.
A backend set must be associated with one or more listeners. Optionally, you can add session persistence settings and configure SSL for HTTPS requests.
**Caution**
Changing the backend set's load balancing policy interrupts traffic and may cause active connections to be dropped. 

Backend Servers
    
Backend servers can be set up as individual compute instances or as instance pools. The transport protocol of a backend server is configured as part of the backend set. You can add and remove backend servers without disrupting traffic. When creating a load balancer, you must specify the backend servers to include in each backend set.
When you add backend servers to a backend set, you specify either the instance OCID or an IP address for the server to add. An instance with multiple VNICs attached can have multiple IP addresses pointing to it. If you identify a backend server by OCID, the Load Balancing service uses the primary VNIC primary private IP address. If you identify the backend servers to add to a backend set by their IP addresses, it is possible to point to the same instance more than once.
The load balancer routes incoming traffic to the backend servers based on the selected load balancing policy. To route traffic to a backend server, the Load Balancing service requires the IP address of the compute instance and the relevant application port. If the backend server resides within the same VCN as the load balancer, we recommend that you specify the compute instance's private IP address. The private IP address will also work if a local peering gateway enables traffic between the load balancer VCN and the backend server's VCN. If the backend server and load balancer reside in different VCNs without peering connection, you must specify the public IP address of the compute instance. You must also ensure that the VCN security rules allow external traffic.
To enable backend traffic, your backend server subnets must have appropriate ingress and egress security rules. When you add backend servers to a backend set, you can specify the applicable network security groups (NSGs). If you prefer to use security lists for your VCN, you can configure them through the Networking service.
**Note**
To accommodate high-volume traffic, we recommend that you use stateless security rules for your load balancer subnets. See in the chapter Virtual Networking Overview.
Was this article helpful?
YesNo

