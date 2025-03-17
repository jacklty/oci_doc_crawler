Updated 2024-09-03
# Using Implicit Access for Default Domains
OCI creates an automatic break glass workflow for default domains. This prevents users from being locked out of the system when a sign-on policy or an identity provider (IdP) policy isn't correctly configured.
## Sign-On Policy
To minimize the risk of the default identity domain's administrator of being locked out, the system creates an implicit break glass workflow. This workflow is created when the following conditions apply:
  * The user accessing the Console is an administrator.
  * The user is accessing the default domain.
  * No specific deny statement exists in the applicable sign-in policy for the Console.


**Note** We recommend the default domain administrators use multi-factor authentication.
**Example** :
This scenario uses the following users, admin1, admin2, admin3, and user1.
**Requirements:**
  * All users are members of the Default domain.
  * The sign-on policy is configured with the following rules in the same order. 
**Note** The admin3 user is a member of group1.
    * Rule 1: `Allow all administrators access except exclude the admin2`.
    * Rule 2: `Allow all users who are members of group group1 access`.


**Results** :
  * admin1: Access allowed. None of the sign-on rule matches, no explicit deny, administrator and accessing default domain.
  * admin2: Access denied. The user admin2 is explicitly denied access in Rule 1.
  * admin3: Access allowed. The admin3 user is an administrator and a member of group1.
  * user1: Access denied. The user user1 doesn't match any rules.


**Note**
Implicit break glass workflows only apply to the default domain.
## Identity Provider Policy
The system triggers an implicit break glass workflow for Console access when the identity provider rule of identity provider policy is configured with only one SAML or SOCIAL (OIDC) identity provider. In such cases, the system always shows the Console sign in page instead of redirecting user to a remote federation partner, when accessing Default domain of Console.
**Note** This only applies to only the Default domain.
Was this article helpful?
YesNo

