Updated 2024-08-14
# Adding OCI Service Broker for Kubernetes to Clusters
_Find out how to add OCI Service Broker for Kubernetes to clusters you've created with Kubernetes Engine (OKE)._
**Note** Instead of the OCI Service Broker for Kubernetes, Oracle now recommends you use the OCI Service Operator for Kubernetes to interact with Oracle Cloud Infrastructure services using the Kubernetes API and Kubernetes tooling. See [Adding OCI Service Operator for Kubernetes to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingosok.htm#contengaddingosok "Find out how to add OCI Service Operator for Kubernetes to clusters you've created with Kubernetes Engine \(OKE\).").
Service brokers offer a catalog of backing services to workloads running on cloud native platforms. The Open Service Broker API is a commonly-used standard for interactions between service brokers and platforms. The Open Service Broker API specification describes a simple set of API endpoints that platforms use to provision, gain access to, and manage service offerings. For more information about the Open Service Broker API, see resources available online including those at [openservicebrokerapi.org](https://www.openservicebrokerapi.org/).
OCI Service Broker for Kubernetes is an implementation of the Open Service Broker API. OCI Service Broker for Kubernetes is specifically for interacting with Oracle Cloud Infrastructure services from Kubernetes clusters. It includes service broker adapters to bind to the following Oracle Cloud Infrastructure services:
  * Object Storage 
  * Autonomous Database for Transaction Processing and Mixed Workloads 
  * Autonomous Database for Analytics and Data Warehousing
  * Streaming


You can add OCI Service Broker for Kubernetes to clusters you've created with Oracle Cloud Infrastructure Kubernetes Engine to interact with the Oracle Cloud Infrastructure services listed above. Having added OCI Service Broker for Kubernetes to a cluster, you don't have to manually provision and de-provision the Oracle Cloud Infrastructure services each time you deploy or un-deploy an application on the cluster. Instead, you interact with the Oracle Cloud Infrastructure services by using kubectl to call the Open Service Broker APIs implemented by OCI Service Broker for Kubernetes . 
OCI Service Broker for Kubernetes is available as a Helm chart, a Docker container, and as source code from [Github](https://github.com/oracle/oci-service-broker).
For more information about OCI Service Broker for Kubernetes, see the OCI Service Broker for Kubernetes documentation in the [Github repository](https://github.com/oracle/oci-service-broker). 
## Adding OCI Service Broker for Kubernetes to a Cluster 🔗 
To add OCI Service Broker for Kubernetes to a cluster, follow the detailed instructions in the [Github repository](https://github.com/oracle/oci-service-broker). 
For convenience, here's a high-level summary of the steps involved:
  1. Install OCI Service Broker for Kubernetes. During this step, you will typically:
     * Install the Service Catalog.
     * Install the svcat tool.
     * Deploy OCI Service Broker for Kubernetes.
     * Grant RBAC permissions and roles.
     * Register OCI Service Broker for Kubernetes.
For more information about installation, see the OCI Service Broker for Kubernetes documentation in the [Github repository](https://github.com/oracle/oci-service-broker).
  2. Secure OCI Service Broker for Kubernetes. During this step, you will typically:
     * Restrict access to Service Catalog resources using RBAC permissions and roles.
     * Configure TLS for OCI Service Broker for Kubernetes.
     * Set up an Oracle Cloud Infrastructure user for use by OCI Service Broker for Kubernetes.
     * Set up appropriate policies to control access to resources (according to the Oracle Cloud Infrastructure services to be used).
     * Limit access to the OCI Service Broker for Kubernetes endpoint using NetworkPolicy.
     * Stand up an etcd cluster for Service Catalog and OCI Service Broker for Kubernetes.
     * Protect sensitive values by creating secrets.
The security configuration to choose will depend on your particular requirements. For more information, see the OCI Service Broker for Kubernetes documentation in the [Github repository](https://github.com/oracle/oci-service-broker).
  3. Provision and bind to the required Oracle Cloud Infrastructure services. During this step, you will typically:
     * Provide service provision request parameters.
     * Provide service binding request parameters.
     * Provide service binding response credentials.
The details to provide will depend on the Oracle Cloud Infrastructure service to bind to. For more information, see the OCI Service Broker for Kubernetes documentation in the [Github repository](https://github.com/oracle/oci-service-broker). 


Was this article helpful?
YesNo

