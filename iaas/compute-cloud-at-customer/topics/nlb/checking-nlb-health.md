Updated 2024-05-07
# Checking NLB Health
On Compute Cloud@Customer, use health status indicators to check the health of your network load balancers (NLBs) and their resources.
You can see health status indicators and summaries in the NLBs, backend sets, and backend servers. 
On Compute Cloud@Customer, Network Load Balancer (NLB) health checks are tests to confirm the availability of backend servers. These tests occur in the form of an attempt to make a TCP connection with the backend servers and validate the response based on the connection status. 
The health status of the specified backend set server is reported by the primary and standby NLB. 
The health check policy includes a time interval you specify, to ensure that the backend servers are continuously monitored. If a server fails a health check, the NLB takes the server temporarily out of rotation. If the server later passes the health check, the NLB returns it to the rotation.
The health check policy is configured when you create a backend set. 
The TCP handshake can succeed and indicate that the service is up even when the HTTP service is incorrectly configured or having other issues. Although the health check returns no errors, you might experience transaction failures. 
The service provides application-specific health check capabilities to help you increase availability and reduce your application maintenance window.
Health status indicators are used to report the general health of an NLB and its backend servers and sets. The possible statuses are: 
  * `ok` – No attention required. The resource is functioning as expected.
  * `warning` – Some reporting entities require attention. The resource is not functioning at peak efficiency or the resource is incomplete and requires further work.
  * `critical` – Some or all reporting entities require immediate attention. The resource isn't functioning or unexpected failure is imminent.
  * `unknown` – Health status cannot be determined. The resource isn't responding or is in transition and might resolve to another status over time.


Health status is updated every three minutes. No finer granularity is available. Historical health data isn't provided.
Was this article helpful?
YesNo

