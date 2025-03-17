Updated 2025-02-13
# How Policies Work
This topic describes how policies work and the basic features.
## Overview of Policies 🔗 
A _policy_ is a document that specifies who can access which Oracle Cloud Infrastructure resources that your company has, and how. A policy simply allows a **group** to work in certain ways with specific types of **resources** in a particular **compartment**. If you're not familiar with users, groups, or compartments, see [Overview of Identity and Access Management](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm#Overview_of_Oracle_Cloud_Infrastructure_Identity_and_Access_Management). 
In general, here's the process an IAM administrator in your organization needs to follow:
  1. Define users, groups, and one or more compartments to hold the cloud resources for your organization.
  2. Create one or more policies, each written in the policy language. See [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
  3. Place users into the appropriate groups depending on the compartments and resources they need to work with.
  4. Provide the users with the one-time passwords that they need in order to access the Console and work with the compartments. For more information, see [User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/usercredentials.htm#User_Credentials). 


After the administrator completes these steps, the users can access the Console, change their one-time passwords, and work with specific cloud resources as stated in the policies. 
## Policy Basics 🔗 
To govern control of your resources, your company will have at least one policy. Each policy consists of one or more policy _statements_ that follow this basic syntax:
```
Allow group <group_name> to <verb> <resource-type> in compartment <compartment_name>
```

Notice that the statements always begin with the word `Allow`. Policies only _allow_ access; they cannot deny it. Instead there's an implicit deny, which means by default, users can do nothing and have to be granted access through policies. (There's one exception to this rule; see [Can users do anything without an administrator writing a policy for them?](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Can)) 
An administrator in your organization defines the groups and compartments in your tenancy. Oracle defines the possible verbs and resource-types you can use in policies (see [Verbs](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Verbs) and [Resource-Types](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Resource-Types)).
In some cases you'll want the policy to apply to the tenancy and not a compartment inside the tenancy. In that case, change the end of the policy statement like so:
```
Allow group <group_name> to <verb> <resource-type> in tenancy
```

For more details about the syntax, see [Policy Syntax](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policysyntax.htm#Policy_Syntax).
For information about how many policies you can have, see [Service Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase.").
### A Few Examples 🔗 
Let's say your administrator creates a group called _HelpDesk_ whose job is to manage users and their credentials. Here is a policy that enables that: 
```
Allow group HelpDesk to manage users in tenancy
```

Notice that because users reside in the tenancy (the root compartment), the policy simply states the word `tenancy`, without the word `compartment` in front of it.
Next, let's say you have a compartment called _Project-A_ , and a group called _A-Admins_ whose job is to manage all of the Oracle Cloud Infrastructure resources in the compartment. Here's an example policy that enables that:
```
Allow group A-Admins to manage all-resources in compartment Project-A
```

Be aware that the policy directly above includes the ability to write policies _for that compartment_ , which means A-Admins can control access to the compartment's resources. For more information, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3).
If you wanted to limit A-Admins' access to only launching and managing compute instances and block storage volumes (both the volumes and their backups) in the Project-A compartment, but the network itself lives in the Networks compartment, then the policy could instead be:
```
Allow group A-Admins to manage instance-family in compartment Project-A
Allow group A-Admins to manage volume-family in compartment Project-A
Allow group A-Admins to use virtual-network-family in compartment Networks
```

The third statement with the `virtual-network-family` resource-type enables the instance launch process, because the cloud network is involved. Specifically, the launch process creates a new VNIC and attaches it to the subnet where the instance resides.
For additional examples, see [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
### Details about Specifying Groups and Compartments 🔗 
Typically you'll specify a group or compartment by name in the policy. However, you can use the OCID instead. Just make sure to add "`id`" before the OCID. For example:
```
Allow group
 id ocid1.group.oc1..aaaaaaaaqjihfhvxmumrl3isyrjw3n6c4rzwskaawuc7i5xwe6s7qmnsbc6a
 to manage instance-family in compartment Project-A
```

You can specify multiple groups separated by commas: 
```
Allow group A-Admins, B-Admins to manage instance-family in compartment Projects-A-and-B
```

### Verbs 🔗 
Oracle defines the possible verbs you can use in your policies. Here's a summary of the verbs, from least amount of access to the most: 
Verb | Target User | Types of Access Covered  
---|---|---  
`inspect` | Third-party auditors | Ability to list resources, without access to any confidential information or user-specified metadata that might be part of that resource. **Important:** The operation to list policies includes the contents of the policies themselves. The list operations for the Networking resource-types return all the information (for example, the contents of security lists and route tables).   
`read` | Internal auditors | Includes `inspect` plus the ability to get user-specified metadata and the actual resource itself.   
`use` | Day-to-day end users of resources | Includes `read` plus the ability to work with existing resources (the actions vary by resource type). Includes the ability to update the resource, except for resource-types where the "update" operation has the same effective impact as the "create" operation (for example, `UpdatePolicy`, `UpdateSecurityList`, and more), in which case the "update" ability is available only with the `manage` verb. In general, this verb doesn't include the ability to create or delete that type of resource.  
`manage` | Administrators | Includes all permissions for the resource.  
The verb gives a certain general type of access (for example, `inspect` lets you list and get resources). When you then join that type of access with a particular resource-type in a policy (for example, `Allow group XYZ to inspect compartments in the tenancy`), then you give that group access to a specific set of permissions and API operations (for example, `ListCompartments`, `GetCompartment`). For more examples, see [Details for Verbs + Resource-Type Combinations](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#Identity). Each service details the list of API operations covered for each combination of verb and resource-type. 
some special exceptions or nuances for certain resource-types. 
**Users:** Access to both `manage users` and `manage groups` lets you do anything with users and groups, including creating and deleting users and groups, and adding/removing users from groups. To add/remove users from groups without access to creating and deleting users and groups, only both `use users` and `use groups` are required. See [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top). 
**Policies:** The ability to update a policy is available only with `manage policies`, not `use policies`, because updating a policy is similar in effect to creating a new policy (you can overwrite the existing policy statements). In addition, `inspect policies `lets you get the full contents of the policies. 
**Object Storage objects:** `inspect objects` lets you list all the objects in a bucket and do a HEAD operation for a particular object. In comparison, `read objects` lets you download the object itself.
**Load Balancer resources:** Be aware that `inspect load-balancers` lets you get _all_ information about your load balancers and related components (backend sets, and more.). 
**Networking resources:**
Be aware that the `inspect` verb not only returns general information about the cloud network's components (for example, the name and OCID of a security list, or of a route table). It also includes the contents of the component (for example, the actual rules in the security list, the routes in the route table, and so on). 
Also, the following types of abilities are available only with the `manage` verb, not the `use` verb:
  * Update (enable/disable) `internet-gateways`
  * Update `security-lists`
  * Update `route-tables`
  * Update `dhcp-options`
  * Attach a Dynamic Routing Gateway (DRG) to a Virtual Cloud Network (VCN)
  * Create an IPSec connection between a DRG and customer-premises equipment (CPE)
  * Peer VCNs


**Important** Each VCN has various components that directly affect the behavior of the network (route tables, security lists, DHCP options, Internet Gateway, and so on). When you create one of these components, you establish a relationship between that component and the VCN, which means you must be allowed in a policy to both create the component and manage the VCN itself. However, the ability to _update_ that component (to change the route rules, security list rules, and so on) **doesn't** require permission to manage the VCN itself, even though changing that component can directly affect the behavior of the network. This discrepancy is designed to give you flexibility in granting least privilege to users, and not require you to grant excessive access to the VCN so the user can manage other components of the network. Be aware that by giving someone the ability to update a particular type of component, you're implicitly trusting them with controlling the network's behavior.
### Resource-Types 🔗 
Oracle also defines the resource-types you can use in your policies. First, there are _individual_ types. Each individual type represents a specific type of resource. For example, the `vcns` resource-type is specifically for virtual cloud networks (VCNs). 
To make policy writing easier, there are _family_ types that include multiple individual resource-types that are often managed together. For example, the `virtual-network-family` type brings together a variety of types related to the management of VCNs (e.g., `vcns`, `subnets`, `route-tables`, `security-lists`, etc.). If you need to write a more granular policy that gives access to only an individual resource-type, you can. But you can also easily write a policy to give access to a broader range of resources.
In another example: Block Volume has `volumes`, `volume-attachments`, and `volume-backups`. If you need to give access to only making backups of volumes, you can specify the` volume-backups` resource-type in your policy. But if you need to give broad access to all of the Block Volume resources, you can specify the family type called `volume-family`. For a full list of the family resource-types, see [Resource-Types](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/policyreference.htm#Resource).
**Important** If a service introduces new individual resource-types, they will typically be included in the family type for that service. For example, if Networking introduces a new individual resource-type, it will be automatically included in the definition of the `virtual-network-family` resource type. For more information about future changes to the definitions of resource-types, see [Policies and Service Updates](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policies).
Note that there are other ways to make policies more granular, such as the ability to specify conditions under which the access is granted. For more information, see [Advanced Policy Features](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policyadvancedfeatures.htm#Advanced_Policy_Features).
**Important** If a service introduces new permissions for an existing resource type, you must update the policy statement for the existing resource type to make the new permissions take effect. For more information, see [New permissions in resource-types are not propagated](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/known-issues_root.htm#new-permissions-in-family) for more information.
### Access that Requires Multiple Resource-Types 🔗 
Some API operations require access to multiple resource-types. For example, `LaunchInstance` requires the ability to create instances and work with a cloud network. The `CreateVolumeBackup` operation requires access to both the volume and the volume backup. That means you'll have separate statements to give access to each resource-type (for an example, see [Let volume backup admins manage only backups](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#volume-backup-admins-manage-only-backups)). These individual statements do not have to be in the same policy. And a user can gain the required access from being in different groups. For example, George could be in one group that gives the required level of access to the `volumes` resource-type, and in another group that gives the required access to the `volume-backups` resource-type. The sum of the individual statements, regardless of their location in the overall set of policies, gives George access to `CreateVolumeBackup`.
### Policy Inheritance 🔗 
A basic feature of policies is the concept of _inheritance_ : Compartments inherit any policies from their parent compartment. The simplest example is the Administrators group, which automatically comes with your tenancy (see [The Administrators Group and Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm#The)). There's a built-in policy that enables the Administrators group to do anything in the tenancy:
```
Allow group Administrators to manage all-resources in tenancy
```

Because of policy inheritance, the Administrators group can also do anything in _any_ of the compartments in the tenancy. 
To illustrate further, consider a tenancy with three levels of compartments: CompartmentA, CompartmentB, and ComparmentC, shown here:
[![Image shows CompartmentA. CompartmentB, CompartmentC hierarchy](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_compartment_hierarchy.PNG)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_compartment_hierarchy.PNG)
Policies that apply to resources in CompartmentA also apply to resources in CompartmentB and CompartmentC. So this policy:
```
Allow group NewtworkAdmins to manage virtual-network-family in compartment CompartmentA
```

allows the group NetworkAdmins to manage VCNs in CompartmentA, CompartmentB, and CompartmentC.
### Policy Attachment 🔗 
Another basic feature of policies is the concept of _attachment_. When you create a policy you must attach it to a compartment (or the tenancy, which is the root compartment). **Where you attach it controls who can then modify it or delete it.** If you attach it to the tenancy (in other words, if the policy _is in_ the root compartment), then anyone with access to manage policies in the tenancy can then change or delete it. Typically that's the Administrators group or any similar group you create and give broad access to. Anyone with access only to a child compartment cannot modify or delete that policy. 
If you instead attach the policy to a child compartment, then anyone with access to manage the policies _in that compartment_ can change or delete it. In practical terms, this means it's easy to give compartment administrators (i.e., a group with access to `manage all-resources` in the compartment) access to manage their own compartment's policies, without giving them broader access to manage policies that reside in the tenancy. For an example that uses this kind of compartment administrator design, see [Example Scenario](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm#Example). (Recall that because of policy inheritance, users with access to manage policies in the tenancy automatically have the ability to manage policies in compartments inside the tenancy.) 
The process of attaching the policy is easy (whether attaching to a compartment or the tenancy): If you're using the Console, when you add the policy to IAM, simply make sure you're in the desired compartment when you create the policy. If you're using the API, you specify the OCID of the desired compartment (either the tenancy or other compartment) as part of the request to create the policy. 
When you attach a policy to a compartment, you must be in that compartment _and_ you must indicate directly in the statement which compartment it applies to. If you are not in the compartment, you'll get an error if you try to attach the policy to a different compartment. Notice that attachment occurs during policy creation, which means a policy can be attached to only one compartment. To learn how to attach a policy to a compartment, see [To create a policy](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy).
### Policies and Compartment Hierarchies 🔗 
As described in the previous section, a policy statement must specify the compartment for which access is being granted (or the tenancy). Where you create the policy determines who can update the policy. If you attach the policy to the compartment or its parent, you can simply specify the compartment name. If you attach the policy further up the hierarchy, you must specify the path. The format of the path is each compartment name (or OCID) in the path, separated by a colon:
<compartment_level_1>**:** <compartment_level_2>**:** . . . <compartment_level_n>
For example, assume you have a three-level compartment hierarchy, shown here:
[![Image shows CompartmentA. CompartmentB, CompartmentC hierarchy](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_compartment_hierarchy.PNG)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_compartment_hierarchy.PNG)
You want to create a policy to allow NetworkAdmins to manage VCNs in CompartmentC. If you want to attach this policy to CompartmentC or to its parent, CompartmentB, write this policy statement:
Copy
```
Allow group NewtworkAdmins to manage virtual-network-family in compartment CompartmentC
```

However, if you want to attach this policy to CompartmentA (so that only administrators of CompartmentA can modify it), write this policy statement that specifies the path:
Copy
```
Allow group NewtworkAdmins to manage virtual-network-family in compartment CompartmentB:CompartmentC
```

To attach this policy to the tenancy, write this policy statement that specifies the path from CompartmentA to CompartmentC:
Copy
```
Allow group NewtworkAdmins to manage virtual-network-family in compartment CompartmentA:CompartmentB:CompartmentC
```

### Policies and Service Updates 🔗 
It's possible that the definition of a verb or resource-type could change in the future. For example, let's say that the `virtual-network-family` resource-type changes to include a new kind of resource that's been added to Networking. By default, your policies automatically stay current with any changes in service definition, so any policy you have that gives access to `virtual-network-family` would automatically include access to the newly added resource. 
**Important** If a service introduces new permissions for an existing resource type, you must update the policy statement for the existing resource type to make the new permissions take effect. For more information, see [New permissions in resource-types are not propagated](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/known-issues_root.htm#new-permissions-in-family) for more information.
### Writing Policies for Each Service 🔗 
The [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.") includes details of the specific resource-types for each service, and which verb + resource-type combination gives access to which API operations.
Was this article helpful?
YesNo

