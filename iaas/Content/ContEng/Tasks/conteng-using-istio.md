Updated 2024-08-23
# Using Istio on Clusters Created with Kubernetes Engine (OKE)
_Find out about using Istio on clusters you've created with Kubernetes Engine (OKE)._
Istio is an open-source, platform-independent service mesh that provides traffic management, policy enforcement, and telemetry collection. Istio is designed to manage communications between microservices and applications. Istio uses Envoy proxies, deployed as sidecars to the underlying services, to mediate all inbound and outbound traffic for all services in the service mesh. Without requiring changes to the underlying services, Istio provides automated baseline traffic resilience, service metrics collection, distributed tracing, traffic encryption, protocol upgrades, and advanced routing functionality for all service-to-service communication. 
Istio uses ingress and egress gateways to configure load balancers executing at the edge of a service mesh. Istio ingress gateways are implemented using Kubernetes Gateway and VirtualService resources, and provide a consistent, high-performance traffic management layer across all the services in the service mesh. An ingress gateway is a single entry point into the service mesh through which all incoming HTTP and HTTPS request traffic flows. The ingress gateway routes traffic to the appropriate service based on the request. Similarly, an egress gateway defines exit points from the service mesh.
For more information about Istio, see the [Istio documentation](https://istio.io/latest/docs/).
You can deploy Istio on a Kubernetes cluster in two ways:
  * as a standalone program (see [Working with Istio as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-intro-topic.htm#Example_Installing_Calico_and_Setting_Up_Network_Policies "Find out how to install Istio as a standalone program on clusters you've created with Kubernetes Engine \(OKE\)."))
  * as a cluster add-on (see [Working with Istio as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengistio-cluster-add-on.htm#contengistio-cluster-add-on "Find out how to install, configure, and use Istio as a cluster add-on to simplify traffic management, security, connections, and observability in clusters you've created with Kubernetes Engine \(OKE\)."))


Note that service mesh products (such as Oracle Cloud Infrastructure Service Mesh, Istio, and Linkerd) are supported when using the OCI VCN-Native Pod Networking CNI plugin for pod networking. Note that, with the exception of the Istio add-on, support is currently limited to Oracle Linux 7 (Oracle Linux 8 support is planned). The Istio add-on is supported with both Oracle Linux 7 and Oracle Linux 8. Worker nodes must be running Kubernetes 1.26 (or later).
**Note**
You can use Istio with managed node pools, but not with virtual node pools.
Was this article helpful?
YesNo

