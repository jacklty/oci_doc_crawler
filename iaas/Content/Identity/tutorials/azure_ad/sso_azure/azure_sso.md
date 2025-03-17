Updated 2025-01-14
# SSO Between OCI and Microsoft Entra ID
In this tutorial, configure SSO between the OCI IAM and Microsoft Entra ID, using Entra ID as the identity provider (IdP).
This 30 minute tutorial shows you how to integrate OCI IAM, acting as a service provider (SP), with Entra ID, acting as an IdP. By setting up federation between Entra ID and OCI IAM, you enable users' access to services and applications in OCI using user credentials that Entra ID authenticates.
This tutorial covers setting up Entra ID as an IdP for OCI IAM.
  1. First, download the metadata from the OCI IAM identity domain.
  2. In the next few steps you create and configure an app in Entra ID.
  3. In Entra ID, set up SSO with OCI IAM using the metadata.
  4. In Entra ID, edit the Attributes and Claims so that the email name is used as the identifier for users.
  5. In Entra ID, add a user to the app.
  6. For the next steps, you return to your identity domain to finish the setup and configuration.In OCI IAM, update the default IdP policy to add Entra ID.
  7. Test that federated authentication works between OCI IAM and Entra ID.


**Note** This tutorial is specific to IAM with Identity Domains.
[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm)
To perform this tutorial, you must have the following:
  * A paid Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier "Learn about Oracle Cloud Infrastructure's Free Tier.").
  * Identity domain administrator role for the OCI IAM identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
  * An Entra ID account with one of the following Entra ID roles:
    * Global Administrator
    * Cloud Application Administrator
    * Application Administrator


**Note** The user used for Single Sign On (SSO), must exist in both OCI IAM and Entra ID for SSO to work. After you complete this SSO tutorial, there is another tutorial, [Identity Lifecycle Management Between OCI IAM and Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/azure_lifecycle.htm#azure-lifecycle "Configure provisioning between OCI IAM and Entra ID using three different methods."). This other tutorial guides you through how to provision user accounts from Entra ID to OCI IAM or from OCI IAM to Entra ID.
[1. Get the Service Provider Metadata from OCI IAM ](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm)
You need the SP metadata from your OCI IAM identity domain to import into the SAML Entra ID application you create. OCI IAM provides a direct URL to download the metadata of the identity domain you are using. To download the metadata, follow these steps.
  1. Open a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm) and enter the Console URL: 
`https://cloud.oracle.com[](https://cloud.oracle.com)`.
  2. Enter your **Cloud Account Name** , also referred to as the tenancy name, and select **Next**.
  3. Select the identity domain to sign in to. This is the identity domain that is used to configure SSO, for example `Default`.
  4. Sign in with your username and password.
  5. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  6. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Settings** and then **Domain settings**.
  7. Under Access signing certificate, check **Configure client access**.
This lets a client to access the signing certification for the identity domain without signing in to the domain.
  8. Select **Save changes.**
