Updated 2025-01-14
# Identity Lifecycle Management Between OCI and Okta
In this tutorial, you configure user life cycle management between Okta and OCI IAM, where Okta act as the authoritative identity store.
This 30 minute tutorial shows you how to provision users and groups from Okta to OCI IAM.
  1. Create a confidential application in OCI IAM.
  2. Get the identity domain URL and generate a secret token.
  3. Create an app in Okta.
  4. Update Okta's settings.
  5. Test that provisioning works between OCI IAM and Okta.
  6. In addition, instructions on how to
     * Set users' federated status so that they're authenticated by the external identity provider.
     * Stop users getting notification emails when their account is created or updated.


**Note** This tutorial is specific to IAM with Identity Domains.
[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm)
To perform this set of tutorials, you must have the following:
  * A paid Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier "Learn about Oracle Cloud Infrastructure's Free Tier.").
  * Identity domain administrator role for the OCI IAM identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
  * An Okta account with administrator privileges to configure provisioning.


You gather the additional information the additional information you need from the steps of the tutorial:
  * The OCI IAM domain URL.
  * The OCI IAM client ID and client secret.


[1. Create a Confidential Application in OCI](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm)
Create a confidential application in OCI IAM and activate it.
  1. Open a [supported browser ](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm) and enter the Console URL: 
`https://cloud.oracle.com[](https://cloud.oracle.com)`
  2. Enter your **Cloud Account Name** , also referred to as your tenancy name, and select **Next**.
  3. Sign in with your username and password.
  4. Open the navigation menu and select **Identity & Security**. Under Identity, select **Domains**.
  5. Select the identity domain in which you want to configure Okta provisioning and select **Applications**.
  6. Select **Add Application** , and choose **Confidential Application** and select **Launch workflow**.
