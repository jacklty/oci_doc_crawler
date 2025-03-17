Updated 2025-01-13
# Listing Policies
List the policies in an IAM compartment.
**Note**
If you use the name of a group, dynamic group, or compartment in a policy, the policy is mapped to the OCID of the group, dynamic group, or compartment when the policy is created. If the OCID of the group, dynamic group, or compartment changes, you must recompile one of the policies that applies to the group or compartment to update the OCID in all the policies. 
To recompile the policy, open a policy, and make a small edit. Save the policy.
Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Policies**.
A list of the policies in the compartment you're currently viewing is displayed. 
To view policies attached to a different compartment, select that compartment from the list on the left. You can't get a single list of all policies; they're always displayed by compartment.
To decide which policies apply to a particular group, you must view the individual statements inside all your policies. There isn't a way to automatically obtain that information in the Console.
Was this article helpful?
YesNo

