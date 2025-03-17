Updated 2025-01-14
# Managing Dynamic Groups
This topic describes how to manage dynamic groups and define the rules to determine a dynamic group's members.
## About Dynamic Groups 🔗 
Dynamic groups allow you to group Oracle Cloud Infrastructure compute instances as "principal" actors (similar to user groups). You can then create policies to permit instances to [make API calls against Oracle Cloud Infrastructure services](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#Calling_Services_from_an_Instance). When you create a dynamic group, rather than adding members explicitly to the group, you instead define a set of _matching rules_ to define the group members. For example, a rule could specify that all instances in a particular compartment are members of the dynamic group. The members can change dynamically as instances are launched and terminated in that compartment.
## Required IAM Policy 🔗 
If you're in the Administrators group, then you have the required access for managing dynamic groups. 
If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top). If you want to dig deeper into writing policies for dynamic groups or other IAM components, see [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top).
## Tagging Resources 🔗 
Apply tags to resources to help organize them according to business needs. Apply tags at the time you create a resource, or update the resource later with the wanted tags. For general information about applying tags, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
## Working with Dynamic Groups 🔗 
When creating a dynamic group, you must provide a unique, unchangeable _name_ for the dynamic group. The name must be unique across all groups within your tenancy. You must also provide the dynamic group with a _description_ (although it can be an empty string), which is a non-unique, changeable description for the group. Oracle will also assign the group a unique ID called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Resource_Identifiers). 
**Note**
If you delete a dynamic group and then create a new dynamic group with the same name, they'll be considered different groups because they'll have different OCIDs. 
A dynamic group has no permissions until you write at least one **policy** that gives that dynamic group permission to either the tenancy or a compartment. When writing the policy, you can specify the dynamic group by using either the unique name or the dynamic group's OCID. Per the preceding note, even if you specify the dynamic group name in the policy, IAM internally uses the OCID to determine the dynamic group. For information about writing policies, see [Managing Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingpolicies.htm#Managing_Policies). 
You can delete a dynamic group, but only if the group is empty.
## Updating Dynamic Groups 🔗 
You can update the matching rules that define the members of a dynamic group. For example, you might change a matching rule that includes all instances in a compartment to exclude a particular instance. Or, you might update a rule to include a new tag value.
**Important** When you make a change to a matching rule you must allow about one hour for the updated policy to take effect. For example, if you update tags on an instance to either include or exclude that instance from a dynamic group, you must wait for that policy to take effect to include or exclude the instance.
## Limits on Dynamic Groups 🔗 
A single compute instance can belong to a maximum of 5 dynamic groups. 
You can have a maximum of 50 dynamic groups in your tenancy.
## Using the Console 🔗 
[To create a dynamic group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Under **Identity domain** , select **Dynamic groups**.
  2. Select **Create Dynamic Group**. 
  3. Enter the following: 
     * **Name:** A unique name for the group. The name must be unique across all groups in your tenancy (dynamic groups and user groups). You can't change this later. Avoid entering confidential information.
     * **Description:** A friendly description.
  4. Enter the **Matching Rules**. Resources that meet the rule criteria are members of the group.
     * **Rule 1:** Enter a rule following the guidelines in [Writing Matching Rules to Define Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Writing). You can manually enter the rule in the text box or launch the rule builder.
     * Enter additional rules as needed. To add a rule, select **+Additional Rule**.
  5. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. 
  6. Select **Create Dynamic Group**.
The matching rule syntax is verified, but the OCIDs are not. Be sure that the OCIDs you enter are correct.


Next, to give the dynamic group permissions, you need to write a policy. See [Writing Policies for Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/callingservicesfrominstances.htm#Writing).
[To delete a dynamic group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Under **Identity domain** , select **Dynamic groups**. A list of the dynamic groups in your tenancy is displayed.
  2. Locate the dynamic group in the list. 
  3. For the dynamic group you want to delete, select **Delete**.
  4. Confirm when prompted.


[To update a dynamic group's description](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Under **Identity domain** , select **Dynamic groups**. A list of the groups in your tenancy is displayed.
  2. Select the dynamic group you want to update. The dynamic's group's details are displayed. 
  3. Select **Edit Dynamic Group**.
  4. Edit the description. When finished, select **Save Changes**. 


[To update a dynamic group's matching rules](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. Under **Identity domain** , select **Dynamic groups**. A list of the dynamic groups in your tenancy is displayed.
  2. Select the dynamic group you want to update. The dynamic group's details are displayed. 
  3. Select **Edit All Matching Rules**.
  4. Edit the matching rule in the text box; or, you can use the rule builder if the change is [supported by the rule builder](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Limitati). 


## Writing Matching Rules to Define Dynamic Groups 🔗 
Matching rules define the resources that belong to the dynamic group. In the Console, you can either enter the rule manually in the provided text box, or you can use the [rule builder](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Using2). The rule builder lets you make selections and entries in a dialog, then writes the rule for you, based on your entries. 
You can define the members of the dynamic group based on the following:
  * compartment ID - include (or exclude) the instances that reside in that compartment based on compartment OCID
  * instance ID - include (or exclude) an instance based on its instance OCID
  * tag namespace and tag key - include (or exclude) instances tagged with a specific tag namespace and tag key. All tag values are included. For example, include all instances tagged the with tag namespace `department` and the tag key `operations`. 
  * tag namespace, tag key, and tag value - include (or exclude) instances tagged with a specific value for the tag namespace and tag key. For example include all instances tagged with the tag namespace `department` and the tag key `operations` and with the value '`45`'.
  * resource.compartment.id - the OCID of the compartment where the resource resides
  * resource.id - the OCID of the resource
  * resource.type - the type of the resource


A matching rule has the following syntax:
For a single condition:
```
variable =|!= 'value'
```

For multiple conditions:
```
any|all {<condition>,<condition>,...}
```

Supported variables are:
  * `instance.compartment.id` - the OCID of the compartment where the instance resides 
  * `instance.id` - the OCID of the instance 
  * `tag.<tagnamespace>.<tagkey>.value` - the tag namespace and tag key. For example, `tag.department.operations.value`. 
  * `tag.<tagnamespace>.<tagkey>.value='<tagvalue>'` - the tag namespace, tag key, and tag value. For example, `tag.department.operations.value='45'`


Here are some examples:
[Include All Instances in a Specific Compartment in the Dynamic Group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
To include all instances that are in a specific compartment, add a rule with the following syntax:
```
instance.compartment.id = '<compartment_ocid>'
```

You can type the rule directly in the text box, or you can use the [rule builder](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Using2).
Example entry in text box:
```
instance.compartment.id = 'ocid1:compartment:oc1:phx:samplecompartmentocid6q6igvfauxmima74jv'
```

To add the same rule using the Console rule builder:
  * For **Include Instances That Match:** Select **All of the following**.
  * For **Match Instances with:** Select **Compartment OCID**.
  * For **Value:** Enter the compartment OCID. For this example, you would enter `ocid1:compartment:oc1:phx:samplecompartmentocid6q6igvfauxmima74jv`


All instances that currently exist or get created in the compartment (identified by the OCID) are members of this group.
[Include All Instances in Any of Two or More Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
To include all instances that reside in any of two (or more) compartments, add a rule with the following syntax:
```
Any {instance.compartment.id = '<compartment_ocid>', instance.compartment.id = '<compartment_ocid>'}
```

separating each compartment entry with a comma.
You can type the rule directly in the text box, or you can use the [rule builder](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm#Using2).
Example entry in the text box:
```
Any {instance.compartment.id = 'ocid1:compartment:oc1:phx:samplecompartmentocid6q6igvfauxmima74jv', instance.compartment.id = 'ocid1:compartment:oc1:phx:samplecompartmentocidythksk89ekslsoelu2'}
```

To add the same rule using the Console rule builder:
  1. For **Include Instances That Match:** Select **Any of the following**.
  2. For **Match Instances With:** Select **Compartment OCID**.
  3. For **Value:** Enter the compartment OCID. For this example, you would enter `ocid1:compartment:oc1:phx:samplecompartmentocid6q6igvfauxmima74jv`
  4. Select **+Additional Line**. Enter the following on the second line:
     * For **Match Instances With:** Select **Compartment OCID**.
     * For **Value:** Enter the additional compartment OCID. For this example, you would enter `ocid1:compartment:oc1:phx:samplecompartmentocidythksk89ekslsoelu2`


Instances that currently exist or are later created in either of the specified compartments are members of this group.
[Include All Instances Tagged with a Specific Namespace and Tag Key](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
To include all instances that are tagged with a specific tag namespace and tag key, add a rule with the following syntax:
```
tag.<tagnamespace>.<tagkey>.value
```

All instances assigned the tagnamespace.tagkey combination are included. Note that the tag value is not evaluated, so all values are included.
**Example:** Assume you have a tag namespace called `department` and a tag key called `operations`. You want to include all instances that are tagged with the namespace and tag key.
Enter the following rule in the text box:
```
tag.department.operations.value
```

All instances that currently exist or get created with the tag namespace and tag key `department.operations` are members of this group.
[Include All Instances In a Specific Compartment with a Specific Tag Namespace, Tag Key, and Tag Value](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
To include all instances in a specific compartment that are tagged with a specific tag namespace, key, and value, add a rule with the following syntax:
`All {instance.compartment.id = '<compartment_ocid>', tag.<tagnamespace>.<tagkey>.value='<tagvalue>'}`
All instances that are in the identified compartment and that are assigned the tagnamespace.tagkey with the specified tag value are included. 
**Example:** Assume you have a tag namespace called `department` and a tag key called `operations`. You want to include all instances that are tagged with the value 45, that are in a particular compartment.
Enter the following statement in the text box:
```
All {instance.compartment.id='ocid1:compartment:oc1:phx:oc1:phx:samplecompartmentocid6q6igvfauxmima74jv,',
tag.department.operations.value='45'}
```

### Using the Rule Builder 🔗 
The rule builder is a tool available from the Console to help you write matching rules. The rule builder provides menus and text boxes for you to make entries and then writes the rule for you. The rule builder does have some limitations, so you can't use it for all cases.
#### Limitations of the Rule Builder 🔗 
The rule builder does not support the following:
  * Exclusion rules - the rule builder lets you select compartment IDs and instance IDs to include only. 
  * Rules based on tags - the rule builder does not allow you to select tags to include in your rule. To add a rule based on tag values, you need to enter the rule in the Rule text box using the syntax above. 


#### Launching the Rule Builder 🔗 
When you select **Create Dynamic Group** , the Rule Builder is displayed in the **Create Dynamic Group** dialog.
To create a matching rule using the rule builder
  1. Under the **Matching Rules** section, select **Rule Builder**.
  2. From the **Include Instances That Match** menu, select **All of the following** or **Any of the following**.
**All of the following** includes only instances that match all of the statements in the rule.
**Any of the following** includes instances that match any of the statements in the rule.
**Note** You can select the following instance and compartment variables:
     * instance.compartment.id and instance.id are applicable when matching instances
     * resource.compartment.id, resource.id and resource.type are applicable when matching resources
     * tag.* variables apply to both instances and resources
  3. Select a resource type from the **Match Instances With** menu, and then enter the OCID for the resource in the **Value** field:
**Compartment OCID** includes instances in the compartment you specify.
**Instance OCID** includes the instances with the OCIDs you specify.
  4. Select **+Additional line** to add more statements to this rule.
When you add multiple statements to a rule, remember that **Any of the following** includes instances that match any of the statements. If you choose **All of the following** , instances must match all of the specifications in the statements to be included in the group.


#### Examples Using the Rule Builder 🔗 
[Include All Instances in a Specific Compartment in the Dynamic Group](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
To include all instances that are in a specific compartment, using the rule builder: 
  * Select **All of the following**.
  * For **Match Instances With:** Select **Compartment OCID**.
  * For **Value:** Enter the compartment OCID, for example, `ocid1:compartment:oc1:phx:samplecompartmentocidythksk89ekslsoelu2`


All instances that currently exist or are later created in the compartment (identified by the OCID) are members of this group.
[Include All Instances in Any of Two or More Compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingdynamicgroups.htm)
To include all instances that reside in any of two (or more) compartments using the rule builder:
  1. From the **Include Instances That Match** menu, select **Any of the following**.
  2. In the first line, enter:
     * For **Match Instances With** , select **Compartment OCID**.
     * For **Value** , enter the compartment OCID, for example: `ocid1:compartment:oc1:phx:samplecompartmentocid6q6igvfauxmima74jv`
  3. Select **+Additional Line**. Enter the following on the second line:
     * For **Match Instances With** , select **Compartment OCID**
     * For **Value** , enter the compartment OCID, for example: `ocid1:compartment:oc1:phx:samplecompartmentocidythksk89ekslsoelu2`
  4. Continue adding additional lines as needed for each compartment you want to include.


Instances that currently exist or get created in any of the specified compartments are members of this group.
## Using the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations to manage dynamic groups:
  * [CreateDynamicGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/CreateDynamicGroup)
  * [ListDynamicGroups](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/ListDynamicGroups)
  * [GetDynamicGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/GetDynamicGroup)
  * [UpdateDynamicGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/UpdateDynamicGroup)
  * [DeleteDynamicGroup](https://docs.oracle.com/iaas/api/#/en/identity/latest/DynamicGroup/DeleteDynamicGroup)


Was this article helpful?
YesNo

