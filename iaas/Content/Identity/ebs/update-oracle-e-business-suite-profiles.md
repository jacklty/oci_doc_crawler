Updated 2025-01-14
# Updating Oracle E-Business Suite Profiles
Configure the URL allowlist property to prevent access to the Oracle E-Business Suite local login and direct all requests to the E-Business Suite Asserter log in instead.
  1. Log in to Oracle E-Business Suite console as a user that is assigned the Functional Administrator responsibility (typically `sysadmin`).
  2. Use the drawer icon (E-Business Suite version 12.2.8) or navigator icon (E-Business Suite version 12.1/12.2), select **Functional Administrator**.
  3. In the **Oracle Applications Administration** page, select the **Core Services** tab, and then select **Profiles**.
  4. Enter `APPS_AUTH_AGENT` in the **Code** field and then select **Go**.
  5. On the list of profiles, select **Application Authenticate Agent** , and then select **Define Profile Values**.
  6. On the **Define Profile Values: Application Authenticate Agent** page, enter the E-Business Suite Asserter URL in the **Site Value** field, and then select **Update**.
  7. Select **Profiles** under the **Core Services** tab, enter `APPS_SSO` in the **Code** field, and then select **Go**.
  8. On the list of profiles, select **Applications SSO Type** , select **Define Profile Values** , change the **Site Value** field from **SSWA** to **SSWA w/SSO** , and then select **Update**.
  9. Select **Profiles** under the **Core Services** tab, enter `ICX_SESSION_COOKIE_DOMAIN` in the **Code** field, and then select **Go**.
  10. On the list of profiles, select **Oracle Applications Session Cookie Domain** , select **Define Profile Values** , replace the **Site Value** field from **HOST** to **DOMAIN** , and then select **Update**.
  11. Restart the Oracle E-Business Suite servers.


Was this article helpful?
YesNo

