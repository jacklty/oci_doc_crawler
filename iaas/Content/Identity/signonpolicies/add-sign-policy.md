Updated 2025-01-14
# Creating a Sign-On Policy
Add a sign-on policy to an identity domain in IAM.
This task adds a sign-on policy in a deactivated state. After completing this task, you must activate the policy to begin enforcing it in the identity domain.
You can define the following criteria for sign-on policies:
  * The identity providers to be used to authenticate the user
  * The groups of which the user is a member
  * Whether the user is an identity domain administrator 
  * Whether to exclude a user
  * The IP address that the user is using to sign in to the identity domain
  * Whether the user is forced to sign in to the identity domain again (for authentication purposes), or is authenticated the next time they sign in to the identity domain
  * Whether the user is prompted for an another factor to sign in to the identity domain


To add a sign-on policy, follow these steps:
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Security** and then select **Sign-on policies**.
  4. Select **Create sign-on policy**.
  5. Enter a name and an optional description for the policy. Avoid entering confidential information. 
  6. Select **Add policy**.
The sign-on policy is saved in a deactivated state. When you finish creating the policy, you must activate the policy to use it.
  7. On the **Add sign-on rules** page, select **Add sign-on rule**.
  8. Add a name for the sign-on rule. Avoid entering confidential information.
  9. Under **Conditions** , provide the following information: 
     * **Authenticating identity provider** (Optional): Enter or select all identity providers that are used to authenticate the user accounts evaluated by this rule. If you leave this empty, the other conditions are used for authentication.
     * **Group membership** : Enter or select the groups that the user must be a member of to meet the criteria of this rule. You must enter at least three characters to initiate a search of groups.
     * **Administrator** : If the user must be assigned to administrator roles in the identity domain to meet the criteria of this rule, then select this checkbox.
     * **Keep me signed in** : Select this option to apply the rule only if a valid **Keep me signed in session** exists for the user.
To use this condition, you must enable **Keep me signed in**. See [Changing Session Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/sessionsettings/change-session-settings.htm#change-session-settings "Identity domain session settings in IAM include setting the session duration; the URLs for login, logout, errors, and social callback; the authentication flow for accessing an identity domain, such as keeping the user signed in; and CORS settings."). 
The sign-on policy overrides the **Keep-me signed in** session. This means that even though a user is signed in using **Keep-me signed in** , after the session expires, if the policy requires reauthentication or multifactor authentication (MFA), then the user is challenged to reauthenticate or challenged to provide MFA.
     * **Exclude users** : Enter or select the users to exclude from the rule. You must enter at least three characters to initiate a search of users. 
**Important** Ensure you exclude one identity domain administrator from each policy, which ensures that at least one administrator always has access to the identity domain if issues arise.
     * **Filter by client IP address** : Select one of the following options:
       * **Anywhere** : Users can sign in to the identity domain by using any IP address.
       * **Restrict to the following network perimeters** : Users can sign in to the identity domain by using only IP addresses that are contained in defined network perimeters. In the **Network perimeters** text box, enter or select network perimeters that you defined. For more information, see [Creating a Network Perimeter](https://docs.oracle.com/en-us/iaas/Content/Identity/networkperimeters/add-network-perimeter.htm#add-network-perimeter "Create a network perimeter in an identity domain in IAM and configure it to restrict the IP addresses that users can use to sign in.").
  10. Under **Actions** , select whether a user is allowed to access the Console if the user account meets the criteria of this rule. 
If you select **Deny access** , then skip to the next step.
If you select **Allow access** , enter values for the following additional options:
     * Prompt for reauthentication: Select this checkbox to force the user to re-enter credentials to access the assigned application even when there's an existing IAM domains session.
       * If selected, this option prevents single sign-on for the applications assigned to the sign-on policy. For example, an authenticated user must sign on to a new application.
       * If not selected, and the user has previously authenticated, the user can access the application by using their existing single sign-on session without needing to enter credentials
     * **Prompt for an additional factor** : Select this checkbox to prompt the user for an additional factor to sign in to the identity domain.
If you select this checkbox, then you must specify whether the user is required to enroll in multifactor authentication (MFA) and how often this additional factor is to be used to sign in.
     * **Any factor** or **Specified factors only** : Select one of these options:
       * **Any factor** : Prompts the user to enroll in and verify any factor enabled in the MFA tenant-level settings.
       * **Specified factors** : Only prompts the user to enroll in and verify a subset of factors enabled in the MFA tenant-level settings. After you select **Specified factors** , select factors that must be enforced by this rule.
     * **Frequency** : Specify how often users are prompted for a second factor:
       * **Once per session or trusted device** : For each session that the user has opened from an authoritative device, they must use both their username and passwords, and a second factor.
       * **Every time:** : Each time a user signs in from a trusted device, they must use their usernames and passwords, and a second factor.
       * **Custom interval** : Specify how often users must provide a second factor to sign in. For example, if you want users to use this additional factor every two weeks, then select `14` for the **Number** and select **Days** for **Interval**. If you configured MFA, then this number must be less than or equal to the number of days a device can be trusted according to MFA settings. For more information, see [Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm#understand-multi-factor-authentication "Multifactor Authentication \(MFA\) is a method of authentication that requires the use of more than one factor to verify a user's identity to access an identity domain in IAM.").
     * **Enrollment** : Select one of the following options:
**Important** Set **Enrollment** as **Optional** until you're finished testing the sign-on policy.
       * Required forces the user to enroll in MFA.
       * Select **Optional** to gives users the option of skipping enrolling enrollment in MFA. Users see the inline enrollment setup process after they enter their username and password, but they can select **Skip**. Users can then enable MFA later from the **2–step verification** setting in the **Security** settings of My Profile. Users aren't prompted to set up a factor the next time that they sign in. If you set **Enrollment** to **Required** , and later change it to **Optional** , the change affects only new users. Users already enrolled in MFA won't see the inline enrollment process and won't be able to select **Skip** when signing in
  11. Select **Add sign-on rules**.
  12. (Optional) On the **Add sign-on rules** page, select **Add sign-on rule** again to add another sign-on rule to this policy. Otherwise, select **Next**.
**Note** If you added multiple sign-on rules to this policy, then you can change the order in which they will be evaluated. Select **Edit priority** and then use the arrows to change the order of the rules.
  13. On the **Add apps** page, select **Add app** to add apps to this policy.
  14. In the **Add app** panel, select the checkbox for each app that you want to add to the policy. Then, select **Add app**.
**Note**
You can add an app to only one sign-on policy. If the app isn't assigned to any sign-on policy explicitly, then the default sign-on policy applies to the app.
  15. When you're ready, select **Close**. The details page for the sign-on policy is displayed.


Was this article helpful?
YesNo

