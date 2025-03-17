Updated 2025-01-14
# Federating with Microsoft Active Directory
This topic describes how to federate with Microsoft Active Directory using Microsoft Active Federation Services (AD FS).
**Note**
Before following the steps in this topic, see [Federating with Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top) to ensure that you understand general federation concepts. 
## About Federating with Microsoft Active Directory 🔗 
Your organization can have multiple Active Directory accounts (for example, one for each division of the organization). You can federate multiple Active Directory accounts with Oracle Cloud Infrastructure, but each federation trust that you set up must be for a single Active Directory account. 
To federate with Active Directory, you set up a trust between Active Directory and Oracle Cloud Infrastructure. To set up this trust, you perform some steps in the Oracle Cloud Infrastructure Console and some steps in Active Directory Federation Services.
Following is the general process an administrator goes through to set up federation with Active Directory. Details for each step are given in the sections below. 
  1. Get required information from Active Directory Federation Services. 
  2. Federate Active Directory with Oracle Cloud Infrastructure:
    1. Add the identity provider (AD FS) to your tenancy and provide the required information.
    2. Map Active Directory groups to IAM groups.
  3. In Active Directory Federation Services, add Oracle Cloud Infrastructure as a trusted, relying party.
  4. In Active Directory Federation Services, add the claim rules required in the authentication response by Oracle Cloud Infrastructure.
  5. Test your configuration by logging in to Oracle Cloud Infrastructure with your Active Directory credentials.


## Federating with Active Directory 🔗 
**Prerequisites**
You have installed and configured Microsoft Active Directory Federation Services for your organization.
You have set up groups in Active Directory to map to groups in Oracle Cloud Infrastructure.
**Tip** Consider naming Active Directory groups that you intend to map to Oracle Cloud Infrastructure groups with a common prefix, to make it easy to apply a filter rule. For example, OCI_Administrators, OCI_NetworkAdmins, OCI_InstanceLaunchers.
### Step 1: Get required information from Active Directory Federation Services  🔗 
**Summary:** Get the SAML metadata document and the names of the Active Directory groups that you want to map to Oracle Cloud Infrastructure Identity and Access Management groups.
  1. Locate the SAML metadata document for your AD FS federation server. By default, it is at this URL:
Copy
```
https://<yourservername>/FederationMetadata/2007-06/FederationMetadata.xml
```

Download this document and make a note of where you save it. You will upload this document to the Console in the next step.
  2. Note all the Active Directory groups that you want to map to Oracle Cloud Infrastructure IAM groups. You will need to enter these in the Console in the next step.


### Step 2: Add Active Directory as an identity provider in Oracle Cloud Infrastructure 🔗 
**Summary:** Add the identity provider to your tenancy. You can set up the group mappings at the same time, or set them up later. 
  1. Go to the Console and sign in with your Oracle Cloud Infrastructure login and password.
  2. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
  3. Select **Add identity provider**. 
  4. Enter the following:
    1. **Display Name:** A unique name for this federation trust. This is the name federated users see when choosing which identity provider to use when signing in to the Console. The name must be unique across all identity providers you add to the tenancy. You cannot change this later. 
    2. **Description:** A friendly description.
    3. **Type:** Select Microsoft Active Directory Federation Services (ADFS) or SAML 2.0 compliant identity provider.
    4. **XML:** Upload the FederationMetadata.xml file you downloaded from Azure AD.
    5. Select **Show Advanced Options**.
    6. **Encrypt Assertion:** Selecting the checkbox lets the IAM service know to expect the encryption from IdP. Do not select this checkbox unless you have enabled assertion encryption in Azure AD.
