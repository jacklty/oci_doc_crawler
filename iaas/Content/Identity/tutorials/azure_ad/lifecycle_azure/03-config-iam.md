Updated 2025-01-14
# Tutorial 3: OCI IAM as Authoritative Source to Manage Identities in Entra ID
Configure OCI IAM as the authoritative identity store to manage identities, along with entitlements in Entra ID
In this scenario, OCI IAM acts as the identity manager. OCI IAM pushes users, groups, and licenses to Entra ID.
  1. First, configure OCI IAM to enable IAM as the authoritative identity store to manage identities in Entra ID. Create an app in OCI IAM for MS Office 365 using IAM's App Catalog, which provides pre built integrations with major cloud services.
  2. Assign a user to the MS Office 365 application in OCI IAM, and assign the groups and roles you want the user to be provisioned to MS Office 365.


[1. Add MS Office 365 as an App in OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/03-config-iam.htm)
Use OCI IAM's App Catalog to create an app which uses MS Office 365.
  1. Open a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm) and enter the Console URL
`https://cloud.oracle.com[](https://cloud.oracle.com)`.
  2. Enter your **Cloud Account Name** , also referred to as your tenancy name, and select **Next**.
  3. Select the identity domain to sign in to. This is the identity domain that you will configure user lifecycle management in.
  4. Sign in with your username and password.
  5. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  6. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**.
  7. Select **Add Application** , and choose **Application Catalog** and select **Launch app catalog** which contains pre configured application templates.
  8. Search for the MS Office 365 application template by entering the string `MS Office`, then select the tile.
  9. Select the tile to create an MS Office 365 application.
  10. Enter a name for the application, or use the default `MS Office 365`.
  11. Select **Next** and then **Next** again, and on the Configure provisioning page enable provisioning, and confirm that you want to enable provisioning.
  12. Configure connectivity by selecting **Authorize with MS Office 365**.
  13. Microsoft opens a new browser window.
  14. Log in using your MS Office 365 credentials. On the Permissions requested dialog, Select **Consent on behalf of your organization** , and select **Accept**.
[![Microsoft request permissions to access resources](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/ms-office-permissions.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/ms-office-permissions.png)
  15. The new browser closes and you are returned to the Add MS Office 365 page.
  16. A message pops up to say that the connection has been successful.
  17. Select **Finish**.
  18. On the application overview page, select **Activate** and confirm that you want to activate the application.
The MS Office application is now active.


You have successfully created an MS Office 365 application in OCI IAM, and configured it to connect to MS Office 365.
[2. Assign Users to the MS Office 365 App](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/03-config-iam.htm)
Assign a user to the MS Office 365 application, and assign it to the Office roles and groups the user will have when provisioned to MS Office 365.
  1. In the MS Office 365 application, select **Users** on the left under **Resources**.
  2. Select **Assign users**.
  3. Search for the user you want to assign, then select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for that user and select **Assign**.
[![Assign user to MS Office 365 application](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/ms-office-assign-user.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/ms-office-assign-user.png)
  4. Select **Next**.
  5. On the Add Details page, scroll down, and under **Licenses** , select **Add** and assign the licences you want the user to be provisioned with on MS Office 365.
  6. On the Add Details page, scroll down, and under **Roles** , select **Add** and assign the roles you want the user to be provisioned with.
  7. Under **Groups** , select **Add** and assign the groups you want the user to be provisioned with.
  8. Select **Assign User**.


You can see the new user in the User List with Active status.
[![New users are listed](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/lifecycle-users.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/lifecycle-users.png)
Was this article helpful?
YesNo

