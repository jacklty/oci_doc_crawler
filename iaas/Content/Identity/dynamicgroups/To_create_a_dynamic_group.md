Updated 2025-01-14
# Creating a Dynamic Group
Create a dynamic group in IAM.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the identity domain you want to work in and select **Dynamic Groups**.
  3. Select **Create dynamic group**.
  4. Enter the following information: 
     * **Name:** A unique name for the group. The name must be unique across all groups in your tenancy (dynamic groups and user groups). You can't change the name later. Avoid entering confidential information.
     * **Description:** A friendly description.
  5. Enter the **Matching rules**. Resources that meet the rule criteria are members of the group.
     * **Rule 1:** Enter a rule following the guidelines in [Writing Matching Rules to Define Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/Writing_Matching_Rules_to_Define_Dynamic_Groups.htm#Writing "Matching rules define the resources that belong to a dynamic group."). You can manually enter the rule in the text box or launch the rule builder.
     * Enter additional rules as needed. To add a rule, select **+Additional rule**.
  6. To assign tags to the group, select **Show advanced options** and enter the tagging details.
If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later. You can apply tabs later.
  7. Select **Create**. 
The matching rule syntax is verified, but the OCIDs are not. Be sure that the OCIDs you enter are correct.


To give the dynamic group permissions, you need to write a policy. See [Writing Policies for Dynamic Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/callresources/Writing_Policies_for_Dynamic_Groups.htm#Writing "After you create a dynamic group, you need to create policies to permit the dynamic groups to access Oracle Cloud Infrastructure services.").
Was this article helpful?
YesNo

