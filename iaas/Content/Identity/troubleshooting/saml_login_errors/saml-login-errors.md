Updated 2025-02-18
# SAML Login Errors
Identify SAML login error messages and learn steps to resolve them.
**Note** SAML login errors are meant for a service administrator to help them troubleshoot sign in problems. If you're not an administrator and are having difficulty signing in, contact your service administrator. If you need help contacting your administrator, see _Contacting Your Administrator_ in the [Contacting Support](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#contacting_support) section.
SAML login errors display when a problem with metadata occurs, or when a security certificate is missing or fails to validate. To fix, access, compare, and correct the metadata, or provide current certificates from the service provider.
  * [The Federation partner <partner_name> is not recognized](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/saml_login_errors/saml-login-errors.htm#error_samlsrv_common_unknownPartnerProvider "Compare the application single sign-on metadata with the identity domain provider metadata to ensure they match.")
  * [Certificate was missing when trying to verify incoming digital signature for partner <partner_name>](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/saml_login_errors/saml-login-errors.htm#error_samlsrv_security_certMissing "Upload the missing security certificate to the SAML application.")
  * [URL query signature verification failed for partner <partner_name>. The certificate from the remote partner may need to be updated](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/saml_login_errors/saml-login-errors.htm#error_samlsrv_frontend_translator_urlQuerySignatureVerifyFailed "Upload the current security certificate to the SAML application.")
  * [Signature verification failed for partner <partner_name>. The certificate from the remote provider may need to be updated](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/saml_login_errors/saml-login-errors.htm#error_samlsrv_frontend_translator_signatureVerifyFailed "Upload the current security certificate to the SAML application.")
  * [No user returned through correlation policy](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/saml_login_errors/saml-login-errors.htm#error_samlsrv_sp_sso_assertion_noUserReturnedViaCorrelationPolicy "Users specified in the SAML assertion need to exist in the service provider data store, and the user correlation mechanism in the IdP resource needs to be setup correctly.")
  * [Multiple users returned through correlation policy](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/saml_login_errors/saml-login-errors.htm#error_samlsrv_sp_sso_assertion_multipleUserReturnedViaCorrelationPolicy "The user correlation mechanism in the IdP resource needs to be setup correctly.")
  * [The Federation partner saml-app is not enabled](https://docs.oracle.com/en-us/iaas/Content/Identity/troubleshooting/saml_login_errors/saml-login-errors.htm#error_samlsrv_common_partnerNotEnabled "Activate the disabled saml-app.")


## The Federation partner <_partner_nam_ e> is not recognized 🔗 
Compare the application single sign-on metadata with the identity domain provider metadata to ensure they match.
This message displays if there was a misconfiguration when setting up SAML as an identity provider or a service provider. If identity domains is the identity provider (IdP), then its configuration must match with the metadata obtained from the service provider (SP). If identity domains is the service provider, then its configuration must match with the metadata obtained from the identity provider.
### Identity Domains is the Identity Provider (IdP)
  1. Open the navigation menu and select **Identity Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then select **Integrated applications**. 
  3. Access the SSO information of the SAML application being verified.
  4. Access the identity domains provider metadata of the service provider online at `https://_<IDCS-service-instance>_.identity.oraclecloud.com/fed/v1/metadata`.
  5. Compare **entityID** and **AssertionConsumerService** with the SSO information from the metadata and ensure that they match.
  6. If single logout is enabled, compare **SingleLogoutService** and **ResponseLocation** and ensure that they match.
  7. Correct any mismatches.


### Identity Domains is the Service Provider (SP)
  1. Open the navigation menu and select **Identity Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Security** and then **Identity providers**. 
  3. Access identity domains metadata of the identity provider online at `https://_<IDCS-service-instance>_.identity.oraclecloud.com/fed/v1/metadata`.
  4. If you uploaded metadata from the IdP, ensure you uploaded the correct metadata file.
  5. If you manually entered IdP metadata, ensure **entityID** and **AssertionConsumerService** match with the IdP metadata.
  6. If single logout is enabled, compare **SingleLogoutService** and **ResponseLocation** and ensure that they match.
  7. Correct any mismatches.


## Certificate was missing when trying to verify incoming digital signature for partner <_partner_name_ > 🔗 
Upload the missing security certificate to the SAML application.
This message displays when a signing certificate isn't in the SAML application in the identity domain.
  1. Open the navigation menu and select **Identity Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then select **Integrated applications**. 
  3. Access the SSO information of the SAML application being verified.
  4. Check the **Signing Certificate** field and if empty, upload the certificate received from the service provider.


## URL query signature verification failed for partner <_partner_name_ >. The certificate from the remote partner may need to be updated 🔗 
Upload the current security certificate to the SAML application.
This message displays when a signing certificate in IDCS is expired or otherwise can't be verified.
  1. Open the navigation menu and select **Identity Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then select **Integrated applications**. 
  3. Access the SSO information of the SAML application being verified.
  4. Upload a current certificate received from the service provider.


## Signature verification failed for partner <_partner_name_ >. The certificate from the remote provider may need to be updated 🔗 
Upload the current security certificate to the SAML application.
This message displays when a signing certificate in an identity domain is expired or otherwise can't be verified.
  1. Open the navigation menu and select **Identity Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Security** and then **Identity providers**. 
  3. Select the Actions menu (![Actions Menu](https://docs.oracle.com/en-us/iaas/Content/libraries/global-images/actions-menu.png)) (Actions Menu) for the identity provider that you want to update.
  4. Select **Edit IdP**. A window that displays configuration settings for the IdP opens. 
  5. If you uploaded metadata from the IdP, obtain and upload current metadata.
  6. If you manually entered IdP metadata, obtain and upload a new signing certificate from the IDP.


## No user returned through correlation policy 🔗 
Users specified in the SAML assertion need to exist in the service provider data store, and the user correlation mechanism in the IdP resource needs to be setup correctly.
This message displays for one of two reasons:
  * The specified user hasn't been added to the service provider. Navigate to the domain and add them.
  * The user correlation mechanism in the IdP resource is incorrectly setup. Check that there's a user with the correlation mechanism defined in the IdP resource.


### No user found in service provider data store for the defined correlation policy
  1. Open the navigation menu and select **Identity Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Users**.
  3. Verify the specified user is in the list of users. If not, create a new user or use Just in Time (JIT) or System for Cross-domain Identity Management (SCIM) to provision the user.


### **Correlation policy issue**
  1. Open the navigation menu and select **Identity Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Security** and then **Identity providers**. 
  3. Verify that the SAML assertion attribute/Name ID configuration matches the user defined in the service provider identity store. Or, if any provisioning configurations are enabled such as JIT/SCIM, verify them as well.


## Multiple users returned through correlation policy 🔗 
The user correlation mechanism in the IdP resource needs to be setup correctly.
This message displays if the SAML assertion Name ID or SAML assertion attribute configuration incorrectly matches with multiple users.
  1. Open the navigation menu and select **Identity Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, select **Security** and then **Identity providers**. 
  3. Verify the SAML assertion Name ID or SAML assertion attribute configuration. It might be matching with multiple users in the identity store.


## The Federation partner saml-app is not enabled 🔗 
Activate the disabled saml-app.
This issue occurs when SAML app configured on the IDP end is not activated
  1. Open the navigation menu and select **Identity Security**. Under **Identity** , select **Domains**.
  2. Select the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then select **Integrated applications**. 
  3. Ensure the SAML application being verified is activated. If not, select **Activate**.


Was this article helpful?
YesNo

