Updated 2023-12-06
# Tagging Resources on Compute Cloud@Customer
On Compute Cloud@Customer, tagging enables you to add metadata to resources by defining key/value pairs that are assigned to resources. You can use the tags to organize and list resources based on your business needs.
On Compute Cloud@Customer, tags are applied using the same methods as other resources in Oracle Cloud Infrastructure (OCI), using the following practices:
  * [Defined tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm) are set up in your tenancy by an administrator. Only users granted permission to work with the defined tags can apply them to resources. Defined tags provide a key/value map and are organized by combining the tag namespaces with tag keys using dot notation. For example, a tag namespace called `HumanResources` could have a key named `CostCenter`. You then associate the namespace and key `HumanResource.CostCenter` and then assign the tag.
To apply defined tags to resources on Compute Cloud@Customer, first create the namespace and defined tags in the OCI tenancy where the Compute Cloud@Customer infrastructure is located. After one to ten minutes, the namespace and defined tags are synchronized on Compute Cloud@Customer, and can be applied to Compute Cloud@Customer resources.
  * [Free-form tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm) can be applied by any user with permissions on the resource. Free-form tags are a key/value map. These tags can be applied directly to Compute Cloud@Customer resources. Unlike defined tags, free-form tags don't require any configuration at the tenancy level.
  * You can add tags to resources during resource creation. See [Adding Tags at Resource Creation](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/adding-tags-at-resource-creation.htm#adding-tags-at-resource-creation "On Compute Cloud@Customer, any tag defaults that are defined on a compartment are automatically added to all resources that are created in that compartment, or any child compartment of that compartment, after the tag default was defined. A tag default might require you to enter a value for the tag to create the resource.").
  * You can use tags to automatically add user names and creation dates to Compute Cloud@Customer resources. See [Using Tags to Automatically Add User Names and Creation Dates to Resources](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/tags/using-tags-to-automatically-add-user-names.htm#using-tags-to-automatically-add-user-names)


**Note** Defined tags and tag namespaces must be configured in your OCI tenancy. See [Defined tags](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagsandtagnamespaces.htm).
**Note** On the Compute Cloud@Customer infrastructure you can't manage resource tags using bulk add, bulk update, or bulk remove operations.
For more information, refer to these OCI resources:
  * Conceptual information: [Tagging Overview](https://docs.oracle.com/iaas/Content/Tagging/Concepts/taggingoverview.htm)
  * Managing tags: [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags)


Was this article helpful?
YesNo

