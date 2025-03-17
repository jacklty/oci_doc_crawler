Updated 2024-08-14
# Retired Tags and Cluster-Related Resources
_Find out about the impact of retiring tags on the cluster-related resources you create using Kubernetes Engine (OKE)._
Oracle Cloud Infrastructure Tagging supports the concept of retiring tags (see [Tags and Tag Namespace Concepts](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)). If a tag is retired, the tag is not removed from resources it was previously applied to. However, the retired tag can no longer be applied to new resources.
In the context of Kubernetes clusters, existing cluster-related resources to which a tag has already been applied continue to function as normal if the tag is subsequently retired. The tag still exists as metadata on those resources, and you can still use the retired tag in operations such as listing, sorting, and reporting. 
However, attempting to apply a retired tag to new cluster-related resources will return an error. If a tag is retired that was previously specified as a tag default, node tag, initial load balancer tag, or initial block volume tag, then new corresponding cluster-related resources cannot be created. 
In particular, if a managed node pool definition specifies a node tag and the tag is subsequently retired, the node pool cannot scale out because new worker nodes cannot be created. To enable the node pool to scale out, remove the retired tag from the node pool definition.
Was this article helpful?
YesNo

