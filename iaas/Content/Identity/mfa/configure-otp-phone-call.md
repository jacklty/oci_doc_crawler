Updated 2025-01-14
# Configuring OTP Text Messages and Phone Calls
Configure passcode settings to send users in an identity domain in IAM a one-time passcode (OTP) as a phone call or text message. Use a phone call template to configure the phone call.
Before you can configure phone call settings, you must first set up a [Vonage](https://www.vonage.com/) provider.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Security**.
  4. On the **Security** page, select **Two-factor authentication**.
  5. Select the **Phone number** tab.
  6. Make any necessary changes to the **Passcode length** and **Passcode validity duration**. These settings apply to one-time passcodes sent in phone calls.
     * **Passcode length:** The number of characters in the passcode.
     * **Passcode validity duration:** The number of minutes for which the passcode will be valid, after the passcode was sent.
  7. Configure a phone call.
    1. Expand **Phone call provider**.
    2. If you haven't already done so, set up your [Vonage](https://www.vonage.com/) provider. When you are ready, select **Select here to proceed if the Vonage provider is already configured**.
You can enter the Vonage provider settings only after you select this checkbox.
    3. Enter the **Vonage provider settings**.
    4. Under **Phone call template** , select the language for the message.
    5. Modify the template to create the wording that's sent in the message to users.
IAM provides a fixed list of message variables. Select **Message variables** to view the available variables and variable definitions.
**Note**
Add your company name to the **Company name** field on the **Branding** page in **Settings**. A company name longer than 30 characters are truncated in the message body. If you leave the **Company name** field, your company details don't appear in notifications such as Oracle Mobile Authenticator (OMA) when a user completes MFA enrollment.
  8. Select **Save changes**.
  9. Confirm the changes when prompted.


Was this article helpful?
YesNo

