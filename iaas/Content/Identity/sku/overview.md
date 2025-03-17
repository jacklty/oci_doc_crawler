Updated 2024-10-03
# IAM Identity Domain Types
Learn about identity domain types and the features and limits associated with each.
An IAM **identity domain** is deployed with one of five identity domain types. Each **identity domain type** is associated with a different set of features and object limits. Use this information to decide which domain type is appropriate for what you want to do.
This section summarizes:
  * The different identity domain types, see [Understand Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#understand).
  * The features associated with each type, see [Feature Availability for Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#features).
  * The number of different types of object for each identity domain type, see [IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits).
  * Supported data types for custom attributes and their limits, see [Data Types for Custom Attributes](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#data-types-custom-attr).
  * Rate limiting for APIs for different identity domain types, see [API Rate Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/api-rate-limiting.htm "Understand the rate limiting for APIs for different identity domain types.").
  * Meters used for different identity domain types, see [Meters for Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#meters).
  * How to change to a different identity domain type, see [Changing your Identity Domain Type](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#changing-domain-type).


This section has information about identity domains and the various features and limits associated with each identity domain type. For information about IAM tenancy level limits, see [IAM With Identity Domains Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#iam-service-limits).
## Understand Identity Domain Types 🔗 
IAM has five different identity domain types to address different organizational needs. Start here to understand which suits your requirements best, and which type to choose when you create an identity domain.
Here's a summary of the identity domain types. Decide which provides the best fit for your requirements and check the features and limits below to that you get with that identity domain type to select the identity domain type that's right for you.
### Free
When you create an OCI tenancy, you are automatically provisioned with a **Free** identity domain. This domain type allows you to use the IAM service to manage access to OCI Infrastructure and Platform resources. Use this domain type to learn about the IAM service, and to manage access to OCI IaaS and PaaS resources. This domain type should include everything you need to manage OCI. But if you require higher limits or additional features, you can change to a different identity domain type.
**Example Use case:** Your organization uses Oracle Cloud and your cloud administrators need secure access to manage subscribed OCI services.
### Oracle Apps
Some Oracle PaaS services and SaaS applications offer their customers an **Oracle Apps** identity domain which allows you to use the IAM service to manage access to the subscribed service. In most cases, the identity domain is either provided by the service at provisioning time or a pre existing domain will automatically become an Oracle Apps domain when a registered service is attached to it. This domain type should include everything you need to manage access to your subscribed Oracle service. But if you require higher limits or additional features, you can change to a different identity domain type.
**Example Use Case:** Your organization subscribes to an Oracle PaaS or SaaS service that provides an Oracle Apps identity domain with their service. You can use this domain type to manage access to Oracle PaaS and SaaS services. You might also have one or two third-party applications for which you'd like users to seamlessly sign-in without having to reauthenticate.
### Oracle Apps Premium
**Oracle Apps Premium** identity domains add support for hybrid IAM scenarios which extend the IAM service to manage access for on-premises or OCI hosted Oracle applications such as Oracle E-Business Suite, PeopleSoft, and Oracle Database. While this identity domain type is intended primarily for use with Oracle applications, it also allows you to manage access for a limited number of third-party or custom applications.
**Example Use Case:** Your organization would like to enable authentication and single sign-on for your workforce users to access Oracle SaaS applications as well as on-premises or cloud-hosted Oracle applications such as E-Business Suite, JD Edwards, PeopleSoft, Siebel, and/or Oracle Database. You might also want bidirectional synchronization with Microsoft Active Directory or other on-premises systems and you might have a few third-party or custom applications for which you'd like users to seamlessly sign-in without having to reauthenticate.
### Premium
**Premium** identity domains provide the full IAM feature set and highest limits for employee and workforce use cases giving you enterprise-ready access management across hybrid IT environments. It includes all supported integration types and unlimited third-party applications. This is the ideal domain type if you are standardizing on OCI IAM as your enterprise identity and access management provider.
**Example Use Case:** You want an Identity-as-a-Service (IDaaS) solution to manage workforce authentication and access to all of your Oracle and third-party applications whether they're SaaS apps, on-premises enterprise apps, or apps that are hosted in the cloud. You want to use modern authentication and authorization features such as passwordless authentication, FIDO2 hardware tokens, and adaptive security. You might also want automated provisioning and deprovisioning of accounts across these systems.
### External User
**External** identity domains provide a robust IAM feature set for non employee use cases, consumer-facing apps, and custom app development. This domain type provides relevant features for these scenarios such as user self-service, social sign in, and consent management.
**Note** External identity domains are only licensed for non employee user accounts. If your business needs require that you have employee user accounts stored within an External identity domain (for example, if an app only supports one identity provider), that is allowed only if those user accounts also exist in another identity domain of type Free, Oracle Apps, Oracle Apps Premium, or Premium.
**Example Use Case:** You want a full-featured Identity-as-a-Service (IDaaS) solution that helps you manage authentication and access to custom or consumer-facing applications. The solution should support social sign in, user self-service password and profile management, and terms of use consent. And you might need the solution to scale to support millions of users.
## Feature Availability for Identity Domain Types 🔗 
Understand the features available for the different identity domain types.
This table shows the features available to each domain type.
Feature | Free | Oracle Apps | Oracle Apps Premium | Premium | External User  
---|---|---|---|---|---  
**Core IAM features**  
User and group management | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
End-user self-registration | - | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Self-service profile management | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Account recovery (self-service password reset by way of email, SMS, security questions) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)SMS is not part of the Free domain type | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Default password policy | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Group-based password policy | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
**Support for External Apps**[ 1](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#features__footnote1)  
Outbound SSO to third-party apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 2 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 2 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 10 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Unlimited | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Unlimited  
Provisioning to third-party apps using App Catalog | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 2 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 2 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 10 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Unlimited | -  
OAuth/token mgmt for third-party apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 2 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 2 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 10 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Unlimited | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Unlimited  
Generic SCIM app template | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 2 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 2 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Limit of 10 external apps | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Unlimited | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Unlimited  
**Manage Access to Oracle Cloud Infrastructure**  
All current Infrastructure as a Service IAM features  | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
Manage access to OCI resources | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
Dynamic groups (for OCI) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
Credential types specific to OCI | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
**Security Options**  
External IdPs and social login _(Federation / Inbound SSO)_ | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)5 external IdPs | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)5 external IdPs | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)30 external IdPs | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)30 external IdPs | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)30 external IdPs  
Flexible IdP routing policies | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Terms of use | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Just in time provisioning | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
PIV / CAC card support | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Schema extension | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Delegated administration | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Uni-directional Active Directory sync which supports inbound sync from AD to the IAM identity domain | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
Authentication Options: Oracle Mobile Authenticator (MFA) and adaptive security (MFA - TOTP and push, phone call, security questions, FIDO2, DUO, email). | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)SMS is not part of the Free domain type | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Passwordless authentication | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Sign in policies (conditions - authenticated by, groups, administrators, exclusions, network perimeter, built-in risk engine) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Application SDKs | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
**Oracle SaaS Integration**  
SSO for Oracle Cloud services | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
User provisioning for Oracle Cloud services (with account form, custom attributes, filters, and so on) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
OAuth/Token management for Oracle App and SaaS extensions[2](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#features__footnote2) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
**Reports**  
Auditing and reporting | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
**Branding**  
Customized look and feel | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
Hosted sign-in | - | - | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
**Advanced and hybrid identity and access management features**  
**Advanced IAM**  
Bi-directional sync with LDAP by way of provisioning bridge | - | - | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
Bi-directional sync with AD bridge | - | - | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
Delegated authentication by way of AD bridge | - | - | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
SSO for any application | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
**Hybrid IAM**  
Application Gateway (for any enterprise app) | - | - | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Oracle enterprise apps only | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Any enterprise app | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Any enterprise app  
EBS Asserter[3](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#features__footnote3) | - | - | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)  
RADIUS proxy (all - Oracle DB, VPNs, network devices, and so forth) | - | - | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)Oracle DB only | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png)All - Oracle DB, VPNs, Network Devices, and so on | -  
Linux PAM | - | - | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | ![Checkmark](https://docs.oracle.com/en-us/iaas/Content/Resources/Images/checkmark.png) | -  
1 External or third-party apps are defined as either commercial applications offered by a provider other than Oracle or as custom-developed applications (including, for example, applications built on OCI using APEX). Note that custom applications built using Visual Builder Cloud Service do not count against the limit on external apps.
2 SaaS Extensions are custom-developed applications that are only used as extensions to subscribed Oracle SaaS applications such as HCM, ERP, SCM, and so on. The sole purpose of these applications is to augment Oracle SaaS apps. These do not count against the limit on external apps.
3 The right to use Oracle E-Business Suite Asserter also includes the right to use WebLogic Server Enterprise Edition solely for the purposes of running the asserter application in accordance with all terms and conditions as described in the [Oracle Fusion Middleware Licensing Information User Manual](https://docs.oracle.com/en/middleware/fusion-middleware/fmwlc/).
## IAM Identity Domain Object Limits 🔗 
Understand the number of different types of object allowed in each identity domain type.
You can create different identity domain types subject to the limit allowed by your subscription type. To find out the identity domain limits for each subscription type, see [IAM With Identity Domains Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#iam-service-limits).
This table shows the limits of the number of each type of object for each identity domain type.
Resource | Free | Oracle Apps | Oracle Apps Premium | Premium | External User  
---|---|---|---|---|---  
[Users](https://docs.oracle.com/en-us/iaas/Content/Identity/users/about-managing-users.htm#overview "Describes how to create and manage user accounts, including creating, updating, and deleting them.") | 2,000 | 1,000,000 | 1,000,000 | 1,000,000 | 100,000,000  
[Groups](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/managinggroups.htm#Managing_Groups) | 250 | 10,000 | 100,000 | 100,000 | 100,000  
[Users in a group](https://docs.oracle.com/en-us/iaas/Content/Identity/users/about-managing-users.htm#overview "Describes how to create and manage user accounts, including creating, updating, and deleting them.") | 2,000 | 10,000 | 100,000 | 100,000 | 100,000  
[Groups per user](https://docs.oracle.com/en-us/iaas/Content/Identity/groups/managinggroups.htm#Managing_Groups) | 250 | 500 | 5,000 | 5,000 | 5,000  
[Default password and group-based password policies](https://docs.oracle.com/en-us/iaas/Content/Identity/passwordpolicies/Managing-Password-Policies.htm#topic_g2w_wms_l4b "Create and manage group-based password policies for an identity domain in IAM.") | 10 | 10 | 10 | 10 | 10  
[Non Oracle apps](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/oracle-and-custom-applications.htm#oracle-and-custom-applications "Learn about using Oracle applications and custom applications in OCI.")[ 1](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits__footnote1) | 2 | 2[ 2](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits__footnote2) | 10[ 2](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits__footnote2) | 5,000 | 5,000  
[Oracle Cloud apps](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/oracle-and-custom-applications.htm#oracle-and-custom-applications "Learn about using Oracle applications and custom applications in OCI.") | 2,000 | 2,000 | 2,000 | 2,000 | -  
[Enterprise apps](https://docs.oracle.com/en-us/iaas/Content/Identity/applications/enterprise-applications.htm#enterprise-applications "Enterprise applications are web applications that require App Gateway to integrate with IAM for authentication and authorization purposes.") | - | - | 500 (Only Oracle enterprise apps) | 500 | 500  
[RADIUS proxy](https://docs.oracle.com/en-us/iaas/Content/Identity/radiusproxy/overview.htm#overview "Remote Authentication Dial In User Service \(RADIUS\) is a network protocol that defines rules and conventions for communication between network devices. RADIUS Proxy authenticates and authorizes users or devices and also tracks the usage of those services.") | - | - | 50 | 50 | -  
[Active Directory (AD) domains](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/microsoft-active-directory-ad-bridge1.htm#microsoft-active-directory-ad-bridge1 "The Microsoft Active Directory \(AD\) bridge provides a link between a Microsoft Active Directory enterprise directory structure and IAM.") | 2 | 10 | 20 | 20 | -  
[Active domain bridges per AD domain](https://docs.oracle.com/en-us/iaas/Content/Identity/msadbridge/microsoft-active-directory-ad-bridge1.htm#microsoft-active-directory-ad-bridge1 "The Microsoft Active Directory \(AD\) bridge provides a link between a Microsoft Active Directory enterprise directory structure and IAM.") | 4 | 10 | 10 | 10 | -  
[Provisioning bridges](https://docs.oracle.com/en-us/iaas/Content/Identity/provisioningbridges/managing-provisioning-bridge.htm#understand-provisioning-bridge "The provisioning bridge provides a link between your on-premises apps and IAM. Through synchronization, account data that's created and updated directly on the apps is pulled into an identity domain and stored for the corresponding identity domain users and groups. As a result, any changes to these records are transferred into an identity domain. So, if a user is deleted in one of your apps, then this change is propagated into the identity domain. Because of this, the state of each record is synchronized between your apps and the identity domain.") | 4 | 10 | 10 | 10 | -  
[Application Gateway](https://docs.oracle.com/en-us/iaas/Content/Identity/appgateways/understand-app-gateway.htm#understand-administrator-roles "App Gateway is a software appliance that lets you integrate applications hosted either on a compute instance, in a cloud infrastructure, or in an on-premises server with IAM for authentication purposes.") | - | - | 20 | 20 | 20  
[External Identity Providers and Social Login (IdPs)](https://docs.oracle.com/en-us/iaas/Content/Identity/identityproviders/manage-identity-providers.htm#manage-identity-providers "You can set up federated login between an identity domain and external identity provider. This allows users to sign in and access Oracle Cloud Infrastructure resources by using existing logins and passwords managed by the identity provider.")_(Federation / inbound SSO)_ | 5 | 5 | 30 | 30 | 30  
[IdP policies](https://docs.oracle.com/en-us/iaas/Content/Identity/idppolicies/manage-idp-policies.htm#manage-idp-policies "Learn how identity provider policies let you define which identity providers are visible in the Sign In page.") | 5 | 50 | 100 | 100 | 100  
[Terms of use](https://docs.oracle.com/en-us/iaas/Content/Identity/termsofuse/manage-terms-use.htm#manage-terms-use "This feature lets you present disclaimers and acceptable use policies, also known as terms of use, to users in an identity domain. You can configure terms of use for each application and collect consent from users before allowing them to access the application.") | 500 | 500 | 500 | 500 | 500  
[Sign in policies](https://docs.oracle.com/en-us/iaas/Content/Identity/signonpolicies/managingsignonpolicies.htm#Managing_signonpolicies) | 5 | 50 | 200 | 200 | 200  
[Self-registration profiles](https://docs.oracle.com/en-us/iaas/Content/Identity/selfregistrationprofiles/overview.htm#understand-self-registration-profiles "Use self-registration profiles to create accounts in a verified or unverified state. Customize the self-registration process by specifying the user's email domains allowed when self-registering, and adding header, footer, success, and user consent text.") | - | 50 | 50 | 50 | 50  
[Dynamic groups](https://docs.oracle.com/en-us/iaas/Content/Identity/dynamicgroups/managingdynamicgroups.htm#Managing_Dynamic_Groups) | 50 | 50 | 50 | 50 | -  
[API key per user](https://docs.oracle.com/en-us/iaas/Content/Identity/access/managing-user-credentials.htm#managing_credentials "Learn how users can manage their own credentials and what administrators can do with various types of user credentials for other users.") | 3 | 3 | 3 | 3 | -  
[Auth token per user](https://docs.oracle.com/en-us/iaas/Content/Identity/access/managing-user-credentials.htm#managing_credentials "Learn how users can manage their own credentials and what administrators can do with various types of user credentials for other users.") | 2 | 2 | 2 | 2 | -  
[OAuth2 client credentials per user](https://docs.oracle.com/en-us/iaas/Content/Identity/access/managing-user-credentials.htm#managing_credentials "Learn how users can manage their own credentials and what administrators can do with various types of user credentials for other users.") | 10 | 10 | 10 | 10 | -  
[SMTP credentials](https://docs.oracle.com/en-us/iaas/Content/Identity/access/managing-user-credentials.htm#managing_credentials "Learn how users can manage their own credentials and what administrators can do with various types of user credentials for other users.") | 2 | 2 | 2 | 2 | -  
[Customer secret key per user](https://docs.oracle.com/en-us/iaas/Content/Identity/access/managing-user-credentials.htm#managing_credentials "Learn how users can manage their own credentials and what administrators can do with various types of user credentials for other users.") | 2 | 2 | 2 | 2 | -  
[DB credentials per user](https://docs.oracle.com/en-us/iaas/Content/Identity/access/managing-user-credentials.htm#managing_credentials "Learn how users can manage their own credentials and what administrators can do with various types of user credentials for other users.") | 2 | 2 | 2 | 2 | -  
OAuth Client Certificate | 20 | 200 | 200 | 20,000 | 20,000  
OAuth Partner Certificates | 20 | 20 | 100 | 100 | 100  
Trusted Partner Certificates | 20 | 20 | 100 | 100 | 100  
1 Non Oracle or third-party apps are defined as either commercial applications offered by a provider other than Oracle or as custom-developed applications (including, for example, applications built on OCI using APEX). Note that custom applications built using Visual Builder Cloud Service do not count against the limit on external apps.
2 The limits for the number of non Oracle or third-party apps for the domain types Oracle Apps and Oracle Apps Premium are temporarily not enforced. They will be enforced in future.
## Data Types for Custom Attributes 🔗 
See the supported data types for custom attributes and their limits. These apply to all identity domain types.
Data Type |  Limit  
---|---  
4K char String Indexed (searchable) | 84  
40 char String Indexed (searchable) | 5  
4K char String Unindexed | 36  
40 char String Unindexed | 15  
Integer | 20  
## API Rate Limits 🔗 
Understand the rate limiting for APIs for different identity domain types.
Oracle APIs are subject to rate limiting to protect the API service usage for all Oracle's customers. If you reach the API limit for the identity domain type, then IAM returns a 429 error code.
### Rate Limits for all Identity Domain Types 🔗 
API Group | Per |  Free | Oracle Apps | Oracle Apps Premium | Premium | External User  
---|---|---|---|---|---|---  
**AuthN** | second | 10 | 50 | 80 | 95 | 90  
**AuthN** | minute | 150 | 1000 | 2100 | 4500 | 3100  
**Token Mgmt** | second | 10 | 40 | 50 | 65 | 60  
**Token Mgmt** | minute | 150 | 1000 | 1700 | 3400 | 2300  
**Others** | second | 20 | 50 | 55 | 90 | 80  
**Others** | minute | 150 | 1500 | 1750 | 5000 | 4000  
**Bulk** | second | 5 | 5 | 5 | 5 | 5  
**Bulk** | minute | 200 | 200 | 200 | 200 | 200  
**Import and export** | day | 4 | 8 | 10 | 10 | 10  
### APIs in API Groups 🔗 
API limits apply to the total of all APIs within a group.
[Authentication](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm)
  * `/sso/v1/user/login`
  * `/sso/v1/user/secure/login`
  * `/sso/v1/user/logout`
  * `/sso/v1/sdk/authenticate`
  * `/sso/v1/sdk/session`
  * `/sso/v1/sdk/idp`
  * `/sso/v1/sdk/secure/session`
  * `/mfa/v1/requests`
  * `/mfa/v1/users/{userguid}/factors`
  * `/oauth2/v1/authorize`
  * `/oauth2/v1/userlogout`
  * `/oauth2/v1/consent`
  * `/fed/v1/user/request/login`
  * `/fed/v1/sp/sso`
  * `/fed/v1/idp/sso`
  * `/fed/v1/idp/usernametoken`
  * `/fed/v1/metadata`
  * `/fed/v1/mex`
  * `/fed/v1/sp/slo`
  * `/fed/v1/sp/initiatesso`
  * `/fed/v1/sp/ssomtls`
  * `/fed/v1/idp/slo`
  * `/fed/v1/idp/initiatesso`
  * `/fed/v1/idp/wsfed`
  * `/fed/v1/idp/wsfedsignoutreturn`
  * `/fed/v1/user/response/login`
  * `/fed/v1/user/request/logout`
  * `/fed/v1/user/response/logout`
  * `/fed/v1/user/testspstart`
  * `/fed/v1/user/testspresult`
  * `/admin/v1/SigningCert/jwk`
  * `/admin/v1/HTTPAuthenticator`
  * `/admin/v1/PasswordAuthenticator`
  * `/admin/v1/Asserter`
  * `/admin/v1/MyAuthenticationFactorInitiator`
  * `/admin/v1/MyAuthenticationFactorEnroller`
  * `/admin/v1/MyAuthenticationFactorValidator`
  * `/admin/v1/MyAuthenticationFactorsRemover`
  * `/admin/v1/TermsOfUseConsent`
  * `/admin/v1/MyTermsOfUseConsent`
  * `/admin/v1/TrustedUserAgents`
  * `/admin/v1/AuthenticationFactorInitiator`
  * `/admin/v1/AuthenticationFactorEnroller`
  * `/admin/v1/AuthenticationFactorValidator`
  * `/admin/v1/MePasswordResetter`
  * `/admin/v1/UserPasswordChanger`
  * `/admin/v1/UserLockedStateChanger`
  * `/admin/v1/AuthenticationFactorsRemover`
  * `/admin/v1/BypassCodes`
  * `/admin/v1/MyBypassCodes`
  * `/admin/v1/MyTrustedUserAgents`
  * `/admin/v1/Devices`
  * `/admin/v1/MyDevices`
  * `/admin/v1/TermsOfUses`
  * `/admin/v1/TermsOfUseStatements`
  * `/admin/v1/AuthenticationFactorSettings`
  * `/admin/v1/SsoSettings`
  * `/admin/v1/AdaptiveAccessSettings`
  * `/admin/v1/RiskProviderProfiles`
  * `/admin/v1/Threats`
  * `/admin/v1/UserDevices`
  * `/session/v1/SessionsLogoutValidator`
  * `/ui/v1/signin`


[Tokens](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm)
  * `/oauth2/v1/token`
  * `/oauth2/v1/introspect`
  * `/oauth2/v1/revoke`
  * `/oauth2/v1/device`


[Import/Export](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm)
  * `/job/v1/JobSchedules?jobType=UserImport`
  * `/job/v1/JobSchedules?jobType=UserExport`
  * `/job/v1/JobSchedules?jobType=GroupImport`
  * `/job/v1/JobSchedules?jobType=GroupExport`
  * `/job/v1/JobSchedules?jobType=AppRoleImport`
  * `/job/v1/JobSchedules?jobType=AppRoleExport`


[Bulk](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm)
  * `/admin/v1/Bulk`
  * `/admin/v1/BulkUserPasswordChanger`
  * `/admin/v1/BulkUserPasswordResetter`
  * `/admin/v1/BulkSourceEvents`


[Other](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm)
Any API not in one of the other API Groups is included in the Other API Group
### Other Restrictions 🔗 
These restrictions are for Bulk, Import, and Export for all tiers:
  * Payload size: 1 MB
  * Bulk API: 50 operations limit per call
  * Only one of these can be run at a time: 
    * Import: For Users, Groups & App Role Memberships
    * Full sync from apps
    * Bulk APIs
    * Export: For Users, Groups & App Role Memberships
  * CSV Import: 100 K rows limit per CSV & Max file size: 10 MB
  * CSV Export: 100 K rows limit


## Meters for Identity Domain Types 🔗 
Understand the meters used for different identity domain types.
Free and Oracle Apps identity domain types do not use meters.
Oracle Apps Premium, Premium, and External User identity domain types use these meters:
  * **Users per Month:** The number of active and inactive users in the system, reported per hour. These meters are aggregated at the end of the billing cycle.
  * **SMS:** The number of SMS messages sent from the system, reported every hour. These meters are aggregated at the end of the billing cycle.
  * **Tokens:** The number of tokens issued by the system, reported every hour.
  * **Replicated Users per Month:** If you configure replication to more regions, this meter applies to the number of active and inactive users in each replicated region, reported per hour. These meters are aggregated at the end of the billing cycle.


After you have provisioned your service, Oracle Cloud Infrastructure has tools to help you analyze and understand the costs associated with your account. See [Checking Your Expenses and Usage](https://docs.oracle.com/iaas/Content/Billing/Concepts/costs.htm).
## Changing your Identity Domain Type 🔗 
When you change the identity domain type, IAM validates the change you are making.
  1. You cannot change the default domain to External User identity domain type.
  2. Your subscription type controls the number of identity domains of each type. If the change would exceed the number of identity domains of that type for your subscription type, you cannot change to the new identity domain type. See [IAM With Identity Domains Limits](https://docs.oracle.com/en-us/iaas/Content/General/Concepts/servicelimits.htm#iam-service-limits).
  3. If the number of objects of any type in your identity domain is higher than is allowed in the target identity domain type, you cannot change to the new identity domain type. See [IAM Identity Domain Object Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#iam-object-limits).
  4. The features available in your current identity domain type are checked. See [Feature Availability for Identity Domain Types](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/overview.htm#features). A warning message appears reminding you to exercise caution when changing from one identity domain type to another. You can proceed after the warning message, but some of your existing features might no longer work.
  5. You cannot change a Free, Premium, or External User identity domain to an Oracle Apps identity domain.


Was this article helpful?
YesNo

