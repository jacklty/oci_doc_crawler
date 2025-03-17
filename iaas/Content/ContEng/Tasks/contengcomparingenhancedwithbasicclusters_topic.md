Updated 2024-08-14
# Comparing Enhanced Clusters with Basic Clusters
_Find out about the differences between the enhanced clusters and basic clusters you can create using Kubernetes Engine (OKE)._
When creating a new cluster with Kubernetes Engine, you specify the type of cluster to create as one or other of the following:
  * **Enhanced cluster:** Enhanced clusters support all available features. See [Enhanced Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingenhancedwithbasicclusters_topic.htm#contengcomparingenhancedwithbasicclusters_topic-enhancedclusters).
  * **Basic cluster:** Basic clusters support all the core functionality provided by Kubernetes and Kubernetes Engine, but none of the enhanced features that Kubernetes Engine provides. See [Basic Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingenhancedwithbasicclusters_topic.htm#contengcomparingenhancedwithbasicclusters_topic-basicclusters).


Note the following when creating clusters:
  * When using the Console to create a cluster, if you don't select any enhanced features during cluster creation, you have the option to create the new cluster as a basic cluster. A new cluster is created as an enhanced cluster by default, unless you explicitly choose to create a basic cluster.
  * When using the CLI or the API to create a cluster, you can specify whether to create a basic cluster or an enhanced cluster. If you don't explicitly specify the type of cluster to create, a new cluster is created as a basic cluster by default.


Creating a new cluster as an enhanced cluster enables you to easily add enhanced features later, even if you didn't select any enhanced features initially. When you create an enhanced cluster, you must create it as [VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengfaqs.htm#VCN_Native_Clusters). If you do choose to create a new cluster as a basic cluster, you can still choose to upgrade it to an enhanced cluster later on, provided it is [VCN-native](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengfaqs.htm#VCN_Native_Clusters). However, you can't downgrade an enhanced cluster to a basic cluster.
All references to 'clusters' in the Kubernetes Engine documentation refer to both enhanced clusters and basic clusters, unless explicitly stated otherwise.
## Enhanced Clusters 🔗 
Enhanced clusters support all available features, including features not supported by basic clusters (such as virtual nodes, cluster add-on management, workload identity, additional worker nodes per cluster, self-managed nodes, and node cycling when updating or upgrading node pools). Enhanced clusters come with a financially-backed service level agreement (SLA).
### Notable features supported differently by enhanced clusters
Depending on the enhanced features you select for an enhanced cluster, some features are supported differently in enhanced clusters when compared to basic clusters:
  * **Managed and virtual node pools:** In an enhanced cluster, you can choose to create virtual node pools (as well as the managed node pools that you are restricted to creating in a basic cluster). If you choose to create virtual nodes and node pools, then load balancing, pod networking, autoscaling, and application log viewing are supported differently. See [Virtual Nodes and Virtual Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm#contengcomparingvirtualwithmanagednodes_topic-virtualnodes).
  * **Cluster add-ons:** In an enhanced cluster, you can use Kubernetes Engine to manage both essential add-ons and a growing portfolio of optional add-ons. You can enable or disable specific add-ons, select add-on versions, opt into and out of automatic updates by Oracle, and manage add-on specific customizations. See [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
  * **Permissions:** In an enhanced cluster, you can choose to define OCI IAM policies that authorize specific pods to make OCI API calls, and access OCI resources. See [Granting Workloads Access to OCI Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contenggrantingworkloadaccesstoresources.htm#contengmanagingworkloads_topic-grantingworkloadaccesstoresources "Find out how to use the identity of a workload running on a Kubernetes cluster to grant the workload fine-grained access to other OCI resources using Kubernetes Engine \(OKE\).").


In addition, you can [contact us](https://support.oracle.com/) to request an increase to the number of enhanced clusters you can create in a region (see [Kubernetes Engine Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Container_Engine_for_Kubernetes_Limits)).
### Notable features not supported by enhanced clusters
Enhanced clusters support all the features supported by basic clusters. There are no features supported by basic clusters that are not supported by enhanced clusters.
## Basic Clusters 🔗 
Basic clusters support all the core functionality provided by Kubernetes and Kubernetes Engine, but none of the enhanced features that Kubernetes Engine provides with enhanced clusters (such as virtual nodes, cluster add-on management, workload identity, node cycling, self-managed nodes, and additional worker nodes per cluster). Basic clusters come with a service level objective (SLO), but not a financially-backed service level agreement (SLA). 
### Notable features supported differently by basic clusters
Some features are supported differently in basic clusters when compared to enhanced clusters:
  * **Managed and virtual node pools:** In a basic cluster, you can only create managed node pools (rather than the managed and virtual node pools you can choose to create in an enhanced cluster). Load balancing, pod networking, autoscaling, and application log viewing are supported differently with managed nodes and node pools. See [Managed Nodes and Managed Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm#contengcomparingvirtualwithmanagednodes_topic-managednodes).
  * **Cluster add-ons:** In a basic cluster, you have more responsibility and less flexibility when managing cluster add-ons. You are responsible for upgrading essential add-ons, but you cannot install or disable specific add-ons, select add-on versions, opt into and out of automatic updates by Oracle, or manage add-on specific customizations. In addition, you are responsible for installing, managing, and maintaining any optional add-ons you want in the cluster. See [Configuring Cluster Add-ons](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengconfiguringclusteraddons.htm#contengconfiguringclusteraddons "Find out about configuring cluster add-ons in clusters you create using Kubernetes Engine \(OKE\).").
  * **Permissions:** In a basic cluster, you have to define OCI IAM policies that authorize users and instances (rather than workload identity you can choose to implement in an enhanced cluster). Consequently, more privileges are granted than the absolute minimum required, which is not best practice. See [Granting Workloads Access to OCI Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contenggrantingworkloadaccesstoresources.htm#contengmanagingworkloads_topic-grantingworkloadaccesstoresources "Find out how to use the identity of a workload running on a Kubernetes cluster to grant the workload fine-grained access to other OCI resources using Kubernetes Engine \(OKE\).")


In addition, you cannot request an increase to the number of basic clusters you can create in a region (see [Kubernetes Engine Limits](https://docs.oracle.com/iaas/Content/General/Concepts/servicelimits.htm#Container_Engine_for_Kubernetes_Limits)).
### Notable features not supported by basic clusters
Basic clusters do not support some of the features supported by enhanced clusters:
  * Virtual node pools
  * Fine-grained cluster add-on deployment and configuration
  * Workload identity
  * Increased numbers of worker nodes
  * Self-managed nodes
  * Financially-backed service level agreement (SLA)
  * Node cycling when updating or upgrading node pools


Was this article helpful?
YesNo

