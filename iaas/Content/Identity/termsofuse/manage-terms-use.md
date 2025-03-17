Updated 2024-09-26
# Managing Terms of Use Documents
This feature lets you present disclaimers and acceptable use policies, also known as _terms of use_ , to users in an identity domain. You can configure terms of use for each application and collect consent from users before allowing them to access the application.
## Required Policy or Role
To manage terms of use settings, you must have one of the following access grants:
  * Be a member of the Administrators group
  * Be granted the Identity Domain Administrator role or the Security Administrator role
  * Be a member of a group granted `manage identity-domains`


To understand more about policies and roles, see [The Administrators Group, Policy, and Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/getstarted/identity-domains.htm#The), [Understanding Administrator Roles](https://docs.oracle.com/en-us/iaas/Content/Identity/roles/understand-administrator-roles.htm#understand-administrator-roles "Learn about administrator roles and the privileges associated with each role so that you can delegate administrative tasks to other users, as needed."), and [IAM Policies Overview](https://docs.oracle.com/en-us/iaas/Content/Identity/policieshow/Policy_Basics.htm#top "IAM policies govern control of resources in Oracle Cloud Infrastructure \(OCI\) tenancies.").
## About Terms of Use Documents 🔗 
About terms of use documents.
The terms of use feature enables you to set the terms and conditions to access the Console or a target application, based on the user's consent. This feature allows the identity domain administrator to set relevant disclaimers for legal or compliance requirements and enforce the terms by refusing the service unless consent is received.
In an identity domain, you can optionally grant or deny access to applications based on the consent provided by the user. When the user logs in for the first time, the disclaimers for legal or compliance requirements are displayed. The user has the option of either consenting or denying consent. If the user does not provide consent by accepting the terms of use, they will not be allowed to access the application. 
When you create a terms of use, you add the customized content and language that you want to display and choose the applications that will use the terms. You can also set an expiration date for the consent to require users to provide consent again after a set period of time. 
When you add a terms of service to an identity domain, it is always added in the deactivated state.
Was this article helpful?
YesNo

