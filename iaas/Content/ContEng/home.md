Updated 2025-03-06
#  Kubernetes Engine
Kubernetes Engine (OKE) helps you define and create Kubernetes clusters to enable the deployment, scaling, and management of containerized applications.
[What's new](https://docs.oracle.com/iaas/releasenotes/services/conteng/)
#### Get Started
[Learn about OKE](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengoverview.htm#Overview_of_Container_Engine_for_Kubernetes "Find out about Kubernetes Engine \(OKE\), a fully-managed, scalable, and highly available service that enables you to deploy your containerized applications to the cloud.")
[Review key concepts](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengclustersnodes.htm#Container_Engine_and_Kubernetes_Concepts "Find out about the key concepts you need to understand before using Kubernetes Engine \(OKE\).")
[Prepare for OKE](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengprerequisites.htm#Preparing_for_Container_Engine_for_Kubernetes "Find out about the prerequisites you have to meet before you can use Kubernetes Engine \(OKE\).")
[Product page](https://www.oracle.com/cloud/cloud-native/container-engine-kubernetes/)
#### Create Clusters
[Quick Create workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Quick_Cluster_with_Default_Settings.htm#create-quick-cluster "Find out how to use the 'Quick Create' workflow to create a Kubernetes cluster with default settings and new network resources using Kubernetes Engine \(OKE\).")
[Custom Create workflow](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingclusterusingoke_topic-Using_the_Console_to_create_a_Custom_Cluster_with_Explicitly_Defined_Settings.htm#create-custom-cluster "Find out how to use the 'Custom Create' workflow to create a Kubernetes cluster with explicitly defined settings and existing network resources using Kubernetes Engine \(OKE\).")
[Supported images and shapes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengimagesshapes.htm#Supported_Images_Including_Custom_Images_and_Shapes_for_Worker_Nodes "Find out about the images and shapes you can specify for worker nodes in clusters created by Kubernetes Engine \(OKE\).")
[Enhanced clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithenhancedclusters.htm#contengworkingwithenhancedclusters "Find out about enhanced clusters and basic clusters, the differences between them, and how to create them using Kubernetes Engine \(OKE\).")
[Virtual nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithvirtualnodes.htm#contengspecifyingvirtualnodes "Find out about virtual nodes, the differences between virtual nodes and managed nodes, and how to create virtual nodes using Kubernetes Engine \(OKE\).")
#### Access Clusters
[Set up access](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdownloadkubeconfigfile.htm#Setting_Up_Cluster_Access "Find out about the steps to set up access to the clusters you create using Kubernetes Engine \(OKE\). Having completed the steps, you can start using kubectl to manage the cluster.")
[Add auth token to kubeconfig](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengaddingserviceaccttoken.htm#Adding_a_Service_Account_Authentication_Token_to_a_Kubeconfig_File "Find out how to add a service account authentication token to the kubeconfig file of a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).")
[IAM and Kubernetes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutaccesscontrol.htm#About_Access_Control_and_Container_Engine_for_Kubernetes "Find out about the permissions required to access clusters you've created using Kubernetes Engine \(OKE\).")
[SSH to worker nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconnectingworkernodesusingssh.htm#Connecting_to_Worker_Nodes_Using_SSH "Find out how to use SSH to connect to worker nodes in node pools in clusters you've created using Kubernetes Engine \(OKE\).")
#### Support
[Support Requests](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport.htm)
[Create a service request](https://support.oracle.com)
#### Manage Clusters
[Edit clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingcluster.htm#top "Find out how to modify properties of existing Kubernetes clusters you've created using Kubernetes Engine \(OKE\).")
[Edit nodes and node pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmodifyingnodepool.htm#top "Find out how to modify properties of existing node pools and worker nodes you've created using Kubernetes Engine \(OKE\).")
[Encrypt Kubernetes secrets](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengencryptingdata.htm#Encrypting_Kubernetes_Secrets_at_Rest_in_Etcd "Find out how to encrypt configuration data stored as Kubernetes secrets in etcd when using Kubernetes Engine \(OKE\).")
[Configure DNS servers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringdnsserver.htm#Configuring_DNS_Servers_for_Kubernetes_Clusters "Find out how to configure DNS servers for Kubernetes clusters you've created using Kubernetes Engine \(OKE\).")
#### Manage Deployments
[Deploy sample Nginx app](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeployingsamplenginx.htm#Deploying_a_Sample_Nginx_App_on_a_Cluster_Using_Kubectl "Find out how to use kubectl to deploy an Nginx app on a cluster you've created using Kubernetes Engine \(OKE\).")
[Pull images from Registry](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengpullingimagesfromocir.htm#Pulling_Images_from_Registry_during_Deployment "Find out how to create a Docker registry secret, and how to specify the image to pull from Oracle Cloud Infrastructure Registry \(along with the Docker secret to use\) during deployment of an application to a cluster you've created using Kubernetes Engine \(OKE\).")
[Create load balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingloadbalancer.htm#Creating_Load_Balancers_to_Distribute_Traffic_Between_Cluster_Nodes "Find out how to create different types of load balancer to distribute traffic between the nodes of a cluster you've created using Kubernetes Engine \(OKE\).")
[Set up storage](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcreatingpersistentvolumeclaim.htm#Creating_a_Persistent_Volume_Claim "Find out how to define and apply persistent volume claims to clusters you've created using Kubernetes Engine \(OKE\). With Oracle Cloud Infrastructure as the underlying IaaS provider, you can provision persistent volume claims by attaching volumes from the Block Volume service or by mounting file systems from the File Storage service.")
[Set up disaster recovery](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengfullstackdisasterrecovery.htm#contengfullstackdisasterrecovery "Find out more about setting up Full Stack Disaster Recovery for clusters created with Kubernetes Engine \(OKE\).")
#### Observe Clusters
[Monitor clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringclusters.htm#Monitoring_Clusters "Find out how to monitor the clusters, node pools, and nodes you've created using Kubernetes Engine \(OKE\).")
[View work requests](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkrequests.htm#contengviewingworkrequests "Find out how to view the operations of Kubernetes Engine \(OKE\) as work requests.")
[View audit logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengmonitoringoke.htm#Monitoring_Container_Engine_for_Kubernetes_and_the_Kubernetes_API_Server "Find out how to view operations of both Kubernetes Engine \(OKE\) and the Kubernetes API server as log events in the Oracle Cloud Infrastructure Audit.")
[View application logs](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengviewingworkernodelogs.htm#Viewing_Worker_Node_Logs "Find out how to view the logs of applications running on managed nodes and self-managed nodes in a Kubernetes cluster you've created using Kubernetes Engine \(OKE\).")
[Metrics](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengmetrics.htm#Container_Engine_for_Kubernetes_Metrics "Find out about the metrics emitted by Kubernetes Engine \(OKE\).")
#### Developer Tools
[Kubernetes Engine API](https://docs.oracle.com/iaas/api/#/en/containerengine/)
[Kubernetes Engine CLI](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/ce.html)
[SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm)
[Cloud Shell](https://docs.oracle.com/iaas/Content/API/Concepts/devcloudshellintro.htm)
#### Scale Clusters
[Add and remove node pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingclusters.htm#contengscalingclusters "Find out how to add and remove node pools to scale up and scale down the Kubernetes clusters you've created using Kubernetes Engine \(OKE\).")
[Scale node pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengscalingnodepools.htm#contengscalingnodepools "Find out how to scale up and scale down the node pools you've created using Kubernetes Engine \(OKE\).")
[Autoscale node pools and pods](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengautoscalingclusters.htm#Autoscaling_Kubernetes_Node_Pools_and_Pods "Find out about autoscaling Kubernetes node pools and pods you've created using Kubernetes Engine \(OKE\).")
#### Admission Controllers
[Supported admission controllers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Reference/contengadmissioncontrollers.htm#Supported_Admission_Controllers "Find out about the admission controllers that are turned on in Kubernetes clusters you create using Kubernetes Engine \(OKE\).")
[Pod security policies](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengusingpspswithoke.htm#Using_Pod_Security_Polices_with_Container_Engine_for_Kubernetes "Find out how to use pod security policies with Kubernetes clusters you've created using Kubernetes Engine \(OKE\).")
#### Upgrade Clusters
[Upgrade to new Kubernetes versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutupgradingclusters.htm#Upgrading_Clusters_to_Newer_Kubernetes_Versions "Find out about the different ways to upgrade control plane nodes and worker nodes to newer Kubernetes versions using Kubernetes Engine \(OKE\).")
[Supported Kubernetes versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutk8sversions.htm#Supported_Versions_of_Kubernetes "Find out about the Kubernetes versions that Kubernetes Engine \(OKE\) currently supports, along with details of previously supported versions and planned support for future versions.")
[Kubernetes support policy](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengupgradeoverview.htm#Kubernetes_Versions_and_Container_Engine_for_Kubernetes "Find out about the Kubernetes versioning scheme and Kubernetes Engine \(OKE\) support for different Kubernetes versions.")
#### Troubleshooting and FAQs
[Troubleshooting](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtroubleshooting.htm#contengtroubleshooting "Find out about troubleshooting information for Kubernetes Engine \(OKE\).")
[Frequently Asked Questions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengfaqs.htm#Container_Engine_FAQs "Find out answers to frequently asked questions about Kubernetes Engine \(OKE\).")
#### Community
[Oracle Cloud Infrastructure Blog](https://blogs.oracle.com/cloud-infrastructure/)
[Cloud infrastructure community forum](https://community.oracle.com/tech/apps-infra/categories/18430-cloud-infrastructure)
[AI solutions hub](https://www.oracle.com/artificial-intelligence/solutions/)
Was this article helpful?
YesNo