To enable assertion encryption for this single sign-on application in Azure AD, set up the SAML Signing Certificate in Azure AD to sign the SAML response and assertion. For more information, see the [Azure AD documentation](https://docs.microsoft.com/azure/active-directory/manage-apps/certificate-signing-options).
    7. **Force Authentication:** Selected by default. When selected, users are required to provide their credentials to the IdP (re-authenticate) even when they are already signed in to another session. 
    8. **Authentication Context Class References:** This field is required for Government Cloud customers. When one or more values are specified, Oracle Cloud Infrastructure (the relying party), expects the identity provider to use one of the specified authentication mechanisms when authenticating the user. The returned SAML response from the IdP must contain an authentication statement with that authentication context class reference. If the SAML response authentication context does not match what is specified here, the Oracle Cloud Infrastructure auth service rejects the SAML response with a 400. Several common authentication context class references are listed in the menu. To use a different context class, select **Custom** , then manually enter the class reference. 
    9. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  5. Select **Continue**.
  6. Set up the mappings between Active Directory groups and IAM groups in Oracle Cloud Infrastructure. A given Active Directory group can be mapped to zero, one, or multiple IAM groups, and vice versa. However, each individual mapping is between only a single Active Directory group and a single IAM group. Changes to group mappings take effect typically within seconds in your home region, but may take several minutes to propagate to all regions.
**Note**
If you don't want to set up the group mappings now, you can simply select **Create** and come back to add the mappings later. 
To create a group mapping:
    1. Under **Identity Provider Group** , enter the Active Directory group name. You must enter the name exactly, including the correct case.
Choose the IAM group you want to map this group to from the list under **OCI Group**.
**Tip** Requirements for IAM group name: No spaces. Allowed characters: letters, numerals, hyphens, periods, underscores, and plus signs (+). The name cannot be changed later. 
    2. Repeat the above sub-steps for each mapping you want to create, and then select **Create**.


The identity provider is now added to your tenancy and appears in the list on the **Federation** page. Select the identity provider to view its details and the group mappings you just set up.
Oracle assigns the identity provider and each group mapping a unique ID called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Resource_Identifiers). 
In the future, come to the **Federation** page if you want to edit the group mappings or delete the identity provider from your tenancy.
### Step 3: Copy the URL for the Oracle Cloud Infrastructure Federation Metadata document
**Summary:** The Federation page displays a link to the Oracle Cloud Infrastructure Federation Metadata document. Before you move on to configuring Active Directory Federation Services, you need to copy the URL. 
  1. On the Federation page, select **Download this document**.
  2. Copy the URL. The URL looks similar to:
Copy
```
https://auth.r2.oracleiaas.com/v1/saml/ocid1.tenancy.oc1..aaaaaaaaqdt2tvdmhsa3jmvc5dzulgs3pcv6imfwfgdya4aq/metadata.xml
```



### Step 4: In Active Directory Federation Services, add Oracle Cloud Infrastructure as a trusted relying party  🔗 
  1. Go to the AD FS Management Console and sign in to the account you want to federate. 
  2. Add Oracle Cloud Infrastructure as a **trusted relying party** : 
    1. From the AD FS Management Console, right-click AD FS and select **Add Relying Party Trust**. 
    2. In the **Add Relying Party Trust Wizard** , select **Start**.
    3. Select **Import data about the relying party published online or on a local network**. 
Paste the Oracle Cloud Infrastructure Federation Metadata URL that you copied in Step 3. Select **Next**.
AD FS will connect to the URL. If you get an error during the attempt to read the federation metadata, you can alternatively upload the Oracle Cloud Infrastructure Federation Metadata XML document.
[To upload the federation metadata document](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm)
      1. In a web browser, paste the Oracle Cloud Infrastructure Federation Metadata URL in the address bar.
      2. Save the XML document to a location that is accessible by your AD FS Management Console. 
      3. In the **Select Data Source** step of the **Add Relying Party Trust Wizard** , select **Import data about the relying party from a file**.
      4. Select **Browse** and select the metadata.xml file that you saved.
      5. Select **Next**.
    4. Set the display name for the relying party (for example, Oracle Cloud Infrastructure) and then select **Next**.
    5. Select **I do not want to configure multifactor authentication settings for this relying party trust at this time**.
    6. Choose the appropriate Issuance Authorization Rules to either permit or deny all users access to the relying party. Note that if you choose "Deny", then you must later add the authorization rules to enable access for the appropriate users. 
Select **Next**.
    7. Review the settings and select **Next**.
    8. Check **Open the Edit Claim Rules** dialog for this relying part trust when the wizard closes and then select **Close**.


### Step 5: Add the claim rules for the Oracle Cloud Infrastructure relying party
Summary: Add the claim rules so that the elements that Oracle Cloud Infrastructure requires (Name ID and groups) are added to the SAML authentication response. 
**Add the Name ID rule:**
  1. In the **Add Transform Claim Rule Wizard** , select **Transform an Incoming Claim** , and select **Next**.
  2. Enter the following:
     * **Claim rule name:** Enter a name for this rule, for example, nameid.
     * **Incoming claim type:** Select Windows account name.
     * **Outgoing claim type:** Select Name ID.
     * **Outgoing name ID format:** Select Persistent Identifier.
     * Select**Pass through all claim value**.
     * Select **Finish**.
  3. The rule is displayed in the rules list. Select **Add Rule**.


