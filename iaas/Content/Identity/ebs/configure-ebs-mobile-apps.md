Updated 2025-01-14
# Configuring E-Business Suite for Mobile Applications
Configure Oracle E-Business Suite to enable E-Business Suite mobile applications to authenticate with IAM.
  1. Access the drawer icon (E-Business Suite version 12.2.8) or navigator icon (E-Business Suite version 12.1/12.2), select **Mobile Applications Manager** , and then select **Applications**.
  2. Search for **Application Name**. For example, `EBS             Approvals`.
  3. In the results list, select the **Configure** icon for the application. For example, **EBS Approvals**.
  4. In the **Configure Mobile Application** page, expand the **Connection Settings**.
  5. Select **Sub Category** as `AppsSSO           Login`.
  6. Expand the **Connection Settings** category, and then update the parameters as follows:
     * **LoginURL** : `%APPS_AUTH_AGENT%/login/sso`
     * **LogoutURL** : `%APPS_AUTH_AGENT%/logout/sso`
     * **LoginSuccessURL** : `%APPS_AUTH_AGENT%/login/sso`
     * **APPS_SESSION_SERVICE** : `%APPS_AUTH_AGENT%/login/apps`
  7. Select **Apply**.

After you save the changes, restart Oracle E-Business Suite.
Was this article helpful?
YesNo

