Updated 2025-01-14
# Federating with Microsoft Azure Active Directory
This topic describes how to federate with Microsoft Azure Active Directory (AD).
**Note**
Before following the steps in this topic, see [Federating with Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top) to ensure that you understand general federation concepts. 
## About Federating with Azure AD 🔗 
To federate with Azure AD, you set up Oracle Cloud Infrastructure as a basic SAML single sign-on application in Azure AD. To set up this application, you perform some steps in the Oracle Cloud Infrastructure Console and some steps in Azure AD.
Following is the general process an administrator goes through to set up the federation. Details for each step are given in the next section. 
  1. In Oracle Cloud Infrastructure, download the federation metadata document. 
  2. In Azure AD, set up Oracle Cloud Infrastructure Console as an enterprise application. 
  3. In Azure AD, configure the Oracle Cloud Infrastructure enterprise application for single sign-on.
  4. In Azure AD, set up the user attributes and claims.
  5. In Azure AD, download the Azure AD SAML metadata document.
  6. In Azure AD, assign user groups to the application.
  7. In Oracle Cloud Infrastructure, set up Azure AD as an identity provider.
  8. In Oracle Cloud Infrastructure, map your Azure AD groups to Oracle Cloud Infrastructure groups.
  9. In Oracle Cloud Infrastructure, set up the IAM policies to govern access for your Azure AD groups.
  10. Share the Oracle Cloud Infrastructure sign-in URL with your users.


## Steps to Federate with Azure AD 🔗 
**Prerequisites**
You have an Azure tenancy with groups and users set up in Azure AD.
### Step 1: In Oracle Cloud Infrastructure, download the federation metadata document 🔗 
**Summary:** The Oracle Cloud Infrastructure Console Federation page displays a link to the Oracle Cloud Infrastructure federation metadata document. Before you set up the application in Azure AD, you need to download the document. 
  1. Go to the **Federation** page: Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**.
  2. On the Federation page, select **Download this document**.
