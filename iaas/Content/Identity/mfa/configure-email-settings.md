Updated 2025-01-14
# Configuring Email Settings
Configure settings in an identity domain in IAM to send a one-time passcode (OTP) to a user's primary email address.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Security**.
  4. On the **Security** page, select **Two-factor authentication**.
  5. Select the **Email** tab.
  6. Under **Configure the email settings for MFA** , enter the following values:
     * **Passcode length:** The number of characters in the passcode.
     * **Passcode validity:** The number of minutes for which the passcode will be valid, after the passcode was sent.
  7. Under **Configure the email settings for account recovery and activation** , enter the following values:
     * **Activation email validity:** The number of days that the activation email remains valid. Enter a value between 1 and 30.
     * **Password reset email validity:** The number of hours that that the password reset email remains valid. Enter a value between 1 and 720.
  8. To allow the user to add an alternate email address for account recovery, select the checkbox.
  9. Select **Save changes**.
  10. Confirm the changes when prompted.
  11. To access the email template that's sent to the user's primary email account and edit it as needed, follow these steps:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
    2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
    3. On the domain details page, select **Settings**.
    4. On the **Settings** page, select **Notifications**.
    5. Select the **Email templates** tab.
    6. The template name is **2-Step email one-time passcode verification**.
    7. Edit the template as needed.


Was this article helpful?
YesNo

