Updated 2025-01-14
# Creating an Identity Provider Policy
Create an identity provider policy for an identity domain.
You can define the following criteria in an IdP policy:
  * The username of the user
  * The IP address that the user is using to sign in to the identity domain
  * The IdPs that will be available to the user to access the identity domain


  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Under **Security** click **IdP policies**.
  3. On the **Identity provider (IdP) policies** page, select **Create IdP policy**.
  4. On the **Add policy** page, enter a name and then select **Add policy**.
The policy is added.
  5. On the **Add identity provider rules** page, select **Add IdP rule** to define rules for this policy.
  6. Enter a **Rule name** for the identity provider rule.
  7. Use the **Assign identity providers** menu to select the IdPs to assign to this rule.
  8. Configure the following **Conditions** :
     * **Expression placement** : The following options are associated with this field:
       * If you select **Starts with expression** , then the rule evaluates the start of the username in the user account.
       * If you select **Ends with expression** , then the rule evaluates the end of the username in the user account.
     * **Enter user name expression** : Specify information about users' usernames to evaluate whether they meet the criteria of the rule. For example, if you want the rule to be applicable only to those users who have usernames that end with **@example.com** , then select **Ends with expression** from the preceding menu, and then enter `@example.com` in this text box.
     * **Exclude users** : Optionally, enter or select the users to exclude from the rule.
     * **Group membership** : Optionally, enter or select the groups to exclude from the rule.
     * **Filter by client IP address** : The following options are associated with this field:
       * If you select **Anywhere** , then the IdPs that you specify in this rule will be available to users that sign in from any IP address.
       *  If you select **Restrict to the following network perimeters** , then you enter or select network perimeters that you have defined. For more information, see [Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter.htm#add-network-perimeter "Create a network perimeter in an identity domain in IAM and configure it to restrict the IP addresses that users can use to sign in."). The IdPs that you specify in this rule will be available to users that sign in using only IP addresses that are contained in the defined network perimeters.
  9. Select **Add IdP rule**.
  10. To add another identity provider rule to this policy, repeat the preceding steps.
**Note:** If you have added multiple identity provider rules to this policy, you can change the order in which they are evaluated. Select **Edit priority** and then change the priority order.
  11. When you are finished adding rules, select **Next**.
  12. Add apps to the policy. For more information see [Adding Apps to the Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/add-apps-idp-policy.htm#assign-apps-idp-policy "You can assign apps to an identity provider policy. When a user attempts to authenticate through the apps, the only identity providers in the Sign In page are the ones you assigned to the policy. \(You can assign only one identity provider policy to an app. If the app isn't assigned to any identity provider policy explicitly, then the default identity provider policy applies to the app.\)").
  13. When you are done, select **Close**.


Was this article helpful?
YesNo

