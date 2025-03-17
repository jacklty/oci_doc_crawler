Updated 2024-08-14
# Summary of Tagging Concepts for Kubernetes Clusters
_Find out about key concepts when tagging cluster-related resources you create using Kubernetes Engine (OKE)._
The [Oracle Cloud Infrastructure Tagging service documentation](https://docs.oracle.com/iaas/Content/Tagging/home.htm) describes how tagging works in detail. This topic summarizes some of the key concepts you need to be familiar with when tagging cluster-related resources you create with Kubernetes Engine.
## Defined tags
Defined tags are set up and managed by a tag administrator. A defined tag consists of a tag namespace, a key, and a value. The tag namespace and tag key definition must be set up in a tenancy before you can apply a defined tag to a resource. 
The tag administrator can set up a defined tag key with either a tag value type of string (enabling you to add a value, or leave blank), or with a list of predefined values (from which you must choose a value). The tag administrator can specify tag variables to set the value of a defined tag.
You can apply a defined tag when creating a new resource, or when updating an existing resource. When applying a defined tag, you select the defined tag from a list of defined tags.
For more information, see [Tags and Tag Namespace Concepts](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm).
## Free-form tags
Free-form tags are not managed by a tag administrator. A free-form tag consists of a key and a value. Unlike defined tags, free-form tags do not belong to a tag namespace. 
Free-form tags cannot be set up with pre-defined values, or with tag variables. You cannot include free-form tags in IAM policies.
You can apply a free-form tag when creating a new resource, or when updating an existing resource. When applying a free-form tag, you don't see a list of existing free-form tags from which to select.
For more information, see [Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).
## Tag Defaults
Tag defaults are set up and managed for a specific compartment. Tag defaults are compartment-specific. Tag defaults specify tags that are applied automatically to all resources created in a specific compartment at the time of creation. A maximum of five tag defaults can be set up for each compartment.
Tag defaults must have a tag value. When a tag default is set up, the value of the tag default is specified as one of the following:
  * a default value, which is always applied to all resources created in the compartment, with no input from the user creating the resource
  * a user-applied value, which the user creating a resource in the compartment must enter at the time of resource creation


Note that if tag defaults are updated or deleted, existing tags that have already been applied to resources are not modified.
For more information, see [Managing Tag Defaults](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagdefaults.htm).
## Cost-Tracking Tags
All defined tags can be used for [Cost Analysis](https://docs.oracle.com/iaas/Content/Billing/Concepts/costanalysisoverview.htm) and in [Cost and Usage Reports](https://docs.oracle.com/iaas/Content/Billing/Concepts/costusagereportsoverview.htm). However, you can also designate one or more defined tags as cost-tracking tags, for use when [setting budgets](https://docs.oracle.com/iaas/Content/Billing/Concepts/budgetsoverview.htm). Cost-tracking tags enable you to set soft limits on your Oracle Cloud Infrastructure spending. You can set alerts on your budget to let you know when you might exceed your budget, and you can view all of your budgets and spending from a single place in the Console. 
For more information, see [Using Cost-Tracking Tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/usingcosttrackingtags.htm).
Was this article helpful?
YesNo

