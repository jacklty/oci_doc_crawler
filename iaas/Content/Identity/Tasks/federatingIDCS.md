Updated 2025-01-14
# Federating with Oracle Identity Cloud Service
This topic points to the appropriate topics for federating Oracle Cloud Infrastructure with [Oracle Identity Cloud Service](https://www.oracle.com/cloud/paas/identity-cloud-service.html) depending on when you activated your tenancy.
## Tenancies created December 21, 2018 and after 🔗 
These tenancies are automatically federated with Oracle Identity Cloud Service and configured to provision federated users in Oracle Cloud Infrastructure. 
To manage your federated users and groups, see [Managing Oracle Identity Cloud Service Users and Groups in the Oracle Cloud Infrastructure Console](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#Managing_Oracle_Identity_Cloud_Service_Users_and_Groups_in_the_Oracle_Cloud_Infrastructure_Console).
For information about the federation, see [Find Out More About Oracle Identity Cloud Service Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/autofederationfaq.htm#Frequently_Asked_Questions_for_Oracle_Identity_Cloud_Service_Federated_Users).
## Tenancies created between December 18, 2017 and December 20, 2018 🔗 
These tenancies are automatically federated with Oracle Identity Cloud Service but are not configured to provision federated users in Oracle Cloud Infrastructure to allow these users to have additional credentials (API keys, auth tokens, etc.).
To enable this feature for users, you need to perform a one-time upgrade, see: [User Provisioning for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingscim.htm#User_Provisioning_for_Federated_Users).
After you have performed this upgrade, see [Managing Oracle Identity Cloud Service Users and Groups in the Oracle Cloud Infrastructure Console](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/addingidcsusersandgroups.htm#Managing_Oracle_Identity_Cloud_Service_Users_and_Groups_in_the_Oracle_Cloud_Infrastructure_Console) to manage your federated users and groups.
## Tenancies created before December 18, 2017 🔗 
These tenancies must be manually federated with Oracle Identity Cloud Service. See [Federating with Oracle Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#top) described below.
## Manually Federating with Oracle Identity Cloud Service 🔗 
Your organization can have multiple Oracle Identity Cloud Service accounts (e.g., one for each division of the organization). You can federate multiple Identity Cloud Service accounts with Oracle Cloud Infrastructure, but each federation trust that you set up must be for a single Identity Cloud Service account. 
**Note**
Before following the steps in this topic, see [Federating with Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#top) to ensure that you understand general federation concepts. 
## Components of the Manual Federation to Understand 🔗 
### Web Application and Client Credentials 🔗 
For each trust, you must set up a _web application_ in Oracle Identity Cloud Service (also called a _trusted application_); instructions are in [Instructions for Federating with Oracle Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#Instruct). The resulting application has a set of client credentials (a client ID and client secret). When you federate your Identity Cloud Service account with Oracle Cloud Infrastructure, you must provide these credentials.
### COMPUTEBAREMETAL application 🔗 
A _trusted application_ in Oracle Identity Cloud Service that contains the set of client credentials (a client ID and client secret) you'll need to provide when you federate your Identity Cloud Service account with Oracle Cloud Infrastructure.
### Required URLs 🔗 
The easiest way to federate with Oracle Identity Cloud Service is through the Oracle Cloud Infrastructure Console, although you could do it programmatically with the API. If you're using the Console, you're asked to provide a _base URL_ instead of the metadata URL. The base URL is the left-most part of the URL in the browser window when you're signed in to the Identity Cloud Service console:
  * **Base URL:** <Identity Cloud Service account name>.identity.oraclecloud.com 


If you're using the API to federate, you need to provide the metadata URL, which is the base URL with /fed/v1/metadata appended, like so:
  * **Metadata URL:** <Identity Cloud Service account name>.identity.oraclecloud.com/fed/v1/metadata


The metadata URL links directly to the IdP-provided XML required to federate. If you're using the API, you need to provide both the metadata URL and the metadata itself when federating. For more information, see [Managing Identity Providers in the API](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#Managing).
### OCI-V2-<tenancy_name> app 🔗 
When you manually federate an Oracle Identity Cloud Service account with Oracle Cloud Infrastructure, a new SAML application called _OCI-V2- <tenancy_name>_ is automatically created in that Oracle Identity Cloud Service account. If you later need to delete the Oracle Identity Cloud Service identity provider from your Oracle Cloud Infrastructure tenancy, make sure to also delete the OCI-V2-<tenancy_name> from Oracle Identity Cloud Service. If you don't, and you later try to federate the same Oracle Identity Cloud Service account again, you'll get a 409 error saying that an application with the same name already exists (that is, OCI-V2-<tenancy_name>).
#### Provisioned User
A provisioned user is provisioned by Oracle Identity Cloud Service in Oracle Cloud Infrastructure and is synched to a federated user that is managed in Oracle Identity Cloud Service. The provisioned user can have the special Oracle Cloud Infrastructure credentials like API keys and auth tokens to enable programmatic access. Provisioned users cannot have Console passwords. 
## Instructions for Federating with Oracle Identity Cloud Service 🔗 
Following is the general process an administrator goes through to set up the identity provider, and below are instructions for each step. It's assumed that the administrator is an Oracle Cloud Infrastructure user with the required credentials and access.
  1. Sign in to Oracle Identity Cloud Service. Perform one of the following, as appropriate: 
Option A: Get the required information from the COMPUTEBAREMETAL application you'll need to perform the set up steps in Oracle Cloud Infrastructure. 
Option B: If Oracle Identity Cloud Service does not include the COMPUTEBAREMETAL application, set up a trusted application.
  2. In Oracle Cloud Infrastructure, set up the federation:
    1. Set up Oracle Identity Cloud Service as an identity provider.
    2. Map Oracle Identity Cloud Service groups to IAM groups.
  3. In Oracle Cloud Infrastructure, set up the IAM policies for the IAM groups to define the access you want the members of the mapped groups to have. 
  4. Inform your users of the name of your Oracle Cloud Infrastructure tenant and the URL for the Console, <https://cloud.oracle.com>. 


[Step 1: Get required information from Oracle Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm)
[Option A: Get information from the COMPUTEBAREMETAL application](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm)
  1. Go to the Oracle Identity Cloud Service console and sign in with admin privileges. Make sure you're viewing the Admin Console. 
  2. In the Identity Cloud Service console, select **Applications**. The list of trusted applications is displayed.
  3. Select COMPUTEBAREMETAL. If your instance does not include the COMPUTEBAREMETAL application, perform **Step 1 Option B** , instead.
  4. Select **Configuration**.
  5. Expand **General Information**. The client ID is displayed. Select **Show Secret** to display the client secret.
[![Screenshot shows the client secret key in the Oracle Identity Cloud Service console](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_fed_secret.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_fed_secret.png)
  6. Record the Client ID and Client Secret. They look similar to this:
     * Client ID: de06b81cb45a45a8acdcde923402a9389d8
     * Client Secret: 8a297afd-66df-49ee-c67d-39fcdf3d1c31


[Option B: Set up a trusted application and get required information from Oracle Identity Cloud Service ](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm)
Perform this step only if you were unable to complete Step 1 Option A.
**Summary:** For Oracle Identity Cloud Service, you need to create a _confidential application_ (also referred to as a _trusted application_) with particular properties described in the following instructions. For the general Oracle Identity Cloud Service documentation, see [Add a Confidential Application](http://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/adding-trusted-application.html). 
**Instructions for Oracle Identity Cloud Service:**
  1. Go to the Oracle Identity Cloud Service console and sign in with privileges to create the application. Make sure you're viewing the Admin Console. 
  2. [Add a confidential (or trusted) application](http://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/adding-trusted-application.html), which enables secure, programmatic interaction between Oracle Cloud Infrastructure and Oracle Identity Cloud Service. Specify these items when setting up the application: 
    1. On the first page: 
      1. Enter an application a name (e.g., Oracle Cloud Infrastructure Federation). 
      2. Leave other fields empty or unselected.
    2. On the next page:
      1. Select **Configure this application as a client now**.
      2. For the **Allowed Grant Types** , select the checkbox for **Client Credentials**.
      3. Leave other fields empty.
      4. At the bottom of the page: 
        1. Select the checkbox for **Grant the client access to Identity Cloud Service Admin APIs**.
        2. Select **Identity Domain Administrator** from the list of roles.
    3. On the next page, leave any fields empty or unselected and continue until you select **Finish**.
    4. Copy and paste the displayed client credentials so you can later give them to Oracle Cloud Infrastructure when federating. You can view the application's client credentials any time in the Oracle Identity Cloud Service console. They look similar to this: 
       * Client ID: de06b81cb45a45a8acdcde923402a9389d8
       * Client Secret: 8a297afd-66df-49ee-c67d-39fcdf3d1c31
  3. Record the [Oracle Identity Cloud Service base URL](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#Required), which you'll need when federating.
  4. [Activate the application](http://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/activating-applications.html).


[Step 2: Add Oracle Identity Cloud Service as an identity provider in Oracle Cloud Infrastructure](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm)
  1. Go to the [Console](https://cloud.oracle.com/) and sign in with your Oracle Cloud Infrastructure login and password.
  2. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**.
  3. Select **Add identity provider**. 
  4. Enter the following:
    1. **Name:** A unique name for this federation trust. This is the name federated users see when choosing which identity provider to use when signing in to the Console (for example., _ABCCorp_IDCS_ as shown in the screenshot in [Experience for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#Experien)). The name must be unique across all identity providers you add to the tenancy. You cannot change this later. 
    2. **Description:** A friendly description.
    3. **IDCS Base URL:** See [Required URLs](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#Required).
    4. **Client ID:** From [Step 1](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#Step) Option A or Option B.
    5. **Client secret:** From [Step 1](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#Step) Option A or Option B.
    6. **Encrypt Assertion:** Selecting the checkbox lets the IAM service know to expect the encryption from the IdP. If you select this checkbox, you must also set up encryption of the assertion in IDCS. For more information, see [General Concepts](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#concepts). For information about setting this feature up in the IDCS, see [Managing Oracle Identity Cloud Service Applications](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/managing-oracle-identity-cloud-service-applications.html).
    7. **Force Authentication:** Selected by default. When selected, users are required to provide their credentials to the IdP (re-authenticate) even when they are already signed in to another session. 
    8. **Authentication Context Class References:** This field is required for Government Cloud customers. When one or more values are specified, Oracle Cloud Infrastructure (the relying party), expects the identity provider to use one of the specified authentication mechanisms when authenticating the user. The returned SAML response from the IdP must contain an authentication statement with that authentication context class reference. If the SAML response authentication context does not match what is specified here, the Oracle Cloud Infrastructure auth service rejects the SAML response with a 400. Several common authentication context class references are listed in the menu. To use a different context class, select **Custom** , then manually enter the class reference. 
    9. If you have permissions to create a resource, then you also have permissions to apply free-form tags to that resource. To apply a defined tag, you must have permissions to use the tag namespace. For more information about tagging, see [Resource Tags](https://docs.oracle.com/iaas/Content/General/Concepts/resourcetags.htm). If you're not sure whether to apply tags, skip this option or ask an administrator. You can apply tags later.
  5. Select **Continue**.
  6. Set up the mappings between Oracle Identity Cloud Service groups and IAM groups in Oracle Cloud Infrastructure. A given Oracle Identity Cloud Service group can be mapped to zero, one, or multiple IAM groups, and vice versa. However, each individual mapping is between only a single Oracle Identity Cloud Service group and a single IAM group. Changes to group mappings take effect typically within seconds.
**Note**
If you don't want to set up the group mappings now, you can simply select **Create** and come back to add the mappings later. 
To create a group mapping:
    1. Select the Oracle Identity Cloud Service group from the list under **Identity Provider Group**.
    2. Choose the IAM group you want to map this group to from the list under **OCI Group**.
**Tip** Requirements for IAM group name: No spaces. Allowed characters: letters, numerals, hyphens, periods, underscores, and plus signs (+). The name cannot be changed later. 
    3. Repeat the above sub-steps for each mapping you want to create, and then select **Create**.


#### After the Federation Set Up
The identity provider is now added to your tenancy and appears in the list on the **Federation** page. Select the identity provider to view its details and the group mappings you just set up.
Oracle assigns the identity provider and each group mapping a unique ID called an Oracle Cloud ID (OCID). For more information, see [Resource Identifiers](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/identifiers.htm#Resource_Identifiers). 
In the future, come to the **Federation** page if you want to edit the group mappings or delete the identity provider from your tenancy.
Users that are members of the Oracle Identity Cloud Service groups mapped to the Oracle Cloud Infrastructure groups are now listed in the Console on the Users page. See [Managing User Capabilities for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm#Managing_User_Capabilities_for_Federated_Users) for more information on assigning these users additional credentials.
[Step 3: Set up IAM policies for the groups](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm)
If you haven't already, set up IAM policies to control the access the federated users have to your organization's Oracle Cloud Infrastructure resources. For more information, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top).
[Step 4: Give your federated users the name of the tenant and URL to sign in](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm)
Give your federated users need the URL for the Oracle Cloud Infrastructure Console, <https://cloud.oracle.com>), and the name of your tenant. They'll be prompted to provide the tenant name when they sign in to the Console. 
## Managing Identity Providers in the Console 🔗 
[To add an Oracle Identity Cloud Service as an identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm)
See [Instructions for Federating with Oracle Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#Instruct).
[To delete the identity provider](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm)
All the group mappings will also be deleted.
  1. Delete the identity provider from your tenancy:
    1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**.
A list of the identity providers in your tenancy is displayed.
    2. Select the identity provider to view its details.
    3. Select**Delete**.
    4. Confirm when prompted.
  2. Delete the [_OCI-V2- <tenancy_name>_](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#BMCS-SAM) from your Oracle Identity Cloud Service account:
    1. Go to Oracle Identity Cloud Service and sign in to the federated account.
    2. Select **Applications**. The list of applications is displayed.
    3. Locate the _OCI-V2- <tenancy_name>_ and select its name to view its details page.
    4. In the upper right of the page, select **Deactivate**. Confirm when prompted.
    5. Select **Remove**. Confirm when prompted.


[To add group mappings for Oracle Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm)
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
A list of the identity providers in your tenancy is displayed.
  2. Select the name you chose for your Oracle Identity Cloud Service federation to view its details.
  3. Select **Add Mappings**.
    1. Select the Oracle Identity Cloud Service group from the list under **Identity Provider Group**.
    2. Choose the IAM group you want to map this group to from the list under **OCI Group**.
    3. To add more mappings, select **+Another Mapping.**
    4. When you are finished, select **Add Mappings**.


Your changes take effect typically within seconds in your home region. Wait several more minutes for changes to propagate to all regions. 
Users that are members of the Oracle Identity Cloud Service groups mapped to the Oracle Cloud Infrastructure groups are now listed in the Console on the Users page. See [Managing User Capabilities for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm#Managing_User_Capabilities_for_Federated_Users) for more information on assigning these users additional credentials.
[To update or delete a group mapping](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm)
You can't update a group mapping, but you can delete the mapping and add a new one.
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
A list of the identity providers in your tenancy is displayed.
  2. Select the identity provider to view its details.
  3. For the mapping you want to delete, select it, and then select **Delete**.
  4. Confirm when prompted.
  5. Add a new mapping, if wanted.


Your changes take effect typically within seconds in your home region. Wait several more minutes for changes to propagate to all regions.
If this action results in federated users no longer having membership in any group that is mapped to Oracle Cloud Infrastructure, the federated users' provisioned users' will also be removed from Oracle Cloud Infrastructure. Typically, this process takes several minutes.
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

