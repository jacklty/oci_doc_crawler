Updated 2025-01-14
# SSO Between OCI and ADFS
In this tutorial, configure SSO between the OCI IAM and ADFS, using ADFS as the identity provider (IdP).
This 30 minute tutorial shows you how to integrate OCI IAM, acting as a service provider (SP), with ADFS, acting as an IdP. By setting up federation between ADFS and OCI IAM, you enable users' access to services and applications in OCI using user credentials that ADFS authenticates.
This tutorial covers setting up ADFS as an IdP for OCI IAM.
OCI IAM provides integration with SAML 2.0 IdPs. This integration:
  * Works with federated Single Sign-On (SSO) solutions that are compatible with SAML 2.0 as an IdP, such as ADFS.
  * Lets users sign in to OCI using their ADFS credentials.
  * Lets users sign in to end applications.


  1. First, download the metadata from the OCI IAM identity domain.
  2. In the next few steps you create and configure a relying party in ADFS.
  3. In ADFS, set up SSO with OCI IAM using the metadata.
  4. In ADFS, edit the Attributes and Claims so that the email name is used as the identifier for users.
  5. In ADFS, add a user to the app.
  6. For the next steps, you return to the identity domain to finish the setup and configuration. In OCI IAM, update the default IdP policy to add ADFS.
  7. Test that federated authentication works between OCI IAM and ADFS.


