Updated 2024-08-14
# Support and Shared Responsibilities
_Find out about some of the key responsibilities for both Oracle and users, along with technical support policies and limitations for Kubernetes Engine (OKE). Also find out about responsibilities for node management, managed control plane components, third-party open-source components, and security and patch management._
Running a business-critical application on Kubernetes Engine requires both you and Oracle to assume different but equally essential responsibilities. This non-exhaustive topic:
  * Captures some of the key responsibilities for both you and Oracle.
  * Describes technical support policies for, and limitations of, Kubernetes Engine.
  * Details responsibilities for node management, managed control plane components, third-party open-source components, security, and patch management.


## Oracle's Responsibilities for the Control Plane 🔗 
Kubernetes Engine provides a fully-managed Kubernetes control plane, which consists of the necessary components for Kubernetes clusters. All components of the control plane are maintained and operated by Oracle. The service is 'managed' in the sense that Oracle deploys, operates, and is responsible for service availability and functionality. 
Kubernetes Engine is certified as Kubernetes software conformant by the CNCF through the [Certified Kubernetes Conformance Program](https://www.cncf.io/certification/software-conformance). The Certified Kubernetes Conformance Program ensures that every vendor's version of Kubernetes supports the required APIs. For organizations using Kubernetes, conformance enables interoperability between one Kubernetes installation and another. When compared with the upstream Kubernetes project, Oracle limits customization to ensure a stable and consistent user experience.
As part of a fully-managed Kubernetes control plane, Kubernetes Engine manages and monitors the following components:
  * [kube-apiserver](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-apiserver/)
  * [kube-controller-manager](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-controller-manager/)
  * [cloud-controller-manager](https://github.com/oracle/oci-cloud-controller-manager)
  * [kube-scheduler](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-scheduler/)
  * [Kubernetes etcd](https://kubernetes.io/docs/concepts/overview/components/#etcd)


These components are fully managed by Oracle and exist in the Kubernetes Engine service tenancy. You cannot access the fully-managed components directly, and you can only modify them in ways supported by Kubernetes Engine public APIs.
Since Kubernetes Engine provides a managed Kubernetes control plane, Oracle performs automated etcd backup every 15 minutes. You cannot access these backups. However, if an event requiring disaster recovery occurs, Oracle uses these backups to restore clusters created byKubernetes Engine.
If you want to configure or directly access the Kubernetes control plane, consider using the [Kubernetes Cluster API Provider for Oracle Cloud Infrastructure](https://github.com/oracle/cluster-api-provider-oci) to deploy self-managed Kubernetes clusters.
## Shared Responsibilities for the Control Plane 🔗 
Oracle has responsibility for managing the Kubernetes control plane (including both the Kubernetes control plane components themselves, and the compute instances hosting these components).
However, upgrading the Kubernetes control plane is a task for which you and Oracle share responsibility.
Kubernetes Engine regularly releases updates to support new Kubernetes minor and patch versions, containing security or functionality improvements for the Kubernetes control plane components. 
You are responsible for initiating the upgrade of the Kubernetes control plane components, using the provided user interfaces (such as the Console, API, and CLI). See [Upgrading the Kubernetes Version on Control Plane Nodes in a Cluster](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8smasternode.htm#top "Find out how to upgrade the version of Kubernetes running on the control plane nodes of clusters that you create using Kubernetes Engine \(OKE\).").
Once you have initiated the upgrade of the Kubernetes control plane, Oracle has responsibility for actually performing the control plane upgrade.
## Shared Responsibilities for the Data Plane 🔗 
You and Oracle share responsibilities for the data plane components. The data plane components fall into two categories:
  * [Kubernetes Components](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengsupportsharedresponsibilities.htm#contengsupportsharedresponsibilities_topic-Shared_responsibility__section_Kubernetes_Components) that must run within the data plane for a cluster to function correctly.
  * [Worker Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengsupportsharedresponsibilities.htm#contengsupportsharedresponsibilities_topic-Shared_responsibility__section_Worker_Nodes) that run the applications you deploy in a cluster.


### Kubernetes Components 🔗 
Kubernetes Engine manages the following Kubernetes components of the data plane:
  * [kubelet](https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/)
  * [kube-proxy](https://kubernetes.io/docs/reference/command-line-tools-reference/kube-proxy/)
  * CNI plugin ([kube-flannel](https://github.com/flannel-io/flannel) or [VCN Native pod networking](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengpodnetworking_topic-flannel_CNI_plugin.htm#flannel_CNI_plugin "Find out about using the flannel CNI plugin for pod communication on worker nodes in clusters created using Kubernetes Engine \(OKE\)."))
  * [CSI volume plugin](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim_topic-Provisioning_PVCs_on_BV.htm#Provisioning_Persistent_Volume_Claims_on_the_Block_Volume_Service "Find out how to provision persistent volume claims for clusters you've created using Kubernetes Engine \(OKE\) by attaching volumes from the Block Volume service.")
  * [CoreDNS](https://kubernetes.io/docs/tasks/administer-cluster/coredns/)
  * Additional add-ons running in the kube-system namespace (more specifically, just those add-ons installed by Kubernetes Engine, and those add-ons for which installation instructions have been included in the Kubernetes Engine documentation). 


These components run in the Kubernetes data plane, and you therefore have access to them. You and Oracle share responsibility for ensuring that the components are functioning properly. Oracle hardens the above components to comply with [Center for Internet Security (CIS)](https://www.cisecurity.org/) and [Security Technical Implementation Guide (STIG)](https://stigviewer.com/stig/kubernetes/2021-04-14/) benchmarks. However, if you modify or remove any of the components, Oracle will consider the cluster unsupported. 
### Worker Nodes 🔗 
Worker nodes in user tenancies (managed nodes and self-managed nodes) are part of the data plane, and you and Oracle share responsibility for them. Furthermore, worker nodes execute private code, and store sensitive data. As a result, Kubernetes Engine and Oracle Support do not have access to worker nodes. Therefore, you have a responsibility to assist in the maintenance of worker nodes. For example, without your assistance, Oracle Support cannot sign in to worker nodes, execute commands on worker nodes, or view logs for worker nodes.
It is Oracle's responsibility to:
  * Provide Oracle-supported OS images for worker nodes, and to promptly provide patches to those images as necessary. Note that Oracle does not does not automatically patch worker nodes, and does not provide patches for custom images. 
  * Enhance Kubernetes Engine to support new Kubernetes versions.
  * Enable you to upgrade existing worker nodes from older (but still supported) Kubernetes versions to more recent versions.
  * Support the upgrade of worker nodes from non-supported Kubernetes versions of Kubernetes to supported versions (even though Oracle does not provide support for clusters running non-supported versions).


It is your responsibility to:
  * Regularly update the OS image running on worker nodes by changing their node pool's **Image** property, and removing worker nodes running older images (see [Creating Worker Nodes with Updated Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode.htm#Upgrading_the_Image_Running_on_Worker_Nodes_by_Creating_a_New_Node_Pool "Find out about the different ways to update worker node properties using Kubernetes Engine \(OKE\).")). Note this applies to the host-level operating system running on the nodes beneath containers, rather than the operating system running in containers themselves.
  * Regularly upgrade worker nodes to Kubernetes versions supported by Kubernetes Engine (see [Upgrading Clusters to Newer Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutupgradingclusters.htm#Upgrading_Clusters_to_Newer_Kubernetes_Versions "Find out about the different ways to upgrade control plane nodes and worker nodes to newer Kubernetes versions using Kubernetes Engine \(OKE\).")). 
  * Harden the host operating system and any non-Kubernetes data plane software to meet compliance and security requirements (for example, CIS or STIG benchmarks). 
  * Maintain workloads, including application code, build files, container images, data, Role-based access control (RBAC)/IAM policies, and containers and pods.
  * Setup and maintain required cluster networking , including VCNs, subnets, gateways, and so on (see [Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#Network_Resource_Configuration_for_Cluster_Creation_and_Deployment "Find out how to configure network resources to use Kubernetes Engine \(OKE\).")).
  * Monitor the cluster and applications, and respond to any alerts and incidents.
  * Provide Oracle with environment details when requested for troubleshooting purposes.


## Shared Responsibilities for Patching Security Issues 🔗 
You and Oracle have a shared responsibility for patching security issues, as follows:
  * If a security vulnerability is detected in one or more of the Kubernetes control plane components managed by Kubernetes Engine, it is Oracle's responsibility to patch all affected clusters to mitigate the issue.
  * If a security vulnerability is detected in one or more of the Kubernetes data plane components, it is Oracle's responsibility to provide a patched image. It is your responsibility to update the Kubernetes data plane with this patched image.


## Support Coverage 🔗 
### Areas covered by Oracle Support
Oracle provides support via My Oracle Support (MOS) for the following areas:
  * Connectivity to the Kubernetes API server.
  * Management, uptime, quality of service, and operations of all Kubernetes components that Kubernetes Engine provides and supports.
  * Any integration points in the OCI cloud-controller-manager provider for Kubernetes. These integration points include integration with other OCI services (such as load balancers, persistent volumes, and networking).
  * Issues related to networking (such as kube-proxy, CoreDNS, or other network access and functionality issues). Note that changes to the Kubernetes data plane components are not supported.
  * Failures associated with other OCI services that are outside Kubernetes Engine (for these cases, raise a MOS support ticket for the service that is failing). Examples include, but are not limited to:
    * Block volumes failing to attach to a worker node.
    * Load balancers dropping network packets.
  * Configuration of OCI resources other than those used by Kubernetes Engine.
  * Limits and Quota for services beyond Kubernetes Engine, such as compute, load balancers, and block volumes.


### Areas not covered by Oracle Support
Oracle does not provide support for the following areas:
  * Questions about how to use Kubernetes. For example, advice on how to create manifest files, how to deploy images, how to structure applications for Kubernetes.
  * Third-party open-source projects that are not provided as part of the Kubernetes control plane, or not deployed with clusters created by Kubernetes Engine. These projects might include Istio, Helm, Envoy, and others. If Oracle provides documentation on how to install such a project, Oracle will provide best effort support.
  * Third-party closed-source software. This software can include security scanning tools and networking devices or software.
  * Versions of Kubernetes beyond those listed in [Supported Versions of Kubernetes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#Supported_Versions_of_Kubernetes "Find out about the Kubernetes versions that Kubernetes Engine \(OKE\) currently supports, along with details of previously supported versions and planned support for future versions."). If you request support for a cluster running an unsupported version of Kubernetes, you will be asked to upgrade the cluster to a supported version of Kubernetes. To learn more about which versions of Kubernetes are currently supported, refer to [Supported Versions of Kubernetes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#Supported_Versions_of_Kubernetes "Find out about the Kubernetes versions that Kubernetes Engine \(OKE\) currently supports, along with details of previously supported versions and planned support for future versions.").
  * Upstream Kubernetes bugs.
  * Kubernetes Alpha features.


## Responsibility Matrix 🔗 
The following matrix summarizes how responsibilities are shared between you and Oracle.
Area | Oracle's Responsibility | Your Responsibility  
---|---|---  
Kubernetes Engine Service (API) |  **Responsibility:** Total Oracle is solely responsible for the management of the Kubernetes Engine service. |  **Responsibility:** None  
Kubernetes Control Plane |  **Responsibility:** Total Oracle is solely responsible for the management of:
  * Kubernetes control plane nodes.
  * Kubernetes control plane processes (for example, kube-apiserver, kube-controller-manager, kube-scheduler, etcd, cloud-controller-manager).

|  **Responsibility:** None  
Kubernetes Data Plane |  **Responsibility:** Shared Oracle is responsible for deploying Kubernetes data plane components and add-on software (for example, kubelet, kube-proxy, flannel). |  **Responsibility:** Shared
  * If you deviate from configuration or software based on Oracle-provided documentation, Oracle will only provide 'best-effort' support.
  * If you deviate from configuration or software not based on Oracle-provided documentation, Oracle will not provide support.

  
Worker Nodes |  **Responsibility:** Shared Oracle is responsible for:
  * Provisioning worker nodes in your tenancy.
  * Providing tools (for example, the cluster autoscaler) to dynamically scale the number of worker nodes.
  * Providing OS images for provisioning worker nodes.
  * Providing updated OS images containing security and general updates.

|  **Responsibility:** Shared You are responsible for:
  * Using the provided user interfaces (API, CLI, Console) to adjust required compute and storage capacity to meet application workload requirements.
  * Monitoring worker node health, and troubleshooting issues associated with unhealthy worker nodes.
  * Replacing unhealthy worker nodes, using the provided user interfaces (API, CLI, Console).
  * Applying security and general software updates to worker nodes, using the provided user interfaces (API, CLI, Console).

  
Kubernetes Version |  **Responsibility:** Shared Oracle is responsible for:
  * Providing APIs to automate the upgrade of the Kubernetes control plane.
  * Providing APIs to upgrade the Kubernetes version of the Kubernetes Data Plane node pool.
  * Automatically applying Kubernetes patch versions and OS updates to control plane nodes.
  * Making available Kubernetes major and minor updates for you to apply to both the Kubernetes control plane and the Kubernetes data plane.

|  **Responsibility:** Shared You are responsible for:
  * Applying Kubernetes upgrades, using the provided user interfaces (API, CLI, Console).
  * Re-deploying worker nodes within a node pool, so the nodes are recreated with the same new Kubernetes version as the node pool.

  
Cluster Observability |  **Responsibility:** Shared Oracle is responsible for providing:
  * Kubernetes audit logs, integrated into OCI logging.
  * Metrics covering the health of both the Kubernetes control plane and of node pools.

|  **Responsibility:** Shared You are responsible for monitoring the health of worker nodes using the cluster observability features provided by Oracle.  
Backups |  **Responsibility:** Shared Oracle is responsible for performing an automated etcd backup every 15 minutes. |  **Responsibility:** Shared You are responsible for backups required by the application.  
Disaster Recovery |  **Responsibility:** Shared If an event requiring disaster recovery occurs, Oracle is responsible for restoring the cluster from the etcd backups. |  **Responsibility:** Shared You are responsible for restoring data from backups created by the application.  
Cluster Networking |  **Responsibility:** None |  **Responsibility:** Total You are solely responsible for:
  * Setting up the required cluster networking (see [Network Resource Configuration for Cluster Creation and Deployment](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm#Network_Resource_Configuration_for_Cluster_Creation_and_Deployment "Find out how to configure network resources to use Kubernetes Engine \(OKE\).")).
  * Configuring worker node connectivity (both SSH and console connectivity).

  
Application Networking |  **Responsibility:** None |  **Responsibility:** Total You are solely responsible for setting up application networking capabilities (for example, load balancers, ingress controllers, and network policies).  
Application Observability |  **Responsibility:** None |  **Responsibility:** Total You are solely responsible for setting up and managing container logs (see[Viewing Application Logs on Managed Nodes and Self-Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkernodelogs.htm#Viewing_Worker_Node_Logs "Find out how to view the logs of applications running on managed nodes and self-managed nodes in a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).")) and metrics.  
Application Health and Performance |  **Responsibility:** None |  **Responsibility:** Total You are solely responsible for monitoring the health and performance of applications running on clusters.  
Application Security |  **Responsibility:** None |  **Responsibility:** Total You are solely responsible for application security.  
Application |  **Responsibility:** None |  **Responsibility:** Total You are solely responsible for workloads running within a cluster. This responsibility covers both software you have written and software written by the open source community.  
Was this article helpful?
YesNo

