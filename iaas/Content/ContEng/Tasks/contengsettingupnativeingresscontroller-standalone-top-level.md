Updated 2024-06-05
# Working with the OCI Native Ingress Controller as a Standalone Program
_Find out how to set up the OCI native ingress controller as a standalone program, to implement the rules and configuration options defined in a Kubernetes ingress resource to load balance and route incoming traffic to service pods running on worker nodes in a cluster._
Using the OCI native ingress controller as a standalone program rather than as a cluster add-on gives you complete control and responsibility for configuration and ongoing maintenance, including:
  * Installing a version of the OCI native ingress controller that is compatible with the version of Kubernetes running on the cluster.
  * Specifying configuration arguments correctly.
  * Manually upgrading the OCI native ingress controller when you upgrade a cluster to a new version of Kubernetes, to ensure the OCI native ingress controller is compatible with the cluster's new Kubernetes version.


The sections below describe how to set up the OCI native ingress controller as a standalone program to load balance and route incoming traffic to service pods running on worker nodes in a cluster:
  * [High Level Steps to Set Up the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-highlevelsteps.htm#contengsettingupnativeingresscontroller-highlevelsteps "Find out the high level steps to set up the OCI native ingress controller as a standalone program to load balance and route incoming traffic to service pods running on worker nodes in a cluster.")
  * [Prerequisites for deploying the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-prereqs "Find out what you have to do before you can deploy the OCI native ingress controller as a standalone program to load balance and route incoming traffic to service pods running on worker nodes in a Kubernetes cluster.")
  * [Installing the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-installing-creating-resources.htm#contengsettingupnativeingresscontroller-installing-creating-resources "Find out how to install the OCI native ingress controller as a standalone program.")
  * [Creating IngressClassParameters, IngressClass, and Ingress Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm#contengsettingupnativeingresscontroller-createresources "Find out how to create the Kubernetes ingress-related resources that are required to use the OCI native ingress controller.")
  * [Configuring the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-configuring "Find out how to configure and customize the OCI native ingress controller to load balance and route incoming traffic to service pods running on worker nodes in a Kubernetes cluster.")
  * [Troubleshooting the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-troubleshooting.htm#contengsettingupnativeingresscontroller-troubleshooting "Find out how to fix common problems with the OCI native ingress controller.")


Was this article helpful?
YesNo

