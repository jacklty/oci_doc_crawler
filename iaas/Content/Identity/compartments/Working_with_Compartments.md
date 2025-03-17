Updated 2024-07-08
# Working with Compartments
Learn about how to use compartments to organize your cloud resources in OCI.
When you first start working with Oracle Cloud Infrastructure, you need to think carefully about how you want to use compartments to organize and isolate your cloud resources. Compartments are fundamental to that process. Most resources can be moved between compartments. However, it's important to think through your compartment design for your organization up front, before implementing anything. For more information, see [Learn Best Practices for Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm). 
The Console is designed to display your resources by _compartment_ within the current region. When you work with your resources in the Console, you must choose which compartment to work in from a list on the page. That list is filtered to show only the compartments in the tenancy that you have permission to access. If you're an administrator, you'll have permission to view all compartments and work with any compartment's resources, but if you're a user with limited access, you probably won't. 
Compartments are tenancy-wide, across regions. When you create a compartment, it is available in every region that your tenancy is subscribed to. You can get a cross-region view of your resources in a specific compartment with the tenancy explorer. See [Viewing All Resources in a Compartment](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm#Viewing_All_Resources_in_a_Compartment).
For added security, you can associate a compartment with a security zone. For more information, see [Security Zones](https://docs.oracle.com/iaas/security-zone/home.htm).
This introduction covers the following topics.
  * [Access Control for Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Access_Control_for_Compartments)
  * [Putting Resources in a Compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Putting_Resources_in_a_Compartment)
  * [Discovering Resources in Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#StacksfromCompartments)
  * [Implications for Moving Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#MoveCompartment)


## Access Control for Compartments 🔗 
After creating a compartment, you need to write at least one **policy** for it, otherwise no one can access it (except administrators or users who have permissions set at the tenancy level). When creating a compartment inside another compartment, the compartment inherits access permissions from compartments higher up its hierarchy. For more information, see [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Inheritance.htm#top "A basic policy feature is the concept of inheritance in IAM.").
When you create an access policy, you need to specify which compartment to attach it to. This controls who can later modify or delete the policy. Depending on how you've designed your compartment hierarchy, you might attach it to the tenancy, a parent, or to the specific compartment itself. For more information, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Attachment.htm#top "When you create an IAM policy, you must attach it to a compartment in IAM."). 
## Putting Resources in a Compartment 🔗 
To place a new resource in a compartment, you simply specify that compartment when creating the resource (the compartment is one of the required pieces of information to create a resource). If you're working in the Console, you just make sure you're first viewing the compartment where you want to create the resource. Keep in mind that most IAM resources reside in the tenancy (this includes users, groups, compartments, and any policies attached to the tenancy) and can't be created in or managed from a specific compartment. 
## Discovering Resources in Compartments 🔗 
With [Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm) you can capture deployed resources as Terraform configuration and state files using [resource discovery](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#features__resourcediscovery). The created stack provides you with a Terraform configuration that you can use to programmatically manage, version, and persist your IT infrastructure as "infrastructure as code."
A stack created from a compartment represents all [supported resources](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resource-discovery.htm#supported-resources) in the entire compartment, at the appropriate scope. If you select the root compartment for your tenancy, then the scope is the tenancy level, such as users and groups. If you select a non-root compartment, then the scope is compartment level, such as compute instances.
Stack creation is supported from a single compartment only. Stacks can't be created from nested compartments.
For instructions, see [Creating a Stack from an Existing Compartment](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm).
## Implications for Moving Compartments 🔗 
You can move a compartment to a different parent compartment within the same tenancy. When you move a compartment, all its contents (subcompartments and resources) are moved with it. Moving a compartment has implications for the contents. These implications are described in the following sections. Ensure that you are aware of these before you move a compartment.
  * [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Required)
  * [Restrictions on Moving Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Restrict)
  * [Understanding the Policy Implications When You Move a Compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Understa)
  * [Policy Examples](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Policy_Examples)
  * [Groups with Permissions in the Current Compartment Lose Access; Groups with Permissions in the Destination Compartment Gain Access](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Groups_with_Permissions_in_the_Current_Compartment_Lose_Access_Groups_with_Permissions_in_the_Destination_Compartment_Gain_Access)
  * [Automatic Update of Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Automatic_Update_of_Policies)
  * [Understanding Compartment Quota Implications When You Move a Compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Understa2)
  * [Understanding Tagging Implications When You Move a Compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/Working_with_Compartments.htm#Understa3)


### Required IAM Policy 🔗 
To move a compartment, you must belong to a group that has `manage all-resources` permissions on the lowest shared parent compartment of the current compartment and the destination compartment.
### Restrictions on Moving Compartments 🔗 
  * You can't move a compartment if the source or destination is part of a [security zone](https://docs.oracle.com/iaas/security-zone/home.htm). You must use the Security Zones console to [manage compartments](https://docs.oracle.com/iaas/security-zone/using/managing-security-zones.htm) within a security zone.
  * You can't move a compartment to a destination compartment with the same name as the compartment being moved. 
For example, assume compartment A and compartment B are both under the root compartment. Under compartment A is a subcompartment, also called compartment B. You can't move the compartment B to the parent compartment B.
[![Compartment B can't be moved to a parent compartment also named Compartment B](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_samename.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_samename.png)
Item | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) | Two compartments within the same parent can't have the same name. Therefore you can't move a compartment to a destination compartment where a compartment with the same name already exists.   


### Understanding the Policy Implications When You Move a Compartment 🔗 
After you move a compartment to a new parent compartment, the access policies of the new parent take effect and the policies of the previous parent no longer apply. Before you move a compartment, ensure that:
  * You are aware of the policies that govern access to the compartment in its current position.
  * You are aware of the polices in the new parent compartment that will take effect when you move the compartment.


In some cases, when moving nested compartments with policies that specify the hierarchy, the polices are automatically updated to ensure consistency. 
### Policy Examples 🔗 
#### Groups with Permissions in the Current Compartment Lose Access; Groups with Permissions in the Destination Compartment Gain Access 🔗 
The following figure shows a compartment hierarchy in which compartment C, a child of A:B is moved to the hierarchy A:D.
[![Compartment C is moved from A:B to A:D](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_policy1.PNG)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_policy1.PNG)
Item | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) |  The tenancy has the following policies defined for compartments B and D: Policy1: `Allow group G1 to manage instance-family in compartment A:B`  
![Callout 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable2.png) |  Impact when compartment C is moved from B to D: Policy2: `Allow group G2 to manage instance-family in compartment A:D`  
  * Group G1 can no longer manage instance-families in compartment C.
  * Group G2 can now manage instance-families in compartment C.


Ensure that you are aware not only of what groups lose permissions when you move a compartment, but also what groups will gain permissions.
#### Automatic Update of Policies 🔗 
When you move a compartment, some polices will be automatically updated. Policies that specify the compartment hierarchy down to the compartment being moved will automatically be updated when the policy is attached to a shared ancestor of the current and target parent. Consider the following examples:
**Example 1: Policy automatically updated**
[![Policy is automatically updated when the policy is attached to a shared ancestor](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample1.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample1.png)
Item | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) | Policy:```
Allow group G1 to manage buckets in compartment Test:A 
```
  
![Callout 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable2.png) | Policy:```
Allow group G1 to manage buckets in compartment Dev:A
```
  
![Callout 3](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable3.png) | The policy is automatically updated. Group G1 does not lose permissions.   
In this example, you move compartment A from Operations:Test to Operations:Dev. The policy that governs compartment A is attached to the shared parent, Operations. When the compartment is moved, the policy statement is automatically updated by the IAM service to specify the new compartment location.
No manual intervention is required to allow group G1 to continue to access compartment A in its location.
**Example 2: Policy not updated**
[![Policy isn't updated](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample2.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample2.png)
Item | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) | Policy: Allow group G1 to manage buckets in compartment A  
![Callout 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable2.png) | Policy: Allow group G1 to manage buckets in compartment A  
![Callout 3](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable3.png) | The policy isn't updated. Group G1 loses this permission. This policy is invalid and must be manually removed.   
In this example, you move compartment A from Operations:Test to Operations:Dev. However, the policy that governs compartment A here is attached directly to the Test compartment. When the compartment is moved, the policy isn't automatically updated. The policy that specifies compartment A is no longer valid and must be manually removed. Group G1 no longer has access to compartment A in its new location under Dev. Unless another existing policy grants access to group G1, you must create a new policy to allow G1 to continue to manage buckets in compartment A. 
**Example 3: Policy attached to the tenancy is updated**
[![Policy is automatically updated when the policy is attached to a shared ancestor](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample3.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample3.png)
Item | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) | Policy: Allow group G1 to manage buckets in compartment Operations:Test:A  
![Callout 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable2.png) | Policy: Allow group G1 to manage buckets in compartment HR:Prod:A  
![Callout 3](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable3.png) | The policy is automatically updated. Group G1 does not lose permissions.  
In this example, you move compartment A from Operations:Test to HR:Prod. The policy that governs compartment A is attached to the tenancy, which is a shared ancestor by the original parent compartment and the new parent compartment. Therefore, when the compartment is moved, the policy statement is automatically updated by the IAM service to specify the new compartment location.
### Understanding Compartment Quota Implications When You Move a Compartment 🔗 
When you move one compartment to another, resource quotas in the destination compartment aren't verified and aren't enforced. Therefore, if the compartment move results in a quota violation in the destination compartment, the move isn't blocked. After the move is complete, the destination compartment will be in an over-quota state. You will not be able to create new resources that are over-quota until you either adjust the quotas for the destination compartment or remove resources to comply with the existing quota. For more information on managing compartment quotas, see [Overview of Compartment Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).
### Understanding Tagging Implications When You Move a Compartment 🔗 
Tags aren't automatically updated after a compartment move. If you have implemented a tagging strategy based on compartment, you must update the tags on the resources after the move. For example, assume CompartmentA has a child compartment, CompartmentB. CompartmentA is set up with tag defaults so that every resource in CompartmentA is tagged with TagA. Therefore CompartmentB and all its resources are tagged with default tag, TagA. When you move CompartmentB to CompartmentC, it will still have the default tags from CompartmentA. If you have set up default tags for CompartmentC, you'll need to add those to the resources in the moved compartment.
[![Tag defaults aren't updated after a compartment is moved](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_tag_defaults.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_tag_defaults.png)
Item | Description  
---|---  
![Callout 1](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable1.png) | All the resources in CompartmentB are tagged with the default tags defined for its parent, CompartmentA.  
![Callout 2](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/callout_iamtable2.png) | When CompartmentB is moved to CompartmentC, the default tags aren't updated. CompartmentB still has the default tags from CompartmentA applied.  
Was this article helpful?
YesNo