**Add the groups rule:**
**Important** Any users who are in more than 100 IdP groups cannot be authenticated to use the Oracle Cloud InfrastructureConsole. To enable authentication, apply a filter to the groups rule, as described below.
[If your Active Directory users are in no more than 100 groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm)
**Add the groups rule:**
  1. Under Claim rule template, select **Send Claims Using a Custom Rule**. Select **Next**.
  2. In the **Add Transform Claim Rule Wizard** , enter the following:
    1. **Claim rule name:** Enter groups.
    2. **Custom rule:** Enter the following custom rule:
Copy
```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"] => issue(store = "Active Directory", types = ("https://auth.oraclecloud.com/saml/claims/groupName"), query = ";tokenGroups;{0}", param = c.Value);
```

    3. Select **Finish**.


[If your Active Directory users are in more than 100 groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm)
**Add the groups rule with a filter:**
To limit the groups sent to Oracle Cloud Infrastructure, create two custom claim rules. The first one retrieves all groups the user belongs to directly and indirectly. The second rule applies a filter to limit the groups passed to the service provider to only those that match the filter criteria.
Add the first rule:
  1. In the Edit Claim Rules dialog, select **Add Rule**.
  2. Under Claim rule template, select **Send Claims Using a Custom Rule**. Select **Next**.
  3. In the **Add Transform Claim Rule Wizard** , enter the following:
    1. **Claim rule name:** Enter a name, for example, groups.
    2. **Custom rule:** Enter the following custom rule:
```
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"] => add(store = "Active Directory", types = ("https://auth.oraclecloud.com/saml/claims/groupName"), query = ";tokenGroups;{0}", param = c.Value);
```

Note that in this custom rule you use `add` instead of `issue`. This command passes the results of the rule to the next rule, instead of sending the results to the service provider.
    3. Select **Finish**.
  4. Now add the filter rule. 
    1. In the Edit Claim Rules dialog, select **Add Rule**.
    2. Under Claim rule template, select **Send Claims Using a Custom Rule**. Select **Next**. 
    3. In the **Add Transform Claim Rule Wizard** , enter the following:
      1. **Claim rule name:** Enter groups.
      2. **Custom rule:** Enter an appropriate filter rule. For example to send only groups that begin with the string "OCI", enter the following:
Copy
```
c:[Type == "https://auth.oraclecloud.com/saml/claims/groupName", Value =~ "(?i)OCI"] => issue(claim = c);
```

This rule filters the list from the first rule to only those groups that begin with the string `OCI`. The `issue` command, sends the results of the rule to the service provider. 
You can create filters with the appropriate criteria for your organization. 
For information on AD FS syntax for custom rules, see the Microsoft document: [Understanding Claim Rule Language in AD FS 2.0 and Higher](https://social.technet.microsoft.com/wiki/contents/articles/4792.understanding-claim-rule-language-in-ad-fs-2-0-higher.aspx).
      3. Select **Finish**.


### Step 6: Set up IAM policies for the groups
If you haven't already, set up IAM policies to control the access the federated users have to your organization's Oracle Cloud Infrastructure resources. For more information, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
### Step 7: Give your federated users the name of the tenant and URL to sign in
Give federated users the URL for the Oracle Cloud Infrastructure Console, <https://cloud.oracle.com>, and the name of your tenant. They'll be prompted to provide the tenant name when they sign in to the Console. 
## Managing Identity Providers in the Console 🔗 
[To add an identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm)
See [About Federating with Microsoft Active Directory](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm#About_Federating_with_Microsoft_Active_Directory).
[To delete an identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm)
All the group mappings for the identity provider will also be deleted.
  1. Delete the identity provider from your tenancy:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
A list of the identity providers in your tenancy is displayed.
    2. Select the identity provider to view its details.
    3. Select**Delete**.
    4. Confirm when prompted.


[To add group mappings for an identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
A list of the identity providers in your tenancy is displayed.
  2. Select the identity provider to view its details.
  3. Select**Add Mappings**.
    1. Under **Identity Provider Group** , enter the Active Directory group name. The name you enter here must match exactly the name in Active Directory.
    2. Choose the IAM group you want to map this group to from the list under **OCI Group**.
    3. To add more mappings, select **+Another Mapping.**
    4. When you are finished, select **Add Mappings**.


Your changes take effect typically within seconds.
[To update a group mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm)
You can't update a group mapping, but you can delete the mapping and add a new one.
[To delete a group mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm)
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

