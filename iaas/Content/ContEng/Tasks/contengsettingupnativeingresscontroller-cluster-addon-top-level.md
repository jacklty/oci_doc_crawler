Updated 2024-06-05
# Working with the OCI Native Ingress Controller as a Cluster Add-on
_Find out how to set up the OCI native ingress controller as a cluster add-on, to implement the rules and configuration options defined in a Kubernetes ingress resource to load balance and route incoming traffic to service pods running on worker nodes in a cluster._
Using the OCI native ingress controller as a cluster add-on rather than as a standalone program gives simplifies configuration and ongoing maintenance. You can more simply:
  * Enable or disable the OCI native ingress controller.
  * Opt into, and out of, automatic updates by Oracle.
  * Select OCI native ingress controller add-on versions.
  * Manage add-on specific customizations using approved key/value pair configuration arguments.


Note that if the OCI native ingress controller has already been deployed on the cluster as a standalone program, do not deploy the OCI native ingress controller cluster add-on on the cluster .
The sections below describe how to set up the OCI native ingress controller as a cluster add-on to load balance and route incoming traffic to service pods running on worker nodes in a cluster:
  * [High Level Steps to Set Up the OCI Native Ingress Controller as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-highlevelsteps.htm#contengsettingupnativeingresscontroller-addon-highlevelsteps "Find out the high level steps to set up the OCI native ingress controller as a cluster add-on to load balance and route incoming traffic to service pods running on worker nodes in a cluster.")
  * [Prerequisites for deploying the OCI Native Ingress Controller as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-prereqs.htm#contengsettingupnativeingresscontroller-addon-prereqs "Find out what you have to do before you can deploy the OCI native ingress controller as a cluster add-on to load balance and route incoming traffic to service pods running on worker nodes in a Kubernetes cluster.")
  * [Installing the OCI Native Ingress Controller as a Cluster Add-on](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-addon-installing-creating-resources.htm#contengsettingupnativeingresscontroller-addon-installing-creating-resources "Find out how to install the OCI native ingress controller as a cluster add-on.")
  * [Creating IngressClassParameters, IngressClass, and Ingress Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm#contengsettingupnativeingresscontroller-createresources "Find out how to create the Kubernetes ingress-related resources that are required to use the OCI native ingress controller.")
  * [Configuring the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-configuring "Find out how to configure and customize the OCI native ingress controller to load balance and route incoming traffic to service pods running on worker nodes in a Kubernetes cluster.")
  * [Troubleshooting the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-troubleshooting.htm#contengsettingupnativeingresscontroller-troubleshooting "Find out how to fix common problems with the OCI native ingress controller.")


Was this article helpful?
YesNo

