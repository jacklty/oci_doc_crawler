Updated 2025-02-05
# Federated Identity Providers
The Compute Cloud@Customer service uses the same federated identity provider that provides your identity services to Oracle Cloud Infrastructure. The identity provider manages usernames, passwords, and authentication to access the service.
Federation involves setting up a trust relationship between the identity provider and Oracle Cloud Infrastructure. When the administrator has established that relationship, any user who accesses the Compute Cloud@Customer console is prompted with a single sign-on experience offered by the identity provider. 
For more information, see [Federating with Identity Providers](https://docs.oracle.com/iaas/Content/Identity/Concepts/federation.htm).
## Identity Provider Administration 🔗 
Your federated identity provider is configured in the tenancy, and Oracle ensures that the same identity provider is configured in Compute Cloud@Customer during installation (see [Establish a Federated Identity Provider](https://docs.oracle.com/en-us/iaas/compute-cloud-at-customer/topics/site-prep/preparing-your-tenancy.htm#establish-a-federating-identity-provider "Before Compute Cloud@Customer is installed, your tenancy must be set up to use a federated identity provider to manage authentication.").) 
If you are federating with Oracle Identity Cloud Service, see [Federating with IDCS](https://docs.oracle.com/iaas/Content/Identity/Tasks/federatingIDCS.htm).
**Important**
If you change your identity provider configuration in Oracle Cloud Infrastructure, Oracle must make the same administrative changes on Compute Cloud@Customer. In this situation, open an Oracle Support Request to request help. See [Creating a Support Request](https://docs.oracle.com/iaas/Content/GSG/support/create-incident.htm).
Was this article helpful?
YesNo

