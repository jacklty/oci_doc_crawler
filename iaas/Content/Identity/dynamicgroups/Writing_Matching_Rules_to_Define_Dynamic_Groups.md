Updated 2025-01-23
# Writing Matching Rules to Define Dynamic Groups
Matching rules define the resources that belong to a dynamic group.
In the Console, you can either enter the rule manually in the provided text box, or you can use the [rule builder](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Using_the_Rule_Builder.htm#using-rule-builder "The rule builder is a tool available from the Console to help you write matching rules."). The rule builder lets you make selections and entries in a dialog, then writes the rule for you, based on your entries. The rule builder supports the instance and compartment variables. To write a rule based on other variables, enter it manually.
You can define the members of the dynamic group based on the following:
  * compartment OCID 
  * instance OCID (for instances) or resource OCID (for other resources)
  * resource type 
  * tag namespace and tag key - include (or exclude) instances tagged with a specific tag namespace and tag key. All tag values are included. For example, include all instances tagged the with tag namespace `department` and the tag key `operations`. 
  * tag namespace, tag key, and tag value - include (or exclude) instances tagged with a specific value for the tag namespace and tag key. For example include all instances tagged with the tag namespace `department` and the tag key `operations` and with the value '`45`'.


A matching rule has the following syntax:
For a single condition:
```
variable {{=}} | !='value'
```

For several conditions:
```
any|all {<condition>,<condition>,...}
```

Supported variables are:
For instances, you can use:
  * `instance.compartment.id` - the OCID of the compartment where the instance resides 
  * `instance.id` - the OCID of the instance 


For all supported resource types, you can use:
  * `resource.id` - the OCID of the resource 
  * `resource.compartment.id` - the OCID of the compartment where the resource resides
  * `resource.type` - the type of resource. The resource type is shown in the resource's OCID. For example:
    * a domain's OCID has the format `ocid1.domain...`, so specify `domain` as the `resource.type`.
    * a function's OCID has the format `ocid1.fnfunction...`, so specify `fnfunction` as the `resource.type`
    * an API gateway's OCID has the format `ocid1.apigateway...` , so specify `apigateway` as the `resource.type`
  * `tag.<tagnamespace>.<tagkey>.value` - the tag namespace and tag key. For example, `tag.department.operations.value`. 
  * `tag.<tagnamespace>.<tagkey>.value           = '<tagvalue>'` - the tag namespace, tag key, and tag value. For example, `tag.department.operations.value =           '45'`


**Note** IAM policies don't support free-form tags. See [Understanding Free-form Tags](https://docs.oracle.com/iaas/Content/Tagging/Concepts/understandingfreeformtags.htm).
**Examples:**
[Include all instances in a compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm)
To include all instances that are in a specific compartment, add a rule with the following syntax:
```
instance.compartment.id = '<compartment_ocid>'
```

You can type the rule directly in the text box, or you can use the [rule builder](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Using_the_Rule_Builder.htm#using-rule-builder "The rule builder is a tool available from the Console to help you write matching rules.").
Example entry in text box:
```
instance.compartment.id = 'ocid1.compartment.oc1.phx.samplecompartmentocid6q6igvfauxmima74jv'
```

To add the same rule using the Console rule builder:
  * For **Include instances that match:** Select **All of the following**.
  * For **Match instances with:** Select **Compartment OCID**.
  * For **Value:** Enter the compartment OCID. For this example, you would enter `ocid1.compartment.oc1.phx.samplecompartmentocid6q6igvfauxmima74jv`


All instances that currently exist or get created in the compartment (identified by the OCID) are members of this group.
[Include all instances in any of two or more compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm)
To include all instances that reside in any of two (or more) compartments, add a rule with the following syntax:
```
Any {instance.compartment.id = '<compartment_ocid>', instance.compartment.id = '<compartment_ocid>'}
```

separating each compartment entry with a comma.
You can type the rule directly in the text box, or you can use the [rule builder](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Using_the_Rule_Builder.htm#using-rule-builder "The rule builder is a tool available from the Console to help you write matching rules.").
Example entry in the text box:
```
Any {instance.compartment.id = 'ocid1.compartment.oc1.phx:samplecompartmentocid6q6igvfauxmima74jv', instance.compartment.id = 'ocid1.compartment.oc1.phx.samplecompartmentocidythksk89ekslsoelu2'}
```

To add the same rule using the Console rule builder:
  1. For **Include instances that match:** Select **Any of the following**.
  2. For **Match instances with:** Select **Compartment OCID**.
  3. For **Value:** Enter the compartment OCID. For this example, you would enter `ocid1.compartment.oc1.phx.samplecompartmentocid6q6igvfauxmima74jv`
  4. Select **+ Additional line**. Enter the following on the second line:
     * For **Match instances with:** Select **Compartment OCID**.
     * For **Value:** Enter the additional compartment OCID. For this example, you would enter `ocid1.compartment.oc1.phx.samplecompartmentocidythksk89ekslsoelu2`


Instances that currently exist or are later created in either of the specified compartments are members of this group.
[Include a specific resource in a specific compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm)
To include a specific resource that's in a specific compartment, add a rule with the following syntax:
```
All {resource.id = '<resource_ocid>', resource.compartment.id = <compartment_ocid>}
```

Type the rule directly in the text box.
For example, to include a specific API gateway in a specific compartment, enter a statement like the following:
```
All {resource.id = 'ocid1.apigateway.oc1.phx.amaaaaaexampleuniqueid', resource.compartment.id = 'ocid1.compartment.oc1.phx.samplecompartmentocid'}
```

The API gateway with the specified OCID in the specified compartment belongs to this dynamic group.
[Include all occurrences of a resource type in a specific compartment](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm)
To include all occurrences of a specific resource type in a specific compartment, add a rule with the following syntax:
```
All {resource.type = '<resource_type', resource.compartment.id = <compartment_ocid>}
```

Type the rule directly in the text box.
For example, to include all vaults in a specific compartment, enter a statement like the following:
```
All {resource.type = 'vaults', resource.compartment.id = 'ocid1.compartment.oc1.phx.samplecompartmentocid'}
```

All vaults in the specified compartment will be members of this dynamic group.
[Include all instances tagged with a specific namespace and tag key](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm)
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
[Include all instances in a specific compartment with a specific tag namespace, tag key, and tag value](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm)
To include all instances in a specific compartment that are tagged with a specific tag namespace, key, and value, add a rule with the following syntax:
`All {instance.compartment.id =         '<compartment_ocid>',           tag.<tagnamespace>.<tagkey>.value         = '<tagvalue>'}`
All instances that are in the identified compartment and that are assigned the tagnamespace.tagkey with the specified tag value are included. 
**Example:** Assume you have a tag namespace called `department` and a tag key called `operations`. You want to include all instances that are tagged with the value 45, that are in a particular compartment.
Enter the following statement in the text box:
```
All {instance.compartment.id = 'ocid1.compartment.oc1.phx.oc1.phx.samplecompartmentocid6q6igvfauxmima74jv,',
tag.department.operations.value = '45'}
```

Was this article helpful?
YesNo

