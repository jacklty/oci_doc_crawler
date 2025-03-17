Updated 2025-01-14
# Adding Identity Provider Rules to a Policy 
You can add identity provider rules to an identity provider policy in an identity domain.
By adding identity provider policy rules, you can prevent some of your identity providers from being available to users to authenticate into the identity domain. Or you can allow other identity providers to be available only to those users who access the identity domain from an IP address contained in one of your network perimeters.
  1. Select **Identity provider rules**.
  2. Select **Add IdP rule**.
  3. Enter a **Rule name** for the identity provider rule.
  4. Use the **Assign identity providers** menu to select the identity providers to assign to this rule.
  5. Under **Conditions** , provide the following values:
     * **Expression placement** : Select one of the following values:
       * **Starts with expression** : This rule evaluates the start of the username in the user account.
       * **Ends with expression** : The rule evaluates the end of the username in the user account.
     * **Enter user name expression** : Specify information about users' usernames to evaluate to determine whether they meet the criteria of the rule. For example, if you want the rule to be applicable only to those users that have usernames that end with `@example.com`, then select **Ends with expression** from the drop-down menu, and enter `@example.com` in the **Enter user name expression** text box.
     * **Exclude users** : Optionally, enter or select the users to exclude from the rule.
     * **Group membership** : The identity providers that you specify in this rule will be available to all users that are members of the group.
     * **Filter by client IP address** : Select one of the following options:
       * **Anywhere** : The identity providers that you specify in this rule will be available to users that sign in from any IP address.
       * **Restrict to the following network perimeters** : A text box appears. In this text box, enter or select network perimeters that you defined. For more information, see [Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter.htm#add-network-perimeter "Create a network perimeter in an identity domain in IAM and configure it to restrict the IP addresses that users can use to sign in."). The identity providers that you specify in this rule will be available to users that sign in using only IP addresses that are contained in the defined network perimeters.


Was this article helpful?
YesNo

