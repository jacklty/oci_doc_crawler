Updated 2025-01-14
# Managing a SAML Identity Provider
Use the Console to add a SAML 2.0 identity provider (IdP) to an identity domain so authenticated users from the IdP can access Oracle Cloud Infrastructure can access resources and cloud applications.
## Common terms 🔗  

Identity Provider (IdP)
    
An IdP is a service that provides identifying credentials and authentication for users. 

Service Provider (SP)
    
A service (such as an application, website, and so on) that calls upon an IdP to authenticate users.
Use the following steps to create a SAML 2.0 IdP:
## Configuring SAML JIT Provisioning 🔗 
SAML JIT Provisioning can be configured using the Console or `/admin/v1/IdentityProviders` REST API endpoint. See the following references to configure SAML JIT Provisioning: 
  * [Adding a SAML Just-in-Time Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/add-saml-idp-jit-prov.htm#add-just-in-time-saml "Set up a SAML identity provider \(IdP\) that uses just-in-time \(JIT\) provisioning for an identity domain in IAM.")
  * [Configuring IdP metadata](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/add-saml-identity-provider.htm#configure-idp-metadata "Enter IdP metadata details manually, or import a metadata file.")
  * [Creating an Identity Provider with a REST API](https://docs.oracle.com/en/cloud/paas/iam-domains-rest-api/op-admin-v1-identityproviders-post.html)
  * [Configuring SAML JIT Provisioning with a REST API](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/workingWithIDPs.html#unique_1219769806)


## Adding a SAML Identity Provider 🔗 
Entering the SAML details for an identity provider.
  1. Navigate to the identity domain: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **Identity providers**.
  3. Select **Add IdP** , and then select **Add SAML IdP**.
  4. Enter the following information:
     * **Name** : Enter the name of the IdP.
     * (Optional) **Description** : Enter a description of the IdP.
     * (Optional) **Identity provider icon** : Drag and drop a supported image, or select **select one** to browse for the image.
  5. Select **Next**.
  6. On the **Exchange metadata** screen, select **Export SAML metadata** button to send the SAML metadata to the identity provider. Do one of the following:
     * **Import IdP metadata** : Select this option if you have an XML file exported from your IdP. Drag and drop the XML file to upload the metadata, or select **select one** to browse for the metadata file.
     * **Enter IdP metadata** : Select this option if you want to manually enter the IdP metadata. Provide the following details: 
       * **Identity provider issuer URI**
       * **SSO service URI**
       * **SSO service binding**
       * **Upload identity provider signing certificate**
       * **Enable global logout**
     * **Import IdP URL** : Enter the URL of your IdP metadata.
  7. Select **Show advanced options** if you want to select the following:
     * **Signature hashing algorithm** : Select SHA-256 or SHA-1
     * **Require encrypted assertion** : Indicates that the identity domain authorization expects an encrypted assertion from the IdP.
     * **Force authentication** : Select this option to require users to authenticate with the IdP, even if the session is still valid.
     * **Requested authentication context** : Select authentication content class references.
     * **Holder-of-Key subject confirmation required** : Available after you upload a Holder-of-Key (HOK) supported valid metadata file.
     * **Send signing certificate with SAML message** : Select this to include the identity domain's signing certificate with SAML messages sent by your identity domain. Some SAML providers require the signing certificate to look up the SAML partner configuration.
  8. Select **Next**.
  9. On the **Add SAML identity provider** screen, do the following:
    1. Select a **Requested Name ID format**.
  10. Map user's identity attributes received from the IdP to an Oracle Cloud Infrastructure identity domain.
Mapping options vary based on identity provider. You might directly assign an IdP value to an Oracle Cloud Infrastructure identity domain value. For example, **NameID** might map to **UserName**. If you select SAML assertion attribute as the source, select the Assertion attribute name and then enter the Oracle Cloud Infrastructure identity domain.
  11. Select **Submit**.
  12. On the **Review and create** screen, review your SAML identity provider settings. If the settings are correct, select **Create**. Select **Edit** next to the set of settings, if you need to change them.
  13. The Console displays a message when the SAML identity provider is created. You can do the following from the overview page:
     * Select **Test** to verify that the SAML SSO connection is working correctly.
     * Select **Activate** to activate the IdP so the identity domain can use it.
     * Select **Assign to IdP policy rule** to assign this SAML identity provider to an existing policy rule you have created.
  14. Select **Close**.


[Import Metadata for a SAML Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/add-saml-identity-provider.htm)
Import the SAML metadata for an identity provider.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **Identity providers**.
  3. Select **Add IdP** , and then select **Add SAML IdP**.
  4. Enter details for the IdP:
Field | Description  
---|---  
**Name** | Enter the name of the IdP.  
**Description** | Enter explanatory information about the IdP.  
**Icon** | Browse for and select or drag and drop an icon that represents the IdP. The icon should be 95 x 95 pixels in size and have a transparent background. Supported file formats are .png, .fig, .jpg, .jpeg.   
  5. Select **Next**. Enter the configuration details:
Field | Description  
---|---  
**Import identity provider metadata** | Select this option to import the metadata for the IdP.  
**Identity provider metadata** | Select the XML file that contains the metadata for the IdP that you want to import.**Note:** You can only define one IdP in the identity domain with a particular Issuer ID, also known as the Provider ID or Entity ID. The Entity ID attribute is part of the IdP metadata, so you can only create one IdP with a given metadata file. Furthermore, you can update an IdP with new metadata, but you cannot change its Issuer ID.  
**Send signing certificate with SAML message** |  To include the identity domain's signing certificate with SAML messages sent to the IdP, select this checkbox. The signing certificate is used to verify the signature of the messages for the IdP. This is typically not needed, but some IdPs require it as part of their signature verification process.  
**Signature hashing algorithm** |  Select the secure hash algorithm to use to sign messages sent to the IdP.
     * **SHA-256** is the default.
     * If the IDP doesn't support SHA-256, then select **SHA-1**.  
  6. Select **Next**. Configure the mapping between IdP and identity domain user attributes:
Field | Description  
---|---  
**Identity provider user attribute** |  Select the user attribute value received from the IdP that can be used to uniquely identify the user. You can specify either the assertion **Name ID**. Or, you can specify another **SAML attribute** from the assertion by entering it in the **Assertion attribute** text box.  
**Identity domain user attribute** |  Select the attribute in the identity domain to which you are mapping the attribute received from the IdP. You can specify the username or another attribute (such as the user's display name, primary or recovery email address, or an external ID). You use the external ID when you want to map the attribute received from the IdP to a special ID that's associated with the provider.  
**Requested NameID format** |  When SAML authentication requests are sent to the IdP, you can specify a Name ID format in the request. If your IdP does not require this in the request, then select **< None Requested>**.  
  7. Select **Create IdP**. Export the identity domain's SAML metadata:
Task | Description  
---|---  
**Service provider metadata** |  To export metadata for the identity domain, select **Download**. Then, import this metadata into the IdP. If the IdP does not support importing a SAML metadata XML document, use the following information to manually configure the IdP. If the federation partner into which you are importing the identity domain metadata performs CRL validation (for example, AD FS performs CRL validation) instead of using the metadata exported from this button, download the metadata from: `https://[instancename.idcs.internal.oracle.com:port]/fed/v1/metadata?adfsmode=true` Turn on the switch under Access Signing Certificate in [Default Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/set-access-signing-certificate.htm#change-default-settings "Allow clients to access the signing certificate for the identity domain in IAM without logging in to an identity domain.") to enable clients to access the metadata without logging in to the identity domain.  
**Service provider metadata with self-signed certificates** |  To export metadata for the identity domain along with self-signed certificates, select **Download** . Then, import this metadata into the IdP. If the IdP does not support importing a SAML metadata XML document, use the following information to manually configure the IdP. If the federation partner into which you are importing the identity domain metadata performs CRL validation (for example, AD FS performs CRL validation) instead of using the metadata exported from this button, download the metadata from: `https://[instancename.idcs.internal.oracle.com:port]/fed/v1/metadata?adfsmode=true` Turn on the switch under Access Signing Certificate in [Default Settings](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/set-access-signing-certificate.htm#change-default-settings "Allow clients to access the signing certificate for the identity domain in IAM without logging in to an identity domain.") to enable clients to access the metadata without logging in to the identity domain.  
**Provider ID** |  The Uniform Resource Identifier (URI) that uniquely identifies the identity domain. The Provider ID is also known as the Issuer ID or Entity ID.  
**Assertion consumer service URL** | The Uniform Resource Locator (URL) of the identity domain service endpoint that receives and processes assertions from the IdP.  
**Logout service endpoint URL** | The URL of the identity domain service endpoint that receives and processes logout requests from the IdP.  
**Logout service return URL** | The URL of the identity domain service endpoint that receives and processes logout responses from the IdP.  
**Service provider signing certificate** | To export the identity domain's signing certificate, select **Download**. Select the file that contains the signing certificate. This certificate is used by the IdP to verify the signature on SAML requests and responses sent by the identity domain to the IdP.  
**Service provider encryption certificate** | To export the identity domain's encryption certificate, select **Download**. Select the file that contains the encryption certificate. This certificate is used by the IdP to encrypt SAML assertions that it sends to the identity domain. This is only needed if the IdP supports encrypted assertions.  
To get the issuing identity domain root certificate, see [Obtain the Root CA Certificate](https://docs.oracle.com/en-us/iaas/Content/Identity/defaultsettings/obtain-root-ca-certificate.htm#obtain-root-ca-certificate "When you set up service providers and identity providers for federated SSO in an identity domain in IAM, you need to download the metadata file and the signing and encryption certificates. However, these certificates are not self-signed and are issued by a root certificate. So, for a proper setup and function, you need to get the root certificate and install it at the federation partner.").
  8. Select **Next**.
  9. On the **Test IdP** page, select **Test login** to test the configuration settings for the IdP. (You must be logged in to the identity domain for which you configured the IdP to test the configuration settings.)
  10. Select **Next**.
  11. On the **Activate IdP** page, select **Activate** to activate the IdP.
  12. Select **Finish**.


## Exporting SAML Metadata 🔗 
Exporting the SAML metadata for an identity domain in IAM.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Domains**.
  2. Click the name of the identity domain that you want to work in. You might need to change the compartment to find the domain that you want. Then, click **Security** and then **Identity providers**.
  3. Open an identity provider.
  4. Select **Export SAML metadata**.
  5. Select one of the following:
     * **Metadata File** : Select download the SAML XML metadata file, or download the SAML XML metadata with self-signed certificates.
     * **Manual Export** : Manually exporting the metadata allows you to choose from multiple SAML options, for example the Entity ID or Logout response URL. After you copy the export file, you can download the **Service provider signing certificate** or the **Service provider encryption certificate**.
     * **Metadata URL** : If your IdP supports downloading SAML metadata directly. Select **Access signing certificate** to allow clients to access the signing certificate without having to log into an IdP.


## Configuring IdP metadata 🔗 
Enter IdP metadata details manually, or import a metadata file.
  1. Select one of the following:
     * **Import IdP metadata** : Select this option if you have an XML file exported from your IdP. Drag and drop the XML file to upload the metadata, or select **select one** to browse for the metadata file.
     * **Enter IdP metadata** : Select this option if you want to manually enter the IdP metadata. Provide the following details: 
       * **Identity provider issuer URI** : 
       * **SSO service URI**
       * **SSO service binding**
       * **Upload identity provider signing certificate**
       * **Upload identity provider encryption certificate**
       * **Enable global logout**
       * **Identity provider logout request URL**
       * **Identity provider logout response URL**
       * **Logout binding**
  2. Select the **Signature hashing algorithm** method.
  3. Select whether you want to use a **Signed signing certificate with SAML message**.
  4. Select **Next**.


## Mapping user attributes 🔗 
Map the relationship between the IdP user attributes and identity domain user attributes.
  1. In the field **Requested Name ID format** , select a mapping option. 
Mapping options vary based on identity provider. You might be able to directly assign an IdP value to an Oracle Cloud Infrastructure identity domain value. For example, **NameID** might map to **UserName**. If you select SAML assertion attribute as the source, select the Assertion attribute name and then enter the Oracle Cloud Infrastructure identity domain.
If you select **Custom** , enter the details in the field **Custom Name ID format**.
  2. Select fields in **Identity provider user attribute** and select a corresponding field in **Identity domain user attribute**.
  3. Select **Next**.


## Reviewing and creating the IdP 🔗 
Verify the IdP options are accurate and then create the IdP.
  1. Select **Test login** to open the IdP sign-in screen.
  2. Select **Create IdP**.
**Note** To edit an IdP after creating it, go to the **Identity Providers** list, select the IdP, and then [edit the IdP](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/modify-identity-provider.htm#modify-identity-provider "Update an identity provider.").


Was this article helpful?
YesNo