[![Confidential application](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app.png)
  7. Enter a name for the confidential application, for example **OktaClient**. Select **Next**.
  8. Under Client configuration, select **Configure this application as a client now**.
  9. Under Authorization, select **Client Credentials**.
[![Configure application as a client](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-client-credent-config.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-client-credent-config.png)
  10. Scroll to the bottom, and select **Add app roles.**
  11. Under App roles select **Add roles** , and in the Add app roles page select **User Administrator** and select **Add**.
[![Add app roles](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-add-roles.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-add-roles.png)
  12. Select **Next** , then select **Finish**.
  13. In the application details page select **Activate** and confirm that you want to activate the new application.


[2. Find the OCI IAM GUID and Generate a Secret Token](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm)
You need two pieces of information to use as part of the connection settings for the Okta app you create later.
  1. Return to the identity domain overview by selecting the identity domain name in the breadcrumbs. Select **Copy** next to the **Domain URL** in Domain information and save the URL to an app where you can edit it.
[![The domain information showing where the Domain URL information is.](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/domain-url.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/domain-url.png)
The OCI IAM GUID is part of the domain URL:
`https://_<IdentityDomainID>_.identity.oraclecloud.com:443/fed/v1/idp/sso`
For example:`idcs-9ca4f92e3fba2a4f95a4c9772ff3278`
  2. In the confidential app in OCI IAM, select **OAuth configuration** under Resources.
  3. Scroll down, and under General Information make a note of the client ID and client secret.
  4. Scroll down, and find the **Client ID** and **Client secret** under General Information.
  5. Copy the client ID and store it
  6. Select **Show secret** and copy the secret and store it.
[![Client ID and client secret](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-client-id.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/confid-app-client-id.png)
The secret token is the base64 encoding of `_<clientID>_:_<clientsecret>_`, or```
base64( _<clientID>_:_<clientsecret>_)
```

These examples show how to generate the secret token on Windows and MacOS.
In a Windows environment, open CMD and use this powershell command to generate base64 encoding `[Convert]::ToBase64String([System.Text.Encoding]::Unicode.GetBytes('client_id:secret'))"`
In MacOS, use```
echo -n  _<clientID>_:_<clientsecret>_ | base64
```

The secret token is returned. For example```
echo -n 392357752347523923457437:3454-9853-7843-3554 | base64
Nk0NzUyMzcyMzQ1NzMTc0NzUyMzMtNTQzNC05ODc4LTUzNQ==
```

Make a note of the secret token value.


[3. Create an app in Okta](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm)
Create an application in Okta.
  1. In the browser, sign in to Okta using the URL:
`https://_<Okta-org>_-admin.okta.com`
Where _`<okta-org>`_is the prefix for your organization with Okta.
  2. In the menu on the left, select **Applications**.
If you already have an application which you created when you went through [SSO With OCI and Okta](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm#sso-get-started "In this tutorial, you set up Single Sign-On between OCI and Okta, where Okta acts as the identity provider \(IdP\) and OCI IAM is service provider \(SP\)."), you can use it. Select to open it and edit it, and go to [5. Change Okta Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm#okta-settings).
  3. Select **Browse App Catalog** and search for `Oracle Cloud`. Select **Oracle Cloud Infrastructure IAM** from the options available.
  4. Select **Add Integration**.
  5. Under General settings, enter a name for the application, for example `OCI IAM`, and select **Done**.


[5. Change Okta Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm)
Connect the Okta app to the OCI IAM confidential app using the domain URL and secret token from an earlier step.
  1. In the newly created application page, select the Sign On tab.
  2. In Settings, select **Edit**.
  3. Scroll down to Advanced Sign-on Settings.
  4. Enter the domain URL in **Oracle Cloud Infrastructure IAM GUID**.
  5. Select **Save**.
  6. Near the top of the page, select the Provisioning tab.
  7. Select **Configure API Integration**.
  8. Select **Enable API Integration**.
[![Enable API integration](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta_lcm_prov.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta_lcm_prov.png)
  9. Enter the the secret token value you copied earlier in **API Token**.
  10. Select **Test API Credentials**.
If you get an error message, check the values that you have entered and try again.
When you get a message `Oracle Cloud Infrastructure IAM was verified successfully!`, Okta has successfully connected to the OCI IAM SCIM endpoint.
  11. Select **Save**.


The Provisioning to App page opens, where you can create users, update user attributes, map attributes between OCI IAM and Okta.
[6. Test User and Group Provisioning](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm)
To test user and group provisioning for Okta:
  1. In the newly created application, choose the Assignments tab.
  2. Select **Assign** and select **Assign to People**.
  3. Search for the user to provision from Okta to OCI IAM.
Select **Assign** next to the user.
  4. Select **Save** , and then **Go Back**.
  5. Now provision Okta groups into OCI IAM. In the Assignments tab, select **Assign** and select **Assign to Groups**.
  6. Search for the groups to be provisioned to OCI IAM. Next to the group name, select **Assign**.
  7. Select **Done**.
  8. Now sign in to OCI:
    1. Open a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm) and enter the OCI Console URL: 
`https://cloud.oracle.com[](https://cloud.oracle.com)`.
    2. Enter your **Cloud Account Name** , also referred to as your tenancy name, and select **Next**.
    3. Select the identity domain in which Okta has been configured.
  9. Select **Users**.
  10. The user which was assigned to the OCI IAM application in Okta is now present in OCI IAM.
  11. Select **Groups**.
  12. The group which was assigned to the OCI IAM application in Okta is now present in OCI IAM.


[7. Additional Configurations for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm)
  * You can set users' federated status so that they're authenticated by the external identity provider.
  * You can disable notification emails being sent to the user when their account is created or updated.


[a. Setting Users' Federated Status](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm)
Federated users don't have credentials to sign in directly to OCI. Instead they're authenticated by the external identity provider. If you want users to use their federated accounts to sign in to OCI, set the federated attribute to true for those users.
To set the user's federated status:
  1. In the browser, sign in to Okta using the URL:
`https://_<Okta-org>_-admin.okta.com`
Where _`<okta-org>`_is the prefix for your organization with Okta.
  2. In the menu on the left, select **Applications**.
  3. Select the application you created earlier, `OCI IAM`.
  4. Scroll down to the Attribute Mappings section.
  5. Select **Go to Profile Editor**.
  6. Under Attributes, select **Add Attributes**.
  7. In the Add Attribute page:
     * For **Data Type** , choose `Boolean`.
     * For **Display Name** enter `isFederatedUser`.
     * For **Variable Name** enter `isFederatedUser`.
**Note** The external name is automatically populated by the value of the variable name.
     * For **External namespace** , enter `urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User`.
     * Under **Scope** , check `User personal`.
[![Add attribute page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users.png)
  8. Navigate back to Okta's Application page and select the `OCI IAM` application.
  9. Select **Provisioning**.
  10. Scroll down to Attributes Mapping and select **Show Unmapped Attributes**.
  11. Locate `isFederatedUser` attribute and select the edit button next to it.
  12. In the attribute page:
     * For **Attribute value** choose `Expression`.
     * In the box below, enter `true`.
     * For **Apply on** , choose **Create and update**.
[![Attribute page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users2.png)
  13. Select **Save**.
[![Attribute values showing federation](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users7.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users7.png)


Now, when the users are provisioned from Okta to OCI, their federated status is set to true. You can see this in the user's profile page in OCI.
  * In the OCI Console, navigate to the identity domain you are using, select **Users** , and select the user to show the user information.
  * **Federated** is shown as `Yes`.
[![User information showing that the user is federated](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users4.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-prov-users4.png)


[b. Disable Notifications for Account Creation or Updates](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm)
The bypass notification flag controls whether an email notification is sent after creating or updating a user account in OCI. If you don't want users to be notified that account have been created for them, then set the bypass notification flag to true.
To set the bypass notification flag:
  1. In the browser, sign in to Okta using the URL:
`https://_<Okta-org>_-admin.okta.com`
Where _`<okta-org>`_is the prefix for your organization with Okta.
  2. In the menu on the left, select **Applications**.
  3. Select the application you created earlier, `OCI IAM`.
  4. Scroll down to the Attribute Mappings section.
  5. Under Attributes, select **Add Attributes**.
  6. In the Add Attribute page:
     * For **Data Type** , choose `Boolean`.
     * For **Display Name** enter `bypassNotification`.
     * For **Variable Name** enter `bypassNotification`.
**Note** The external name is automatically populated by the value of the variable name.
     * For **External namespace** , enter `urn:ietf:params:scim:schemas:oracle:idcs:extension:user:User`.
     * Under **Scope** , check `User personal`.
[![Add Attribute page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users4.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users4.png)
  7. Navigate back to Okta's Application page and select the `OCI IAM` application.
  8. Select **Provisioning**.
  9. Scroll down to Attributes Mapping and select **Show Unmapped Attributes**.
  10. Locate `bypassNotification` attribute and select the edit button next to it.
  11. In the attribute page:
     * For **Attribute value** choose `Expression`.
     * In the box below, enter `true`.
     * For **Apply on** , choose **Create and update**.
[![Attribute page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users5.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users5.png)
  12. Select **Save**.
[![Attribute values showing bypass notification](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users6.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-prov-users6.png)


[What's Next](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/lifecycle_okta/okta-lifecycle.htm)
Congratulations! You have successfully set up user lifecycle management between Okta and OCI.
To explore more information about development with Oracle products, check out these sites:
  * [Oracle Developers Portal](https://developer.oracle.com/)
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)


Was this article helpful?
YesNo

