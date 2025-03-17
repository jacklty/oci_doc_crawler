Updated 2024-08-23
# Security Best Practices
_Find out about security best practices for clusters you've created with Kubernetes Engine (OKE)._
This section contains best practices for security and Kubernetes Engine.
Read this section in conjunction with the [Securing Kubernetes Engine](https://docs.oracle.com/iaas/Content/Security/Reference/oke_security.htm) section of the [Oracle Cloud Infrastructure Security Guide](https://docs.oracle.com/iaas/Content/Security/Concepts/security_guide.htm). The information here supplements the information in the [Oracle Cloud Infrastructure Security Guide](https://docs.oracle.com/iaas/Content/Security/Concepts/security_guide.htm).
## Best Practice: Plan exposure level 🔗 
We recommend that you answer the following questions before implementing a security plan for the clusters you create with Kubernetes Engine:
  * How much internet exposure do you want clusters to have?
  * How do you plan to expose workloads internally to your VCN, and/or externally to the internet?
  * How do you plan to scale workloads?
  * Which types of Oracle services will the cluster consume?


Having answered the preceding questions, we recommend that you consider the following best practices:
  * **Best Practice: Create private clusters**
We recommend that if you only want to expose workloads internally to your VCN and not to the internet, you create VCN-native clusters, with the Kubernetes API endpoint in a private subnet. Such clusters are sometimes referred to as private clusters.
When you configure private clusters, all the control plane components (including the cluster's Kubernetes API endpoint) are in a private [RFC 1918](https://en.wikipedia.org/wiki/Private_network) network space. As a result, access is limited and all traffic stays within Oracle's networks. You can lock down access to the Kubernetes API to a specific VCN. 
If you do not use private clusters, the cluster's Kubernetes API endpoint has a public IPv4 address and all traffic to the API (including traffic from the cluster's node pools) goes over the public network space.
See [Announcing private Kubernetes clusters](https://blogs.oracle.com/cloud-infrastructure/post/announcing-private-kubernetes-clusters). 
  * **Best Practice: Place all applications in private subnets**
We recommend that if you want to reduce the exposure of a service to the internet, you place worker node compute instances running application workloads in private subnets and set up load balancers to access them.
Isolating service instances from the internet reduces the attack surface of a service. Most service instances do not need direct exposure to the internet. 
See [Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#Network_Resource_Configuration_for_Cluster_Creation_and_Deployment "Find out how to configure network resources to use Kubernetes Engine \(OKE\).").
  * **Best Practice: Restrict cluster traffic using Network Security Groups**
We recommend that you define security rules in network security groups (rather than in security lists) for the VCN in which you want to create and deploy clusters.
Kubernetes Engine creates required security rules by default, but you can change these to meet your specific requirements.
See [Security Rule Configuration in Network Security Groups and/or Security Lists](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#securitylistconfig).


## Best Practice: Apply security patches regularly 🔗 
We recommend that you regularly update the operating system running on worker nodes to apply the latest security patches.
Worker nodes in clusters created by Kubernetes Engine run a hardened Linux image. 
It is important to keep the worker node operating system hardened and secure because services running on worker nodes include the container runtime, kubelet and kube-proxy.
Another good practice is to use the [Center for Internet Security (CIS) Kubernetes benchmark](https://www.cisecurity.org/benchmark/kubernetes/) for worker nodes.
See [Creating Worker Nodes with Updated Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode.htm#Upgrading_the_Image_Running_on_Worker_Nodes_by_Creating_a_New_Node_Pool "Find out about the different ways to update worker node properties using Kubernetes Engine \(OKE\).").
## Best Practice: Use a combination of Kubernetes network policies and network security groups (NSGs) 🔗 
We recommend that you consider implementing Kubernetes network policies in combination with OCI network security groups (recommended) and/or security lists.
A combination of Kubernetes network policies (to secure pod-level network communication) and NSGs and/or OCI security lists (to secure host-level network communication) can offer the best network security posture.
See [Network Security](https://docs.oracle.com/iaas/Content/Security/Reference/oke_security.htm#Network_Security).
## Best Practice: Use network security groups (NSGs) in conjunction with infrastructure-as-code tools (such as Terraform) 🔗 
We recommend using security rules in network security groups (NSGs) rather than in security lists, when implementing a load-balancing controller in conjunction with infrastructure-as-code tools such as Terraform, 
To operate Kubernetes at scale, you'll typically use infrastructure-as-code tools such as Terraform to track the state of infrastructure resources. For example, to maintain infrastructure in its original and intended state, you'll typically run and re-run a Terraform configuration. However, a potential conflict arises for Kubernetes services of type LoadBalancer if the cloud-controller-manager adds or updates security rules in the security list that a subnet uses. Changes to security rules in a security list are not reflected in the Terraform configuration. As a result, the next time you run Terraform, changes to the security rules in the security list are flagged as a 'drift' from the original state and are discarded when you apply the Terraform configuration. Without the security rules, applications deployed on a cluster might fail because the load balancer or network load balancer provisioning the service of type LoadBalancer cannot serve traffic or communicate with nodes hosting the application pods. 
You can configure the cloud-controller-manager to not manage the security rules in a subnet's security list, or to manage only egress security rules for the load balancer or network load balancer. However, in both cases, you have to either manually configure selected ports every time a new service is deployed on the cluster, or open up the node port range altogether. Neither solution is ideal, as one involves manual work at runtime and the other introduces a potential security vulnerability.
To avoid the possibility of the cloud-controller-manager mutating a security list resource by adding or updating security rules, and those changes being subsequently discarded when you apply a Terraform configuration, we therefore recommend the cloud-controller-manager uses NSGs. Security rules defined for an NSG are resources in their own right with their own OCIDs, and are independent of the NSG itself. Since changing NSG security rules does not mutate the NSG resource itself, no changes are discarded when you apply a Terraform configuration.
For more information, see [Using the oci.oraclecloud.com/security-rule-management-mode annotation to manage security rules in NSGs and security lists](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringloadbalancersnetworkloadbalancers-subtopic.htm#contengcreatingloadbalancer_topic-Specifying_Load_Balancer_Security_Rule_Management_Annotation).
## Best Practice: Rotate secrets and certificates regularly 🔗 
We recommend that you set short lifetimes for secrets, credentials, and certificates, and that you automate their rotation.
## Best Practice: Run all applications as a non-privileged user 🔗 
We recommend that you run all applications as a non-privileged user. This is also a requirement in a number of regulatory standards. 
Running applications as a non-privileged user ensures that if an attacker does exploit a vulnerability (such as a remote code execution vulnerability), they are restricted to the limited access given to the non-privileged user. The attacker will also find it more difficult to escalate an attack to gain additional privileges, to break out of a container, or to get root access through a kernel bug.
## Best Practice: Treat containers as immutable 🔗 
We recommend that you define container root filesystems as read-only. If you allow libraries and binaries in a container's root filesystem to be updated, you make the entire cluster vulnerable to attack.
The ephemeral nature of containers provides significant security benefits. As applications and their immediate environment are deployed and upgraded as a whole, persistent attacks on the overall system are harder. Preventing modification of the root filesystem strengthens security, both by reducing the likelihood of threats, and by reducing their potential impact.
## Best Practice: Consider offloading SSL processing to ingress controllers or load balancers (if allowed) 🔗 
We recommend that if your organization's network security policy gives you the flexibility to do so, you offload SSL processing to ingress controllers or load balancers.
Ingress controllers (for example, [Traefik](https://www.traefik.io/), NGINX Open Source) enable you to intelligently route HTTP/S traffic that emanates from outside the cluster to services running inside the cluster. The Oracle Cloud Infrastructure Load Balancer service has support for transport encryption protocols (SSL and TLS) to encrypt data in-transit.
Encrypted traffic can be terminated at different places within the network (for example, at the load balancer, at the ingress resource, at the pod). How and where you terminate SSL connections is ultimately dictated by your organization's network security policy. For instance, if your organization's network security policy requires end-to-end encryption, traffic has to be decrypted at the pod. Decrypting traffic will place an additional burden on the pod because the pod will have to spend cycles establishing the initial handshake, and SSL/TLS processing is very CPU intensive. Consequently, if your organization's network security policy gives you the flexibility to do so, offload SSL processing to the ingress controller or the load balancer.
## Best Practices for auditing, logging, and monitoring 🔗 
We recommend that you consider the following best practices when you enable auditing, logging, and monitoring:
  * **Best Practice: Check logs regularly**
We recommend that you regularly check both the Kubernetes API Server audit logs, and the application logs of applications running on worker nodes in the cluster. Checking the logs regularly enables you to identify threats or vulnerabilities in the cluster.
See [Observing Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengobservingclusters_topic.htm#contengobservingclusters_topic "Find out about monitoring, and viewing logs, work requests, and metrics for, clusters you've created using Kubernetes Engine \(OKE\).").
  * **Best Practice: Enable audit logging**
We recommend that you enable audit logging, and save the audit logs in a secure repository for future analysis in the event of a compromise.
See [Viewing Kubernetes API Server Audit Logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringoke.htm#Monitoring_Container_Engine_for_Kubernetes_and_the_Kubernetes_API_Server "Find out how to view operations of both Kubernetes Engine \(OKE\) and the Kubernetes API server as log events in the Oracle Cloud Infrastructure Audit.")
  * **Best Practice: Use Kubernetes cluster-based logging**
We recommend that you use Kubernetes cluster-based logging to record container activity in a central logging subsystem. The standard output and standard error output of each container in a Kubernetes cluster can be ingested (using an agent like [Fluentd](https://www.fluentd.org/) running on each node) into tools like [Elasticsearch](https://www.elastic.co/), and viewed with [Kibana](https://www.elastic.co/kibana). 
See [Logging Architecture](https://kubernetes.io/docs/concepts/cluster-administration/logging/) in the Kubernetes documentation.
  * **Best Practice: Monitor cluster components**
We recommend that you monitor containers, pods, applications, services, and other cluster components using tools such as [Prometheus](https://prometheus.io/), [Grafana](https://grafana.com/), and [Jaeger](https://www.jaegertracing.io/).
  * **Best Practice: Log network traffic metadata and analyze it regularly**
We recommend that you enable VCN flow logs in the Oracle Cloud Infrastructure Logging service to capture metadata about the traffic flowing through a VCN, such as source and destination IP address and port, along with accepted/dropped packets. Having captured it, analyze the metadata regularly to identify suspicious or unusual activity between resources within the VCN, including between pods. See [Network Traffic Monitoring using Oracle VCN Flow Logs](https://blogs.oracle.com/observability/post/network-traffic-monitoring-using-oracle-vcn-flow-logs).


See [Observing Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengobservingclusters_topic.htm#contengobservingclusters_topic "Find out about monitoring, and viewing logs, work requests, and metrics for, clusters you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Use small and secure container images 🔗 
We recommend that you build small and secure container images that only contain the packages, libraries and tools required by the container's application. 
A new developer often makes the mistake of using the base image, even though they don't need the majority of the packages and libraries in the base image. We recommend choosing smaller images that require less storage space. A smaller image helps you pull and build the image faster. And with a smaller image comes less likelihood of security issues. 
To further reduce container image size, we recommend that you only install those tools needed for the container's application. Do not include debugging tools in production containers. 
If applications only need network tools at pod start-time, instead of putting exploitable tools like curl in an image for long-running applications, we recommend that you consider using separate init containers or delivering the data using a more Kubernetes-native method (such as ConfigMaps). 
We also recommend that you keep container images up-to-date, and look out for new versions of both the base image and any third-party tools you install.
## Best Practice: Limit credential exposure 🔗 
We recommend that you do not define credentials within application code. Instead, use a digital vault (such as Oracle Cloud Infrastructure Vault) to store and retrieve digital keys and credentials.
## Best Practice: Use an appropriate authentication token to access the cluster 🔗 
We recommend that you only use the authentication token generated by the command in a cluster's kubeconfig file when you access the cluster with kubectl and the Kubernetes Dashboard. When other processes and tools access the cluster, use a non-user-specific authentication token for authentication.
When you set up the kubeconfig file for a cluster, by default the file contains an Oracle Cloud Infrastructure CLI command to generate a short-lived, cluster-scoped, user-specific authentication token. The authentication token generated by the CLI command is appropriate to authenticate individual users accessing the cluster using kubectl and the Kubernetes Dashboard.
However, the generated authentication token is not appropriate to authenticate processes and tools accessing the cluster, such as continuous integration and continuous delivery (CI/CD) tools. To ensure access to the cluster, such tools require long-lived, non-user-specific authentication tokens. One solution is to use a Kubernetes service account.
See [Adding a Service Account Authentication Token to a Kubeconfig File](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingserviceaccttoken.htm#Adding_a_Service_Account_Authentication_Token_to_a_Kubeconfig_File "Find out how to add a service account authentication token to the kubeconfig file of a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).").
## Best Practice: Configure least privileged access when creating RoleBindings and ClusterRoleBindings 🔗 
We recommend that you only define Kubernetes RoleBindings and ClusterRoleBindings that include the set of permissions necessary to perform a specific function. 
By default, users are not assigned any Kubernetes RBAC roles (or clusterroles). So before attempting to create a new role (or clusterrole), you must be assigned an appropriately privileged role (or clusterrole). A number of such roles and clusterroles are always created by default, including the cluster-admin clusterrole (for a full list, see [Default roles and role bindings](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#default-roles-and-role-bindings) in the Kubernetes documentation). The cluster-admin clusterrole essentially confers super-user privileges. A user granted the cluster-admin clusterrole can perform any operation across all namespaces in a given cluster. 
See [About Access Control and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\).").
Was this article helpful?
YesNo

