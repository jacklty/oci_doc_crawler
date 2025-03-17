Updated 2025-01-14
# Managing Compartments
This topic describes the basics of working with compartments.
## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access for managing compartments. 
For an additional policy related to compartment management, see [Let a compartment admin manage the compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#compartment-admin-manage-compartment).
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top). If you want to dig deeper into writing policies for compartments or other IAM components, see [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top).
## Tagging Resources 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Working with Compartments 🔗 
When you first start working with Oracle Cloud Infrastructure, you need to think carefully about how you want to use compartments to organize and isolate your cloud resources. Compartments are fundamental to that process. Most resources can be moved between compartments. However, it's important to think through your compartment design for your organization up front, before implementing anything. For more information, see [Learn Best Practices for Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm). 
The Console is designed to display your resources by _compartment_ within the current region. When you work with your resources in the Console, you must choose which compartment to work in from a list on the page. That list is filtered to show only the compartments in the tenancy that you have permission to access. If you're an administrator, you'll have permission to view all compartments and work with any compartment's resources, but if you're a user with limited access, you probably won't. 
Compartments are tenancy-wide, across regions. When you create a compartment, it is available in every region that your tenancy is subscribed to. You can get a cross-region view of your resources in a specific compartment with the tenancy explorer. See [Viewing All Resources in a Compartment](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm#Viewing_All_Resources_in_a_Compartment).
For added security, you can associate a compartment with a security zone. For more information, see [Security Zones](https://docs.oracle.com/iaas/security-zone/home.htm).
### Creating Compartments 🔗 
When creating a compartment, you must provide a _name_ for it (maximum 100 characters, including letters, numbers, periods, hyphens, and underscores) that is unique within its parent compartment. You must also provide a _description_ , which is a non-unique, changeable description for the compartment, from 1 through 400 characters. Oracle will also assign the compartment a unique ID called an Oracle Cloud ID. For more information, see [Resource Identifiers](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Resource_Identifiers). 
You can create subcompartments in compartments to create hierarchies that are six levels deep. 
[![Figure showing compartment hierarchy six levels deep](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartment_levels.PNG)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartment_levels.PNG)
For information about the number of compartments you can have, see [Service Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase.").
### Access Control for Compartments 🔗 
After creating a compartment, you need to write at least one **policy** for it, otherwise no one can access it (except administrators or users who have permissions set at the tenancy level). When creating a compartment inside another compartment, the compartment inherits access permissions from compartments higher up its hierarchy. For more information, see [Policy Inheritance](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy2).
When you create an access policy, you need to specify which compartment to attach it to. This controls who can later modify or delete the policy. Depending on how you've designed your compartment hierarchy, you might attach it to the tenancy, a parent, or to the specific compartment itself. For more information, see [Policy Attachment](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policies.htm#Policy3). 
### Putting Resources in a Compartment 🔗 
To place a new resource in a compartment, you simply specify that compartment when creating the resource (the compartment is one of the required pieces of information to create a resource). If you're working in the Console, you just make sure you're first viewing the compartment where you want to create the resource. Keep in mind that most IAM resources reside in the tenancy (this includes users, groups, compartments, and any policies attached to the tenancy) and can't be created in or managed from a specific compartment. 
### Moving Resources to a Different Compartment 🔗 
Most resources can be moved after they are created. There are a few resources that you can't move from one compartment to another. Also, you can't move certain resources from a security zone to a compartment that's not in the same security zone, because it might be less secure. For details about restrictions for resources in security zones, see [Restrict Resource Movement](https://docs.oracle.com/iaas/security-zone/using/security-zone-policies.htm).
Some resources have attached resource dependencies and some don't. Not all attached dependencies behave the same way when the parent resource moves.
For some resources, the attached dependencies move with the parent resource to the new compartment. The parent resource moves immediately, but in some cases attached dependencies move asynchronously and are not visible in the new compartment until the move is complete.
For other resources, the attached resource dependencies do not move to the new compartment. You can move these attached resources independently.
After you move the resource to the new compartment, the policies that govern the new compartment apply immediately and affect access to the resource. Depending on the structure of your compartment organization, metering, billing, and alarms can also be affected.
See the service documentation for individual resources to familiarize yourself with the behavior of each resource and its attachments.
### Viewing Resources in a Compartment 🔗 
It's not possible to get a list of all the resources in a compartment by using a single API call. Instead you can list all the resources of a given type in the compartment (e.g., all the instances, all the block storage volumes, etc.). 
**Tip** In the Console, the tenancy explorer allows you to get a list of resources in a compartment, across regions, with some limitations. For more information, see [Viewing All Resources in a Compartment](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm#Viewing_All_Resources_in_a_Compartment).
[Discovering Resources in Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
With [Resource Manager](https://docs.oracle.com/iaas/Content/ResourceManager/home.htm) you can capture deployed resources as Terraform configuration and state files using [resource discovery](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resourcemanager.htm#features__resourcediscovery). The created stack provides you with a Terraform configuration that you can use to programmatically manage, version, and persist your IT infrastructure as "infrastructure as code."
A stack created from a compartment represents all [supported resources](https://docs.oracle.com/iaas/Content/ResourceManager/Concepts/resource-discovery.htm#supported-resources) in the entire compartment, at the appropriate scope. If you select the root compartment for your tenancy, then the scope is the tenancy level, such as users and groups. If you select a non-root compartment, then the scope is compartment level, such as compute instances.
Stack creation is supported from a single compartment only. Stacks can't be created from nested compartments.
For instructions, see [Creating a Stack from an Existing Compartment](https://docs.oracle.com/iaas/Content/ResourceManager/Tasks/create-stack-compartment.htm).
### Deleting Compartments 🔗 
To delete a compartment, it must be empty of all resources. Before you initiate deleting a compartment, be sure that all its resources have been moved, deleted, or terminated, including any policies attached to the compartment. 
The delete action is asynchronous and initiates a work request. The state of the compartment changes to Deleting while the work request is executing. It typically takes several minutes for the work request to complete. While it is in the Deleting state it is not displayed on the compartment picker. If the work request fails, the compartment is not deleted and it returns to the Active state.
After a compartment is deleted, its state is updated to Deleted and a random string of characters is appended to its name, for example, CompartmentA might become CompartmentA.qR5hP2BD. Renaming the compartment allows you to reuse the original name for a different compartment. Oracle displays the deleted compartment on the Compartments page for 90 days.The deleted compartment is removed from the compartment picker. If any policy statements reference the deleted compartment, the name in the policy statement is updated to the new name. 
[Troubleshooting tips for when a compartment fails to delete](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
If the compartment fails to delete, verify that you have removed all the resources: 
  * For most resources, you can use the tenancy explorer to help you locate them. See [Resources Supported by the Tenancy Explorer](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/compartmentexplorer.htm#Resource) for the list of supported resources.
[To view resources in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
Open the **navigation menu** and select **Governance & Administration**. Under **Tenancy Management** , select **Tenancy Explorer**. 
The tenancy explorer opens with a view of the root compartment. Select the compartment you want to explore from the compartment picker on the left side of the Console. After you select a compartment, the resources that you have permission to view are displayed. The **Name** and **Description** of the compartment you are viewing are displayed at the top of the page.To also list all resources in the subcompartments of the selected compartment, select **Show resources in subcompartments**. When viewing resources in all subcompartments, it is helpful to use the **Compartment** column in the results list to see the compartment hierarchy where the resource resides. 
  * Verify that there are no policies in the compartment (polices are not included in Search results).
[To find policies in a compartment ](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**. 
    2. From the compartments list on the left, select the compartment you want to delete.
Policies attached to the compartment are displayed.
  * If you can't locate any resources in the compartment, check with your Administrator; you might not have permission to view all resources.


**Important**
There is a known issue causing deleted compartments to continue to count against your [service limit](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#iamlimits) of compartments. See [Deleted compartments continue to count against service limits](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/known-issues_root.htm#iamdelComp).
### Recovering Compartments 🔗 
To recover a compartment, you must first select it from the list on the Compartment page. You may have to use the state filter to see the deleted compartment. Remember that deleted compartments are renamed by appending a random string of characters to the original compartment name. For example, CompartmentA might become CompartmentA.qR5hP2BD. Oracle displays the deleted compartment on the Compartments page for 90 days.
When you recover a deleted compartment, the name is not changed. For example, if you recover a deleted compartment named CompartmentA.qR5hP2BD, the name remains the same. Because policy statements are updated to use the new names of deleted compartments, any policy statements that had referenced the deleted compartment now reference the recovered compartment. 
### Adding Tag Defaults for a Compartment 🔗 
Tag defaults let you specify tags to be applied automatically to all resources, at the time of creation, in the current compartment. For more information, see [Managing Tag Defaults](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagdefaults.htm).
## Moving a Compartment to a Different Parent Compartment 🔗 
You can move a compartment to a different parent compartment within the same tenancy. When you move a compartment, all its contents (subcompartments and resources) are moved with it. Moving a compartment has implications for the contents. These implications are described in the following sections. Ensure that you are aware of these before you move a compartment.
  * [Required IAM Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm#one)
  * [Restrictions on Moving Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm#Restrict)
  * [Understanding the Policy Implications When You Move a Compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm#Understa)
  * [Understanding Compartment Quota Implications When You Move a Compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm#Understa2)
  * [Understanding Tagging Implications When You Move a Compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm#Understa3)


### Required IAM Policy 🔗 
To move a compartment, you must belong to a group that has `manage all-resources` permissions on the lowest shared parent compartment of the current compartment and the destination compartment.
### Restrictions on Moving Compartments 🔗 
  * You can't move a compartment if the source or destination is part of a [security zone](https://docs.oracle.com/iaas/security-zone/home.htm). You must use the Security Zones console to [manage compartments](https://docs.oracle.com/iaas/security-zone/using/managing-security-zones.htm) within a security zone.
  * You can't move a compartment to a destination compartment with the same name as the compartment being moved. 
For example, assume compartment A and compartment B are both under the root compartment. Under compartment A is a subcompartment, also called compartment B. You cannot move the compartment B to the parent compartment B.
[![Compartment B can't be moved to a parent compartment also named Compartment B](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_samename.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_samename.png)
  * Two compartments within the same parent cannot have the same name. Therefore you can't move a compartment to a destination compartment where a compartment with the same name already exists. 


### Understanding the Policy Implications When You Move a Compartment 🔗 
After you move a compartment to a new parent compartment, the access policies of the new parent take effect and the policies of the previous parent no longer apply. Before you move a compartment, ensure that:
  * You are aware of the policies that govern access to the compartment in its current position.
  * You are aware of the polices in the new parent compartment that will take effect when you move the compartment.


In some cases, when moving nested compartments with policies that specify the hierarchy, the polices are automatically updated to ensure consistency. 
### Policy Examples 🔗 
### Groups with Permissions in the Current Compartment Lose Access; Groups with Permissions in the Destination Compartment Gain Access 🔗 
The following figure shows a compartment hierarchy in which compartment C, a child of A:B is moved to the hierarchy A:D.
[![Compartment C is moved from A:B to A:D](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_policy1.PNG)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_policy1.PNG)
The tenancy has the following policies defined for compartments B and D:
Policy1: `Allow group G1 to manage instance-family in compartment A:B`
Policy2: `Allow group G2 to manage instance-family in compartment A:D`
Impact when compartment C is moved from B to D:
Group G1 can no longer manage instance-families in compartment C.
Group G2 can now manage instance-families in compartment C.
Ensure that you are aware not only of what groups lose permissions when you move a compartment, but also what groups will gain permissions.
### Automatic Update of Policies 🔗 
When you move a compartment, some polices will be automatically updated. Policies that specify the compartment hierarchy down to the compartment being moved will automatically be updated when the policy is attached to a shared ancestor of the current and target parent. Consider the following examples:
**Example 1: Policy automatically updated**
[![Policy is automatically updated when the policy is attached to a shared ancestor](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample1.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample1.png)
In this example, you move compartment A from Operations:Test to Operations:Dev. The policy that governs compartment A is attached to the shared parent, Operations. When the compartment is moved, the policy statement is automatically updated by the IAM service to specify the new compartment location.
The policy
```
Allow group G1 to manage buckets in compartment Test:A 
```

is updated to
```
Allow group G1 to manage buckets in compartment Dev:A
```

No manual intervention is required to allow group G1 to continue to access compartment A in its location.
**Example 2: Policy not updated**
[![Policy is not updated](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample2.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample2.png)
In this example, you move compartment A from Operations:Test to Operations:Dev. However, the policy that governs compartment A here is attached directly to the Test compartment. When the compartment is moved, the policy is not automatically updated. The policy that specifies compartment A is no longer valid and must be manually removed. Group G1 no longer has access to compartment A in its new location under Dev. Unless another existing policy grants access to group G1, you must create a new policy to allow G1 to continue to manage buckets in compartment A.
**Example 3: Policy attached to the tenancy is updated**
[![Policy is automatically updated when the policy is attached to a shared ancestor](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample3.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_polexample3.png)
In this example, you move compartment A from Operations:Test to HR:Prod. The policy that governs compartment A is attached to the tenancy, which is a shared ancestor by the original parent compartment and the new parent compartment. Therefore, when the compartment is moved, the policy statement is automatically updated by the IAM service to specify the new compartment location.
The policy statement:
```
Allow group G1 to manage buckets in compartment Operations:Test:A 
```

is updated to
```
Allow group G1 to manage buckets in compartment HR:Prod:A
```

No manual intervention is required to allow group G1 to continue to access compartment A.
### Understanding Compartment Quota Implications When You Move a Compartment 🔗 
When you move one compartment to another, resource quotas in the destination compartment are not verified and are not enforced. Therefore, if the compartment move results in a quota violation in the destination compartment, the move is not blocked. After the move is complete, the destination compartment will be in an over-quota state. You will not be able to create new resources that are over-quota until you either adjust the quotas for the destination compartment or remove resources to comply with the existing quota. For more information on managing compartment quotas, see [Overview of Compartment Quotas](https://docs.oracle.com/iaas/Content/Quotas/Concepts/resourcequotas.htm).
### Understanding Tagging Implications When You Move a Compartment 🔗 
Tags are not automatically updated after a compartment move. If you have implemented a tagging strategy based on compartment, you must update the tags on the resources after the move. For example, assume CompartmentA has a child compartment, CompartmentB. CompartmentA is set up with tag defaults so that every resource in CompartmentA is tagged with TagA. Therefore CompartmentB and all its resources are tagged with default tag, TagA. When you move CompartmentB to CompartmentC, it will still have the default tags from CompartmentA. If you have set up default tags for CompartmentC, you'll need to add those to the resources in the moved compartment.
[![Tag defaults are not updated after a compartment is moved](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_tag_defaults.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/compartmentmove_tag_defaults.png)
## Using the Console 🔗 
[To create a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**. A list of the compartments you have access to is displayed.
  2. Navigate to the compartment in which you want to create the new compartment:
     * To create the compartment in the tenancy (root compartment) select **Create Compartment**. 
     * Otherwise, select through the hierarchy of compartments until you reach the detail page of the compartment in which you want to create the compartment. On the **Compartment Details** page, select **Create Compartment**.
  3. Enter the following: 
     * **Name:** A unique name for the compartment (maximum 100 characters, including letters, numbers, periods, hyphens, and underscores). The name must be unique across all the compartments in your tenancy. Avoid entering confidential information.
     * **Description:** A friendly description. You can change this later if you want to.
     * **Compartment:** The compartment you are in is displayed. To choose another compartment to create this compartment in, select it from the list.
     * **Tags:** If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  4. Select **Create Compartment**.


Next, you might want to write a policy for the compartment. See [To create a policy](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpolicies.htm#To_create_a_policy).
[To update a compartment's name](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**. 
A list of the compartments in your tenancy is displayed. 
  2. For the compartment you want to rename, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Rename Compartment**.
**Tip** You can't change the name of your root compartment.
  3. Enter the new **Name**. The name must be unique across all the compartments in your tenancy. The name can have a maximum of 100 characters, including letters, numbers, periods, hyphens, and underscores. Avoid entering confidential information.
  4. Select **Rename Compartment**.


[To update a compartment's description](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**. 
A list of the compartments in your tenancy is displayed. 
  2. For the compartment you want to update, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Edit Compartment Description**.
  3. Enter the new description. Avoid entering confidential information.
  4. Select **Save**.


[To view the contents of a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
  1. Open the navigation menu and select the type of resource you want to view. For example, to view Compute resources: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  2. Choose the compartment from the list on the left side of the page. The page updates to show only the resources in that compartment.


Remember that most IAM resources reside in the tenancy (this includes users, groups, and compartments). Policies can reside in either the tenancy (root compartment) or other compartments.
[To move a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
To move a compartment, you must belong to a group that has `manage all-resources` permissions on the lowest shared parent compartment of the current compartment and the destination compartment.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**. 
A list of the compartments in your tenancy is displayed. If the compartment you want to move is not directly beneath the root compartment, select through the hierarchy of compartments to view the wanted compartment. 
  2. For the compartment you want to move, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Move Compartment**.
  3. Select the destination compartment.
  4. Confirm that you are aware of the [implications of the move](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm#Understa).
  5. Select **Move Compartment**.


[To move a resource to a different compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
  1. Open the Console.
  2. Open the navigation menu and select the type of resource you want to work with. For example, to view Compute resources: Open the **navigation menu** and select **Compute**. Under **Compute** , select **Instances**.
  3. In the **List Scope** section, select a compartment. Resources in the selected compartment are displayed. 
  4. Find the resource in the list, select the the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and follow the prompts to move the resource to a new compartment. See the resource documentation for specific steps. 


The resource is moved immediately. If attached resource dependencies move with the parent resource, the resource dependencies are moved asynchronously, and do not appear in the new compartment until the move is complete. 
[To apply tags to a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
For instructions, see [Resource Tags](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/resourcetags.htm#Resource_Tags). 
[To manage tag defaults for a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
See [Managing Tag Defaults](https://docs.oracle.com/iaas/Content/Tagging/Tasks/managingtagdefaults.htm).
[To delete a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
You must remove all resources from a compartment before you can delete it.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**. A list of the compartments in your tenancy is displayed.
  2. For the compartment you want to delete, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Delete Compartment**.
  3. At the prompt, select **OK**.


After you select **OK** , a work request is submitted to delete the compartment. The compartment state changes to Deleting. If the work request fails, the state returns to Active. 
[To recover a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcompartments.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Compartments**. A list of the compartments in your tenancy is displayed.
  2. In **State** , select Deleted. 
  3. For the compartment you want to recover, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)), and then select **Recover**.
  4. At the prompt, select **OK**.


## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage compartments:
  * [CreateCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/CreateCompartment)
  * [ListCompartments](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/ListCompartments)
  * [GetCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/GetCompartment): Returns the metadata for the compartment, not its contents.
  * [UpdateCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/UpdateCompartment)
  * [DeleteCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/DeleteCompartment)
  * [MoveCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/MoveCompartment)
  * [GetWorkRequest](https://docs.oracle.com/iaas/api/#/en/identity/latest/WorkRequest/GetWorkRequest): Gets the work requests spawned by the DeleteCompartment operation. 
  * [RecoverCompartment](https://docs.oracle.com/iaas/api/#/en/identity/latest/Compartment/RecoverCompartment)


You can retrieve the contents of a compartment only by resource type. There's no API call that lists _all_ resources in the compartment. For example, to list all the instances in a compartment, call the Core Services API [ListInstances](https://docs.oracle.com/iaas/api/#/en/iaas/latest/Instance/ListInstances) operation and specify the compartment ID as a query parameter. 
Was this article helpful?
YesNo

