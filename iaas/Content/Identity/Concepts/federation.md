Updated 2023-01-04
# Federating with Identity Providers
This topic describes identity federation concepts. Oracle Cloud Infrastructure supports federation with [Oracle Identity Cloud Service](https://www.oracle.com/cloud/paas/identity-cloud-service.html),and Microsoft Active Directory (via Active Directory Federation Services (AD FS)), Microsoft Azure Active Directory, Okta, and other identity providers that supports the Security Assertion Markup Language (SAML) 2.0 protocol.
## Overview 🔗 
Enterprise companies commonly use an _identity provider (IdP)_ to manage user login/passwords and to authenticate users for access to secure websites, services, and resources. 
When someone in your company wants to use Oracle Cloud Infrastructure resources in the Console, they must sign in with a user login and password. Your administrators can federate with a supported IdP so that each employee can use an existing login and password and not have to create a new set to use Oracle Cloud Infrastructure resources. 
To federate, an administrator goes through a short process to set up a relationship between the IdP and Oracle Cloud Infrastructure (commonly referred to as a _federation trust_). After an administrator sets up that relationship, any person in your company who goes to the Oracle Cloud Infrastructure Console is prompted with a "single sign-on" experience provided by the IdP. The user signs in with the login/password that they've already set up with the IdP. The IdP authenticates the user, and then that user can access Oracle Cloud Infrastructure. 
When working with your IdP, your administrator defines groups and assigns each user to one or more groups according to the type of access the user needs. Oracle Cloud Infrastructure also uses the concept of groups (in conjunction with IAM policies) to define the type of access a user has. As part of setting up the relationship with the IdP, your administrator can map each IdP group to a similarly defined IAM group, so that your company can re-use the IdP group definitions when authorizing user access to Oracle Cloud Infrastructure resources. Here's a screenshot from the mapping process:
[![This screenshot shows the group mapping dialog](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federation_group_mappings.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federation_group_mappings.png)
For information about the number of federations and group mappings you can have, see [Service Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#top "This topic describes the service limits for Oracle Cloud Infrastructure and the process for requesting a service limit increase."). There's no limit on the number of federated users.
**Note**
Any users who are in more than 50 IdP groups cannot be authenticated to use the Oracle Cloud Infrastructure Console.
### Automated User Provisioning and Synchronization with SCIM 🔗 
Tenancies federated with Oracle Identity Cloud Service or the [third-party provider Okta](https://www.okta.com/), can also leverage [SCIM (System for Cross-domain Identity Management)](http://www.simplecloud.info/) to enable provisioning of federated users in Oracle Cloud Infrastructure. Federated users that have been provisioned in Oracle Cloud Infrastructure through this process can have the additional user credentials such as API keys and auth tokens that are managed in the **User Settings** page. This enables federated users to use the SDK and CLI, and other features that require the additional user credentials. For more information, see [User Provisioning for Federated Users](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/usingscim.htm#User_Provisioning_for_Federated_Users).
## General Concepts 🔗 
Here's a list of the basic concepts you need to be familiar with. 

IDP
    IdP is short for _identity provider_ , which is a service that provides identifying credentials and authentication for users.      Tenancies created after December 18, 2017 are automatically federated with [Oracle Identity Cloud Service](https://www.oracle.com/cloud/paas/identity-cloud-service.html) as the IdP. Oracle Cloud Infrastructure can be federated with any IdP that supports the Security Assertion Markup Language (SAML) 2.0 protocol.  

SERVICE PROVIDER (SP)
    A service (such as an application, website, and so on) that calls upon an IdP to authenticate users. In this case, Oracle Cloud Infrastructure is the SP.  

FEDERATION TRUST
    A relationship that an administrator configures between an IdP and SP. You can use the Oracle Cloud Infrastructure Console or API to set up that relationship. Then, the specific IdP is "federated" to that SP. In the Console and API, the process of federating is thought of as _adding an identity provider to the tenancy._ 

SAML METADATA DOCUMENT
    An IdP-provided XML-based document that provides the required information to an SP to federate with that IdP. Oracle Cloud Infrastructure supports the SAML 2.0 protocol, which is an XML-based standard for sharing required information between the IdP and SP. Depending on which idP you are federating with, you must either provide the metadata URL (see below) to this document or upload the document to Oracle Cloud Infrastructure. 

METADATA URL
    An IdP-provided URL that enables an SP to get required information to federate with that IdP. Oracle Cloud Infrastructure supports the SAML 2.0 protocol, which is an XML-based standard for sharing required information between the IdP and SP. The metadata URL points to the SAML metadata document the SP needs. 

FEDERATED USER
    Someone who signs in to use the Oracle Cloud Infrastructure Console by way of a federated IdP.  

LOCAL USER 
    A non-federated user. In other words, someone who signs in to use the Oracle Cloud Infrastructure Console with a login and password created in Oracle Cloud Infrastructure.  

GROUP MAPPING
    A mapping between an IdP group and an Oracle Cloud Infrastructure group, used for the purposes of user authorization.  

SCIM
    [SCIM (System for Cross-domain Identity Management)](http://www.simplecloud.info/) is an IETF standard protocol that enables user provisioning across identity systems. Oracle Cloud Infrastructure hosts a SCIM endpoint for provisioning federated users into Oracle Cloud Infrastructure. Using a SCIM client to provision users in Oracle Cloud Infrastructure enables you to assign credentials to the users in Oracle Cloud Infrastructure.  

PROVISIONED (OR SYNCHRONIZED) USER
    A user provisioned by the identity provider's SCIM client in Oracle Cloud Infrastructure. These users can be listed in the Oracle Cloud Infrastructure Console and can have all the Oracle Cloud Infrastructure user credentials except for a Console password. 

Encrypt Assertion
    Some IdPs support the encryption of the SAML assertion. When enabled, the service provider expects the SAML assertion to be encrypted by the identity provider, using the service provider's encryption key. In this case, the service provider is Oracle Cloud Infrastructure authentication service. If you choose to enable this feature of your IdP, you must also enable the feature when you set up your Federation provider in the IAM service. Note that Microsoft AD FS enables the encryption of the SAML assertion by default. If your IdP is Microsoft AD FS, you must either enable this feature in IAM or disable it for Microsoft AD FS.
## Experience for Federated Users 🔗 
Federated users can use the Console to access Oracle Cloud Infrastructure (according to IAM policies for the groups the users are in). 
They'll be prompted to enter their Oracle Cloud Infrastructure tenant (for example, ABCCorp). 
They then see a page with two sets of sign-in instructions: one for federated users and one for non-federated (Oracle Cloud Infrastructure) users. See the following screenshot.
[![This screenshot shows the sign-in page for federated users](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federation_signin.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/federation_signin.png)
The tenant name is shown on the left. Directly below is the sign-in area for federated users. On the right is the sign-in area for non-federated users. 
Federated users choose which identity provider to use for sign-in, and then they're redirected to that identity provider's sign-in experience for authentication. After entering their login and password, they are authenticated by the IdP and redirected back to the Oracle Cloud Infrastructure Console. 
The federated users (without SCIM configuration) cannot access the "User Settings" page in the Console. This page is where a user can change or reset their Console password and manage other Oracle Cloud Infrastructure credentials such as [API signing keys](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/credentials.htm#API) and [auth tokens](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/credentials.htm#Swift).
### Experience for Federated Users with SCIM Configuration 🔗 
If your IdP has also been configured with a SCIM client, a user signed in through their identity provider can access the User Settings page and have user capabilities such as API keys, auth tokens, and other user credentials. (**Note:** This is currently available for Oracle Identity Cloud Service and Okta federations only.)
## Required IAM Policy 🔗 
To add and manage identity providers in your tenancy, you must be authorized by an IAM policy. If you're in the [Administrators group](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/overview.htm#The), then you have the required access.
Here's a more limited policy that restricts access to only the resources related to identity providers and group mappings:
Copy
```
Allow group IdPAdmins to manage identity-providers in tenancy
Allow group IdPAdmins to manage groups in tenancy
```

If you're new to policies, see [Getting Started with Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/policygetstarted.htm#Getting_Started_with_Policies) and [Common Policies](https://docs.oracle.com/en-us/iaas/Content/Identity/Concepts/commonpolicies.htm#top). If you want to dig deeper into writing policies for groups or other IAM components, see [Details for IAM without Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/Reference/iampolicyreference.htm#top).
## Supported Identity Providers 🔗 
**Important**
Oracle Cloud Infrastructure tenancies created December 18, 2017 or later are automatically federated with Oracle Identity Cloud Service. 
If your tenancy was created before December 18, 2017, and you want to set up a federation with Oracle Identity Cloud Service, see [Federating with Oracle Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingIDCS.htm#top).
For instructions for federating with other identity providers, see the following:
[Federating with Microsoft Active Directory](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFS.htm#top)
[Federating with Microsoft Azure Active Directory](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingADFSazure.htm#top)
[Oracle Cloud Infrastructure Okta Configuration for Federation and Provisioning](https://docs.oracle.com/iaas/Content/Resources/Assets/whitepapers/okta-federation-with-oci.pdf) (white paper)
[Federating with SAML 2.0 Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/federatingSAML.htm#top)
Was this article helpful?
YesNo

