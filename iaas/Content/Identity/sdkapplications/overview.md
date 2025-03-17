Updated 2024-09-26
# Managing Downloaded SDKs and Applications
Download SDKs, the EBS Asserter, the Secure Form Fill Client, the Linux PAM, the Provisioning Bridge Client, App Gateway, RADIUS Proxy, or the Device Fingerprint Utility from the Console in IAM.
## Required Policy or Role 🔗 
To download SDKs and applications, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role or the Security Administrator role
  * Be a member of a group granted `manage` domains


To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
IAM can be used to provide single sign-on for your applications. These applications can be integrated with IAM using one of the following options:
  * **App Catalog:** The App Catalog contains ready-to-use templates to integrate with most of your cloud-based applications.
  * **SAML 2.0:** Use IAM as an identity provider for applications that support the SAML standard.
  * **SDKs:** Use SDKs to develop applications to use the IAM authentication mechanism.
  * **OpenID Connect:** Use IAM as the authentication server for applications that support the OpenID Connect standard.
  * **OAuth 2.0:** Uses IAM as the authorization server for applications that support the OAuth standard.


When none of these methods apply to the applications you need to integrate for authentication, use Secure Form Fill. To help you configure Secure Form Fill for your applications, you use an admin client known as the Secure Form Fill Client.
The following table lists and describes the SDKs and applications that are available in IAM.
Name | Type | Description  
---|---|---  
E-Business Suite Asserter | Application | You might want to integrate your Oracle E-Business Suite (EBS) environment with other cloud services in single-sign-on (SSO) mode using IAM. Using the EBS Asserter, you can integrate Oracle E-Business Suite with IAM for authentication and password management purposes.  
App Gateway | Application | If your web application supports header-based authentication, then use App Gateway to protect access to your application. App Gateway acts as a reserve proxy protecting web applications by restricting unauthorized network access to them. These applications are called Enterprise Applications.  
Secure Form Fill Client | Application | If you can't change the source code of your Web application or the application isn't based on headers, then use Secure Form Fill. The Secure Form Fill Client helps you map the sign-in form for your Web application, so IAM knows how to populate the username and password automatically and submit the user's credentials to the application's identity store.  
Provisioning Bridge | Application | If you want to establish a link between your on-premises apps and IAM, then create a Provisioning Bridge. By doing so, you're synchronizing user and group account data that's created and updated directly on the apps with IAM. Any changes to this data will be transferred into IAM and stored for the corresponding IAM users and groups. For more information about using the Provisioning Bridge, see Synchronize Users from Oracle Internet Directory to IAM.  
Linux Pluggable Authentication Module (PAM) | Application | Use the Linux Pluggable Authentication Module (PAM) to integrate your Linux environment with an identity domain to perform end-user authentication with first and second factor authentication.   
Device Fingerprint Utility | Application | If you have a custom sign-in page for an identity domain and you want to enable device fingerprinting for it, then use Adaptive Security and the Device Fingerprint Utility. If a user uses your sign-in page to access an identity domain from a device that hasn't been previously used to access the service, then device finger printing is triggered.   
Identity cloud SDKs | SDK | Use SDKs to develop your web-based Java, Node.js, Python, and .NET applications.   
SDKs for Android and iOS | SDK | Use SDKs to develop mobile Android or iOS applications.  
Was this article helpful?
YesNo

