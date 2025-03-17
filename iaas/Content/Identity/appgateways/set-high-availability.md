Updated 2023-05-25
# Set Up High Availability
Use a load balancer to achieve high availability for multiple instances of App Gateway.
If high-availability is a requirement to access your web application, you can have multiple App Gateways, configure each of them to integrate with IAM, and use a load balancer to balance the request among the App Gateway instances.
This architecture diagram shows the components required for high availability.
[![App Gateway Load Balancer Diagram](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-appgateway_load_balancer.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam-appgateway_load_balancer.png)
This architecture requires that you install and configure more than one instance of App Gateway. Each App Gateway instance is configured to link to the same IAM URL, and to use the same Client ID and client cecret from the App Gateway registration in IAM Console.
Use a load balancer to distribute request between the App Gateway instances.
Also, the load balancer must perform health checks by way of HTTP with `HTTP keepalives` enabled for a duration that exceeds the health check interval. This prevents the load balancer from redirecting browser requests to an offline App Gateway instance.
The health check endpoint of App Gateway is `/cloudgate/v1/about`.
Was this article helpful?
YesNo