[![Download link on Console Federation page](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federation_downloandlink.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federation_downloandlink.png)
After you select the link, the metadata.xml document opens in your browser window. Use your browser's **Save page as** command to save the xml document locally where you can access it later. 


### Step 2: In Azure AD, add Oracle Cloud Infrastructure as an enterprise application 🔗 
  1. In the Azure portal, on the left navigation panel, select **Azure Active Directory**.
  2. In the **Azure Active Directory** pane, select **Enterprise applications**. A sample of the applications in your Azure AD tenant is displayed.
  3. At the top of the **All applications** pane, select **New application**.
  4. In the **Add from gallery** region, enter **Oracle Cloud Infrastructure Console** in the search box. 
  5. Select the Oracle Cloud Infrastructure Console application from the results.
  6. In the application-specific form, you can edit information about the application. For example, you can edit the name of the application.
  7. When you are finished editing the properties, select **Create**.
The getting started page is displayed with the options for configuring the application for your organization.


### Step 3: In Azure AD, configure Oracle Cloud Infrastructure as an enterprise application 🔗 
  1. Under the **Manage** section, select **Single sign-on**.
[![Azure AD Single sign-on option](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_sso.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_sso.png)
  2. Select **SAML** to configure single sign-on. The **Set up Single Sign-On with SAML** page is displayed.
  3. At the top of the page, select **Upload metadata file**. 
[![Azure AD upload metadata link](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_metadatafile.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_metadatafile.png)
  4. Locate the federation metadata file (metadata.xml) you downloaded from Oracle Cloud Infrastructure in Step 1, and upload it here. After you upload the file, these **Basic SAML Configuration** fields are automatically populated:
     * Identifier (Entity ID)
     * Reply URL (Assertion Consumer Service URL)
  5. In the **Basic SAML Configuration** section, select**Edit**. On the **Basic SAML Configuration** pane, enter the following required field:
     * **Sign on URL:** Enter the URL in the following format:
`https://cloud.oracle.com`
[![Azure AD Basic SAML Configuration panel](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_basicsaml.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_basicsaml.png)
  6. Select **Save**.


### Step 4: Configure User Attributes & Claims 🔗 
The Oracle Cloud Infrastructure Console enterprise application template is seeded with the required attributes, so you don't need to add any. However, you do need to make the following customizations:
  1. In the **User Attributes & Claims** section, select **Edit** in the upper-right corner. The **Manage claim** panel is displayed.
  2. Next to the **Name identifier value** field, select **Edit**.
     * Under **Required claim** , select Unique User Identifier (Name ID) .
     * Select **Email address** and change it to **Persistent**.
     * For **Source** , select Attribute.
     * For **Source attribute** , select user.userprincipalname.
[![Azure AD Manage User Claims panel](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_userclaims.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_userclaims.png)
     * Select **Save**.
  3. Select **Add a group claim**.
  4. In the **Group Claims** panel, configure the following:
     * Select Security groups.
     * **Source attribute:** Select Group ID.
     * Under **Advanced Options** , select **Customize the name of the group claim**.
     * In the **Name** field, enter: groupName.
Ensure that you enter groupName with spelling and case exactly as given.
     * In the **Namespace** field, enter: `https://auth.oraclecloud.com/saml/claims`
[![Azure AD Group Claims panel](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_groupclaims.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_groupclaims.png)
     * Select **Save**.


### Step 5: Download the SAML metadata document 🔗 
  1. In the **SAML Signing Certificate** section, select the download link next to **Federation Metadata XML**. 
  2. Download this document and make a note of where you save it. You will upload this document to the Console in the next step.


### Step 6: Assign user groups to the application 🔗 
To enable Azure AD users to sign in to Oracle Cloud Infrastructure, you need to assign the appropriate user groups to your new enterprise application. 
  1. On the left navigation pane, under **Manage** , select **Users and Groups**.
  2. Select **Add** at the top of the **Users and Groups** list to open the **Add Assignment** pane.
  3. Select the **Users and groups** selector.
  4. Enter the name of the group you want to assign to the application into the **Search by name or email address** search box.
  5. Hover over the group in the results list to display a checkbox. Select the checkbox to add the group to the **Selected** list.
  6. When you are finished selecting groups, select **Select** to add them to the list of users and groups to be assigned to the application.
  7. Select **Assign** to assign the application to the selected groups.


### Step 7: Add Azure AD as an identity provider in Oracle Cloud Infrastructure 🔗 
**Summary:** Add the identity provider to your tenancy. You can set up the group mappings at the same time, or set them up later. 
  1. Go to the Console and sign in with your Oracle Cloud Infrastructure username and password.
  2. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
  3. Select **Add identity provider**. 
  4. Enter the following:
    1. **Display Name:** A unique name for this federation trust. This is the name federated users see when choosing which identity provider to use when signing in to the Console. The name must be unique across all identity providers you add to the tenancy. You cannot change this later. 
    2. **Description:** A friendly description.
    3. **Type:** Select  SAML 2.0 compliant identity provider.
    4. **XML:** Upload the FederationMetadata.xml file you downloaded from Azure AD.
    5. Select **Show Advanced Options**.
    6. **Encrypt Assertion:** Selecting the checkbox lets the IAM service know to expect the encryption from IdP. Do not select this checkbox unless you have enabled assertion encryption in Azure AD.
To enable assertion encryption for this single sign-on application in Azure AD, set up the SAML Signing Certificate in Azure AD to sign the SAML response and assertion. For more information, see the [Azure AD documentation](https://docs.microsoft.com/azure/active-directory/manage-apps/certificate-signing-options).
    7. **Force Authentication:** Selected by default. When selected, users are required to provide their credentials to the IdP (re-authenticate) even when they are already signed in to another session. 
    8. **Authentication Context Class References:** This field is required for Government Cloud customers. When one or more values are specified, Oracle Cloud Infrastructure (the relying party), expects the identity provider to use one of the specified authentication mechanisms when authenticating the user. The returned SAML response from the IdP must contain an authentication statement with that authentication context class reference. If the SAML response authentication context does not match what is specified here, the Oracle Cloud Infrastructure auth service rejects the SAML response with a 400. Several common authentication context class references are listed in the menu. To use a different context class, select **Custom** , then manually enter the class reference. 
    9. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  5. Select **Continue**.
**Note**
If you don't want to set up the group mappings now, you can simply select **Create** and come back to add the mappings later. 


### Step 8: Add group mappings 🔗 
Summary: Set up the mappings between Azure AD groups and IAM groups in Oracle Cloud Infrastructure. A given Azure AD group can be mapped to zero, one, or multiple IAM groups, and vice versa. However, each individual mapping is between only a single Azure AD group and a single IAM group. Changes to group mappings take effect typically within seconds in your home region, but may take several minutes to propagate to all regions. Note that the Azure AD groups that you choose to map must also be assigned to the enterprise application in Azure AD. See [Step 6: Assign user groups to the application](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFSazure.htm#Step6).
**Before you begin:** Have your Azure AD groups page open. From the Azure Dashboard, under **Manage** , select **Groups**. From the list of groups, select the group you want to map to an Oracle Cloud Infrastructure group. In the group's details page, select the **Copy** icon next to the Object ID for the group.
To create a group mapping:
  1. For **Identity Provider Group** , enter (or paste) the Object ID of the Azure AD group. You must enter the Object ID exactly, including the correct case. An example Object ID looks like: aa0e7d64-5b2c-623g-at32-65058526179c
[![Mapping an Azure AD group to an OCI group](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_mapping.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federationazure_mapping.png)
  2. Choose the IAM group you want to map this group to from the list under **OCI Group**.
  3. Repeat the preceding steps for each mapping you want to create, and then select **Create**.


**Tip** Requirements for IAM group name: No spaces. Allowed characters: letters, numerals, hyphens, periods, underscores, and plus signs (+). The name cannot be changed later. 
The identity provider is now added to your tenancy and appears in the list on the **Federation** page. Select the identity provider to view its details and the group mappings you just set up.
Oracle assigns the identity provider and each group mapping a unique ID called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Resource_Identifiers). 
In the future, come to the **Federation** page if you want to edit the group mappings or delete the identity provider from your tenancy.
### Step 9: Set up IAM policies for the groups 🔗 
If you haven't already, set up IAM policies to control the access the federated users have to your organization's Oracle Cloud Infrastructure resources. For more information, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
### Step 10: Give your federated users the name of the tenant and URL to sign in 🔗 
The federated users need the URL for the Oracle Cloud Infrastructure Console (for example, Console) and the name of your tenant. They'll be prompted to provide the tenant name when they sign in to the Console. 
## Managing Identity Providers in the Console 🔗 
[To add an identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFSazure.htm)
See [About Federating with Azure AD](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFSazure.htm#About_Federating_with_Azure_AD).
[To delete an identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFSazure.htm)
All the group mappings for the identity provider will also be deleted.
  1. Delete the identity provider from your tenancy:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
A list of the identity providers in your tenancy is displayed.
    2. Select the identity provider to view its details.
    3. Select**Delete**.
    4. Confirm when prompted.


[To add group mappings for an identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFSazure.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
A list of the identity providers in your tenancy is displayed.
  2. Select the identity provider to view its details.
  3. Select**Add Mappings**.
    1. Under **Identity Provider Group** , select Custom Group. Enter (or paste) the Object ID of the Azure AD group. You must enter the Object ID exactly, including the correct case. An example Object ID looks like: aa0e7d64-5b2c-623g-at32-65058526179c. Note that for groups to be able to sign in to Oracle Cloud Infrastructure, they must also be assigned to the enterprise application in Azure AD. See [Step 6: Assign user groups to the application](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFSazure.htm#Step6).
    2. Choose the IAM group you want to map this group to from the list under **OCI Group**.
    3. To add more mappings, select **+Another Mapping.**
    4. When you are finished, select **Add Mappings**.


Your changes take effect typically within seconds.
[To update a group mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFSazure.htm)
You can't update a group mapping, but you can delete the mapping and add a new one.
[To delete a group mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFSazure.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
A list of the identity providers in your tenancy is displayed.
  2. Select the identity provider to view its details.
  3. For the mapping you want to delete, select it, and then select **Delete**.
  4. Confirm when prompted.


Your changes take effect typically within seconds.
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

