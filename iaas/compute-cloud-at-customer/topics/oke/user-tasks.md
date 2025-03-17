Updated 2024-12-16
# Cluster Administrator Tasks
Perform a set of tasks to create OKE clusters on Compute Cloud@Customer. 
## Prerequisites 🔗 
Perform the following tasks on your local system that you use to administer OKE:
  1. Configure the OCI CLI so you can run CLI commands. See [Command Line Interface (CLI)](https://docs.oracle.com/iaas/Content/API/Concepts/cliconcepts.htm#Command_Line_Interface_CLI). 
If you already have the OCI CLI installed, use `oci -v` to check the version. The minimum required version for using OKE is 3.15.1.
If you work in more than one tenancy, create a profile for each tenancy as described in [Creating a Profile in the Oracle Cloud Infrastructure CLI Configuration File](https://docs.oracle.com/iaas/Content/Functions/Tasks/functionsconfigureocicli.htm).
  2. Install the Kubernetes client command line tool, `kubectl`. See [Install kubectl](https://kubernetes.io/docs/tasks/tools/). 
If you already have `kubectl` installed, ensure the version is within one minor version of the Kubernetes version that you're using. See [Supported Versions of Kubernetes](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/container-engine-for-kubernetes.htm#container-engine-for-kubernetes__k8s-versions).


## Cluster Administrator Workflow 🔗 
Perform the tasks in the following table to configure OKE on Compute Cloud@Customer.
No. | Task | Links  
---|---|---  
1. |  **Create Network resources.** Create a VCN, subnets, internet gateway, NAT gateway, route tables, and security lists.  | [Creating OKE Network Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/network-resources-for-oke.htm#network-resources-for-oke "Learn about the required network resources for Kubernetes Engine \(OKE\) on Compute Cloud@Customer.")  
2. |  **Create an OKE cluster.** | [Creating an OKE Cluster](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-cluster.htm#creating-a-kubernetes-cluster "Learn how to create OKE Clusters on Compute Cloud@Customer.")  
3. |  **Create a Kubernetes configuration file for the cluster.** | [Creating a Kubernetes Configuration File](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-kubernetes-configuration-file.htm#creating-a-kubernetes-configuration-file "On Compute Cloud@Customer, you can set up a Kubernetes configuration file for each OKE cluster that you work with. Your Kubernetes configuration file enables you to access OKE clusters using the kubectl command and the Kubernetes Dashboard.")  
4. |  **Create a Kubernetes Dashboard.** The dashboard helps you manage the cluster and manage and troubleshoot applications running in the cluster. |  On the [Kubernetes site](https://kubernetes.io/), see [Deploy and Access the Kubernetes Dashboard](https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/)  
5. |  **Create a worker node pool.** | [Creating an OKE Worker Node Pool](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-a-worker-node-pools.htm#creating-a-worker-node-pools "Learn how to create OKE worker node pools on Compute Cloud@Customer for a workload cluster.")  
6. | **Configure any registries or repositories that the worker nodes need.**  
7. |  **Create a service to expose containerized applications outside the infrastructure.** | [Exposing Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/exposing-containerized-applications.htm#exposing-containerized-applications "To expose an application deployment so that worker node applications can be reached from outside the Compute Cloud@Customer infrastructure, create an external load balancer. An external load balancer is a Service of type LoadBalancer. The service provides load balancing for an application that has multiple running instances.")  
8. |  **Create persistent storage for applications to use.** | [Adding Storage for Containerized Applications](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/oke/adding-storage-for-containerized-applications.htm#adding-storage-for-containerized-applications "On Compute Cloud@Customer, you can add persistent storage for use by applications on an OKE cluster node. Storage created in a container's root file system is deleted when you delete the container. For more durable storage for containerized applications, configure persistent volumes to store data outside of containers.")  
Was this article helpful?
YesNo

