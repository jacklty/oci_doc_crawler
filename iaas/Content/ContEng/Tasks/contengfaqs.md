Updated 2024-08-23
# Frequently Asked Questions About Kubernetes Engine (OKE)
_Find out answers to frequently asked questions about Kubernetes Engine (OKE)._
This topic provides answers to some frequently asked questions about Kubernetes Engine.
## Does Kubernetes Engine (OKE) Support Alpha and Beta Features in Kubernetes? 🔗 
Periodically, Kubernetes releases new features. New Kubernetes features are introduced in the following stages, as described in the [Kubernetes documentation](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-stages) and summarized below: 
  * **Alpha stage:** An Alpha feature is disabled by default, might contain bugs, and might change or be dropped at any time. The feature is recommended for short-lived testing clusters only.
  * **Beta stage:** A Beta feature is usually enabled by default, has been well-tested, and will not be dropped. However, details of the feature might change in incompatible ways, and is recommended for non-business-critical use only.
  * **General Availability stage:** A Generally Available (or Stable) feature is always enabled, and will appear in released software for many subsequent versions.


Kubernetes Engine supports the use of Kubernetes Beta features that are enabled by default in Kubernetes. Kubernetes Engine does not support Alpha features, nor Beta features that are disabled by default.
For more information about Kubernetes Alpha and Beta features, see the [Kubernetes documentation](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features).
## What Are VCN-Native Clusters? 🔗 
Kubernetes Engine creates Kubernetes clusters that are completely integrated with your Oracle Cloud Infrastructure Virtual Cloud Network (VCN). Worker nodes, load balancers, and the Kubernetes API endpoint are part of your VCN, and you can configure them as public or private. Such clusters that are fully integrated with your VCN are known as "VCN-native clusters".
**Note**
In earlier releases, clusters were provisioned with public Kubernetes API endpoints that were not integrated into your VCN.
You can continue to create such clusters using the CLI or API, but not the Console. Note that you can only create these clusters as basic clusters, not as enhanced clusters.
## What Are Virtual Nodes and Virtual Node Pools? 🔗 
Virtual nodes are fully managed by Oracle. Virtual nodes provide a 'serverless' Kubernetes experience, enabling you to run containerized applications at scale without the operational overhead of upgrading the data plane infrastructure and managing the capacity of clusters. You can only create virtual nodes in enhanced clusters.
By contrast, managed nodes run on compute instances (either bare metal or virtual machine) in your tenancy, and are at least partly managed by you. As you are responsible for managing managed nodes, you have the flexibility to configure them to meet your specific requirements. You are responsible for upgrading Kubernetes on managed nodes, and for managing cluster capacity. You can create managed nodes in both basic clusters and enhanced clusters.
For a detailed comparison of virtual nodes and managed nodes, see [Comparing Virtual Nodes with Managed Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcomparingvirtualwithmanagednodes_topic.htm#contengusingvirtualormanagednodes_topic "Find out about the differences between the virtual nodes and managed nodes you can create using Kubernetes Engine \(OKE\).").
Was this article helpful?
YesNo

