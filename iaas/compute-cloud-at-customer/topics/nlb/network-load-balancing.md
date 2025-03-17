Updated 2024-04-19
# Network Load Balancing
On Compute Cloud@Customer, you can configure the Network Load Balancing (NLB) feature to automatically distribute network traffic. 
Network Load Balancer (NLB) provides automated traffic distribution from one entry point to multiple servers in a backend set. NLBs ensure that your services remain available by directing traffic only to healthy servers based on Layer 3/Layer 4 (IP protocol) data.
## NLB Essentials 🔗 
When working with network load balancers (NLBs), understanding the building blocks and related key terminology is important. 

Backend Server
    
An NLB has a set of backend servers to route incoming traffic to destinations while balancing the load placed on each individual server in the set. 
A backend server is an application server responsible for generating content in reply to the incoming client traffic. You typically identify application servers with a unique combination of overlay (private) IPv4 address and port number. For example, `10.10.10.1:8080` and `10.10.10.2:8080`.
**Note** The backend server can't function as both a client and a backend simultaneously as is unable to be a traffic source to the NLB virtual IP (VIP).  

Backend Set
    
The backend set is a logical entity that includes:
  * A list of backend servers (compute instances) that accept traffic from the NLB.
  * A network-level load balancing policy to distribute traffic to the backend servers in a consistent manner.
  * A health check policy to decide if the backend servers are functioning and can accept traffic from the NLBs.



Network Load Balancing Policy
    
A network load balancing policy tells the NLB how to distribute incoming traffic to backend servers in the backend set.
A NLB uses an IP hash mapped from an _n-tuple_ , which is an ordered and finite list of elements. These elements are typically drawn from the fields in a packet header or from items from the grid of a relational database. The _n_ indicates how many fields the tuple contains.
Allowed NLB policies for the IP hash include:
  * A hash on 5 fields in the TCP/IP header (called "5-Tuple Hash")
  * A hash on 3 fields in the TCP/IP header (called "3-Tuple Hash")
  * A hash on 2 fields in the TCP/IP header (called "2-Tuple Hash"


**Note** NLB policies are different than LBaaS policies. NLB policies don't handle IP addresses and port numbers directly. Hashing is a way to manipulate these and other packet header fields to provide a number that the NLB can use without processing the entire packet header. The more tuples that are used for the load balancing policy, the more processing required for each load balanced packet, but the wider the range of values that can be used by the NLB to distribute traffic. 

Health Check
    
A health check is a test to confirm the availability of backend servers. A health check can be a request or a connection try. Based on a time interval you specify, the NLB applies the health check policy to continuously monitor backend servers. If a server fails the health check, the NLB takes the server temporarily out of rotation. If the server later passes the health check, the NLB returns it to the rotation.
You configure a health check policy when you create a backend set. TCP-level health checks try to make a TCP connection with the backend servers and validate the response based on the connection status
The health check results update the health status of the NLB. The health status is an indicator that reports the general health of NLBs and their components.  

Listener
    
A logical entity that checks for incoming traffic on the NLB IP address. You configure a listener's port number and various optional settings. When creating a listener, the VCN security rules must let the listener accept traffic.  

Work Request
    
An object that reports on the current state of an NLB request. Some NLB configuration tasks can take much longer to complete than others. Work requests let NLBs handle configuration steps asynchronously and form a queue. This lets the user issue more configuration commands without waiting for the completion of a previous configuration directive. 
Was this article helpful?
YesNo

