Updated 2023-03-13
# Calling Services from an Instance
This topic describes how you can authorize Compute instances to call services in Oracle Cloud Infrastructure.
## Introduction 🔗 
This procedure describes how you can authorize a Compute instance to make API calls in Oracle Cloud Infrastructure services. After you set up the required resources and policies, an application running on an instance can call Oracle Cloud Infrastructure public services, removing the need to configure user credentials or a configuration file.
## Concepts 🔗  

DYNAMIC GROUP
    Dynamic groups allow you to group Oracle Cloud Infrastructure Compute instances as principal actors, similar to user groups. You can then create policies to permit instances in these groups to make API calls against Oracle Cloud Infrastructure services. Membership in the group is determined by a set of criteria you define, called _matching rules_. 

MATCHING RULE
    When you set up a dynamic group, you also define the rules for membership in the group. Resources that match the rule criteria are members of the dynamic group. Matching rules have a specific syntax you follow. See [Writing Matching Rules to Define Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm#Writing "Matching rules define the resources that belong to a dynamic group."). 

INSTANCE PRINCIPALS
    The IAM service feature that enables Compute instances to be authorized actors (or principals) to perform actions on service resources. Each Compute instance has its own identity, and it authenticates using the certificates that are added to it. These certificates are automatically created, assigned to instances and rotated, preventing the need for you to distribute credentials to your hosts and rotate them.
## Security Considerations 🔗 
Any user who has access to the Compute instance (who can SSH to the instance), automatically inherits the privileges granted to the instance. Before you grant permissions to an instance using the process described in this topic, ensure that you know who can access it (either because they have the SSH key or you added them as users to the instance), and that they should be authorized with the permissions you are granting to the instance.
All Compute instance principals are granted the `compartment_inspect` permission. You cannot revoke this permission. This permission allows the instance to ListCompartments in the tenancy to retrieve the following information:
  * Compartment names
  * Compartment descriptions
  * [Free-form tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm) applied to compartments
  * [Automatic tag defaults](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingautomaticdefaulttags.htm) applied to compartments. These tags, such as CreatedBy and CreatedOn, are in the Oracle-Tag namespace and are automatically added by Oracle.


Was this article helpful?
YesNo

