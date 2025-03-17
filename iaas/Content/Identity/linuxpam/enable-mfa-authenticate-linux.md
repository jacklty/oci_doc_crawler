Updated 2025-01-14
# Enabling MFA to Authenticate into Linux
Learn how to set up Multi Factor Authentication (MFA) so Linux users can authenticate using multiple factors.
  1. Enable the MFA factors for your requirements. See [Configuring Multifactor Authentication Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-multi-factor-authentication-settings.htm#configure-multi-factor-authentication-settings "Configure multifactor authentication \(MFA\) settings and compliance policies that define which MFA factors are required to access an identity domain in IAM, and then configure the MFA factors.") and [Configuring Authentication Factors](https://docs.oracle.com/en-us/iaas/Content/Identity/mfa/configure-authentication-factors.htm#configure-authentication-factors "You can configure the following authentication factors for an identity domain.")
  2. Create a group for MFA, and add the POSIX Users to this group.
    1. Navigate to **Groups** > **Create group.**
    2. Enter the **Name** of the group.
    3. Search for the POSIX users you want to enable for MFA.
    4. Select the users and select **Create**.
  3. Create a Sign-On rule.
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
    2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
    3. Select the **Default Sign-On Policy**.
    4. Select **Add sign-on rule**. 
    5. Enter a **Rule name** , and under **Conditions** in the field **Group membership** type and select the group that you created above. Under **Actions** ensure that **Allow access** and **Prompt for an additional factor** is checked. Change the **Enrollment** to **Optional** and select **Add sign-on rule**.
**Note** The only sign on policy that the Linux Pluggable Authentication Module (PAM) supports, is the **Default Sign-On Policy**.
  4. Move the newly created sign-on rule to the top by selecting the sign-on rule and dragging it to the top of the list. Select **Save**. This ensures that this rule gets evaluated first so that users belonging to the chosen group are prompted for MFA when they sign in.
  5. Sign in to IAM as a user in the MFA Group, for example via `https://identity-cloud-service-instance-url/ui/v1/myconsole`
  6. Enroll the user in MFA and select the factors to enroll in.
**Note** Backup factors aren't currently supported with the IAM Linux PAM.
  7. After the user is enrolled in MFA, test authentication on Linux:
    1. SSH into your Linux environment where the IAM Linux PAM is installed.
    2. When prompted enter the password for the IAM user.
    3. Enter the second factor with which to authenticate.


Was this article helpful?
YesNo