**Note** This tutorial is specific to IAM with Identity Domains.
[Before You Begin](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/sso_adfs/adfs_sso.htm)
To perform this tutorial, you must have the following:
  * A paid Oracle Cloud Infrastructure (OCI) account, or an OCI trial account. See [Oracle Cloud Infrastructure Free Tier](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier.htm#Oracle_Cloud_Infrastructure_Free_Tier "Learn about Oracle Cloud Infrastructure's Free Tier.").
  * Identity domain administrator role for the OCI IAM identity domain. See [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
  * An on-premises ADFS installation. 
**Note** This tutorial describes using the ADFS software provided with Microsoft Windows Server 2016 R2.
  * In addition, you must verify that the same user exists in OCI and ADFS, and that ADFS is working.


[Create the Same User in Both Systems](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/sso_adfs/adfs_sso.htm)
Ensure that a user with the same email address exists in both systems.
For SAML SSO to work between ADFS and OCI IAM, there must be a user with the same email address in both the Microsoft Active Directory domain and the OCI IAM identity domain. In this task, you confirm that such a user that exists on both systems.
  1. Open the Microsoft Active Directory Users and Computers utility. In Windows 2016 Server, select **Server Manager** , then **Tools** , and then **Active Directory Users and Computers**.
  2. In the **Employees** folder, double-click the user you want to use. Make a note of the user's email address.```
ADFS USER(adfsuser01@gmail.com)
```

[![User in Active Directory Users and Computers utility](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-check-user.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-check-user.png)
**Note**
If more than one user in the OCI IAM domain has the same email address then SAML SSO fails because because it's impossible to determine which user is to be signed in.
     * The user's email address is used to link the user signed in to ADFS with the same user's entry in OCI IAM.
     * If you don't have an ADFS user to test the connection, you can create one.
  3. In a browser, enter the Console URL to access the OCI IAM Console:
`https://cloud.oracle.com[](https://cloud.oracle.com)`
  4. Enter your **Cloud Account Name** , also referred to as the tenancy name, and select **Next**.
  5. Sign in with your username and password.
  6. Select the domain that you are going to use.
  7. Select **Users**.
  8. In the search field, enter the email address you recorded from Microsoft Active Directory.
  9. In the search results, confirm that a user exists with the same email address as the user in the Microsoft Active Directory.
**Note** If the user doesn't exist in OCI IAM, select **Add** and create the user with the same email address as in Microsoft Active Directory.


[Verify ADFS is Running](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/sso_adfs/adfs_sso.htm)
Verify that ADFS is running, and that you can successfully challenge the user for sign in.
  1. In the browser, sign in to ADFS using the URL: ```
https://_adfs.example.com_/adfs/ls/IdpInitiatedSignOnPage
```
where` _adfs.example.com_`is your ADFS hostname.
  2. If you need to, select **Sign in to this site**. Select **Sign In**.
  3. Enter the Microsoft Active Directory credentials for a user that exists on both ADFS and OCI IAM (in this example, `adfsuser01`) and select **Sign In**.
[![ADFS sign in page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-signin.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-signin.png)
  4. You'll see the message `You are signed in`.
[![ADFS confirmation that you are signed in](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-add-signed-in.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-add-signed-in.png)


[1. Create ADFS as IdP in OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/sso_adfs/adfs_sso.htm)
  1. In the browser, sign in to ADFS using the URL: ```
https://_adfs.example.com_/FederationMetadata/2007-06/FederationMetadata.xml
```
where` _adfs.example.com_`is your ADFS hostname.
  2. Save the `FederationMetadata.xml` file. You will use this file to register ADFS with OCI IAM.
  3. In the OCI Console navigate to the domain you want to work in. You might need to change the compartment to find the domain that you want. Select **Security** and then **Identity providers**.
  4. Select **Add IdP** , then select **Add SAML IdP**.
  5. Enter a name for the SAML IdP, for example `ADFS_IdP`. Select **Next**.
  6. Select **Enter IdP metadata**.
  7. Download the OCI IAM Service Provider (SP) metadata by selecting **Export SAML metadata**.
    1. On the Export SAML metadata page under **Metadata with self-signed certificates** , select **Download XML**.
**Note** Use metadata with self-signed certificates when the identity provider performs CRL or OCSP checks on certificates issued by a CA. In this tutorial, ADFS does this during certificate path validation.
    2. Save the file to an appropriate location.
    3. Transfer the `Metadata.xml` file to the Windows Server where ADFS is managed. You will use this file to register the OCI IAM domain with ADFS.
[![Export SAML metadata for OCI IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-metadata.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-metadata.png)
  8. Close the Export SAML metadata page.
  9. Select **Import IdP metadata** , and then select **Upload**. Select the `FederationMetadata.xml` file that you saved earlier from ADFS, select **Open** , and then select **Next**.
  10. In Map user identity, set the following
     * Under **Requested NameID format** , select `Email address`.
     * Under **Identity provider user attribute** , select `SAML assertion Name ID`.
     * Under **Identity domain user attribute** , select `Primary email address`.
[![SAML identity provider attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs_map_user_id.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs_map_user_id.png)
  11. Select **Next**.
  12. Under Review and Create verify the configurations, and select **Create IdP**.
  13. Select **Activate**.
  14. Select **Add to IdP Policy Rule**. Adding the ADFS IdP to an IdP Policy allows it to be displayed on the OCI IAM sign-in screen.
  15. Select **Default Identity Provider Policy** to open it, then select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) for the rule and select **Edit IdP rule**.
[![The context menu showing "Edit IdP Rule"](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/edit-idp-rule.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/edit-idp-rule.png)
  16. Select **Assign identity providers** and then select **ADFS_IdP** to add it to the list.
[![adding ADFS as an identity provider in the default IdP rule](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-iam_policy.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-iam_policy.png)
  17. Select **Save Changes**.


Now, ADFS is registered as identity provider in OCI IAM.
Next, you register OCI IAM as a trusted relying party in ADFS.
[2. Register OCI IAM as a Trusted Relying Party](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/sso_adfs/adfs_sso.htm)
First, register OCI IAM as the relying party with ADFS. Then, configure claim rules for OCI IAM as a relying party.
**Register the Relying Party**
  1. Open the ADFS management utility. For example, in Windows 2016 Server Manager utility, select **Tools** , then select **Microsoft Active Directory Federation Services Management**.
  2. Select **Action** , then select **Add Relying Party Trust**.
  3. In the Add Relying Party Trust Wizard window, select **Start**.
[![Add relying party trust wizard in ADFS](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-add-relying-party.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-add-relying-party.png)
  4. Select Import data about the relying party from a file, and then select **Browse**.
[![Select data source](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-select-data-source.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-select-data-source.png)
  5. Select `Metadata.xml` which you downloaded earlier from OCI IAM, and select **Next**.
  6. Enter a display name, for example `OCI IAM`, and optionally enter a description under **Notes**. Select **Next**.
[![Setting the display name](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-relying-metadata.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-relying-metadata.png)
  7. Proceed with the default options until you reach the Finish step, and then select **Close**. The Edit Claim Rules window opens.
[![Edit claims window](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-edit-claim-rules.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-edit-claim-rules.png)


**Configure Claim Rules**
Claim rules define the information about a signed-in user sent from ADFS to OCI IAM after successful authentication. Here, you define two claim rules for OCI IAM to act as a relying party:
  * **Email** : This rule indicates that the user's email address is sent to OCI IAM in the SAML assertion.
  * **Name ID** : This rule indicates that the result of the Email rule is sent to OCI IAM in the Subject `NameID` element of the SAML assertion.


  1. In the Edit Claim Rules window, select **Add Rule**.
  2. Select **Send LDAP Attributes as Claims** as claim rule template, and then select **Next**
  3. In the Choose Rule Type page, provide the following information for the Email rule:
     * **Claim rule name** : `Email`
     * **Attribute store** : `Active Directory`
     * **Mapping of LDAP attributes to outgoing claim types** : 
       * **LDAP Attribute** : `E-Mail-Addresses`
       * **Outgoing Claim Type** : `E-Mail Address`
[![Choose Rule Type page of Add transform claim rule wizard.](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-edit-claims.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-edit-claims.png)
  4. Select **Finish**.
  5. In the Edit Claim Rules window, select **Add Rule** to add the second claim rule.
  6. Select **Transform an Incoming Claim** as claim rule template, then select **Next**.
  7. In the Choose Rule Type page, provide the following information for the Name ID rule:
     * **Claim rule name** : `Name ID`
     * **Incoming claim type** : `E-Mail Address`
     * **Outgoing claim type** : `Name ID`
     * **Outgoing name ID format** : `Email`
[![Choose Rule Type page of Add transform claim rule wizard.](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-config-claim.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-config-claim.png)
  8. Select **Finish**.
  9. In the Edit Claim Rules for Oracle Cloud window, check that the Email and Name ID rules have been created.
[![Confirm that both claims are present](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-confirm-claim-rules.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-confirm-claim-rules.png)


Now, ADFS and OCI IAM have enough information to establish SSO and you can test the integration. 
[3. Test SSO Between ADFS and OCI](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/sso_adfs/adfs_sso.htm)
In this task, you test the authentication between OCI IAM and ADFS. If the authentication is successful, you enable the identity provider for end-users.
  1. Restart your browser, and enter the Console URL to access the OCI IAM Console:
`https://cloud.oracle.com[](https://cloud.oracle.com)`
  2. Enter the **Cloud Account Name** , also referred to as the tenancy name, and select **Next**.
  3. Sign in with your username and password.
  4. Select the domain that you configured the ADFS IdP for.
  5. Select **Security** and then **Identity Providers**.
  6. Select the ADFS IdP entry.
  7. On the details page for the IdP, select **More actions** then select **Test login**.
  8. Scroll to the bottom and select **Test Login**.
  9. On the ADFS sign in page, sign in with a user that exists on ADFS and OCI IAM.
[![ADFS sign in page](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-test.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-test.png)
  10. You see the confirmation message **Your connection is successful**.
[![Confirmation message](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-test-confirm.png)](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/images/adfs-test-confirm.png)


[What's Next](https://docs.oracle.com/en-us/iaas/Content/Identity/tutorials/adfs/sso_adfs/adfs_sso.htm)
Congratulations! You have successfully set up SSO between ADFS and OCI IAM.
To explore more information about development with Oracle products, check out these sites:
  * [Oracle Developers Portal](https://developer.oracle.com/)
  * [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/)


Was this article helpful?
YesNo

