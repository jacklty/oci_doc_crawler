Updated 2024-08-14
# Applying Tags to Cluster-Related Resources 
_Find out how to tag cluster-related resources you create using Kubernetes Engine (OKE)._
You can apply tags to all cluster-related resources.
If you use the 'Custom Create' workflow to create a new cluster, you can specify defined and free-form tags to apply to cluster-related resources (the cluster itself, node pools, nodes, load balancers, and block storage volumes). In the case of load balancers and block storage volumes, you can override these 'initial' tags using annotations and parameters in manifest files.
If you use the 'Quick Create' workflow to create a new cluster, a free-form tag is automatically added to all the resources that are created (to the cluster itself, as well as to any new VCNs, subnets, security lists, internet gateways, service gateways, and NAT gateways). In addition, a free-form tag is also automatically added to new managed node pools and managed nodes (compute instances) created as part of the 'Quick Create' workflow. These free-form tags are not added to resources if you use the 'Custom Create' workflow to create the cluster.
When tags are applied to cluster-related resources, you can use the tags to filter the resources you see in the Console. For more information, see [Filtering the Displayed List of Resources](https://docs.oracle.com/iaas/Content/GSG/Concepts/search-filter.htm#Filterin).
For more information about applying tags to particular types of resources, see:
  * [Applying Tags to Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_cluster-tags.htm#contengtaggingclusterresources_tagging_oke_resources_cluster_tags "Find out how to apply tags to Kubernetes clusters you create using Kubernetes Engine \(OKE\).")
  * [Applying Tags to Node Pools](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_node-pool-tags.htm#contengtaggingclusterresources_tagging_oke_resources_node_pool_tags "Find out how to apply tags to node pools you create using Kubernetes Engine \(OKE\).")
  * [Applying Tags to Nodes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_node-tags.htm#contengtaggingclusterresources_tagging_oke_resources_node_tags "Find out how to apply tags to worker nodes in node pools you create using Kubernetes Engine \(OKE\).")
  * [Applying Tags to Load Balancers](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_load-balancer-tags.htm#contengtaggingclusterresources_tagging_oke_resources_load_balancer_tags "Find out how to apply tags to load balancer resources, and how to override initial load balancer tags, when using Kubernetes Engine \(OKE\).")
  * [Applying Tags to Block Volumes](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources_block-volume-tags.htm#contengtaggingclusterresources_tagging_oke_resources_block_volume_tags "Find out how to apply tags to block volume resources, and how to override initial block volume tags, when using Kubernetes Engine \(OKE\).")


Was this article helpful?
YesNo

