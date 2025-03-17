Updated 2023-08-16
# Viewing and Editing Health Checks and Policies
On Compute Cloud@Customer, load balancer health checks are tests to confirm the availability of backend servers. 
A health check can be a request or a connection attempt. The LB applies the health check policy, based on a configured time interval, to monitor the backend server set. If a server fails the health check, then the LB takes the server temporarily out of the balancing rotation. If the server later passes a subsequent health check, then the LB returns the backend server to the balancing rotation.
The health status of the specified backend set server is reported by the primary and standby load balancers. 
For general information about LBaaS, see [Load Balancer Health Checks](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/lbaas/load-balancer-health-checks.htm#load-balancer-health-checks "Load balancer health checks are tests to confirm the availability of backend servers.").
Was this article helpful?
YesNo

