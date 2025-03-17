Updated 2023-05-25
# Managing Trusted Partner Certificates
Learn about trusted partners and trusted partner certificates.
A **trusted partner** is any application or organization, remote to IAM that communicates with IAM. They have the following characteristics:
  * IAM uses identity propagation to communicate with a trusted partner. During identity propagation, a front-end Oracle Identity Management product, such as Oracle Access Manager, challenges a user and authenticates the user's credentials.
  * After the user's identity is validated, a token is generated. This token is used in place of a password to prove that the user is who they claim to be. The asserted identity is then passed into the identity domain. Because the identity has already been established, the identity domain trusts that it's a valid user identity, and can use it, as required.
  * For example, an identity domain receives a user assertion from Oracle Access Manager. As a result, a user can use Oracle Access Manager to sign in to a portal associated with a trusted partner. This portal takes the user to the Home page of an order management system. The Home page displays the orders the user made from the order management system.
  * The first step in establishing a trusted partner is to determine the partner's role in the trust relationship. A trusted partner can be a source site (one that generates an SSO assertion) or a destination site (one that consumes an SSO assertion).
  * Trusted partners generate SSO assertions that IAM consumes.
  * To ensure that the assertions are transmitted to the identity domains securely, the information contained in the assertions is encrypted in X.509 digital certificates. These certificates are known as **trusted partner certificates**.
  * Identity domains use trusted partner certificates that have Distinguished Encoding Rules (DER) file extensions.


You can perform the following tasks:
  * [Importing a Trusted Partner Certificate](https://docs.oracle.com/en-us/iaas/Content/Identity/trustedpartnercert/import-trusted-partner-certificate.htm#import-trusted-partner-certificate "Import a trusted partner certificate to an identity domain in IAM.")
  * [Viewing Details About a Trusted Partner Certificate](https://docs.oracle.com/en-us/iaas/Content/Identity/trustedpartnercert/view-details-trusted-partner-certificate.htm#view-details-trusted-partner-certificate "View details of a trusted partner certificate for an identity domain in IAM.")
  * [Deleting a Trusted Partner Certificate](https://docs.oracle.com/en-us/iaas/Content/Identity/trustedpartnercert/delete-trusted-partner-certificate.htm#delete-trusted-partner-certificate "Delete a trusted partner certificate from an identity domain in IAM.")


Was this article helpful?
YesNo

