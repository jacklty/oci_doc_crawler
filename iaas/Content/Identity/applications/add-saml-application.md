Updated 2025-01-14
# Adding a SAML Application
Create a Security Assertion Markup Language (SAML) application and grant it to users so that your users can single sign-on (SSO) into your SaaS applications that support SAML for SSO.
**Before You Begin:**
Before you create the SAML application, all users who need to sign in using this application must be present in the Service Provider (SP). If needed, use SCIM provisioning to sync any users or groups from the Identity Provider (IdP) to the SP. See [Integrating Custom Applications with IAM](https://docs.oracle.com/en-us/iaas/Content/Identity/scim/overview.htm#using "Learn how to use the SCIM interface to integrate custom applications with an identity domain.").
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**. 
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Integrated applications**. 
  3. Select **Add application**. 
  4. In the Add application window, select **SAML Application** , and then **Launch workflow**.
  5. In the Add SAML Application page, provide values for the following fields:
     * In the **Name** field, enter a name for the application.
For applications with lengthy names, the application name appears truncated in the **My Apps** page. Consider keeping application names as short as possible.
     * In the **Description** field, enter 250 or fewer characters to provide a description of the application.
     * Select the close (X) in the Application icon window to delete the default **Application icon** and then add your own icon for the application.
     * Select **Add app links** to add links that are associated with the application. Select **Add** and the **Add app link** window appears. App links are services such as Mail or Calendar that are offered by applications such as Google or Office 365.
In the **Add app link** window:
       1. Enter a **Name** for the **App link**.
       2. In the **Relay state** field, enter the URL used to access the application.
       3. Select the close (X) in the Application icon window to delete the default **Application icon** for the app link and then add your own icon for the application.
       4. Select **Visible** if you want your application to appear automatically on each user's My Apps page. 
**Note** Selecting this checkbox doesn't enable or disable SSO into the application.
       5. Select **Add**.
The **App link** information appears in the table in the **App links** section.
To remove an **App link** , select the row, and then select **Remove**.
**Note** There's a delay (a few seconds) between selecting **Remove** and the App no longer appearing on the My Apps page. App link deletion (and grants related to those App links) is asynchronous. Wait a few seconds for the asynchronous task to remove the App and its grants before trying **My Apps** again.
     * In the **Relay state** field, enter a value which is sent to the SAML SP as the SAML RelayState parameter.
     * In the **Custom sign-in URL** field, specify a custom sign-in URL. However, if you're using a default login page provided by IAM, then leave this field blank.
     * In the **Custom error URL** field, enter the error page URL to which a user has to be redirected, if there is a failure. This is an optional field. However, if not specified, the domain-specific Error page URL is used. If both the error URLs are not configured, then the error is redirected to the IAM Error Page (/ui/v1/error). 
When a user tries to use social authentication (ex: Google, Facebook, and so on) for logging into IAM, the callback URL must be configured in the Custom Error URL field. Social providers need this callback URL to call IAM> and send the response back after social authentication. The provided callback URL is used to verify whether the user exists or not (in the case of first-time social login), and display an error if the social authentication has failed.
     * In the **Custom social linking callback URL** field, enter the URL that IAM> can redirect to after linking of a user between social providers and IAM> is complete. This is an optional field.
When you create a custom app using IAM> custom SDK and integrate with IAM> Social Login, the custom app needs to have the Linking callback URL which can be redirected after linking of the user between social provider and IAM is complete.
  6. In the **Display settings** sections of the Add SAML Application page, make the following selections:
     * Select **Display in My Apps** checkbox to specify you want the SAML App to be listed on the My Apps page.
When you select the **Display in My Apps** checkbox in applications, the app is then visible in the My Apps page, but selecting this checkbox doesn't enable or disable SSO to the app.
The flag to enable or disable SSO comes from the app template. 
     * Select the **User can request access** checkbox if you want the app to be listed in the Catalog. This option allows end users to request access to the app from their My Apps page by selecting **Add** and then selecting the app from the Catalog.
**Note** Don't forget to activate the application so that users can request access.
  7. When you're creating SAML app from scratch rather than creating a preconfigured SAML app created from the App Catalog, the **Authentication and authorization** section appears. The **Enforce grants as authorization** checkbox is selected by default. This checkbox enables users to access only the application that you assigned or granted access to. If the checkbox is selected, IAM can control access to the SAML application based on grants to users and groups. If the check box isn't selected, any authenticated user has access to the application regardless of the assignment status. 
  8. Select **Next** and configure SSO for the SAML application. 
  9. In the **General** section of the Configure single sign-on page, define the following:
     * **Entity ID** : Enter a globally unique name for a SAML entity. The **Entity ID** is usually the URL of an identity provider or a service provider.
     * **Holder-of-Key subject confirmation required** : Turn on this option and then enter the endpoint at the service provider where the identity provider can send SAML authentication Holder-of-Key (HOK) assertions.
     * **Assertion consumer URL** : Enter the URL to which the SAML identity provider sends the SAML assertion. This URL must begin with either the HTTP or HTTPS protocol.
     * **Name ID format** : Select the type of format to use for the Name ID. The service provider and the identity provider use this format to easily identify a subject during their communication.
**Note** When you integrate IAM with MS SharePoint app based on WS Fed 1.1 protocol, the following options aren't available in the Name ID format: **Persistent** , **Kerberos** , and **Transient**.
     * **Name ID value** : Select the Name ID Value to identify the user that's logged in. The available options are **Username** , the user's **Primary email** address and **Expression**. When you select the **Expression** option, enter a regular expression as a value in the text box. There's no character limit for the value, however, there are validation rules that are performed on the value for any invalid characters that can't be mapped.
     * **Signing certificate** : Upload the signing certificate that's used to encrypt the SAML assertion.
**Note** Some browsers show file paths prepended with `c:\fakepath\`. This behavior is a security feature of the browser and doesn't disrupt the upload process.
  10. Use the following table to define a more fine-grained SAML configuration in the **Additional configurations** section.
Option | Description  
---|---  
**Signed SSO** |  Select **Assertion** to indicate that you want the SAML assertion signed. Select **Response** when you want the SAML authentication response signed.  
**Include signing certificate in signature** |  Select the checkbox to include the signing certificate in the signature, for example, when the application requires that the signing certificate is sent along with the assertion.  
**Signature hashing algorithm** |  Select the type of signing algorithm that you want to use to sign the assertion or the response, either **SHA-256** or **SHA-1**. SHA-256 generates a fixed 256-bit hash. SHA-1 generates a 160-bit hash value known as a message digest. **Note:** In a FIPS enabled environment, set the **Signature hashing algorithm** to SHA-256, the only supported hashing algorithm, to avoid errors during SSO.   
**Enable single logout** |  Select to configure SAML single logout. Single logout enables a user to lot out of all participating sites in a federated session almost simultaneously. This checkbox is selected by default. Clear it if you do not want to enable single logout.  
**Logout binding** |  Select whether the log out request is sent as a REDIRECT (transported using HTTP 302 status-code response messages) or a POST (transported in HTML form-control content, which uses a base-64 format). This list box appears only if you select the **Enable single logout** checkbox.  
**Single logout URL** |  Enter the location (HTTP or HTTPS) where the log out request is sent. This field appears only if you select the **Enable single logout** check box.  
**Logout response URL** |  Enter the location (HTTP or HTTPS) where the log out response is sent. This field appears only if you select the **Enable single logout** check box.  
**Encrypt assertion** |  Select if you want to encrypt the assertion, and then define the encryption algorithm that you want to use and upload the encryption certificate.  
**Encryption certificate** |  Select **Upload** to upload the encryption certificate that's used to encrypt the SAML assertion. This button appears only if you select the **Encrypt assertion** checkbox.  
**Encryption algorithm** |  Select which encryption algorithm you want to use to encrypt the SAML assertion. This list box appears only if you select the **Encrypt assertion** checkbox.  
**Key Encryption algorithm** |  Select which key encryption algorithm you want to use to encrypt the SAML assertion. This list box appears only if you select the **Encrypt assertion** checkbox.  
  11. In the **Attribute configuration** section, add user-specific and group-specific attributes to the SAML assertion. This is useful if your application uses user-specific or group-specific attributes, and you want to send that information as part of the SAML assertion.
  12. Select **Additional attributes** , and then use the following table to specify the user attribute that you want to include. User information in the attribute statement contains a list of attributes. Each attribute includes a name and a list of values (if there are multiple attribute values). Each value includes a value and the format of the value.
Option | Description  
---|---  
**Name** |  Enter the name of the SAML assertion attribute.  
**Format** |  Select the format of this SAML assertion attribute: **Basic** , **URI Reference** , or **Unspecified**. **Note:** When you integrate IAM with MS SharePoint app based on WS Fed 1.1 protocol, **Format** menu is replaced with **Namespace**.  
**Type** |  Select one of the following options to specify the value of the assertion attribute.: 
     * **User attribute** Select this option to choose one of the predefined list of user attributes or group attributes in the **Value** menu as the value of the assertion attribute. To specify group attributes, select **User attribute** and in the **Value** field, select **Group membership**.
     * **Expression/literal** Select this option when you can't use any of the predefined values in the **Value** menu. You can provide an expression in the **Value** text box to specify the value of the SAML assertion attribute.  To specify group attributes, select **Expression/literal** and specify an expression to fetch the groups. Example: The following expression specifies that the value of the SAML attribute should be the names of all the groups to which the user belongs: `$(user.groups[*].display)`.  
**Type value** |  Select or enter the value to send as part of the assertion based on the **Type** that you have selected. When the type is **User attribute** , you can select one of the predefined list of user attributes as the value of the assertion attribute. Select the **Group membership** option in the menu if you want to send the users group membership as the value of the assertion attribute. The **Condition** and **Value** columns appear when you choose **Group membership**.  When the type is **Expression/literal** , the value field is a text box and you can enter any path expression to specify what should be the value of the assertion attribute.  The following are some examples of path expressions:
     * To send a list of literal values as the value of the assertion attribute, use `["value1",                          "value2", "value3"]`.
     * To send "home email" as the value of the assertion attribute, use `$(user.emails[type eq "home"].value)`.
     * To send users first name concatenated with last name as the assertion attribute, use `#concat($(user.name.givenName),                          $(user.name.familyName))`.
     * To send an account attribute called `SALARY` as the value of the assertion attribute, use `$(account.SALARY)`.
     * To include an attribute `department` from custom schema extension, use `$(user.urn:ietf:params:scim:schemas:idcs:extension:custom:User:department)`.
     * To send a literal value as the value of assertion, use `aLiteralValue`.  
**Condition** |  Select a condition from the menu to filter the group memberships. This field is enabled only when you select **User attribute** as **Type** and **Group membership** as **Type value**. The available values are: **Equals** , **Starts with** , and **All groups**.  
**Condition value** |  Enter the filter value to use when filtering the group memberships.  
  13. Select **Finish**. The application is added in a deactivated state. To activate your application, see [Activating Applications](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/activate-applications.htm#activate-applications "Activate an application in an identity domain in IAM to reinstate the access rights to the application for users and groups.").
  14. In the SSO Configuration section, to import the IAM signing certificate into your application, select **Download signing certificate** to first download the certificate file in PEM format. This certificate is used by the SAML application to verify that the SAML assertion is valid.
  15. In the SSO Configuration section, to import the IAM Identity Provider metadata into your application, select **Download identity provider metadata** to first download the metadata file in XML format. The SAML application needs this information so that it can trust and process the SAML assertion that's generated by IAM as part of the federation process. This information includes, for example, profile and binding support, connection endpoints, and certificate information. To get the issuing IAM root certificate, see [Getting the Root CA Certificate](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/obtain-root-ca-certificate.htm#obtain-root-ca-certificate "When you set up service providers and identity providers for federated SSO in an identity domain in IAM, you need to download the metadata file and the signing and encryption certificates. However, these certificates are not self-signed and are issued by a root certificate. So, for a proper setup and function, you need to get the root certificate and install it at the federation partner.").


Was this article helpful?
YesNo

