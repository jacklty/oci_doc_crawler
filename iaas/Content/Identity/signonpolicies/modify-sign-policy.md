Updated 2025-01-14
# Updating a Sign-On Policy
Update a sign-on policy in an identity domain in IAM.
You can make the following changes to a sign-on policy:
  * Edit the name or description of the policy
  * Add, remove, edit, or change the priority of sign-on rules for the policy
  * Add or remove apps for the policy


**Note** Policy changes might require a few minutes to propagate to other regions.
To change a sign-on policy, follow these steps:
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Security** , and then select **Sign-in policies**.
  4. In the **Sign-on policies** page, select the sign-on policy that you want to change.
  5. To edit the policy name or description, select **Edit sign-on policy** and then make and save the changes.
  6. To add, remove, edit, or change the priority of sign-on rules for the policy, under **Resources** , select **Sign-on rules**.
     * To add a rule to the policy, select **Add sign-on rule** and provide the required values. For a description of the fields, see [Adding a Rule to a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/add-more-rules-policy.htm#add-sign-rules-policy "Add a rule to an identity domain sign-on policy in IAM.").
     * To edit a rule, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the rule and select Edit sign-on rule. Make your edits. For a description of the fields, see [Adding a Rule to a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/add-more-rules-policy.htm#add-sign-rules-policy "Add a rule to an identity domain sign-on policy in IAM.").
     * To remove a rule, select the checkbox for the rule in the table, select **Remove sign-on rule** , and then confirm the deletion.
     * To change the priority of the rules, select **Edit priority** and then select the up or down arrow next to the rule to move it to the position in the listed order that you want the rule applied.
For example, if the sign-on rule is listed fourth, and you want the identity domain to evaluate it first, select the up arrow next to the rule until it's at the top of the list. That sign-on rule now has a priority of 1, and the rule that was listed first now has a priority of 2.
  7. To add or remove apps for the policy, under **Resources** , select **Apps**.
     * To add an app, select **Add app** , select the checkbox for each app that you want to add to the policy, and then select **Add app**.
     * To remove an app, select the checkbox for the app in the table, select **Remove app** , and then confirm the removal.


Was this article helpful?
YesNo

