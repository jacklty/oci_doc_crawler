Updated 2024-05-28
# Managing Multifactor Authentication
Multifactor Authentication (MFA) is a method of authentication that requires the use of more than one factor to verify a user's identity to access an identity domain in IAM.
**Note** The tasks in this section are for an **administrator** that needs to set up MFA for an identity domain in IAM. If you're a user that needs to set up 2-step verification for yourself, see [Setting Up Account Recovery and 2-Step Verification](https://docs.oracle.com/en-us/iaas/Content/Identity/usersettings/manage_security_and_2_step_verification.htm#manage_security_and_2_step_verification "Set up and manage account recovery, 2-step verification, and generate bypass codes to ensure that you always have secure access to your account.").
With MFA enabled in an identity domain, when a user signs in to an application, they're prompted for their username and password, which is the first factor – something that they know. The user is then required to provide a second type of verification. The two factors work together to add an additional layer of security by using either additional information or a second device to verify the user's identity and complete the sign in process.
MFA may include any two of the following:
  * Something that you **know** , such as a passcode.
  * Something that you **have** , such as a device.
  * Something that you **are** , such as a fingerprint.


Users are increasingly connected, accessing their accounts and applications from anywhere. As an administrator, when you add MFA on top of the traditional username and password, you reduce the likelihood of online identity theft and fraud, which secures your business applications even if an account password is compromised.
This section contains the following topics:
  * [Securing IAM MFA with Oracle Best Practices](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm#understand-multi-factor-authentication__iam-domains-mfa-best-practice)
  * [Using MFA in Restricted Realms](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/understand-multi-factor-authentication.htm#understand-multi-factor-authentication__mfa-restr-realms)
  * [Default MFA Security for Identity Domains My Profile and My Apps Pages](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/default_mfa_access_for_identity_domains_my_profile.htm#default_mfa_access_for_identity_domains_my_profile "MFA enrollment and authentication is enabled by default for My Profile and My Apps access for all users.")
  * [Using Mobile Authenticator Apps with MFA](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/learn-using-mobile-authenticator-app-mfa.htm#learn-using-mobile-authenticator-app-mfa "Using a mobile authenticator application for MFA in an identity domain in IAM provides a second factor of authentication in the form of a time-based one-time passcode \(OTP\) or push notification, and offers several options for implementing app protection and compliance policy.")
  * [Multifactor Authentication Authorization Flow](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/multi-factor-authentication-authorization-flows.htm#multi-factor-authentication-authorization-flows "The authorization flows that support multifactor authentication \(MFA\) in an identity domain in IAM are the Authorization Code Grant Type and SAML2 Assertion.")
  * [Registering a Client Application](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/register-client-app.htm#register-client-app "Before you configure multifactor authentication \(MFA\) in an identity domain in IAM, register a client application so that you have the credentials \(client ID and client secret\) that are used for authentication in REST API calls. Oracle Support can use your client ID and client secret to help you troubleshoot if you have issues, for example, if you lock yourself out of an identity domain when configuring MFA.")
  * [Configuring Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.")
  * [Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-authentication-factors.htm#configure-authentication-factors "You can configure the following authentication factors for an identity domain.")


## Securing IAM MFA with Oracle Best Practices 🔗 
If you're using MFA with identity domains in IAM, we recommend that you set up MFA using Oracle best practices. See [IAM MFA](https://docs.oracle.com/iaas/Content/Security/Reference/iam_security_topic-IAM_MFA.htm) in the Security guide. 
## Using MFA in Restricted Realms 🔗 
Not all MFA providers operate exclusively within restricted realm boundaries. Therefore, before enabling MFA features, we recommend that you carefully evaluate the MFA providers you might want to use, to ensure they operate within the bounds of a restricted realm and that they meet your organization's security and compliance requirements.
Was this article helpful?
YesNo

