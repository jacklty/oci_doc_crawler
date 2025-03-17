Updated 2024-06-05
# High Level Steps to Set Up the OCI Native Ingress Controller as a Standalone Program
_Find out the high level steps to set up the OCI native ingress controller as a standalone program to load balance and route incoming traffic to service pods running on worker nodes in a cluster._
At a high-level, the steps to set up the OCI native ingress controller as a standalone program are as follows:
  * **Meet the prerequisites for the OCI native ingress controller as a standalone program**
Configure the cluster on which you want to deploy the OCI native ingress controller as a standalone program to meet the prerequisites, as follows:
    * Set up an instance principal, user principal, or workload identity principal to enable the OCI native ingress controller pod to access other Oracle Cloud Infrastructure services and resources.
    * Grant the instance principal, user principal, or workload identity principal the necessary permissions.
    * Install cert-manager on the cluster.
    * Install the Helm CLI.
    * Clone the OCI native ingress controller repository and set parameters in values.yaml.
For more information, see [Prerequisites for deploying the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-prereqs.htm#contengsettingupnativeingresscontroller-prereqs "Find out what you have to do before you can deploy the OCI native ingress controller as a standalone program to load balance and route incoming traffic to service pods running on worker nodes in a Kubernetes cluster.").
  * **Deploy the OCI native ingress controller as a standalone program**
When you have completed the prerequisites, you can deploy the OCI native ingress controller. For more information, see [Installing the OCI Native Ingress Controller as a Standalone Program](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-installing-creating-resources.htm#contengsettingupnativeingresscontroller-installing-creating-resources "Find out how to install the OCI native ingress controller as a standalone program.").
  * **Create Ingress-Related Resources**
Having installed the OCI native ingress controller (either as a standalone program or as a cluster add-on), you have to create the following Kubernetes resources before you can use it:
    * `IngressClassParameters`
    * `IngressClass`
    * `Ingress`
For more information, see [Creating IngressClassParameters, IngressClass, and Ingress Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-createresources.htm#contengsettingupnativeingresscontroller-createresources "Find out how to create the Kubernetes ingress-related resources that are required to use the OCI native ingress controller.").
  * **Configure the OCI native ingress controller**
You can configure the OCI native ingress controller (whether installed as a standalone program or as a cluster add-on) as follows:
    * Add route rules to the `Ingress` resource manifest to specify how the OCI load balancer created by the OCI native ingress controller routes incoming requests. The OCI native ingress controller supports:
      * Host-based routing: Requests are routed to different backend services using rules defined for the ingress resource, based on the domain name in the request's Host header (the host to which the request was originally sent).
      * Path-based routing: Requests are routed to different backend services using rules defined for the ingress resource, based on elements in the path to which the original request was sent.
      * Default backend routing: Requests are routed to a default backend if the request does not match any of the rules defined for the ingress resource.
See [Specifying Route Rules for the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-specifyingrouterules).
    * Use annotations to customize the behavior of the OCI native ingress controller and the OCI load balancer that the OCI native ingress controller creates. You can use annotations to specify:
      * the OCID of an existing OCI load balancer to use, rather than creating a new one
      * a custom load balancing policy
      * a custom listener protocol
      * attributes of the load balancer health check policy
See [Customizing OCI Native Ingress Controller Behavior Using Annotations](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-annotationcustomization).
    * Define pod readiness gates to indicate that a pod is ready to receive traffic (provided the cluster is using the OCI VCN-Native Pod Networking CNI plugin for pod networking). See [Setting Up a Pod Readiness Gate](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-podreadinessgate).
    * Provide support for HTTPS/TLS requests using certificates issued by the OCI Certificates service. See [Adding Support for HTTPS/TLS Requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-configuring.htm#contengsettingupnativeingresscontroller-https_tls).
  * **Troubleshoot the OCI native ingress controller**
Troubleshoot common problems with the OCI native ingress controller. The OCI native ingress controller identifies conflicting declarations in ingress resource manifests, and outputs validation errors in pod logs.
For more information, see [Troubleshooting the OCI Native Ingress Controller](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengsettingupnativeingresscontroller-troubleshooting.htm#contengsettingupnativeingresscontroller-troubleshooting "Find out how to fix common problems with the OCI native ingress controller.").


Was this article helpful?
YesNo