[![Configure client access on the Domain Settings page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/config-client-access.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/config-client-access.png)
  9. Return to the identity domain overview by selecting the identity domain name in the breadcrumb navigation trail. Select **Copy** next to the **Domain URL** in Domain information and save the URL to an app where you can edit it.
[![The domain information showing where the Domain URL information is.](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/domain-url.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/domain-url.png)
  10. In a new browser tab, paste the URL you copied and add `/fed/v1/metadata` to the end.
For example,
```
https://idcs-_<unique_ID>_.identity.oraclecloud.com:443/fed/v1/metadata
```

  11. The metadata for the identity domain is displayed in the browser. Save it as an XML file with the name `OCIMetadata.xml`.


[2. Create an Entra ID Enterprise Application](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm)
For the next few steps, you are working in Entra ID.
Create a SAML enterprise application in Entra ID.
  1. In the browser, sign in to Microsoft Entra using the URL:```
https://entra.microsoft.com[](https://entra.microsoft.com)
```

  2. Select **Identity** then **Applications**.
  3. Select **Enterprise applications** then **New application**.
  4. In **Search applications** , type `Oracle Cloud Infrastructure Console`.
  5. Select the **Oracle Cloud Infrastructure Console by Oracle Corporation** tile.
  6. Enter a name for the app, for example, `Oracle IAM`, and select **Create**.
The enterprise app is created in Entra ID.


[3. Set Up Single Sign-On for the Entra ID Enterprise App](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm)
Set up SSO for the Entra ID SAML application, and download the Entra ID SAML metadata. In this section, you use the OCI IAM SP metadata file you saved in [1. Get the Service Provider Metadata from OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm#get-metadata).
  1. In the Getting Started page, select **Get started** under **Set up single sign on**.
  2. Select **SAML** , then select **Upload metadata file** (button at the top of the page). Browse to the XML file containing the OCI identity domain metadata, `OCIMetadata.xml`.
  3. Provide the Sign on URL. For example ```
https://idcs-_<domain_ID>_.identity.oraclecloud.com/ui/v1/myconsole
```

  4. Select **Save**.
  5. Close the Upload metadata file page from the X in the upper right. If you are asked whether you want to test the application now, choose not to because you will test the application later in this tutorial.
  6. In the Set up Single Sign-On with SAML page, scroll down and in SAML Signing Certificate, select **Download** next to **Federation Metadata XML**.
  7. When prompted, choose **Save File**. The metadata is automatically saved with the default filename `_<your_enterprise_app_name>_.xml`. For example,`OracleIAM.xml`.
[![The Entra ID SAML-based SSO page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-sso.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-sso.png)


[4. Edit Attributes and Claims](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm)
Edit the Attributes and Claims in your new Entra ID SAML app so that the user email address is used as the user name.
  1. In the enterprise application, from the menu on the left, select **Single sign-on**.
  2. In Attributes and Claims, select **Edit**.
  3. Select the required claim: ```
Unique User Identifier (Name ID) = user.mail [nameid-format:emailAddress]
```

  4. In the Manage claim page, change the Source attribute from `user.userprinciplename` to `user.mail`.
[![Entra ID attributes and claims](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-attrib.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure-ad-attrib.png)
  5. Select **Save**.


**Additional Entra ID Configurations**
In Entra ID, you can filter groups based on the group name, or `sAMAccountName`, attribute.
For example, suppose only the `Administrators` group needs to be sent over using SAML:
  1. Select the group claim.
  2. In Group Claims, expand **Advanced options**.
  3. Select **Filter Groups**.
     * For **Attribute to match** , select `Display Name`.
     * For **Match with** , select `contains`.
     * For **String** , provide the name of the group, for example, `Administrators`.
[![Filter for groups](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure_filter_groups.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/azure_filter_groups.png)


Using this option, even if the user in the administrator group is part of other groups, Entra ID only sends the Administrators group in SAML.
**Note** This helps organisations to send only the required groups to OCI IAM from Entra ID.
[5. Add a Test User to the Entra ID Application](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm)
Create a test user for your Entra ID application. Later, this user can use their Entra ID credentials to sign in to the OCI Console.
  1. In the Microsoft Entra admin center, select **Identity** then **Users** , then **All users**.
  2. Select **New user** then **Create new user** , and create a user and enter their email ID.
**Note** Ensure that you use the details of a user present in OCI IAM with the same email id.
  3. Return to the enterprise application menu. Under Getting Started, select **Assign users and groups**. Alternatively, select **Users** from under Manage on the menu on the left.
  4. Select **Add user/group** , and on the next page under Users select **None Selected**.
  5. In the Users page, select the test user you created. As you select it, the user appears under **Selected items**. Select **Select**.
  6. Back on the Add Assignment page, select **Assign**.


[6. Enable Entra ID as IdP for OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm)
For these steps, you are working in OCI IAM.
Add Entra ID as an IdP for OCI IAM. In this section, you use the Entra ID metadata file you saved in [3. Set Up Single Sign-On for the Entra ID Enterprise App](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm#azure-app), for example, `Oracle IAM.xml`.
  1. In the OCI Console in the domain you are working in, select **Security** and then **Identity providers**.
  2. Select **Add IdP** , then select **Add SAML IdP**.
  3. Enter a name for the SAML IdP, for example `Entra ID`. Select **Next**.
  4. Ensure that **Import identity provider metadata** is selected, and browse and select, or drag and drop the Entra ID metadata XML file, `Oracle IAM.xml` into **Identity provider metadata**. This is the metadata file you saved when you worked through [3. Set Up Single Sign-On for the Entra ID Enterprise App](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm#azure-app). Select **Next**.
  5. In Map user identity, set the following
     * Under **Requested NameID format** , select `Email address`.
     * Under **Identity provider user attribute** , select `SAML assertion Name` ID.
     * Under **Identity domain user attribute** , select `Primary email address`.
[![SAML identity provider attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/add-saml-attrib.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/add-saml-attrib.png)
  6. Select **Next**.
  7. Under Review and Create, verify the configurations and select **Create IdP**.
  8. Select **Activate**.
  9. Select **Add to IdP Policy Rule**.
  10. Select **Default Identity Provider Policy** to open it, select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) and select **Edit IdP rule**.
[![The context menu showing "Edit IdP Rule"](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/edit-idp-rule.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/edit-idp-rule.png)
  11. Select **Assign identity providers** and then select **Entra ID** to add it to the list.
[![adding Entra ID as an identity provider in the default IdP rule](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/iam_policy.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/iam_policy.png)
  12. Select **Save Changes**.


[7. Test SSO Between Entra ID and OCI](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm)
In this section, you can test that federated authentication works between OCI IAM and Entra ID.
**Note** For this to work, the user used for SSO must be present in both OCI IAM and Entra ID. Also, the user must be assigned to the OCI IAM application created in Entra ID.
There are two ways to do this:
  * You can manually create a test user in both OCI IAM and Entra ID.
  * However, if you want to test with a real time user, you should set up provisioning between Entra ID and OCI IAM by following the steps in the tutorial, [Identity Lifecycle Management Between OCI IAM and Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/azure_lifecycle.htm#azure-lifecycle "Configure provisioning between OCI IAM and Entra ID using three different methods.").


If you haven't set up users to test this tutorial, you see the following error```
Sorry, but we're having trouble signing you in.
AADSTS50105: Your administrator has configured 
the application application-name (' _<unique_ID>_')
to block users unless they are specifically granted
('assigned') access to the application.
```

Test the SP initiated SSO.
  1. Open a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm) and enter the OCI Console URL: 
`https://cloud.oracle.com[](https://cloud.oracle.com)`.
  2. Enter your **Cloud Account Name** , also referred to as your tenancy name, and select **Next**.
  3. Select the identity domain in which Entra ID federation has been configured.
  4. On the sign-in page, you can see an option to sign in with Entra ID.
[![OCI IAM sign-in page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/sso-iam.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/sso-iam.png)
  5. Select Entra ID. You are redirected to the Microsoft login page.
  6. Provide your Entra ID credentials.
  7. On successful authentication, you are logged in to the OCI Console.


[What's Next](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/sso_azure/azure_sso.htm)
Congratulations! You have successfully set up SSO between Entra ID and OCI IAM.
If you already had a user created in Entra ID and assigned to the application, that had been provisioned to OCI IAM, you were able to test that federation authentication works between OCI IAM and Entra ID. If you didn't have such a user, you can create one by following one of the [Identity Lifecycle Management Between OCI IAM and Entra ID](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/azure_ad/lifecycle_azure/azure_lifecycle.htm#azure-lifecycle "Configure provisioning between OCI IAM and Entra ID using three different methods.") tutorials.
To explore more information about development with Oracle products, check out these sites:
  * [Oracle Developers Portal](https://developer.oracle.com/)
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)


Was this article helpful?
YesNo

