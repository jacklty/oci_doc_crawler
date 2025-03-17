Updated 2025-02-13
# Configuring Multifactor Authentication Settings
Configure multifactor authentication (MFA) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.
**Note** The tasks in this section are for an _administrator_ that needs to set up MFA for an identity domain in IAM. If you're a user that needs to set up 2-step verification for yourself, see [Setting Up Account Recovery and 2-Step Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/manage_security_and_2_step_verification.htm#manage_security_and_2_step_verification "Set up and manage account recovery, 2-step verification, and generate bypass codes to ensure that you always have secure access to your account.").
**Before you begin:**
  * Create a test user in a test identity domain. Use that identity domain to set up MFA for the first time. See [Creating an Identity Domain](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm#create-identity-domain "To create an identity domain in IAM, administrators need to know which identity domain type they want to create, in which compartment to create it, and the new identity domain administrator's sign-in credentials, if needed. The domain types that you're allowed to create are based on your subscription.") and [Creating a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/create-user-accounts.htm#top "Create a user account for a user in an OCI IAM identity domain.").
  * Set up a client application to enable access to an identity domain using the REST API in case your Sign-On Policy configuration locks you out. If you don't set up this client application and a sign-on policy configuration restricts access to everyone, then all users are locked out of the identity domain until you contact Oracle Support. For information about setting up the client application, see [Registering a Client Application](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/register-client-app.htm#register-client-app "Before you configure multifactor authentication \(MFA\) in an identity domain in IAM, register a client application so that you have the credentials \(client ID and client secret\) that are used for authentication in REST API calls. Oracle Support can use your client ID and client secret to help you troubleshoot if you have issues, for example, if you lock yourself out of an identity domain when configuring MFA.").


To define MFA settings, you must be assigned to either the identity domain administrator role or the security administrator role.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Security**.
  4. On the **Security** page, select **MFA**.
  5. Under **Factors** , select each of the factors that you want to be required to access an identity domain.
For an explanation of each factor, see [Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-authentication-factors.htm#configure-authentication-factors "You can configure the following authentication factors for an identity domain.").
  6. (Optional) Select **Configure** for the MFA factors that you have selected to configure them individually.
For instructions for each factor, see [Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-authentication-factors.htm#configure-authentication-factors "You can configure the following authentication factors for an identity domain.").
  7. (Optional) Set the **Maximum number of enrolled factors** that users can configure.
  8. (Optional) Use the **Trusted devices** section to configure trusted device settings. 
Similar to "remember my computer," trusted devices don't require the user to provide secondary authentication each time that they sign in.
  9. (Optional) Under **Sign-in rules** , set the maximum number of unsuccessful MFA attempts that you want to allow a user to incorrectly provide MFA verification before being locked out.
  10. Select **Save changes** , and then confirm the change.
  11. Ensure that any sign-on policies that are active allow two-step authentication: 
    1. On the **Security** page for the domain, select **Sign-on policies**.
    2. On the **Sign-on policies** page, select **Default Sign-On Policy**.
    3. On the **Default Sign-On Policy** page, under **Resources** , select **Sign-on rules**.
    4. In the **Default Sign-On Rule** row, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Edit sign-on rule**.
    5. In the **Edit sign-on rule** dialog box, under **Exclude users** , exclude yourself or another identity domain administrator from this rule until testing is complete. This ensures that at least one administrator always has access to the identity domain should issues arise.
    6. Under **Actions** , select **Allow access** and select **Prompt for an additional factor**.
    7. Select **Save changes**.
    8. If other sign-on policies have been added, follow the preceding steps for each of those policies to ensure that MFA is enabled under all conditions where you want it to be enabled.
**Note**
The settings for the default sign-on rule enable MFA globally. Settings for other sign-on rules might override the default sign-on rule for users and groups specified by conditions for those rules. See [Managing Password Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/Managing-Password-Policies.htm#topic_g2w_wms_l4b "Create and manage group-based password policies for an identity domain in IAM.").
**Important**
Ensure you exclude one Identity Domain Administrator from _each_ policy. This ensures that at least one administrator always has access to the identity domain should issues arise.
Set **Enrollment** as **Optional** until you're finished testing the sign-on policy.
  12. (Optional) Enable separate lock thresholds for MFA validation failure and MFA notification attempts. To enable this, ensure you know how to make REST API calls.
**Note** There are two new attributes in the user MFA schema:
     * **mfaIncorrectValidationAttempts** —Tracks incorrect MFA validation attempts by a user.
     * **mfaNotificationAttempts** —Tracks MFA notification attempts by a user.
Also there are two new attributes added to AuthenticationFactorSettings:
     * **maxMfaIncorrectValidationAttempts** —The maximum number of incorrect MFA validation that can be tried before an account is locked. If a value is set for this attribute, there must also be a value set for maxMfaNotificationAttempts. If this attribute is not set, the MFA locking behavior is determined by maxIncorrectAttempts. If mfaIncorrectValidationAttempts reaches maxMfaIncorrectValidationAttempts, the user is locked immediately.
     * **maxMfaNotificationAttempts** —The maximum number of MFA notifications that can be tried before an account is locked. If a value is set for this attribute, there must also be a value set for maxMfaIncorrectValidationAttempts. If this attribute is not set, the MFA locking behavior is determined by maxIncorrectAttempts. If the mfaNotificationAttempts reaches maxMfaNotificationAttempts, the user is locked the next time they try to initiate a notification, to allow the user to authenticate using the last MFA notification.
Update AuthenticationFactorSettings to set both` maxMfaIncorrectValidationAttempts` and `maxMfaNotificationAttempts` by doing a `PATCH` call on `<_IDENTITY_DOMAIN_URL_>/admin/v1/AuthenticationFactorSettings/AuthenticationFactorSettings`endpoint with following payload:
```

{
 "schemas": [
  "urn:ietf:params:scim:api:messages:2.0:PatchOp"
 ],
 "Operations": [
  {
   "op": "add",
   "path": "endpointRestrictions.maxMfaIncorrectValidationAttempts",
   "value": 3
  },
  {
   "op": "add",
   "path": "endpointRestrictions.maxMfaNotificationAttempts",
   "value": 3
  }
 ]
} 
```

The value for both can vary from a minimum of 3 to a maximum of 10.
  13. To test the configuration, sign out of the Console and then sign in as the test user.
You will be prompted for a second factor.


Was this article helpful?
YesNo

