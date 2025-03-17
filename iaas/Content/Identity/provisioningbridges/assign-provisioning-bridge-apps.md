Updated 2025-01-14
# Assigning a Provisioning Bridge to Apps
After creating a provisioning bridge for an identity domain in IAM, you can assign it to on-premises apps in the App Catalog. Because this bridge serves as a provisioning and synchronizing agent between the identity domain and your apps, the bridge can poll for changes to users or groups in the apps and synchronize those changes into the identity domain.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want.
  3. Select **Applications**.
  4. Select the name of the App Catalog app to which you want to assign a bridge.
  5. On the app details page, select **Deactivate**.
  6. In the **Deactivate application** dialog box, select **Deactivate application**.
**Note** You must deactivate the app so that you can modify it by assigning a provisioning bridge to it.
  7. Under **Resources** , select **Provisioning** , and then select **Edit provisioning**.
  8. Turn on the **Enable Provisioning** switch.
  9. If prompted, confirm that you want to enable provisioning, and then select **Save changes**.
  10. From the **Associate with Provisioning Bridge** list, select the bridge that you want to assign to this app.
**Note** If the provisioning bridge has an inactive status, then activate it.
  11. Select **Save**.
  12. Select **Activate**.
  13. In the **Activate provisioning bridge** window, select **Activate application**.
**Note** By activating this app, the provisioning bridge that you assigned to it can be used either to poll the app for changes to users and groups in the app, and synchronize these changes into the identity domain, or to provision users to the app.
  14. To assign the provisioning bridge to another app, repeat the preceeding steps.
  15. Navigate back to the identity domain by selecting its link in the breadcrumb at the top of the page.
  16. Select **Settings** , and then select **Provisioning Bridges**.
  17. Select the name of the bridge that you assigned to apps, and then select **Apps**.
  18. Verify that you see each app to which you assigned the provisioning bridge.


Was this article helpful?
YesNo

