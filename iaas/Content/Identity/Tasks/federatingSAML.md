Updated 2025-01-14
# Federating with SAML 2.0 Identity Providers
This topic describes the general steps to federate Oracle Cloud Infrastructure with any identity provider that supports the Security Assertion Markup Language (SAML) 2.0 protocol. If you want specific instructions for Oracle Identity Cloud Service or Microsoft Active Directory, see [Federating with Oracle Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#top) or [Federating with Microsoft Active Directory](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm#top). 
**Tip**
Find detailed setup steps for more IdPs in the following white papers: 
  * [Oracle Cloud Infrastructure Okta Configuration for Federation and Provisioning](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/okta-federation-with-oci.pdf)
  * [Federating Oracle Access Manager to Oracle Cloud Infrastructure](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/oracle-access-manager-federation-to-oci.pdf) Oracle Cloud Infrastructure


## Instructions for Federating 🔗 
Following is the general process an administrator goes through to set up the identity provider, and below are instructions for each step. It's assumed that the administrator is an Oracle Cloud Infrastructure user with the required credentials and access.
**Note**
Before following the steps in this topic, see [Federating with Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top) to ensure that you understand general federation concepts. 
  1. In the Oracle Cloud Infrastructure Console, get the federation metadata required to establish a trust relationship with the Identity Provider (IdP).
  2. In the IdP, configure Oracle Cloud Infrastructure as an application (sometimes called a trusted relying party). 
  3. In the IdP, assign users and groups to your new Oracle Cloud Infrastructure application.
  4. In the IdP, get the required information needed by Oracle Cloud Infrastructure. 
  5. In Oracle Cloud Infrastructure:
    1. Add the identity provider to your tenancy and provide information you got from the IdP.
    2. Map the IdP's groups to IAM groups.
  6. In Oracle Cloud Infrastructure, make sure you have IAM policies set up for the groups so you can control users' access to Oracle Cloud Infrastructure resources.
  7. Inform your users of the name of your Oracle Cloud Infrastructure tenant and the URL for the Console: <https://cloud.oracle.com>. 


**Step 1: Get information from Oracle Cloud Infrastructure**
Summary: Download the federation metadata document. 
The federation metadata document is a standard SAML 2.0 document, which provides information about Oracle Cloud Infrastructure you'll need to provide to your IdP. Depending on your provider's setup requirements, you may need to upload the entire document, or you may be asked to provide only specific metadata values from the document.
  1. Sign in to the Oracle Cloud Infrastructure Console as an administrator.
  2. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**.
  3. Right-click the **Download this document** link and save the document.


**Step 2: Set up Oracle Cloud Infrastructure as a trusted application**
Consult your IdP documentation for how to set up a trusted application. Refer to the metadata document you downloaded for required parameters.
**Step 3: Assign users and groups to the new application.**
Follow your IdP's procedures for adding users and groups to the application you set up for Oracle Cloud Infrastructure.
Step 4: Download the IdP's metadata document.
Your IdP should provide a SAML 2.0 document that contains the information Oracle Cloud Infrastructure needs to complete the federation. See your IdP documentation for instructions on downloading this document.
**Step 5: Federate the IdP with Oracle Cloud Infrastructure**
**Summary:** Add the identity provider to your tenancy. You can set up the group mappings at the same time, or set them up later. 
[Details: ](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm)
  1. Go to the [Console](https://cloud.oracle.com/) and sign in with your Oracle Cloud Infrastructure login and password.
  2. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**.
  3. Select **Add Identity Provider**. 
  4. Enter the following:
    1. **Name:** A unique name for this federation trust. This is the name federated users see when choosing which identity provider to use when signing in to the Console, so consider making this a friendly, intuitive name your users will understand. The name must be unique across all identity providers you add to the tenancy. You cannot change this later. 
    2. **Description:** A friendly description.
    3. **Type:** Select **Microsoft Active Directory Federation Service (ADFS) or SAML 2.0 Compliant Identity Provider**.
    4. **XML:** Upload the metadata.xml document that you downloaded from your IdP.
    5. **Encrypt Assertion:** Selecting the checkbox lets the IAM service know to expect the encryption from the IdP. If you select this checkbox, you must also set up encryption of the assertion in your IdP. For more information, see Encrypt Assertion under [General Concepts](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#concepts). See also your IdP's documentation.
    6. **Force Authentication:** Selected by default. When selected, users are required to provide their credentials to the IdP (re-authenticate) even when they are already signed in to another session. 
    7. **Authentication Context Class References:** This field is required for Government Cloud customers. When one or more values are specified, Oracle Cloud Infrastructure (the relying party), expects the identity provider to use one of the specified authentication mechanisms when authenticating the user. The returned SAML response from the IdP must contain an authentication statement with that authentication context class reference. If the SAML response authentication context does not match what is specified here, the Oracle Cloud Infrastructure auth service rejects the SAML response with a 400. Several common authentication context class references are listed in the menu. To use a different context class, select **Custom** , then manually enter the class reference. 
    8. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  5. Select **Continue**.
  6. Set up the mappings between the IdP groups and IAM groups in Oracle Cloud Infrastructure. A given IdP group can be mapped to zero, one, or multiple IAM groups, and conversely. However, each individual mapping is between only a single IdP group and a single IAM group. Changes to group mappings take effect typically within seconds in your home region, but may take several minutes to propagate to all regions.
**Note**
If you don't want to set up the group mappings now, you can simply select **Create** and come back to add the mappings later. 
To create a group mapping:
    1. Under **Identity Provider Group** , enter the name of the group in your IdP. You must enter the name exactly, including the correct case.
Choose the IAM group you want to map this group to from the list under **OCI Group**.
**Tip** Requirements for IAM group name: No spaces. Allowed characters: letters, numerals, hyphens, periods, underscores, and plus signs (+). The name cannot be changed later. 
    2. Repeat the above sub-steps for each mapping you want to create, and then select **Create**.


The identity provider is now added to your tenancy and appears in the list on the **Federation** page. Select the identity provider to view its details and the group mappings you just set up.
Oracle assigns the identity provider and each group mapping a unique ID called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Resource_Identifiers). 
In the future, come to the **Federation** page if you want to edit or add group mappings or delete the identity provider from your tenancy.
**Step 6: Set up IAM policies for the groups**
If you haven't already, set up IAM policies to control the access the federated users have to your organization's Oracle Cloud Infrastructure resources. For more information, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
**Step 7: Give your federated users the name of the tenant and URL to sign in**
The federated users need the URL for the Oracle Cloud Infrastructure Console: <https://cloud.oracle.com>, and the name of your tenant. They'll be prompted to provide the tenant name when they sign in to the Console. 
## Managing Identity Providers in the Console 🔗 
[To add an identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm)
See [Instructions for Federating](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm#Instruc).
[To delete an identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm)
All the group mappings for the identity provider will also be deleted.
  1. Delete the identity provider from your tenancy:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**.
A list of the identity providers in your tenancy is displayed.
    2. Select the identity provider to view its details.
    3. Select**Delete**.
    4. Confirm when prompted.
  2. Follow your IdP's documentation to delete the application from your IdP.


[To add group mappings for an identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
A list of the identity providers in your tenancy is displayed.
  2. Select the identity provider to view its details.
  3. Select**Add Mappings**. 
    1. Enter the IdP group name exactly in the **Identity Provider Group** text box.
    2. Choose the IAM group you want to map this group to from the list under **OCI Group**.
    3. To add more mappings, select **+Another Mapping.**
    4. When you are finished, select **Add Mappings**.


Your changes take effect typically within seconds in your home region. Wait several more minutes for changes to propagate to all regions
[To update a group mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm)
You can't update a group mapping, but you can delete the mapping and add a new one.
[To delete a group mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
A list of the identity providers in your tenancy is displayed.
  2. Select the identity provider to view its details.
  3. For the mapping you want to delete, select it, and then select **Delete**.
  4. Confirm when prompted.


Your changes take effect typically within seconds in your home region. Wait several more minutes for changes to propagate to all regions.
## Managing Identity Providers in the API 🔗 
For information about using the API and signing requests, see [REST API documentation](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm) and [Security Credentials](https://docs.oracle.com/iaas/Content/General/Concepts/credentials.htm). For information about SDKs, see [SDKs and the CLI](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
Use these API operations: 
**Identity providers:**
  * [CreateIdentityProvider](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdentityProvider/CreateIdentityProvider)
  * [ListIdentityProviders](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdentityProvider/ListIdentityProviders)
  * [GetIdentityProvider](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdentityProvider/GetIdentityProvider)
  * [UpdateIdentityProvider](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdentityProvider/UpdateIdentityProvider)
  * [DeleteIdentityProvider](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdentityProvider/DeleteIdentityProvider): Before you can use this operation, you must first use [DeleteIdpGroupMapping](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdpGroupMapping/DeleteIdpGroupMapping) to remove all the group mappings for the identity provider.

**Group mappings:**
  * [CreateIdpGroupMapping](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdpGroupMapping/CreateIdpGroupMapping): Each group mapping is a separate entity with its own OCID.
  * [ListIdpGroupMappings](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdpGroupMapping/ListIdpGroupMappings)
  * [GetIdpGroupMapping](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdpGroupMapping/GetIdpGroupMapping)
  * [UpdateIdpGroupMapping](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdpGroupMapping/UpdateIdpGroupMapping)
  * [DeleteIdpGroupMapping](https://docs.oracle.com/iaas/api/#/en/identity/latest/IdpGroupMapping/DeleteIdpGroupMapping)


Was this article helpful?
YesNo

