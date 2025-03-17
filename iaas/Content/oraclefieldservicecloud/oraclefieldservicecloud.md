Updated 2023-12-12
# Oracle Field Service Cloud
This document describes how to configure IAM with identity domains to provide Single Sign-On (SSO) using SAML and provisioning for Oracle Field Service Cloud.
## Before You Begin 🔗 
### About Oracle Field Service Cloud 🔗 
Oracle Field Service Cloud is built on time-based, self-learning, and predictive technology, empowering customers to solve business problems while evolving their field service organization.
### What Do You Need? 🔗 
  * The Oracle Field Service Cloud application with a minimum supported version of 17.2 Service Update 8 or later.
  * An identity domain account with authorization rights to manage apps and users (Identity Domain Administrator or Application Administrator).
  * An Oracle Field Service Cloud account with administrative rights to configure federated authentication and Oracle Field Service Cloud Login URL.
  * An Oracle Field Service Cloud resource (pending-assignment) to provision user accounts in Oracle Field Service Cloud through an identity domain.
  * Identity Provider metadata. Use the following URL to access the metadata: `https://<domainURL>/fed/v1/metadata`


## Configuring SSO for Oracle Field Service Cloud 🔗 
Use this section to configure an Identity Provider for Oracle Field Service Cloud.
### Configuring an Identity Provider 🔗 
Use this section to create an identity provider.
#### Creating the SSO Login Policy 🔗 
  1. Log in as an administrator using the login URL format: `<https://instance_name.fs.ocs.oraclecloud.com/>`.
  2. In the main page, click **Configuration**. The Configuration tab displays the Users, Security, Integrations section.
  3. From the Users, Security, Integrations section, click **Login Policies**. The Login Polices page appears.
  4. On right side of the page, click **Add New**. The Add Policy page appears.
