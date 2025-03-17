Updated 2024-08-14
# Adding OCI Service Operator for Kubernetes to Clusters
_Find out how to add OCI Service Operator for Kubernetes to clusters you've created with Kubernetes Engine (OKE)._
The OCI Service Operator for Kubernetes is an open source Kubernetes add-on that enables you to create, manage, and connect to Oracle Cloud Infrastructure resources (such as the [Autonomous Database service](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html) and the [HeatWave](https://docs.oracle.com/iaas/mysql-database/home.htm) service) using the Kubernetes API and Kubernetes tooling. Having installed the OCI Service Operator for Kubernetes, you can perform actions on Oracle Cloud Infrastructure resources using the Kubernetes API, without having to use the Oracle Cloud Infrastructure Console, CLI, or other developer tools. As a result, you can manage Oracle Cloud Infrastructure resources the same way you manage Kubernetes applications, reducing complexity and management overhead.
OCI Service Operator for Kubernetes is built using the open source [Operator Framework](https://operatorframework.io/) toolkit. The Operator Framework manages 'Kubernetes native applications' called Operators, in an effective, automated, and scalable way. An Operator implements and automates common activities in a piece of software running inside a Kubernetes cluster, by integrating natively with Kubernetes concepts and APIs. Operator Framework components include:
  * The [Operator SDK](https://sdk.operatorframework.io/), which uses the [Kubernetes controller-runtime library](https://github.com/kubernetes-sigs/controller-runtime) to provide high-level APIs and abstractions to write operational logic, and tools for scaffolding and code generation.
  * The [Operator Lifecycle Manager (OLM)](https://olm.operatorframework.io/), which extends Kubernetes to provide a declarative way to install, manage, and upgrade Operators on a cluster.


OCI Service Operator for Kubernetes enables you to provision and integrate with the following Oracle Cloud Infrastructure services:
  * [Autonomous Database](https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html) (specifically [Transaction Processing and Mixed Workloads](https://docs.oracle.com/en/cloud/paas/atp-cloud/index.html), [Analytics and Data Warehousing ](https://docs.oracle.com/en/cloud/paas/autonomous-data-warehouse-cloud/index.html)), which provides automated patching, upgrades, and tuning. Autonomous Database can perform all routine database maintenance tasks while the system is running, without human intervention.
  * [HeatWave](https://docs.oracle.com/iaas/mysql-database/home.htm), which provides a fully managed database service for developing and deploying secure cloud native applications using the popular MySQL open source database.
  * [Streaming](https://docs.oracle.com/iaas/Content/Streaming/Concepts/streamingoverview.htm), which provides a fully managed, scalable, and durable solution for ingesting and consuming high-volume data streams in real-time.
  * [Service Mesh](https://docs.oracle.com/iaas/Content/service-mesh/home.htm), which provides a set of capabilities to enable microservices within a cloud native application to communicate with each other in a centrally managed and secure manner.


You can add OCI Service Operator for Kubernetes to clusters you've created with Oracle Cloud Infrastructure Kubernetes Engine to interact with the Oracle Cloud Infrastructure services listed above. Having added OCI Service Operator for Kubernetes to a cluster, you don't have to manually provision and de-provision the services each time you deploy or un-deploy an application on the cluster. Instead, you interact with the services by using kubectl to call the Operator Framework APIs implemented by OCI Service Operator for Kubernetes. 
OCI Service Operator for Kubernetes is packaged as an Operator Lifecycle Manager (OLM) bundle to make it easy to install on Kubernetes clusters. The bundle contains all the required objects and definitions to install OCI Service Operator for Kubernetes on a cluster (such as CRDs, RBACs, configmaps, and deployments).
For more information about OCI Service Operator for Kubernetes, see the [OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator). 
## Adding OCI Service Operator for Kubernetes to a Cluster 🔗 
To add OCI Service Operator for Kubernetes to a cluster, follow the detailed instructions in the [OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator). 
For convenience, here's a high-level summary of the steps involved:
  1. Install OCI Service Operator for Kubernetes. During this step, you will typically:
     * Install the [Operator SDK](https://sdk.operatorframework.io/).
     * Install the [Operator Lifecycle Manager (OLM)](https://olm.operatorframework.io/)
     * Deploy OCI Service Operator for Kubernetes.
For more information, see the [OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator). 
  2. Secure OCI Service Operator for Kubernetes. During this step, you will typically:
     * Set up an Oracle Cloud Infrastructure user for use by OCI Service Operator for Kubernetes.
     * Set up appropriate policies to control access to resources (according to the Oracle Cloud Infrastructure services to be used).
     * Protect sensitive values by creating secrets.
The security configuration to choose will depend on your particular requirements. For more information, see the [OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator). 
  3. Provision and bind to the required Oracle Cloud Infrastructure services. During this step, you will typically:
     * Provide service provision request parameters.
     * Provide service binding request parameters.
     * Provide service binding response credentials.
The security configuration to choose will depend on your particular requirements. For more information, see the [OCI Service Operator for Kubernetes documentation in the Github repository](https://github.com/oracle/oci-service-operator). 


Was this article helpful?
YesNo

