Updated 2024-08-23
# Using Service Mesh Products on Clusters Created with Kubernetes Engine (OKE)
_Find out about using service mesh products on clusters you've created with Kubernetes Engine (OKE)._
You can use Kubernetes service mesh products (such as Oracle Cloud Infrastructure Service Mesh, Istio, and Linkerd) with clusters you have created with Kubernetes Engine. 
Service mesh products manage network communication between services in a Kubernetes cluster, by adding a dedicated infrastructure layer (a "service mesh") to applications running on the cluster. Service mesh products typically use sidecar proxies, a control plane, and a data plane to provide observability, security, and traffic management capabilities. These capabilities are provided transparently, without modifying the code of applications running on the cluster. 
Note that service mesh products (such as Oracle Cloud Infrastructure Service Mesh, Istio, and Linkerd) are supported when using the OCI VCN-Native Pod Networking CNI plugin for pod networking. Note that, with the exception of the Istio add-on, support is currently limited to Oracle Linux 7 (Oracle Linux 8 support is planned). The Istio add-on is supported with both Oracle Linux 7 and Oracle Linux 8. Worker nodes must be running Kubernetes 1.26 (or later).
For more information and examples, see:
  * [Using OCI Service Mesh on Clusters created with Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengservice-mesh-intro-topic.htm#Example_Enabling_Service_OKE "Find out how to use Oracle Cloud Infrastructure Service Mesh on Kubernetes Engine \(OKE\).")
  * [Using Istio on Clusters Created with Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/conteng-using-istio.htm#conteng-using-istio "Find out about using Istio on clusters you've created with Kubernetes Engine \(OKE\).")


Was this article helpful?
YesNo

