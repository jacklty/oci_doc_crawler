Updated 2024-04-29
# Tagging Resources
Review how tagging propagates through resources managed by Resource Manager.
When you have many resources (for example, instances, VCNs, load balancers, and block volumes) across multiple compartments in your tenancy, it can become difficult to track resources used for specific purposes, or to aggregate them, report on them, or take bulk actions on them. _Tagging_ allows you to define keys and values and associate them with resources. You can then use the tags to help you organize and list resources based on your business needs.
There are two types of tags:
_[Defined tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm)_ are set up in your tenancy by an administrator. Only users granted permission to work with the defined tags can apply them to resources. Defined tags provide a key/value map and are organized by combining the tag namespaces with tag keys using dot notation. For example, a tag namespace called `HumanResources` could have a key named `CostCenter`. You then associate the namespace and key `HumanResource.CostCenter` and then assign the tag.
_[Free-form tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm)_ can be applied by any user with permissions on the resource. Freeform tags are simple key/value map.
  * Refer to the `oci_identity_tag_namespace` reference for guidance on managing the lifecycle of tag namespaces.
  * Refer to the `oci_identity_tag` reference for guidance on managing tags.


The [`tags.tf`](https://github.com/oracle/terraform-provider-oci/blob/master/examples/identity/tags.tf) configuration file in our examples contains several tagging-related resources.
The full reference of the OCI Terraform provider's supported resources and data sources contains usage, argument, and attribute details. The full reference is available at [docs.oracle.com](https://docs.oracle.com/iaas/tools/terraform-provider-oci/latest/) and [Terraform Registry](https://registry.terraform.io/providers/oracle/oci/latest/docs).
For more detailed information about tags and their features, see [Tagging Overview](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm).
## Propagation of Tagging on Resources 🔗 
OCI services propagate all of a primary resource's freeform tags and defined tags to secondary resources when both resources support the type of tags. For example, if your Terraform configuration has a compute instance as a primary resource and a VNIC as a nested secondary resource, any tags on the compute instance are propagated to the VNIC.
This propagation could cause a drift in the Terraform state resulting in a diff after apply. To avoid potential drift, explicitly add all the primary resource's freeform tags and defined tags on the secondary resources as part of the configuration. 
The same behavior can be seen while using the **Tag Default** or **Required Tags** feature. Avoid drift by applying the **Tag Default** or **Required Tags** on all resources (primary and secondary, if any) in the tenancy where **Tag Default** or **Required Tags** exist.
Was this article helpful?
YesNo

