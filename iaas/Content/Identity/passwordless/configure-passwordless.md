Updated 2024-12-03
# Configuring Passwordless Authentication
Configure passwordless authentication settings and compliance policies that define which authentication factors that you want to allow, and then configure the passwordless factors.
There are three steps to setting up password authentication:
  * First, change the session settings for a domain so that users sign in using their username followed by an additional factor, instead of signing in using their username and password.
  * Then, select the authentication factors you want users to use. For example, one or more of:
    * Email
    * A TOTP (Time-Based One Time Password) from a mobile app passcode generator such as Oracle Mobile Authenticator (OMA) or Google Authenticator.
    * A text message (SMS) or phone call.
To find out about the different authentication factors, see [Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-authentication-factors.htm#configure-authentication-factors "You can configure the following authentication factors for an identity domain.").
  * Finally, update the IdP policy to allow the authentication factors you have selected.
See [Creating an Identity Provider Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/add-identity-provider-policy.htm#add-idp-policy "Create an identity provider policy for an identity domain.") to see how you can configure login options for users.


  * [Configuring Username Only Sign In](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/configure-username-first.htm#configure-username-only "Configure the sign in requirements so the user uses just their username, and sign in is verified by the authentication factor.")
  * [Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/configure-auth-factors.htm#configure-passwordless "Configure the authentication factors to use for passwordless authentication.")
  * [Configuring the IdP Policy](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/configure-idp-policy.htm#configure-username-only "Configure the IdP policy to include a new rule for passwordless authentication.")


Was this article helpful?
YesNo

