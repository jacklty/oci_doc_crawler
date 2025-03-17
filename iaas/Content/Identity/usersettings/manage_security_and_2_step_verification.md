Updated 2024-11-15
# Setting Up Account Recovery and 2-Step Verification
Set up and manage account recovery, 2-step verification, and generate bypass codes to ensure that you always have secure access to your account.
**Important**
The tasks in this section are for **users** to perform to set up account recovery and 2-step verification using the options configured by an administrator. If you're an administrator that needs to set up account recovery or 2-step verification for an identity domain, see [Managing Account Recovery](https://docs.oracle.com/en-us/iaas/Content/Identity/accountrecovery/understand-account-recovery.htm#understand-account-recovery "Account recovery is an automated process that allows users regain access to an identity domain in IAM if they have trouble signing in, if they're locked out, or they forget their passwords.") and [Managing Multifactor Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm#understand-multi-factor-authentication "Multifactor Authentication \(MFA\) is a method of authentication that requires the use of more than one factor to verify a user's identity to access an identity domain in IAM.").
If your administrator has enabled bypass codes, we recommend that you create a bypass code and store it in a secure location, for example, write it down in a notebook. If you lose your bypass code, you also have the option to contact an administrator to obtain a bypass code for access.
Users, to learn how to generate a bypass code for yourself, see [Generating a Bypass Code](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/generate-bypass-code.htm#generate-bypass-code "A bypass code is useful as a second verification factor or for account recovery. You can generate bypass codes after you enroll in 2-Step Verification. And then use that bypass code to access your account when, for example, you don't have your mobile device for verification.").
Administrators, to learn how to generate a bypass code for another user, see [Generating a Bypass Code for a User](https://docs.oracle.com/en-us/iaas/Content/Identity/users/generate-bypass-codes-user-accounts.htm#top "Generate a bypass code for a user in an OCI IAM identity domain. The code can be used as a one-time 2-Step Verification method to sign in.").
## How Account Recovery and 2-Step Verification Work
  1. **Administrators** set up account recovery and 2-step verification for users in an identity domain by: 
     * choosing the recovery and verification factors available to users and
     * specifying whether users must enroll.
  2. You, as a **user** , set up account recovery and 2-step verification using the recovery and verification factors the administrator set up either 
    1. _during your first sign in_ to an identity domain or 
    2. _after your first sign_ to an identity domain by using the self-service **My profile** console.


## Account Recovery
Account recovery is an automated process designed to help you regain access to you account if you have trouble signing in, if you're locked out, or you forget your password.
**Note** The account recovery factors that are available for you to set are dependent upon the selections your identity domain administrator or security administrator made when they set up account recovery for your identity domain. For example, if your administrator disabled _mobile number_ as an account recovery factor, then you can't use _mobile number_ to recover your account. Account recovery factors that aren't enabled don't appear in the **Security** tab of the **My profile** console. 
You must set at least one account recovery factor. In addition to having one account recovery factor, if the option is available, always generate a bypass code and store it in a safe place. See [Generating a Bypass Code](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/generate-bypass-code.htm#generate-bypass-code "A bypass code is useful as a second verification factor or for account recovery. You can generate bypass codes after you enroll in 2-Step Verification. And then use that bypass code to access your account when, for example, you don't have your mobile device for verification.").
## 2-Step Verification 
2-Step verification is an authentication method that requires you to use more than one way of verifying your identity, providing a second layer of security to your account.
**Note**
The 2-step verification factors that are available for you to set are dependent upon the selections your identity domain administrator or security administrator made when they set up 2-factor verification for your identity domain. For example, if your administrator disabled _email_ as a 2-factor verification factor, then you can't use _email_. 2-step verification factors that aren't enabled don't appear in the **Security** tab of the **My profile** console. 
This section contains the following topics:
  * [Setting Account Recovery Options](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/set-your-account-recovery-options.htm#set-your-account-recovery-options "Set account recovery options so that if you have trouble signing in, you're locked out, or you forget your password, then you can regain access to your account.")
  * [Activating 2-Step Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/enroll-2-step-verification-first-login.htm#enroll-2-step-verification-first-login "If your administrator made 2-step verification optional, and you have selected Skip each time you sign in, you can enable 2-step verification in the My profile console Security tab.")
  * [Managing 2-Step Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/manage-2-step-verification.htm#manage-2-step-verification "2-step verification is an authentication method that requires you to use more than one way of verifying your identity, providing a second layer of security to your account.")
  * [Generating a Bypass Code](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/generate-bypass-code.htm#generate-bypass-code "A bypass code is useful as a second verification factor or for account recovery. You can generate bypass codes after you enroll in 2-Step Verification. And then use that bypass code to access your account when, for example, you don't have your mobile device for verification.")
  * [Signing In to an Identity Domain Using an Alternative Login Method](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/sign-in-identity-domain-alternative-login-method.htm#sign-in-identity-domain-alternative-login-method "If you have set up more than one 2-step verification method or at least one 2-step verification method and a bypass code, then you can switch to an alternative login method when you can't use your default.")


Was this article helpful?
YesNo

