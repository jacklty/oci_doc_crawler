Updated 2025-01-14
# Overview of IAM
Oracle Cloud Infrastructure Identity and Access Management (IAM) provides identity and access management features such as authentication, single sign-on (SSO), and identity lifecycle management for Oracle Cloud as well as Oracle and non-Oracle applications, whether SaaS, cloud-hosted, or on-premises. Employees, business partners, and customers can access applications at any time, from anywhere, and on any device in a secure manner.
IAM integrates with existing identity stores, external identity providers, and applications across cloud and on-premises to facilitate easy access for end users. It provides the security platform for Oracle Cloud, which allows users to securely and easily access, develop, and deploy business applications such as Oracle Human Capital Management (HCM) and Oracle Sales Cloud, and platform services such as Oracle Java Cloud Service, Oracle Business Intelligence (BI) Cloud Service, and others.
Administrators and users can use IAM to help them effectively and securely create, manage, and use a cloud-based identity management environment without worrying about setting up any infrastructure or platform details.
**Tip** Watch a [video introduction](https://apexapps.oracle.com/pls/apex/f?p=44785:265:0:::265:P265_CONTENT_ID:31681) to the service.
## Customer Responsibility  🔗 
It is your responsibility to:
  * Understand Oracle Cloud Infrastructure Identity and Access Management (IAM) policies, configurations, and artifacts.
  * Implement your own policies, configurations, and artifacts for all IAM features.
  * Create and administer users, policies, configurations, and artifacts using IAM.
  * Adhere to all the requirements and guidelines for NIST 800-63, including IAL3, AAL3 and FAL3.


For all IAM features, you must use your own configuration values and configure your own artifacts.
## IAM Components 🔗 
IAM uses the components described in this section. To better understand how the components fit together, see [Example Scenario](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm#Example). 

COMPARTMENT
    A collection of related resources. Compartments are a fundamental component of Oracle Cloud Infrastructure for organizing and isolating your cloud resources. You use them to clearly separate resources for the purposes of measuring usage and billing, access (through the use of policies), and isolation (separating the resources for one project or business unit from another). A common approach is to create a compartment for each major part of your organization. For more information, see [Learn Best Practices for Setting Up Your Tenancy](https://docs.oracle.com/iaas/Content/GSG/Concepts/settinguptenancy.htm). 

DYNAMIC GROUPS
    A special type of group that contains resources (such as compute instances) that match rules that you define (thus the membership can change dynamically as matching resources are created or deleted). These instances act as "principal" actors and can make API calls to services according to policies that you write for the dynamic group. 

FEDERATION
    A relationship that an administrator configures between an identity provider and a service provider. When you federate Oracle Cloud Infrastructure with an identity provider, you manage users and groups in the identity provider. You manage authorization in Oracle Cloud Infrastructure's IAM service. 

GROUP
    A collection of users who share a similar set of access privileges. Administrators can grant access policies that authorize a group to consume or manage resources within a tenancy. All users in a group inherit the same set of privileges. 

HOME REGION
    The region where your IAM resources reside. All IAM resources are global and available across all regions, but the master set of definitions reside in a single region, the home region. You must make changes to your IAM resources in your home region. The changes will be automatically propagated to all regions. For more information, see [Managing Regions](https://docs.oracle.com/en-us/iaas/Content/Identity/regions/managingregions.htm#Managing_Regions). 

IDENTITY DOMAIN
    
An identity domain is a container for managing users and roles, federating and provisioning of users, secure application integration through Oracle Single Sign-On (SSO) configuration, and OAuth administration. It represents a user population in Oracle Cloud Infrastructure and its associated configurations and security settings (such as MFA). 

IDENTITY PROVIDER
    A trusted relationship with a federated identity provider. Federated users who attempt to authenticate to the Oracle Cloud Infrastructure console are redirected to the configured identity provider. After successfully authenticating, federated users can manage Oracle Cloud Infrastructure resources in the console just like a native IAM user. 

MFA
    Multifactor authentication (MFA) is a method of authentication that requires the use of more than one factor to verify a user's identity. 

NETWORK SOURCE
    A group of IP addresses that is allowed to access resources in your tenancy. The IP addresses can be public IP addresses or IP addresses from a VCN within your tenancy. After you create the network source, you use policy to restrict access to only requests that originate from the IPs in the network source.  

RESOURCE
    A cloud object that you create and use when interacting with Oracle Cloud Infrastructure services. For example, compute **instances** , block storage **volumes** , virtual cloud networks (**VCNs**), subnets, databases, third-party applications, Software-as-a-Service (SaaS) applications, on-premises software, and retail web applications. 

ROLE
    A set of administrative privileges that can be assigned to a user in an identity domain. 

SECURITY POLICY
    A document that specifies who can access which resources, and how. You can write policies to control access to all of the [services](https://docs.oracle.com/en-us/iaas/Content/services.htm "Oracle Cloud Infrastructure \(OCI\) is a set of complementary cloud services that enable you to build and run a range of applications and services in a highly available hosted environment.") within Oracle Cloud Infrastructure. Access is granted at the group and compartment level, which means you can write a policy that gives a group a specific type of access within a specific compartment, or to the tenancy itself. If you give a group access to the tenancy, the group automatically gets the same type of access to all the compartments inside the tenancy. The word "policy" is used by people in different ways: to mean an individual statement written in the policy language; to mean a collection of statements in a single, named "policy" document (which has an Oracle Cloud ID (OCID) assigned to it); and to mean the overall body of policies your organization uses to control access to resources.      When you apply a policy, there might be a slight delay before the policy is effective. 

SIGN-ON POLICY
    A sign-on policy allows identity domain administrators, security administrators, and application administrators to define criteria that determine whether to allow a user to sign in to an identity domain. 

TAGS
    Tags allow you to organize resources across multiple compartments for reporting purposes or for taking bulk actions. 

TENANCY
    The root compartment that contains _all_ your organization's Oracle Cloud Infrastructure resources. Oracle automatically creates your company's tenancy for you. Directly within the tenancy are your IAM entities (users, groups, compartments, and some policies; you can also put policies into compartments inside the tenancy). You place the other types of cloud resources (for example, instances, virtual networks, block storage volumes, and so on.) inside the compartments that you create.      Tenancy administrators can create users and groups and assign them least-privileged access to resources that are partitioned into compartments. 

USER
    An individual employee or system that needs to manage or use your company's Oracle Cloud Infrastructure resources. Users might need to launch instances, manage remote disks, work with your virtual cloud network, and so on. End users of your application aren't typically IAM users. Users have one or more IAM credentials (see [Working with User Credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/usercred/usercredentials.htm#user_credentials)). 
### Activating and Deactivating Components 🔗 
There are a number of components that have to be activated in order to use them. You can also deactivate them when required.
Find more information about the component you are working with:
  * Adaptive security: [Activate](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/activate-adaptive-security.htm#activate-adaptive-security "Activate adaptive security for an identity domain in IAM to evaluate contextual and threat event analysis, and obtain user risk scores from the configured third-party risk providers.") and [Deactivate](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/deactivate-adaptive-security.htm#deactivate-adaptive-security "Deactivate adaptive security for an identity domain in IAM to stop performing contextual and threat event analysis, and stop obtaining user risk scores from third-party risk providers.")
  * App Gateway: [Activate](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/activate-app-gateways.htm#activate-app-gateways "Activate an app gateway in IAM after registering it and before setting up the app gateway server.") and [Deactivate](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/deactivate-app-gateways.htm#deactivate-app-gateways "Dectivate an app gateway in IAM.").
  * Applications: [Activate](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/activate-applications.htm#activate-applications "Activate an application in an identity domain in IAM to reinstate the access rights to the application for users and groups.") and [Deactivate](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/deactivate-applications.htm#deactivate-applications "Deactivating an application temporarily disables the access rights to applications that users or groups have.")
  * Identity domains: [Deactivate and reactivate](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-deactivate-a-domain.htm#deactivate-domain "You might create an identity domain in IAM that you need only temporarily, for example, for testing purposes. You can deactivate the identity domain when it's not in use and then reactivate it when it's needed. An identity domain must be deactivated before it can be deleted.")
  * Identity providers: [Activating or Deactivating an Identity Provider](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/activate-identity-provider.htm#activate-identity-provider "Activate or deactivate an identity provider \(IdP\) for an identity domain in IAM.")
  * Microsoft AD Bridge: [Activate](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/activate-microsoft-active-directory-ad-bridge.htm#activate-microsoft-active-directory-ad-bridge "Activate a single AD bridge in an IAM identity domain.") and [Deactivate](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/deactivate-microsoft-active-directory-ad-bridge.htm#deactivate-microsoft-active-directory-ad-bridge "Deactivate a single AD bridge in an IAM identity domain.")
  * Risk providers: [Activate](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/activate-risk-provider.htm#activate-risk-provider "Activate a risk provider for an identity domain in IAM to collect user risk scores.") and [Deactivate](https://docs.oracle.com/en-us/iaas/Content/Identity/adaptivesecurity/deactivate-risk-provider.htm#deactivate-risk-provider "Deactivate a risk provider for an identity domain in IAM to stop collecting user risk scores.")
  * Self-registration profiles: [Activate](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/deactivating-self-registration-profiles.htm#activating-self-registration-profiles "Deactivate a self-registration profile in IAM when you no longer need it.")
  * Sign-on policies: [Activate](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/activate-sign-policies.htm#activate-sign-policies "After you create a sign-on policy, you must activate the policy to begin enforcing it in the identity domain in IAM. You must activate a sign-on policy after you create it.") and [Deactivate](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/deactivate-sign-policies.htm#deactivate-sign-policies "Deactivate a sign-on policy.")
  * Terms of use: [Activate](https://docs.oracle.com/en-us/iaas/Content/Identity/termsofuse/activate-terms-use.htm#activate-terms-use "Activate a terms of use document for an identity domain in IAM.") and [Deactivate](https://docs.oracle.com/en-us/iaas/Content/Identity/termsofuse/deactivate-terms-use.htm#deactivate-terms-use "Deactivate a terms of use document for an identity domain in IAM.")
  * Users: [Deactivate and reactivate](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#activate-and-deactivate "There are a number of components that have to be activated in order to use them. You can also deactivate them when required.")


## The Administrators Group, Policy, and Administrator Roles 🔗 
When your company signs up for an Oracle account and identity domain, Oracle sets up a _default administrator_ for the account. This person will be the first IAM user for your company and will be responsible for initially setting up additional administrators. Your tenancy comes with a group called _Administrators_ , and the default administrator automatically belongs in this group. You can't delete this group, and there must always be at least one user in it.
Your tenancy also automatically has a policy that gives the Administrators group access to all of the Oracle Cloud Infrastructure API operations and all of the cloud resources in your tenancy. You can neither change nor delete this policy. Any other users you put into the Administrators group will have full access to all of the services. This means they can create and manage IAM resources such as groups, policies, and compartments. And they can create and manage cloud resources such as virtual cloud networks (VCNs), instances, block storage volumes, and any other new types of Oracle Cloud Infrastructure resources that become available in the future.
Aside from the default administrator and default policy, you can assign user accounts to predefined administrator roles in order to delegate administrative responsibilities. Administrator roles exist within identity domains. You can assign any user account in an identity domain to one or more administrator roles in that identity domain. While policies give access to compartments and the resources in those compartments, if you use administrator roles, you can grant access to resources without learning policy language or writing and maintaining policies.
**Note** Granting users or groups the identity domain administrator role for domains other than the default domain grants them full administrator permissions to only that domain (not to the tenancy). At least one administrator for the identity domain must be granted the identity domain administrator role directly. This is in addition to any identity domain administrator roles granted by group membership. For more information, see [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed.").
IAM evaluates policies and administrator roles together when determining whether a user has access to resources and what that user can do with those resources. If the tenancy already relies on policies, you can continue using them. You can even write policies to grant access to specific identity domains. However, Oracle recommends that you start using administrator roles to grant users access to resources in identity domains moving forward.
## Ways to Access Oracle Cloud Infrastructure 🔗 
You can access Oracle Cloud Infrastructure using the Console (a browser-based interface) or the [REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm). Instructions for the Console are included in topics throughout this guide. For a list of available SDKs, see [Software Development Kits and Command Line Interface](https://docs.oracle.com/iaas/Content/API/Concepts/sdks.htm).
To access the Console, you must use a [supported browser](https://docs.oracle.com/iaas/Content/GSG/Tasks/signinginIdentityDomain.htm#supported-browsers). To go to the **Console** sign-in page, open the navigation menu at the top of this page and select **Infrastructure Console**. You prompted to enter your cloud tenant, your user name, and your password. 
For the REST API Reference for the IAM API, see [Identity and Access Management Service API](https://docs.oracle.com/iaas/api/#/en/identity/). For the REST API Reference for the IAM Identity Domains API, see [IAM Identity Domains API](https://docs.oracle.com/en/cloud/paas/iam-domains-rest-api/index.html). For general information about using the API, see [REST API](https://docs.oracle.com/iaas/Content/API/Concepts/usingapi.htm).
## Documentation to Use for Cloud Identity 🔗 
To help you administer identity in Oracle Cloud Infrastructure (OCI), you need the correct documentation.
The documentation that you choose depends on the following factors:
  * Whether your OCI tenancy has been updated to use Oracle Cloud Infrastructure Identity and Access Management (IAM) identity domains
  * Whether your Oracle Identity Cloud Service (IDCS) stripes have been migrated to IAM identity domains 


Read the following sections to find the correct documentation for you.
### Do You Have Access to Identity Domains? 🔗 
  1. Sign in to the Oracle Cloud Console. Need help signing in? See [Sign In to the Console](https://docs.oracle.com/iaas/Content/GSG/Tasks/signingin.htm). 
  2. In the navigation menu, select **Identity & Security**. Under **Identity** , check for **Domains**. If you see **Domains** , your cloud account has been updated.


[Tenancy with identity domains](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm)
![Screenshot of OCI IAM with identity domains](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/ociiam-domains.jpg)
[Tenancy without identity domains](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm)
![Screenshot of OCI IAM without identity domains](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/ociiam-no-domains.jpg)
If you sign in and see the IDCS Admin Console instead of the Oracle Cloud Console, as shown in the following image, your stripes haven't been migrated into IAM. You don't have access to identity domains.
[Identity Cloud Service](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm)
![Screenshot of IDCS Admin Console](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/identity-cloud-service.jpg)
### Which Documentation Do You Need? 🔗 
After determining whether your tenancy was updated or whether your IDCS stripes migrated, choose the correct documentation for you. 
Has your tenancy been updated? | Use this documentation.  
---|---  
I see **Domains** in the Console. My tenancy was updated.  |  When using the Console: 
  * To administer IAM in tenancies with identity domains, see [Oracle Cloud Infrastructure Identity and Access Management](https://docs.oracle.com/en-us/iaas/Content/Identity/home.htm "Identity and Access Management \(IAM\) uses identity domains to provide identity and access management features such as authentication, single sign-on \(SSO\), and identity lifecycle management for Oracle Cloud as well as for Oracle and non-Oracle applications, whether SaaS, cloud hosted, or on premises.").
  * For user self-service instructions, such as setting up MFA, see the [IAM User Guide](https://docs.oracle.com/en-us/iaas/Content/Identity/using/aboutidentitydomains.htm "Your administrator gives you access to an identity domain. You use an identity domain to configure profile and security settings, manage 2-step verification for your account, generate bypass codes and to use the Oracle Mobile Authenticator \(OMA\) app.").

When using the API:
  * To manage identity domains (for example, creating or deleting a domain), see [IAM API](https://docs.oracle.com/iaas/api/#/en/identity/).
  * To manage resources (for example, users and groups) within identity domains, see [IAM Identity Domains API](https://docs.oracle.com/en/cloud/paas/iam-domains-rest-api/index.html).

If your tenancy has been updated recently, for information about what to expect post update, see:
  * [OCI IAM Identity Domains: What OCI IAM customers need to know](https://www.oracle.com/a/ocom/docs/security/what-oci-iam-customers-should-expect-post-migration.pdf)
  * [OCI IAM Identity Domains: What Oracle IDCS customers need to know](https://www.oracle.com/a/ocom/docs/security/what-idcs-customers-should-expect-post-migration.pdf)

  
I don't see **Domains** in the Console. My tenancy wasn't updated. |  To use the Console to administer IAM in tenancies without identity domains, see [Overview of Identity and Access Management](https://docs.oracle.com/iaas/Content/Identity/Concepts/overview.htm).  To use the API to administer IAM in tenancies without identity domains, see [IAM API](https://docs.oracle.com/iaas/api/#/en/identity/). For information about what to expect when the update happens, see [OCI IAM Identity Domains: What OCI IAM customers need to know](https://www.oracle.com/a/ocom/docs/security/what-oci-iam-customers-should-expect.pdf).   
I see the IDCS Admin Console. My stripes weren't migrated to identity domains. |  When using the Console:
  * To administer stripes in IDCS, see [Administering Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/uaids/index.html).
  * For user self-service instructions, such as setting up MFA, see the [Using Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/usids/index.html).

To use the API to administer stripes in IDCS, see [REST API for Oracle Identity Cloud Service](https://docs.oracle.com/en/cloud/paas/identity-cloud/rest-api/index.html). For information about what to expect when the migration happens, see [OCI IAM Identity Domains: What Oracle IDCS customers need to know](https://www.oracle.com/a/ocom/docs/security/what-idcs-customers-should-expect.pdf).  
Was this article helpful?
YesNo

