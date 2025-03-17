Updated 2024-10-07
# Load Balancer as a Service
On Compute Cloud@Customer, you can configure the Load Balancing service (LBaaS) to automatically distribute network traffic.
The Load Balancing service provides automated traffic distribution from one entry point to multiple servers reachable from your virtual cloud network (VCN). The service offers a load balancer with your choice of a public or private IP address; provisioned bandwidth isn't user-configurable.
A load balancer improves resource usage, facilitates scaling, and helps ensure high availability. You can configure multiple load balancing policies and application-specific health checks to ensure that the load balancer directs traffic only to healthy instances.
## Load Balancer Essentials 🔗 
When working with load balancers, it's critical that you understand its building blocks and related key terminology. 

Backend Server
    
An application server responsible for generating content in reply to the incoming TCP or HTTP traffic.
You typically identify application servers with a unique combination of private IPv4 address and port – for example: 10.25.4.101:8080, 10.25.4.102:8080, etc. 

Backend Set
    
A logical entity defined by a list of backend servers, a load balancing policy, and a health check policy.
The backend set determines how the load balancer directs traffic to the collection of backend servers. SSL configuration is optional. 

Load Balancing Policy
    
A load balancing policy tells the load balancer how to distribute incoming traffic to the backend servers.
Common load balancer policies include: round robin, least connections, IP hash. 

Health Check
    
A test to confirm the availability of backend servers.
You configure the health check policy when you create a backend set. You can configure TCP-level or HTTP-level health checks for backend servers. Test results are reported through health status indicators. 

Listener
    
A logical entity that checks for incoming traffic on the load balancer IP address.
You configure a listener's protocol and port number, and the optional SSL settings. To handle TCP and HTTP traffic, you must configure multiple listeners. Supported protocols include: TCP, HTTP/1.x, HTTP/2. 

Cipher Suite
    
A logical entity for a set of algorithms, or _ciphers_ , using Transport Layer Security (TLS) to determine the security, compatibility, and speed of HTTPS traffic. 

Path Route Set
    
A set of path route rules to route traffic to the correct backend set without using multiple listeners or load balancers. 

Session Persistence
    
A method to direct all requests originating from a single logical client to a single backend web server. 

Shape
    
A template that determines the load balancer total pre-provisioned maximum capacity (bandwidth) for ingress plus egress traffic. Compute Cloud@Customer only provides the 400 Mbps shape.
Pre-provisioned maximum capacity applies to aggregated connections, not to a single client attempting to use the full bandwidth. 

SSL Certificate
    
If you use HTTPS or SSL for the listener, you must associate an SSL server certificate (X.509) with the load balancer. A certificate enables the load balancer to terminate the connection and decrypt incoming requests before passing them to the backend servers. Traffic between the load balancer and the backend can also be SSL-encrypted. 

Work Request
    
An object that reports on the current state of a Load Balancing request.
The Load Balancing service handles requests asynchronously. Each request returns a work request ID (OCID) as the response. You can view the work request item to see the status of the request.
Was this article helpful?
YesNo

