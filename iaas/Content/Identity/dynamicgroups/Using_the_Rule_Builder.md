Updated 2025-01-14
# Using the Rule Builder
The rule builder is a tool available from the Console to help you write matching rules.
The rule builder provides menus and text boxes for you to make entries and then writes the rule for you. The rule builder does have some limitations, so you can't use it for all cases.
[Limitations of the Rule Builder](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Using_the_Rule_Builder.htm)
The rule builder does not support the following:
  * Exclusion rules - the rule builder lets you select compartment IDs and instance IDs to include only.
  * Rules based on tags - the rule builder does not allow you to select tags to include in your rule. To add a rule based on tag values, you need to enter the rule in the Rule text box using the syntax [examples](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm#Writing "Matching rules define the resources that belong to a dynamic group."). 
  * Rules using the `resource.type`, `resource.id`, or `resource.compartment.id` variables.


[Launching the Rule Builder](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Using_the_Rule_Builder.htm)
When you select **Create dynamic group** , the Rule Builder is part of the **Create dynamic group** dialog.
To create a matching rule using the rule builder:
  1. Under the **Matching rules** section, select **Rule builder**.
  2. From the **Include instances that match** menu, select **All of the following** or **Any of the following**.
**All of the following** includes only instances that match all of the statements in the rule.
**Any of the following** includes instances that match any of the statements in the rule.
  3. Select a resource type from the **Match instances with** menu, and then enter the OCID for the resource in the **Value** field:
**Compartment OCID** includes instances in the compartment you specify.
**Instance OCID** includes the instances with the OCIDs you specify.
  4. Select **+ Additional line** to add more statements to this rule.
When you add multiple statements to a rule, remember that **Any of the following** includes instances that match any of the statements. If you choose **All of the following** , instances must match all of the specifications in the statements to be included in the group.


[Examples Using the Rule Builder](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Using_the_Rule_Builder.htm)
[Include all instances in a specific compartment in the dynamic group](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Using_the_Rule_Builder.htm)
To include all instances that are in a specific compartment, using the rule builder: 
  * Select **All of the following**.
  * For **Match instances with:** Select **Compartment OCID**.
  * For **Value:** Enter the compartment OCID, for example, `ocid1.compartment.oc1.phx.samplecompartmentocidythksk89ekslsoelu2`


All instances that currently exist or are later created in the compartment (identified by the OCID) are members of this group.
[Include all instances in any of two or more compartments](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Using_the_Rule_Builder.htm)
To include all instances that reside in any of two (or more) compartments using the rule builder:
  1. From the **Include instances that match** menu, select **Any of the following**.
  2. In the first line, enter:
     * For **Match instances with** , select **Compartment OCID**.
     * For **Value** , enter the compartment OCID, for example: `ocid1.compartment.oc1.phx.samplecompartmentocid6q6igvfauxmima74jv`
  3. Select **+ Additional line**. Enter the following on the second line:
     * For **Match instances with** , select **Compartment OCID**
     * For **Value** , enter the compartment OCID, for example: `ocid1.compartment.oc1.phx.samplecompartmentocidythksk89ekslsoelu2`
  4. Continue adding additional lines as needed for each compartment you want to include.


Instances that currently exist or get created in any of the specified compartments are members of this group.
Was this article helpful?
YesNo

