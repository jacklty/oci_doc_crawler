Updated 2025-01-14
# Changing Customer Endpoint Settings
Set customer endpoint settings in IAM.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. On the domain details page, select **Settings**.
  4. On the **Settings** page, select **Session settings**.
  5. Enter the sign-in URL where you want the user redirected to sign in.
  6. To allow sign-in customization for the Admin Console, select **Allow custom sign-in page**.
  7. To show only the username field on the Sign In page, select **Enable username first flow**.
This allows the user to use [passwordless authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordless/manage-passwordless.htm#manage-passwordless "Passwordless authentication allows you to bypass the standard web-form-based authentication presented to users when using email or a mobile device.") by entering only their username.
  8. Choose whether users see a session picker or a domain picker when they sign in.
     * The session pickers shows the user all active and historical sessions in different domains in the tenancy in the browser. To show the session picker, select **Enable Session Picker for OCI console**. This option is selected by default.
     * The domain picker shows the user all domains available in the tenancy. To show the domain picker, unselect **Enable Session Picker for OCI console**.
  9. Enter a **Sign-out URL**. For example, to redirect the user to the **My profile** console, enter `/ui/v1/myconsole`.
  10. In the **Error URL** field, enter the tenant-specific error page URL to which a user is redirected after an error. This URL is used when the application-specific custom error URL isn't specified for an application.
  11. In **Social linking callback URL** , enter the URL to redirect to after linking a user between social providers and IAM is complete. This URL is used when the application-specific social linking callback URL isn't specified for an application.
  12. Select **Save changes**.


Was this article helpful?
YesNo

