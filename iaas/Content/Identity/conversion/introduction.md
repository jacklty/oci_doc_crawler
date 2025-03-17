Updated 2025-02-03
# Introduction
Some features, such as the sign-in experience and the OCI Console look different when your Identity Cloud Service is migrated.
If you're an OCI customer, you might have been using Oracle Identity Cloud Service without realizing it, although federation with Identity Cloud Service has been how you sign in.
If you're an Identity Cloud Service user, you're probably aware that Identity Cloud Service has been providing identity services.
In both cases, after identity domains are introduced into the OCI tenancy, Identity Cloud Service instances become identity domains. Identity domains are IAM resources that reside in a compartment and are treated like other IAM resources. All Identity Cloud Service instances become identity domains. A Default identity domain is created and is automatically subscribed to the regions that the tenancy is subscribed to. Other converted identity domains with Identity Cloud Service domain types can't be replicated.
All users, groups, security settings, and other configurations are maintained as Identity Cloud Service instances become identity domains. User resource attributes in the newly created identity domain include all previous Identity Cloud Service attributes, as well as tags and credentials for OCI. User resources keep the same Oracle Cloud ID (OCID).
For more information, see
  * [Introducing OCI IAM Identity Domains: What customers need to know](https://www.oracle.com/a/ocom/docs/security/what-oci-iam-customers-should-expect.pdf) (PDF)
  * [Identity and Access Management FAQ](https://www.oracle.com/security/cloud-security/identity-access-cloud/faq/)


## Administrator Sign-In Experience 🔗 
Your sign-in experience is going to change. When you sign in, after the change has happened, upon entering the tenancy name you choose the identity domain you want to sign in to and then enter your credentials. The tenancy and the identity domain can be found in the welcome email. Converted Identity Cloud Service instances appear as identity domains that users can now choose from. Also, identity providers (IdPs) continue to be shown in the sign-in menu.
Before identity domains, you would go to `cloud.oracle.com` and enter the tenancy name, select Next, and on the next page enter your credentials.
After identity domains, upon entering the tenancy name you choose the identity domain you want to sign in to and then enter your credentials.
Choose the identity domain you want to work in.
[![Shows where you select the identity domain.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_conversion_domain.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_conversion_domain.png)
Enter your credentials.
[![Shows where you enter your credentials.](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_conversion_new.png)](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/iam_conversion_new.png)
Converted Identity Cloud Service instances appear as identity domains that users can now choose from. Also, identity providers (IdPs) continue to be shown in the sign-in menu.
## User Sign-In Experience 🔗 
Users must follow these steps to access the identity domain converted from their old Identity Cloud Service instance with the same permissions they had before migration:
  1. A user must sign in to the Console as usual, and select the **Profile** menu on the upper-right side of the navigation bar at the top of the page.
  2. Choose **Identity Domain: Default** , which takes them to the Default identity domain details page.
  3. From the breadcrumbs, choose Domains, then choose the identity domain with the same name as their Identity Cloud Service instance had.


## The OCI Console 🔗 
All customers, including customers of MyServices, now use the OCI Console. Customers who created OCI tenancies before the conversion to using identity domains now manage tenancy users and groups through a Default identity domain. See [Get to Know the Console](https://docs.oracle.com/iaas/Content/GSG/Concepts/console.htm).
## APIs 🔗 
### Identity and Access Management Service API
If you previously used the Identity and Access Management Service API version 20160918, you can continue using it, but operations submitted to those endpoints only work for resources in the Default identity domain, and also CRUD for identity domains. The API version is shown on every page of the IAM service API. See [IAM API](https://docs.oracle.com/iaas/api/#/en/identity/).
### IAM Identity Domains API
Use the new IAM Identity Domains API when you want to perform operations on any resources in an identity domain other than the default domain. For information about using domains other than the default domain, see [Using Multiple Identity Domains](https://docs.oracle.com/en-us/iaas/Content/Identity/domains/multiple-domains.htm#multiple-instances "Create and manage multiple identity domains \(for example, one domain for development and one for production\) each with different identity and security requirements to protect your applications and Oracle Cloud services."). See [IAM Identity Domains API](https://docs.oracle.com/en/cloud/paas/iam-domains-rest-api/index.html).
## Identity Providers 🔗 
For tenancies that configured identity providers (IdPs), we recommend that you eventually manually re-create the IdP relationship within an identity domain. See [Managing Identity Providers](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/manage-identity-providers.htm#manage-identity-providers "You can set up federated login between an identity domain and external identity provider. This allows users to sign in and access Oracle Cloud Infrastructure resources by using existing logins and passwords managed by the identity provider.").
## SKU Tiers 🔗 
Converted Identity Cloud Service instances maintain their existing license, features, limits, and so on.
## Domain Regions 🔗 
In the identity domains model, converted domains with Identity Cloud Service domain types can't be replicated.
The default domain and auto federated instance domain are in the tenancy home region. All other Identity Cloud Service instances are converted to identity domains which maintain their home region.
## Resource Tags 🔗 
Identity domains supports UTF-8 for both group names and in policies.
Was this article helpful?
YesNo

