Updated 2025-01-14
# User Provisioning for Federated Users
This topic describes how you can use SCIM to provision federated users in Oracle Cloud Infrastructure. Provisioned federated users can have API keys and other service-specific credentials.
## Overview 🔗 
[SCIM (System for Cross-domain Identity Management)](http://www.simplecloud.info/) is an IETF standard protocol that enables user provisioning across identity systems. Oracle Cloud Infrastructure hosts a SCIM endpoint for provisioning federated users into Oracle Cloud Infrastructure. If your IdP is Oracle Identity Cloud Service or Okta, you can set up SCIM user provisioning.
After you configure the SCIM integration between your IdP and Oracle Cloud Infrastructure, users that belong to groups mapped to Oracle Cloud Infrastructure groups are automatically provisioned in Oracle Cloud Infrastructure. Provisioned users are assigned a unique **OCID** , and can have API keys and other service-specific credentials. 
The following functionality is supported for provisioned, federated users: 
  * Provisioned users are assigned a unique **OCID**
  * Provisioned users can have API keys, auth tokens, and other service-specific credentials
  * You can list the users in the Console
  * Provisioned users can access the **User Settings** page to see and manage these credentials for themselves
  * When you add or remove users to Oracle Cloud Infrastructure-mapped groups in your IdP, the updates are automatically synched with Oracle Cloud Infrastructure


## Understanding User Types 🔗 
The SCIM configuration introduces the concept of the _provisioned_ or _synchronized_ user. The following descriptions provide details to help you understand the user types you'll be managing.
  * Federated users
A federated user is created and managed in an identity provider. Federated users can sign in to the Console using a password managed in their identity provider. Federated users are granted access to Oracle Cloud Infrastructure based on their membership in groups that are mapped to Oracle Cloud Infrastructure groups.
  * Provisioned (or Synchronized) users 
A synchronized user is systematically provisioned by the identity provider in Oracle Cloud Infrastructure. Synchronized users can have Oracle Cloud Infrastructure credentials, but not Console passwords. When listing users in the Console, you can identify synchronized users using the **User Type** filter.
  * Local users
A local user is a user created and managed in Oracle Cloud Infrastructure's IAM service. Federated tenancies typically would have few, if any, local users. When listing users in the Console, you can identify local users using the **User Type** filter.


The following graphic summarizes the characteristics of the user types:
![This image summarizes the characteristics of the user types.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/idcs_user_graphic.png)
## Who Should Set Up This Integration? 🔗 
Set up this integration if your IdP is Oracle Identity Cloud Service or Okta and your federated users need to have the specialized credentials required by some services and features. For example, if you need your federated users to access Oracle Cloud Infrastructure through the SDK or CLI, setting up this integration enables these users to get the API keys needed for this access. 
## Prerequisite 🔗 
Perform this synchronization setup after you have successfully set up a federation between your IdP and Oracle Cloud Infrastructure. See [Supported Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/federation.htm#Supporte).
## Enabling User Provisioning 🔗 
### Instructions for Oracle Identity Cloud Service Federations 🔗 
If your identity provider is Oracle Identity Cloud Service, you need to perform a one-time upgrade. 
**Important** If your tenancy was created December 21, 2018 or later, your tenancy is automatically configured to provision your Oracle Identity Cloud Service users in Oracle Cloud Infrastructure. You do not need to perform the steps in this topic. See [Understanding User Types](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingscim.htm#Understa) and [Managing User Capabilities for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm#Managing_User_Capabilities_for_Federated_Users) for information on managing your federated users.
[Upgrading Your Oracle Identity Cloud Service Federation](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingscim.htm)
If your federation with Oracle Identity Cloud service was set up before December 21, 2018, perform this one-time upgrade task.
**To upgrade your Oracle Identity Cloud Service federation:**
  1. Open the **navigation menu** and select **Identity & Security**. Under **Identity** , select **Federation**. 
A list of the identity providers in your tenancy is displayed.
  2. Select your Identity Cloud Service federation to view its details. If your tenancy was auto-federated, it is listed as OracleIdentityCloudService.
  3. Select **Edit Mapping**.
  4. When prompted, provide the client ID and client secret for the Oracle Identity Cloud Service application, and then select **Continue**. 
[Where do I find the client ID and client secret?](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingscim.htm)
The client ID and client secret are stored in Oracle Identity Cloud Service. To get this information:
    1.       1. Sign in to the Oracle Identity Cloud Service console.
      2. In the Identity Cloud Service console, click **Applications**. The list of trusted applications is displayed.
      3. Click COMPUTEBAREMETAL. 
      4. Click **Configuration**.
      5. Expand **General Information**. The client ID is displayed. Click **Show Secret** to display the client secret.
[![Screenshot shows the client secret key in the Oracle Identity Cloud Service console](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_fed_secret.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_fed_secret.png)


Allow several minutes for the changes to take effect.
### Instructions for Okta Federations 🔗 
If you do not have an existing federation with Okta, follow the instructions in the white paper, [Oracle Cloud Infrastructure Okta Configuration for Federation and Provisioning](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/okta-federation-with-oci.pdf). This paper includes instructions for both setting up your federation and provisioning with SCIM.
If you have an existing federation with Okta with group mappings that you want to maintain, you can add SCIM provisioning as follows:
  1. In Okta, delete the existing SAML application you originally set up to federate with Oracle Cloud Infrastructure.
  2. Set up a new SAML application in Okta according to the instructions in the white paper, [Oracle Cloud Infrastructure Okta Configuration for Federation and Provisioning](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/okta-federation-with-oci.pdf), with the following exceptions:
     * Skip the steps to **Add Identity Provider** to Oracle Cloud Infrastructure (you already have this resource in Oracle Cloud Infrastructure).
     * Instead, select **Edit Identity Provider** and upload the new metadata.xml document from the new Okta app you created.
     * Then, in Oracle Cloud Infrastructure, ensure that you **Reset Credentials**. Add the new Client ID and Secret to the API integration settings page in Okta (Step 7 in the white paper).


## What to Expect After the Upgrade 🔗 
When the system has had time to synchronize, you can manage user capabilities for federated users in the Console. Users that belong to a group mapped to a group in Oracle Cloud Infrastructure are listed on the Users page in the Console. Whenever you add new users to mapped groups in Oracle Identity Cloud Service, they will be available in the Console after the system synchronizes.
By default, the following user capabilities are enabled:
  * API keys
  * auth tokens
  * SMTP credentials
  * customer secret keys


Notice that you can't enable a local password. The Oracle Cloud Infrastructure console password is still managed only in your IdP.
For more information about user capabilities, see [Managing User Capabilities for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingusersfederated.htm#Managing_User_Capabilities_for_Federated_Users).
### Resetting Credentials 🔗 
Use the **Reset Credentials** button to reset your SCIM client credentials. You can perform this task periodically as a security measure to rotate your credentials. After you reset these credentials, you'll need to update the SAML app in your identity provider with the new credentials.
**Note:** If your IdP is Oracle Identity Cloud Service, Oracle Cloud Infrastructure automatically resets the credentials with Oracle Identity Cloud Service for you. You don't need to manually reset the configuration.
### Actions You Still Perform in Your Identity Provider 🔗 
After the integration is set up, continue to perform the following actions in your IdP:
  * Create users and assign them to groups. 
  * Delete users.
Users that you delete from your IdP are removed from Oracle Cloud Infrastructure when the next synching cycle completes. 
  * Query for group membership.
  * Manage sign-in passwords for users.


Was this article helpful?
YesNo

