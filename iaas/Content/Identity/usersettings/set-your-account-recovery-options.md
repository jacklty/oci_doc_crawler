Updated 2024-02-13
# Setting Account Recovery Options
Set account recovery options so that if you have trouble signing in, you're locked out, or you forget your password, then you can regain access to your account.
**Note**
The tasks in this section are for **users** to perform to set up account recovery using the options configured by an administrator. If you're an administrator that needs to set up account recovery for an identity domain, see [Managing Account Recovery](https://docs.oracle.com/en-us/iaas/Content/Identity/accountrecovery/understand-account-recovery.htm#understand-account-recovery "Account recovery is an automated process that allows users regain access to an identity domain in IAM if they have trouble signing in, if they're locked out, or they forget their passwords.").
You set up account recovery either _during your first sign in_ to an identity domain or _after your first sign_ to an identity domain by using the self-service **My profile** console.
The account recovery factors that are available for you to set are dependent upon the selections your identity domain administrator or security administrator made when they set up account recovery for your identity domain. For example, if your administrator disabled _mobile number_ as an account recovery factor, then you can't use this factor to recover your account. Account recovery factors that aren't enabled don't appear in the **Security** tab of the **My profile** console. 
You can set the following account recovery factors if they've been enabled by your administrator:
  * **Recovery email** : By default, your primary email address has been set as the email address that IAM uses to help you recover your account. If you have to regain access, then IAM sends a notification to this email address. Follow the instructions in the notification to recover your account. Instead of your primary email address, you can specify an alternate (recovery) email address to regain access.
  * **Mobile number** : You can provide a mobile number that IAM uses to help you recover your account. This way, if you have to regain access, then IAM sends a one-time passcode in a text message to this mobile number. You enter this passcode to recover your account.
  * **Security questions** : You can select and answer security questions, and provide hints for answers to these questions, to verify your identity. If you need to recover your account, then you must answer these questions correctly to regain access.


This section contains the following tasks: 
  * [Changing Your Account Recovery Email](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/set-recovery-email-address-account-recovery-factor.htm#set-recovery-email-address-account-recovery "Set up an email other than your primary email as a factor for password recovery.")
  * [Setting Your Mobile Number for Account Recovery](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/set-your-mobile-number-account-recovery-factor.htm#set-your-mobile-number-account-recovery "You can provide a mobile number that IAM uses to help you recover your account. This way, if you have to regain access, then IAM sends a one-time passcode in a text message to this mobile number. You enter this passcode to recover your account.")
  * [Selecting Security Questions for Account Recovery](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/set-security-questions-account-recovery-factor.htm#set-security-questions-account-recovery "You can select and answer security questions, and provide hints for answers to these questions, to verify your identity. If you have to recover your account, then you must answer these questions correctly to regain access.")
  * [Updating or Removing an Account Recovery Factor](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/remove-account-recovery-factor.htm#remove-security-questions-account-recovery-factor "If you no longer want to use a specific account recovery factor to recover your account, then you can remove it.")


Was this article helpful?
YesNo

