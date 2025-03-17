Updated 2024-09-26
# Managing Identity Providers
You can set up federated login between an identity domain and external identity provider. This allows users to sign in and access Oracle Cloud Infrastructure resources by using existing logins and passwords managed by the identity provider.
## Required Policy or Role
To manage identity domain security settings and identity providers, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role or the Security Administrator role
  * Be a member of a group granted `manage identity-domains` permissions


To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
## About Identity Providers and Service Providers 🔗 
About identity providers and service providers.
An identity provider, also known as an authentication authority, provides external authentication for users who want to sign in to an identity domain using their external provider's credentials. While an identity domain can serve as an identity provider to a third-party service provider, in this context where it relies on an identity provider to authenticate users that access the identity domain, the identity domain is the service provider. More generally, you can also think of Oracle Cloud Infrastructure as the service provider because it provides the services and resources that users want access to.
For example, your organization may want users to sign in and gain access to Oracle Cloud Services by using their Microsoft Active Directory Federation Services (AD FS) credentials. In this case, Microsoft AD FS acts as the identity provider (IdP) and the identity domain functions as the service provider (SP). MS AD FS authenticates the user and returns a token containing identity and authentication information to the identity domain (for example, the user name and the email address of the user). This security token is digitally signed by the IdP. The SP verifies the signature on the token and then uses the identity information to establish an authenticated session for the user. This is known as federated single sign-on where a user is challenged for credentials in one domain and is granted access to another domain.
To federate a Microsoft Active Directory Bridge, see [Setting Up a Microsoft Active Directory (AD) Bridge](https://docs.oracle.com/iaas/Content/Identity/msadbridge/microsoft-active-directory-ad-bridge1.htm).
## About Digital Certificates 🔗 
A digital certificate is like an electronic passport that helps a person, computer, or organization to exchange information securely over the internet using public key cryptography. A digital certificate may be referred to as a public key certificate.
Just like a passport, a digital certificate provides identifying information, is forgery resistant, and can be verified because it is issued by an official, trusted agency. The certificate can contain the name of the certificate holder, a serial number, expiration dates, a copy of the certificate holder's public key (used for encrypting messages and verifying digital signatures) and the digital signature of the certificate-issuing authority (CA) so that a recipient can verify that the certificate is real.
In order to verify external identity providers' signatures, the service provider stores copies of their signing certificates. When the service provider receives a signed message from an identity provider, before the stored certificate is used to verify the signature, the certificate must be verified as valid. Certificate validation includes verifying that the certificate has not expired. After the certificate has been validated, the certificate is used to verify the signature on the message.
In order for this operation to succeed, the public key embedded in the certificate must match the private key that the identity provider used to sign the message.
### What Happens When an Identity Provider's Certificate Expires? 🔗 
If an identity provider's signing certificate expires and they change their signing key pair when they renew the certificate, then signature validation fails, and the identity domain is unable to complete single sign-on (SSO) operations for that identity provider's users. Therefore, when an identity provider's certificate nears its expiration date, you should make plans to replace it. The typical process is as follows:
  1. Obtain the new signing certificate from the identity provider. This may be published by the identity provider for self-service download, or you may need to contact the identity provider administrator.
  2. Load the new signing certificate into the identity domain configuration for the identity provider.
  3. If the identity provider has also rolled over its signing private/public key pair (rather than only reissuing a new certificate for the existing key pair), then you must update the identity provider configuration to begin using the new keys to sign messages. Again, this may be self-service or require coordination with the identity provider administrator.


**Note** If the identity provider rolls over its signing key pair, then SSO will fail during the period of time between Step 2 and Step 3 above. For this reason, the certificate update is typically coordinated between the identity provider and identity domain administrators.
## About SAML Just-In-Time Provisioning 🔗 
SAML Just-In-Time (JIT) Provisioning automates user account creation when the user first tries to perform SSO and the user doesn't yet exist in the identity domain. In addition to automatic user creation, JIT allows granting and revoking group memberships as part of provisioning. JIT can be configured to update provisioned users so the users' attributes in the service provider (SP) store can be kept in sync with the identity provider (IdP) user store attributes.
### Benefits 🔗 
The advantages of JIT are:
  * The footprint of user accounts in the identity domain is limited to those users who actually sign in through federated SSO, rather than all users in the IdP's user directory.
  * Reduced administrative costs as accounts are created on demand as part of the SSO process and the identity provider and service provider user stores don't have to be synchronized manually.
  * Any new users added later to the identity provider user store won't require administrators to create corresponding service provider accounts manually (users will always be in sync).


### How It Works 🔗 
There are four runtime flows for JIT Provisioning:
When Signing In, The User:  | Flow  
---|---  
Exists in the SP and JIT provisioning is enabled. | Normal SSO flow.  
Doesn't exist in the SP and JIT provisioning is not enabled. | Normal SSO failure flow.  
Doesn't exist in the SP and JIT create user is enabled. | User is created, and populated with the SAML assertion attributes, as mapped in the JIT configuration.  
Exists in the SP and JIT update is enabled. | User attribute values are updated with the SAML assertion attributes, as mapped in the JIT configuration.  
Was this article helpful?
YesNo

