Updated 2023-09-28
# Load Balancing Policies
On Compute Cloud@Customer, after you create a load balancer, you can apply policies to control traffic distribution to your backend servers. The primary policy types that the Load Balancing service supports, are: Round Robin, Least Connections, and IP Hash. 

Round Robin
    
The Round Robin policy is the default load balancer policy. This policy distributes incoming traffic sequentially to each server in a backend set list. After each server has received a connection, the load balancer repeats the list in the same order.
Round Robin is a simple load balancing algorithm. It works best when all the backend servers have similar capacity and the processing load required by each request doesn't vary significantly. 

Least Connections
    
The Least Connections policy routes incoming nonsticky request traffic to the backend server with the fewest active connections. This policy helps you maintain an equal distribution of active connections with backend servers. As with the round robin policy, you can assign a weight to each backend server and further control traffic distribution.
This policy works best with protocols using long sessions, such as LDAP and SQL. It's not recommended for short sessions as typically seen in HTTP use cases. If you select the Least Connections policy for HTTP connections, the load balancer might instead apply Round Robin internally, and even adjust server weighting dynamically.
**Note**
In TCP use cases, a connection can be active but have no current traffic. Such connections don't serve as a good load metric. 

IP Hash
    
The IP Hash policy uses an incoming request's source IP address as a hashing key to route nonsticky traffic to the same backend server. The load balancer routes requests from the same client to the same backend server as long as that server is available. This policy honors server weight settings when establishing the initial connection.
**Caution**
Multiple clients that connect to the load balancer through a proxy or NAT router appear to have the same IP address. If you apply the IP Hash policy to your backend set, the load balancer routes traffic based on the incoming IP address and sends these proxied client requests to the same backend server. If the proxied client pool is large, the requests could flood a backend server.
When processing load or capacity varies among backend servers, you can refine each of these policy types with backend server _weighting_. Weighting affects the proportion of requests directed to each server. For example, a server weighted '3' receives three times the number of connections as a server weighted '1.' You assign weights based on criteria of your choosing, such as each server's traffic-handling capacity. Weight values must be from 1 to 100.
Load balancer policy decisions apply differently to TCP load balancers, cookie-based session persistent HTTP requests – also known as sticky requests –, and nonsticky HTTP requests.
  * A TCP load balancer considers policy and weight criteria to direct an initial incoming request to a backend server. All subsequent packets on this connection go to the same endpoint.
  * An HTTP load balancer configured to handle cookie-based session persistence forwards requests to the backend server specified by the cookie's session information.
  * For nonsticky HTTP requests, the load balancer applies policy and weight criteria to every incoming request and determines an appropriate backend server. Multiple requests from the same client could be directed to different servers.


Was this article helpful?
YesNo

