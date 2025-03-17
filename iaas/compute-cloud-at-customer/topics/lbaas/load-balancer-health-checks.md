Updated 2024-08-06
# Load Balancer Health Checks
Load balancer health checks are tests to confirm the availability of backend servers.
These tests occur in the form of a request or a connection attempt depending on the protocol. The health check policy includes a time interval you specify, to ensure that the backend servers are continuously monitored. If a server fails a health check, the load balancer takes the server temporarily out of rotation. If the server later passes the health check, the load balancer returns it to the rotation.
The health check policy is configured when you create a backend set. You can configure TCP-level or HTTP-level health checks for your backend servers. For backend sets configured with SSL the health checks also use SSL encryption.
  * TCP-level health checks attempt to make a TCP connection with the backend servers and validate the response based on the connection status.
  * HTTP-level health checks send requests to the backend servers at a specific URI and validate the response based on the status code or entity data (body) returned.


Configure your health check protocol to match your application or service. If you run an HTTP service, then configure an HTTP-level health check. If you run a TCP-level health check against an HTTP service, then you might not get an accurate response. The TCP handshake can succeed and indicate that the service is up even when the HTTP service is incorrectly configured or having other issues. Although the health check returns no errors, you might experience transaction failures. 
For example:
  * The backend HTTP service has issues when communicating with the health check URL and the health check URL returns 5` _nn_`messages. An HTTP health check catches the message from the health check URL and marks the service as down. In this case, a TCP health check handshake succeeds and marks the service as healthy, even though the HTTP service might not be usable.
  * The backend HTTP service responds with 4 _nn_ messages because of authorization issues or no configured content. A TCP health check does not catch these errors.


The service provides application-specific health check capabilities to help you increase availability and reduce your application maintenance window.
Health status indicators are used to report the general health of a load balancer and its backend servers/sets. The possible statuses are: `ok`, `warning`, `critical`, `unknown`. Health status is updated every three minutes. No finer granularity is available. Historical health data is not provided.
## Interpreting Load Balancer Health Issues 🔗 
At the highest level, load balancer health reflects the status of its components. The health status indicators provide information you might need to drill down into and investigate further. Below are several common issues that the health status indicators can help you detect and correct. 

Health check misconfigured
    
All the backend servers for one or more of the affected listeners report as unhealthy. If your investigation finds that the backend servers do not have problems, then a backend set probably includes a misconfigured health check. 

Listener misconfigured
    
All the backend server health status indicators report OK, but the load balancer does not pass traffic on a listener. The listener might be configured to listen on the wrong port, use the wrong protocol, or use the wrong policy. If your investigation shows that the listener is not at fault, check the security rule configuration. 

Security rule misconfigured
    
Health status indicators help you diagnose these cases of misconfigured security rules:
  * All health status indicators report OK, but traffic does not flow (as with misconfigured listeners). If the listener is not at fault, check the security rule configuration.
  * All health status indicators report as unhealthy. You have checked your health check configuration and your services run properly on your backend servers. In this case, your security rules might not include the IP range for the source of the health check requests. The source IP for health check requests belongs to a compute instance managed by the Load Balancing service.


**Note**
Traffic may also be blocked because of misconfigured route tables in the compute instances. 

Backend server unhealthy
    
A backend server might be unhealthy or the health check might be misconfigured. To see the corresponding error code, check the status field in the backend server's details through the Console or CLI.
## Common Side Effects of Load Balancer Health Check Misconfiguration 🔗 
Misconfiguration scenarios are known to occur regularly. This page helps with troubleshooting. 

Wrong Port
    In this scenario, all backend servers are reported as unhealthy. If you confirmed that there are no issues with the backend servers, you might have made a mistake setting the port. Traffic must be allowed, and the backend must be listening on that port. 

Wrong Path
    
In this scenario, all backend servers are reported as unhealthy. If you confirmed that there are no issues with the backend servers, you might have made a mistake setting the path for the HTTP health check. It needs to match an actual application on the backend.
You can use the curl utility to run a test from a system within the same network. For example: `curl -i http://_backend_ip_address_/health.`
You receive the configured status code in the response: ```
"msg":"invalid statusCode","statusCode":404,"expected":"200"
```


Wrong Protocol
    
In this scenario, all backend servers are reported as unhealthy. If you confirmed that there are no issues with the backend servers, for an HTTP health check you might have made a mistake setting the status code. It must match the actual status code being returned from the backend. A typical mismatch is when a backend returns a 302 status code while a 200 status code is expected. This is often caused by the backend directing you to a login page or another location on the server. You can either make the backend return the expected code or use 302 in your health check configuration.
Error message: `msg:invalid statusCode, statusCode:nnn,expected:200` (where `nnn` represents the actual status code returned). 

Wrong Regex Pattern
    
In this scenario, all backend servers are reported as unhealthy. If you confirmed that there are no issues with the backend servers, you might have made a mistake setting a regex pattern that's not consistent with the body, or the backend isn't returning the expected body. In this scenario, you can either change the backend to match the pattern or correct the pattern to match the backend.
Error message: `response match resulte: failed`. 

Misconfigured Security Rules
    
In this scenario, all or some backend servers report as unhealthy. If you confirmed that there are no issues with the backend servers, then you might have improperly configured either the network security groups, security lists, or local firewalls (such as firewalld, iptables, or SELinux).
In this scenario, you can use either the curl or netcat utilities to run a test from a system within the same subnet and network security group (NSG) as your load balancer instance HTTP. For example: `curl -i http://_backend_ip_address_/health TCP        or nc -zvw3 _backend_ip_address_ 443`.
Local firewalls can be verified by using the command: firewall-cmd --list-all --zone=public. If the expected rules are missing from the firewall configuration, then add the required service. For example, to add HTTP port 80:
```
firewall-cmd --zone=public --add-service=http
firewall-cmd --zone=public --permanent --add-service=http
```

Was this article helpful?
YesNo