![Image ofs_add_policy_auth.png displays Add Policy page \(Authentication - SAML\)](https://docs.oracle.com/en-us/iaas/Content/oraclefieldservicecloud/images/ofs_add_policy_auth.png)
  5. Enter a **Label** and a **Policy Name**.
  6. Select **SAML** from the **Authenticate using** drop-down list. The SAML specific fields get updated in the Add Policy page.
  7. Select **Upload Metadata XML** from the **Specify SAML IdP** drop-down list. The specific fields for the identity domain get updated on the Add Policy page.
![Image ofs_add_policy_upload_metadata.png displays : Add Policy page \(SAML IdP - Oracle IDCS\)](https://docs.oracle.com/en-us/iaas/Content/oraclefieldservicecloud/images/ofs_add_policy_upload_metadata.png)
  8. Click **Upload,** and then locate the identity domain metadata that you previously downloaded. See the "What Do You Need" section.
  9. Click **Open** , and then click **Download** to download the SP metadata.
  10. Do not enter any value for the **SAML attribute containing username** text box.
  11. Enter a value for Max sessions. Max sessions are the maximum number of simultaneous sessions allowed for a user.
  12. Click **Add**. The new policy appears in the list of login policies.
**Note:** Based on requirements, you need to create separate policies for manage applications and for mobility applications. As an alternative, you can use a common policy for both applications.


#### Updating User Types to Use the New Login Policy Created for SSO Profile 🔗 
  1. Log in as an administrator using the login URL format: `<https://instance_name.fs.ocs.oraclecloud.com/>`.
  2. In the main page, click **Configuration**. The Configuration tab displays the Users, Security, Integrations section.
  3. From the Users, Security, Integrations section, click **User Types**. The Users Types page appears.
  4. On the left side of the page, select the **User Type** that you want to use for the newly created SSO policy. The selected user type appears.
  5. From the **Login Policy** drop-down list, select the SSO policy that you created in the "Create SSO Login Policy" section.
  6. Click **Save**.
**Note:**
     * Alternatively, to save configuration time, create a new user type, and then modify settings as per your requirement.
     * For SSO to work for a user, ensure that the user is mapped to the correct user type and the user type is assigned to the SSO login policy.


### Saving the X509 Certificate in PEM Format 🔗 
Use this section to convert the X509 Certificate value into a format that is suitable for an identity domain.
  1. In the SP metadata file, locate `<ds:X509Certificate>` under `<samlmd:KeyDescriptor use="signing">`.
  2. Copy value between `<ds:X509Certificate>` and `</ds:X509Certificate>` to a text file.
![Image ofs_copy_X509Certificate.png displays a sample SAML 2.0 compliant SP metadata xml file with an arrow pointing to the certificate text to copy.](https://docs.oracle.com/en-us/iaas/Content/oraclefieldservicecloud/images/ofs_copy_X509Certificate.png)
  3. Add `-----BEGIN CERTIFICATE-----` at the beginning of the file.
  4. Add `-----END CERTIFICATE-----` at the end of the file.
![Image ofs_begin_end_certificate.png displays the .cer file contents after manually converting to PEM format.](https://docs.oracle.com/en-us/iaas/Content/oraclefieldservicecloud/images/ofs_begin_end_certificate.png)
  5. Save and change the file extension to **.cer**.


### Obtaining Oracle Field Service Cloud Details 🔗 
The tenant ID is required before you can register and activate Oracle Field Service Cloud. You obtain this information from the Oracle Field Service Cloud URL: `https://instance_name.fs.ocs.oraclecloud.com/`.
The Oracle Field Service Cloud server name is the instance_name.fs.ocs portion of the URL, and the tenant ID is the your.tenant.id portion of the URL.
## Configuring Oracle Field Service Cloud in an Identity Domain 🔗 
Use this section to register and activate Oracle Field Service Cloud and to enable provisioning for Oracle Field Service Cloud. You can then assign users or groups to Oracle Field Service Cloud and start the user provisioning process.
**Note** : The Synchronization feature is currently not supported.
### Prerequisite Steps 🔗 
To enable provisioning, client credentials (client ID and client secret) and API access permissions are required to authenticate with Oracle Field Service Cloud REST APIs. You obtain these values while registering identity domain tenant with Oracle Field Service Cloud using the Oracle Field Service Cloud admin console.
For details, see the "Configuring Authentication using Oracle Field Service Cloud Token Service" and "Authorization" sections in the [_REST API for Oracle Field Service Cloud Service_](https://docs.oracle.com/cloud/latest/fieldservicecs_gs/CXFSC/) document.
### Registering and Activating Oracle Field Service Cloud 🔗 
  1. Access the OCI Console with your identity domain administrator credentials.
  2. Open the navigation menu and click **Identity & Security**. Under **Identity** , click **Domains**. Select the identity domain you want to work in and click **Applications**.
  3. Click **Add application**.
  4. In the **Add application** window, click **Application Catalog** , and then **Launch app catalog**.
  5. Search for `Oracle Field Service Cloud`, and then click **Add**.
  6. In the App Details section, enter the **Name** and **Description**.
  7. By default, both of the Oracle Field Service Cloud apps are selected. Clear the sub app that is not required.
  8. Enter the **OFSC Tenant Id** that you previously obtained. See the "Obtain the Oracle Field Service Cloud Details" section.
  9. Enter the **OFSC Manage Login Policy** and **OFSC Mobility Login Policy** that you previously created, and then click **Next**. See the "Create SSO Login Policy" section.
**Note:** The OFSC Manage Login Policy and the OFSC Mobility Login Policy are similar when you use the same policy for both applications.
  10. Click **Upload** to upload the signing certificate that you previously saved in PEM format. See the "Saving the X509 Certificate in PEM Format" section.
  11. Click **Next** to enable provisioning for Oracle Field Service Cloud. See the "Enabling Provisioning for Oracle Field Service Cloud" section.
  12. After you enable provisioning, click **Finish**. Yiou should see a confirmation message.
  13. Click **Activate** , and then click **Activate Application**. Yiou should see a confirmation message.


### Enabling Provisioning for Oracle Field Service Cloud 🔗 
Use this section to enable provisioning for managing user accounts in Oracle Field Service Cloud through an identity domain in IAM.
  1. On the Provisioning page, select **Enable Provisioning**.
  2. Use the table to enter values for establishing a connection with Oracle Field Service Cloud through an identity domain in IAM:


**Parameter**| **Value**  
---|---  
Client ID @ Instance Name| Enter the value in the `Client ID@Instance Name` format. In this format, replace `Client ID` with the Client ID that you obtained in the "Prerequisite Steps" section. Replace `Instance Name` with the Oracle Field Service Cloud instance name that appears on the About tab of the Oracle Field Service Cloud admin console. For example: “idcsApp@acmeinstance“  
Client Secret| Enter the client secret value that you obtained in the “Prerequisite Steps” section.  
  1. Click **Test Connectivity** to verify the connection with Oracle Field Service Cloud. Yiou should see a confirmation message.
  2. To view predefined attribute mappings between the user account fields defined in Oracle Field Service Cloud and the corresponding fields defined in an identity domain in IAM, click **Attribute Mapping** , and then click **OK**.
To add a new attribute for provisioning, click **Add Attribute** , specify the attributes in the **User** and **Oracle Field Service Cloud Account** columns, and then click **OK**. For example, if you want to add the **User Name** field, enter `$(user.userName)` in the **User** column, and then select the corresponding field from the drop-down list in the **Oracle Field Service Cloud Account** column.
**Note** : For SSO to work for provisioned users, ensure that the user type that you specify (in the **User** column for the **userType** attribute) is assigned to the login policy that you created for SSO profile in the "Creating the SSO Login Policy" section.
  3. Specify the provisioning operations that you want to enable for Oracle Field Service Cloud:
**Note:** By default, the **Create Account** and **Delete Account** check boxes are selected.
**Create Account** : Automatically creates an account in Oracle Field Service Cloud when access is granted to the corresponding user in an identity domain in IAM.
**Delete Account** : Automatically deletes an account from Oracle Field Service Cloud when access is revoked from the corresponding user in an identity domain in IAM.


You can now manage Oracle Field Service Cloud accounts through an identity domain in IAM. For more information on performing provisioning tasks, see the [Managing Users](https://docs.oracle.com/iaas/Content/Identity/users/about-managing-users.htm) and [Managing Groups](https://docs.oracle.com/iaas/Content/Identity/groups/managinggroups.htm) sections in _IAM with Identity Domains_.
**Note** : Before assigning the Oracle Field Service Cloud app to a user account, ensure that the **Time Zone** and **Preferred Language** attributes are specified for the account otherwise the app grant process fails.
## Verifying the Integration 🔗 
Use this section to verify that SSO and single log-out (SLO) work when initiated from an identity domain in IAM (IdP Initiated SSO and IdP Initiated SLO) and when initiated from Oracle Field Service Cloud (SP Initiated SSO and SP Initiated SLO).
### Verifying Identity Provider Initiated SSO from IAM 🔗 
  1. Access the identity domain's My Profile console: `https://<domainURL>/identity/domains/my-profile`.
  2. Log in using credentials for a user that is assigned to Oracle Field Service Cloud. You should see a shortcut to the Oracle Field Service Cloud sub app under **My Apps**. For example, it displays Oracle Field Service Cloud Manage or Oracle Field Service Cloud Mobility.
  3. Click one of the Oracle Field Service Cloud sub apps. The Oracle Field Service Cloud home page appears.
  4. On the Oracle Service Cloud home page, confirm that the user that is logged in is the same for both Oracle Field Service Cloud and the identity domain in IAM.
This confirms that SSO that is initiated from the identity domain works.
**Note:** In some scenarios, the user might not be assigned to a given app in Oracle Field Service Cloud. The user is still able to view the app in the identity domain in IAM. However, if the user tries to access the app, the user is logged out of Oracle Field Service Cloud and the identity domain in IAM. This is a known limitation that users can't be assigned to individual sub apps in the identity domain in IAM.


### Verifying Service Provider Initiated SSO from Oracle Field Service Cloud 🔗 
  1. Access Oracle Field Service Cloud using the URL: `https://instance_name.fs.ocs.oraclecloud.com/login_policy_label/`. The identity domain login page appears. See [Set Up the SSO Authentication](https://docs.oracle.com/en/cloud/saas/field-service/faadu/c-set-up-the-sso-authentication.html#t_set_up_the_sso_authentication) to set up the Service Provider initiated implementation method.
  2. Enter credentials for a user that is assigned to Oracle Field Service Cloud, and then click **Sign In**. The Oracle Field Service Cloud home page appears.
  3. Confirm that the user that is logged in is the same for both Oracle Field Service Cloud and the identity domain in IAM.
This confirms that SSO that is initiated from Oracle Field Service Cloud works.


### Verifying Identity Provider Initiated SLO 🔗 
  1. On the Console home page, click the user name in the upper-right corner, and then select **Sign out** from the drop-down list. The user is logged out, and the identity domain login page appears.
  2. On the Oracle Field Service Cloud home page, perform any operation. The identity domain login page appears. This confirms that SLO works and that the user is no longer logged in to Oracle Field Service Cloud and the identity domain in IAM.


### Verifying Service Provider Initiated SLO 🔗 
  1. On the Oracle Field Service Cloud home page, click the user name in the upper-right corner, and then select **Logout** from the drop-down list. The user is logged out of Oracle Field Service Cloud and the identity domain login page appears.
  2. Access the My Profile console, and then confirm that the user is no longer logged in.
This confirms that SLO works and that the user is no longer logged in to Oracle Field Service Cloud and the identity domain in IAM.


## Troubleshooting 🔗 
Use this section to locate solutions to common integration issues.
### Known Issues 🔗 
Use this section to learn about any known issues.
#### Oracle Field Service Cloud displays the error, "Incorrect request. If the problem persists, please contact the administrator" 🔗 
**Cause** : SSO is not configured correctly.
**Solution** : Verify that your SSO configuration is configured correctly.
#### Identity Domains displays the message, " You are not authorized to access the app. Contact your system administrator." 🔗 
**Cause1** : The administrator revokes access for the user at the same time that the user tries to access the Oracle Field Service Cloud using the identity domain in IAM.
**Solution1** :
  * Access the Console, select **Applications** , **OFSC** , **Users** , and then click **Assign** to re-assign the user.


**Cause2** : The SAML 2.0 integration between the identity domain in IAM and Oracle Field Service Cloud is deactivated.
**Solution2** :
  * Access the identity domain in IAM administration console, select Applications, and then Oracle Field Service Cloud.
  * Click Activate, and then click **Activate Application**. Yiou should see a confirmation message.


#### In the console, users can view multiple application links. At times, a log-out operation is initiated when users attempt to access a particular application link. 🔗 
**Cause** : In the current release, two the applications are displayed in the console, namely Oracle Field Service Cloud Manage application and Oracle Field Service Cloud Mobility application. Few users have access to the Oracle Field Service Cloud Mobility application only. When users, who have access only to Oracle Field Service Cloud Mobility application, attempt to access the Oracle Field Service Cloud Manage application, a Single Logout Operation (SLO) is triggered.
**Solution** : Users need to verify and then click the application links considering their granted access.
#### SLO at times is not successful. 🔗 
Consider a scenario where a user is logged in to the identity domain in IAM, Oracle Field Service Cloud Mobility and Oracle Field Service Cloud Manage applications. In such a scenario, when the user performs a logout operation, then the logout operation is successful from the identity domain in IAM application and from one of the Oracle Field Service Cloud applications.
**Cause:** The identity domain in IAM logout operation is successful, however, the SLO operation either from Oracle Field Service Cloud Mobility or Oracle Field Service Cloud Manage applications will not get triggered. This is because, Oracle Field Service Cloud Mobility and Oracle Field Service Cloud Manage applications are two different interfaces. Operations in these applications are handled separately.
**Solution:** Users need to manually logout from Oracle Field Service applications.
### Unknown Issues 🔗 
For unknown issues, open a support ticket. See [Open a Support Ticket](https://docs.oracle.com/iaas/Content/GSG/Tasks/contactingsupport_topic-Open_a_support_service_request.htm).
Was this article helpful?
YesNo

