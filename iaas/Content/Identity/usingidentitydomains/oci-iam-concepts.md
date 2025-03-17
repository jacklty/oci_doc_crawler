Updated 2023-01-04
# IAM Technologies
Get introduced to some concepts you'll come across when you work with IAM with identity domains.
## Oracle Cloud Services 🔗 
Learn about Software as a Service (SaaS), Data as a Service (DaaS), Platform as a Service (PaaS), and Infrastructure as a Service (IaaS) services used in Oracle Cloud.
Oracle Cloud offers a host of cloud services.
Application services are classified into two categories:
  * Software as a Service (SaaS): Provides a software licensing and delivery model in which software is licensed on a subscription basis and is centrally hosted.
  * Data as a Service (DaaS): Provides data on demand to a user regardless of geographic or organizational separation of the provider and consumer.


Platform services are also classified into two categories:
  * Platform as a Service (PaaS): Provides a platform allowing customers to develop, run, and manage applications without the complexity of building and maintaining the infrastructure typically associated with developing and deploying an application.
  * Infrastructure as a Service (IaaS): Provides access to computing resources (that is, virtualized hardware and computing infrastructure) in Oracle Cloud across a public connection.


For a comprehensive list of the available Oracle Cloud SaaS, DaaS, PaaS, and IaaS services, go to <https://www.oracle.com/cloud> and from the **Oracle Cloud** menu, select that category of services that interests you. From the page that opens, you can find links to detailed information about each service.
Oracle Cloud securely integrates its different cloud services, customer applications, and cloud services from other vendors. For example; this integration lets you, 
  * Embed Oracle Sales Cloud within your own application running on Oracle Java Cloud Service - SaaS Extension.
  * Extend Oracle Fusion Customer Relationship Management Cloud Service with a custom application.
  * Tie together an Oracle Cloud service with functionality from other sites, such as Salesforce. 
  * Use an Oracle Cloud service as the infrastructure for building your own applications.


## SAML, OAuth, and OpenID Connect 🔗 
Learn about the basic concepts behind the SAML, OAuth, and OpenID Connect standards used in IAM.
Security Assertion Markup Language (SAML) supports both authentication and authorization and is an open framework for sharing security information on the internet through XML documents. SAML includes three parts:
  * SAML Assertion: How you define authentication and authorization information.
  * SAML Protocol: How you ask (SAML Request) and get (SAML Response) the assertions you need.
  * SAML Bindings and Profiles: How SAML assertions ride _on_ (Bindings) and _in_ (Profiles) industry-standard transport and messaging frameworks. 


The OAuth 2.0 token service provided by the Oracle Cloud identity infrastructure provides secure access to the Representational State Transfer (REST) endpoints of cloud services by other cloud services and user applications. 
OAuth 2.0 provides the following benefits:
  * It increases security by eliminating the use of passwords in service-to-service REST interactions.
  * It reduces the lifecycle costs by centralizing trust management between clients and servers. OAuth reduces the number of configuration steps to secure service-to-service communication.


IAM leverages the power of OpenID Connect and OAuth to deliver a highly-scalable, multi-tenant token service for securing programmatic access to custom applications by other custom applications, and for federated SSO and authorization integration with these applications:
  * Use OAuth 2.0 to define authorization in IAM for your custom applications. OAuth 2.0 has an authorization framework, commonly used for third-party authorization requests with consent. Custom applications can implement both two-legged and three-legged OAuth flows.
  * Use OpenID Connect to externalize authentication to IAM for your custom applications. OpenID Connect has an authentication protocol that provides Federated SSO, leveraging the OAuth 2.0 authorization framework as a way to federate identities in the cloud. Custom applications participate in an OpenID Connect flow.


Using the OAuth 2.0 and OpenID Connect standards provides the following benefits:
  * Federated SSO between the custom application and IAM. Resource owners (users accessing the custom application) need a single login to access IAM plus all applications integrated. IAM handles the authentication and credentials itself, insulating custom applications. This capability is provided by OpenID Connect with OAuth 2.0.
  * Authorization to perform operations on third-party servers with consent. Resource owners can decide at runtime whether the custom applications should have authorization to access data or perform tasks for them. This capability is provided by OAuth 2.0.


## SCIM 🔗 
Learn about the basic concepts behind the SCIM standard used in IAM.
With REST APIs, you can use a System for Cross-Domain Identity Management (SCIM) to securely manage your IAM resources, including identities and configuration data. These APIs provide an alternative to using the web-based user interface when you want to use Identity Domains for your own UI or for clients.
You can manage users, groups, and applications, perform identity functions and administrative tasks, and manage your identity domain settings.
IAM provides SCIM templates to help you integrate your applications for provisioning and synchronization.
Was this article helpful?
YesNo

