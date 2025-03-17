Updated 2025-01-14
# Adding a Rule to a Sign-On Policy
Add a rule to an identity domain sign-on policy in IAM.
  1. On the sign-on policy details page, select **Add sign-on rule**.
  2. Use the following table to configure the rule:
     * **Rule name** : Enter the name of the sign-on rule.
     * **Authenticating identity provider** (Optional): Enter or select all identity providers used to authenticate the user accounts evaluated by this rule. If you leave this empty, the other conditions are used for authentication.
     * **Group membership** : Enter or select the groups that the user must be a member of to meet the criteria of this rule. You must enter at least three characters to begin a search of groups.
     * **Administrator** : If the user must be assigned to administrator roles in the identity domain to meet the criteria of this rule, then select this checkbox.
     * **Exclude users** : Enter or select the users to exclude from the rule. You must enter at least three characters to begin a search of users.
     * **Filter by client IP address** : There are two options associated with this field: **Anywhere** and **Restrict to the following network perimeters**.
       * If you select **Anywhere** , then users can sign in to the identity domain using any IP address.
       * If you select **Restrict to the following network perimeters** , then the **Network perimeters** text box appears. In this text box, enter or select network perimeters that you defined. For more information, see [Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter.htm#add-network-perimeter "Create a network perimeter in an identity domain in IAM and configure it to restrict the IP addresses that users can use to sign in."). Users can sign in to the identity domain using only IP addresses that are contained in the defined network perimeters.
     * **Allow access** or **Deny access** : Select whether a user can access the Console if the user account meets the criteria of this rule. When you select **Allow access** , the more options are presented.
     * **Prompt for reauthentication** : Select this check box to force the user to sign in to the identity domain again. If not selected, the user will be authenticated the next time they sign in to the identity domain.
     * **Prompt for an additional factor** : Select this checkbox to prompt the user for another factor to sign in to the identity domain. If you select this checkbox, then you must specify whether the user is required to enroll in multifactor authentication (MFA) and how often this additional factor is to be used to sign in. Select **Any factor** to prompt the user to enroll and verify any factor enabled in the MFA tenant level settings. Select **Specified factors only** to prompt the user to enroll and verify a subset of factors enabled in the MFA tenant level settings. After you select **Specified factors only** , you can select factors that must be enforced by this rule.
     * **Frequency** : 
       * Select **Once per session or trusted device** , so that for each session that the user has opened from an authoritative device, they must use both their user names and passwords, and a second factor.
       * Select **Every time** , so that each time users sign in from a trusted device, they must use their user names and passwords, and a second factor.
       * Select **Custom interval** , and then specify how often users must provide a second factor to sign in. For example, if you want users to use this additional factor every two weeks, then select **Number** , enter `14` in the text field, and then select the **Interval** drop-down menu to select **Days**. If you configured multifactor authentication (MFA), then this number must be less than or equal to the number of days a device can be trusted according to MFA settings. For more information, see [Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm#understand-multi-factor-authentication "Multifactor Authentication \(MFA\) is a method of authentication that requires the use of more than one factor to verify a user's identity to access an identity domain in IAM.").
     * **Enrollment** : This menu contains two options: **Required** and **Optional**. 
       * Select **Required** to force the user to enroll in MFA.
       * Select **Optional** to give users the option of skipping enrolling in MFA. Users see the inline enrollment setup process after they enter their user name and password, but can select **Skip**. Users can then enable MFA later from the **2–Step Verification** setting in the **Security** settings of My Profile. Users are not prompted to set up a factor the next time that they sign in.
**Note:** If you set **Enrollment** to **Required** , and later change it to **Optional** , the change only affects new users. Users already enrolled in MFA will not see the inline enrollment process and will not be able to select **Skip** when signing in.
  3. Select **Add sign-on rule**.
**Note** If you have added multiple sign-on rules to this policy, then you can change the order that they will be evaluated. See [Changing the Priority of a Rule for a Sign-On Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/change-priority-sign-rule-policy.htm#change-priority-sign-rule-policy "If you have more than one sign-on rule for a sign-on policy, you can change the priority of a rule to change the order in which the identity domain evaluates it.").


Was this article helpful?
YesNo

