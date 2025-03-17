Updated 2024-08-23
# Upgrade Best Practices
_Find out about upgrade best practices for clusters you've created with Kubernetes Engine (OKE)._
This section contains best practices for upgrade and Kubernetes Engine.
## Best Practice: Use the latest version of Kubernetes 🔗 
New Kubernetes releases typically include many updates, additional features, and most importantly, patches to address security issues in previous versions. Kubernetes Engine provides support for three minor versions of Kubernetes, with the latest patch version for each of those versions.
We therefore recommend that:
  * Production clusters always run the latest stable version of Kubernetes. 
  * You specify the latest minor supported version of Kubernetes when creating clusters using Kubernetes Engine.
  * You upgrade existing clusters when Oracle announces Kubernetes Engine support for a Kubernetes major version, minor version, or patch version. Regularly upgrading clusters enables you to avoid situations where clusters are running older Kubernetes versions that do not include the latest features and fixes.


See [Kubernetes Versions and Kubernetes Engine (OKE)](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengupgradeoverview.htm#Kubernetes_Versions_and_Container_Engine_for_Kubernetes "Find out about the Kubernetes versioning scheme and Kubernetes Engine \(OKE\) support for different Kubernetes versions."), [Upgrading Clusters to Newer Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutupgradingclusters.htm#Upgrading_Clusters_to_Newer_Kubernetes_Versions "Find out about the different ways to upgrade control plane nodes and worker nodes to newer Kubernetes versions using Kubernetes Engine \(OKE\).").
## Best Practice: Set up Test and Production environments 🔗 
We recommend that you use multiple Kubernetes Engine environments as part of a workflow to deploy and release applications. Using multiple environments helps to minimize risk and unwanted downtime by enabling you to test software and infrastructure updates in an environment that's separate from the production environment. At a minimum, we recommend that you have a production environment, and a pre-production or test environment. 
We also recommend that before you upgrade a cluster to a new version of Kubernetes, you test any applications deployed on the cluster to confirm that the applications are compatible with the new Kubernetes version. After upgrading control plane nodes to a newer version of Kubernetes, you cannot downgrade the control plane nodes to an earlier Kubernetes version. Hence the importance of testing applications before upgrading the cluster to a new Kubernetes version. For example, before upgrading a cluster, you might create a separate cluster running the new Kubernetes version and test applications on that cluster.
See [Upgrading Clusters to Newer Kubernetes Versions](https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengaboutupgradingclusters.htm#Upgrading_Clusters_to_Newer_Kubernetes_Versions "Find out about the different ways to upgrade control plane nodes and worker nodes to newer Kubernetes versions using Kubernetes Engine \(OKE\).").
## Best Practice: Use a blue-green deployment strategy 🔗 
We recommend that you use a blue-green deployment strategy to reduce risk and minimize downtime when upgrading Kubernetes clusters. Blue-green deployments use two production environments, known as "blue" and "green", to provide reliable testing, continuous no-outage upgrades, and instant rollbacks. Using a blue-green deployment strategy ensures that users have access to one production environment while the other production environment is being updated.
## Best Practice: Schedule maintenance windows 🔗 
We recommend that you schedule maintenance activities during off-peak hours to limit the impact on applications that do not gracefully handle pod interruption caused by cluster/node upgrades and maintenance.
For example, during upgrades, there can be temporary disruptions when workloads are moved in order to recreate nodes. To ensure such disruptions cause minimal impact, where possible:
  * schedule upgrades for off-peak hours
  * design application deployments to handle partial disruptions seamlessly


## Best Practice: Treat worker nodes as immutable 🔗 
We recommend that you treat existing worker nodes as immutable entities.
Any changes you make to a node pool's worker node properties only apply to new worker nodes that are subsequently created. You cannot change the properties of existing worker nodes. 
For example, rather than updating the OS image running on existing worker nodes, consider creating a new node pool with worker nodes that have the updated OS image. Having specified cordon and drain options for the original node pool to prevent new pods starting and to delete existing pods, you can shift work from the original node pool to the new node pool. You can then delete the original node pool. 
See [Creating Worker Nodes with Updated Properties](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingimageworkernode.htm#Upgrading_the_Image_Running_on_Worker_Nodes_by_Creating_a_New_Node_Pool "Find out about the different ways to update worker node properties using Kubernetes Engine \(OKE\).").
## Best Practice: Cordon and drain worker nodes in preparation for maintenance 🔗 
We recommend that you cordon and drain a worker node in advance of scheduled maintenance on that node.
Cordoning marks a worker node as unschedulable and prevents the kube-scheduler from placing new pods onto that node. Draining safely evicts pods from a worker node, which ensures containers terminate gracefully and perform any necessary cleanup.
See [Notes on Cordoning and Draining Managed Nodes Before Termination](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdeletingworkernodes.htm#contengscalingnodepools_topic-Notes_on_cordon_and_drain). Also see [Manual Node Administration](https://kubernetes.io/docs/concepts/architecture/nodes/#manual-node-administration) and [Safely Drain a Node](https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node) in the Kubernetes documentation.
Was this article helpful?
YesNo

