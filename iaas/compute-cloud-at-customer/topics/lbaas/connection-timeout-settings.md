Updated 2024-08-06
# Connection Timeout Settings
On Compute Cloud@Customer, you can configure load balancer listeners to control the maximum idle time allowed during each TCP connection or HTTP request and response pair.
Load balancers support connection multiplexing. The load balancer can route many incoming requests from multiple clients to the destination backend server through a small number (one or multiple) of backend connections.
After your load balancer connects a client to a backend server, the connection can be closed because of inactivity. You can configure load balancer listeners to control the maximum idle time allowed during each TCP connection or HTTP request and response pair.
The following timeout settings affect the load balancer behavior:
  * Keep-alive setting between load balancer and client
  * Keep-alive setting between load balancer and backend server
  * Idle timeout in seconds


## Keep-Alive Settings
The Load Balancing service does not honor keep-alive settings from backend servers. The load balancer closes backend server connections that are idle for more than 300 seconds. We recommend that you do not allow your backend servers to close connections to the load balancer. To prevent possible 502 errors, ensure that your backend servers do not close idle connections in less than 310 seconds.
The Load Balancing service sets the keep-alive value to maintain the connection until it has been idle for 65 seconds. The value for this setting cannot be changed.
## Idle Timeout Settings
When you create or edit a TCP or HTTP listener, you can specify the maximum idle time in seconds. This setting applies to the time allowed between two successive receive or two successive send network input/output operations during the HTTP request-response phase. If the configured timeout has elapsed with no packets sent or received, the client's connection is closed. For HTTP and WebSocket connections, a send operation does not reset the timer for receive operations and a receive operation does not reset the timer for send operations.
**Note**
This timeout setting does not apply to idle time between a completed response and a subsequent HTTP request.
The default timeout values are: 300 seconds for TCP listeners and 60 seconds for HTTP listeners. The maximum timeout value is 7200 seconds.
Modify the timeout parameter if either the client or the backend server requires more time to transmit data; for example:
  * The client sends a database query to the backend server and the database takes over 300 seconds to run. Therefore, the backend server does not transmit any data within 300 seconds.
  * The client uploads data using the HTTP protocol. During the upload, the backend does not transmit any data to the client for more than 60 seconds.
  * The client downloads data using the HTTP protocol. After the initial request, it stops transmitting data to the backend server for more than 60 seconds.
  * The client starts transmitting data after establishing a WebSocket connection, but the backend server does not transmit data for more than 60 seconds.
  * The backend server starts transmitting data after establishing a WebSocket connection, but the client does not transmit data for more than 60 seconds.


Was this article helpful?
YesNo

