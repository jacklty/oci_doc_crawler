Updated 2023-08-16
# Request Routing
On Compute Cloud@Customer, the Load Balancing service enables you to route incoming requests to different backend servers based on certain properties of the request. The goal is to optimize the usage of backend resources.
When multiple applications are hosted on the backend, several virtual host names can be associated with the load balancer listeners, so that incoming HTTP requests matching a particular host name are routed to the right backend servers.
When backend applications use multiple endpoints or content types, represented by a distinct URI or path, HTTP requests for each of those endpoints can be routed to different backend servers based on path route rules. These path route rules contain a string that's matched against the URI of an incoming request to determine the appropriate backend destination.
Virtual host names and path route rule sets are frequently combined in request routing. Note that virtual host names take precedence over URI matching.
Was this article helpful?
YesNo

