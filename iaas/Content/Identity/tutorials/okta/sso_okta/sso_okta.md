Updated 2025-01-14
# SSO With OCI and Okta
In this tutorial, you set up Single Sign-On between OCI and Okta, where Okta acts as the identity provider (IdP) and OCI IAM is service provider (SP).
This 15 minute tutorial shows you how to set up Okta as an IdP, with OCI IAM acting as SP. By setting up federation between Okta and OCI IAM, you enable users' access to services and applications in OCI IAM using user credentials that Okta authenticates.
  1. First, gather the information needed from OCI IAM.
  2. Configure Okta as an IdP for OCI IAM.
  3. Configure OCI IAM so Okta acts as IdP.
  4. Create IdP policies in OCI IAM.
  5. Test that federated authentication works between OCI IAM and Okta.


[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm)
To perform either of these tutorials, you must have the following:
  * A paid Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier "Learn about Oracle Cloud Infrastructure's Free Tier.").
  * Identity domain administrator role for the OCI IAM identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
  * An Okta account with administrator privileges to configure provisioning.


You gather the additional information you need from the steps of each tutorial:
  * Get the OCI IdP metadata and the signing certificate for the identity domain.
  * Get the identity domain's signing certificate.


[1. Get the OCI Identity Provider Metadata and the Domain URL](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm)
You need the IdP SAML metadata from your OCI IAM identity domain to import into the Okta application you create. OCI IAM provides a direct URL to download the metadata of the identity domain you are using. Okta uses the OCI domain URL to connect to OCI IAM.
  1. Open a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm) and enter the Console URL: 
`https://cloud.oracle.com[](https://cloud.oracle.com)`.
  2. Enter your **Cloud Account Name** , also referred to as your tenancy name, and select **Next**.
  3. Select the identity domain to sign in to. This is the identity domain that is used to configure SSO, for example `Default`.
  4. Sign in with your username and password.
  5. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  6. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **Identity providers**.
  7. Select **Export SAML metadata**.
[![Download SAML metadata](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta_saml_metadata.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta_saml_metadata.png)
  8. Select the **Metadata file** option, and select **Download XML**.
[![Download the XML file](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta_saml_metadata2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta_saml_metadata2.png)
  9. Rename the downloaded XML file to `OCIMetadata.xml`.
  10. Return to the identity domain overview by selecting the identity domain name in the breadcrumb navigation trail. Select **Copy** next to the **Domain URL** in Domain information and save the URL. This is the OCI IAM domain URL which you will use later.
[![The domain information showing where the Domain URL information is.](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/domain-url.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/domain-url.png)


[2. Create an App in Okta](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm)
Create an app in Okta, and make a note of values you'll need later.
  1. In the browser, sign in to Okta using the URL:```
https://_<OktaOrg>_-admin.okta.com
```

where` _<OktaOrg>_`is the prefix for your organization with Okta.
  2. In the left menu, select **Security** and choose **Applications** and then select **Browse App****Catalog**.
  3. Search for `Oracle Cloud` and select **Oracle Cloud Infrastructure IAM** from the options available.
  4. Select **Add Integration**.
  5. Under General settings, enter a name for the application, for example `OCI IAM`, and select **Done**.
  6. In the application details page for your new application, select the Sign On tab, and under SAML Signing Certificates select **View SAML setup instructions**.
  7. On the View SAML setup instructions page, make a note of the following:
     * Entity ID
     * SingleLogoutService URL
     * SingleSignOnService URL
  8. Download and save the certificate, with a file extension of`.pem`.


[3. Create Okta as an IdP in OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm)
Create an IdP for Okta on the OCI Console.
  1. In the OCI Console in the domain you are working in, select **Security** and then **Identity providers**.
  2. Select **Add IdP** , then select **Add SAML IdP**.
  3. Enter a name for the SAML IdP, for example `Okta`. Select **Next**.
  4. On the Exchange metadata page, ensure that **Enter IdP metadata** is selected.
  5. Enter the following from step 8 in [2. Create an App in Okta](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm#create-app-in-okta):
     * For **Identity provider issuer URI** : Enter the Enter ID.
     * For **SSO service URL** : Enter the SingleSignOnService URL.
     * For **SSO service binding** : Select `POST`.
     * For **Upload identity provider signing certificate** : Use the `.pem` file of the Okta certification.
[![Exchange metadata page of create SAML identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-as-idp-in-iam.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-as-idp-in-iam.png)
Further down the page, ensure that **Enable Global logout** is selected, and enter the following.
     * For **IDP Logout Request URL** : Enter the SingleLogoutService URL.
     * For **IDP Logout Response URL** : eEnter tbhe SingleLogoutService URL.
     * Ensure that the **Logout binding** is set to POST.
[![additional configuration](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-as-idp-in-iam2.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/okta-as-idp-in-iam2.png)
  6. Select **Next**.
  7. On the Map attributes page:
     * For **Requested NameId format** , choose `Email address`.
     * For **Identity provider user attribute** : Choose SAML assertion Name ID.
     * For **Identity Domain user attribute** : Choose Primary email address.
  8. Select **Next**.
  9. Review, and select **Create IDP**.
  10. On the What's Next page, select **Activate** , then select **Add to IdP policy**.
  11. Select **Default Identity Provider Policy** to open it, then select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the rule and select **Edit IdP rule**.
  12. Select in **Assign identity providers** and then select **Okta** to add it to the list.
  13. Select **Save changes**.
  14. Download the SP Certificate:
     * In the OCI Console in the domain you are working in, select **Security** and then **Identity providers**.
     * Select **Okta**.
     * On the Okta IdP page, select **Service Provider metadata**.
     * Select **Download** next to Service Provider signing certificate to download the SP signing certificate and save it.


[4. Configure Okta](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm)
  1. In the Okta console, select Application then select the new application `OCI IAM`.
  2. Go to the Sign On tab and select **Edit**.
  3. Select **Enable Single Logout**.
  4. Browse to the certificate you downloaded from the OCI IAM Console in the previous step, and select **Upload**.
  5. Scroll down to Advance Sign-on Settings.
  6. Enter the following:
     * **Oracle Cloud Infrastructure IAM GUID** : Enter the OCI IAM domain URL from step 10 in [1. Get the OCI Identity Provider Metadata and the Domain URL](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm#get-metadata).
     * Set the **Application username format** to `Email`.
  7. Select **Save**.
  8. Go to the Assignments tab and assign users who you want to have access to this application.
  9. Select **Next**.


[5. Test Single Sign On](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm)
  1. Enter the Console URL:
`https://cloud.oracle.com[](https://cloud.oracle.com)`
  2. Enter your **Cloud Account Name** , also referred to as your tenancy name, and select **Next**.
  3. Sign in with your username and password.
  4. Select the domain that you configured Okta IdP for.
  5. On the sign-in page, select the Okta icon.
  6. Enter your Okta credentials. You are signed in to the OCI Console.


[What's Next](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/okta/sso_okta/sso_okta.htm)
Congratulations! You have successfully set up an SSO between Okta and OCI IAM in two different ways.
To explore more information about development with Oracle products, check out these sites:
  * [Oracle Developers Portal](https://developer.oracle.com/)
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)


Was this article helpful?
YesNo

