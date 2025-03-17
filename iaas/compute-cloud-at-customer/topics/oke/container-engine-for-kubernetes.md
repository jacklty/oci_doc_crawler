Updated 2025-02-05
# Kubernetes Engine (OKE) on Compute Cloud@Customer
The Kubernetes Engine (OKE) is a scalable, highly available service that can be used to deploy any containerized application to Compute Cloud@Customer.
The Compute Cloud@Customer OKE documentation doesn't cover OKE extensively. It covers OKE networking requirements and OKE administration that are specific to Compute Cloud@Customer.
For more information about Kubernetes in Oracle, see [What is Kubernetes?](https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/what-is-kubernetes/). For more general information about Kubernetes, see the [Kubernetes site](https://kubernetes.io/).
## OKE Overview 🔗 
The OKE service uses Kubernetes, the open source system for automating deployment, scaling, and management of containerized applications across clusters of hosts. Kubernetes groups the containers that make up an application into logical units called pods for easy management.
The OKE service uses _Cluster API Provider_ (CAPI) and _Cluster API Provider for Oracle Cloud Infrastructure_ (CAPIOCI) to orchestrate the cluster on the Compute Cloud@Customer.
You can access the OKE service to create OKE clusters by using the [Compute Cloud@Customer Console](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/compute-cloud-customer-console.htm#accessing-the-console "Use the Compute Cloud@Customer Console to create and manage compute, storage and other resources on a Compute Cloud@Customer infrastructure."), the CLI, and API. 
You can access OKE clusters by using the Kubernetes command line (`kubectl`), the Kubernetes Dashboard, and the Kubernetes API.
On Compute Cloud@Customer, OKE service manages all OKE cluster nodes, which are compute instances. An authorized user can perform tasks such as patch the instance.
For information about OKE service limits, see [Limits on Resources Provided by Compute Cloud@Customer](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/overview/resource-limits.htm#limits-on-resources "Review the limits on the resources provided to customers by a Compute Cloud@Customer infrastructure and request new limits.").
## Supported Versions of Kubernetes 🔗 
The OKE service uses versions of Kubernetes that are certified as conformant by the Cloud Native Computing Foundation (CNCF). The OKE service is itself ISO-Compliant (ISO-IEC 27001, 27017, 27018).
Supported versions of Kubernetes are 1.28.8, 1.27.12, and 1.26.15.
## Public IP Address Requirements 🔗 
At least three available public IP addresses are required to use OKE on Compute Cloud@Customer for the NAT gateway, the control plane load balancer, and the worker load balancer. For more information, see [Creating OKE Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/network-resources-for-oke.htm#network-resources-for-oke "Learn about the required network resources for Kubernetes Engine \(OKE\) on Compute Cloud@Customer.").
The public IP addresses are configured specifically for your environment by Oracle, when Oracle installs the Compute Cloud@Customer infrastructure in your data center. If you think you might not have three available IP addresses, submit a support request. See [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm). To access support, sign in to the Oracle Cloud Console as described in [Sign In to the OCI Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm#Signing_In_to_the_Console).
Was this article helpful?
YesNo

