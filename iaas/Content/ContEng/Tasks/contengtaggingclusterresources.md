Updated 2024-08-14
# Tagging Kubernetes Cluster-Related Resources
_Find out about tagging cluster-related resources you create using Kubernetes Engine (OKE)._
You can use Oracle Cloud Infrastructure tags to organize, control, manage, and report on cloud resources used by the Kubernetes clusters you create with Kubernetes Engine. Tagging enables you to group disparate resources across compartments, and also enables you to annotate resources with your own metadata.
Typically, you'll find tagging useful for:
  * **Resource tracking:** For example, to:
    * report all Oracle Cloud Infrastructure resources (compute instances, load balancers, block volumes) associated with a Kubernetes cluster 
    * apply application-specific tags to load balancers and block volumes to track resources for a given application running in a cluster
  * **Cost tracking:** For example, to obtain detailed cost reports for the running of Kubernetes clusters by application, or by line of business.
  * **Authorization grouping:** For example, to authorize managed nodes to access a designated object storage bucket (using instance principals for worker nodes as part of a node pool dynamic group tag).


For more information about using Oracle Cloud Infrastructure tags with Kubernetes Engine, see:
  * [Summary of Tagging Concepts for Kubernetes Clusters](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_summary-tagging-concepts.htm#contengtaggingclusterresources_summary_tagging_concepts "Find out about key concepts when tagging cluster-related resources you create using Kubernetes Engine \(OKE\).")
  * [Applying Tags to Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_tagging-oke-resources.htm#contengtaggingclusterresources_tagging_oke_resources "Find out how to tag cluster-related resources you create using Kubernetes Engine \(OKE\).")
  * [Managing Access By Applying Tags to Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_managing-access-using-tags.htm#contengtaggingclusterresources_managing_access_using_tags "Find out how to use tags and IAM policies to manage access to resources related to the clusters you create using Kubernetes Engine \(OKE\).")
  * [Retired Tags and Cluster-Related Resources](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_retired-tags.htm#contengtaggingclusterresources_retired_tags "Find out about the impact of retiring tags on the cluster-related resources you create using Kubernetes Engine \(OKE\).")
  * [Additional IAM Policy when a Cluster and a Tag Namespace are in Different Compartments](https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengtaggingclusterresources_iam-tag-namespace-policy.htm#contengtaggingclusterresources_iam-tag-namespace-policy "Find out about an additional IAM policy you have to create if you want to apply defined tags from a tag namespace belonging to one compartment to cluster-related resources belonging to a different compartment, when using Kubernetes Engine \(OKE\).")


Was this article helpful?
YesNo

