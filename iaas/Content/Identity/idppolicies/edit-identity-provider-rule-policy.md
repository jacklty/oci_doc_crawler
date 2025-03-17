Updated 2025-01-14
# Updating an Identity Provider Rule for the Policy
Update configuration settings for an identity provider rule of an identity provider policy.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Under **Security** click **IdP policies**.
  3. In the **Identity provider (IdP) policies** page, select **Identity provider rules**.
  4. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the identity provider rule that you want to edit.
  5. Select **Edit IdP rule**. A window that displays configuration settings for the identity provider rule opens.
  6. Enter a **Rule name** for the identity provider rule.
  7. Use the **Assign identity providers** menu to select the identity providers to assign to this rule.
  8. Use the following table to configure rule **Conditions** :
     * **Expression placement** : There are two options associated with this field: **Starts with expression** and **Ends with expression**. If you select **Starts with expression** , then the rule evaluates the start of the username in the user account. If you select **Ends with expression** , then the rule evaluates the end of the username in the user account.
     * **Enter user name expression** : Specify information about users' usernames to evaluate to determine whether they meet the criteria of the rule. For example, if you want the rule to be applicable only to those users that have usernames that end with `@example.com`, then select **Ends with expression** from the drop-down menu, and enter `@example.com` in the **Enter user name expression** text box.
     * (Optional) **Exclude users** : Enter or select the users to exclude from the rule.
     * (Optional) **Group membership** : Enter or select the groups to exclude from the rule.
     * **Filter by client IP address** : There are two options associated with this field: **Anywhere** and **Restrict to the following network perimeters**. If you select **Anywhere** , then the identity providers that you specify in this rule will be available to users that sign in from any IP address. If you select **Restrict to the following network perimeters** , then a text box appears. In this text box, enter or select network perimeters that you defined. For more information, see [Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter.htm#add-network-perimeter "Create a network perimeter in an identity domain in IAM and configure it to restrict the IP addresses that users can use to sign in."). The identity providers that you specify in this rule will be available to users that sign in using only IP addresses that are contained in the defined network perimeters.
  9. When you're finished, select **Save changes**.


Was this article helpful?
YesNo

