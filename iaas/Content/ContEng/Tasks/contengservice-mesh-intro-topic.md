Updated 2024-08-23
# Using OCI Service Mesh on Clusters created with Kubernetes Engine (OKE)
_Find out how to use Oracle Cloud Infrastructure Service Mesh on Kubernetes Engine (OKE)._
Oracle Cloud Infrastructure Service Mesh is a free, Oracle-managed service that provides a set of capabilities to enable microservices within a cloud native application to communicate with each other in a centrally managed and secure manner. Adding a service mesh is done by deploying a proxy alongside each microservice, which receives configuration information from a managed control plane. Oracle Cloud Infrastructure Service Mesh includes standardized patterns around observability, security, and traffic management for communication between microservices.
Companies continue to build net-new applications in a cloud native architecture or modernize their applications using containerization techniques using microservice-based approaches. Oracle Cloud Infrastructure Service Mesh makes it easier for you to develop and operate their cloud native applications.
Note that service mesh products (such as Oracle Cloud Infrastructure Service Mesh, Istio, and Linkerd) are supported when using the OCI VCN-Native Pod Networking CNI plugin for pod networking. Note that, with the exception of the Istio add-on, support is currently limited to Oracle Linux 7 (Oracle Linux 8 support is planned). The Istio add-on is supported with both Oracle Linux 7 and Oracle Linux 8. Worker nodes must be running Kubernetes 1.26 (or later).
**Note**
You can use Oracle Cloud Infrastructure Service Mesh with managed node pools, but not with virtual node pools.
## Enabling OCI Service Mesh 🔗 
In the Service Mesh Overview tutorial, deploy the Bookinfo application in a Kubernetes cluster you've created with Kubernetes Engine. Then, add Service Mesh to your application deployment.
Key tasks include how to:
  * Install the required software to access your application from a local machine.
  * Set up OCI CLI to access your cluster.
  * Set up a Kubernetes cluster on OCI.
  * Set up Service Mesh required Services.
  * Deploy and Configure your Application for Service Mesh.
  * Test your application using Service Mesh features.
  * Configure your application for Logging and Metrics.


The following illustration shows the BookInfo Application on Service Mesh: ![A diagram of the components needed to run a Spring Boot app on Oracle Cloud Infrastructure Kubernetes Engine](https://docs.oracle.com/en-us/iaas/Content/ContEng/images/service-mesh-deployment.jpg)
**Note** The gray rectangular boxes in the picture represent virtual deployments in the application. The named virtual deployments include: Product Page, Details, Reviews v1 to v3, and Ratings.
**[Click here to start the Service Mesh Overview Tutorial](https://docs.oracle.com/iaas/Content/service-mesh-tutorials/service-mesh-overview/00-overview.htm)**
Was this article helpful?
YesNo

