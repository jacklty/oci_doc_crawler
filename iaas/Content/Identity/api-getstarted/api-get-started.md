Updated 2024-04-02
# Getting Started with the Identity Domains REST API
The identity domains REST API securely manage resources, including identities and configuration data. Support for OpenID Connect allows integration with compliant applications and identity domains. The OAuth2 service provides an API infrastructure for authorization that supports a range of token grant types that enable you to securely connect clients to services.
The identity domains REST API supports SCIM 2.0 compliant endpoints with standard SCIM 2.0 core schemas and Oracle schema extensions to:
  * Manage users, groups, and apps.
  * Perform identity functions, including password generation and reset.
  * Perform administrative tasks including bulk operations and job scheduling.
  * Configure settings for an identity domain including multifactor authentication, branding, and notification templates.


This guide contains the following sections: 
  * [Endpoints Deprecation Notices](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/DeprecatedEndpoints.htm "Read the endpoint deprecation notices for identity domains in IAM."): Learn about endpoints deprecation notices for identity domains.
  * [Quick Start](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/QuickStart.htm "Quickly get started with the identity domains REST API by completing prerequisites, installing curl, and setting up authorization to manage your identity domain resources such as users, groups, and applications."): Quickly get started with the identity domains REST API by completing prerequisites, installing curl, and setting up authorization to manage your identity domain resources such as users, groups, and applications. 
  * [API Rate Limits](https://docs.oracle.com/en-us/iaas/Content/Identity/sku/api-rate-limiting.htm "Understand the rate limiting for APIs for different identity domain types."): Understand the rate limiting for APIs for different identity domain types.
  * [Structuring Resource Requests](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/RequestResponse.htm#RequestResponse "Learn the guidelines for building send requests in an identity domain."): Learn the guidelines for building send requests in an identity domain.
  * [Using cURL](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/UsecURL.htm "cURL is an open source, command line tool for transferring data with URL syntax, supporting various protocols including HTTP and HTTPS. The examples within this document use cURL to demonstrate how to access the identity domains REST API."): Learn how to use cURL to access the REST APIs.
  * [Managing Authorization Using the API](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-managing-authorization.htm "The identity domains REST API supports both token-based authorization and OCI request signatures. For security reasons, the identity domains REST API isn't accessible using only the username and password that you use to sign in to the identity domain. To access the identity domains REST API, you need an OAuth2 access token or an API key to use for authorization."): Learn how to use an OAuth client to access identity domains REST API. The identity domains REST API isn't accessible using only an identity domain username and password. To access the identity domains REST API, you need an OAuth2 access token or an API key to use for authorization.
  * [API Use Cases](https://docs.oracle.com/en-us/iaas/Content/Identity/api-getstarted/api-use-cases.htm "Step through typical use cases using the IAM identity domain REST APIs."): Step through typical use cases using the identity domain REST APIs.


The following resources aren't in this guide but are also available to you. 
When using the identity domains user interface:
  * To administer IAM in tenancies with identity domains, see [Oracle Cloud Infrastructure Identity and Access Management](https://docs.oracle.com/en-us/iaas/Content/Identity/home.htm "Identity and Access Management \(IAM\) uses identity domains to provide identity and access management features such as authentication, single sign-on \(SSO\), and identity lifecycle management for Oracle Cloud as well as for Oracle and non-Oracle applications, whether SaaS, cloud hosted, or on premises.").
  * For user self-service instructions, such as setting up MFA, see the [IAM User Guide](https://docs.oracle.com/en-us/iaas/Content/Identity/using/aboutidentitydomains.htm "Your administrator gives you access to an identity domain. You use an identity domain to configure profile and security settings, manage 2-step verification for your account, generate bypass codes and to use the Oracle Mobile Authenticator \(OMA\) app.").


When using the API or CLI:
  * To manage identity domains (for example, creating or deleting a domain), see [IAM API](https://docs.oracle.com/iaas/api/#/en/identity/).
  * To manage resources within an identity domain, for example, users, dynamic resource groups, groups, and identity providers, see [Identity Domains CLI](https://docs.oracle.com/iaas/tools/oci-cli/latest/oci_cli_docs/cmdref/identity-domains.html).


Was this article helpful?
YesNo

