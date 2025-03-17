Updated 2025-01-14
# Changing Data Sharing Settings
Identity domain session settings in IAM include setting the session duration; the URLs for sign-in, logout, errors, and social callback, the authentication flow for accessing an identity domain, such as keeping the user signed in, and CORS settings.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Settings**.
  4. On the **Settings** page, select **Session settings**.
  5. Select **Allow cross-origin resource sharing (CORS)**. CORS allows client applications from one domain to obtain data from another domain. If you select this option, you might also want to set the **Allowed CORS domain names** option.
  6. Leave the **Show the specific error message for login policy violation** option on.
This option is turned on by default and allows the system to display the specific policy-violation error-message if the sign-in policy is violated. If the option is turned off, the system displays the standard error message.
  7. Select **Enable Keep me signed in**. This option allows users to stay signed in to the identity domain. If you select this option, a **Keep me signed in** option displays on the sign-in page for users to enable it for their account. Customize **Keep me signed in** using the following options.
     * **Keep me signed in duration (days)**. Enter how many days users can stay signed in before they're automatically signed out.
     * **Reauthentication interval (days)**. Enter the interval at which a user must reauthenticate if a user hasn't signed in using Keep me signed in.
     * **Maximum keep me signed-in sessions**. Enter the maximum number of signed-in sessions that a user can have.
**Note** Changing the Keep Me Signed In settings cancels current sign-in tokens. Users need to sign-in again.
  8. Select **Save changes**.


Was this article helpful?
YesNo

