Updated 2025-02-18
# Tutorial 1: Entra ID as Authoritative Source to Manage Identities Using Entra ID Gallery Application
Configure Entra ID as the authoritative identity store to manage identities in OCI IAM using an application template from Entra ID Gallery.
  1. Configure OCI IAM so that Entra ID is the identity store to manage identities in OCI IAM. In OCI IAM, create a confidential application.
  2. Generate a secret token from the OCI IAM identity domain's client ID and client secret. Use this, along with the domain URL, in Entra ID.
  3. Create an app in Entra ID and use the secret token and identity domain URL to specify the OCI IAM identity domain, and prove that it works by pushing users from Entra ID to OCI IAM.
  4. Assign the users and groups which you want to provision to OCI IAM to the Entra ID application.


  1. In addition, instructions on how to
     * Set users' federated status so that they're authenticated by the external identity provider.
     * Stop users getting notification emails when their account is created or updated.


[1. Create a Confidential Application](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm)
In this section, you configure Entra ID to act as the identity manager so that user accounts are synchronized from Entra ID to OCI IAM.
  1. In the identity domain, you are working in, select **Applications**.
  2. Select **Add Application** , and choose **Confidential Application** and select **Launch workflow**.
[![Confidential application](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app.png)
  3. Enter a name for the application, for example `Entra ID`, select **Next**.
  4. Under Client configuration, select **Configure this application as a client now**.
[![Configure application as a client](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-client-config.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-client-config.png)
  5. Under **Authorization** , check **Client credentials**. 
[![Configure application for client credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-client-config2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-client-config2.png)
  6. Under **Client type** select **Confidential**.
  7. Scroll down, and in the Token issuance policy section, set **Authorized resources** to **Specific**.
[![Token issuance policy](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/token-issuance-policy.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/token-issuance-policy.png)
  8. Select **Add app roles**.
  9. In the App Roles section, select **Add roles** , and in the Add app roles page select **User Administrator** then select **Add**.
[![Add app roles](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-add-roles.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-add-roles.png)
  10. Select **Next** , then **Finish**.
  11. On the application overview page, select **Activate** and confirm that you want to activate the application.
The confidential application is activated.


[2. Find the Domain URL and Generate a Secret Token](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm)
You need two pieces of information to use as part of the connection settings for the enterprise app you create in Entra ID:
  * The domain URL.
  * A secret token generated from the client ID and client secret.


  1. Return to the identity domain overview by selecting the identity domain name in the breadcrumbs. Select **Copy** next to the **Domain URL** in Domain information and save the URL to an app where you can edit it.
[![The domain information showing where the Domain URL information is.](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/domain-url.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/domain-url.png)
  2. In the confidential app in OCI IAM, select **OAuth configuration** under Resources.
  3. Scroll down, and find the **Client ID** and **Client secret** under General Information.
  4. Copy the client ID and store it
  5. Select **Show secret** and copy the secret and store it.
[![Client ID and client secret](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-client-id.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-client-id.png)
The secret token is the base64 encoding of `_<clientID>_:_<clientsecret>_`, or```
base64( _<clientID>_:_<clientsecret>_)
```

These examples show how to generate the secret token on Windows, Linux, or MacOS.
In a Windows environment, open CMD and use this powershell command to generate base64 encoding`[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes('client_id:secret'))`
In Linux, use```
echo -n <clientID>:<clientsecret> | base64 --wrap=0
```

In MacOS, use```
echo -n <clientID>:<clientsecret> | base64
```

The secret token is returned. For example```
echo -n 392357752347523923457437:3454-9853-7843-3554 | base64
Nk0NzUyMzcyMzQ1NzMTc0NzUyMzMtNTQzNC05ODc4LTUzNQ==
```

Make a note of the secret token value.


[3. Create OCI application on Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm)
Configure Entra ID to enable Entra ID to be the authoritative identity store to manage identities in IAM.
  1. In the browser, sign in to Microsoft Entra ID using the URL:```
https://portal.azure.com[](https://portal.azure.com)
```

  2. Select **Identity** then Applications.
  3. Select **Enterprise applications**.
[![Add an enterprise app](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ent-apps.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ent-apps.png)
  4. On the Enterprise applications page, select **New application** then **Oracle**.
  5. Select **Oracle Cloud Infrastructure Console**.
[![Choose Oracle Cloud Infrastructure Console](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-oci-app.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-oci-app.png)
  6. Enter a name, or accept the default of `Oracle Cloud Infrastructure Console`.
  7. Select **Create**.
[![Create OCI IAM console app](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-oci-app-create.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-oci-app-create.png)
  8. Choose **Provisioning** from the left menu under Manage.
[![Provisioning page for the enterprise application in Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-oci-prov-getstarted.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-oci-prov-getstarted.png)
  9. Select **Get started** , and change **Provisioning Mode** to **Automatic**.
  10. In **Tenant URL** , enter the OCI IAM Domain URL from [2. Find the Domain URL and Generate a Secret Token](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm#geenerate-secret-token) followed by `/admin/v1`. That is, the tenant URL is ```
https://_<domainURL>_/admin/v1
```

  11. Enter the secret token you generated in [2. Find the Domain URL and Generate a Secret Token](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm#geenerate-secret-token).
[![Enter admin credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-oci-prov-test.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-oci-prov-test.png)
  12. Select **Test Connection**. When this message appears, the connection is successful```
Testing connection to Oracle Cloud Infrastructure Console
The supplied credentials are authorized to enable provisioning
```

  13. Choose **Provisioning** from the left menu under Manage and select **Start provisioning**. The provisioning cycle starts, and the status of provisioning is displayed.


[4. Assign Users and Groups to the Entra ID Application](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm)
Assign the users which you want to provision to OCI IAM to the Entra ID application.
  1. In Entra ID, in the left menu select **Enterprise applications**. 
  2. Select the application you created earlier, `Oracle Cloud Infrastructure Console`.
  3. In the left menu under Manage, select **Users and groups**.
  4. In the Users and groups page, select **Add user/group**.
  5. In the Add Assignment page, on the left under Users and groups, select **None Selected**.
The Users and groups page opens.
  6. Select one or more users or groups from the list by selecting on them. The ones you select are listed under Selected items.
[![Users and Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-users-groups.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-users-groups.png)
  7. Select **Select**. The number of users and groups selected are shown on the Add Assignment page.
[![The number of users and groups you have selected are shown on the Add Assignment page.](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-users-groups2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-users-groups2.png)
  8. On the Add Assignment page, select **Assign**.
The Users and groups page now shows the users and groups you have chosen.
[![The users and group you have chosen are shown in the list of users and groups for the app.](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-users-groups2a.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-users-groups2a.png)
  9. Select Provisioning in the left menu to provision the groups and users. The provisioning log shows the status.
[![The provisioning log showing a status of successful.](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-users-groups3.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-users-groups3.png)
  10. When provisioning has been successful, the **Current cycle status** shows that the incremental cycle has completed and the number of users provisioned to OCI IAM is shown.
[![The status of provisioning is shown, along with the number of users provisioned to OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/lifecycle-prov-complete.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/lifecycle-prov-complete.png)
In OCI IAM, you can now see the users and groups provisioned from Entra ID.
[![The Entra ID users now provisioned in IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/sso-user1.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/sso-user1.png)
**Note** When you remove users from the Oracle Cloud Infrastructure console app on Entra ID, the user will only be deactivated on OCI IAM. 
[![The Entra ID groups now provisioned in IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-users-groups4.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-users-groups4.png)


[5. Additional Configurations for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm)
  * You can set users' federated status so that they're authenticated by the external identity provider.
  * You can disable notification emails being sent to the user when their account is created or updated.


[a. Setting Users' Federated Status](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm)
Federated users don't have credentials to sign in directly to OCI. Instead they're authenticated by the external identity provider. If you want users to use their federated accounts to sign in to OCI, set the federated attribute to true for those users.
To set the user's federated status:
  1. In the browser, sign in to Microsoft Entra ID using the URL:```
https://portal.azure.com[](https://portal.azure.com)
```

  2. Select **Identity** then Applications.
  3. Select **Enterprise applications**.
  4. Select the application you created earlier, `Oracle Cloud Infrastructure Console`.
  5. In the left menu under Manage, select **Provisioning** then select **Edit Provisioning**.
  6. In the Provisioning page, select **Mappings**.
  7. Under Mappings, select **Provision Entra ID Users**.
  8. Under Attribute Mappings, scroll down and select **Add New Mapping**.
[![Add New Mapping field under Attribute Mappings](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users2.png)
  9. In the Edit Attribute page:
     * For **Mapping type** , choose `Expression`.
     * For **Expression** , enter `CBool("true")`.
     * For **Target Attribute** , choose `urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User:isFederatedUser`.
[![Edit Attribute page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users3.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users3.png)
  10. Select **Ok**.
  11. In the Attribute Mapping page, select **Save**.


Now, when the users are provisioned from Entra ID to OCI, their federated status is set to true. You can see this in the user's profile page.
  * In the OCI Console, navigate to the identity domain you are using, select **Users** , and select the user to show the user information.
  * **Federated** is shown as `Yes`.
[![User information showing that the user is federated](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users4.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users4.png)


[b. Disable Notifications for Account Creation or Updates](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/01-config-azure-template.htm)
The bypass notification flag controls whether an email notification is sent after creating or updating a user account in OCI. If you don't want users to be notified that account have been created for them, then set the bypass notification flag to true.
To set the bypass notification flag:
  1. In the browser, sign in to Microsoft Entra ID using the URL:```
https://portal.azure.com[](https://portal.azure.com)
```

  2. Select **Identity** then Applications.
  3. Select **Enterprise applications**.
  4. Select the application you created earlier, `Oracle Cloud Infrastructure Console`.
  5. In the left menu under Manage, select **Provisioning** then select **Edit Provisioning**.
  6. In the Provisioning page, select **Mappings**.
  7. Under Mappings, select **Provision Entra ID Users**.
[![Provision Entra ID Users under Mappings, in the Provisioning Mode page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users.png)
  8. Under Attribute Mappings, scroll down and select **Add New Mapping**.
[![Add New Mapping field under Attribute Mappings](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users2.png)
  9. In the Edit Attribute page:
     * For **Mapping type** , choose `Expression`.
     * For **Expression** , enter `CBool("true")`.
     * For **Target Attribute** , choose `urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User:bypassNotification`.
[![Edit Attribute page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users7.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users7.png)
  10. Select **Ok**.
  11. In the Attribute Mapping page, select **Save**.


Was this article helpful?
YesNo

