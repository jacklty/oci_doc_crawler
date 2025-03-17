Updated 2025-01-14
# Updating a Policy's Statements
Update the statements in an IAM policy.
**Note**
If you use the name of a group, dynamic group, or compartment in a policy, the policy is mapped to the OCID of the group, dynamic group, or compartment when the policy is created. If the OCID of the group, dynamic group, or compartment changes, you must recompile one of the policies that applies to the group or compartment to update the OCID in all the policies. 
To recompile the policy, open a policy, and make a small edit. Save the policy.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
A list of the policies in the compartment you're viewing is displayed. If you don't see the one you're looking for, verify that you're viewing the correct compartment (select from the list on the left side of the page).
  2. Select the name of the policy to show its details.
  3. Under **Statements** , select **Edit Policy Statements**.
  4. Use the **Basic** policy builder option if you want to interact with the statements using graphical controls. Use the **Advanced** policy builder option to edit the statements in a simple text box.
**Basic** option:
     * To revise a statement, enter the changes by using the format in [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
     * To add a statement, select **+ Another Statement** and enter the statement by using the required format.
     * To delete a statement, select the X next to the statement.
     * To rearrange the order of the statements, use the up and down arrows to move statements to the correct order, or grab the handle to drag statements.
**Advanced** option:
     * Select **Advanced**.
     * Revise the policy statements in the text box by using the format in [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
  5. Select **Save Changes**. 
Your changes go into effect typically within 10 seconds.


Was this article helpful?
YesNo

