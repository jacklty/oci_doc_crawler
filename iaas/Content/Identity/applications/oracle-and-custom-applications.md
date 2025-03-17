Updated 2023-06-02
# Oracle and Custom Applications
Learn about using Oracle applications and custom applications in OCI.
**Oracle applications** are a complete and modular set of enterprise applications, engineered to be cloud-ready. In Oracle Cloud, you'll find a broad range of software as a service (SaaS), platform as a service (PaaS), and infrastructure as a service (IaaS) applications. You can use these applications as part of a subscription-based service; there's no software license or hardware to buy and manage. Oracle handles all the supporting underlying technologies.
You can extend Oracle applications or even build your own custom cloud applications in Oracle Cloud. **Custom applications** are applications (such as a mobile application, a web page, a client application, or a server application) that you can integrate with IAM. By default, for security purposes, custom applications are trusted or confidential.
IAM leverages the power of OpenID Connect and OAuth to deliver a highly-scalable, multi-tenant token service for securing programmatic access to custom applications by other custom applications, and for federated SSO and authorization integration with these applications:
  * Use OAuth 2.0 to define authorization in IAM for your custom applications. OAuth 2.0 has an authorization framework, commonly used for third-party authorization requests with consent. Custom applications can implement both two-legged and three-legged OAuth flows.
  * Use OpenID Connect to externalize authentication to IAM for your custom applications. OpenID Connect has an authentication protocol that provides Federated SSO, leveraging the OAuth 2.0 authorization framework as a way to federate identities in the cloud. Custom applications participate in an OpenID Connect flow.


Using the OAuth 2.0 and OpenID Connect standards provides the following benefits:
  * Federated SSO between the custom application and IAM. Resource owners (users accessing the custom application) need a single login to access IAM plus all applications integrated. IAM handles the authentication and credentials itself, insulating custom applications. This capability is provided by OpenID Connect with OAuth 2.0.
  * Authorization to perform operations on third-party servers with consent. Resource owners can decide at runtime whether the custom applications should have authorization to access data or perform tasks for them. This capability is provided by OAuth 2.0.


Was this article helpful?
YesNo

